# Literature Status and Three-Regime Scope Audit

Status checked: **2026-08-06**

This is an internal author note, not manuscript text. Publication status and
novelty claims must be checked again immediately before submission.

## The Three Regimes Used in This Project

The classification below follows the intended system behavior, not the words
`dynamic`, `long-term`, or `changing` in a paper title.

1. **D1 — continuously observed motion**
   - The robot sees the object moving during the same session.
   - A successful system can represent a trajectory, temporal box, timestamps,
     or time-indexed dynamic geometry.

2. **D2 — hidden change inside one still-running session**
   - The robot observes an old state, looks elsewhere while the same SLAM
     session remains active, and later re-observes the region.
   - The transition itself was not observed. The output should distinguish
     persistent, absent, unobserved, and new content without inventing a
     trajectory.

3. **D3 — environmental change across completed independent sessions**
   - Session A terminates, the robot leaves, the scene changes, and Session B is
     a new process or deployment.
   - B must load persistent scene memory from A. B can simultaneously contain
     new D1 and D2 events.

A temporal gap alone is not D3. Splitting one continuous sequence, restarting,
and continuing with the same observations is primarily a checkpoint/recovery
control unless it represents a genuinely independent revisit.

## Main Novelty Warning

A broad claim such as **“the first SLAM system to unify dynamic tracking and
long-term map update” is not defensible**.

Two particularly important prior works already make closely related claims:

- Pomerleau et al., ICRA 2014, describe their system as the first to
  “unify long-term map update with tracking of dynamic objects” (Abstract).
- Changing-SLAM, JINT 2023, explicitly targets both objects moving in front of
  the robot and objects moved after the scene was mapped.

The defensible target is narrower:

> To the best of our knowledge, no published **dense metric-semantic
> spatio-temporal SLAM** system combines D1 time-indexed dynamic reconstruction,
> D2 same-session hidden-change reconciliation, and D3 persistent continuation
> across independent process-separated sessions in one recurring scene memory.

This wording still requires a final systematic literature review.

## Closest Published Methods

### 1. Long-Term 3D Map Maintenance in Dynamic Environments

- **Authors:** Pomerleau, Krüsi, Colas, Furgale, Siegwart
- **Venue/status:** ICRA 2014 — **published**
- **DOI:** https://doi.org/10.1109/ICRA.2014.6907397
- **D1:** Yes, at point level. It estimates velocities for dynamic points from
  consecutive point clouds.
- **D2:** Partial. Visibility-based repeated observations change point-level
  static/dynamic belief, but the method does not formulate object-level hidden
  jumps with persistent/absent/unobserved/new states.
- **D3:** Yes in a broad long-term sense. It maintains a map using surveys
  collected over seven months.
- **Representation:** Sparse 3D LiDAR points with static/dynamic probability and
  point-wise velocity history.
- **Boundary relative to this project:** This is the strongest early warning
  against a broad first-unification claim. It does not construct a dense
  metric-semantic scene history with object identity, private geometry,
  structural elements, or an explicit A-final-memory to B-initial-prior
  protocol.
- **Original wording:** “first work to unify long-term map update with tracking
  of dynamic objects” (Abstract, p. 1).

### 2. Changing-SLAM

- **Full title:** Visual Localization and Mapping in Dynamic and Changing
  Environments
- **Venue/status:** Journal of Intelligent & Robotic Systems 109:95, 2023 —
  **published**
- **DOI:** https://doi.org/10.1007/s10846-023-02019-6
- **D1:** Yes for localization-oriented dynamic processing. It tracks movable
  objects with an EKF and filters dynamic ORB keypoints.
- **D2:** Yes/partial. Its changing-environment sequences contain objects moved
  outside the field of view after being mapped.
- **D3:** **Not established as defined here.** The paper uses ORB-SLAM3 Atlas,
  active/non-active maps, and long-term association inside its SLAM system, but
  it does not present a process-separated A-save/B-load scene-memory protocol.
  The PDF contains no session, save, or load experiment definition.
- **Representation/output:** Object belief map plus an ORB-feature sparse map;
  the primary evaluation is camera trajectory robustness.
- **Boundary relative to this project:** It is a major conceptual predecessor
  for D1 plus changing-scene SLAM. The difference cannot merely be “we also
  handle moving and changed objects.” The target must be dense spatio-temporal
  metric-semantic reconstruction, explicit D1/D2 outputs, and independently
  persistent D3 memory.
- **Original wording:** “the sparse map clear of outliers” (Sec. 4, p. 5).

### 3. Khronos

- **Venue/status:** Robotics: Science and Systems 2024 — **published**
- **DOI:** https://doi.org/10.15607/RSS.2024.XX.081
- **D1:** Yes. Active-window estimation represents continuously observed
  motion.
- **D2:** Yes. Global reconciliation reasons about abrupt changes across
  observation gaps in the same evolving SMS problem.
- **D3:** No published process-separated continuation protocol. The paper
  formulates one spatio-temporal map over a continuous temporal sequence.
- **Representation:** Dense spatio-temporal metric-semantic map, background
  mesh, objects, dynamic trajectories, and global reconciliation.
- **Boundary relative to this project:** The most direct technical base. The new
  problem is not to rediscover D1 or D2, but to make the complete D1+D2 system
  recur across independent sessions through persistent memory.
- **Original wording:** “a fast process tracks short-term dynamics” and “a
  slower process reasons over long-term changes” (Abstract).

### 4. Efficient Long-Term Mapping in Dynamic Environments

- **Venue/status:** IROS 2018 — **published**
- **DOI:** https://doi.org/10.1109/IROS.2018.8594310
- **D1:** No explicit object trajectory or dynamic-object representation.
- **D2:** Partial map-update behavior, but not the D1/D2 scene-history model.
- **D3:** Yes. It explicitly supports single or multiple mapping sessions and
  begins later sessions from a previous graph.
- **Representation:** Pose graph with up-to-date 2D local point-cloud maps.
- **Boundary relative to this project:** A direct baseline for persistent
  geometric map maintenance, but not dense 3D metric-semantic scene evolution.
- **Original wording:** “across a single or multiple mapping sessions”
  (Abstract).

### 5. Panoptic Multi-TSDFs

- **Venue/status:** ICRA 2022 — **published**
- **DOI:** https://doi.org/10.1109/ICRA46639.2022.9811877
- **D1:** No. The paper says short-term object tracking is left for future work.
- **D2:** Partial through active/inactive submap consistency.
- **D3:** Yes/partial. Its changing-scene experiments reuse prior submaps across
  runs and update persistent/absent/unobserved states, with externally supplied
  poses.
- **Representation:** Object/background TSDF submaps.
- **Boundary relative to this project:** Strong dense D3 mapping baseline and a
  key source for persistent/absent/unobserved semantics, but not a full dynamic
  SLAM system with D1.
- **Original wording:** Short-term tracking “is left for future work” (Sec. II).

### 6. POCD

- **Venue/status:** Robotics: Science and Systems 2022 — **published**
- **DOI:** https://doi.org/10.15607/RSS.2022.XVIII.013
- **D1:** No explicit continuously observed dynamic trajectory.
- **D2:** Not the primary regime under this project’s taxonomy.
- **D3:** Yes. It updates object-level volumetric maps in repeated traversals and
  evaluates objects that change between runs.
- **Representation:** Object TSDFs with a Gaussian-Beta state combining geometry
  change and stationarity.
- **Boundary relative to this project:** Strong probabilistic D3 baseline and
  possible source for object belief updates; it does not preserve a complete
  D1+D2 spatio-temporal map in every session.
- **Original wording:** “objects that change between runs” (dataset description).

### 7. POV-SLAM

- **Venue/status:** Robotics: Science and Systems 2023 — **published**
- **DOI:** https://doi.org/10.15607/RSS.2023.XIX.069
- **D1:** No complete dynamic-object history of the Khronos type.
- **D2:** Not the primary regime under this taxonomy.
- **D3:** Yes. It jointly estimates pose and semi-static object consistency over
  repeated visits, including warehouse data collected over four months.
- **Representation:** Object-aware factor graph with variational inference.
- **Boundary relative to this project:** Important for future joint
  pose/change estimation across sessions, but not a dense D1+D2+D3 scene-memory
  system.
- **Original wording:** “captured in a warehouse over four months” (Abstract).

### 8. ObVi-SLAM

- **Venue/status:** IEEE Robotics and Automation Letters 9(3), 2024 —
  **published**
- **DOI:** https://doi.org/10.1109/LRA.2024.3363534
- **D1:** No.
- **D2:** No complete hidden-change reconstruction.
- **D3:** Yes. It maintains persistent object landmarks across 16 deployment
  sessions for long-term localization.
- **Representation:** Sparse visual features plus an uncertainty-aware map of
  persistent objects.
- **Boundary relative to this project:** Strong D3 localization baseline, not a
  dense evolving scene representation.
- **Original wording:** the object map “updates it after every deployment”
  (Abstract).

### 9. Detection and Tracking of General Movable Objects in Large 3D Maps

- **Venue/status:** IEEE Transactions on Robotics 35(1), 2019 — **published**
- **DOI:** https://doi.org/10.1109/TRO.2018.2876111
- **D1:** Partial through a local-motion process.
- **D2:** Yes at object level: objects may move while the robot observes another
  area, with linked local-motion and global-jump models.
- **D3:** Not necessarily process-separated; the main distinction is large-map
  partial observability.
- **Representation:** Long-term movable-object tracker, not dense SLAM geometry.
- **Boundary relative to this project:** Highly relevant mathematical prior for
  D2 identity association, especially local movement versus global jumps.
- **Original wording:** objects “might be moved when the robot is not there”
  (Abstract).

### 10. Living Scenes

- **Venue/status:** CVPR 2024 — **published**
- **Paper:** https://openaccess.thecvf.com/content/CVPR2024/html/Zhu_Living_Scenes_Multi-object_Relocalization_and_Reconstruction_in_Changing_3D_Environments_CVPR_2024_paper.html
- **D1:** No online visible-motion SLAM.
- **D2:** No same-session dynamic mapping process.
- **D3:** Yes in a scan-to-scan reconstruction sense.
- **Representation:** Multi-object matching, registration, and accumulated
  reconstruction across scans.
- **Boundary relative to this project:** Strong cross-time object reconstruction
  baseline, but not online robot SLAM or persistent dense background memory.
- **Original wording:** “scans taken at different points in time” (Abstract).

### 11. Gaussian Mapping for Evolving Scenes (GaME)

- **Venue/status:** CVPR 2026 — **published**
- **Paper:** https://openaccess.thecvf.com/content/CVPR2026/html/Yugay_Gaussian_Mapping_for_Evolving_Scenes_CVPR_2026_paper.html
- **D1:** Not its principal contribution; it discusses existing short-term
  dynamic Gaussian methods.
- **D2:** Yes. It updates an evolving 3D Gaussian map after out-of-view changes
  and manages stale keyframes.
- **D3:** Not established as an independent-session memory protocol.
- **Representation:** 3D Gaussian Splatting for mapping and novel-view synthesis.
- **Boundary relative to this project:** Important recent dense evolving-scene
  baseline, but not an object/structure-aware multi-session SMS system.
- **Original wording:** “the scene evolving through changes out of view”
  (Abstract).

## Concurrent / Unpublished Work

### OASIS-Map — SPECIAL STATUS MARK

- **Title:** OASIS-Map: Object-Level Change Detection in Multi-Session Mapping
  Using Semantic Correspondence Matching
- **Authors:** Oh, Tao, Chebrolu, Fallon
- **Status on 2026-08-06:** **UNDER REVIEW / ARXIV PREPRINT; NOT YET A
  PEER-REVIEWED PUBLICATION**
- **arXiv:** https://arxiv.org/abs/2607.14899
- **Official project:** https://ori-drs.github.io/projects/oasis-map/
- **Official citation wording:** `note={Under review}`.
- **D1:** No continuously observed dynamic trajectory as defined here.
- **D2:** No same-session D1+D2 dynamic SLAM pipeline; its “within-view” and
  “out-of-view” labels refer to cross-session object correspondence behavior.
- **D3:** Yes. It performs object association and appear/disappear/static/moved/
  unknown reasoning across revisits.
- **Representation:** Object-level multi-session map plus 2D and 3D change maps.
- **Action before submission:** Re-check whether it has been accepted or
  published. If it remains a preprint, cite it explicitly as concurrent
  unpublished work or remove it depending on the final conference policy and
  narrative.

## Direction-Only Supporting Papers

These are useful references but are not the main novelty threats.

- **Co-Fusion, ICRA 2017 — published:** D1 multi-object segmentation, tracking,
  and reconstruction.
- **MaskFusion, ISMAR 2018 — published:** D1 instance-level tracking and dense
  reconstruction of multiple moving objects.
- **DynaSLAM, RA-L 2018 — published:** D1 dynamic-region rejection and static
  reconstruction; does not preserve the moving entity as a scene history.
- **Dynablox, RA-L 2023 — published:** D1 moving-object detection from
  conservative free-space reasoning.
- **DynoSAM, T-RO 2025 early access — published:** D1 joint optimization of
  camera, object motion/poses, and object structure.
- **Dynamic Pose Graph SLAM, IROS 2012 — published:** D3-style long-term graph
  editing in 2D LiDAR maps; no D1 scene representation.
- **Feature Persistence, ICRA 2016 — published:** exact recursive Bayesian
  persistence model for semi-static landmarks; not a dense dynamic system.
- **Practical Persistence Reasoning, ICRA 2020 — published:** persistence filter
  integrated into ORB-SLAM; focused on sparse landmark retention.

## Dataset Consequences

No inspected public dataset cleanly supports all three regimes under one common
scene-memory evaluation.

- **Khronos Office/Apartment:** Best for D1 and D2 in one continuous session.
  Artificial reverse playback can validate software flow, but reverses causal
  dynamics and is not a final D3 benchmark.
- **PUC-USP / Changing-SLAM:** Contains visible dynamic scenes and objects moved
  after mapping, but is organized as short sequences rather than a documented
  process-separated A-memory/B-prior protocol.
- **Panoptic Flat:** Useful for dense prior-run/current-run map update and
  persistent/absent/unobserved tests; weak for D1 trajectories.
- **POCD warehouse and ToyCar:** Useful D3 object-level map-update benchmarks;
  weak for dense background and D1.
- **3RScan:** Strong D3 object identity/rearrangement ground truth; no visible
  dynamic trajectories.
- **NSS stage pairs:** Strong candidate for D3 structural additions/removals and
  exact current-stage geometry; requires rendered trajectories, semantic/instance
  labels, and a visibility-aware evaluation protocol.
- **New RGB-D recordings:** Needed for a single end-to-end episode containing
  D1 and D2 inside Session A, real A-to-B interventions, and new D1/D2 events
  inside independent Session B. A third Session C would establish recurring
  memory rather than pairwise differencing.

## Immediate Writing Rule

Until the final method and experiments are complete, use the following claim:

> We formulate and investigate dense persistent spatio-temporal metric-semantic
> mapping across independent sessions, where every session retains both visible
> dynamic reconstruction and hidden-change reconciliation.

Do **not** currently claim:

- first system to combine dynamic tracking and long-term map update;
- first SLAM system robust to both moving and changed objects;
- first long-term dynamic SLAM system;
- full native Khronos backend restart;
- quantitative superiority across all three regimes.
