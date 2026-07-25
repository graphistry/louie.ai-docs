# Splunk Alert Deep Links

Use a Splunk dashboard or alert to open a prepared Louie investigation with the
alert's fields already bound to a skill. Louie does not require a Splunk app for
this: Splunk renders a normal, tokenized URL and the analyst opens it in a
browser.

## How it works

The browser launcher is:

```
GET https://<louie-host>/web-api/launch/?query=<prompt>&agent=LouieAgent&execute=true
```

Louie creates a DataThread, optionally starts the run, and redirects the browser
to `/n/<thread-id>`. Use `skills` to activate a saved investigation playbook and
`param.<name>` to bind alert values that the playbook references as `:<name>`.

The previous `web/chat_singleshot` launcher is obsolete. Use `/web-api/launch/`
for browser deep links.

## Launch parameters

| Parameter | Purpose |
| --- | --- |
| `query` | Required natural-language request. URL-encode it. |
| `agent` | Reasoning agent; defaults to `LouieAgent`. |
| `skills` | Comma-separated saved-skill keys, such as `dcso-notable-triage`. |
| `execute` | `true` (default) starts the run; `false` creates a prepared thread only. |
| `name` | DataThread title, for example the alert name. |
| `share_mode` | `Private` or `Organization`. |
| `dthread_id` | Append to an existing DataThread rather than create one. |
| `folder` | Target folder path. |
| `param.<key>` | Named value available to the playbook as `:<key>`. Keys must be valid identifiers. |
| `param_type.<key>` | Optional value type: `str`, `int`, `float`, `bool`, `relative_time`, or `json`. |
| `timezone` | Time zone for `relative_time` values; defaults to UTC. |

## Build a repeatable triage skill

First save the investigation flow as a Louie skill. For example, a
`dcso-notable-triage` skill can query Splunk using named values:

```text
search index=notable host=":host" src_ip=":src_ip" earliest=":earliest"
| stats count by signature, dest, action
```

Match the `:host`, `:src_ip`, and `:earliest` names to the URL parameters.
Keep a parameter in a complete quoted value position as above. Alert data is
untrusted input; do not use it to supply SPL commands, field names, or other
query structure. For shared or lower-trust workflows, enable the administrator
setting `MACRO_PARAM_ESCAPING` so Splunk string values are escaped. See
[Database Connector Configuration](../admin/020_Database_Config) for connector setup.

## Dashboard drilldown example

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

## Alert email or webhook link

The same pattern works in a saved-search alert. Use result tokens rather than
row tokens in the email body or webhook payload:

```text
https://louie.dcso.example/web-api/launch/?query=Investigate%20alert%20%24name%24&agent=LouieAgent&skills=dcso-notable-triage&execute=true&param.host=$result.host$&param_type.host=str&param.src_ip=$result.src_ip$&param_type.src_ip=str
```

This is a browser handoff: an analyst follows the link and completes the
investigation in Louie. For a server-to-server alert action, use the authenticated
`POST /api/chat/` streaming API or `POST /api/chat_singleshot/` batch API instead.

## Authentication and cross-origin launches

The simplest path is an analyst who is already signed in to Louie in the same
browser. Louie evaluates `execute=true` browser launches for cross-site request
safety. By default, hosts from configured Splunk and Databricks connectors are
derived as trusted launch origins (`LOUIE_LAUNCH_AUTODERIVE_FROM_CONNECTORS`).
Administrators can also set `LOUIE_LAUNCH_ALLOWED_ORIGINS` explicitly.

If the originating site is not trusted, Louie creates a prepared investigation
and requires the analyst to confirm before it runs. A bearer JWT bypasses this
browser-origin gate and is appropriate for a server-to-server caller; obtain one
through `POST /api/auth/keypair` using a Graphistry Personal Key. Never put a
JWT or other credential in a deep-link URL.

## Setup checklist

1. Make the Louie host reachable from analysts' browsers.
2. Configure and index the Splunk connector in Louie.
3. Create a skill with parameter names matching the `param.*` keys.
4. Choose browser-session authentication or a server-side Personal Key/JWT flow.
5. Verify the Splunk host is derived or explicitly listed as an allowed launch
   origin if the dashboard should auto-run.
6. Test with representative alert values, including spaces and reserved URL
   characters.
