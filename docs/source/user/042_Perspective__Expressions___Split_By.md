# Split By

**Split By** turns one series into several — one per distinct value of the
chosen column. Grouping by `Month` and splitting by `Region` gives, for each
month, a separate mark per region.

Where Group By decides the categories along the axis, Split By decides how many
series are drawn at each category.

Split columns are named `<split value>|<column>` internally — `North|Sales`,
`South|Sales` — which is why axis labels and legends show that form.

Splitting on a high-cardinality column produces a series per distinct value, so
filter with **Where** first if the column has many.
