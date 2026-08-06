# Self-Fetched Full-Text Audit: Core D3 Methods

Status checked: **2026-08-07**

This audit records five papers independently acquired from their official or
author-hosted full PDFs and read across the problem statement, assumptions,
representation, method equations, experiments, figures, conclusion, and stated
limitations. The classifications below use the project's strict hierarchy:

```text
D1 = motion observed and retained as trajectory/time-indexed geometry
D2 = hidden change during an observation gap in the same running session
D3 = a completed prior session provides state to an independent later session
```

These papers are primarily D3 methods. None transfers a complete dense D1+D2
scene state across sessions.

## 1. Panoptic Multi-TSDFs

**Paper:** *Panoptic Multi-TSDFs: A Flexible Representation for Online
Multi-Resolution Volumetric Mapping and Long-Term Dynamic Scene Consistency*
(ICRA 2022).

### Actual task and assumptions

The method receives externally estimated camera poses and panoptic labels. It
represents a scene as a collection of volumetric submaps rather than one global
TSDF. Submaps may represent objects, background regions, or free space. Each
submap stores a TSDF and semantic/instance information and is either active or
inactive.

Objects are treated as the minimal change unit. The paper explicitly states that
short-term dynamic-object tracking could be added, but is left for future work.
Thus the representation is designed for long-term consistency, not for retaining
D1 motion histories.

### Change state

Inactive submaps are assigned one of three states:

```text
persistent
unobserved
absent
```

The decision uses current surface matches and free-space conflicts. A prior
object that is outside current reliable observation remains `unobserved`; an
object contradicted by current free space becomes `absent`; matched content is
`persistent`.

### Session protocol and experiments

The Flat dataset contains two robot runs with objects moved, added, and removed
between the runs. The second run is evaluated from a prior map created during the
first run. This is a genuine D3 prior/current protocol.

### Correct relationship to the project

```text
D1: no
D2: no under the strict same-running-session definition
D3: yes, dense object/submap representation and update
```

It is a central D3 representation baseline because it explicitly preserves
`unobserved` prior entities. It does not preserve trajectories or time-indexed
geometry and does not make every new session a full D1+D2 dynamic SLAM process.

### Manuscript-safe conclusion

Panoptic Multi-TSDFs provides an important dense volumetric D3 state model. Its
`persistent/absent/unobserved` semantics are existing work and cannot be claimed
as new. The missing capability relative to the target is the continuation of a
complete D1+D2 dynamic scene model.

## 2. POCD

**Paper:** *POCD: Probabilistic Object-Level Change Detection and Mapping in
Semi-Static Environments* (RSS 2022).

### Actual task and assumptions

POCD focuses on bounded rigid indoor objects whose state changes between robot
traversals, potentially while the robot is offline. It assumes:

- externally supplied robot poses;
- object semantic type and approximate dimensions;
- additions, removals, and planar object motion between traversals;
- object detections/segments used to construct object TSDFs.

The output is a current dense semantic map composed of object-level volumes.

### Object state and inference

Each object stores a pose, point cloud, TSDF, bounding box, semantic class, and a
joint Gaussian--Beta belief:

- a Gaussian variable models geometric change magnitude;
- a Beta variable models stationarity.

Data association uses semantic compatibility, centroid distance, ICP-based
geometric alignment, and Hungarian assignment. The paper does not require
association across very large displacements.

A particularly important detail is its handling of a previous object that lies
in the current view but receives no associated observation. The implementation
assigns a large pseudo-change measurement to drive the stationarity estimate
toward removal. The paper calls these objects `unobserved`, but operationally the
state is used as evidence for disappearance. This differs from the project's
strict requirement that lack of reliable observation must be preserved as
`unobserved` rather than converted into absence.

### Dynamic-object experiment

The toy-car experiment does not provide explicit D1 tracking. The moving object
is repeatedly erased and reconstructed, and the discussion states that
incremental dynamic object-pose tracking is not part of the current method and is
future work.

### Correct relationship to the project

```text
D1: no retained dynamic trajectory/history
D2: no; its principal changes are between traversals
D3: yes, object-level semi-static mapping with probabilistic stationarity
```

### Manuscript-safe conclusion

POCD is a major D3 object-belief baseline. Gaussian--Beta change/stationarity
beliefs, object TSDFs, and probabilistic semi-static update are existing
mechanisms. Its visible-but-unmatched removal rule should be contrasted with an
explicit observability model rather than described as equivalent to the
project's `unobserved` semantics.

## 3. POV-SLAM

**Paper:** *POV-SLAM: Probabilistic Object-Oriented Variational SLAM in
Semi-Static Environments* (RSS 2023).

### Actual task and assumptions

POV-SLAM extends semi-static object reasoning into the SLAM estimation problem.
It assumes bounded rigid objects, semantic class and approximate dimensions,
objects that may be added, removed, or shifted between traversals, and enough
unchanged structure to support localization.

### State and optimization

The map contains object poses, TSDFs, bounding boxes, semantic labels, object
landmarks, and Beta-distributed consistency variables. The factor graph uses a
Gaussian--Uniform mixture likelihood to model whether object observations are
consistent with the map. Variational EM jointly estimates robot poses and latent
object-consistency variables.

An optional dynamic-object motion model is discussed and tested in simulation,
but the principal system and real experiments address semi-static object
consistency rather than preserving complete D1 histories.

### Session protocol and experiments

A real-world experiment concatenates two trajectories captured four months
apart, thereby introducing object changes between visits. The method is a real
SLAM estimator, unlike POCD's externally localized mapping pipeline, and shows
that object consistency can improve robot localization. The reported real-time
operation is roughly 1 Hz, with variational inference triggered periodically.

### Correct relationship to the project

```text
D1: optional/limited model, not complete retained dynamic history
D2: no explicit same-session hidden-change output
D3: yes, joint pose and semi-static object consistency over repeated visits
```

### Manuscript-safe conclusion

POV-SLAM is a strong D3 probabilistic SLAM baseline. Joint pose/object
consistency and latent stationarity are existing ideas. It does not export and
restore a dense D1+D2 spatio-temporal map across independent sessions.

## 4. LT-Mapper

**Paper:** *LT-Mapper: A Modular Framework for LiDAR-Based Lifelong Mapping*
(ICRA 2022).

### Actual task and pipeline

LT-Mapper is a modular LiDAR lifelong-map framework with three components:

1. LT-SLAM for multi-session alignment;
2. LT-removert for removal of highly dynamic points;
3. LT-map for positive/negative change detection and map update.

High-dynamic points are removed before inter-session comparison. A central map
and query sessions are aligned through inter-session loop closures.

### Change representation

The method distinguishes:

- positive differences: newly appeared geometry;
- negative differences: disappeared geometry.

Negative differences are split into strong and weak evidence. Weak negatives can
be reverted to reduce false deletion caused by occlusion or insufficient
coverage. This is an important observability safeguard, although it is not an
explicit object-level `unobserved` belief.

The system maintains meta/live maps and a delta representation. The live map is
updated by removing negative changes and adding positive changes to the
high-dynamic-cleaned session map.

### Correct relationship to the project

```text
D1: no; moving content is removed
D2: no
D3: yes, geometric multi-session map alignment and revision
```

### Manuscript-safe conclusion

LT-Mapper is a central current-map-maintenance baseline. Multi-session alignment,
positive/negative differences, live/meta maps, and occlusion-aware negative
change filtering are existing mechanisms. It does not retain dynamic-object
history or continue a D1+D2 scene model.

## 5. ObVi-SLAM

**Paper:** *ObVi-SLAM: Long-Term Object-Visual SLAM* (IEEE RA-L 2024).

### Actual deployment protocol

ObVi-SLAM explicitly separates operation into two phases:

1. online visual SLAM during a deployment;
2. long-term object-map extraction after the deployment.

The long-term object map from a previous deployment is inserted as a prior in
the next deployment's factor graph. This is a genuine recursive D3 prior
mechanism.

### Assumptions and representation

The method assumes:

- known initial pose for each deployment;
- configured classes of static objects;
- class-specific object-dimension priors.

The persistent map is an uncertainty-aware set of static object ellipsoids used
for long-term localization. After a deployment, the full trajectory is refined,
nearby same-class objects are merged, visual features and robot poses are
marginalized, and the object map is sparsified before use in the next deployment.

### Limitation relevant to this project

The map is designed around static object landmarks. The paper lists object-based
change detection and stale-object removal as future work. It does not retain a
dense background map or moving-object trajectories.

### Correct relationship to the project

```text
D1: no
D2: no
D3: yes, explicit deployment-indexed object prior and re-extraction
```

### Manuscript-safe conclusion

ObVi-SLAM already demonstrates an uncertainty-aware, serialized, recursive
object prior across deployments. Therefore save/load, deployment-indexed priors,
and post-session sparsification are not novel by themselves. Its persistent
state is restricted to static object landmarks and does not contain dense
structural geometry or a D1+D2 scene history.

## 6. Cross-paper comparison

| Method | Persistent representation | D1 history | Same-session D2 | D3 prior/update | Key distinction |
|---|---|---:|---:|---:|---|
| Panoptic Multi-TSDFs | active/inactive object TSDF submaps | no | no | yes | explicit persistent/absent/unobserved |
| POCD | object TSDF + Gaussian--Beta belief | no | no | yes | stationarity/change belief; external poses |
| POV-SLAM | object map + latent consistency factor graph | limited optional | no | yes | joint pose/object variational inference |
| LT-Mapper | point maps + live/meta/delta changes | no | no | yes | large-scale geometric map revision |
| ObVi-SLAM | uncertainty-aware static object ellipsoids | no | no | yes | explicit recursive deployment prior |
| Project target | dense structure + objects + temporal history | yes | yes | yes | every independent session resumes complete D1+D2 |

## 7. Updated novelty boundary

These five papers strengthen the evidence that D3 already contains mature
mechanisms for volumetric state, object stationarity, joint pose/object
consistency, geometric map revision, and recursive deployment priors. They do not
show a system that transfers a complete dense D1+D2 dynamic scene state into an
independently initialized later session.

No universal-negative claim is authorized yet. The remaining direct core PDFs
must still be acquired and audited before the novelty wording is frozen.
