# Downloading Chart Data

The data behind a chart can be exported without re-running anything.

## From the notebook

**Download table** beside a dataframe or chart downloads its data directly.

## From the chart

The chart's own toolbar has an **export** control, which offers:

- **CSV**
- **JSON**
- **Arrow**
- **HTML**

and can either save a file or copy to the clipboard.

What is exported is the data **as the chart is currently configured** — grouped,
filtered and sorted as you see it, not the original table. To export the
underlying data instead, switch the chart to **Datagrid** first, or use
**Download table** on the source dataframe.
