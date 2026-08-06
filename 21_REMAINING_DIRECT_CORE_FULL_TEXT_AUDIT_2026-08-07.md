# Remaining Direct-Core Full-Text Audit

Status checked: **2026-08-07**

This file records the completion of the twelve papers previously fixed as the
remaining direct-core queue. The classification follows the project taxonomy:

```text
D1 = continuously observed motion inside one running session
D2 = hidden change while the same session remains active
D3 = change across completed independent sessions and transfer of persistent state
```

A paper is not classified from its title. Each entry below records the temporal
protocol, inputs, state/representation, actual update mechanism, experiments,
limitations, and the precise overlap with the project.

## 1. LTC-Mapping

**Paper:** J.-L. Matez-Bandera et al., *LTC-Mapping, Enhancing Long-Term
Consistency of Object-Oriented Semantic Maps in Robotics*, Sensors 2022.

**Source:** full 16-page open-access PDF, DOI `10.3390/s22145308`.

### Actual problem and protocol

LTC-Mapping incrementally maintains an object-oriented semantic map from a
single stream of RGB-D images. The camera pose is assumed known; the paper uses
AMCL to obtain the robot/world pose. The evaluation trajectory is followed twice
in succession and selected objects are moved during the second lap. There is no
completed-Session-A serialization and independent Session-B restoration.

### Representation and method

Each object is a 3D Z-oriented bounding box augmented with:

- pose and size;
- per-class confidence scores;
- visibility flags for bounding-box vertices;
- an accumulated observation count.

The pipeline performs object detection/modeling, data association, integration,
and maintenance. Vertex visibility is used to distinguish partial observations
and prevent duplicate object instances. For mapped objects expected to appear in
the current image, a missing detection generates a `non-detection` observation.
Repeated non-detections increase the `Other` class confidence; an object is
removed when `Other` becomes its dominant class.

### Experiments and limits

Experiments use six Robot@VirtualHome environments. Each path is traversed twice;
objects are repositioned in the second lap. Metrics include object classification
accuracy/F1, 3D IoU, position error, and runtime. The pipeline runs at roughly
2 Hz and assumes known poses. Structural elements such as walls and active
perception are explicitly future work.

### Correct classification

```text
D1: no retained trajectory or temporal geometry
D2: object-level D2-like maintenance through expected visibility and repeated non-detection
D3: no process-separated session protocol
```

LTC-Mapping is a useful predecessor for visibility-aware object existence and
non-detection evidence. It does not perform SLAM jointly, does not retain D1, and
cannot update structural geometry.

---

## 2. GaME

**Paper:** N. Yugay et al., *Gaussian Mapping for Evolving Scenes*, CVPR 2026.

**Source:** complete official arXiv/CVF paper text.

### Actual problem and protocol

GaME maintains one global 3D Gaussian map while a posed RGB-D stream continues.
It targets rigid geometry added, moved, or removed outside the current view. Its
evaluation deliberately merges captures made before and after scene changes into
one continuous sequence, without telling the mapper when the scene changed.
Ground-truth poses are used in the main comparison; an external pose estimator is
examined separately.

### Representation and method

GaME does not maintain persistent object entities. It reduces evolving geometry
to two operations:

- **Add:** current depth lies in front of the model rendering, so new Gaussians
  are initialized from current observations;
- **Remove:** current depth rays contradict old Gaussians, so the contradicted
  Gaussians are removed.

It additionally masks changed regions in stale keyframes and removes keyframes
whose support has become obsolete, preventing old imagery from reintroducing
stale content during Gaussian optimization.

### Experiments and limits

The paper evaluates Flat, Aria, and static TUM-RGBD scenes using PSNR, SSIM,
LPIPS, and depth L1. It explicitly states that short-term dynamic objects are not
handled and that pose tracking is external. The output is the latest Gaussian
map rather than a complete 4D history.

### Correct classification

```text
D1: no
D2: yes, dense online representation update in one continuous process
D3: no export/import process-separated protocol
```

GaME is a strong representation-level D2 baseline, not a full D1+D2 SLAM system
and not a D3 continuation system.

---

## 3. OASIS-Map

**Paper:** *OASIS-Map: Object-Level Change Detection in Multi-Session Mapping
using Semantic Correspondence Matching*, arXiv 2026.

**Status:** under-review preprint as of 2026-08-07; no peer-reviewed venue is
claimed here.

**Source:** complete official arXiv paper text.

### Actual problem and protocol

OASIS-Map takes a previous completed session and a current ongoing session. All
poses from both sessions are already expressed in a common metric frame supplied
by a separate multi-session LiDAR SLAM system. The method builds an object map
for each session and associates objects between those maps.

### Representation and method

Per-session geometry is reconstructed using TSDF submaps or accumulated LiDAR
points. Object masks and dense semantic features are extracted from images.
The back-end computes dense DINO patch correspondences between co-visible
bi-temporal images, aggregates correspondences within object masks, and solves
one-to-one object association.

The final labels are:

```text
static / moved / appeared / disappeared / unknown
```

An unmatched object is only declared appeared/disappeared when at least half of
its 3D volume is covered by the other session; otherwise it remains `unknown`.

### Experiments and limits

The paper evaluates 3RScan, a car-park replacement sequence, and a market
sequence spanning days to months. It reports object detection/association and
change-label precision, recall, and F1. The system relies on external session
alignment and per-session object maps. It does not retain dynamic trajectories
or run a Khronos-style D1+D2 engine inside the current session.

### Correct classification

```text
D1: no
D2: no dedicated same-session hidden-change process
D3: yes, strong object-level association/change-state component
```

OASIS-Map makes cross-session object association, moved/appeared/disappeared
labels, and coverage-gated `unknown` existing work. It does not transfer a full
dense dynamic-SLAM state.

---

## 4. Living Scenes / MoRE2

**Paper:** L. Zhu et al., *Living Scenes: Multi-object Relocalization and
Reconstruction in Changing 3D Environments*, CVPR 2024.

**Source:** complete official arXiv/CVF paper and supplementary text.

### Actual problem and protocol

The input is a collection of 3D scans captured at irregular times and segmented
into object instances. Because captures are separated by long gaps, the authors
state that reconstructing intermediate motion is infeasible. The task is to
match object instances across scans, estimate their relative 6-DoF transforms,
and accumulate observations into more complete object reconstructions.

### Representation and method

MoRE2 uses one SE(3)-equivariant encoder-decoder representation for instance
matching, point-cloud registration, and implicit-shape reconstruction. A joint
optimization improves object pose and shape as more temporal scans are
accumulated.

### Experiments and limits

Evaluation uses synthetic FlyingShape and real 3RScan data. Metrics cover
instance matching, registration recall/rotation error/Chamfer distance, and
reconstruction quality. The method is post-processing, includes test-time
optimization, and is not real-time. It struggles with identical/symmetric
objects and incomplete rescans. It does not estimate robot poses or maintain a
dense background map.

### Correct classification

```text
D1: no; intermediate trajectories are explicitly not reconstructed
D2: no online same-session process
D3: offline object-level relocalization/reconstruction component
```

Living Scenes is relevant for cross-time identity, rigid object registration,
and cumulative object geometry, but it is not SLAM or persistent background
scene memory.

---

## 5. Dynamic Pose Graph SLAM

**Paper:** A. Walcott-Bryant et al., *Dynamic Pose Graph SLAM: Long-Term Mapping
in Low Dynamic Environments*, IROS 2012.

**Source:** complete 8-page author-hosted PDF.

### Actual problem and assumptions

DPG-SLAM focuses on low-dynamic indoor environments. High-dynamic objects are
assumed to have been filtered by other methods. The robot repeatedly traverses a
bounded environment, and the paper assumes environmental changes occur between
passes.

### Representation and method

A Dynamic Pose Graph node stores robot pose, change/active indicators, pass
number, and a laser scan divided into angular sectors. Scan points are labelled
`static`, `added`, or `removed`. The system maintains:

- an **active map** representing the most recent usable environment state;
- a **dynamic map** containing representative added/removed laser points as a
  history of detected changes.

Current pose-chain scans are compared with an old local submap. Change labels
turn stale scan sectors off; sufficiently stale nodes become inactive and may be
removed to bound graph complexity.

### Experiments and limits

Experiments include a Reading Room with boxes changed between passes and a
Tuebingen office sequence with many traversals over several weeks. The system is
2D laser based, can retain false positives/negatives, and lists 3D mapping,
semantics, and active maintenance planning as future work.

### Correct classification

```text
D1: no; high dynamics are filtered
D2: no; changes are assumed between passes
D3: yes, low-dynamic scan-level map/history maintenance
```

DPG-SLAM establishes that an active current map and a separate history of
added/removed geometry are not new. Its dynamic history is scan evidence, not
object identity or time-indexed D1 trajectories.

---

## 6. Pomerleau et al. 2014

**Paper:** F. Pomerleau et al., *Long-Term 3D Map Maintenance in Dynamic
Environments*, ICRA 2014.

**Source:** complete author-uploaded full paper text.

### Actual problem and method

The system registers incoming 3D LiDAR scans, maintains a global point map, and
estimates for each point a Bayesian dynamic/static probability. It is explicitly
point based and avoids object segmentation. Points classified as currently
dynamic are compared with dynamic points from the previous scan. Dual non-rigid
ICP estimates per-point translations; dividing by the acquisition interval gives
velocity, with a local smoothness filter.

The approach therefore combines two capabilities:

- repeated-survey point-map maintenance;
- instantaneous point-wise velocity estimation for currently moving content.

### Experiments and limits

Experiments include repeated surveys over multiple days with pedestrians, bikes,
and cars moving during runs and parked cars changing between runs. The map can be
thresholded into static/dynamic points and dynamic probability is used to reduce
ICP corruption. The authors report ambiguity for periodic objects such as trams
and cars repeatedly occupying parking spaces and state that higher-level object
models are needed. Velocity estimation also depends on scan rate and nearest
point assumptions.

### Correct classification

```text
D1: partial, point-wise velocity only; no object trajectory or identity
D2: no explicit hidden-transition state or object association
D3: yes, repeated-survey point-map probability update
```

This paper invalidates a broad claim of being first to combine dynamic tracking
and long-term map update. It does not preserve a dense semantic object history or
resume a complete D1+D2 scene model across sessions.

---

## 7. RBIF Map Maintenance

**Paper:** M. Breitfuss et al., *Long-Term Map-Maintenance in Changing
Environments using Ray-Bundle-Impact-Factor Estimation*, IROS 2024.

**Source status:** complete author-uploaded full-text rendering was read through
ResearchGate; KIT/DBLP metadata verified the venue and DOI
`10.1109/IROS58592.2024.10802029`. Direct PDF-byte retrieval was blocked by
ResearchGate rate limiting, so this source mode is explicitly recorded.

### Actual problem and method

RBIF continuously incorporates 3D LiDAR scans into an octree localization map.
Ray tracing assigns traversed voxels to `traversed-empty`, `traversed-occupied`,
or `hit`. Both ray bundles and map-voxel contents are modeled as multivariate
Gaussians. A normalized Kullback-Leibler-divergence construction estimates the
maximum interference between a ray bundle and an occupied voxel. The resulting
RBIF updates occupancy and geometry at sub-voxel precision; sigma-point
adjustment avoids destructive holes caused by discrete voxel updates.

### Experiments and limits

The paper evaluates static mapping, fast transient objects while the robot is
stationary, and a virtual scenario combining moving trucks with slow gravel-pile
deformation. It compares against two map-maintenance baselines and evaluates map
compliance and localization stability.

### Correct classification

```text
D1: no trajectory/history; moving objects only affect occupancy update
D2: no object-level hidden-change reasoning
D3: geometric map-maintenance component usable across repeated operation
```

RBIF is highly relevant to conservative geometric evidence and sub-voxel
add/delete updates. It does not maintain semantics, identity, object trajectories,
or a process-separated D1+D2 state.

---

## 8. 4D Gaussian Splatting SLAM

**Paper:** Y. Li et al., *4D Gaussian Splatting SLAM*, ICCV 2025.

**Source:** complete official arXiv/CVF paper text; formal ICCV status verified.

### Actual problem and method

The input is a continuous RGB-D sequence plus motion masks. Static and dynamic
Gaussians are initialized separately; sparse control points and an MLP model the
6-DoF deformation of dynamic Gaussians. Camera tracking renders only static
Gaussians, while mapping jointly optimizes poses, Gaussian attributes,
deformation, ARAP regularization, and optical-flow supervision.

A critical method restriction is that dynamic Gaussians/control points are
initialized from a selected initial frame. New keyframes add static Gaussians,
but new dynamic Gaussians are not inserted; for a dynamic object appearing later,
the initialization frame is manually preselected.

### Experiments and limits

Evaluation uses TUM RGB-D and BONN Dynamic RGB-D, with ATE and rendering metrics
PSNR/SSIM/LPIPS. The task is continuous-sequence tracking and 4D rendering.

### Correct classification

```text
D1: yes, explicit continuous dynamic Gaussian reconstruction
D2: no hidden-change/current-map state
D3: no independent-session memory transfer
```

It is an important D1 representation reference, not a D3 map-maintenance system.

---

## 9. 4DTAM

**Paper:** H. Matsuki et al., *4DTAM: Non-Rigid Tracking and Mapping via Dynamic
Surface Gaussians*, CVPR 2025.

**Source:** complete official arXiv/CVF paper and supplementary text.

### Actual problem and method

4DTAM jointly estimates camera ego-motion and non-rigid surface evolution from an
online RGB-D stream. It represents the canonical surface with 2D Gaussian
surface primitives and uses an MLP warp field for time-dependent deformation.
Tracking and mapping optimize camera poses, canonical Gaussians, and deformation
within a sliding window; optional global optimization finalizes the map.

### Experiments and limits

The paper introduces the synthetic Sim4D dataset and evaluates camera ATE,
depth, geometric precision/recall/F1, and rendering. It also includes real RGB-D
capture. The authors state that tests are mostly small scale, the current system
runs at about 1.5 fps, and complex real scenes may require point-track or optical-
flow priors.

### Correct classification

```text
D1: yes, non-rigid continuous 4D tracking and mapping
D2: no explicit hidden-transition reasoning
D3: no process-separated session continuation
```

4DTAM is a rich D1 reconstruction method, but it does not maintain a long-term
current-scene memory across independent deployments.

---

## 10. DynaGSLAM

**Paper:** R. B. Li et al., *DynaGSLAM: Real-Time Gaussian-Splatting SLAM for
Online Rendering, Tracking, Motion Predictions of Moving Objects in Dynamic
Scenes*, WACV 2026.

**Source:** complete official arXiv/CVF paper text; formal WACV status verified.

### Actual problem and method

The paper formulates time-varying Gaussian mapping from a continuous RGB-D
stream. Despite the title, localization and mapping are separated: the camera
trajectory is taken directly from DynoSAM without modification. The Gaussian
mapper uses RAFT flow and SAM2 masks, lifts optical flow to a dynamic 3D Gaussian
flow, associates/propagates dynamic Gaussians, and jointly renders static and
dynamic Gaussian sets. Dynamic Gaussians are pruned by observability and longevity
rules to control memory.

### Experiments and limits

It evaluates rendering, dynamic-region rendering, camera ATE, runtime, and memory
on three dynamic datasets. DynoSAM localization alone costs roughly 450 ms/frame;
the paper trades motion-model complexity for online operation. Because old
dynamic Gaussians are deleted, the representation is not an append-only long-term
history.

### Correct classification

```text
D1: yes, online moving-Gaussian representation and short-horizon prediction
D2: no explicit hidden-change reconciliation
D3: no independent-session state transfer
```

It is primarily a D1 Gaussian mapping component coupled to an existing dynamic
localizer.

---

## 11. 4D Primitive-Mache

**Paper:** K. Mazur et al., *4D Primitive-Mache: Glueing Primitives for
Persistent 4D Scene Reconstruction*, CVPR 2026.

**Source:** complete official arXiv/CVF paper text; formal CVPR status verified.

### Actual problem and method

The input is one casual monocular video. Each keyframe is decomposed into rigid
3D primitives. Dense 2D correspondences between adjacent keyframes constrain a
joint optimization of per-primitive rigid poses. Motion grouping, contact, and
velocity extrapolation maintain object permanence when previously observed
primitives become temporarily invisible. Time remapping produces a replayable
reconstruction at all observed timestamps.

### Experiments and limits

The paper evaluates object scanning, multi-object reconstruction, and object
permanence with geometric F-scores and related metrics. It explicitly assumes
rigid primitives and states that incremental mapping in which the representation
is built and updated over extended sequences has not been explored.

### Correct classification

```text
D1: yes, persistent/replayable within-video motion reconstruction
D2: only motion extrapolation inside one video, not evidence-based hidden scene change
D3: no
```

`Persistent` here means permanence within a continuous video, not a serialized
robot scene memory across independent sessions.

---

## 12. LT-Gaussian

**Paper:** H. Cheng et al., *LT-Gaussian: Long-Term Map Update Using 3D Gaussian
Splatting for Autonomous Driving*, IEEE IV 2025.

**Source:** complete official arXiv paper/PDF; formal IEEE IV status verified.

### Actual problem and method

LT-Gaussian takes an outdated multimodal Gaussian map and a current LiDAR
traversal. It extracts Gaussian centers as a point set, aligns the current LiDAR
submap by ICP, and applies kNN tests to identify emerging current points and
disappearing old Gaussian centers. Old Gaussians corresponding to disappearing
points are removed; emerging LiDAR points are initialized as new Gaussians using
nearby semantic/appearance priors. The modified old map becomes the initialization
for a short Gaussian refinement.

### Experiments and limits

A nuScenes revisit benchmark is constructed from old/new scene sequences. The
updated map is evaluated mainly through SSIM, PSNR, LPIPS, and update time against
reconstruction from scratch. The paper does not evaluate absent-versus-unobserved
classification, object identity, or dynamic trajectories. It is a pairwise
old-map/current-traversal update; recursive A-to-B-to-C memory is not established.

### Correct classification

```text
D1: no
D2: no single-session hidden-change engine
D3: yes, Gaussian map-revision component
```

LT-Gaussian is relevant as a representation-specific D3 updater, not as a full
long-term dynamic SLAM system.

---

# Consolidated conclusions from this queue

## Existing capabilities confirmed

The audited papers establish that the following are already present in prior
work:

- expected-visibility and repeated non-detection object maintenance;
- dense D2 Gaussian add/remove and stale-keyframe management;
- cross-session object labels including moved/appeared/disappeared/unknown with
  coverage gating;
- offline cross-time object matching, registration, and cumulative reconstruction;
- active current maps plus a separate history of added/removed scan geometry;
- repeated-survey point-level dynamic probability plus instantaneous velocity;
- probabilistic ray/voxel interference for conservative sub-voxel map updates;
- rich continuous D1 representations based on dynamic Gaussians, non-rigid
  surfaces, and rigid primitives;
- old-Gaussian-map/current-LiDAR revision.

## What these papers do not jointly provide

None of the twelve simultaneously provides:

1. retained D1 trajectories and time-indexed dynamic geometry;
2. explicit same-session D2 reasoning that separates lack of observation from
   evidence of absence;
3. a dense current map covering both objects and structural surfaces;
4. process-separated export/import of the complete scene state;
5. a new independent session that both reconciles D3 and resumes full D1+D2;
6. recursive output for a following session.

This is a finding about the explicitly audited direct-core set, not a universal
proof over all literature. It supports a narrow `to the best of our knowledge`
position only after the remaining citation-chain saturation check is completed.
