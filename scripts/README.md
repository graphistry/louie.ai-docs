# Documentation tooling

Maintainer scripts for this repository. Nothing here is published to the docs
site — these are run by hand when a guide's assets need refreshing.

## `capture_launch_deep_links.py`

Regenerates the two screenshots in
[Launch Deep Links](../docs/source/user/071_Launch_Deep_Links.md):

1. the external-launch confirmation gate, showing the typed named parameters
   and the not-yet-available Run action, and
2. the same link after approval, reaching `Completed` with its result table.

These are deliberately separate proof targets. The guide claims only what each
image shows, so both assertions must pass before either file is written.

The script pins the browser version, viewport, color scheme, locale, time zone,
demo inputs, and output filenames, and rewrites volatile UI text (durations,
timestamps, model labels) so consecutive runs are byte-comparable. It drives a
real cross-site click, completes login, asserts each documented state, and
re-asserts the named values *after* redaction so a sanitizer rule cannot quietly
rewrite the values the screenshot exists to prove.

### Running it

From the repository root:

```bash
read -rsp 'Disposable test-account password: ' LOUIE_CAPTURE_PASSWORD
echo
LOUIE_SCREENSHOT_BASE_URL='https://your-louie-host' \
LOUIE_SCREENSHOT_USERNAME='test-account' \
LOUIE_SCREENSHOT_PASSWORD="$LOUIE_CAPTURE_PASSWORD" \
LOUIE_SCREENSHOT_REDACT_TEXT='organization-name,account-email' \
  uv run scripts/capture_launch_deep_links.py
unset LOUIE_CAPTURE_PASSWORD
```

The password is read without echo and never reaches shell history. Inline
dependencies are declared in the script; install its matching browser once:

```bash
uv run --with playwright==1.61.0 playwright install chromium
```

| Variable | Purpose |
| --- | --- |
| `LOUIE_SCREENSHOT_BASE_URL` | Required. HTTPS origin only — the script rejects any other scheme, or a URL carrying userinfo, path, query, or fragment. |
| `LOUIE_SCREENSHOT_USERNAME` | Required. Use a disposable test account. |
| `LOUIE_SCREENSHOT_PASSWORD` | Required. Supply at runtime; never store it. |
| `LOUIE_SCREENSHOT_REDACT_TEXT` | Comma-separated extra strings to scrub, such as the organization name and account email. |
| `LOUIE_SCREENSHOT_CERT_SPKI` | Optional base64 SHA-256 SPKI pin, for a test host whose chain Chromium cannot validate. |
| `LOUIE_SCREENSHOT_OUTPUT_DIR` | Optional override; defaults to the guide's image directory. |

### TLS

Certificate verification stays on. If a non-production host presents a chain
Chromium cannot validate, obtain that host's base64 SHA-256 SPKI pin through a
trusted administrator channel and set `LOUIE_SCREENSHOT_CERT_SPKI` for that run
only. The pin grants a narrowly scoped exception for one public key; it does
**not** disable validation while credentials are sent to the identity provider.
Never commit a pin.

### Output layout

Images are published as an immutable `generation-<content-hash>/` directory
with a `current` symlink swapped atomically once both files are written:

```
docs/source/user/images/user/071_launch_deep_links/
├── current -> generation-<hash>
└── generation-<hash>/
    ├── 071_launch_deep_link_confirmation.png
    └── 071_launch_deep_link_result.png
```

The guide references the images through `current/`, so the two documented paths
can never come from different runs. Stale generations are removed on success,
and a failed run leaves nothing behind. Identical content republishes to the
same hash, so a no-op regeneration produces no diff.

### Before committing

Review both images by eye — a screenshot tool cannot tell you that a picture
looks wrong. Confirm no real hostname, account name, email, organization, or
other instance detail is visible, and keep credentials, cookies, browser state,
and certificate pins out of the repository.
