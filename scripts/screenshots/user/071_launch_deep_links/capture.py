# /// script
# requires-python = ">=3.10"
# dependencies = ["playwright==1.61.0"]
# ///
"""Regenerate the launch deep-link documentation screenshots.

Credentials are required at runtime and are never written to disk. The script
captures only the notebook's <main> region, validates the documented states,
and replaces runtime identity and volatile UI text with demo values.
"""

from __future__ import annotations

import hashlib
import html
import json
import os
import re
import shutil
import tempfile
from pathlib import Path
from urllib.parse import urlencode, urlsplit
from uuid import uuid4

from playwright.sync_api import BrowserType, Locator, Page, sync_playwright

VIEWPORT = {"width": 1440, "height": 1000}
# px: tall enough for the demo result table, short enough to exclude the
# volatile follow-up composer rendered below it.
RESULT_CAPTURE_HEIGHT = 820
CONFIRM_LAUNCH_TEXT = "Confirm External Launch"
EXTERNAL_SOURCE = "https://external.example/"
DEMO_CASE = "CASE-DEMO-1042"
DEMO_SEVERITY = "high"
DEMO_DELIVERY = "Launch deep link"
DEMO_STATUS = "Completed"
CONFIRMATION_FILENAME = "071_launch_deep_link_confirmation.png"
RESULT_FILENAME = "071_launch_deep_link_result.png"


def required_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise SystemExit(f"Set {name} before running this script.")
    return value


def secure_base_url(raw_url: str) -> str:
    parsed = urlsplit(raw_url)
    if (
        parsed.scheme.lower() != "https"
        or not parsed.hostname
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise SystemExit(
            "LOUIE_SCREENSHOT_BASE_URL must be an HTTPS origin without "
            "userinfo, path, query, or fragment."
        )
    return f"https://{parsed.netloc}"


def launch_browser(chromium: BrowserType):
    kwargs: dict[str, object] = {"headless": True}
    certificate_spki = os.environ.get("LOUIE_SCREENSHOT_CERT_SPKI", "").strip()
    if certificate_spki:
        if not re.fullmatch(r"[A-Za-z0-9+/]{43}=", certificate_spki):
            raise SystemExit(
                "LOUIE_SCREENSHOT_CERT_SPKI must be one base64 SHA-256 SPKI pin."
            )
        kwargs["args"] = [f"--ignore-certificate-errors-spki-list={certificate_spki}"]
    return chromium.launch(**kwargs)


def resolve_consent_and_open_notebook(page: Page, base_url: str) -> None:
    consent = page.locator('input[name="allow"]')
    confirmation = page.get_by_text(CONFIRM_LAUNCH_TEXT, exact=True)
    consent.or_(confirmation).first.wait_for(timeout=60_000)
    if consent.is_visible():
        consent.click()
    page.wait_for_url(f"{base_url}/n/**", timeout=90_000)
    page.locator("main").wait_for(timeout=60_000)


def log_in_after_external_launch(
    page: Page,
    base_url: str,
    username: str,
    password: str,
) -> None:
    page.wait_for_url(f"{base_url}/login**", timeout=60_000)
    page.get_by_role("button", name="Continue with Graphistry").click()
    page.wait_for_url(re.compile(r"https://hub\.graphistry\.com/.*"), timeout=60_000)

    login_input = page.locator('input[name="login"]')
    consent = page.locator('input[name="allow"]')
    confirmation = page.get_by_text(CONFIRM_LAUNCH_TEXT, exact=True)
    login_input.or_(consent).or_(confirmation).first.wait_for(timeout=60_000)
    if login_input.is_visible():
        login_input.fill(username)
        page.locator('input[name="password"]').fill(password)
        page.locator('button[type="submit"]').click()

    resolve_consent_and_open_notebook(page, base_url)


def replace_visible_text(page: Page, replacements: dict[str, str]) -> None:
    main = page.locator("main")
    for source, replacement in replacements.items():
        if source:
            main.evaluate(
                """(root, values) => {
                  const [source, replacement] = values;
                  const walker = document.createTreeWalker(
                    root, NodeFilter.SHOW_TEXT
                  );
                  while (walker.nextNode()) {
                    walker.currentNode.nodeValue =
                      walker.currentNode.nodeValue.split(source).join(replacement);
                  }
                }""",
                [source, replacement],
            )


def sanitize_main(
    page: Page,
    *,
    username: str,
    base_url: str,
    extra_redactions: list[str],
) -> None:
    replace_visible_text(
        page,
        {
            username: "demo-user",
            base_url: "https://louie.example",
            **{value: "REDACTED" for value in extra_redactions},
        },
    )

    will_run_as = page.get_by_text(re.compile(r"^Will run as:")).first
    if will_run_as.count():
        will_run_as.evaluate(
            """node => {
              const row = node.parentElement ?? node;
              row.textContent =
                "Will run as: demo-user @ Example Organization";
            }"""
        )

    page.locator("main").evaluate(
        r"""root => {
          const replacements = [
            [/Run enabled in (?:\d+(?:\.\d+)?s|duration)/gi,
              "Run available after safety delay"],
            [/\bjust now\b/gi, "recently"],
            [/\b\d+(?:\.\d+)?s\b/g, "duration"],
            [/\b\d{1,2}:\d{2}\s*(?:AM|PM)\b/g, "time"],
            [/\bgpt-[\w.-]+\b/gi, "demo-model"],
            [/^\s*(?:low|medium|high|xhigh|max|ultra)\s*$/i,
              " demo-effort "]
          ];
          const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
          while (walker.nextNode()) {
            for (const [pattern, replacement] of replacements) {
              walker.currentNode.nodeValue =
                walker.currentNode.nodeValue.replace(pattern, replacement);
            }
          }
        }"""
    )


def assert_sanitized(page: Page, forbidden_values: list[str]) -> None:
    visible_text = page.locator("main").inner_text()
    for value in forbidden_values:
        if value and value in visible_text:
            raise AssertionError("A configured sensitive value remains visible.")
    if re.search(r"\borg_id=\d+\b", visible_text):
        raise AssertionError("An organization ID remains visible.")
    if re.search(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b", visible_text):
        raise AssertionError("An email address remains visible.")


def assert_named_params(page: Page, *, timeout: float = 30_000) -> None:
    """Prove the launch URL's typed named parameters are rendered verbatim.

    Called once before sanitization and again afterwards, so a redaction rule
    can never quietly rewrite the very values the screenshot is meant to show.
    """
    main = page.locator("main")
    named_params = main.get_by_text("named_params", exact=True)
    named_params.wait_for(timeout=timeout)

    parameter_group = named_params.locator(
        "xpath=ancestor::*["
        f"contains(normalize-space(.), '{DEMO_CASE}') and "
        f"contains(normalize-space(.), '{DEMO_SEVERITY}')"
        "][1]"
    )
    parameter_group.wait_for(timeout=timeout)
    if parameter_group.evaluate("node => node.tagName") == "MAIN":
        raise AssertionError("Named-parameter values are not scoped to their UI group.")
    parameter_text = " ".join(parameter_group.inner_text().split())
    object_start = parameter_text.find("{")
    object_end = parameter_text.rfind("}")
    if object_start < 0 or object_end <= object_start:
        raise AssertionError("Named-parameter group does not contain a JSON object.")
    named_values = json.loads(parameter_text[object_start : object_end + 1])
    expected_values = {"case_id": DEMO_CASE, "severity": DEMO_SEVERITY}
    if named_values != expected_values:
        raise AssertionError(
            f"Unexpected named-parameter values: {sorted(named_values)}"
        )


def assert_confirmation_state(page: Page) -> None:
    main = page.locator("main")
    main.get_by_text(CONFIRM_LAUNCH_TEXT, exact=True).wait_for(timeout=60_000)
    assert_named_params(page)

    checkbox = page.get_by_role("checkbox")
    run_button = page.get_by_role("button", name="Run", exact=True)
    if checkbox.is_checked():
        raise AssertionError("External-launch approval is already checked.")
    if run_button.is_enabled():
        raise AssertionError("Run is enabled before external-launch approval.")


def assert_result_state(page: Page) -> Locator:
    """Prove the approved run completed, and return the asserted result table."""
    main = page.locator("main")
    main.get_by_text("Completed", exact=True).last.wait_for(timeout=120_000)
    result_table = (
        main.locator("table")
        .filter(has_text=DEMO_DELIVERY)
        .filter(has_text=DEMO_STATUS)
        .last
    )
    result_table.wait_for(timeout=30_000)

    headers = [
        " ".join(text.split()) for text in result_table.locator("th").all_inner_texts()
    ]
    if headers != ["Field", "Value"]:
        raise AssertionError(f"Unexpected result-table headers: {headers}")
    rows = {
        " ".join(text.split())
        for text in result_table.locator("tbody tr").all_inner_texts()
    }
    expected_rows = {
        f"Delivery {DEMO_DELIVERY}",
        f"Status {DEMO_STATUS}",
    }
    if not expected_rows.issubset(rows):
        raise AssertionError(f"Result table is missing rows: {expected_rows - rows}")
    return result_table


def screenshot_result(page: Page, path: Path, result_table: Locator) -> None:
    """Capture the fixed result region above the volatile follow-up composer."""
    main_box = page.locator("main").bounding_box()
    if main_box is None:
        raise AssertionError("Cannot determine the stable result capture region.")
    capture_height = min(main_box["height"], RESULT_CAPTURE_HEIGHT)

    # The assertions above are DOM-based and pass regardless of where the table
    # renders, so prove the asserted table is actually inside the pixels we crop.
    # Sub-pixel layout floats: allow half a pixel so a table that is visibly
    # inside the crop cannot abort the run on a rounding edge.
    tolerance = 0.5
    table_box = result_table.bounding_box()
    if (
        table_box is None
        or table_box["y"] < main_box["y"] - tolerance
        or table_box["y"] + table_box["height"]
        > main_box["y"] + capture_height + tolerance
    ):
        raise AssertionError("Result table falls outside the fixed capture region.")

    page.screenshot(
        path=path,
        clip={
            "x": main_box["x"],
            "y": main_box["y"],
            "width": main_box["width"],
            "height": capture_height,
        },
    )


def publish_generation(temporary_path: Path, output_dir: Path) -> tuple[Path, Path]:
    """Publish both screenshots atomically, keyed by their content hash.

    Idempotent for identical content, swaps the `current` pointer only once
    the new generation is fully in place, garbage-collects stale
    generations, and leaves no partial directory behind on failure.
    """
    digest = hashlib.sha256()
    for filename in (CONFIRMATION_FILENAME, RESULT_FILENAME):
        digest.update(filename.encode())
        digest.update((temporary_path / filename).read_bytes())
    generation_name = f"generation-{digest.hexdigest()[:16]}"
    generation_path = output_dir / generation_name

    staging_path = output_dir / f".generation-{uuid4().hex}"
    temporary_path.replace(staging_path)
    try:
        if generation_path.exists():
            for filename in (CONFIRMATION_FILENAME, RESULT_FILENAME):
                existing = (generation_path / filename).read_bytes()
                candidate = (staging_path / filename).read_bytes()
                if existing != candidate:
                    raise RuntimeError(
                        f"{generation_name} already exists with different content "
                        f"(hash collision or stale state) — delete "
                        f"{generation_path} and rerun."
                    )
            shutil.rmtree(staging_path)
        else:
            # Raises if a concurrent run published this generation first.
            staging_path.replace(generation_path)
    except Exception:
        # Never leave a dot-prefixed staging directory in the docs asset tree:
        # `git add <dir>` would sweep it into a commit.
        shutil.rmtree(staging_path, ignore_errors=True)
        raise

    pointer_path = output_dir / "current"
    temporary_pointer = output_dir / f".current-{uuid4().hex}"
    try:
        temporary_pointer.symlink_to(generation_name, target_is_directory=True)
        temporary_pointer.replace(pointer_path)
    except Exception:
        temporary_pointer.unlink(missing_ok=True)
        raise

    for old_generation in output_dir.glob("generation-*"):
        if old_generation != generation_path and old_generation.is_dir():
            shutil.rmtree(old_generation)

    return (
        pointer_path / CONFIRMATION_FILENAME,
        pointer_path / RESULT_FILENAME,
    )


def capture() -> None:
    base_url = secure_base_url(required_env("LOUIE_SCREENSHOT_BASE_URL"))
    username = required_env("LOUIE_SCREENSHOT_USERNAME")
    password = required_env("LOUIE_SCREENSHOT_PASSWORD")
    extra_redactions = [
        value.strip()
        for value in os.environ.get("LOUIE_SCREENSHOT_REDACT_TEXT", "").split(",")
        if value.strip()
    ]
    forbidden_values = [username, password, base_url, *extra_redactions]
    output_dir = Path(
        os.environ.get(
            "LOUIE_SCREENSHOT_OUTPUT_DIR",
            "docs/source/user/images/user/071_launch_deep_links",
        )
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    prompt = (
        "Return a compact markdown table with columns Field and Value. "
        f"Use these rows: Delivery = {DEMO_DELIVERY}; "
        f"Status = {DEMO_STATUS}."
    )
    params = {
        "query": prompt,
        "agent": "LouieAgent",
        "execute": "true",
        "share_mode": "Private",
        "name": "Launch parameters in a live investigation",
        "param.case_id": DEMO_CASE,
        "param_type.case_id": "str",
        "param.severity": DEMO_SEVERITY,
        "param_type.severity": "str",
    }
    launch_url = f"{base_url}/web-api/launch/?{urlencode(params)}"

    temporary_path = Path(
        tempfile.mkdtemp(
            prefix=".launch-capture-",
            dir=output_dir,
        )
    )
    try:
        temporary_confirmation = temporary_path / CONFIRMATION_FILENAME
        temporary_result = temporary_path / RESULT_FILENAME

        with sync_playwright() as playwright:
            browser = launch_browser(playwright.chromium)
            try:
                context = browser.new_context(
                    viewport=VIEWPORT,
                    color_scheme="light",
                    reduced_motion="reduce",
                    locale="en-US",
                    timezone_id="UTC",
                )
                page = context.new_page()
                context.route(
                    f"{EXTERNAL_SOURCE}**",
                    lambda route: route.fulfill(
                        status=200,
                        content_type="text/html",
                        body=(
                            "<!doctype html><title>Example source system</title>"
                            f'<a href="{html.escape(launch_url)}">'
                            "Launch in Louie</a>"
                        ),
                    ),
                )
                page.goto(EXTERNAL_SOURCE, wait_until="domcontentloaded")
                page.get_by_role("link", name="Launch in Louie").click()
                log_in_after_external_launch(page, base_url, username, password)

                assert_confirmation_state(page)
                sanitize_main(
                    page,
                    username=username,
                    base_url=base_url,
                    extra_redactions=extra_redactions,
                )
                assert_sanitized(page, forbidden_values)
                # Prove no redaction rule rewrote the values this shot exists
                # to show (DEMO_SEVERITY collides with the effort-label rule).
                assert_named_params(page, timeout=5_000)
                page.locator("main").screenshot(path=temporary_confirmation)

                page.get_by_role("checkbox").check()
                page.get_by_role("button", name="Run", exact=True).click()
                page.get_by_text(CONFIRM_LAUNCH_TEXT, exact=True).wait_for(
                    state="hidden", timeout=60_000
                )
                page.get_by_text("Run complete", exact=False).last.wait_for(
                    timeout=120_000
                )
                assert_result_state(page)
                sanitize_main(
                    page,
                    username=username,
                    base_url=base_url,
                    extra_redactions=extra_redactions,
                )
                assert_sanitized(page, forbidden_values)
                # Re-assert after sanitization for the same reason, and use the
                # freshly asserted table to bound the capture region.
                result_table = assert_result_state(page)
                screenshot_result(page, temporary_result, result_table)
            finally:
                browser.close()

        confirmation_path, result_path = publish_generation(temporary_path, output_dir)
    finally:
        shutil.rmtree(temporary_path, ignore_errors=True)

    print(f"Wrote {confirmation_path}")
    print(f"Wrote {result_path}")


if __name__ == "__main__":
    capture()
