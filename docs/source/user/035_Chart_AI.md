# Chart AI

**Chart AI** turns a plain-language request into a chart.

## Writing a good request

Name these four things and the result is usually right first time:

1. **Which dataframe** — by its variable name
2. **The chart type** — bar, line, scatter, heatmap
3. **Which columns** — what goes on each axis
4. **Any grouping** — one series per region, per month

For example:

> Chart `monthly_sales_dataframe` as a bar chart with Month on the x-axis and
> one bar per Region.

## After it runs

The chart is a Perspective chart, so anything the agent chose can be changed by
hand afterwards — chart type, grouping, sorting, filtering — without re-running
the cell. See [Perspective Charts](037_Perspective_charts.md).

If a chart comes out shaped oddly, that is usually the data's layout rather than
the request: a wide table with one column per series often needs reshaping to
long format first. Asking for that reshape in the same request works.
