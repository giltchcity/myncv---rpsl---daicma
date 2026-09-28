# Full-Text Evidence Audit for Related Work

Status checked: **2026-08-06**

This file is the evidence ledger behind `manuscript/sec/1_intro.tex` and
`manuscript/sec/2_related_work.tex`. It is an internal author document, not
manuscript prose.

## Audit standard

A title, abstract, project-page summary, or another paper's description is not
sufficient evidence for a technical claim. For every paper below, the audit
checked, where available:

1. the problem definition and assumptions;
2. the actual state variables and map representation;
3. the method section, not only the abstract;
4. the experiments and what they really evaluate;
5. the limitations or conclusion;
6. whether a claimed capability is implemented, merely discussed, or left as
   future work;
7. whether a statement is the authors' own contribution or their criticism of
   prior work.

Quotes are intentionally short. The source section and PDF page are supplied so
that the complete surrounding paragraph can be checked in the downloaded paper.
An absence claim is phrased conservatively as “the paper does not specify or
evaluate X,” never as “the system cannot possibly support X.”

## Project taxonomy

- **D1 — continuously observed motion:** an entity moves while visible in the
  current session; the estimator can retain a trajectory, poses, temporal boxes,
  or time-indexed geometry.
- **D2 — hidden change inside one still-running session:** the system observes
  the old state, looks elsewhere while the same SLAM process remains active, and
  later re-observes the changed region.
- **D3 — inter-session change:** a completed Session A is followed by a new,
  independent Session B that imports persistent memory from A. Session B may
  itself contain new D1 and D2 events.

A temporal gap without a completed-session boundary is not D3.

---

## 1. Co-Fusion

**Citation:** Rünz and Agapito, ICRA 2017.  
**Status:** Peer-reviewed and published.  
**Full-text source:** arXiv:1706.06629.  
**Sections audited:** Introduction; Sec. III system overview and object-model
management; tracking, segmentation and fusion subsections; experiments and
conclusion.

**Short original evidence:**
> “Co-Fusion is a live RGB-D SLAM system that processes each new frame in real time.”

**Source location:** Sec. III, PDF p. 3.

**What the paper actually implements:** A live RGB-D system with a background
surfel model and separate surfel models for multiple active rigid objects. It
segments, tracks and fuses these models online.

**Allowed conclusion:** Strong D1 precedent for dense multi-object segmentation,
tracking and reconstruction during continuous observation.

**Do not write:** That Co-Fusion reasons about an object that changes while
unobserved, or that it transfers a completed scene state between independent
sessions.

**Coverage:** D1 yes; D2 no; D3 no.

---

## 2. MaskFusion

**Citation:** Rünz, Buffier and Agapito, ISMAR 2018.  
**Status:** Peer-reviewed and published.  
**Full-text source:** arXiv:1804.09194.  
**Sections audited:** Introduction; system overview; instance segmentation,
tracking and reconstruction; evaluation; conclusion and limitations.

**Short original evidence:**
> “The system maintains independent 3D models for each object instance and for the background.”

**Source location:** Conclusion, PDF p. 8.

**What the paper actually implements:** Instance-aware RGB-D mapping with
independent object and background models. The tracked and reconstructed objects
are rigid. The limitation section says non-rigid objects such as people are
removed instead of reconstructed.

**Allowed conclusion:** Strong D1 precedent for semantic, instance-level rigid
object tracking and dense reconstruction.

**Do not write:** That it reconstructs arbitrary non-rigid motion, hidden jumps,
or cross-session object memory.

**Coverage:** D1 yes for rigid objects; D2 no; D3 no.

---

## 3. DynaSLAM

**Citation:** Bescos et al., RA-L 2018.  
**Status:** Peer-reviewed and published.  
**Full-text source:** arXiv:1806.05620.  
**Sections audited:** Introduction; dynamic-content detection; background
inpainting; experiments; conclusion.

**Short original evidence:**
> “Our system accurately tracks the camera and creates a static and therefore reusable map of the scene.”

**Source location:** Sec. V, PDF p. 8.

**What the paper actually implements:** Semantic and multi-view geometric
masking to remove dynamic or potentially movable regions from tracking and
mapping, plus reconstruction of occluded background. The moving entities are not
retained as a time-indexed scene history.

**Allowed conclusion:** D1-related precedent for protecting camera tracking and
constructing a static reusable map in dynamic scenes.

**Do not write:** That DynaSLAM models moving-object trajectories or maintains
D2/D3 scene evolution.

**Coverage:** D1 measurements handled by rejection; D2 no; D3 no.

---

## 4. Dynablox

**Citation:** Schmid et al., RA-L 2023.  
**Status:** Peer-reviewed and published.  
**Full-text source:** arXiv:2304.10049.  
**Sections audited:** Problem definition; volumetric free-space model; dynamic
point detection; experiments; limitations and conclusion.

**Short original evidence:**
> “We presented Dynablox, a novel online mapping-based approach for real-time moving object detection in complex dynamic environments.”

**Source location:** Conclusion, PDF p. 9.

**What the paper actually implements:** Appearance-agnostic moving-point
detection based on a conservative spatio-temporal estimate of free space in an
online volumetric map. It detects motion rather than jointly estimating an
object's pose, identity and complete trajectory.

**Allowed conclusion:** Strong D1 detector and a source of conservative
free-space reasoning.

**Do not write:** That Dynablox is a complete object-motion SLAM system or a
multi-session scene-memory method.

**Coverage:** D1 yes as detection; D2 no complete change state; D3 no.

---

## 5. DynoSAM

**Citation:** Morris et al., IEEE T-RO 2025.  
**Status:** Peer-reviewed journal publication / early-access record.  
**Full-text source:** arXiv:2501.11893 and the IEEE article record.  
**Sections audited:** Introduction and dynamic-SLAM definition; motion and pose
formulations; factor-graph construction; experiments; limitations.

**Short original evidence:**
> “DynoSAM is an open-source smoothing and mapping framework for Dynamic SLAM.”

**Source location:** Introduction and Fig. 1 discussion.

**What the paper actually implements:** Joint smoothing formulations for camera
state, dynamic-object motion or poses, and static/dynamic structure. The paper
explicitly distinguishes motion estimation from methods that merely remove
dynamic measurements.

**Allowed conclusion:** Strong D1 state-estimation baseline for joint robot and
object motion.

**Do not write:** That its contribution is hidden-change inference or
process-separated persistent map continuation.

**Coverage:** D1 yes; D2 no; D3 no.

---

## 6. Detection and Tracking of General Movable Objects in Large 3D Maps

**Citation:** Bore et al., IEEE T-RO 2019.  
**Status:** Peer-reviewed and published.  
**Full-text source:** arXiv:1712.08409.  
**Sections audited:** Introduction; local-motion process; global-movement and
association process; experiments; discussion.

**Short original evidence:**
> “The objects might be moved when the robot is not there.”

**Source location:** Abstract, PDF p. 1; the local/global process is developed in
the method sections.

**What the paper actually implements:** A long-term movable-object tracker for a
large partially observed map, combining frequent local motion with rarer global
jumps and data association over observation gaps.

**Allowed conclusion:** Important mathematical and object-association precedent
for D2, especially the distinction between locally observed motion and global
jumps while another part of the map is being observed.

**Do not write:** That it reconstructs a dense background scene or provides a
complete metric-semantic SLAM representation.

**Coverage:** D1 partial; D2 yes at object level; D3 not established as a
process-separated protocol.

---

## 7. Long-Term 3D Map Maintenance in Dynamic Environments

**Citation:** Pomerleau et al., ICRA 2014.  
**Status:** Peer-reviewed and published.  
**Full-text source:** Author-accessible full text; DOI 10.1109/ICRA.2014.6907397.  
**Sections audited:** Introduction; point-state representation; visibility and
observation update; velocity estimation; seven-month experiments; discussion of
failure cases.

**Short original evidence:**
> “This is the first work to unify long-term map update with tracking of dynamic objects.”

**Source location:** Abstract, PDF p. 1; the implementation and experiments are
specified in the following sections.

**What the paper actually implements:** Long-term 3D LiDAR point-map maintenance,
point-wise static/dynamic probabilities, visibility-based updates and velocity
estimation from consecutive clouds over surveys spanning seven months.

**Allowed conclusion:** A strong broad predecessor spanning visible dynamics and
long-term map update. It invalidates an unrestricted “first to unify dynamic
tracking and long-term mapping” claim.

**Important limitations from the full text:** The representation is sparse and
point-level rather than object- and structure-aware. The discussion identifies
ambiguity for periodically moving objects and motivates higher-level models.

**Do not write:** That all earlier long-term mapping ignored moving-object
tracking, or present the paper's criticism of periodic ambiguity as a capability
it solved.

**Coverage:** D1 yes at point/velocity level; D2 partial through visibility
updates; D3 broad long-term repeated-survey maintenance.

---

## 8. Changing-SLAM: Visual Localization and Mapping in Dynamic and Changing Environments

**Citation:** Soares et al., JINT 2023.  
**Status:** Peer-reviewed and published.  
**Full-text source:** Official Springer PDF, DOI 10.1007/s10846-023-02019-6.  
**Sections audited:** Dynamic-versus-changing problem definition; ORB-SLAM3
Atlas integration; dynamic filtering; object belief; long-term association;
experiments; output description.

**Short original evidence:**
> “The output is the pose of the camera frame by frame ... and the sparse map clear of outliers.”

**Source location:** Sec. 4, PDF p. 5.

**What the paper actually implements:** Dynamic-keypoint filtering, movable
object tracking, an object-level Bayesian belief map and long-term association
inside ORB-SLAM3. It targets both objects moving in front of the robot and
objects changed after an area was mapped.

**Allowed conclusion:** Major conceptual predecessor spanning visible dynamics
and changed-scene localization/mapping.

**Boundary:** Its geometric map remains ORB-feature sparse and the primary
quantitative output is camera trajectory robustness. The paper does not specify
or evaluate the explicit completed-process export/import protocol used in our
strict D3 definition.

**Do not write:** That no previous SLAM system considered both currently moving
and previously moved objects.

**Coverage:** D1 yes for tracking/filtering; D2 yes/partial; D3 not explicitly
validated as process-separated persistence.

---

## 9. Khronos

**Citation:** Schmid et al., RSS 2024.  
**Status:** Peer-reviewed and published.  
**Full-text source:** official RSS PDF.  
**Sections audited:** SMS problem statement; active temporal window; global
optimization; deformable change detection and reconciliation; experiments;
limitations.

**Short original evidence:**
> “A fast process tracks short-term dynamics, while a slower process reasons over long-term changes.”

**Source location:** Abstract; the two processes are formalized in Secs. IV--V.

**What the paper actually implements:** Dense spatio-temporal metric-semantic
mapping in one evolving temporal sequence. The active window represents visible
motion; global optimization and reconciliation reason about abrupt changes over
observation gaps using fragments, deformation and ray evidence.

**Allowed conclusion:** The closest complete D1+D2 system and the direct
technical foundation of this project.

**Boundary from the full protocol:** The paper formulates and evaluates one
continuously evolving SMS problem. It does not specify or evaluate a completed
Session-A export, independent Session-B import, and recurring process-separated
continuation protocol. This is a carefully bounded absence statement, not a
claim that the representation could never be extended.

**Do not write:** That Khronos lacks long-term changes, or that we invented its
D1/D2 mechanisms.

**Coverage:** D1 yes; D2 yes; D3 not specified/evaluated.

---

## 10. Panoptic Multi-TSDFs

**Citation:** Schmid et al., ICRA 2022.  
**Status:** Peer-reviewed and published.  
**Full-text source:** arXiv:2109.10165.  
**Sections audited:** Representation; submap activity and map management; TSDF
conflict/match logic; experiments; related-work boundary and future work.

**Short original evidence:**
> “However, this is left for future work.”

**Source location:** Sec. II, PDF p. 3, referring to short-term object tracking.

**What the paper actually implements:** Active and inactive volumetric object
and background submaps, with inactive entities classified as persistent, absent
or unobserved from current surface/free-space agreement. Camera poses are
provided externally.

**Allowed conclusion:** Strong dense D2/D3-style map-consistency baseline and a
source for persistent/absent/unobserved semantics.

**Do not write:** That the paper already contains Khronos-like D1 trajectory
tracking; it explicitly leaves that direction for future work.

**Coverage:** D1 no; D2 partial; D3 yes/partial through prior-run/current-run
submap consistency.

---

## 11. Efficient Long-Term Mapping in Dynamic Environments

**Citation:** Lázaro, Capobianco and Grisetti, IROS 2018.  
**Status:** Peer-reviewed and published.  
**Full-text source:** author-accessible full text; DOI 10.1109/IROS.2018.8594310.  
**Sections audited:** Problem definition; pose-graph and local-map update;
inter-/intra-session loop closure; graph pruning; experiments.

**Short original evidence:**
> “The environment across a single or multiple mapping sessions.”

**Source location:** Abstract; multi-session graph handling is detailed in the
method.

**What the paper actually implements:** A full 2D pose-graph SLAM system that
maintains up-to-date local point-cloud maps and removes outdated graph parts over
single or multiple sessions.

**Allowed conclusion:** Direct D3 geometric-map-maintenance precedent.

**Do not write:** That it preserves moving-object trajectories or a dense 3D
metric-semantic history.

**Coverage:** D1 no explicit object history; D2 partial map maintenance; D3 yes.

---

## 12. POCD

**Citation:** Qian et al., RSS 2022.  
**Status:** Peer-reviewed and published.  
**Full-text source:** arXiv:2205.01202 / official RSS paper.  
**Sections audited:** Semi-static problem definition and assumptions;
object-level TSDF representation; Gaussian--Beta state; Bayesian update;
experiments and dataset description; conclusion.

**Short original evidence:**
> “The environment contains static objects that change between runs.”

**Source location:** Dataset description, PDF p. 2.

**What the paper actually implements:** Probabilistic object-level volumetric
mapping for changes between robot runs. It combines geometric change and object
stationarity in a Gaussian--Beta state.

**Important assumptions:** The modeled objects are bounded and rigid; object
type/dimensions and localization are supplied; the evaluated changes occur
between traversals.

**Allowed conclusion:** Strong D3 probabilistic object-map baseline and a
possible source for cross-run object beliefs.

**Do not write:** That POCD is mainly D2, or that it outputs the complete
continuous trajectory of an object moving in the current run.

**Coverage:** D1 no; D2 not its primary taxonomy; D3 yes.

---

## 13. POV-SLAM

**Citation:** Qian et al., RSS 2023.  
**Status:** Peer-reviewed and published.  
**Full-text source:** arXiv:2307.00488 / official RSS paper.  
**Sections audited:** Semi-static problem and likelihood; variational inference;
pose/object joint factor graph; synthetic and warehouse experiments; conclusion.

**Short original evidence:**
> “We stitch two trajectories captured along the same route four months apart.”

**Source location:** Warehouse experiment, PDF p. 11.

**What the paper actually implements:** Joint robot-pose and semi-static object
consistency estimation using variational inference, evaluated on repeated visits
including warehouse traversals separated by months.

**Allowed conclusion:** D3 SLAM baseline addressing pose/change ambiguity.

**Do not write:** That POV-SLAM is principally D2, or that it represents
Khronos-style continuous dynamic trajectories and temporal geometry.

**Coverage:** D1 no complete dynamic history; D2 not primary; D3 yes.

---

## 14. ObVi-SLAM

**Citation:** Adkins, Chen and Biswas, RA-L 2024.  
**Status:** Peer-reviewed and published.  
**Full-text source:** arXiv:2309.15268 / IEEE article.  
**Sections audited:** Long-term problem statement; deployment-time estimator;
long-term map extraction; prior use; multi-deployment experiments; limitations.

**Short original evidence:**
> “ObVi-SLAM builds an uncertainty-aware long-term map of persistent objects and updates it after every deployment.”

**Source location:** Abstract; the two-stage architecture is detailed in the
method.

**What the paper actually implements:** A sparse visual SLAM system coupled to a
persistent-object map, where the previous deployment's object map becomes a
prior for the next deployment. Evaluation spans 16 sessions.

**Allowed conclusion:** Strong D3 localization and persistent-object-memory
precedent.

**Do not write:** That it reconstructs dense dynamic geometry, D1 trajectories,
or full D2 scene change.

**Coverage:** D1 no; D2 no complete reconstruction; D3 yes.

---

## 15. Living Scenes

**Citation:** Zhu et al., CVPR 2024.  
**Status:** Peer-reviewed and published.  
**Full-text source:** arXiv:2312.09138 / CVPR Open Access.  
**Sections audited:** Problem setting; object matching; registration;
reconstruction; experiments and assumptions; conclusion.

**Short original evidence:**
> “Due to the long gaps between captures, modeling the objects' intermediate motions is infeasible.”

**Source location:** Introduction.

**What the paper actually implements:** Multi-object matching, registration and
incremental reconstruction from instance-segmented scans captured at irregular
times. Unmatched instances are treated as added or removed.

**Allowed conclusion:** Strong D3 scan-to-scan object correspondence and
reconstruction baseline.

**Do not write:** That it is an online SLAM system, models visible continuous
motion, or maintains a dense evolving background map.

**Coverage:** D1 no; D2 no; D3 yes in cross-time scan reconstruction.

---

## 16. Gaussian Mapping for Evolving Scenes (GaME)

**Citation:** Yugay et al., CVPR 2026.  
**Status:** Peer-reviewed and published.  
**Full-text source:** arXiv:2506.06909 / CVPR Open Access.  
**Sections audited:** Problem definition; external inputs; dynamic-scene
adaptation; add/remove rules; keyframe masking; experiments; limitations.

**Short original evidence:**
> “GaME processes depth and color images ... using camera poses and panoptic segmentation from external estimators.”

**Source location:** Method overview, Sec. 4.

**What the paper actually implements:** Online maintenance of an evolving 3D
Gaussian map, with new geometry added and contradicted geometry removed while
stale keyframe pixels are masked from multi-view optimization.

**Allowed conclusion:** Strong dense hidden-change and evolving-representation
baseline, especially for out-of-view changes.

**Do not write:** That GaME jointly solves camera SLAM, retains object
trajectories, or evaluates a process-separated persistent-session protocol. Its
objective is primarily map/rendering quality.

**Coverage:** D1 not principal; D2 yes; D3 not specified/evaluated as our strict
protocol.

---

## 17. OASIS-Map

**Citation:** Oh et al., arXiv:2607.14899.  
**Status:** **UNDER REVIEW / PREPRINT as of 2026-08-06; not yet a peer-reviewed
publication.**  
**Full-text source:** arXiv:2607.14899 and the official project page.  
**Sections audited:** Session definitions; per-session front end;
cross-session association; change-state definitions; experiments; limitations.

**Short original evidence:**
> “The system takes two mapping sessions as input: a previous, completed session and a current, ongoing session.”

**Source location:** System overview.

**What the paper actually implements:** Per-session object maps followed by
cross-session semantic correspondence and association, outputting static,
appeared, disappeared, moved and unknown object states. Robot poses come from a
separate multi-session LiDAR SLAM system.

**Allowed conclusion:** Important concurrent D3 object-association and
change-detection work.

**Do not write:** That it supplies D1 trajectories, same-session D2
spatio-temporal mapping, dense background memory, or a peer-reviewed result.

**Coverage:** D1 no; D2 no under this project's taxonomy; D3 yes.

**Submission action:** Recheck publication status immediately before submission.
If accepted, replace the `@misc` entry with its formal venue. If still under
review, retain the explicit preprint label or remove it according to the final
narrative and venue policy.

---

## Evidence-backed synthesis

The full-text audit supports the following restrained positioning:

1. **A broad first-unification claim is false or at least indefensible.**
   Pomerleau et al. already combine long-term point-map update and dynamic-point
   velocity estimation; Changing-SLAM combines current dynamics and changed
   objects in sparse visual SLAM.
2. **Khronos is the closest dense D1+D2 system.** Its paper does not specify or
   evaluate the strict process-separated D3 recurrence proposed here.
3. **POCD, POV-SLAM, ObVi-SLAM, Living Scenes and OASIS-Map are primarily D3
   methods under this taxonomy.** They must not be mislabeled as same-session D2
   simply because the physical transition was unobserved.
4. **Panoptic Multi-TSDFs and GaME are strong dense change-maintenance
   precedents.** Panoptic explicitly lacks short-term tracking; GaME uses
   external poses/segmentation and optimizes an evolving Gaussian/NVS map.
5. The remaining defensible research gap is a **dense metric-semantic
   spatio-temporal SLAM recurrence** in which every independent session imports
   persistent scene memory, performs both D1 and D2, reconciles D3, and exports
   the prior for the next session.

This is a working literature conclusion, not a permanent first claim. The audit
must be refreshed before submission, especially for concurrent 2026 work.