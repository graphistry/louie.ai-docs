# Column Selection and Computed Columns

**All Columns**, at the bottom of the configuration panel, lists every column in
the chart's data. Columns are added to the chart by dragging them into **Group
By**, **Split By**, **Order By** or **Where**.

## Computed columns

**New Column** (the `fx` entry) creates a column from an expression over the
existing ones — a conversion rate from two counts, a bucketed value, a string
built from several fields.

A computed column behaves like any other afterwards: it can be grouped, split,
sorted, filtered and plotted.

## Filtering

**Where** restricts which rows reach the chart. It is the right place to narrow
a high-cardinality column before splitting on it.
