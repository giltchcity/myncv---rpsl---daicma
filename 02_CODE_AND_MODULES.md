# Code and Functional Modules

Date: 2026-08-06

All paths below are relative to `/home/jixian/Desktop/FT`.

## Build and Main Entry Point

### Build definition

`session_update_baseline/CMakeLists.txt`

Builds:

- `run_session_update_baseline`: main reconciliation runner;
- `export_4dmap_mesh_ply`: map/trajectory/display exporter;
- `audit_base1_mesh_errors`: geometric error and object-region audit;
- `test_panoptic_core_in_khronos_env`: portable Panoptic predicate test.

### Environment wrapper

`session_update_baseline/scripts/run_base1_khronos_env.sh`

Loads ROS2 Jazzy and the installed Khronos/Hydra environment, then builds or
runs the Base1 binaries.

### Baseline runner

`session_update_baseline/app/run_session_update_baseline.cpp`

Responsibilities:

1. parse the experiment mode and evidence thresholds;
2. load the current `.4dmap` through Khronos map IO;
3. optionally load a prior map and prior object memory;
4. save an untouched `original_final.4dmap` copy;
5. invoke `ObjectGuidedMapReconciler`;
6. save `improved_final.4dmap` as a single final-current DSG;
7. write command, config, object memory, and CSV/JSON diagnostics.

Important boundary: this runner reconciles saved/current map state. It does not
restore a running Khronos backend or PGMO optimizer.

## Core Reconciliation

### Public interface and configuration

`session_update_baseline/include/session_update_baseline/base1/object_guided_map_reconciler.h`

Defines:

- `ReconcilerConfig`: all cleanup, fusion, protection, dynamic, structural, and
  prior-memory controls;
- `ObjectAuditRow`: per-object geometry, timing, evidence, and decision fields;
- `MeshUpdateSummary`: per-run update counters;
- `ReconcileResult`: object rows and explainable per-vertex decisions;
- `ObjectGuidedMapReconciler`.

### Main implementation

`session_update_baseline/src/base1/object_guided_map_reconciler.cpp`

Major implemented functions:

#### Cross-session global-map initialization

`initializeCrossSessionMesh()` around line 840.

- copies A's global mesh as the output starting state;
- uses B surface proximity as persistent support;
- queries Khronos `RayVerificator` for unsupported A vertices;
- removes ray-confirmed absent A vertices;
- retains unobserved A vertices;
- welds B vertices/faces into the retained A topology;
- records absent/persistent/unobserved/new counts.

#### Main reconciliation flow

`ObjectGuidedMapReconciler::reconcile()` around line 2636.

Coordinates:

- cross-session initialization;
- object audit and prior-memory association;
- object injection/repair;
- optional temporal background/object repair;
- optional plane/volume repair experiments;
- object-guided cleanup;
- dynamic-residue diagnostics and cleanup;
- prior object-node restoration;
- final mesh mutation and reporting.

#### Re-observation-gated object cleanup

Around lines 3042-3156.

The implemented decision is:

```text
B surface support within threshold -> protect
ray presence evidence              -> protect
no ray evidence                    -> unobserved, protect
ray-confirmed absence              -> allow removal
```

This prevents a chair's private mesh/bbox from deleting nearby unchanged wall
or floor geometry.

#### Dynamic-residue safety gate

Around lines 3168-3420.

Candidate residue must be near stored dynamic point frames and overlap the
track time. Horizontal structure and configured labels are protected. Removal
requires later absence evidence unless an explicitly unsafe quarantine ablation
is selected.

#### Persistent diagnostics

Around lines 4160-4683.

Writes object audit, mesh summary, object update, per-vertex update,
evidence summary, and object-memory outputs.

## Khronos Active-Window Extensions

Portable patches live in:

`session_update_baseline/ports/khronos_core/`

### `0001-mask-configured-dynamic-semantics.patch`

Target: `khronos/src/active_window/active_window.cpp`

Combines configured dynamic semantic labels with Khronos's geometric
`dynamic_image` before static TSDF integration. This prevents Human pixels from
becoming static geometry after geometric tracking is lost.

### `0002-promote-dynamic-semantic-clusters.patch`

Targets `connected_semantics.h/.cpp`.

Promotes connected components carrying configured dynamic labels into the
existing dynamic measurement stream and avoids duplicates with substantially
overlapping geometric dynamic clusters.

### `0003-preserve-promoted-dynamic-semantics.patch`

Target: `max_iou_tracker.cpp`.

Allows a promoted dynamic observation to initialize/update the track semantic
label while preserving the original rule for semantics-free geometric motion.

### `0004-accept-semantic-dynamic-tracks.patch`

Targets `mesh_object_extractor.h/.cpp`.

Optionally accepts a semantically dynamic track even when its measured
displacement is below the original displacement threshold.

All four extensions are opt-in/config-controlled where applicable; the source
patches document the exact changes from Khronos.

## Panoptic-Derived Portable Logic

`session_update_baseline/ports/panoptic_core/`

### `tsdf_conflict_checker.hpp/.cpp`

Adapts Panoptic Mapping's `TsdfRegistrator::submapsConflict()` predicate behind
a ROS-independent `DistanceQuery` interface. It retains:

- free-space conflict tests;
- non-free-space TSDF conflict and match tests;
- class-consistent persistent transitions;
- absent transitions on conflict;
- weighted acceptance/rejection thresholds.

This is reusable evidence logic, not the full ROS1 Panoptic mapper.

## Map Export, Audit, and Visualization

### `.4dmap` mesh and trajectory export

`session_update_baseline/app/export_4dmap_mesh_ply.cpp`

Exports the global mesh, optional valid private object meshes, robot agent
poses, and trajectory-start metadata. Object meshes are combined only for
display when requested; this does not alter evaluator input.

### Error audit

`session_update_baseline/app/audit_base1_mesh_errors.cpp`

Measures geometric errors and their overlap with object bounding boxes.

### A/B process generation

`session_update_baseline/scripts/prepare_office_ab_process_visualization.py`

Generates A and B map checkpoints, runs reconciliation at each B checkpoint,
exports display geometry, and creates the sequence manifest.

### Dense playback

`session_update_baseline/scripts/densify_office_ab_manifest.py`

Creates a dense playback timeline while holding the latest real map checkpoint;
it does not synthesize intermediate geometry.

### Latest viewer

`session_update_baseline/rounds/khronos_office_reversed_ab_30s_20260730/`
`process_visualization_semantic_unified_v5_reobservation/view_process.py`

Displays:

- 0 -> Session A -> Session B map evolution;
- A history and current reconciled geometry;
- A and B robot trajectories and sensing envelopes;
- dynamic trajectories, temporal boxes, and point frames;
- synchronized prior/current RGB sensor views.

## NSS/Data Adaptation Utilities

The following scripts support the separate dataset-construction track:

- `render_nss_textured_flat_rgb.py`: render virtual flat RGB-D observations;
- `generate_nss_ade20k_masks.py`: generate semantic masks;
- `refine_nss_construction_masks.py`: construction-scene mask refinement;
- `stabilize_nss_semantic_masks.py`: temporal label stabilization;
- `nss_flat_ros2_player.py`: ROS2 input player;
- `run_nss_khronos_session.sh`: Khronos session runner;
- `validate_nss_khronos_semantics.py`: semantic/input validation.

These utilities are relevant to future real A/B evaluation, but the latest
Office proof-of-pipeline should not be confused with a completed NSS benchmark.

