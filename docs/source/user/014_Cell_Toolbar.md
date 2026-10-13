# The Cell Toolbar

Every cell carries a toolbar for building up and rearranging a notebook.

## Adding cells

- **Add cell** — a new prompt cell, run by an agent of your choosing
- **Add markdown cell** — formatted notes, with no agent and no run step
- **Add input group cell** — parameters that later cells can read

## Rearranging and removing

**Move cell up** (Alt+Shift+Up), **Move cell down** (Alt+Shift+Down) and
**Delete cell** act on the current cell.

## Choosing how a cell runs

**Select agent** sets what the cell does when it runs. Agents come in two
kinds, and the picker separates them:

- **Passthrough** — your input goes straight to the tool, with no AI step:
  Chart, Graph, Kusto, Mermaid, Python, Spanner, Splunk, UMAP
- **AI agents** — an AI model interprets the request and drives the tool:
  Chart AI, Graph+UMAP AI, Kusto AI, Map, MCP AI, Mermaid AI, Notebook AI,
  Python AI, Spanner AI, Splunk AI, Table AI, Text AI

Use a passthrough agent when you already know the query or the code you want
to run; use an AI agent when you want it written for you.

![Agent picker, showing passthrough and AI agents](./images/user/014_agent_picker.png)

**Run cell** (⌘+Enter) runs the current cell.
