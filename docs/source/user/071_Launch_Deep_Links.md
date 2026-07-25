# Launch Deep Links

Use a URL to turn context from another application into a live Louie
investigation. A launch deep link can come from a dashboard, alert, ticket,
email, chat message, internal portal, or any other system that can render a
link.

The link can provide a prompt, select an agent or saved skill, and bind named
values from the source system. Louie creates a DataThread, optionally starts
the run, and opens the investigation in the browser.

## How it works

The browser launcher is:

```text
GET https://<louie-host>/web-api/launch/?query=<prompt>&agent=LouieAgent&execute=true
```

Louie redirects the browser to `/n/<thread-id>` while results stream. Use
`skills` to activate a saved playbook and `param.<name>` to bind source-system
values that the playbook references as `:<name>`.

The previous `web/chat_singleshot` launcher is obsolete. Use `/web-api/launch/`
for browser deep links.

## Launch parameters

| Parameter | Purpose |
| --- | --- |
| `query` | Required natural-language request. URL-encode it. |
| `agent` | Reasoning agent; defaults to `LouieAgent`. |
| `skills` | Comma-separated saved-skill keys, such as `incident-triage`. |
| `execute` | `true` (default) starts the run; `false` creates a prepared thread only. |
| `name` | DataThread title, for example an alert or ticket name. |
| `share_mode` | `Private` or `Organization`. |
| `dthread_id` | Append to an existing DataThread rather than create one. |
| `folder` | Target folder path. |
| `param.<key>` | Named value available to the playbook as `:<key>`. Keys must be valid identifiers. |
| `param_type.<key>` | Optional value type: `str`, `int`, `float`, `bool`, `relative_time`, or `json`. |
| `timezone` | Time zone for `relative_time` values; defaults to UTC. |

## Basic example

This link creates and immediately runs a private investigation:

```text
https://louie.example/web-api/launch/?query=Investigate%20case%20CASE-1042&agent=LouieAgent&execute=true&share_mode=Private&name=CASE-1042
```

Set `execute=false` when the user should review or extend the prepared
investigation before running it.

## Templated flows with skills and named parameters

For a repeatable workflow, save the investigation playbook as a Louie skill and
pass the changing values separately:

```text
https://louie.example/web-api/launch/?query=Investigate%20the%20incoming%20case&skills=incident-triage&execute=true&name=CASE-1042&param.case_id=CASE-1042&param_type.case_id=str&param.window=-4h&param_type.window=relative_time
```

The `incident-triage` skill can use `:case_id` and `:window` in compatible
connector queries. Match every placeholder name to its `param.*` key.

Treat values from the source system as untrusted input. Put them in complete
value positions; do not use them to supply query commands, field names, or
other query structure. Parameter escaping and native binding depend on the
connector and server configuration.

## Authentication and cross-origin launches

The simplest path is a user who is already signed in to Louie in the same
browser. Louie evaluates `execute=true` browser launches for cross-site request
safety. Administrators can configure trusted source sites with
`LOUIE_LAUNCH_ALLOWED_ORIGINS`.

Some configured connector hosts can also be derived as trusted launch origins.
By default, `LOUIE_LAUNCH_AUTODERIVE_FROM_CONNECTORS` includes Splunk and
Databricks.

If the originating site is not trusted, Louie creates a prepared investigation
and requires the user to confirm before it runs. A bearer JWT bypasses this
browser-origin gate and is appropriate for a server-to-server caller; obtain one
through `POST /api/auth/keypair` using a Graphistry Personal Key. Never put a
JWT or other credential in a deep-link URL.

## Programmatic alternative

Launch deep links are browser handoffs. For a source system that should invoke
Louie directly, use the authenticated `POST /api/chat/` streaming API or
`POST /api/chat_singleshot/` batch API instead.

## Splunk integration recipe

Splunk makes launch links especially useful because dashboard and alert tokens
can populate the named parameters. No Splunk-side Louie app is required: use a
normal drilldown or alert link.

First save the repeatable analysis as a skill such as
`dcso-notable-triage`. Its SPL can reference the incoming values:

```text
search index=notable host=":host" src_ip=":src_ip" earliest=":earliest"
| stats count by signature, dest, action
```

For shared or lower-trust workflows, administrators can enable
`MACRO_PARAM_ESCAPING` so Splunk string values are escaped. See
[Database Connector Configuration](../admin/020_Database_Config) for connector
setup.

### Dashboard drilldown

Add a drilldown link to a Splunk Simple XML panel. Splunk substitutes its row
and time tokens when the analyst clicks it.

```xml
<drilldown>
  <link target="_blank">
    https://louie.dcso.example/web-api/launch/?query=Triage%20notable%20alert%20on%20host%20%3Ahost%20from%20%3Asrc_ip%20in%20the%20last%20window%3B%20correlate%20and%20summarize&amp;agent=LouieAgent&amp;skills=dcso-notable-triage&amp;execute=true&amp;share_mode=Organization&amp;name=Notable%3A%20$row.signature$&amp;param.host=$row.host$&amp;param_type.host=str&amp;param.src_ip=$row.src_ip$&amp;param_type.src_ip=str&amp;param.earliest=$earliest$&amp;param_type.earliest=relative_time
  </link>
</drilldown>
```

On click, the link opens a thread named for the alert signature, activates the
skill, passes the host, source IP, and time window, and begins the investigation.
Depending on the Splunk configuration, use Splunk's URL-token encoding for
values that can contain reserved URL characters.

### Alert email or webhook link

The same pattern works in a saved-search alert. Use result tokens rather than
row tokens in the email body or webhook payload:

```text
https://louie.dcso.example/web-api/launch/?query=Investigate%20alert%20%24name%24&agent=LouieAgent&skills=dcso-notable-triage&execute=true&param.host=$result.host$&param_type.host=str&param.src_ip=$result.src_ip$&param_type.src_ip=str
```

Splunk substitutes `$result.host$` and the other result tokens when it creates
the alert. If a webhook should run Louie without a browser, use the programmatic
API instead of putting credentials in this URL.

## Setup checklist

1. Make the Louie host reachable from users' browsers.
2. Create a skill when the launch should follow a repeatable playbook.
3. Match skill placeholders to the `param.*` keys.
4. Choose browser-session authentication or a server-side Personal Key/JWT flow.
5. Trust the source origin if links from that system should auto-run.
6. URL-encode prompts and dynamic values, then test spaces and reserved
   characters.
7. For connector-backed flows such as Splunk, configure and index the connector
   and review its parameter-safety settings.
