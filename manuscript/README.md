# Manuscript

**Working title:** Continuing Dense Dynamic Maps Across Deployments.

The canonical paper is `main.tex`. In Overleaf, select `manuscript/main.tex` as the main document. The section order is:

1. `sec/0_abstract.tex`
2. `sec/1_intro.tex`
3. `sec/2_related_work.tex`
4. `sec/4_method.tex`
5. `sec/5_experiments.tex`
6. `sec/6_limitations.tex`
7. `sec/7_conclusion.tex`

The historical files under `../paper_sections_20260923/` are snapshots and are not used by the current manuscript.

## Build

From this directory, run `latexmk -pdf main.tex`, or run `pdflatex main.tex`, `bibtex main`, and `pdflatex main.tex` twice.

The bibliography files used by `main.tex` are `main.bib`, `gaussian.bib`, `landscape.bib`, `bib_additions.bib`, and `revision_context.bib`.
