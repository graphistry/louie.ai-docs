# Large Charts: Specific Charts

## UMAP Clustering (with Graphistry Graphs)
Large amounts should use trained models to map full dataset ("fit + transform")

After UMAP generated, size considerations follow regular Graphistry ones

Discuss with Graphistry staff:

- Train & embed in databricks or graphistry, and just load in louie
- GPU (remote) for 100K row training sets: Discuss - adding support for new Graphistry GPU endpoint
- GPU (local) for 100K row training sets: Discuss - adding support for local GPU workers
- CPU (local) for 10K row training sets: Discuss

## X Bar, Y Bar

- Single-dimensional (single column) is fast
- Two-dimensional (two columns) often too slow
- A groupby aggregate runs per bar
- Many bars * many sub-bars => explosion!

## Graphistry Graphs

For strong clients with good networks:
- < 2M edges
- < 400K nodes
- Less for weaker clients

Discuss: VDI options

Limit number of attributes, especially strings: Blows up memory

