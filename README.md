# CVPR Paper Workspace

Created: 2026-08-06

This directory is the independent Git-ready writing and agent-handoff workspace
for the current Khronos-based scene-memory project.

## Read In This Order

1. `AGENT_HANDOFF.md`: scope, implementation truth, and writing rules.
2. `01_STORYLINE.md`: canonical D1+D2 / D3 research story.
3. `02_CODE_AND_MODULES.md`: implementation entry points.
4. `03_CLAIMS_AND_EVIDENCE.md`: established, preliminary, and unproved claims.
5. `17_VERIFIED_PDF_AUDIT_TRACKER_2026-08-07.md`: **authoritative count of
   complete primary-text audits. Current verified count: 28.**
6. `14_AUTHORITATIVE_FULL_TEXT_AUDIT_PROTOCOL_2026-08-07.md`: binding audit
   standard.
7. `18_KHRONOS_SELF_FETCHED_FULL_TEXT_AUDIT_2026-08-07.md`: Khronos.
8. `19_CORE_D3_SELF_FETCHED_FULL_TEXT_AUDIT_2026-08-07.md`: Panoptic
   Multi-TSDFs, POCD, POV-SLAM, LT-Mapper, and ObVi-SLAM.
9. `20_CORE_D1_D2_AND_PERSISTENCE_SELF_FETCHED_AUDIT_2026-08-07.md`:
   Changing-SLAM, General Movable Objects, Perpetua, and Lost & Found.
10. `21_REMAINING_DIRECT_CORE_FULL_TEXT_AUDIT_2026-08-07.md`: LTC-Mapping,
    GaME, OASIS-Map, Living Scenes, Dynamic Pose Graph SLAM, Pomerleau 2014,
    RBIF, 4DGS-SLAM, 4DTAM, DynaGSLAM, 4D Primitive-Mache, and LT-Gaussian.
11. `13_SUPERMAP_DYMRO_ELITE_FULL_TEXT_CORRECTION_2026-08-07.md`: SuperMap,
    DYMRO-SLAM, and ELite.
12. `16_EFFICIENT_MAPPING_PROBPER_FULL_TEXT_CORRECTION_2026-08-07.md`: Efficient
    Long-Term Mapping and ProbPer-LiLo.
13. `15_SATURATED_CORE_FULL_TEXT_NOVELTY_AUDIT_2026-08-07.md`: **retracted**;
    never use it as evidence.
14. `10_BROAD_DYNAMIC_MAPPING_LANDSCAPE_2026-08-07.md`: candidate pool only.
15. `literature/README.md`: source acquisition and hash workflow.

## Canonical Storyline

```text
D1 + D2 = dynamic mapping inside each continuously running session
D3      = persistent scene-memory continuation across completed sessions
```

Every D3 session loads prior memory, reconciles changes since the previous
session, and simultaneously runs new D1 and D2 events.

## Current Evidence Status

The fixed direct-core queue is complete:

```text
self-acquired complete primary texts: 22
  direct PDF/complete publisher text: 21
  complete author full-text rendering: 1 (RBIF; PDF bytes rate-limited)
user-uploaded complete PDFs:          6
total verified complete:             28
direct-core queue pending:            0
```

The earlier claim that 38 papers had already been fully audited was false and is
withdrawn. Only `17_VERIFIED_PDF_AUDIT_TRACKER_2026-08-07.md` provides a valid
count.

The verified set establishes:

- **Dense single-session D1+D2:** Khronos; sparse object-level D1+D2:
  Changing-SLAM.
- **Object-level D2 theory/maintenance:** General Movable Objects, LTC-Mapping,
  SuperMap; dense Gaussian D2: GaME.
- **D3 geometric/static-map maintenance:** Dynamic Pose Graph SLAM, Pomerleau,
  Efficient Long-Term Mapping, LT-Mapper, RBIF, ELite, ProbPer-LiLo, and
  LT-Gaussian.
- **D3 object/volumetric methods:** Panoptic Multi-TSDFs, POCD, POV-SLAM,
  ObVi-SLAM, OASIS-Map, and Living Scenes.
- **Rich continuous D1 representations:** Lost & Found, DYNEMO-SLAM,
  4DGS-SLAM, 4DTAM, DynaGSLAM, and 4D Primitive-Mache.

Within the verified set, no method jointly retains D1 trajectories and
 time-indexed geometry, performs explicit same-session D2 reasoning, maintains a
dense object-plus-structural current map, exports/imports complete state across a
D3 process boundary, and resumes D1+D2 recursively in Session B/C.

This is not yet a universal proof. A bounded forward/backward citation-chain pass
must still test whether the closest papers lead to a genuinely new direct
neighbour. Only such new neighbours require another complete audit.

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

A title or abstract never determines D1/D2/D3 coverage:

- `dynamic` may mean only rejection or static-map cleaning;
- `persistent` may mean permanence within one continuous video;
- `lifelong` may mean recursive maintenance of a static localization map;
- `multi-session` does not imply restoration of a complete dynamic-scene state.

Future work is not an implemented capability, and one paper's criticism of
another is not evidence of the cited paper's actual method.
