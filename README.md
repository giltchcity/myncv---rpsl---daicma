# CVPR Paper

**Persistent Map Updates from Temporally Valid Observations**

This repository contains the LaTeX manuscript and publication assets.

## Paper sources

- `manuscript/main.tex` — main entry point
- `manuscript/sec/` — paper sections
- `manuscript/figures/` — figures and diagram sources
- `manuscript/*.bib` — bibliographies
- `manuscript/cvpr.sty`, `manuscript/ieeenat_fullname.bst` — CVPR formatting

## Build

```bash
cd manuscript
latexmk -pdf main.tex
```

For Overleaf, select `manuscript/main.tex` as the main document.

Research PDFs, literature download manifests, temporary drafts, and agent handoff notes are maintained separately from this paper repository.
