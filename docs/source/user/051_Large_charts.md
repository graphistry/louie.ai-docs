# Large Charts

Charts render in the browser, so the limit is not how much data Louie can query
but how much the browser can hold and draw. A query that returns 100K+ rows can
be 100MB+ over the wire, and a chart configuration that looks harmless can
multiply that again.

Two pages cover this:

- [General](052_Large_charts__General.md) — what to do about query size and
  chart configuration
- [Specific charts](053_Large_charts__Specific_charts.md) — the limits that
  apply to UMAP, bar charts and Graphistry graphs

The short version: pull only the columns you need, start small and grow, and
switch chart types through Datagrid rather than directly.
