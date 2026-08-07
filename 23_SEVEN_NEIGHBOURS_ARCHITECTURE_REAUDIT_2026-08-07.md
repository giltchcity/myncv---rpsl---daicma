# Seven Additional Neighbours: Architecture-Axis Full-Text Re-Audit

Status: **COMPLETE, 2026-08-07**

This file records the architecture-focused re-audit of seven papers that were
identified after the original 28-paper verified corpus. Each complete primary
text was re-read using the canonical A -> D3 -> B -> C checklist rather than a
component-level novelty checklist.

These seven papers are now eligible for inclusion in the authoritative verified
count.

## Binding question

For every paper, the relevant question is:

```text
Session A
  complete D1 + D2
  -> export persistent scene state
  -> A terminates

D3
  inter-session change

Independent Session B
  -> import A state
  -> reconcile D3
  -> again execute new D1 + D2
  -> export equivalent state for Session C
```

A method does not solve this architecture merely because it performs dynamic map
updates, object association, Gaussian revision, ray deletion, relocalization, or
long-horizon memory maintenance.

---

## 1. CubifyGS

**Paper:** *CubifyGS: Object-Centric 3D Gaussian Splatting for Lifelong Dynamic
Scene Maintenance*  
**Status:** accepted to IROS 2026; arXiv:2606.28720v2.  
**Primary text:** complete arXiv HTML/PDF text re-read.

### Temporal protocol

The method takes a **continuous stream** of posed RGB-D observations. It maintains
an active object-centric Gaussian scene and a persistent global asset library.
The active scene is updated online as rigid objects appear, disappear, or are
rearranged.

### State

Each active object stores Gaussian geometry, a multi-view semantic feature bank,
and a gravity-aligned 3D bounding box. A global asset library stores reusable
canonical object templates.

The tracking module performs persistent identity association between current
proposals and active objects, and an existence probability is updated from
hit/free/occluded ray evidence.

### Architecture checklist

- **A/D1:** partial only. The method tracks object identity/current box state in a
  continuous stream, but it does not retain a Khronos-style observed trajectory
  or time-indexed dynamic geometry history as the session output.
- **A/D2:** yes for object lifecycle/current-map maintenance: appearance,
  disappearance, occlusion, pruning, and re-instantiation are handled.
- **Export:** active Gaussian scene plus reusable asset library; not a complete
  D1+D2 dynamic-scene backend state.
- **Process separation:** not demonstrated. The method is formulated over a
  continuous stream.
- **D3:** no implemented process-separated cross-session merge protocol.
- **B/D1:** not demonstrated.
- **B/D2:** not demonstrated as an independently restored session.
- **Recursion:** not demonstrated.

### Decisive boundary

The conclusion explicitly lists **incremental asset update and cross-session
asset merging as future work**. Therefore cross-session asset continuity is not
an implemented capability of the paper.

### Classification

`continuous object-centric Gaussian lifecycle maintenance; partial tracking;
no implemented process-separated D3; no recursive restoration of complete D1+D2`

---

## 2. DynaMem

**Paper:** *DynaMem: Online Dynamic Spatio-Semantic Memory for Open World Mobile
Manipulation*  
**Venue:** ICRA 2025; arXiv:2411.04999v2.  
**Primary text:** complete arXiv HTML/PDF text re-read.

### Temporal protocol

DynaMem explicitly assumes that the robot **does not start with a map**. It
explores an unknown, constantly changing environment and continuously updates one
running voxel memory while manipulation tasks are executed.

The real-world experiments modify each environment in several rounds while the
robot continues operating over the evolving memory.

### State

Each sparse voxel stores 3D position, observation count, source image ID, a VLM
semantic feature, and latest observation time. New observations add/update
voxels; ray casting removes contradicted old voxels.

### Architecture checklist

- **A/D1:** no retained entity-motion trajectory or time-indexed dynamic object
  geometry. Latest-observation timestamps are memory metadata, not D1 history.
- **A/D2:** yes at the memory level. Objects/obstacles can change outside the
  robot's knowledge and later contradictory observations update the map.
- **Export:** the paper does not define a completed-session state contract for an
  independent later mapping process.
- **Process separation:** no. The method is an online continuously evolving
  memory built from no initial map.
- **D3:** no process-separated A-to-B reconciliation protocol.
- **B/D1:** no.
- **B/D2:** no independently restored B protocol.
- **Recursion:** no.

### Classification

`continuous online voxel D2/current-memory maintenance; no retained D1 entity
history; no process-separated D3 continuation`

---

## 3. CogniMap3D

**Paper:** *CogniMap3D: Cognitive 3D Mapping and Rapid Retrieval*  
**Venue:** ICLR 2026 Poster; arXiv:2601.08175.  
**Primary text:** complete arXiv/OpenReview primary text re-read.

### Temporal protocol

CogniMap3D is explicitly designed for **multiple visits**. It identifies dynamic
regions in monocular videos, creates a memory bank from static scene content,
retrieves a stored scene when it recognizes a familiar environment, relocalizes
the camera, and updates the recalled scene with new static observations.

### Dynamic processing versus persistent memory

The method does more than a one-frame dynamic mask: after identifying dynamic
areas, SAM2 is used to track those dynamic areas across subsequent video frames.
However, the cognitive memory is intentionally built from **static regions**.
The persistent bank stores static 3D geometry and retrieval features; dynamic
areas are excluded so that the recalled representation remains a stable spatial
memory.

### Architecture checklist

- **A/D1:** partial front-end tracking of dynamic regions, but no persistent
  entity trajectory/time-indexed geometry is retained as scene memory.
- **A/D2:** not a Khronos-style hidden-transition state model. Dynamic regions
  are separated to support stable reconstruction rather than retained as
  persistent absent/unobserved/new entity history.
- **Export:** static-scene memory bank plus visual/geometric retrieval features.
- **Process separation:** multiple visits are genuine in the paper's framing;
  prior memories are recalled on revisits.
- **D3:** yes for static-scene retrieval/relocalization/update across visits.
- **B/D1:** the B video can again detect/track current dynamic regions, but the
  persistent state does not restore a D1 dynamic-history representation from A.
- **B/D2:** no complete D2 scene-state machinery comparable to the target.
- **Recursion:** static memory can be repeatedly recalled and updated, but the
  transferred contract is a static-scene memory, not a complete D1+D2 state.

### Classification

`genuine multi-visit D3 for persistent static scene memory, with within-video
dynamic-region tracking used to isolate static content; no retained D1 history
and no complete D1+D2 session restoration`

---

## 4. DovSG

**Paper:** *Dynamic Open-Vocabulary 3D Scene Graphs for Long-term
Language-Guided Mobile Manipulation*  
**Venue:** IEEE RA-L 2025; arXiv:2410.11989v2.  
**Primary text:** complete arXiv primary text re-read.

### Temporal protocol

DovSG maintains and locally updates an object-centric open-vocabulary 3D scene
graph while a robot executes long-term manipulation tasks.

The experiment section is decisive: it asks whether the robot can perform
**consecutive tasks without manual resets**. After the first task, the robot is
not returned to an initial state; it continues the second task from its current
state while the scene graph is continuously updated.

### Architecture checklist

- **A/D1:** no retained observed trajectory/time-indexed dynamic geometry.
- **A/D2:** yes for object/scene-graph changes discovered during continued task
  execution.
- **Export:** no completed-session state contract is defined.
- **Process separation:** explicitly no; the evaluation emphasizes consecutive
  tasks without manual reset.
- **D3:** no independent A-termination/B-start boundary.
- **B/D1:** not applicable under the target definition because there is no
  independent B.
- **B/D2:** the same running system continues updating its graph.
- **Recursion:** no process-separated recursive contract.

### Classification

`continuous-deployment object/scene-graph D2 maintenance; no independent D3
restart and no retained D1 history`

---

## 5. DynamicGSG

**Paper:** *DynamicGSG: Dynamic 3D Gaussian Scene Graphs for Environment
Adaptation*  
**Venue:** IROS 2025; arXiv:2502.15309v2.  
**Primary text:** complete arXiv primary text re-read.

### Temporal protocol

DynamicGSG incrementally constructs and updates an object-centric Gaussian scene
graph from posed RGB-D sequences. In real-world experiments, VIO supplies initial
poses and incoming RGB-D frames drive local map/scene-graph updates.

The dynamic-update experiment uses VINS-Fusion plus a RealSense D455 to acquire
aligned RGB-D streams and performs 80 manual environment modifications while the
same map is incrementally updated.

### Architecture checklist

- **A/D1:** no retained object trajectory/time-indexed dynamic geometry; motion
  is represented through current object-map changes.
- **A/D2:** yes for disappearance, relocation, and emergence of objects in the
  running map.
- **Export:** current Gaussian scene graph; no complete dynamic-session state
  contract is described.
- **Process separation:** not demonstrated; the real-world update pipeline is a
  continuing posed RGB-D/VIO stream.
- **D3:** no independent later-session restoration protocol.
- **B/D1:** no.
- **B/D2:** no independent B protocol.
- **Recursion:** no.

### Classification

`continuous posed-RGB-D/VIO Gaussian object-level D2/current-scene update; no
retained D1 history; no process-separated recursive D3`

---

## 6. DGSG-Mind

**Paper:** *DGSG-Mind: Dynamic 3D Gaussian Scene Graphs for Long-Term Scene
Understanding and Grounding*  
**Status:** arXiv preprint v2, 2026; arXiv:2605.29879v2.  
**Primary text:** complete arXiv primary text re-read.

### Why it is the closest of the seven to the D3 boundary

DGSG-Mind explicitly improves on DynamicGSG's dependence on continuous VIO. It
uses ACE-based camera relocalization followed by pose optimization against the
existing Gaussian map. The paper states that the update path can relocalize new
observations against the optimized Gaussian map **without requiring continuous
online SLAM**.

After relocalization, geometric/appearance/semantic consistency is used to
identify object-level changes; affected Gaussian instances and scene-graph nodes
are locally updated while the static background is kept fixed.

### Architecture checklist

- **A/D1:** no. The paper does not provide a complete observed-motion tracking
  module or retained trajectory/time-indexed dynamic geometry.
- **A/D2:** yes, strong object-level current-map change detection and local
  Gaussian revision.
- **Export:** persistent Gaussian/voxel instance map and scene graph sufficient
  for later relocalization and revision.
- **Process separation:** it no longer depends on a continuously running SLAM
  pose stream for later updates, making it substantially closer to a real prior
  map / later observation boundary than DynamicGSG.
- **D3:** representation-level prior-map reuse and later change reconciliation
  are present.
- **B/D1:** no. There is no complete D1 tracker after relocalization.
- **B/D2:** yes at the object-map revision level.
- **Recursion:** a maintained prior map can support later updates, but the state
  contract is not a complete D1+D2 mapper state.

### Decisive boundary

The conclusion explicitly says that **developing an integrated tracking module is
future work**. Thus the paper itself confirms that its current system does not
contain the D1 capability required by the target architecture.

### Classification

`strong prior-map relocalization plus dense Gaussian object-level D2 revision;
D3-like representation reuse, but no D1 tracker/history and therefore no
restoration of a complete D1+D2 mapper`

---

## 7. DREAM

**Paper:** *Dynamic Resilient Spatio-Semantic Memory with Hybrid Localization
for Mobile Manipulation*  
**Status:** arXiv preprint, 2026; arXiv:2606.00576v1.  
**Primary text:** complete arXiv primary text re-read.

### Temporal protocol

DREAM is explicitly an online closed-loop robot framework for a previously
unseen environment **without a pre-built map**. A LiDAR-inertial-visual SLAM
backend supplies trajectories and a voxel spatio-semantic memory is continuously
updated during task execution.

Its Redundancy-Aware Memory Pruning mechanism stores observation/keyframe history
and reintegrates affected observations when pose-graph optimization changes
historical camera poses. This is history of sensing/map integration, not D1
entity motion history.

### State

Each voxel stores geometry, observation count, source image ID, semantic feature,
and latest observation time. Historical observations/keyframes are retained in a
bounded form for pose-graph-aware memory rebuilding.

### Architecture checklist

- **A/D1:** no retained dynamic entity trajectory/time-indexed entity geometry.
- **A/D2:** yes for current-memory relocation/removal updates and target
  reacquisition.
- **Export:** no completed-session dynamic-scene state contract for independent
  later restart is defined.
- **Process separation:** no; the paper presents a closed-loop online deployment
  whose memory is continuously updated from incoming observations.
- **D3:** no independent A-terminate/B-import protocol.
- **B/D1:** no.
- **B/D2:** no independent B restoration protocol.
- **Recursion:** no process-separated recursive state contract.

### Classification

`continuous long-horizon voxel memory with pose-graph-aware historical
reintegration and D2/current-memory updates; no D1 entity history; no
process-separated D3 continuation`

---

# Combined architecture matrix

| Paper | A/D1 retained history | A/D2 | State survives/reused later | True independent D3 boundary | B again has D1 | B again has D2 | Recursive complete state to C |
|---|---:|---:|---:|---:|---:|---:|---:|
| CubifyGS | partial tracking only | yes | active scene/assets | no; cross-session merge future work | no | no independent B | no |
| DynaMem | no | yes | one running voxel memory | no | no | no independent B | no |
| CogniMap3D | dynamic-region tracking only; not retained | limited/non-equivalent | static scene memory bank | yes, for static memory visits | no retained D1 continuation | no complete D2 | static memory recursion only |
| DovSG | no | yes | running scene graph | no; consecutive tasks without reset | no | same-process only | no |
| DynamicGSG | no | yes | running Gaussian scene graph | no; continuous posed RGB-D/VIO | no | same-process only | no |
| DGSG-Mind | no | yes | Gaussian/voxel instance map + graph | strong prior-map/later-observation reuse | no; tracking is future work | yes at map-update level | not complete D1+D2 |
| DREAM | no | yes | running voxel + bounded observation history | no | no | same-process only | no |

# Corpus-level conclusion after this re-audit

The seven papers materially strengthen the literature on dynamic semantic memory,
Gaussian scene revision, multi-visit static memory, and prior-map relocalization.
They do **not** bridge the complete architecture:

```text
complete D1+D2 Session A
+ persistent export after A terminates
+ independent Session B import
+ D3 reconciliation
+ B resumes complete D1+D2
+ equivalent export for Session C
```

The verified corpus can therefore increase from **28 to 35 complete primary
texts**, while the architecture-level result remains corpus-bounded rather than a
universal non-existence proof.

# Primary-source anchors used in this re-audit

- CubifyGS: arXiv:2606.28720v2, especially Sec. III and Conclusion.
- DynaMem: arXiv:2411.04999v2, especially Secs. 3.1--3.4 and Sec. 4.
- CogniMap3D: arXiv:2601.08175 / ICLR 2026 OpenReview, especially Secs. 3.1--3.2
  and the multi-visit experiments.
- DovSG: arXiv:2410.11989v2, especially Sec. IV-B (consecutive tasks without
  manual resets).
- DynamicGSG: arXiv:2502.15309v2, especially Sec. III-E and Sec. IV-E.
- DGSG-Mind: arXiv:2605.29879v2, especially Sec. III-E and Conclusion.
- DREAM: arXiv:2606.00576v1, especially Sec. III-A and the closed-loop robot
  experiments.
