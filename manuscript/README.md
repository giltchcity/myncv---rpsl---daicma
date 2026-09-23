# Manuscript

**Working title:** Continuing Dense Dynamic Maps Across Deployments.

The canonical paper is `main.tex`. In Overleaf, select `manuscript/main.tex` as the main document. Its complete section order is:

1. `sec/0_abstract.tex`
2. `sec/1_intro.tex`
3. `sec/2_related_work.tex`
4. `sec/4_method.tex`
5. `sec/5_experiments.tex`
6. `sec/6_limitations.tex`
7. `sec/7_conclusion.tex`

The historical files under `../paper_sections_20260923/` are preserved snapshots, not the current manuscript.

## Build

From this directory, run `latexmk -pdf main.tex`, or run `pdflatex main.tex`, `bibtex main`, and `pdflatex main.tex` twice. The paper uses `main.bib`, `gaussian.bib`, `landscape.bib`, `bib_additions.bib`, and `revision_context.bib`.

The repository's original CVPR author kit is retained: release `CVPR2026-v1(latex)`, upstream commit `12909ae`, acquired 2026-08-06. `cvpr.sty` and `ieeenat_fullname.bst` have not been replaced or edited. Verify the correct target-year kit, submission metadata, page limits, and author guidelines before submission. The current paper ID is still a placeholder.

## Reading proof and review record

`reading_copy.tex` is a separate two-column proof wrapper using the same seven section files and `reading_refs.bib`. It can be compiled without the CVPR style and was used for the supplied reading PDF. It is not the official submission layout and does not establish template compliance.

`READABILITY_REVIEW_20260924.md` records the full rewrite, three actual self-review passes, preservation of the 152 numerical result-table entries, and remaining source specifications. An attempted independent AI review failed to read any file; it is explicitly not counted as a completed review.

This is a writing revision. It does not introduce new experiments, automatic re-identification, uncertainty-aware background fusion, or a proven restart-equivalence property. Unknown implementation details must be checked against the matching code and run records rather than filled in from prose.
