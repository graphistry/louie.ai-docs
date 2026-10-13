# Group By

**Group By** sets the category axis. Rows sharing the same value in the chosen
column collapse into one group, and the chart plots one mark per group.

Grouping by `Month` on a table of daily rows gives one bar per month.

Several columns can be grouped at once, producing a hierarchy — `Region` then
`Month` nests months inside regions. In a Datagrid the hierarchy appears as
expandable rows.

The aggregate applied to each group is chosen per column: **sum**, **avg**,
**count**, **distinct count**, **min**, **max**, **median**, **stddev** and
others are available from the column's own menu.

To break each group into series instead of nesting, use
[Split By](042_Perspective__Expressions___Split_By.md).
