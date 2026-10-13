# Running Non-AI Cells

A **passthrough agent** sends your input straight to the tool, with no AI step in
between. What you write is what runs.

## How to run one

1. Choose a passthrough agent with **Select agent** — they are grouped under **PASSTHROUGH**
2. Write the query or code in that tool's own syntax
3. Run the cell

## The passthrough agents

Chart · Graph · Kusto · Mermaid · Python · Spanner · Splunk · UMAP

Use these when you already know exactly what you want to run, when a query must
execute verbatim, or when you are reproducing a result and want no
interpretation in the way. Output lands in the notebook as a named value, usable
by later cells exactly like the output of an AI agent.
