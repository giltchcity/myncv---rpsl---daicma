# CVPR Paper Workspace

Created: 2026-08-06

This directory is the independent Git-ready writing and agent-handoff workspace
for the current Khronos-based scene-memory project.

## Read In This Order

1. `AGENT_HANDOFF.md`: scope, implementation truth, and writing rules.
2. `01_STORYLINE.md`: canonical D1+D2 / D3 research story.
3. `02_CODE_AND_MODULES.md`: implementation entry points.
4. `03_CLAIMS_AND_EVIDENCE.md`: established, preliminary, and unproved claims.
5. `17_VERIFIED_PDF_AUDIT_TRACKER_2026-08-07.md`: **authoritative count of PDFs
   actually opened and read end-to-end. Current verified count: 12.**
6. `14_AUTHORITATIVE_FULL_TEXT_AUDIT_PROTOCOL_2026-08-07.md`: binding PDF-level
   literature standard.
7. `18_KHRONOS_SELF_FETCHED_FULL_TEXT_AUDIT_2026-08-07.md`: complete
   self-fetched Khronos audit.
8. `19_CORE_D3_SELF_FETCHED_FULL_TEXT_AUDIT_2026-08-07.md`: complete audits of
   Panoptic Multi-TSDFs, POCD, POV-SLAM, LT-Mapper, and ObVi-SLAM.
9. `13_SUPERMAP_DYMRO_ELITE_FULL_TEXT_CORRECTION_2026-08-07.md`: verified
   correction for SuperMap, DYMRO-SLAM, and ELite.
10. `16_EFFICIENT_MAPPING_PROBPER_FULL_TEXT_CORRECTION_2026-08-07.md`: verified
    correction for Efficient Long-Term Mapping and ProbPer-LiLo.
11. `15_SATURATED_CORE_FULL_TEXT_NOVELTY_AUDIT_2026-08-07.md`: **retracted**;
    it must not be used as evidence.
12. `10_BROAD_DYNAMIC_MAPPING_LANDSCAPE_2026-08-07.md`: candidate pool only.
13. `11_PRIORITY_FULL_TEXT_AUDIT_QUEUE_2026-08-07.md`: remaining PDFs to verify.
14. `literature/README.md`: local PDF download and hash workflow.

## Canonical Storyline

```text
D1 + D2 = dynamic mapping inside each continuously running session
D3      = persistent scene-memory continuation across completed sessions
```

Every new D3 session loads prior memory, reconciles changes since the previous
session, and simultaneously runs new D1 and D2 events.

## Current Evidence Status

No universal-negative or first-work novelty claim is currently authorized.
Technical statements may enter the manuscript only after the original PDF has
been read across its exact problem, inputs, state variables, method, experiments,
and limitations.

The following earlier claim has been explicitly withdrawn:

```text
38 papers were fully audited and the literature search was saturated.
```

That standard had not been met. The only valid count is maintained in
`17_VERIFIED_PDF_AUDIT_TRACKER_2026-08-07.md`.

Current verified total:

```text
self-fetched and complete: 6
user-uploaded and complete: 6
total complete: 12
```

Key verified classifications:

- **Khronos:** complete dense D1+D2 inside one continuous session; no published
  process-separated D3 continuation.
- **Panoptic Multi-TSDFs:** dense D3 object/submap state with
  persistent/absent/unobserved; D1 tracking is future work.
- **POCD:** object-level D3 mapping with Gaussian--Beta change/stationarity
  belief; external poses; no retained D1.
- **POV-SLAM:** joint robot-pose and semi-static object-consistency D3 SLAM; no
  complete D1 history or explicit same-session D2 output.
- **LT-Mapper:** D3 geometric current-map maintenance with positive/negative
  changes; moving content is removed.
- **ObVi-SLAM:** genuine recursive deployment object prior, restricted to static
  object landmarks.
- **SuperMap:** one continuous RGB-D/point-cloud stream; ten-minute change run;
  semantic object-map maintenance rather than process-separated D3.
- **DYMRO-SLAM:** dynamic feature rejection for ORB-SLAM3 localization.
- **DYNEMO-SLAM:** one continuous dynamic-entity scene-graph SLAM run.
- **ELite:** current-session dynamic-point removal plus cross-session point-map
  ephemerality and refinement.
- **Efficient Long-Term Mapping:** free-space-aware cleaning of 2D local maps
  plus multi-session pose-graph/local-map maintenance; no D1/D2 state.
- **ProbPer-LiLo:** binary static/non-static persistence modeling followed by
  recursive static lifelong-map refinement; all dynamic and quasi-static content
  is removed rather than preserved.

## Working Title

**Evidence-Gated Scene Memory Reconciliation for Dynamic and Revisited
Environments**

## One-Sentence Project Description

We extend a Khronos-based mapping pipeline with persistent cross-session scene
memory and conservative evidence-gated reconciliation, while retaining
Khronos's within-session dynamic tracking.

## Technical Sources

- Code repository: `giltchcity/session_update_baseline_project`
- Main specification: `session_update_baseline/base1.md`
- Temporal model: `session_update_baseline/THREE_MODE_UNIFIED_MODEL.md`
- Latest Office A/B record:
  `session_update_baseline/experiment_records/current/RUN_SUMMARY.md`

Repository notes are implementation records, not substitutes for original-paper
literature evidence.

## Literature Rule

A paper title or abstract never determines D1/D2/D3 coverage. In particular:

- `dynamic` may mean only feature rejection;
- `persistent` may mean identity within one video;
- `lifelong` may mean recursively cleaning a static localization map;
- `multi-session` does not imply that a complete dynamic-scene state is restored.

Future work is not an implemented capability, and criticism in one paper's
Related Work is not evidence about the cited method.
