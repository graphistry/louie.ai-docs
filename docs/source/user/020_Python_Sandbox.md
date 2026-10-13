# The Python Sandbox

Python runs server-side in a sandbox, not in your browser.

- **No internet access.** Code cannot reach outside; work from data already in
  the notebook or pulled through a connector.
- **Preinstalled pydata stack** — pandas, numpy, matplotlib and the usual
  companions. Packages cannot be installed from a cell.
- **Stateless between runs.** Variables do not survive from one run to the next.
  Anything you want to keep must be saved as an output — see
  [Python Outputs](024_Python_Outputs.md).

Statelessness is the part that surprises people coming from Jupyter: a cell
cannot rely on a variable another cell defined. Pass data between cells through
named values instead.
