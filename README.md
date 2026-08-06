# CVPR Paper Workspace

Created: 2026-08-06

This directory is the independent Git-ready writing and agent-handoff workspace for the current
Khronos-based scene-memory project. The separate top-level `papers/` directory
stores source PDFs and literature material; do not mix those files with this
working paper package.

## Read In This Order

1. `AGENT_HANDOFF.md`: scope, current truth, and immediate writing task.
2. `01_STORYLINE.md`: the research problem and paper narrative.
3. `02_CODE_AND_MODULES.md`: implementation entry points and module behavior.
4. `03_CLAIMS_AND_EVIDENCE.md`: what is proved, preliminary, or not yet proved.
5. `04_PROGRESS_2026-08-06.md`: dated progress and reproducible artifact paths.
6. `05_LITERATURE_STATUS_2026-08-06.md`: publication status and D1/D2/D3 scope.
7. `06_FULL_TEXT_EVIDENCE_AUDIT_2026-08-06.md`: section/page-grounded evidence,
   allowed conclusions, limitations, and prohibited misreadings for the core
   robotics and SLAM literature.
8. `07_GAUSSIAN_FULL_TEXT_EVIDENCE_AUDIT_2026-08-06.md`: dedicated audit of
   static-map Gaussian SLAM, 4D Gaussian SLAM, and evolving Gaussian maps.
9. `literature/README.md`: reproducible local PDF download and hash workflow.

## Working Title

**Evidence-Gated Scene Memory Reconciliation for Dynamic and Revisited
Environments**

This is a working title, not a finalized paper title.

## One-Sentence Project Description

We extend a Khronos-based mapping pipeline with persistent cross-session scene
memory and conservative evidence-gated reconciliation, while retaining
Khronos's within-session dynamic tracking and preventing dynamic semantics from
leaking into the static map.

## Authoritative Technical Sources

- Baseline code repository:
  `https://github.com/giltchcity/session_update_baseline_project`
- Main specification: `session_update_baseline/base1.md` in the code repository.
- Unified temporal model: `session_update_baseline/THREE_MODE_UNIFIED_MODEL.md`
  in the code repository.
- Latest Office A/B run record:
  `session_update_baseline/experiment_records/current/RUN_SUMMARY.md` in the
  code repository.
- Historical final-current evaluation:
  `session_update_baseline/base1_eval_summary.md` in the code repository.

When these files disagree, prefer the dated latest run record, but preserve its
interpretation boundaries.

## Literature Evidence Rule

Technical statements about prior work must be grounded in the original full
paper, including its assumptions, method, experiments, and limitations. The
repository does not redistribute third-party PDFs. Instead,
`literature/papers.json` and `literature/gaussian_papers.json` record open sources,
and `literature/download_papers.py` downloads local audit copies and computes
their SHA-256 hashes. The PDFs and generated hash manifests are intentionally
ignored by Git.

## Repository Layout

```text
CVPR/
  README.md
  AGENT_HANDOFF.md
  01_STORYLINE.md
  02_CODE_AND_MODULES.md
  03_CLAIMS_AND_EVIDENCE.md
  04_PROGRESS_2026-08-06.md
  05_LITERATURE_STATUS_2026-08-06.md
  06_FULL_TEXT_EVIDENCE_AUDIT_2026-08-06.md
  07_GAUSSIAN_FULL_TEXT_EVIDENCE_AUDIT_2026-08-06.md
  GITHUB_OVERLEAF_WORKFLOW.md
  literature/
    README.md
    papers.json
    gaussian_papers.json
    download_papers.py
    pdfs/                                  # local, ignored
    download_manifest.generated.json       # local, ignored
    gaussian_download_manifest.generated.json # local, ignored
  manuscript/
    main.tex
    cvpr.sty
    preamble.tex
    main.bib
    gaussian.bib
    sec/
      0_abstract.tex
      1_intro.tex
      2_related_work.tex
    figures/
```

`manuscript/` currently contains the official `CVPR2026-v1(latex)` author kit as
a provisional drafting template. No official CVPR 2027 author kit was available
on 2026-08-06. Replace the kit and recheck the author guidelines when the target
year publishes its official release.

The implementation is intentionally kept out of this Overleaf-facing paper
repository. The separate code repository is
`giltchcity/session_update_baseline_project`; it excludes datasets, maps, bags,
build products, and generated visualization sequences.
