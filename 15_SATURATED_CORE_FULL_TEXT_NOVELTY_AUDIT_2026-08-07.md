# Saturated Core Full-Text Novelty Audit

Status checked: **2026-08-07**

This is the current authoritative novelty audit for the paper. It supersedes
all earlier title/abstract-level classifications. The audit is based on the
original full paper or full publisher/arXiv article, not only the abstract or a
project page. For each core work, the problem statement, state/representation,
method, experiment protocol, conclusion, and stated limitations were inspected.

## 1. Audit question

The project uses the following strict hierarchy:

```text
Within every continuously running session:
  D1 = motion is observed while it occurs, so a real trajectory and
       time-indexed geometry can be estimated.
  D2 = the same session remains active, but the transition occurs while the
       robot looks elsewhere; the system later infers persistent / absent /
       unobserved / new content without inventing a trajectory.

Across completed independent sessions:
  D3 = Session A terminates and exports persistent scene state. Independent
       Session B imports that state, reconciles A-to-B changes, runs its own
       D1+D2, and exports the state needed by Session C.
```

The novelty question is not whether any paper uses the words short-term,
long-term, dynamic, persistent, or multi-session. It is whether a system preserves
complete D1 history, performs explicit D2 reasoning, and recursively carries the
required dense scene state across process-separated D3 sessions.

## 2. Search and stopping rule

A defensible novelty audit does not require reading every paper containing the
word `dynamic`. It requires saturation of the relevant method space.

The current audit contains **38 full-text core or adjacent papers**, organized
into six independent research families. Search saturation was tested using:

1. direct queries for dynamic, semi-static, changing-scene, lifelong,
   multi-session, spatio-temporal, scene-memory, and 4D SLAM;
2. backward references from Khronos, Panoptic Multi-TSDFs, POCD, POV-SLAM,
   ELite, SuperMap, and LT-Mapper;
3. forward/near-neighbour searches for work combining intra-session and
   inter-session dynamics;
4. representation-specific searches for TSDF/mesh, object maps, scene graphs,
   point maps, neural fields, and Gaussian maps.

The stop condition is met for the current claim when two independent search
passes and reference chaining produce no new problem family or system closer to
the exact D1+D2-over-D3 specification. New 2026+ publications must still be
checked immediately before submission.

## 3. Full-text corpus

### A. Dense/object D1 and single-session dynamic SLAM

1. Co-Fusion, ICRA 2017.
2. MaskFusion, ISMAR 2018.
3. MID-Fusion, ICRA 2019.
4. EM-Fusion, ICCV 2019.
5. DynaSLAM, RA-L 2018.
6. DynaSLAM II, RA-L 2021.
7. Dynablox, RA-L 2023.
8. DynoSAM, T-RO 2025.
9. DYMRO-SLAM, IEEE Access 2025.
10. DYNEMO-SLAM, arXiv v2 2025.
11. Lost & Found, RA-L 2025.

### B. Single-session D2 and combined D1+D2

12. Detection and Tracking of General Movable Objects in Large 3D Maps,
    T-RO 2019.
13. Changing-SLAM / Visual Localization and Mapping in Dynamic and Changing
    Environments, JINT 2023.
14. Khronos, RSS 2024.
15. SuperMap, RSS 2026.
16. LTC-Mapping, Sensors 2022.
17. GaME, CVPR 2026.

### C. Cross-session geometric D3 maintenance

18. Dynamic Pose Graph SLAM, IROS 2012.
19. Long-Term 3D Map Maintenance in Dynamic Environments, ICRA 2014.
20. Multi-Session RGB-D SLAM in Low Dynamic Workspace Environments, 2016.
21. Efficient Long-Term Mapping in Dynamic Environments, IROS 2018.
22. A General Framework for Lifelong Localization and Mapping in Changing
    Environments, IROS 2021.
23. LT-Mapper, ICRA 2022.
24. RBIF Map Maintenance, IROS 2024.
25. ELite, ICRA 2025.
26. Lifelong 3D Mapping Framework for Hand-Held and Robot-Mounted LiDAR,
    accepted RA-L manuscript / public version.

### D. Cross-session object and volumetric D3

27. Panoptic Multi-TSDFs, ICRA 2022.
28. POCD, RSS 2022.
29. POV-SLAM, RSS 2023.
30. ObVi-SLAM, RA-L 2024.
31. Living Scenes, CVPR 2024.
32. OASIS-Map, under-review arXiv preprint as of the audit date.

### E. Gaussian and 4D adjacent representations

33. 4D Gaussian Splatting SLAM, ICCV 2025.
34. 4DTAM, CVPR 2025.
35. 4D Primitive-Mache, CVPR 2026.
36. DynaGSLAM, WACV 2026.
37. LT-Gaussian, IEEE IV 2025.

### F. Temporal existence theory

38. Perpetua, IROS 2025.

ProbPer-LiLo is deliberately **not** used to support a final novelty statement
because the complete paper PDF was not available in the current audit workspace.
Only its official metadata and abstract were available. It remains a mandatory
pre-submission check rather than silently being treated as fully read.

## 4. What the closest systems actually do

### 4.1 Khronos: the complete dense single-session D1+D2 base

Khronos defines one spatio-temporal metric-semantic estimation problem indexed
by a continuous time sequence. Its active temporal window tracks visible motion
and preserves dynamic trajectories/time-indexed geometry (D1). Its global
reconciliation associates and reconciles scene fragments separated by
observation gaps (D2).

It does not define or evaluate a completed-Session-A export, independent
Session-B import, B-resumes-D1+D2, and B-exports-to-C protocol. Therefore:

```text
Khronos = dense D1 + D2 inside one running session
Khronos != published process-separated D3 continuation
```

### 4.2 Efficient Long-Term Mapping 2018: closest high-level predecessor

This paper is the strongest warning against claiming that nobody has combined
intra-session and inter-session dynamics. It explicitly presents a full SLAM
system for:

- highly dynamic situations within a mapping session; and
- map updates across multiple sessions to handle low dynamics.

However, its single-session high dynamics are handled by maintaining/merging 2D
local point-cloud maps so that non-static observations are removed from the
current localization map. It does not preserve moving-object identities,
trajectories, temporal bounding boxes, or time-indexed dynamic geometry. It also
does not distinguish D1 observed motion from D2 hidden transitions as two scene
outputs. The cross-session representation is an up-to-date pose graph/local-map
model with outdated nodes removed.

Therefore it already covers the broad engineering pattern:

```text
single-session dynamic suppression + multi-session current-map update
```

but not the exact target:

```text
retain D1 history + explicit D2 reasoning + recursive dense D3 scene memory
```

### 4.3 ELite: strong point-level D3, not D1+D2

ELite estimates local ephemerality within each new LiDAR session, uses ray
observations to classify and remove dynamic points, and updates point-wise global
ephemerality over multiple sessions. It recursively maintains lifelong, static,
and delta point maps.

Its local ephemerality is a dynamic-versus-static removal score, not the
project's D1/D2 decomposition. Dynamic points are deliberately discarded before
the cross-session update. ELite has no D1 object trajectory/history and no
object-level D2 identity reasoning.

### 4.4 Multi-session RGB-D and lifelong point-map systems

Dynamic Pose Graph SLAM, the 2016 multi-session RGB-D framework, Efficient
Long-Term Mapping, the 2021 general lifelong framework, LT-Mapper, RBIF, ELite,
and the Lifelong 3D Mapping Framework already provide combinations of:

- independent-session registration or loop closure;
- prior/current graph or point-map reuse;
- high-dynamic removal;
- positive/negative change detection;
- outdated scan/node replacement;
- base/live/delta maps;
- map-history or version-control reconstruction;
- recursive current-map maintenance.

These mechanisms are existing work. Their target is normally a clean and
up-to-date localization map, not an auditable dense dynamic scene history.

### 4.5 Panoptic Multi-TSDFs, POCD, and POV-SLAM: D3 state foundations

Panoptic Multi-TSDFs starts a later run from prior active/inactive object
submaps and labels inactive entities as persistent, absent, or unobserved. It
uses externally provided poses and explicitly leaves short-term object tracking
for future work.

POCD models bounded rigid objects across traversals with object TSDFs,
geometric-change beliefs, and stationarity beliefs. It assumes external
localization and leaves explicit dynamic handling for future work.

POV-SLAM incorporates semi-static object consistency into joint robot-pose
estimation and evaluates repeated visits separated by months. None of the three
preserves the complete D1 history of moving entities during every current
session.

### 4.6 ObVi-SLAM: a genuine recursive deployment prior, but static/object only

ObVi-SLAM is important because it explicitly has deployment-indexed operation:
a previous long-term object map is used as a prior during a new deployment, and
a new uncertainty-aware long-term map is extracted after the deployment.
However, its persistent map consists of selected static object landmarks for
long-term localization. It does not preserve dense background geometry, D1
moving-object history, or a Khronos-style D2 scene evolution.

### 4.7 SuperMap: continuous semantic-object maintenance, not D3

SuperMap formally processes one RGB-D or point-cloud video sequence indexed by
`t=1,...,T`. It updates pose, instance IDs, an object map, occupancy confidence,
semantic confidence, and spatial/temporal scene-graph relations online. Its
change experiment is a ten-minute continuous run containing added and removed
objects. Its own limitation states that highly dynamic-object tracking remains
limited.

SuperMap is a useful D2-like object-semantic maintenance method. It is not a
process-separated cross-session system and does not preserve Khronos-style dense
D1 trajectories/time-indexed geometry.

### 4.8 DYNEMO-SLAM and Lost & Found: observed entity motion

DYNEMO-SLAM jointly optimizes robot keyframes, time-indexed entity poses,
planes, and floors in one factor graph. Its experiments use AprilTags and leave
real perception, segmentation, and multi-observation association outside scope.
It handles moving agents and objects relocated after initial exploration inside
one running graph.

Lost & Found observes human-object interactions, estimates object 6-DoF motion
during the interaction, and applies the observed transform to a scene graph.
Both are D1/entity-update work rather than hidden D2 or process-separated D3.

### 4.9 Gaussian and 4D methods: rich D1 or map revision, not the complete problem

4DGS-SLAM, 4DTAM, 4D Primitive-Mache, and DynaGSLAM build rich temporal
representations from a continuous image/RGB-D stream. They are strong D1
references. `Persistent` in this literature usually means object permanence or
motion continuity within one video, not process-separated session memory.

GaME updates one online Gaussian map after out-of-view changes and is a strong
D2 representation component. LT-Gaussian updates an old Gaussian map with a
later LiDAR traversal and is a D3 map-revision component. Neither carries a
complete D1+D2 dynamic SLAM state through independent sessions.

### 4.10 Perpetua: existence theory, not dense mapping

Perpetua models binary feature presence with mixtures of persistence and
emergence filters, multiple temporal hypotheses, online adaptation, and
prediction under missing observations. It is a mandatory theory reference for
existence/persistence modeling, but it has no dense geometry, object identity,
D1 trajectories, or map materialization.

## 5. Final novelty conclusion from the saturated core set

### What is not new

The following broad claims are false or indefensible:

- first to consider dynamics at multiple time scales;
- first to handle both intra-session and inter-session dynamics;
- first to maintain a map over repeated sessions;
- first to distinguish persistent, absent, unobserved, and new content;
- first to use ray evidence for dynamic removal or map update;
- first to retain base/current/delta maps or map history;
- first to model object persistence, stationarity, ephemerality, existence, or
  reappearance probabilistically;
- first to combine dynamic SLAM with a scene graph;
- first to update objects that were moved outside the current view.

### What was not found

Across the 38-paper full-text core set, no audited system jointly provides all
of the following in one recurring architecture:

1. **D1 retained history:** moving entities observed during a session are kept as
   trajectories and time-indexed geometry rather than only rejected or removed;
2. **D2 explicit same-session reasoning:** hidden transitions within the same
   active session are represented without fabricating motion and distinguish
   lack of observation from evidence of absence;
3. **dense object + structural current map:** the current environment includes
   both discrete objects and non-object structural geometry;
4. **process-separated D3 bridge:** a completed session exports the state needed
   by an independent later session;
5. **recursive continuation:** the later session reconciles inter-session
   changes, again performs full D1+D2, and exports the prior for a third session.

The defensible statement is therefore not `nobody proposed three dynamics`.
It is:

> In the full-text core literature audited, methods either preserve rich
> dynamic histories inside one continuously running session or maintain cleaned
> geometric/object maps across sessions. We did not find a dense
> metric-semantic system that recursively transfers the state required to
> preserve D1 histories, perform D2 hidden-change reasoning, update object and
> structural geometry across D3, and resume the same D1+D2 process in each
> independently initialized session.

This remains a `to the best of our knowledge` claim and must be refreshed before
submission, but it is now grounded in a saturated method-space audit rather than
paper titles.

## 6. Existing method components that the new method must not claim

### Already established for D1

- semantic/geometric dynamic masking;
- moving-point detection from free space;
- per-object surfel, TSDF, SDF, octree, primitive, and Gaussian models;
- joint robot/object BA or factor graphs;
- time-indexed object poses and temporal boxes;
- object/agent motion priors;
- scene-graph entity factors;
- non-rigid deformation and continuous-time motion fields.

### Already established for D2

- local-motion/global-jump association;
- fragment and object re-association;
- visibility and repeated non-detection updates;
- ray-based presence/absence contradiction;
- inactive/reactivated object states;
- persistent/absent/unobserved/new labels;
- stale-keyframe or stale-geometry deletion;
- multi-hypothesis persistence/emergence models.

### Already established for D3

- independent-session alignment and multi-session PGO;
- prior-map/current-session initialization;
- point-level local/global ephemerality;
- object stationarity and persistency factors;
- positive/negative changes and delta maps;
- current-map replacement and outdated-node pruning;
- version control and historical-map reconstruction;
- cross-session object correspondence;
- old-Gaussian-map/current-traversal revision.

## 7. Method territory that remains defensible

The method should not be presented as a simple composition of Khronos and an
existing D3 updater. The strongest remaining direction is a **session-boundary
scene state that is sufficient to restart complete D1+D2 inference**.

A useful boundary state should preserve, for each object or structural element:

```text
- current geometry and semantic state;
- last reliable presence and contradiction evidence;
- observed coverage / unobserved support;
- object identity and association information;
- D1 history that must not be collapsed into the static map;
- unresolved D2/D3 event evidence;
- session provenance and coordinate-frame information.
```

The method must demonstrate something unavailable from a cleaned point map,
object persistence score, or hard union/deletion rule. Promising directions are:

1. a principled export/import state for the Khronos global scene and object
   memory;
2. a unified evidence model for object instances and structural patches;
3. explicit separation of `unobserved` from `observed absent` during map
   materialization;
4. preservation of D1 history while producing a current actionable map;
5. recursive A-to-B-to-C operation, not only pairwise A/B differencing.

## 8. Experimental implications

The minimum convincing protocol is:

```text
Session A:
  contains D1 and D2
  exports memory M_A

A-to-B gap:
  genuine environmental intervention

Independent Session B:
  imports M_A
  reconciles D3
  contains new D1 and D2
  exports M_B

Session C:
  imports M_B and demonstrates recursion / error control
```

Required baselines should include:

- original Khronos for D1+D2;
- naive union and newest-session-only replacement;
- a point/ray geometric D3 updater inspired by Efficient Long-Term Mapping,
  ELite, or RBIF;
- Panoptic Multi-TSDF-style persistent/absent/unobserved logic;
- object-level POCD/POV/OASIS-style association where input assumptions permit;
- the proposed complete state transfer and reconciliation.

## 9. Remaining mandatory pre-submission checks

- Obtain and fully inspect ProbPer-LiLo.
- Recheck the publication status of OASIS-Map, DYNEMO-SLAM, and GS-LTS.
- Repeat current-year searches immediately before submission.
- Do not add a new novelty sentence unless its strongest counterexample has a
  completed source entry in this audit.
