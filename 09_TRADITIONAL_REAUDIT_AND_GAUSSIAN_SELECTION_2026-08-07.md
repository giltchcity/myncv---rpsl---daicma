# Traditional Mapping Re-Audit and Gaussian Selection

Status checked: **2026-08-07**

> **Selection update:** the earlier three-paper Gaussian shortlist in this file
> has been superseded by `10_BROAD_DYNAMIC_MAPPING_LANDSCAPE_2026-08-07.md`.
> After the broader search, the manuscript now retains six to seven Gaussian
> representatives spanning dynamic-robust static mapping, D1 4D reconstruction,
> D2 evolving maps, and D3 map revision. The traditional-paper audit below
> remains valid.

The authoritative storyline remains:

```text
D1 + D2 = dynamic mapping inside every continuously running session
D3      = persistent scene-memory continuation across completed sessions
```

## Current Gaussian selection

The recommended manuscript set is:

1. WildGS-SLAM - dynamic-input robust static Gaussian map;
2. 4DTAM - non-rigid online D1 tracking and mapping;
3. 4D Gaussian Splatting SLAM - explicit D1 Gaussian SLAM;
4. DynaGSLAM - real-time D1 rendering, tracking, and motion prediction;
5. GaME - D2 map evolution after out-of-view change;
6. LT-Gaussian - D3 old-map/current-traversal update component;
7. GS-LTS - optional D3 semantic Gaussian editor, marked as a preprint.

The larger Gaussian candidate set remains in
`07_GAUSSIAN_FULL_TEXT_EVIDENCE_AUDIT_2026-08-06.md` and
`literature/gaussian_papers.json`.

## Traditional papers added after the re-audit

### MID-Fusion

- **Citation:** Xu et al., ICRA 2019, DOI 10.1109/ICRA.2019.8794371.
- **Representation:** one octree-based volumetric model per object plus static
  background; color, depth, semantics, and foreground probabilities are fused.
- **Correct role:** strong dense object-level D1 predecessor.
- **Boundary:** relies on continuous object observations; no D2 change-state
  reasoning and no D3 session memory.
- **Baseline feasibility:** possible D1 comparator, not a D3 baseline.

### EM-Fusion

- **Citation:** Strecke and Stueckler, ICCV 2019,
  DOI 10.1109/ICCV.2019.00596.
- **Representation:** background and rigid objects as local SDF volumes with
  probabilistic pixel association and occlusion reasoning.
- **Correct role:** dense probabilistic D1 predecessor.
- **Boundary:** no hidden-change state after an object leaves the observation
  stream and no process-separated memory continuation.

### DynaSLAM II

- **Citation:** Bescos et al., RA-L 2021,
  DOI 10.1109/LRA.2021.3068640.
- **Representation:** feature-based static and dynamic structure, camera and
  object trajectories, and temporal 3D boxes.
- **Correct role:** strong joint-estimation D1 reference.
- **Boundary:** no dense D2 scene reconciliation and no D3 memory.

### VDO-SLAM

- **Status:** manuscript/preprint; final publication status was not verified on
  2026-08-07.
- **Correct role:** D1 spatio-temporal feature-map reference.
- **Action:** keep in the watchlist unless a final publication record is found.

### Building Volumetric Beliefs for Dynamic Environments

- **Citation:** Mersch et al., RA-L 2023,
  DOI 10.1109/LRA.2023.3292583.
- **Representation:** probabilistic local volumetric belief derived from
  moving-object segmentation.
- **Correct role:** D1-related probabilistic motion evidence and static-map
  maintenance.
- **Boundary:** no object trajectories or persistent D2/D3 scene elements.

### Ray-Bundle-Impact-Factor map maintenance

- **Citation:** Breitfuss et al., IROS 2024,
  DOI 10.1109/IROS58592.2024.10802029.
- **Representation:** discretized 3D occupancy/localization map updated by
  probabilistic interference between ray bundles and occupied voxels.
- **Correct role:** recent traditional D3 geometric-map-maintenance reference.
- **Important difference:** it addresses partial versus contradictory ray
  traversal and erroneous holes, but does not preserve object identity,
  semantics, dynamic trajectories, or a complete D1+D2 history.
- **Baseline feasibility:** one of the most relevant geometric D3 comparators.

## Manuscript selection rule

A work belongs in the main Related Work only if it satisfies at least one of:

1. it is a central D1, D2, or D3 technical predecessor;
2. it is a serious novelty threat;
3. it can plausibly be evaluated under compatible inputs and outputs;
4. it represents a major current trend with a concise representative citation.

The broad candidate pool is intentionally much larger than the manuscript.
Citation count is not evidence quality, and representation-incompatible methods
should not dominate a paper evaluated with metric-semantic meshes, object
memories, and ray evidence.
