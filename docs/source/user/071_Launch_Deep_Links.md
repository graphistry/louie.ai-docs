# Launch Deep Links

**Without a launch deep link**, investigating something starts with retyping
whatever you were just looking at. You leave the dashboard, the alert, the
ticket, or the chat thread, open Louie, copy the details across by hand, and
ask the same questions you asked last time.

**With one**, you click instead. The link lives in the tool you were already
using and carries those details with it. Louie opens with them filled in and
the investigation already running, or staged and waiting if you would rather a
person press Run.

Reach for one when the same investigation keeps starting the same way and you
would rather click than retype. Anything that can build a URL can hand off to
Louie, and there is nothing to install on that side.

It works like this: you write a URL that says what to ask, which values to ask
about, and optionally which saved playbook to follow. Louie opens a thread,
starts the run, and lands the reader on results as they stream in.

## How it works

The browser launcher is:

```text
GET https://<louie-host>/web-api/launch/?query=<prompt>&agent=LouieAgent&execute=true
```

Louie redirects the browser to `/n/<thread-id>` while results stream. Use
`skills` to activate a saved playbook and `param.<key>` to add source-system
values to the launched investigation's named-value context.

## Launch parameters

| Parameter | Purpose |
| --- | --- |
| `query` | Required natural-language request. URL-encode it. Example: `query=Triage%20alert%20A-1042` |
| `agent` | Reasoning agent; defaults to `LouieAgent`. Example: `agent=LouieAgent` |
| `skills` | Comma-separated saved-skill keys. Example: `skills=incident-triage,host-enrichment` |
| `execute` | `true` (default) starts the run; `false` prepares a new thread without running it. Example: `execute=false` |
| `name` | DataThread title, such as the alert or ticket name. Example: `name=Notable%3A%20brute%20force` |
| `share_mode` | `Private` or `Organization`; defaults to `Private`. Example: `share_mode=Organization` |
| `org` | Organization id, slug, or name; defaults to the account's active organization. Naming a different organization is rejected with `403` rather than switching, even when the account is a member. Example: `org=soc-team` |
| `space` | `personal` or `shared`. An alternative way to set sharing when `share_mode` is omitted; supplying both with conflicting values is rejected with `400`. Example: `space=shared` |
| `dthread_id` | Target an existing DataThread. With `execute=true`, append and run a new cell. Example: `dthread_id=<existing-thread-id>` |
| `folder` | Target folder path. Example: `folder=Investigations/SOC` |
| `create_folders` | `true` creates missing folders in the `folder` path; `false` (default) fails when the folder does not exist. Example: `create_folders=true` |
| `param.<key>` | Named value added to the agent context. Keys must be valid identifiers. Example: `param.host=web-01` |
| `param_type.<key>` | Optional value type: `str`, `int`, `float`, `bool`, `relative_time`, or `json`. Defaults to `str`. Example: `param_type.host=str` |
| `timezone` | Time zone used to resolve `relative_time` values; defaults to UTC. Example: `timezone=America/New_York` |
| `options` | JSON object of per-request model and behavior overrides, URL-encoded. Example: `options=%7B...%7D` |

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
`POST /api/chat_singleshot/` batch API.

## Visual walkthrough

Both images below come from this exact link, opened from a site Louie does not
trust:

```text
https://louie.example/web-api/launch/?query=Return+a+compact+markdown+table+with+columns+Field+and+Value.+Use+these+rows%3A+Delivery+%3D+Launch+deep+link%3B+Status+%3D+Completed.&agent=LouieAgent&execute=true&share_mode=Private&name=Launch+parameters+in+a+live+investigation&param.case_id=CASE-DEMO-1042&param_type.case_id=str&param.severity=high&param_type.severity=str
```

Decoded, it asks for a two-row `Field`/`Value` table, names the thread
`Launch parameters in a live investigation`, and carries `case_id` and
`severity` as typed named values — each of which you can spot in the images.

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

## Splunk integration recipe

Splunk makes launch links especially useful because dashboard and alert tokens
can populate Louie's named-value context. This uses Louie's generic launcher;
dashboard and email links require no Splunk-side Louie app.

Save repeatable triage guidance as a skill such as `notable-triage`. Have
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
    https://louie.example/web-api/launch/?query=Triage%20the%20notable%20alert%20using%20the%20launch%20values%20host%2C%20src_ip%2C%20and%20earliest%3B%20correlate%20and%20summarize&amp;agent=LouieAgent&amp;skills=notable-triage&amp;execute=true&amp;share_mode=Organization&amp;name=Notable%3A%20$row.signature|u$&amp;param.host=$row.host|u$&amp;param_type.host=str&amp;param.src_ip=$row.src_ip|u$&amp;param_type.src_ip=str&amp;param.earliest=$earliest|u$&amp;param_type.earliest=str
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
https://louie.example/web-api/launch/?query=Investigate%20alert%20$name$%20using%20the%20launch%20values&agent=LouieAgent&skills=notable-triage&execute=true&param.host=$result.host$&param_type.host=str&param.src_ip=$result.src_ip$&param_type.src_ip=str
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
