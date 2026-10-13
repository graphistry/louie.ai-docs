# Database Tools

Each database connector contributes two agents: a **passthrough** one that runs
exactly the query you write, and an **AI** one that writes the query from a
plain-language request.

| Connector | Passthrough | AI |
|---|---|---|
| Splunk | `Splunk` | `Splunk AI` |
| Kusto | `Kusto` | `Kusto AI` |
| Spanner | `Spanner` | `Spanner AI` |
| MCP | — | `MCP AI` |

Which agents appear depends on what your organization has configured — a
connector type with no connector set up contributes none. See
[Data Connectors](connectors_overview.md).

## Choosing between them

Use the AI agent when you want the query written for you, or when you do not
know the schema well. Use the passthrough agent when you already have the query,
when it must run verbatim, or when you are reproducing an earlier result.

Both return their output as a named value, usable by later cells either way.

## Schema awareness

An agent can only query what Louie has indexed from the connector. When a table
or field you know exists cannot be found, re-index the connector — see
[Data Connectors](connectors_overview.md).
