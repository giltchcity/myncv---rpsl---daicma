# Agent Handoff

Date: 2026-08-07

## Your Role

You are handling the paper-writing track of a larger implementation project.
Do not redesign the mapping system unless explicitly asked. First turn the
verified implementation and experiment history into a precise paper outline,
method description, claim table, and figure plan.

## Authoritative Reading Order

Before writing or auditing literature, read:

1. `01_STORYLINE.md` -- canonical D1+D2 / D3 research story.
2. `03_CLAIMS_AND_EVIDENCE.md` -- what is established, preliminary, designed, or
   not proved.
3. `17_VERIFIED_PDF_AUDIT_TRACKER_2026-08-07.md` -- only authoritative complete
   primary-text count; current verified total is **35**.
4. `22_ARCHITECTURE_AXIS_CITATION_AUDIT_2026-08-07.md` -- authoritative
   cross-paper synthesis and the remaining literature question.
5. `23_SEVEN_NEIGHBOURS_ARCHITECTURE_REAUDIT_2026-08-07.md` -- complete re-audit
   of CubifyGS, DynaMem, CogniMap3D, DovSG, DynamicGSG, DGSG-Mind, and DREAM.
6. `14_AUTHORITATIVE_FULL_TEXT_AUDIT_PROTOCOL_2026-08-07.md` -- binding rules for
   promoting any new paper to verified status.

Older broad landscape and taxonomy files may be useful as search history, but
must not override these documents.

## Canonical Storyline

The hierarchy is binding:

```text
D1 + D2 = dynamic mapping inside every continuously running session
D3      = persistent scene-memory continuation across completed sessions
```

- **D1:** an entity moves while visible in the current session. Represent the
  observed motion with a trajectory, temporal bounding boxes, timestamps, and
  time-indexed geometry; do not fuse it into the static map.
- **D2:** the same SLAM session remains active, but a change occurs while the
  robot looks elsewhere. On re-observation, infer persistent, absent,
  unobserved, and new content without inventing an unobserved trajectory.
- **D3:** Session A terminates, the environment changes, and independently
  started Session B imports persistent scene memory from A. B reconciles A-to-B
  changes while concurrently running new D1 and D2 events and then exports the
  prior for Session C.

Do not describe D1, D2, and D3 as three parallel detectors. D1 and D2 are the two
intra-session observation modes; D3 is the interface connecting complete D1+D2
sessions. Splitting a continuous sequence and restarting at the cut is a
checkpoint/recovery control, not by itself a D3 experiment.

## Literature Question

Do not convert the project into a component-level novelty checklist. The paper is
not claiming that ray deletion, object association, persistence beliefs,
Gaussian updates, scene graphs, relocalization, or map merging are individually
new.

The remaining architecture-level question is:

> Does prior work run a complete D1+D2 Session A, preserve sufficient scene state
> after A terminates, initialize an independent Session B from that state,
> reconcile D3, let B again execute complete D1+D2, and export the same state
> contract recursively for Session C?

For every new candidate, use the eight-question checklist in
`22_ARCHITECTURE_AXIS_CITATION_AUDIT_2026-08-07.md`. A paper is not a direct
architectural competitor merely because it shares one mechanism with this
system.

The current 35-paper verified corpus includes the seven promoted neighbours in
file `23`. Their key boundaries are:

- **CogniMap3D:** genuine multi-visit retrieval/relocalization/update, but the
  persistent memory is a static-scene memory; dynamic regions are tracked only
  to separate them from the persistent map.
- **DGSG-Mind:** later observations can be relocalized against an existing
  Gaussian map without continuous online SLAM, but the paper explicitly leaves
  an integrated tracking module to future work.
- **CubifyGS:** continuous object identity/asset maintenance, but cross-session
  asset merging is explicitly future work.
- **DovSG:** consecutive tasks are evaluated without manual resets; this is a
  continuing deployment, not an independently restarted B session.
- **DynaMem, DynamicGSG, DREAM:** strong online/current-memory update, but no
  complete process-separated D1+D2 restoration contract.

Within the verified 35-paper corpus, no complete A -> D3 -> B -> C bridge has
been found. This is corpus-bounded, not a universal `first ever` proof.

## Project Context

The project starts from Khronos, which supports D1 short-term dynamic tracking
and D2 hidden-change reconciliation inside one continuous spatio-temporal
mapping problem. The missing layer investigated here is persistent scene memory:
a completed session should export sufficient state for a later independent
session to reconcile inter-session changes and resume the complete D1+D2
mapping process.

The method is not object-only. Objects and structural surface patches should
share the same evidence semantics. Wall/floor labels may protect or group
structure, but semantics alone must never command deletion.

## Current Implementation Truth

- A complete Khronos-derived Office Session A and Session B can be processed.
- Session B output reconciliation starts from Session A's saved global mesh,
  rather than merely reading A object metadata.
- Current B geometry supports, repairs, or extends the inherited map.
- Inherited geometry is deleted only with reliable later absence/free-space
  evidence; unobserved geometry is retained.
- Configured dynamic semantic pixels are excluded from static TSDF fusion.
- Connected dynamic semantic components can enter Khronos's existing D1 tracker,
  producing trajectories, temporal bounding boxes, and point frames.
- Private static object meshes can be displayed and selectively used for map
  repair.
- A complete 0 -> Session A -> Session B visualization exists with both robot
  trajectories and synchronized RGB sensor views.

## Critical Boundaries

Do not write any of the following as established facts:

- This is not a native hot restart of the entire Khronos backend. PGMO state,
  the active window, asynchronous backend threads, and the live ray hash are
  not restored.
- The current Office A/B protocol is a derived reverse-time visualization and
  pipeline test. Its retimed B clock does not directly match the stock Office
  GT timeline, so it does not yet supply official Background/Object/Change
  P/R/F1.
- A temporal split or software restart alone does not prove D3.
- The historical official final-current evaluation did not improve background
  F1. It diagnosed that naive object-distance cleanup was too aggressive.
- Structural-patch reconciliation is designed but not yet implemented as a
  complete patch-level updater.
- The current merge improves coverage and connectivity; it is not a new TSDF
  reintegration or super-resolution method.
- The current method is still largely a combination of existing mechanisms; the
  final methodological innovation and mathematical model remain under
  development.
- Do not claim that the complete A -> D3 -> B -> C architecture has been proved
  by the current Office pipeline unless B is shown to execute new D1 and D2
  events and the recursive state contract is validated.

## Paper Tasks

1. Keep Introduction, Related Work, problem formulation, method, and experiments
   consistent with the D1+D2 / D3 hierarchy.
2. Keep every contribution sentence consistent with `03_CLAIMS_AND_EVIDENCE.md`.
3. Develop a principled persistent scene-memory representation and inference
   mechanism that lets a complete D1+D2 session recur after a D3 boundary.
4. Close the architecture-focused citation chain defined in files `11` and `22`;
   do not add papers merely for corpus size.
5. Plan one system figure showing Session A D1+D2 -> memory -> D3 -> Session B
   D1+D2, one evidence-state figure, one process figure, and one
   failure/ablation figure.
6. Leave quantitative placeholders where official comparable metrics are still
   missing. Never invent or transplant numbers from a different evaluator.

## Literature Rule

Every technical statement about prior work must be grounded in the original
complete paper, including assumptions, method, experiments, and limitations. A
paper's criticism of prior work is not its own capability. Future work is not an
implemented component.

Authoritative literature records are:

- `17_VERIFIED_PDF_AUDIT_TRACKER_2026-08-07.md` -- count and per-paper status;
- `13_SUPERMAP_DYMRO_ELITE_FULL_TEXT_CORRECTION_2026-08-07.md`;
- `16_EFFICIENT_MAPPING_PROBPER_FULL_TEXT_CORRECTION_2026-08-07.md`;
- `18_KHRONOS_SELF_FETCHED_FULL_TEXT_AUDIT_2026-08-07.md`;
- `19_CORE_D3_SELF_FETCHED_FULL_TEXT_AUDIT_2026-08-07.md`;
- `20_CORE_D1_D2_AND_PERSISTENCE_SELF_FETCHED_AUDIT_2026-08-07.md`;
- `21_REMAINING_DIRECT_CORE_FULL_TEXT_AUDIT_2026-08-07.md`;
- `23_SEVEN_NEIGHBOURS_ARCHITECTURE_REAUDIT_2026-08-07.md`;
- `22_ARCHITECTURE_AXIS_CITATION_AUDIT_2026-08-07.md` -- synthesis only, not a
  substitute for per-paper primary-text evidence.

## Useful Starting Artifacts

- Full run record:
  `../session_update_baseline/rounds/khronos_office_reversed_ab_30s_20260730/RUN_SUMMARY.md`
- Latest visualization:
  `../session_update_baseline/rounds/khronos_office_reversed_ab_30s_20260730/process_visualization_semantic_unified_v5_reobservation/`
- Method model: `../session_update_baseline/THREE_MODE_UNIFIED_MODEL.md`
- Khronos patches: `../session_update_baseline/ports/khronos_core/`
- Core reconciler:
  `../session_update_baseline/src/base1/object_guided_map_reconciler.cpp`
