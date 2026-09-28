# Manuscript

**Working title:** Persistent Map Updates from Temporally Valid Observations.

The canonical paper is `main.tex`, on `codex/initial-paper-workspace`.
Select `manuscript/main.tex` as the main document in Overleaf.

The method separates temporal evidence selection from native map integration.
It defines observation validity and memory selection, then gives their TSDF
realization for object and background geometry. The reported tables remain the
existing Khronos-based pipeline results. Author-only `% (double check)` comments
mark synchronization points for the ongoing implementation.

## Contents

- `sec/0_abstract.tex`
- `sec/1_intro.tex`
- `sec/2_related_work.tex`
- `sec/4_method.tex`
- `sec/5_experiments.tex`
- `sec/6_limitations.tex`
- `sec/7_conclusion.tex`
- `figures/update_overview.tex` — editable LaTeX overview diagram

## Build

Run `latexmk -pdf main.tex` from this directory, or `pdflatex main.tex`,
`bibtex main`, and `pdflatex main.tex` twice. The retained CVPR author kit is used
without modification. Bibliography files remain `main.bib`, `gaussian.bib`,
`landscape.bib`, `bib_additions.bib`, and `revision_context.bib`.

Historical workspace notes outside this directory are not included in the paper.
