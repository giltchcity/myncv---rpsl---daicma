# Verified PDF Audit Tracker

Status: **2026-08-07**

This tracker is the only authoritative count of papers whose full PDFs have
actually been opened and read end-to-end under the project's audit protocol.

## Current verified count

```text
SELF-FETCHED + COMPLETE: 6
USER-UPLOADED + COMPLETE: 6
SELF-FETCHED + PENDING: 0
TOTAL COMPLETE: 12
```

The self-fetched set consists of Khronos plus five core D3 papers independently
opened from official or author-hosted full PDFs through the web PDF reader.

## Completion criteria

A paper may be marked `COMPLETE` only when all of the following are recorded:

1. verified title, authors, venue/status, and PDF identity;
2. exact problem definition and temporal/session protocol;
3. inputs, external assumptions, and supplied poses/labels;
4. state variables and map representation;
5. method equations and update rules;
6. what information is removed, compressed, or not represented;
7. experiments, datasets, metrics, and baselines;
8. limitations and future work;
9. D1/D2/D3 classification under the project's definitions;
10. exact PDF page/section/equation/figure support;
11. overlap with the project and claims it does or does not threaten.

## Independently fetched and complete

| # | Paper | Source | Actual relationship |
|---:|---|---|---|
| 1 | Khronos: A Unified Approach for Spatio-Temporal Metric-Semantic SLAM in Dynamic Environments | official arXiv PDF, RSS 2024 | complete dense single-session D1+D2 base; no process-separated D3 continuation |
| 2 | Panoptic Multi-TSDFs | official arXiv PDF, ICRA 2022 | dense D3 object/submap representation with persistent/absent/unobserved states; D1 left for future work |
| 3 | POCD: Probabilistic Object-Level Change Detection and Mapping in Semi-Static Environments | official arXiv PDF, RSS 2022 | object-level D3 map with Gaussian--Beta stationarity/change belief; external poses; no retained D1 |
| 4 | POV-SLAM: Probabilistic Object-Oriented Variational SLAM in Semi-Static Environments | official arXiv PDF, RSS 2023 | joint pose/object-consistency D3 SLAM; no complete D1 history or same-session D2 output |
| 5 | LT-Mapper: A Modular Framework for LiDAR-Based Lifelong Mapping | official arXiv PDF, ICRA 2022 | D3 geometric current-map maintenance with positive/negative changes; moving content removed |
| 6 | ObVi-SLAM: Long-Term Object-Visual SLAM | official arXiv PDF / author manuscript, RA-L 2024 | genuine recursive deployment object prior; static object landmarks only |

Detailed audits:

- `18_KHRONOS_SELF_FETCHED_FULL_TEXT_AUDIT_2026-08-07.md`
- `19_CORE_D3_SELF_FETCHED_FULL_TEXT_AUDIT_2026-08-07.md`

## User-uploaded and complete

| # | Paper | Actual relationship |
|---:|---|---|
| 1 | SuperMap: A Spatio-Temporal SLAM System for Visual-Language Navigation | continuous-stream semantic/object map; D2-like object changes; no process-separated D3 |
| 2 | DYMRO-SLAM: A Robust Stereo Visual SLAM for Dynamic Environments Leveraging Mask R-CNN and Optical Flow | dynamic-feature rejection and localization; no retained D1/D2/D3 scene memory |
| 3 | Ephemerality Meets LiDAR-Based Lifelong Mapping (ELite) | point-level D3 static/lifelong map maintenance; current-session dynamics removed |
| 4 | DYNEMO-SLAM: Dynamic Entity and Motion-Aware 3D Scene Graph SLAM | continuous-run robot/entity factor graph; no process-separated D3 |
| 5 | Efficient Long-Term Mapping in Dynamic Environments | current-session clutter cleaning plus multi-session 2D pose-graph/local-map update; no D1 history or D2 |
| 6 | ProbPer-LiLo: Probabilistic Persistency Modeling for Life-Long Mapping | recursive D3 static point/voxel-map refinement; dynamic and quasi-static content removed |

## Still pending

The remaining direct-core queue includes, at minimum:

- Changing-SLAM;
- Detection and Tracking of General Movable Objects in Large 3D Maps;
- LTC-Mapping;
- GaME;
- Perpetua;
- Lost & Found;
- OASIS-Map;
- Dynamic Pose Graph SLAM;
- Pomerleau et al. 2014;
- selected Gaussian/4D representatives.

The broader candidate pool is not counted until each exact PDF is acquired and
passes the complete checklist.

## Acquisition policy

The user does **not** need to upload every paper.

- Open-access, arXiv, CVF, RSS, PMLR, NeurIPS, and author-hosted PDFs must be
  acquired by the assistant using the web PDF reader.
- The local container cannot always resolve external hosts, so a PDF may be read
  through the web PDF interface without being saved as a local file. This counts
  as self-fetched only when the official full PDF is opened and audited
  end-to-end.
- Paywalled papers without an accessible author copy require the user to upload
  the PDF or provide an accessible copy; the assistant cannot use the user's ETH
  institutional login.
- File names are never trusted. Identity is verified from the PDF title page,
  venue, DOI, and publication metadata.

## Honesty rule

Do not report a self-acquired full-text count larger than
`SELF-FETCHED + COMPLETE`. Do not claim saturation, novelty closure, or a
universal negative until the direct core set is actually complete and searched
again.
