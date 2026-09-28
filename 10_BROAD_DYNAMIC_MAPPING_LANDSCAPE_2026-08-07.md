# Broad Dynamic-Mapping Literature Landscape

Status checked: **2026-08-07**

This document is a high-recall research map, not a claim that every publication
has been found. Technical claims in the manuscript require a separate full-text
audit.

## Authoritative hierarchy

```text
D1 + D2 = dynamic mapping inside each continuously running session
D3      = persistent scene continuation across completed independent sessions
```

Paper-title words such as `dynamic`, `persistent`, `spatio-temporal`, and
`lifelong` do not determine the classification. The actual input protocol,
retained state, and evaluation must be inspected.

## 1. Dynamic-robust localization and static-map cleaning

These methods remove moving content to improve localization or construct a clean
static map. They are not D1 history systems.

Representative work:

- DynaSLAM, DS-SLAM, ReFusion;
- DYMRO-SLAM: Mask R-CNN feature rejection plus optical-flow/feature tracking;
- Dynablox and Volumetric Beliefs;
- NID-SLAM, DDN-SLAM, DVN-SLAM;
- WildGS-SLAM and Gassidy.

**Correct positioning:** useful tracking/static-map baselines. They do not retain
moving-object trajectories, hidden changes, or cross-session scene memory.

## 2. Explicit rigid-object D1 mapping

These systems preserve entities moving while observed:

- Co-Fusion and MaskFusion: per-object surfel models;
- MID-Fusion: per-object octree volumes;
- EM-Fusion: object SDFs and probabilistic association;
- VDO-SLAM, DynaSLAM II, and DynoSAM: joint camera/object states;
- DYNEMO-SLAM and Dynamic Situational Graphs: dynamic entities in scene graphs;
- Lost & Found: observed human-object interactions and transformable scene graph.

**Correct positioning:** strong D1 history methods. They do not become D2 or D3
without an observation-gap or completed-session protocol.

## 3. Non-rigid and video-level 4D reconstruction

Representative work:

- DynamicFusion, VolumeDeform, SurfelWarp;
- 4DTAM;
- 4D Primitive-Mache;
- 4DSurf, DynamicVGGT, Any4D, SLARM, MotionScale.

These methods may use `persistent` to mean object permanence or a replayable
representation inside one continuous video. That is not process-separated D3.

## 4. Single-session D2 and unified D1+D2

Representative work:

- Bore et al.: local motion and global jumps under partial observation;
- Changing-SLAM: sparse dynamic filtering and object persistence in continuous
  sequences;
- Khronos: dense D1 active window plus D2 global reconciliation;
- GaME: online Gaussian map revision after out-of-view changes;
- LTC-Mapping: object visibility, detection, and non-detection evidence;
- SuperMap: continuous-stream open-vocabulary object map and scene graph.

### Correct SuperMap interpretation

SuperMap processes one RGB-D or point-cloud sequence `t=1,...,T` and recursively
updates pose, instance IDs, and an object map. Its point evidence is
`Observable`, `Unobservable`, or `Disappeared`, and its scene graph stores
spatial/temporal relations. The evaluated addition/removal experiment is a
**ten-minute continuous run**, not a two-hour deployment. It is relevant to
semantic instance maintenance and object-level D2-like updates, but it does not
provide dense D1 histories or completed-session D3 continuation.

## 5. Cross-session geometric map maintenance (D3)

Representative work:

- Dynamic Pose Graph SLAM;
- Pomerleau et al. long-term point-map maintenance;
- Efficient Long-Term Mapping;
- LT-Mapper;
- RBIF;
- Lifelong 3D Mapping Framework;
- SLAM-RAMU and LLMF;
- ELite;
- ProbPer-LiLo.

### Correct ELite interpretation

ELite processes each session as LiDAR scans and poses. It aligns the session,
estimates local point ephemerality, removes dynamic points, and updates global
point ephemerality in a lifelong map. Its local/global scores are not D1/D2:
local ephemerality is a dynamic-removal score, while global ephemerality is a D3
transiency score. ELite is a strong point-level D3 baseline, not the same
three-part scene-memory problem.

## 6. Cross-session object, volumetric, and scene-graph memory

Representative work:

- Panoptic Multi-TSDFs;
- POCD and POV-SLAM;
- ObVi-SLAM;
- Living Scenes;
- OASIS-Map;
- 3D Variable Scene Graph;
- Scene Graph Memory and incremental object-search scene graphs.

This family is central to object existence, association, semantics, and
persistent submaps. Many systems omit dense background/structural updates or D1
history.

## 7. Predictive and periodic dynamic maps

Representative work:

- occupancy-grid HMMs for changing environments;
- FreMEn;
- Spatio-Temporal and Bayesian Hilbert Maps;
- temporal exploration and map prediction;
- Perpetua persistence/emergence filters.

These are mainly mathematical sources for uncertainty, recurrence, and active
re-observation rather than direct mesh/TSDF baselines.

## 8. Gaussian representatives

The manuscript should keep approximately six or seven papers with distinct
roles:

1. WildGS-SLAM - dynamic-robust static Gaussian map;
2. 4DTAM - non-rigid D1 tracking/mapping;
3. 4D Gaussian Splatting SLAM - explicit D1 dynamic Gaussian SLAM;
4. DynaGSLAM - online D1 mapping and motion prediction;
5. GaME - continuous-session D2 evolving Gaussian map;
6. LT-Gaussian - D3 old-map/current-traversal revision;
7. GS-LTS - optional D3 semantic editor, clearly marked as a preprint.

Other Gaussian systems remain in the internal audit because their outputs and
metrics are not directly comparable to metric-semantic mesh/scene memory.

## 9. Correct closeness ranking

```text
Very high:
  Khronos                     dense single-session D1+D2
  Panoptic / POCD / POV       dense or object-level D3 state/update

High:
  ELite                       point-level D3 alignment/update
  ProbPer-LiLo                probabilistic multi-session persistence
  OASIS-Map                   object-level cross-session correspondence

Medium:
  SuperMap                    continuous semantic object mapping and change
  LTC-Mapping                 visibility/non-detection object maintenance
  DYNEMO-SLAM                 scene-graph D1/displaced-object representation
  GaME / LT-Gaussian          representation-adjacent D2/D3

Low for the core scene-memory problem:
  DYMRO-SLAM and similar      dynamic-feature rejection/localization
```

## 10. Current safe positioning

The literature is best understood as two adjacent families:

```text
Khronos and dynamic/4D methods:
  rich D1+D2 capabilities inside a continuous session

Panoptic, POCD/POV, ELite, and lifelong mappers:
  cross-session D3 map maintenance without complete D1 history
```

The target gap is to make complete dense D1+D2 session state persist and recur
across D3, while updating both objects and structural geometry.
