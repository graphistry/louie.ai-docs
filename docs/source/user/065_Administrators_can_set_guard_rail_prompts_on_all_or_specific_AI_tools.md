# Guard Rail Prompts

A **guard rail** is extra prompt text an administrator injects into an AI tool's
instructions. It applies to every run of that tool, for everyone.

## Scope

| Variable | Applies to |
|---|---|
| `GLOBAL_GUARD_RAILS` | every AI tool |
| `LOUIE_GUARD_RAILS` | the main conversational agent |
| `OVERRIDE_GUARD_RAILS` | replaces the rest rather than adding to them |
| `META_TOOL_GUARD_RAILS` | tool-selection decisions |

## Per-tool

**Analysis and visualization**

`CODE_GUARD_RAILS` · `GRAPH_GUARD_RAILS` · `GRAPH_EDGE_DECIDER_GUARD_RAILS` ·
`KEPLER_GUARD_RAILS` · `MERMAID_GUARD_RAILS` · `PERSPECTIVE_GUARD_RAILS` ·
`PERSPECTIVE_CHART_GUARD_RAILS` · `TABLEAI_GUARD_RAILS` ·
`EMERGENCY_ENRICHMENT_GUARD_RAILS`

**Databases and query engines**

`ATHENA_GUARD_RAILS` · `BIGQUERY_GUARD_RAILS` · `COCKROACHDB_GUARD_RAILS` ·
`KUSTO_GUARD_RAILS` · `MSSQL_GUARD_RAILS` · `MYSQL_GUARD_RAILS` ·
`NEPTUNE_CYPHER_GUARD_RAILS` · `OPENSEARCH_GUARD_RAILS` ·
`POSTGRES_GUARD_RAILS` · `SNOWFLAKE_GUARD_RAILS` · `SPANNER_GUARD_RAILS` ·
`SPARK_GUARD_RAILS` · `SPLUNK_GUARD_RAILS`

Several of these have a `_QUERY_` counterpart that applies to query generation
specifically rather than to the connector's agent as a whole:
`ATHENA_QUERY_GUARD_RAILS`, `BIGQUERY_QUERY_GUARD_RAILS`,
`COCKROACHDB_QUERY_GUARD_RAILS`, `MSSQL_QUERY_GUARD_RAILS`,
`MYSQL_QUERY_GUARD_RAILS`, `POSTGRES_QUERY_GUARD_RAILS`,
`SNOWFLAKE_QUERY_GUARD_RAILS`.

## Setting one

Guard rails are environment variables. Set them in the server's environment file
and restart `louie` and `api`:

```
GLOBAL_GUARD_RAILS='Use all caps'
```

The text is appended to the tool's instructions, so write it as an instruction
to the model, not as configuration.
