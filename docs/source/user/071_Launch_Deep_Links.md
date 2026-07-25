# Launch Deep Links

Use a URL to turn context from another application into a live Louie
investigation. A launch deep link can come from a dashboard, alert, ticket,
email, chat message, internal portal, or any other system that can render a
link.

The link can provide a prompt, select an agent or saved skill, and add named
values from the source system. Louie creates a DataThread, optionally starts
the run, and opens the investigation in the browser.

## How it works

The browser launcher is:

```text
GET https://<louie-host>/web-api/launch/?query=<prompt>&agent=LouieAgent&execute=true
```

Louie redirects the browser to `/n/<thread-id>` while results stream. Use
`skills` to activate a saved playbook and `param.<key>` to add source-system
values to the launched investigation's named-value context.

The previous browser launcher at `web/chat_singleshot` is obsolete; use
`/web-api/launch/` for browser deep links.

## Launch parameters

| Parameter | Purpose |
| --- | --- |
| `query` | Required natural-language request. URL-encode it. |
| `agent` | Reasoning agent; defaults to `LouieAgent`. |
| `skills` | Comma-separated saved-skill keys, such as `incident-triage`. |
| `execute` | `true` (default) starts the run; `false` prepares a new thread without running it. |
| `name` | DataThread title, for example an alert or ticket name. |
| `share_mode` | `Private` or `Organization`; defaults to `Private`. |
| `org` | Organization id, slug, or name; defaults to the account's active organization. Naming a different organization is rejected with `403` rather than switching, even when the account is a member. |
| `space` | `personal` or `shared`. An alternative way to set sharing when `share_mode` is omitted; supplying both with conflicting values is rejected with `400`. |
| `dthread_id` | Target an existing DataThread. With `execute=true`, append and run a new cell. |
| `folder` | Target folder path. |
| `create_folders` | `true` creates missing folders in the `folder` path; `false` (default) fails when the folder does not exist. |
| `param.<key>` | Named value added to the agent context. Keys must be valid identifiers. |
| `param_type.<key>` | Optional value type: `str`, `int`, `float`, `bool`, `relative_time`, or `json`. Defaults to `str`. |
| `timezone` | Time zone used to resolve `relative_time` values; defaults to UTC. |
| `options` | JSON object of per-request model and behavior overrides. |

`dthread_id` and `execute=false` do not stage a follow-up: Louie opens the
existing thread without appending the query or runnable named values. Requested
skills can still be activated. Use `execute=true` to append to an existing
thread, or omit `dthread_id` to create a prepared new thread.

`relative_time` accepts `now` or a negative integer followed by `s`, `m`, `h`,
`d`, or `w`, such as `-4h`. Use `str` for source-system time expressions outside
that grammar.

A `param_type.<key>` sent without a matching `param.<key>` is rejected with
`400`, so keep the two in step when a source system builds the URL
conditionally.

## Basic example

This link creates and immediately runs a private investigation:

```text
https://louie.example/web-api/launch/?query=Investigate%20case%20CASE-1042&agent=LouieAgent&execute=true&share_mode=Private&name=CASE-1042
```

When creating a new thread, set `execute=false` when the user should review or
extend the prepared investigation before running it.

## Templated flows with skills and named values

For a repeatable workflow, save the investigation playbook as a Louie skill and
pass changing values separately:

```text
https://louie.example/web-api/launch/?query=Investigate%20the%20incoming%20case%20using%20the%20launch%20values&skills=incident-triage&execute=true&name=CASE-1042&param.case_id=CASE-1042&param_type.case_id=str&param.window=-4h&param_type.window=relative_time
```

Louie registers `case_id` and `window` in the agent's named-value context. A
skill can instruct the agent to use those named values, and a tool input that
supports named-value resolution can accept a whole-value reference such as
`:case_id`.

Launch named values are not the same as a connector query's DAG macro
parameters. In particular, do not assume that `param.host=web-01` automatically
replaces an embedded `:host` inside raw SPL or SQL. If a playbook relies on raw
connector-query macros, bind and test those parameters through that playbook's
connector parameter mechanism.

Before depending on named values in a playbook, test the flow on the deployed
Louie version. Older deployments can display `param.*` values in the launch
confirmation without registering them in the agent context. That confirmation
proves receipt at the launch boundary, not downstream agent or connector
consumption.

Treat values from the source system as untrusted input. Keep them in data-value
positions; do not let them supply commands, field names, or query structure.
Escaping and native binding depend on the tool and connector configuration.

## Authentication and cross-origin launches

The simplest path is a user who is already signed in to Louie in the same
browser. Louie evaluates `execute=true` browser launches for cross-site request
safety. Administrators can configure trusted source sites with
`LOUIE_LAUNCH_ALLOWED_ORIGINS`.

Some configured connector hosts can also be derived as trusted launch origins.
By default, `LOUIE_LAUNCH_AUTODERIVE_FROM_CONNECTORS` includes Splunk and
Databricks.

If the originating site is not trusted—or a sign-in redirect prevents Louie
from verifying the source—Louie creates the investigation but requires the user
to confirm before it runs. A bearer JWT bypasses this browser-origin gate and is
appropriate for a server-to-server caller; obtain one through
`POST /api/auth/keypair` using a Graphistry Personal Key. Never put a JWT or
other credential in a deep-link URL.

## Programmatic alternative

Launch deep links are browser handoffs. For a source system that should invoke
Louie directly, use the authenticated `POST /api/chat/` streaming API or
`POST /api/chat_singleshot/` batch API. Despite the similar name,
`/api/chat_singleshot/` is current and unrelated to the obsolete
`web/chat_singleshot` browser launcher; browser deep links always go through
`/web-api/launch/`.

## Visual walkthrough

The first image verifies the security boundary for a browser launch whose
origin Louie could not verify: it pauses before auto-run, previews the prompt,
and shows the `case_id` and `severity` named values. The account identity in
the image is replaced with documented demo values. The dialog lists the
launch request's internal field names, so the `org` parameter appears there as
`org_selector`.

![External launch confirmation showing the prompt preview, named values, and disabled Run action before user approval](images/user/071_launch_deep_links/current/071_launch_deep_link_confirmation.png)

After approval, the same deep link runs in a private DataThread. The second
image verifies the separate execution transition: the run reaches `Completed`
and renders the table requested by the launch prompt. It does not claim that
the agent or a connector consumed the named values shown in the first image.

![Completed deep-link investigation showing the launched prompt and its result table](images/user/071_launch_deep_links/current/071_launch_deep_link_result.png)

### Regenerate the screenshots

The [capture script](../../../scripts/capture_launch_deep_links.py) fixes the
browser version, viewport, color scheme, locale, time zone, demo inputs, stable
UI text, and output filenames. It simulates a real cross-site click, completes
login, asserts the paused approval state and exact named-value rows, approves
the run, and asserts the completed prompt-result table. These are deliberately
separate proof targets. After the full workflow succeeds, the script publishes
an immutable generation and atomically switches the `current` pointer, so the
two documented paths never mix runs.

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

The password is read without echo and is not written into shell history. The
script also rejects non-HTTPS base URLs.

TLS certificate verification remains enabled. If a non-production test host
uses a certificate chain that Chromium cannot validate, obtain that host's
base64 SHA-256 SPKI pin through a trusted administrator channel and set it only
for this capture:

```bash
export LOUIE_SCREENSHOT_CERT_SPKI='base64-sha256-spki-pin'
```

The pin grants a narrowly scoped certificate exception for that exact public
key; it does not disable validation while credentials are sent to the identity
provider.

The script uses an exact inline Playwright version and its matching bundled
Chromium. Install that browser once:

```bash
uv run --with playwright==1.61.0 playwright install chromium
```

Use a disposable test account. Never put a real hostname, credentials, browser
state, cookies, tokens, certificate pins, or sensitive source data in the
repository. Regeneration creates a private test DataThread.

## Splunk integration recipe

Splunk makes launch links especially useful because dashboard and alert tokens
can populate Louie's named-value context. This uses Louie's generic launcher;
dashboard and email links require no Splunk-side Louie app.

Save repeatable triage guidance as a skill such as `dcso-notable-triage`. Have
the skill read named values such as `host`, `src_ip`, and `earliest`, validate
them as data, and use the configured Splunk connector to investigate and
summarize the alert. Do not put raw `:host` placeholders inside SPL unless the
playbook separately binds the connector's query parameters.

### Dashboard drilldown

Add a drilldown link to a Splunk Simple XML panel. Splunk substitutes its row
and time tokens when the analyst clicks it:

```xml
<drilldown>
  <link target="_blank">
    https://louie.dcso.example/web-api/launch/?query=Triage%20the%20notable%20alert%20using%20the%20launch%20values%20host%2C%20src_ip%2C%20and%20earliest%3B%20correlate%20and%20summarize&amp;agent=LouieAgent&amp;skills=dcso-notable-triage&amp;execute=true&amp;share_mode=Organization&amp;name=Notable%3A%20$row.signature|u$&amp;param.host=$row.host|u$&amp;param_type.host=str&amp;param.src_ip=$row.src_ip|u$&amp;param_type.src_ip=str&amp;param.earliest=$earliest|u$&amp;param_type.earliest=str
  </link>
</drilldown>
```

On click, the link opens a thread named for the alert signature, activates the
skill, and adds the host, source IP, and time window to the investigation.
Splunk's `|u` token filter URL-encodes dynamic values. The time token is a
`str`, because Splunk can emit snapped expressions such as `-24h@h` or absolute
epoch values that are outside Louie's narrower `relative_time` grammar.

See Splunk's
[dashboard token filters](https://help.splunk.com/en/splunk-cloud-platform/create-dashboards-and-reports/simple-xml-dashboards/9.2.2406/drilldown-and-dashboard-interactivity/token-usage-in-dashboards)
for version-specific details.

### Alert email link

The same pattern works in a saved-search alert. Use literal Splunk token
delimiters and result tokens in the email body:

```text
https://louie.dcso.example/web-api/launch/?query=Investigate%20alert%20$name$%20using%20the%20launch%20values&agent=LouieAgent&skills=dcso-notable-triage&execute=true&param.host=$result.host$&param_type.host=str&param.src_ip=$result.src_ip$&param_type.src_ip=str
```

Splunk recognizes `$name$` and `$result.<field>$` before the generated link is
opened; percent-encoding the `$` delimiters prevents that substitution. Ensure
the substituted alert values are URL-safe, or precompute URL-encoded result
fields before placing them in the URL.

This example omits `earliest`: an alert email has no per-click time-range token
equivalent to a dashboard's `$earliest$`, so let the skill choose its own
window when that named value is absent. See Splunk's
[email notification token reference](https://help.splunk.com/splunk-enterprise/alert-and-respond/alerting-manual/9.4/configure-alert-actions/use-tokens-in-email-notifications).

### Native webhook alerts

Splunk's native webhook action sends a fixed JSON envelope and cannot add the
bearer `Authorization` header or reshape its body for Louie's chat API. Point it
at an authenticated relay that validates and maps the Splunk payload, or use a
custom Splunk alert action that sends Louie's request shape and bearer header.
Do not put credentials in the destination URL. Splunk administrators must also
allowlist the webhook destination according to Splunk's
[webhook alert-action guidance](https://help.splunk.com/en/splunk-enterprise/alert-and-respond/alerting-manual/10.4/configure-alert-actions/use-a-webhook-alert-action).

## Setup checklist

1. Make the Louie host reachable from users' browsers.
2. Create a skill when the launch should follow a repeatable playbook.
3. Make the skill consume the launch named-value context; separately bind and
   test any raw connector-query macros it uses.
4. Choose browser-session authentication or a server-side Personal Key/JWT
   flow.
5. Trust the source origin if links from that system should auto-run.
6. URL-encode prompts and dynamic values, then test spaces and reserved
   characters.
7. For connector-backed flows such as Splunk, configure and index the connector
   and review its parameter-safety settings.
