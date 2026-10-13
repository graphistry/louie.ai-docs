# Chart Types in Detail

All chart types are chosen the same way — see
[Switching Chart Type](039_Perspective__Chart_switching.md). What each one needs
differs.

## Datagrid

The data as a table, with Group By rendered as expandable rows. Useful for
checking the numbers behind a chart, and for sharing a result that is better
read than looked at.

## Bars

**Y Bar** draws vertical bars, **X Bar** horizontal. Both take a Group By for
the categories and one or more value columns for the bar heights. A Split By
adds a series per distinct value.

## Lines and areas

**Y Line** and **Y Area** suit an ordered category axis — a time series, or any
Group By with a meaningful order. Area fills beneath the line, which reads
better for a cumulative quantity than for one that moves up and down.

## Scatter

**Y Scatter** plots points against the category axis. **X/Y Scatter** plots two
value columns against each other, for a relationship between measures rather
than a measure over categories.

## Heatmap

A grid shaded by value, taking two grouping dimensions and one measure. Reads
density well where a bar chart would need too many bars.

## Sunburst

Nested proportions, one ring per Group By level. Suits a hierarchy where the
shares matter more than the exact values.

## Candlestick and OHLC

Both expect open, high, low and close columns. Candlestick draws filled bodies
with wicks; OHLC draws ticks. Neither renders usefully without all four.

## When a chart comes out empty

Most often the chart type needs more columns than are configured — a Candlestick
with three columns, or a Heatmap with one grouping dimension. Switch to Datagrid
to see what the chart is actually working with.
