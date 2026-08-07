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
6. `22_ARCHITECTURE_AXIS_CITATION_AUDIT_2026-08-07.md`: authoritative synthesis
   of the remaining A -> D3 -> B -> C literature question.
7. `14_AUTHORITATIVE_FULL_TEXT_AUDIT_PROTOCOL_2026-08-07.md`: binding audit
   standard.
8. `18_KHRONOS_SELF_FETCHED_FULL_TEXT_AUDIT_2026-08-07.md`: Khronos.
9. `19_CORE_D3_SELF_FETCHED_FULL_TEXT_AUDIT_2026-08-07.md`: Panoptic
   Multi-TSDFs, POCD, POV-SLAM, LT-Mapper, and ObVi-SLAM.
10. `20_CORE_D1_D2_AND_PERSISTENCE_SELF_FETCHED_AUDIT_2026-08-07.md`:
    Changing-SLAM, General Movable Objects, Perpetua, and Lost & Found.
11. `21_REMAINING_DIRECT_CORE_FULL_TEXT_AUDIT_2026-08-07.md`: LTC-Mapping,
    GaME, OASIS-Map, Living Scenes, Dynamic Pose Graph SLAM, Pomerleau 2014,
    RBIF, 4DGS-SLAM, 4DTAM, DynaGSLAM, 4D Primitive-Mache, and LT-Gaussian.
12. `13_SUPERMAP_DYMRO_ELITE_FULL_TEXT_CORRECTION_2026-08-07.md`: SuperMap,
    DYMRO-SLAM, and ELite.
13. `16_EFFICIENT_MAPPING_PROBPER_FULL_TEXT_CORRECTION_2026-08-07.md`: Efficient
    Long-Term Mapping and ProbPer-LiLo.
14. `11_PRIORITY_FULL_TEXT_AUDIT_QUEUE_2026-08-07.md`: architecture-focused
    citation-chain queue and stop rule.
15. `10_BROAD_DYNAMIC_MAPPING_LANDSCAPE_2026-08-07.md`: candidate pool only;
    never use it as full-text evidence.
16. `literature/README.md`: source acquisition and hash workflow.

## Canonical Storyline

```text
inside every continuously running session:
  D1 = observed motion with explicit temporal history
  D2 = hidden/out-of-view change reasoning

across completed independent sessions:
  D3 = persistent scene-state continuation and inter-session reconciliation
```

D3 is not a third detector. It is the interface connecting complete D1+D2
sessions:

```text
Session A runs D1 + D2
-> export persistent scene state
-> Session A terminates
-> environment changes between sessions
-> independent Session B imports A state and reconciles D3
-> Session B again runs new D1 + D2
-> export B state
-> Session C repeats
```

A temporal split of one continuous sequence is not sufficient evidence of D3.

## The Literature Question

The paper is **not** built around claiming that individual mechanisms such as ray
deletion, object association, persistence beliefs, scene graphs, Gaussian map
updates, relocalization, or map merging are new.

The remaining literature question is architecture-level:

> Has any prior system carried a complete D1+D2 dynamic-mapping capability across
> a real process-separated D3 boundary so that an independent B session imports
> A's persistent state, reconciles inter-session changes, again performs D1 and
> D2, and exports equivalent state recursively for C?

Use `22_ARCHITECTURE_AXIS_CITATION_AUDIT_2026-08-07.md` for this synthesis. Do
not turn component overlap into a novelty checklist.

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
withdrawn. The obsolete saturation artifact has been removed from the current
tree; Git history retains the correction record. Only
`17_VERIFIED_PDF_AUDIT_TRACKER_2026-08-07.md` provides a valid count.

Within the 28 verified complete primary texts, no system has been found that
completes the full architecture:

```text
complete D1+D2 Session A
+ persistent export after A terminates
+ independent Session B import
+ D3 reconciliation
+ B again executes complete D1+D2
+ equivalent export for Session C
```

This is a **verified-corpus result**, not a universal proof. A bounded
forward/backward architecture-focused citation-chain pass remains required before
stronger positioning is authorized.

## Working Title

**Evidence-Gated Scene Memory Reconciliation for Dynamic and Revisited
Environments**

## One-Sentence Project Description

We extend a Khronos-based mapping pipeline with persistent cross-session scene
memory and conservative evidence-gated reconciliation so that complete
within-session dynamic mapping can recur across independent deployments.

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
- `multi-session` does not imply restoration of a complete dynamic-scene state;
- sharing a mechanism does not imply sharing the full session architecture.

Future work is not an implemented capability, and one paper's criticism of
another is not evidence of the cited paper's actual method.
