# Editing Cells

A cell can be edited and re-run as often as you like. Refining the request after
seeing the output is the normal way to work, not a correction.

## Editing and re-running

1. Run a cell and read the output
2. Edit the request in place
3. Run it again with **Run cell** (⌘+Enter)

Re-running replaces the output. The previous run stays reachable through the
cell's run history, so you can compare what changed.

## View and Edit modes

The **View / Edit** toggle at the top of a notebook switches the whole notebook
between the two. View mode presents the outputs as a finished document, with the
prompts and controls out of the way — useful for sharing a notebook with someone
who only needs the result.

## Understanding a result

The tool-call summary in the cell header expands to show every call the agent
made and what came back. When an answer is wrong, this is where to look first:
it usually shows the agent querying something other than what you meant.
