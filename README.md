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
6. `15_SATURATED_CORE_FULL_TEXT_NOVELTY_AUDIT_2026-08-07.md`: **authoritative
   38-paper full-text novelty conclusion, existing method space, and safe claim.**
7. `14_AUTHORITATIVE_FULL_TEXT_AUDIT_PROTOCOL_2026-08-07.md`: binding PDF-level
   literature standard and stopping rule.
8. `08_STORYLINE_TAXONOMY_REAUDIT_2026-08-06.md`: authoritative D1/D2/D3
   hierarchy.
9. `13_SUPERMAP_DYMRO_ELITE_FULL_TEXT_CORRECTION_2026-08-07.md`: correction
   after full-text reading of the uploaded papers.
10. `12_NOVELTY_AND_METHOD_SPACE_AUDIT_2026-08-07.md`: earlier provisional
    method-space analysis; use the saturated audit when the files disagree.
11. `10_BROAD_DYNAMIC_MAPPING_LANDSCAPE_2026-08-07.md`: high-recall candidate
    pool, not an authoritative source of technical claims.
12. `11_PRIORITY_FULL_TEXT_AUDIT_QUEUE_2026-08-07.md`: remaining pre-submission
    checks, especially ProbPer-LiLo and publication-status updates.
13. `06_FULL_TEXT_EVIDENCE_AUDIT_2026-08-06.md`: earlier core evidence ledger.
14. `07_GAUSSIAN_FULL_TEXT_EVIDENCE_AUDIT_2026-08-06.md`: Gaussian evidence.
15. `literature/README.md`: local PDF download and hash workflow.

## Canonical Storyline

```text
D1 + D2 = dynamic mapping inside each continuously running session
D3      = persistent scene-memory continuation across completed sessions
```

Every new D3 session loads prior memory, reconciles changes since the previous
session, and simultaneously runs new D1 and D2 events.

## Current Novelty Conclusion

A broad claim that nobody has combined intra-session and inter-session dynamics
is false. Efficient Long-Term Mapping (2018), ELite, and several lifelong
mapping systems already combine current-session dynamic suppression with
multi-session map update. Khronos already provides dense single-session D1+D2.
Panoptic Multi-TSDFs, POCD, POV-SLAM, ObVi-SLAM, ELite, and related systems
provide important D3 mechanisms.

The defensible gap found in the saturated full-text audit is narrower:

> Existing systems either preserve rich dynamic histories inside one
> continuously running session or maintain cleaned geometric/object maps across
> sessions. The audited literature did not contain a dense metric-semantic
> system that recursively transfers the state required to retain D1 histories,
> perform explicit same-session D2 reasoning, update object and structural
> geometry across D3, and resume the same D1+D2 process in each independent
> session.

This remains a `to the best of our knowledge` statement and must be refreshed
before submission. ProbPer-LiLo is not used to support the final conclusion until
its full PDF is obtained and audited.

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
  15_SATURATED_CORE_FULL_TEXT_NOVELTY_AUDIT_2026-08-07.md
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