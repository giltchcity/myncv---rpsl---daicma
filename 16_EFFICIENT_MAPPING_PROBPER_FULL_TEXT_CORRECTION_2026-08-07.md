# Full-Text Correction: Efficient Long-Term Mapping and ProbPer-LiLo

Status checked: **2026-08-07**

This note corrects earlier overstatements about two lifelong-mapping papers. Both
original PDFs were read across problem definition, method, experiments, figures,
and conclusion.

## Canonical project taxonomy

```text
D1 = observed object motion represented as a real trajectory and time-indexed geometry
D2 = hidden change during an observation gap in the same running session
D3 = completed Session A exports persistent state; independent Session B imports it,
     reconciles inter-session change, runs new D1+D2, and exports state for C
```

## 1. Efficient Long-Term Mapping in Dynamic Environments, IROS 2018

### What the paper actually means by single-session dynamics

The paper states that it handles highly dynamic situations inside a session and
map updates across multiple sessions. However, its intra-session component is not
D1 or D2 scene modeling. It is a 2D local-map cleaning procedure:

- consecutive laser scans are registered using normal-based ICP;
- points are projected into common range-bearing bins;
- if a new ray passes behind an old point, the old point is replaced;
- if a new return lies in front of an old point, it is added;
- nearby returns are averaged;
- the result is a cleaner local point cloud with traces from people and other
  non-static obstacles suppressed.

No dynamic entity is instantiated. The method does not estimate object identity,
motion, trajectory, bounding boxes, or time-indexed dynamic geometry. It also
does not distinguish an observed D1 motion from an unobserved D2 transition.

### What the cross-session component does

Each graph node contains a 2D local point-cloud map and discretized robot
trajectory waypoints. In the multi-session experiment, a new session starts from
the graph produced by the preceding session; initial global localization is
assumed. Inter- or intra-session loop closure triggers local-cloud fusion. The
newer cloud is refined against the older one, the two are merged using the same
ray/depth rules, the old graph node is removed, and condensed measurements
preserve graph coherence.

This is genuine multi-session current-map maintenance. It preserves an updated
pose graph and local maps, not a dynamic scene memory.

### Correct relationship to this project

The paper establishes the engineering pattern:

```text
clean dynamic clutter inside each mapping run
+
reuse and update a graph/local-map representation across runs
```

It does **not** establish:

```text
D1 retained history
+
D2 hidden-change inference
+
D3 transfer of a complete D1+D2 scene state
```

It should therefore be cited as an early D3 localization-map maintenance method,
not as a close predecessor of the three-part dynamic-scene formulation.

**Correct coverage:** dynamic-input cleaning only; D1 history no; D2 no; D3 yes
at the 2D pose-graph/local-map level.

## 2. ProbPer-LiLo, RA-L 2026

### Actual objective

ProbPer-LiLo explicitly defines lifelong mapping as building and maintaining an
accurate representation of the **static part** of the environment. It has two
objectives:

1. remove dynamic and quasi-static objects;
2. refine static geometry across multiple mapping sessions.

The paper states that dynamic and quasi-static objects are intentionally placed
on the same non-static side of the classification boundary. It is not attempting
to preserve their motion history.

### Inputs and state

The method takes:

- a prior point map `M_{t-1}`;
- a current session map observation `Mhat_t` built from scans and supplied poses;
- point-wise semantic labels.

Its primary latent state is binary:

```text
X_i in {0,1} = quasi-static / static
```

It uses a Bayesian survival model with false-detection and missed-detection
probabilities. A factor graph performs maximum-product inference. For large
maps, semantic points are clustered with DBSCAN; corresponding clusters across
the prior and current maps are associated by centroid distance. The paper
explicitly assumes the clustering/correspondence is correct.

Single-session observations detect moving points. Multi-map factors are added to
detect quasi-static clusters that may remain static throughout one session. Both
classes are then removed when generating the prior and current static maps.

### Map refinement

The two static maps are voxelized and compared using centroid distance, surface
normal similarity, and semantic labels. Voxels are classified as:

- previously explored;
- newly explored;
- co-existing;
- obsolete;
- emerging.

The refined lifelong map retains previously/newly explored, co-existing, and
emerging voxels; obsolete voxels are removed and logged in a delta map.

The experiments contain a genuine recursive D3 update: the lifelong map produced
from one NTU sequence is used as the prior for a later sequence collected months
afterward.

### Correct relationship to this project

ProbPer-LiLo is a strong large-scale D3 static-map refinement baseline. It is
more sophisticated than simple binary point differencing because it combines
semantic clustering, temporal persistence, map-overlap handling, and recursive
voxel update.

It still does not solve the target dynamic-scene problem:

- D1 entities and trajectories are removed, not retained;
- D2 observed versus hidden transition is not represented;
- object identity is not maintained beyond assumed cross-map cluster matching;
- its binary variable is static versus non-static, not
  persistent/absent/unobserved/new scene state;
- it does not jointly estimate a dynamic SLAM session or restore a complete
  D1+D2 backend in the next run.

**Correct coverage:** current-session dynamic/static classification; D1 history
no; D2 no; D3 yes for recursive static point-map refinement.

## 3. Correct comparison

| Capability | Efficient Long-Term Mapping | ProbPer-LiLo | Project target |
|---|---|---|---|
| Map representation | 2D local point clouds + pose graph | semantic 3D point/voxel map | dense metric-semantic mesh/TSDF + objects/history |
| Current-session dynamics | ray/depth cleaning | static/non-static classification | D1 retained + D2 inferred |
| Retained moving-object trajectory | no | no | yes |
| Hidden same-session D2 state | no | no | yes |
| Object identity | no | cluster association only | persistent identity/hypotheses |
| Unobserved protection | implicit map coverage | previously explored voxels retained | explicit evidence-aware state |
| Cross-session update | yes | yes, recursively demonstrated | yes, while next session resumes D1+D2 |
| Main output | clean current localization map | refined static lifelong map + delta | current scene + dynamic history + next-session memory |

## 4. Manuscript consequences

1. Do not call Efficient Long-Term Mapping the closest predecessor of the full
   three-part story. It is an early D3 localization-map updater with
   current-session clutter removal.
2. Do not describe ProbPer-LiLo as preserving object histories or jointly
   modeling D1/D2. It intentionally removes all non-static clusters.
3. Both papers show that cross-session prior reuse, recursive update, map-overlap
   categories, and static-map refinement already exist.
4. They do not show that the complete D1+D2 dynamic-scene state has been carried
   across sessions.
5. The novelty question remains open until the remaining directly relevant PDFs
   are read; these two papers alone neither prove nor disprove the exact claim.
