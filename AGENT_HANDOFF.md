# Agent Handoff

Date: 2026-08-06

## Your Role

You are handling the paper-writing track of a larger implementation project.
Do not redesign the mapping system unless explicitly asked. First turn the
verified implementation and experiment history into a precise paper outline,
method description, claim table, and figure plan.

## Canonical Storyline

Read `08_STORYLINE_TAXONOMY_REAUDIT_2026-08-06.md` before writing. The hierarchy
is binding:

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

## Paper Tasks

1. Keep Introduction, Related Work, problem formulation, method, and experiments
   consistent with the D1+D2 / D3 hierarchy.
2. Draft an explicit claim/evidence table using `03_CLAIMS_AND_EVIDENCE.md`.
3. Develop a principled persistent scene-memory representation and inference
   mechanism that lets a complete D1+D2 session recur after a D3 boundary.
4. Plan one system figure showing Session A D1+D2 -> memory -> D3 -> Session B
   D1+D2, one evidence-state figure, one process figure, and one
   failure/ablation figure.
5. Leave quantitative placeholders where official comparable metrics are still
   missing. Never invent or transplant numbers from a different evaluator.

## Literature Rule

Every technical statement about prior work must be grounded in the original
full paper, including assumptions, method, experiments, and limitations. A
paper's criticism of prior work is not its own capability. Future work is not an
implemented component. Use the source ledgers in:

- `06_FULL_TEXT_EVIDENCE_AUDIT_2026-08-06.md`
- `07_GAUSSIAN_FULL_TEXT_EVIDENCE_AUDIT_2026-08-06.md`
- `08_STORYLINE_TAXONOMY_REAUDIT_2026-08-06.md`

## Useful Starting Artifacts

- Full run record:
  `../session_update_baseline/rounds/khronos_office_reversed_ab_30s_20260730/RUN_SUMMARY.md`
- Latest visualization:
  `../session_update_baseline/rounds/khronos_office_reversed_ab_30s_20260730/process_visualization_semantic_unified_v5_reobservation/`
- Method model: `../session_update_baseline/THREE_MODE_UNIFIED_MODEL.md`
- Khronos patches: `../session_update_baseline/ports/khronos_core/`
- Core reconciler:
  `../session_update_baseline/src/base1/object_guided_map_reconciler.cpp`
