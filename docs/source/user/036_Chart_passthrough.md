# Chart Passthrough

The **Chart** agent takes a chart specification and renders it, with no AI step.
Use it when you know exactly what you want, or when you are reproducing a chart
and want no interpretation in the way.

It is selected like any other agent, from **Select agent** on the cell — see
[Running Non-AI Cells](018_Running_Non_AI_Cells.md).

## The other visual agents

The same passthrough/AI split applies across the visual agents:

| Visualization | Passthrough | AI |
|---|---|---|
| Charts | **Chart** | **Chart AI** |
| Network graphs | **Graph** | **Graph+UMAP AI** |
| Clustering | **UMAP** | **Graph+UMAP AI** |
| Maps | — | **Map** |
| Diagrams | **Mermaid** | **Mermaid AI** |

Graphs and maps are not Perspective charts — they render in their own viewers
and do not appear in the Perspective chart type picker.
