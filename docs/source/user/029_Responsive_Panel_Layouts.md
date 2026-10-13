# Responsive Panel Layouts

A dashboard can carry a different layout per screen size, so it stays readable
on a laptop and a wall display alike.

## Editing a layout

**Save Layout** in the top right enters layout editing. The button shows which
**breakpoint** you are editing — `MD`, for example.

Each panel has a drag handle in its top left and a resize handle in its bottom
right.

## How breakpoints cascade

Layouts cascade **down** from the largest. A change at a large breakpoint
applies to the smaller ones that have no layout of their own; a change made at a
smaller breakpoint overrides what it inherited.

Lay out the largest size first and work down, otherwise later edits at a large
breakpoint will not reach the smaller ones you have already customised.
