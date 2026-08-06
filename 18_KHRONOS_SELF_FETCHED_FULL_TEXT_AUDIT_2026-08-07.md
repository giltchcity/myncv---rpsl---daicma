# Khronos — Self-Fetched Full-Text Audit

Status: **COMPLETE, 2026-08-07**

Source: official arXiv PDF `https://arxiv.org/pdf/2402.13817`, version 2, 13
pages. The PDF states that the paper was published at Robotics: Science and
Systems 2024.

This is the first paper independently acquired by the assistant and read through
the complete main text under the repository audit protocol.

## 1. Identity

- **Title:** Khronos: A Unified Approach for Spatio-Temporal Metric-Semantic
  SLAM in Dynamic Environments
- **Authors:** Lukas Schmid, Marcus Abate, Yun Chang, Luca Carlone
- **Venue:** Robotics: Science and Systems 2024
- **Primary source:** arXiv:2402.13817v2

## 2. Actual problem and temporal protocol

Khronos defines Spatio-Temporal Metric-Semantic SLAM over one continuously
indexed time sequence `t = 0, ..., T`. Each object state contains its surface,
pose, and semantic label, and the robot state contains all poses up to current
time `T`.

The objective is a MAP estimate of the states of the robot and scene at all
previous times `t <= T` from the observations and odometry collected in this one
running problem.

**Source:** Sec. III, Eqs. (1)--(7), PDF pp. 3--4.

The paper's short/long distinction is observational rather than session-based:

- short-term dynamics are continuously observed motion;
- long-term dynamics are abrupt changes inferred across observation gaps.

**Source:** Sec. IV, discussion after Eq. (16), PDF p. 5.

There is no completed Session-A serialization, independent Session-B import, or
Session-B-to-C recursion in the published formulation or experiments.

## 3. Inputs and assumptions

Inputs are:

- RGB-D measurements;
- semantic masks or open-set semantic regions;
- robot odometry, including loop-closure candidates supplied by the odometry
  input.

The formulation assumes spatio-temporal local consistency: pose-estimation error
and object change remain small inside a short temporal window `delta`, although
they may become large over longer intervals.

**Source:** Eqs. (8)--(9), PDF p. 4.

## 4. State and representation

The full conceptual state is:

- robot poses `X`;
- object states `O`, including the background as a static object;
- latent object fragments `Y`;
- fragment-to-object associations `A`.

The practical representation contains:

- a TSDF-derived dense mesh for the static background;
- private TSDF/mesh surfaces for static object fragments;
- sequences of point clouds for deformable and dynamic fragments;
- robot poses, mesh control points, and fragment poses in a deformation graph;
- a library/hash of representative free-space rays used during reconciliation.

**Source:** Secs. III--V, Eqs. (1)--(16), PDF pp. 3--6.

## 5. Main factorization

Khronos introduces fragments as the minimal temporal partition of observations
for which local consistency holds. This factorizes the SMS posterior into:

1. local fragment estimation;
2. global SLAM and fragment association;
3. fragment reconciliation into object histories.

The final factorization is Eq. (16):

```text
fragment reconciliation x SLAM/association x local estimation
```

**Source:** Sec. IV, Eqs. (10)--(16), PDF pp. 4--5.

## 6. Active-window estimation — D1

The active window:

- incrementally fuses the static background with projective TSDF fusion;
- obtains candidate object measurements from semantic masks and geometric
  motion detection;
- uses the cue that points occupying previously observed free space are dynamic;
- greedily associates observations to fragment hypotheses using volumetric IoU,
  semantic labels, and proximity;
- rejects weak hypotheses with fewer than 15 observations and dynamic
  hypotheses moving less than 1 m;
- represents static fragments with TSDF meshes and dynamic/deformable fragments
  with point-cloud sequences.

**Source:** Sec. V-A, PDF pp. 5--6.

This is the project's D1 base: continuously observed motion is retained as a
time-indexed fragment representation rather than simply removed.

## 7. Global optimization

The global module jointly optimizes:

- robot poses;
- fragment poses;
- dense background mesh control points;
- binary inlier/outlier weights for candidate loop closures and fragment
  associations.

Candidate fragment associations require matching semantics and overlapping
bounding boxes. The implemented association edge is translation-only between
fragment centroids; full 6-DoF surface registration is explicitly left for
future work.

Optimization uses a TLS robust pose-graph objective solved with GNC in GTSAM.

**Source:** Sec. V-B, Eq. (17), PDF pp. 6--7.

## 8. Reconciliation — D2

Fragments contain positive presence observations but no negative evidence.
Khronos explicitly addresses evidence of absence versus absence of evidence by
querying fragment surface points against a deformable library of background
observation rays.

For a query point:

- a reference vertex closer than the query indicates that the query was behind
  a surface/occluded;
- a query near the reference vertex indicates presence/geometric consistency;
- a ray passing through the query before reaching the reference vertex indicates
  evidence of absence.

An absence timestamp is accepted only when at least 60 percent of the rays in a
5-second temporal window agree. Appearance/disappearance time is then estimated
as the midpoint between the last reliable empty/presence evidence and the first
opposite observation.

**Source:** Sec. V-C, Eqs. (18)--(19), Figs. 5--6, PDF pp. 7--8.

Important nuance: this is an object-history estimate inside one continuous
sequence. It is not an explicit persistent/absent/unobserved/new state machine
exported across independent process sessions.

## 9. Experiments

### Synthetic datasets

The paper constructs two TESSE sequences because no existing annotated dataset
contains both forms of dynamics in one sequence:

- Apartment: 87 s, 39 m, 64 static objects, 10 dynamic objects, 6 long-term
  object changes;
- Office: 217 s, 181 m, 196 objects, 6 dynamic objects, 8 long-term changes.

Dynamic entities include people and a bouncing football; changed items include
furniture and small household objects.

### Real-world validation

The paper additionally evaluates:

- a Clearpath Jackal with a Realsense D455;
- a Boston Dynamics Spot in a university building.

The real experiments contain humans/items moving while visible and orchestrated
object additions/removals between robot observations. These remain continuous
robot runs rather than process-separated sessions.

### Metrics and baselines

It evaluates background, static objects, dynamic objects, and change detection
using precision/recall/F1 and introduces a 4D metric integrated over robot time
and belief time. Baselines are Hydra, Dynablox, and Panoptic Mapping, each
covering only a subset of the SMS task.

**Source:** Sec. VI, Eq. (20), Tables I--III, Figs. 7--9, PDF pp. 7--11.

## 10. Runtime

- active window: `45.5 +/- 9.2 ms`, approximately 22.2 FPS;
- fragment extraction and global mesh deformation usually below 1 s;
- loop-closure optimization may take several seconds but runs asynchronously;
- change detection and reconciliation are generally below 100 ms for all scene
  fragments.

**Source:** Sec. VI-F, PDF p. 11.

## 11. Limitations

The paper explicitly identifies:

1. centroid/bounding-box-based association is sensitive to partial observations
   and occlusions;
2. no full 6-DoF registration between fragments;
3. geometrically moved fragments are not associated, limiting detailed moved
   object history;
4. ray-based change detection needs reference surfaces and may fail in large
   sparse/open spaces;
5. all fragments are retained, causing unbounded growth; marginalizing resolved
   fragments is left as a requirement for lifelong missions.

**Source:** Sec. VII, PDF p. 11.

## 12. Correct D1/D2/D3 classification

```text
D1: YES
    visible dynamic fragments, trajectories/time-indexed point-cloud geometry

D2: YES
    same-running-sequence hidden changes inferred through fragment association
    and deformable ray-based presence/absence evidence

D3: NO in the published paper
    no process-separated completed-A export, independent-B restore, or B-to-C
    recursive continuation protocol
```

## 13. Relationship to this project

Khronos is not merely related work; it is the direct single-session technical
base. The project cannot claim D1, D2, dense SMS, fragments, active/global
factorization, deformable background optimization, or ray-based reconciliation
as new.

The remaining project question is specifically what state and inference must be
persisted across process-separated Session boundaries so that a later independent
run can resume the complete Khronos D1+D2 problem, update object and structural
current geometry, and export the next prior.

## 14. Claims this paper rules out

Do not claim:

- first dense system combining visible motion and out-of-view change;
- first fragment-based unification of short- and long-term dynamics;
- first ray-based distinction between absence evidence and missing evidence;
- first dense time-indexed metric-semantic scene representation;
- first active-window/global-reconciliation architecture.

The only defensible extension must be explicitly cross-session and must go beyond
software save/load by preserving the information required for continued
inference.
