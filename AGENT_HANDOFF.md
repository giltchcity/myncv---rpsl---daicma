# Agent Handoff

Date: 2026-08-06

## Your Role

You are handling the paper-writing track of a larger implementation project.
Do not redesign the mapping system unless explicitly asked. First turn the
verified implementation and experiment history into a precise paper outline,
method description, claim table, and figure plan.

## Project Context

The project starts from Khronos, which already supports short-term dynamic
tracking and long-term change reconciliation inside one continuous run. Our
work investigates a missing practical layer: preserving a final current map
and object memory across a session boundary, then using a later traversal to
conservatively update inherited geometry.

The desired system covers three observation regimes:

1. An entity moves while visible: represent it as a dynamic trajectory and do
   not fuse it into the static map.
2. A change occurs while unobserved inside one session: infer
   `absent@old-location + new@new-location` after re-observation unless identity
   is genuinely established.
3. A change occurs between sessions: load prior scene memory and apply the same
   present/absent/unobserved/new logic using the new session as evidence.

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
- Connected dynamic semantic components can enter Khronos's existing dynamic
  tracker, producing trajectories, temporal bounding boxes, and point frames.
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
- The historical official final-current evaluation did not improve background
  F1. It diagnosed that naive object-distance cleanup was too aggressive.
- Structural-patch reconciliation is designed but not yet implemented as a
  complete patch-level updater.
- The current merge improves coverage and connectivity; it is not a new TSDF
  reintegration or super-resolution method.

## First Paper Tasks

1. Produce a one-page paper outline from `01_STORYLINE.md`.
2. Draft an explicit claim/evidence table using `03_CLAIMS_AND_EVIDENCE.md`.
3. Draft the method around one state/evidence model shared by all three regimes.
4. Plan one system figure, one evidence-state figure, one A/B process figure,
   and one failure/ablation figure.
5. Leave quantitative placeholders where official comparable metrics are still
   missing. Never invent or transplant numbers from a different evaluator.

## Useful Starting Artifacts

- Full run record:
  `../session_update_baseline/rounds/khronos_office_reversed_ab_30s_20260730/RUN_SUMMARY.md`
- Latest visualization:
  `../session_update_baseline/rounds/khronos_office_reversed_ab_30s_20260730/process_visualization_semantic_unified_v5_reobservation/`
- Method model: `../session_update_baseline/THREE_MODE_UNIFIED_MODEL.md`
- Khronos patches: `../session_update_baseline/ports/khronos_core/`
- Core reconciler:
  `../session_update_baseline/src/base1/object_guided_map_reconciler.cpp`

