# Manuscript

**Working title:** Persistent Map Updates from Temporally Valid Observations.

The canonical paper is `main.tex`, on `main`.
Select `manuscript/main.tex` as the main document in Overleaf.

The method is an update layer that runs beside an existing mapper. The paper
connects it to a TSDF mapper (Khronos), a 3D Gaussian mapper (GaME), and an
occupancy mapper (wavemap). Numbers in `\prov{}` are provisional and will be
replaced by the final runs. Author-only `% SRC` comments
give the result file behind each number.

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
`landscape.bib`, `bib_additions.bib`, `revision_context.bib`, and
`supporting_refs_20261019.bib`. Draft markers (`\prov`, `\TODO`, `\note`,
`\directive`) are defined in `draft_macros.tex`; set `\draftmodefalse` there
for a clean copy.

Historical workspace notes outside this directory are not included in the paper.
