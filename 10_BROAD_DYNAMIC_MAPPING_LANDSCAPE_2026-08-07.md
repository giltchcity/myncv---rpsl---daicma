# Broad Dynamic-Mapping Literature Landscape

Status checked: **2026-08-07**

This document is a high-recall candidate map, not a claim that the search is
mathematically exhaustive. Its purpose is to identify the major research
families that call themselves dynamic mapping, dynamic SLAM, 4D reconstruction,
long-term mapping, lifelong mapping, scene memory, or changing-scene mapping.

The authoritative project hierarchy remains:

```text
D1 + D2 = dynamic mapping inside every continuously running session
D3      = persistent scene-memory continuation across completed sessions
```

A paper is not cited in the manuscript merely because it appears here. Audit
levels are:

- **FULL**: original full paper inspected across problem, method, experiments,
  and limitations;
- **PRIMARY**: official paper/project page and method description inspected, but
  the full audit ledger is incomplete;
- **DISCOVERY**: located during broad search; no manuscript claim may rely on it
  until the full text is inspected.

## 1. Dynamic-robust SLAM and static-map cleaning

These methods treat moving content mainly as interference. Their output is a
more reliable camera trajectory and a static or cleaned map, rather than a
history of dynamic entities.

| Work | Representation / goal | Role | Audit |
|---|---|---|---|
| DynaSLAM (RA-L 2018) | sparse visual SLAM + dynamic masking + inpainting | D1 measurements rejected | FULL |
| DS-SLAM (IROS 2018) | semantic + motion-consistency filtering | robust static SLAM | DISCOVERY |
| Dynamic-SLAM (RAS 2019) | semantic feature rejection | robust static SLAM | DISCOVERY |
| ReFusion (2019) | voxel-hashed TSDF + residual/free-space dynamic detection | cleaned static dense map | DISCOVERY |
| Dynablox (RA-L 2023) | volumetric free-space evidence | D1 moving-point detection | FULL |
| Building Volumetric Beliefs (RA-L 2023) | LiDAR voxel belief + Bayesian filtering | dynamic occupancy/static-map support | FULL |
| NID-SLAM (2024) | neural implicit map + semantic/geometric masking | robust static neural SLAM | DISCOVERY |
| DDN-SLAM (RA-L 2025) | neural implicit RGB-D map + semantic dynamic handling | dense robust mapping | PRIMARY |
| DVN-SLAM (ICRA 2025) | local-global neural implicit map | robust neural SLAM | DISCOVERY |
| WildGS-SLAM (CVPR 2025) | uncertainty-weighted Gaussian map | static Gaussian map in dynamic inputs | FULL |
| Gassidy (ICRA 2025) | loss-flow dynamic pruning in Gaussian SLAM | static Gaussian map | FULL |
| Dynamic Visual SLAM using a General 3D Prior (CVPR 2026) | learned dynamic-region filtering + patch BA | robust localization/reconstruction | PRIMARY |
| DROID-SLAM in the Wild (CVPR 2026) | uncertainty-aware differentiable BA | robust dynamic-scene SLAM | PRIMARY |
| DAGS-SLAM (preprint 2026) | per-Gaussian motion probability | static/robust GS-SLAM | DISCOVERY |
| Dynamic 3D Gaussian SLAM via Motion Suppression (ESWA 2026) | semantic-depth filtering + incremental Gaussian repair | static Gaussian map | DISCOVERY |

**Positioning:** this family is important for D1 robustness but does not solve
our scene-memory problem unless dynamic entities and hidden changes are retained
as explicit state.

## 2. Explicit rigid-object D1 mapping

These methods reconstruct or estimate objects that move while continuously
observed.

| Work | Representation / output | Audit |
|---|---|---|
| Co-Fusion (ICRA 2017) | background + per-object surfel models | FULL |
| MaskFusion (ISMAR 2018) | semantic instance surfel models | FULL |
| MID-Fusion (ICRA 2019) | per-object octree volumes | FULL |
| EM-Fusion (ICCV 2019) | per-object SDFs + probabilistic data association | FULL |
| Dynamic SLAM: The Need for Speed (2020) | model-free rigid-object velocity map | PRIMARY |
| VDO-SLAM (2020) | object motion + spatio-temporal feature map | DISCOVERY |
| DymSLAM (2020) | dense static map + rigid-object models and trajectories | PRIMARY |
| DynaSLAM II (RA-L 2021) | tightly coupled camera/object BA + temporal boxes | FULL |
| AirDOS (2021) | articulated dynamic object constraints | DISCOVERY |
| DynoSAM (T-RO 2025) | robot/object smoothing and mapping framework | FULL |
| DYNEMO-SLAM (preprint 2025) | dynamic-entity-aware 3D scene-graph factor graph | PRIMARY |
| Dynamic Situational Graphs (IROS 2025) | hierarchical DSG with dynamic entity constraints | PRIMARY |

**Positioning:** these are D1 systems. Some use persistent object landmarks or
motion priors, but none is automatically D2 or D3 without an explicit
observation-gap or completed-session protocol.

## 3. Non-rigid and persistent 4D reconstruction

This family targets complete dynamic geometry and object permanence over one
video or sensor stream. It is adjacent to D1 and may inform the representation
of dynamic histories, but most systems are not long-term robot map maintainers.

| Work | Representation / target | Audit |
|---|---|---|
| DynamicFusion (CVPR 2015) | canonical TSDF + non-rigid deformation | PRIMARY |
| VolumeDeform (ECCV 2016) | volumetric deformation graph | PRIMARY |
| SurfelWarp (2019) | surfel non-rigid reconstruction | PRIMARY |
| 4DTAM (CVPR 2025) | dynamic surface Gaussians + camera/non-rigid tracking | PRIMARY |
| BA-Track / Back on Track (ICCV 2025) | dynamic-scene bundle adjustment | DISCOVERY |
| Dynamic Point Maps (ICCV 2025) | feed-forward dynamic point map | DISCOVERY |
| C4D (ICCV 2025) | 4D reconstruction | DISCOVERY |
| 4D Primitive-Mache (CVPR 2026 Oral) | replayable rigid primitives + object permanence | PRIMARY |
| 4DSurf (CVPR 2026) | temporally consistent dynamic surfaces | PRIMARY |
| DynamicVGGT (CVPR 2026) | dynamic point maps and Gaussian velocities | PRIMARY |
| Any4D (CVPR 2026) | metric feed-forward 4D reconstruction | PRIMARY |
| SLARM (CVPR 2026) | streaming language-aligned dynamic reconstruction | PRIMARY |
| MotionScale (CVPR 2026) | scalable 4D Gaussian motion field | PRIMARY |
| MoVieS / MoRe (CVPR 2026) | feed-forward monocular 4D reconstruction | DISCOVERY |

**Key boundary:** object permanence inside one continuous video is not D3. A
strict D3 system needs a completed Session A memory package imported into an
independent Session B.

## 4. Single-session hidden change and unified D1+D2

| Work | Main idea | Correct role | Audit |
|---|---|---|---|
| Detection and Tracking of General Movable Objects (T-RO 2019) | local motion + global jumps under partial observation | object-level D2 | FULL |
| Changing-SLAM (JINT 2023) | dynamic filtering + persistence belief + association | sparse D1+D2 | FULL |
| Khronos (RSS 2024) | active-window D1 + global-reconciliation D2 | dense D1+D2 base | FULL |
| GaME (CVPR 2026) | online Gaussian revision after out-of-view changes | dense Gaussian D2 component | FULL |
| SuperMap (RSS 2026) | open-vocabulary 4D scene graph, identity/confidence updates, appearance/disappearance/relocation | very close persistent semantic memory; strict D3 boundary still under audit | PRIMARY |
| LTC-Mapping (Sensors 2022) | object boxes, visibility, detections/non-detections, confidence decay | long-term object semantic map; session structure unspecified | PRIMARY |
| MoPe (preprint 2026) | persistent dynamic posterior in Gaussian mapping | temporal D1 robustness / memory principle | DISCOVERY |

**SuperMap warning:** its public evidence shows a continuous two-hour deployment,
persistent object identities, existence-and-label confidence, temporal edges, and
change detection. It is a major novelty neighbour. Until the full paper audit is
complete, do not claim that it lacks or provides strict completed-A/independent-B
continuation.

## 5. Cross-session geometric map maintenance (D3)

| Work | Representation / update | Audit |
|---|---|---|
| Dynamic Maps for Long-Term Operation (RSS 2005) | multiple temporal 2D maps | DISCOVERY |
| Dynamic Pose Graph SLAM (IROS 2012) | edit old poses/scans after change detection | PRIMARY |
| Generic NDT Mapping / Lifelong SLAM (RAS 2015) | NDT local-map maintenance | DISCOVERY |
| Long-Term 3D Map Maintenance (ICRA 2014) | point-level static/dynamic probabilities and velocity | FULL |
| Efficient Long-Term Mapping (IROS 2018) | multi-session pose graph + local-map replacement | FULL |
| Safe and Robust Map Updating (Sensors 2023) | conservative occupancy-map update | DISCOVERY |
| SLAM-RAMU (Industrial Robot 2024) | LiDAR-IMU relocalization and autonomous update | PRIMARY |
| RBIF (IROS 2024) | probabilistic ray-bundle/voxel interference | FULL |
| Lifelong 3D Mapping Framework (preprint 2025) | dynamic removal, multi-session alignment, change version control | PRIMARY |
| LLMF (2026) | BEV/FV projection alignment and change update over 32 runs | PRIMARY |
| ProbPer-LiLo (RA-L 2026) | factor-graph object persistency + multi-session map refinement | HIGH-PRIORITY PRIMARY |
| Online Multi-Session RTAB-Map (2024) | global loop closure and memory management | PRIMARY |

**Positioning:** these are strong D3 baselines/components for geometry and map
maintenance. Most intentionally produce a clean current localization map rather
than a dense D1+D2 scene history.

## 6. Cross-session object, semantic, and scene-graph memory

| Work | Representation / goal | Audit |
|---|---|---|
| Panoptic Multi-TSDFs (ICRA 2022) | active/inactive TSDF submaps, persistent/absent/unobserved | FULL |
| POCD (RSS 2022) | Gaussian-Beta object geometry/stationarity belief | FULL |
| POV-SLAM (RSS 2023) | variational pose + semi-static object consistency | FULL |
| ObVi-SLAM (RA-L 2024) | persistent object landmarks across deployments | FULL |
| Living Scenes (CVPR 2024) | cross-time object association and accumulated reconstruction | FULL |
| OASIS-Map (under-review preprint 2026) | cross-session object correspondence and change states | FULL / status marked |
| 3D Variable Scene Graph (ICRA 2023) | semantic variability prior | PRIMARY |
| Scene Graph Memory (ICML 2023) | partially observable dynamic graph memory for object search | PRIMARY, not SLAM |
| Long-term Object Search with Incremental Scene Graph (Robotica 2023) | continuously updated semantic scene graph | PRIMARY, navigation-oriented |
| SuperMap (RSS 2026) | queryable open-vocabulary 4D instance scene graph | HIGH-PRIORITY PRIMARY |

This family is central to the representation side of our paper. It often has
better identity and semantic memory than geometric-map systems, but may lack a
dense current background map, D1 temporal geometry, or a strict D3 recursion.

## 7. Predictive and periodic maps of dynamics

These works model *when* occupancy or motion patterns recur rather than only
maintaining the latest scene state.

| Work | Mathematical direction | Audit |
|---|---|---|
| Occupancy Grid Models for Changing Environments (AAAI 2012) | HMM transition probabilities per cell | PRIMARY |
| Spectral Analysis for Long-Term Mapping (2014) | frequency-domain temporal model | PRIMARY |
| FreMEn (T-RO 2017) | spectral periodicity and future-state prediction | PRIMARY |
| Spatio-Temporal Hilbert Maps (NeurIPS 2016) | continuous spatial-temporal kernel occupancy | PRIMARY |
| Bayesian Hilbert Maps (CoRL 2017) | sequential Bayesian continuous occupancy | PRIMARY |
| Spatio-Temporal Exploration (RAS 2017) | information gathering for never-ending temporal maps | PRIMARY |
| Long-Term Navigation via Spatio-Temporal Map Prediction (RAS 2024) | ARMA object/map prediction + Bayesian correction | PRIMARY |
| Maps of Dynamics for Long-Term Human Motion Prediction (RA-L 2025) | environment-conditioned trajectory prediction | PRIMARY |

These are unlikely direct baselines for current-map mesh F1, but they are strong
mathematical sources for priors, time-dependent persistence, uncertainty, and
active re-observation.

## 8. Neural implicit dynamic maps

| Work | Main direction | Audit |
|---|---|---|
| iMAP / NICE-SLAM | static neural implicit SLAM foundations | PRIMARY |
| NID-SLAM (2024) | dynamic masking in neural implicit RGB-D SLAM | PRIMARY |
| DDN-SLAM (RA-L 2025) | dense dynamic neural implicit SLAM | PRIMARY |
| DVN-SLAM (ICRA 2025) | local-global dynamic neural map | PRIMARY |
| DMN-SLAM (IEEE Access 2025) | multi-MLP dynamic neural SLAM | DISCOVERY |
| Neural Radiance Field Dynamic Scene SLAM (2025) | semantic/ray segmentation and BA | DISCOVERY |

The current neural implicit literature largely focuses on robust tracking and
clean reconstruction under moving interference. It is a separate representation
branch and should not dominate our Related Work unless the final method adopts a
learned implicit memory.

## 9. Gaussian representatives for the manuscript

The manuscript should contain **six or seven**, not every Gaussian paper found.
The recommended set spans distinct roles:

1. **WildGS-SLAM (CVPR 2025)** - dynamic-input robust static Gaussian map;
2. **4DTAM (CVPR 2025)** - non-rigid online D1 tracking/mapping;
3. **4D Gaussian Splatting SLAM (ICCV 2025)** - explicit static/dynamic Gaussian D1 SLAM;
4. **DynaGSLAM (WACV 2026)** - real-time D1 rendering, tracking and motion prediction;
5. **GaME (CVPR 2026)** - online D2 evolving-map update;
6. **LT-Gaussian (IV 2025)** - D3 old-map/current-traversal update component;
7. **GS-LTS (preprint 2025, optional)** - service-robot semantic Gaussian revision, explicitly excluding real-time dynamics.

All other Gaussian works remain in the full audit/watchlist. The selected set
shows the complete field split without implying direct metric comparability.

## 10. Long-term localization and experience maps

Experience-based navigation, multi-experience localization, place recognition,
and multi-session loop closure are necessary infrastructure for D3, but they
usually maintain localization references rather than evolving scene content.
Representative directions include Experience-Based Navigation, multi-experience
visual localization, RTAB-Map global multi-session loop closure, and uncertainty-
aware long-term place recognition. These should be cited only if pose/session
alignment becomes part of the final method or experiments.

## 11. What appears genuinely closest now

Priority order for novelty analysis:

1. **SuperMap (RSS 2026)** - persistent open-vocabulary 4D scene graph and change-aware identities;
2. **Khronos (RSS 2024)** - dense single-session D1+D2;
3. **ProbPer-LiLo (RA-L 2026)** - probabilistic multi-session persistency and refinement;
4. **Panoptic Multi-TSDFs / POCD / POV-SLAM** - dense/object D3 foundations;
5. **DYNEMO-SLAM / Dynamic Situational Graphs** - dynamic entities inside a scene-graph SLAM backend;
6. **4D Primitive-Mache** - persistent/replayable dynamic reconstruction and object permanence within one stream;
7. **GaME / LT-Gaussian / GS-LTS** - representation-adjacent D2/D3 map revision;
8. **LTC-Mapping** - visibility and non-detection reasoning in object semantic maps;
9. **FreMEn / Hilbert-map family** - mathematical temporal and predictive memory.

## 12. Baseline implications

### Likely executable or composable baselines

- Khronos;
- Panoptic Multi-TSDFs;
- POCD / POV-SLAM where data assumptions can be met;
- RBIF or a faithfully implemented ray-update baseline;
- ProbPer-LiLo if code/data become available;
- SuperMap for object/change state if its released interface can ingest our data;
- naive union, B-only, overwrite, ray-only, and hard-state ablations.

### Related-work only unless a common protocol is constructed

- 4DTAM / 4DGS-SLAM / DynaGSLAM;
- feed-forward 4D reconstruction;
- FreMEn and Hilbert-map predictors;
- Scene Graph Memory and object-search methods;
- rendering-oriented Gaussian map editors.

## 13. Next audit queue

The immediate full-text queue is versioned separately. No broad-search candidate
should be used to make a novelty claim until it has an evidence-ledger entry with
original section/page anchors.
