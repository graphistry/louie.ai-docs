# Large Charts: General

## Server Interactions

Server fetches, such as database queries and Python outputs, can be 100MB+ when 100K+ rows, so take care!

- Try doing small datasets and steadily increase their size
- Only pull the columns necessary, avoid "Select * ..."
- Limit large string-valued columns
- Avoid datetime columns as some charts perform heavy conversions

## Chart Interactions: Perspective

As most edits autosave, experiment in non-saving areas:
- Initial query output cell
- Dashboard view (vs edit)

Before switching chart types, remove hazards that are listed below.

Instead of directly switching chart types, which may have unintended configurations, switch to the datagrid type, set a safe config (e.g., only 1 column), and then switch to the desired chart type.

Take care with Group By, Split By, and other compute multipliers/exploders.

Consider whether you can do some of the heavier compute on the server, and send a preaggregated value to the frontend.

