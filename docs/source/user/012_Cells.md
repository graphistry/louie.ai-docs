# Cells

A **cell** is the unit of work in a notebook. Each one holds a request and the
output it produced, stacked in the order you ran them.

## What a cell holds

- The request you wrote, in plain language or in a tool's own syntax
- The agent that ran it, and how long the run took
- The output: text, tables, charts, graphs or named values
- The tool calls the agent made, expandable for the reasoning behind them

![A completed cell: the request, the run status, and its output](./images/user/015_running_a_cell.png)

## Working across cells

Named values produced by one cell are available to later cells, so a dataframe
built in one place can be charted or filtered further down the notebook without
rebuilding it.

Three kinds of cell are available from the toolbar — a prompt cell, a markdown
cell for notes, and an input group cell for parameters later cells can read.
See [The Cell Toolbar](014_Cell_Toolbar.md).
