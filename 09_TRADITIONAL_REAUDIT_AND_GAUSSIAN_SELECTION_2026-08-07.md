# Traditional Mapping Re-Audit and Gaussian Selection

Status checked: **2026-08-07**

This note records two decisions for the manuscript:

1. the Related Work should be centered on traditional metric, volumetric,
   object-level, and scene-memory mapping because these methods share our map
   outputs and are the most plausible experimental baselines;
2. Gaussian literature should be represented by a small number of papers that
   mark the D1, D2, and D3 boundaries, while the broader Gaussian audit remains
   available internally.

The authoritative storyline remains:

```text
D1 + D2 = dynamic mapping inside every continuously running session
D3      = persistent scene-memory continuation across completed sessions
```

## Gaussian papers retained in the manuscript

### 1. 4D Gaussian Splatting SLAM — D1 representative

- **Status:** ICCV 2025, published.
- **Why retain:** It is a clear recent example of explicitly representing motion
  observed in a continuous sequence rather than suppressing dynamic objects.
- **Short source evidence:** “Instead of removing dynamic objects as distractors.”
- **Location:** Abstract, PDF p. 1.
- **Boundary:** It does not infer a hidden rearrangement with no observed
  intermediate motion and does not import a completed map into a later session.
- **Baseline role:** Related-work comparison only. Its radiance-field outputs and
  rendering metrics are not directly comparable to our mesh/TSDF current-map and
  change-state evaluation.

### 2. GaME — D2 representative

- **Status:** CVPR 2026, published.
- **Why retain:** It is the closest recent Gaussian method for an online map that
  changes while the affected area is outside the current view.
- **Short source evidence:** “the scene evolving through changes out of view.”
- **Location:** Abstract, PDF p. 1.
- **Boundary:** It receives camera poses and panoptic segmentation externally,
  does not retain visible dynamic trajectories, and does not evaluate a
  completed-A export / independent-B import protocol.
- **Baseline role:** Potential qualitative or rendered-depth comparison only if
  inputs can be aligned; not a required primary baseline for the current
  metric-semantic map task.

### 3. LT-Gaussian — D3 map-update representative

- **Status:** IEEE IV 2025, published.
- **Why retain:** It explicitly updates an old Gaussian map using later LiDAR
  observations, making it a relevant recent D3 map-revision component.
- **Short source evidence:** “emerging and disappearing points are selected.”
- **Location:** Fig. 3 caption and Sec. III-B, PDF p. 4.
- **Boundary:** It does not retain D1 histories, does not implement a complete
  D1+D2 session, and does not explicitly separate unobserved prior geometry from
  evidence-confirmed absence.
- **Baseline role:** Possible D3 geometry-update comparator if code/data are
  available, but its rendering-oriented Gaussian output is not directly
  equivalent to our scene-memory output.

## Gaussian papers removed from the main Related Work

The following remain in `07_GAUSSIAN_FULL_TEXT_EVIDENCE_AUDIT_2026-08-06.md`
and `manuscript/gaussian.bib`, but are not currently cited in the manuscript:

- Gaussian Splatting SLAM and SplaTAM: static Gaussian foundations;
- WildGS-SLAM and Gassidy: dynamic-input robust static Gaussian maps;
- D4DGS-SLAM, DynaGSLAM, Flow4DGS-SLAM, and RU4D-SLAM: additional D1 variants;
- GS-LTS: relevant D3 editing preprint, but explicitly excludes real-time
  dynamics;
- GS-DIFF: pairwise Gaussian change detector, not SLAM or persistent map update.

These papers are scientifically relevant but adding all of them would overstate
Gaussian comparability and displace more relevant volumetric and object-map
literature.

## Traditional papers added after the re-audit

### MID-Fusion

- **Citation:** Xu et al., ICRA 2019, DOI 10.1109/ICRA.2019.8794371.
- **Sections checked:** system overview, object tracking, volumetric fusion,
  experiments, conclusion.
- **Short source evidence:** “continuously estimate geometric, semantic, and motion properties.”
- **Representation:** one octree-based volumetric model per object plus static
  background; color, depth, semantics, and foreground probabilities are fused.
- **Correct role:** strong dense object-level D1 predecessor.
- **Boundary:** relies on continuous object observations; no D2 change-state
  reasoning and no D3 session memory.
- **Baseline feasibility:** possible D1 qualitative/quantitative baseline if the
  original stack can be reproduced, but not a D3 baseline.

### EM-Fusion

- **Citation:** Strecke and Stückler, ICCV 2019, DOI 10.1109/ICCV.2019.00596.
- **Sections checked:** representation, EM data association, occlusion handling,
  tracking, mapping, experiments, limitations.
- **Short source evidence:** “rigid objects in local volumetric signed distance function maps.”
- **Representation:** background and rigid objects as local SDF volumes;
  probabilistic pixel association and occlusion reasoning.
- **Correct role:** highly relevant dense probabilistic D1 predecessor.
- **Boundary:** no hidden-change state after an object leaves the observation
  stream and no process-separated memory continuation.
- **Baseline feasibility:** potentially comparable for D1 object reconstruction,
  but not for D2/D3.

### DynaSLAM II

- **Citation:** Bescos et al., RA-L 2021, DOI 10.1109/LRA.2021.3068640.
- **Sections checked:** object tracking, joint bundle adjustment, temporal object
  boxes, experiments, conclusion and limitations.
- **Short source evidence:** “tightly integrates the multi-object tracking capability.”
- **Representation:** feature-based static and dynamic structure, camera and
  object trajectories, and temporal 3D boxes.
- **Correct role:** strong joint-estimation D1 reference.
- **Boundary:** feature-based representation; no D2 persistent/absent/unobserved/new
  scene reconciliation and no D3 memory.
- **Baseline feasibility:** D1 trajectory baseline where compatible annotations
  exist; not a dense-map D3 baseline.

### VDO-SLAM

- **Status:** arXiv manuscript/preprint record; final publication status was not
  verified on 2026-08-07, so it is not cited in the current manuscript.
- **Sections checked:** unified dynamic formulation, object motion estimation,
  spatio-temporal map, evaluation, conclusion/future work.
- **Short source evidence:** “the full SE(3) motion of the objects.”
- **Correct role:** important D1 spatio-temporal feature-map reference.
- **Boundary:** long-term graph summarization and bounded history are future
  directions; no D2/D3.
- **Action:** retain in the audit/watchlist and cite only after confirming a
  peer-reviewed publication record or deciding that an arXiv citation is needed.

### Building Volumetric Beliefs for Dynamic Environments

- **Citation:** Mersch et al., RA-L 2023, DOI 10.1109/LRA.2023.3292583.
- **Sections checked:** scan/local-map segmentation, sparse 4D CNN, Bayesian
  volumetric fusion, online experiments, conclusion.
- **Short source evidence:** “which parts of the environment can be occupied by moving objects.”
- **Representation:** a probabilistic local volumetric belief derived from
  moving-object segmentation.
- **Correct role:** D1-related probabilistic motion evidence and static-world
  maintenance.
- **Boundary:** it does not estimate object trajectories or persistent D2/D3
  scene elements.
- **Baseline feasibility:** useful component/ablation inspiration; not a direct
  full-system baseline.

### Ray-Bundle-Impact-Factor (RBIF) map maintenance

- **Citation:** Breitfuss et al., IROS 2024,
  DOI 10.1109/IROS58592.2024.10802029.
- **Sections checked:** map-maintenance architecture, ray classification,
  probabilistic ray/voxel interference, synthetic and real experiments.
- **Short source evidence:** “real-time incorporation of 3D LiDAR scans.”
- **Representation:** discretized 3D occupancy/localization map updated by
  probabilistic interference between ray bundles and occupied voxels.
- **Correct role:** recent traditional D3 geometric-map-maintenance reference.
- **Important difference:** RBIF distinguishes partial voxel traversal from full
  contradictory traversal and explicitly addresses hole formation, but it does
  not preserve object identity, semantic change states, dynamic trajectories, or
  a complete D1+D2 session history.
- **Baseline feasibility:** one of the most relevant geometric D3 comparators if
  an implementation can be obtained or reimplemented under the same map type.

## Other located work not yet promoted to the manuscript

- **ReFusion:** strong TSDF-based dynamic-input static reconstruction; useful D1
  robustness reference, but removed entities are not retained.
- **DetectFusion / StaticFusion / FlowFusion:** important dynamic-scene dense
  mapping variants, but largely redundant once Co-Fusion, MID-Fusion,
  EM-Fusion, Dynablox, and DynaSLAM II are represented.
- **AirDOS:** articulated-object D1 factor-graph method and 4D map; relevant if
  articulated motion becomes part of the method or evaluation.
- **LTC-Mapping:** semantic object-map maintenance with visibility and repeated
  non-detection reasoning; requires further full-text session-structure audit.
- **Safe and Robust Map Updating for Long-Term Operations:** localization-driven
  map update with uncertainty; primarily a 2D/localization setting.
- **MTD-Map and Chamelion:** recent 2026 preprints potentially relevant to
  unified removal/change detection and construction-site change; do not cite
  until publication status and full overlap are audited.

## Manuscript selection rule

A work belongs in the main Related Work only if it satisfies at least one of:

1. it is a central D1, D2, or D3 technical predecessor;
2. it is a serious novelty threat;
3. it can plausibly be evaluated as a baseline under compatible inputs and
   outputs;
4. it represents a major current trend with one concise representative citation.

The complete audits may contain many more papers than the manuscript. Citation
count is not evidence quality, and representation-incompatible methods should
not dominate a paper whose experiments use metric-semantic meshes, TSDFs, object
memories, and ray evidence.
