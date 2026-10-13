# Python

Louie runs Python for you in a sandbox, with the usual data-science stack
(pandas, numpy, matplotlib) already installed. Results come back as named
values you can chart, table or feed into later cells.

There is no dedicated "Python cell". You choose a **Python agent** on any
cell — see [The Cell Toolbar](014_Cell_Toolbar.md):

- **Python AI** — describe what you want in plain language and the agent
  writes, runs and debugs the code
- **Python** (passthrough) — you supply the code and it runs as given

## Example

Asking **Python AI** for

> Use Python with pandas to build a dataframe of monthly sales for 3 regions
> over 12 months, then show the dataframe.

runs the code and returns a named dataframe, listed under its name with its
shape, ready to use in later cells.
