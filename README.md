# CVPR Paper Workspace

Created: 2026-08-06

This directory is the independent Git-ready writing and agent-handoff workspace
for the current Khronos-based scene-memory project.

## Read In This Order

1. `AGENT_HANDOFF.md`: scope, current implementation truth, and writing rules.
2. `01_STORYLINE.md`: canonical D1+D2 / D3 research story.
3. `02_CODE_AND_MODULES.md`: implementation entry points.
4. `03_CLAIMS_AND_EVIDENCE.md`: what is established, preliminary, or unproved.
5. `04_PROGRESS_2026-08-06.md`: dated technical status.
6. `14_AUTHORITATIVE_FULL_TEXT_AUDIT_PROTOCOL_2026-08-07.md`: **binding PDF-level
   literature standard, audit reset, and priority sequence.**
7. `08_STORYLINE_TAXONOMY_REAUDIT_2026-08-06.md`: authoritative D1/D2/D3
   hierarchy.
8. `13_SUPERMAP_DYMRO_ELITE_FULL_TEXT_CORRECTION_2026-08-07.md`: correction
   after full-text reading of the uploaded papers.
9. `12_NOVELTY_AND_METHOD_SPACE_AUDIT_2026-08-07.md`: provisional novelty and
   method-space analysis; all non-PDF-audited entries require revalidation.
10. `10_BROAD_DYNAMIC_MAPPING_LANDSCAPE_2026-08-07.md`: high-recall candidate
    pool, not an authoritative source of technical claims.
11. `11_PRIORITY_FULL_TEXT_AUDIT_QUEUE_2026-08-07.md`: papers awaiting complete
    PDF audits.
12. `06_FULL_TEXT_EVIDENCE_AUDIT_2026-08-06.md`: earlier core evidence ledger;
    revalidate against the authoritative protocol.
13. `07_GAUSSIAN_FULL_TEXT_EVIDENCE_AUDIT_2026-08-06.md`: earlier Gaussian
    evidence ledger; revalidate against the authoritative protocol.
14. `literature/README.md`: local PDF download and hash workflow.

## Canonical Storyline

```text
D1 + D2 = dynamic mapping inside each continuously running session
D3      = persistent scene-memory continuation across completed sessions
```

Every new D3 session loads prior memory, reconciles changes since the previous
session, and simultaneously runs new D1 and D2 events.

## Literature-Audit Hold

No universal-negative or first-work claim is currently authorized. A paper may
influence Introduction, Related Work, novelty, method design, or baseline choice
only after its original PDF has been audited across:

- exact problem and temporal protocol;
- inputs, assumptions, and estimated variables;
- representation and update equations;
- what is discarded or not represented;
- experiments, metrics, and limitations;
- D1/D2/D3 coverage under this project's definitions;
- exact source pages, sections, equations, and figures.

Older labels such as `FULL` and `PRIMARY` are deprecated unless revalidated in
`14_AUTHORITATIVE_FULL_TEXT_AUDIT_PROTOCOL_2026-08-07.md`.

## Full-Text Correction Summary

The paper title alone never determines overlap:

- **SuperMap** is a continuous-stream open-vocabulary object map and scene graph;
  its evaluated change run is ten minutes, not two hours, and it does not define
  process-separated D3 continuation.
- **DYMRO-SLAM** filters dynamic features for robust ORB-SLAM3 localization; it
  has no retained dynamic map or session memory.
- **ELite** is a strong point-level D3 lifelong-map updater; local ephemerality is
  a dynamic-removal score, not the project's D1/D2 decomposition.
- **DYNEMO-SLAM** jointly optimizes robot and entity poses inside a continuous
  graph, but does not provide process-separated D3 scene-memory transfer.

## Working Title

**Evidence-Gated Scene Memory Reconciliation for Dynamic and Revisited
Environments**

This is a working title.

## One-Sentence Project Description

We extend a Khronos-based mapping pipeline with persistent cross-session scene
memory and conservative evidence-gated reconciliation, while retaining
Khronos's within-session dynamic tracking and preventing dynamic semantics from
leaking into the static map.

## Authoritative Technical Sources

- Baseline code repository:
  `https://github.com/giltchcity/session_update_baseline_project`
- Main specification: `session_update_baseline/base1.md` in the code repository.
- Unified temporal model: `session_update_baseline/THREE_MODE_UNIFIED_MODEL.md`.
- Latest Office A/B run record:
  `session_update_baseline/experiment_records/current/RUN_SUMMARY.md`.
- Historical final-current evaluation:
  `session_update_baseline/base1_eval_summary.md`.

When these files disagree, prefer the dated latest run record, while preserving
its interpretation boundaries.

## Literature Evidence Rule

Technical statements about prior work must be grounded in the original full
paper, including its problem, representation, method, experiments, and
limitations. The repository does not redistribute third-party PDFs. Source URLs
and local download/hash workflows are maintained under `literature/`.

A paper's criticism of prior work is not its contribution. Future work is not an
implemented capability. `Persistent` inside one video is not automatically D3,
and `lifelong` static-map cleaning is not automatically full dynamic scene
memory.

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
  08_STORYLINE_TAXONOMY_REAUDIT_2026-08-06.md
  09_TRADITIONAL_REAUDIT_AND_GAUSSIAN_SELECTION_2026-08-07.md
  10_BROAD_DYNAMIC_MAPPING_LANDSCAPE_2026-08-07.md
  11_PRIORITY_FULL_TEXT_AUDIT_QUEUE_2026-08-07.md
  12_NOVELTY_AND_METHOD_SPACE_AUDIT_2026-08-07.md
  13_SUPERMAP_DYMRO_ELITE_FULL_TEXT_CORRECTION_2026-08-07.md
  14_AUTHORITATIVE_FULL_TEXT_AUDIT_PROTOCOL_2026-08-07.md
  GITHUB_OVERLEAF_WORKFLOW.md
  literature/
  manuscript/
    main.tex
    main.bib
    gaussian.bib
    landscape.bib
    sec/
      0_abstract.tex
      1_intro.tex
      2_related_work.tex
```

The implementation remains in the separate repository
`giltchcity/session_update_baseline_project`.
