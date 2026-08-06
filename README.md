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
   actually opened and read end-to-end. Current verified count: 16.**
6. `14_AUTHORITATIVE_FULL_TEXT_AUDIT_PROTOCOL_2026-08-07.md`: binding PDF-level
   literature standard.
7. `18_KHRONOS_SELF_FETCHED_FULL_TEXT_AUDIT_2026-08-07.md`: complete Khronos
   audit.
8. `19_CORE_D3_SELF_FETCHED_FULL_TEXT_AUDIT_2026-08-07.md`: Panoptic
   Multi-TSDFs, POCD, POV-SLAM, LT-Mapper, and ObVi-SLAM.
9. `20_CORE_D1_D2_AND_PERSISTENCE_SELF_FETCHED_AUDIT_2026-08-07.md`:
   Changing-SLAM, General Movable Objects, Perpetua, and Lost & Found.
10. `13_SUPERMAP_DYMRO_ELITE_FULL_TEXT_CORRECTION_2026-08-07.md`: SuperMap,
    DYMRO-SLAM, and ELite.
11. `16_EFFICIENT_MAPPING_PROBPER_FULL_TEXT_CORRECTION_2026-08-07.md`: Efficient
    Long-Term Mapping and ProbPer-LiLo.
12. `15_SATURATED_CORE_FULL_TEXT_NOVELTY_AUDIT_2026-08-07.md`: **retracted**;
    it must not be used as evidence.
13. `10_BROAD_DYNAMIC_MAPPING_LANDSCAPE_2026-08-07.md`: candidate pool only.
14. `11_PRIORITY_FULL_TEXT_AUDIT_QUEUE_2026-08-07.md`: remaining PDFs to verify.
15. `literature/README.md`: local PDF download and hash workflow.

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

The earlier claim that 38 papers had been fully audited was withdrawn. The only
valid count is maintained in `17_VERIFIED_PDF_AUDIT_TRACKER_2026-08-07.md`.

Current verified total:

```text
self-fetched and complete: 10
user-uploaded and complete: 6
total complete: 16
```

Key verified boundaries now include:

- **Khronos:** complete dense D1+D2 inside one continuous session.
- **Changing-SLAM:** genuine sparse object-level D1+D2 visual SLAM; no D3.
- **General Movable Objects:** probabilistic D2 identity/location tracking over
  observation gaps; not SLAM and no dense map.
- **Lost & Found:** observed D1 interaction trajectories and scene-graph update;
  object must remain visible.
- **Perpetua:** feature existence/persistence prediction theory; no geometry or
  mapping protocol.
- **Panoptic Multi-TSDFs, POCD, POV-SLAM, LT-Mapper, ObVi-SLAM, ELite,
  ProbPer-LiLo, and Efficient Long-Term Mapping:** different D3 map-maintenance
  or deployment-prior mechanisms, generally without retained D1 histories.
- **SuperMap:** continuous-stream semantic object-map maintenance, not
  process-separated D3.

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
