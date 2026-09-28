# Full-Text Correction Audit: SuperMap, DYMRO-SLAM, and ELite

Status checked: **2026-08-07**

This note corrects earlier overstatements caused by mapping paper-title language
(`spatio-temporal`, `persistent`, `lifelong`) directly onto this project's
D1/D2/D3 taxonomy. All three uploaded PDFs were read across the problem
statement, method, experiments, figures, and limitations.

## Canonical project taxonomy

```text
D1 = observed motion inside one running session
D2 = hidden change while the same session remains active
D3 = completed Session A exports memory; independent Session B imports it,
     reconciles inter-session change, and again runs D1+D2
```

## 1. SuperMap (RSS 2026)

### What the paper actually solves

SuperMap is a real-time **continuous-stream**, open-vocabulary semantic SLAM and
navigation system. Its formal input is one RGB-D or point-cloud video sequence
indexed by `t=1,...,T`. At each time step it estimates pose, instance IDs, and an
updated object map:

```text
P(I_t, M_t, P_t | M_{t-1}, Q_t)
```

The system has three layers:

1. a geometric layer using SuperOdometry for pose and colorized dense point-cloud
   reconstruction;
2. an instance layer for 2D/3D tracking-by-detection, instance association,
   point-level geometric consistency, and Bayesian label fusion;
3. a scene-graph layer for spatial and temporal relations and language queries.

Its point-level geometric update uses three states derived from depth residuals:
`Observable`, `Unobservable`, and `Disappeared`. Contradicted/dynamic object
points are penalized and pruned from the global map. Temporal edges store the
associated object's centroid-level trajectory/identity history.

### What it does not do

- It does not define completed Session A / independent Session B serialization or
  restoration.
- It does not preserve dense D1 object geometry and full trajectories in the
  Khronos sense. The paper's own limitations state that tracking highly dynamic
  objects remains limited.
- It does not formulate D2 as the full dense metric-semantic reconciliation of
  objects and structural surfaces.
- Its dense geometric reconstruction is a SLAM backbone used to ground the
  semantic object map; the paper's main evaluated product is the instance map,
  scene graph, and VLN interface.

### Experiment correction

The change experiment is a **10-minute** continuous run in a 30 m x 20 m indoor
area with three removed and three added objects. An earlier note incorrectly read
the figure label `2Hz Walkaround Video` as a two-hour deployment. That claim is
false and must not appear anywhere in the manuscript or audits.

### Correct relationship to this project

SuperMap is relevant as an online object-centric D2-like semantic map and as a
source for instance association, label confidence, object existence, and
queryable temporal relations. It is **not a close D3 predecessor** and is not a
primary threat to process-separated persistent dense SMS. Its closest overlap is
continuous-session semantic object maintenance, not cross-session continuation.

**Correct coverage:** D1 weak/limited object tracking; object-level D2-like
appearance/disappearance/relocation in one continuous stream; D3 no.

## 2. DYMRO-SLAM (IEEE Access 2025)

### What the paper actually solves

DYMRO-SLAM is an ORB-SLAM3-based stereo visual localization system for dynamic
inputs. It adds:

- Mask R-CNN masks to remove features on dynamic target classes;
- feature-point tracking on keyframes;
- optical-flow tracking on non-keyframes to reduce descriptor computation.

Only static features are used for pose estimation and map construction. The
paper evaluates camera ATE/APE and runtime on TUM, EuRoC, and a self-recorded
laboratory sequence.

### What it does not do

- no retained dynamic-object map;
- no D1 trajectory or time-indexed geometry for moving entities;
- no D2 hidden-change reasoning;
- no D3 multi-session memory;
- no object existence, identity, stationarity, or scene-history state.

### Correct relationship to this project

DYMRO-SLAM belongs only to the broad **dynamic-robust localization/static-map
cleaning** family. It is not a meaningful novelty neighbour and should not appear
in the main Related Work unless a compact sentence groups dynamic-feature
filtering systems. It must not be confused with **DYNEMO-SLAM**, the separate 3D
scene-graph preprint.

**Correct coverage:** dynamic observations rejected; D1 history no; D2 no; D3 no.

## 3. ELite (ICRA 2025)

### What the paper actually solves

ELite is a LiDAR point-cloud lifelong-map maintenance framework. Each session is
a set of scans and poses. It performs:

1. multi-session alignment to the existing lifelong point map;
2. point-wise local-ephemerality estimation by ray evidence and removal of
   dynamic points to create a cleaned session map;
3. point-level cross-session map update and global-ephemerality estimation.

The lifelong map stores `(x,y,z,epsilon_g)` for each point. Local ephemerality
`epsilon_l` is the probability that a point is dynamic **within the current
session**. Global ephemerality `epsilon_g` is its long-term probability of being
transient across sessions. The update partitions points into coexisting,
deleted, emerged, previously explored, and newly explored categories. ELite
outputs a lifelong point map, a thresholded static map, and a delta map.

### Critical taxonomy correction

ELite's `local/global` hierarchy is **not equivalent to our D1/D2/D3 hierarchy**:

- `epsilon_l` is a dynamic-versus-static score used to remove current-session
  moving points. It does not distinguish D1 observed trajectories from D2 hidden
  transitions.
- `epsilon_g` is a D3 point-level transiency score for lifelong map maintenance.
- The system discards D1 dynamic points instead of preserving their identity,
  trajectories, bounding boxes, or temporal geometry.
- It has no object-level D2 identity association and no explicit dense
  absent-versus-unobserved state for objects and structural patches.

### Correct relationship to this project

ELite is a strong **D3 geometric lifelong-map baseline/component**, particularly
for point-wise ray evidence, session alignment, recursive ephemerality, and
lifelong/static/delta map outputs. It does not propose the same three-part dynamic
problem and does not threaten the D1+D2 session model. Its overlap is limited to
the cross-session map-update side.

**Correct coverage:** current-session dynamic removal; D1 history no; D2 no;
D3 yes at point-map maintenance level.

## Corrected ranking of relevance

```text
Khronos             very high: dense single-session D1+D2 base
Panoptic / POCD      high: dense/object D3 state and update
ELite                medium-high: point-level D3 alignment/update baseline
SuperMap             medium: continuous semantic object map and D2-like updates
DYMRO-SLAM           low: dynamic-robust localization only
```

## Manuscript consequences

1. Remove the false `two-hour SuperMap deployment` statement.
2. Do not present SuperMap as a major process-separated novelty threat.
3. Describe ELite as point-level D3 lifelong map maintenance, not as an existing
   version of the complete D1+D2-over-D3 problem.
4. Keep DYMRO-SLAM out of the main Related Work.
5. Do not claim that the taxonomy itself is new solely because of these papers;
   however, also do not weaken the paper as if SuperMap or ELite already solved
   the complete problem.
6. The closest problem decomposition remains:

```text
Khronos: D1 + D2 inside one dense session
Panoptic / POCD / ELite: different D3 map-update mechanisms
Ours: make complete dense D1+D2 sessions persist and recur across D3
```
