# CVPR Paper Workspace

LaTeX manuscript and lightweight literature resources for **Persistent Map Updates from Temporally Valid Observations**.

## Repository layout

- `manuscript/` — canonical CVPR paper, section files, bibliography, figures, and author kit. Start with `manuscript/README.md` and `manuscript/main.tex`.
- `literature/` — paper source manifests and `download_papers.py` for reproducible local PDF acquisition. PDFs are intentionally not tracked.
- `paper_sections_20260923/` — separate draft/exported section assets; the canonical version is in `manuscript/`.
- `research/` — supplementary research materials.
- `AGENT_HANDOFF.md` — historical project context and writing/claim guardrails.
- `GITHUB_OVERLEAF_WORKFLOW.md` — GitHub/Overleaf integration notes.

## Build the paper

```bash
cd manuscript
latexmk -pdf main.tex
```

Alternatively, set `manuscript/main.tex` as the main document in Overleaf.
See `manuscript/README.md` for document structure and the CVPR bibliography.

## Implementation and evidence

The Khronos-based implementation lives in a separate repository:
https://github.com/giltchcity/session_update_baseline_project

Support technical statements with current implementation results and original published papers. The former root-level numbered progress and literature-audit notes (`01_*.md` through `21_*.md`) were removed to keep the writing repository focused. They remain recoverable from the repository's Git history.
