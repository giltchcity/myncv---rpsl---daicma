# Authoritative Full-Text Literature Audit Protocol

Status: **2026-08-07**

This file supersedes every earlier `FULL`, `PRIMARY`, or novelty-threat label in
this repository unless the paper has been re-audited under the rules below.

## Why this reset is necessary

Several earlier notes mapped title-level language such as `spatio-temporal`,
`persistent`, `long-term`, or `lifelong` too directly onto the project's
D1/D2/D3 taxonomy. The full-text re-reading of SuperMap, DYMRO-SLAM, ELite, and
DYNEMO-SLAM showed that these terms can denote substantially different tasks.
No manuscript claim may therefore be based on title, abstract, project page,
another paper's related-work paragraph, or repository filename alone.

## Canonical project problem

```text
Within each continuously running mapping session:
  D1 = motion observed while it occurs
  D2 = a transition occurring while the robot looks elsewhere

Across completed independent sessions:
  D3 = Session B imports persistent scene state from completed Session A,
       reconciles A-to-B change, runs its own D1+D2, and exports state for C
```

## Required audit fields for every promoted paper

A paper may influence Introduction, Related Work, novelty, method design, or
baseline selection only after all of the following are recorded from the
original PDF:

1. **Publication state**: venue, year, DOI, preprint/review status.
2. **Exact task**: what problem the authors explicitly formulate.
3. **Temporal protocol**: continuous stream, revisit inside one run, independent
   sessions, offline scans, or pairwise map comparison.
4. **Inputs and prerequisites**: RGB/RGB-D/LiDAR, externally supplied poses,
   segmentation, object models, markers, known classes, prior maps.
5. **Estimated state variables**: robot poses, object poses, trajectories,
   existence, identity, stationarity, visibility, map points, TSDFs, Gaussians,
   graph nodes, temporal parameters.
6. **Representation**: point map, occupancy grid, TSDF, mesh, object submaps,
   Gaussian map, scene graph, feature map, neural field.
7. **Update mechanism**: factors, filtering, ray evidence, data association,
   change categories, map replacement, pruning, deformation, optimization.
8. **What is discarded or not represented**: dynamic points, intermediate
   motion, unobserved regions, identity ambiguity, structural geometry, history.
9. **Experiments**: actual sequence/session structure, interventions, sensors,
   baselines, metrics, and what the results truly demonstrate.
10. **Limitations/future work**: explicitly separated from implemented
    contributions.
11. **D1/D2/D3 coverage** under this project's definitions.
12. **Method overlap**: exact mechanism shared with the proposed system.
13. **Novelty threat**: what claim the paper invalidates and what it does not.
14. **Baseline feasibility**: whether inputs, outputs, code, data, and metrics
    permit a fair comparison.
15. **Source traceability**: section, equation, table/figure, PDF page, and short
    original excerpts.

## Evidence levels

- **PDF-AUDITED**: every field above completed from the original PDF.
- **PDF-IN-PROGRESS**: PDF acquired and partially read; no manuscript claim may
  rely on it yet.
- **DISCOVERY-ONLY**: title/metadata/abstract located; candidate pool only.

The words `FULL` and `PRIMARY` in older files are deprecated until revalidated.

## Papers currently PDF-audited under this reset

### SuperMap (RSS 2026)

- Continuous stream `t=1,...,T`, not process-separated sessions.
- Object-centric instance map and queryable scene graph on top of dense
  SuperOdometry reconstruction.
- Point update states: observable, unobservable, disappeared.
- Main change experiment: 10-minute continuous run, three objects removed and
  three added.
- Highly dynamic object tracking explicitly remains limited.
- Correct role: continuous-session semantic object maintenance and D2-like
  appearance/disappearance/relocation; not D3.

### DYMRO-SLAM (IEEE Access 2025)

- ORB-SLAM3 plus Mask R-CNN feature rejection and optical-flow acceleration.
- Only static features are used for camera localization/map construction.
- Evaluated with ATE/APE/runtime; no dynamic map or scene history.
- Correct role: dynamic-robust localization/static-map cleaning only.

### ELite (ICRA 2025)

- Independent LiDAR sessions and recursive point-map update.
- Local ephemerality detects/removes current-session dynamic points.
- Global ephemerality models cross-session point transiency.
- Outputs lifelong point map, thresholded static map, and delta map.
- Correct role: point-level D3 map-maintenance system; not D1+D2.

### DYNEMO-SLAM (arXiv v2, 2025; no verified peer-reviewed venue)

- One continuous factor-graph SLAM problem with keyframes, planes, floors,
  moving agents, and relocated objects.
- Jointly optimizes robot poses and time-indexed entity poses using
  keyframe-entity, intra-entity, and floor-entity factors.
- Uses AprilTags; perception, segmentation, and data association are outside
  scope.
- Relocations occur after initial exploration but inside the same run/dataset;
  no process-separated Session-A/Session-B state transfer.
- Correct role: D1 plus observed/re-detected displaced-object factor-graph SLAM;
  not D3.

## Priority PDF audit sequence

The next conclusions must be based on complete PDF audits in this order:

1. Khronos
2. Panoptic Multi-TSDFs
3. POCD
4. POV-SLAM
5. Changing-SLAM
6. Detection and Tracking of General Movable Objects
7. LT-Mapper
8. ProbPer-LiLo
9. Perpetua
10. Lost & Found
11. OASIS-Map
12. LTC-Mapping
13. GaME
14. LT-Gaussian
15. RBIF
16. Pomerleau et al. 2014
17. Lifelong 3D Mapping Framework
18. DualMap
19. 4D Gaussian Splatting SLAM
20. 4DTAM
21. DynaGSLAM
22. 4D Primitive-Mache
23. Recurrent-OctoMap
24. FreMEn
25. Spatio-Temporal Hilbert Maps

References and citations of these papers may remain in the draft, but their
technical wording must be considered provisional until the corresponding audit
entry is complete.

## Search strategy for high recall

The search is performed across the following families rather than only papers
using the word `dynamic`:

- dynamic-robust localization and static-map cleaning;
- explicit rigid/non-rigid D1 reconstruction;
- partially observed and D2 object tracking;
- spatio-temporal metric-semantic SLAM;
- lifelong and multi-session geometric map maintenance;
- object-level and scene-graph memory;
- semantic/open-vocabulary map update;
- occupancy, periodic, predictive, and persistence models;
- neural implicit and Gaussian dynamic mapping;
- cross-session change detection and map versioning.

Citation chaining is bidirectional: references of each core paper and later
papers citing it are searched. Newly discovered papers remain `DISCOVERY-ONLY`
until their PDFs are audited.

## Novelty rule during the audit

Until the priority set is complete, the only safe statement is:

> The exact process-separated combination remains under systematic full-text
> audit. Existing works clearly cover many individual components and adjacent
> combinations; no universal negative claim is currently authorized.

Do not use `first`, `no existing work`, `unprecedented`, or equivalent language
in the manuscript until the audit closes.
