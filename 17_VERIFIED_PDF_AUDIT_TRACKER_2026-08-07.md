# Verified PDF Audit Tracker

Status: **2026-08-07**

This tracker is the only authoritative count of papers that have actually been
held as full PDFs and read end-to-end under the project's audit protocol.

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

## Current verified count

```text
COMPLETE: 6
PENDING:  not yet fixed; the candidate list must be rebuilt from real PDFs
```

## Complete audits

| # | Paper | Verified source | Actual relationship |
|---:|---|---|---|
| 1 | SuperMap: A Spatio-Temporal SLAM System for Visual-Language Navigation | user-uploaded RSS 2026 PDF | continuous-stream semantic/object map; D2-like object changes; no process-separated D3 |
| 2 | DYMRO-SLAM: A Robust Stereo Visual SLAM for Dynamic Environments Leveraging Mask R-CNN and Optical Flow | user-uploaded IEEE Access 2025 PDF | dynamic-feature rejection and localization; no retained D1/D2/D3 scene memory |
| 3 | Ephemerality Meets LiDAR-Based Lifelong Mapping (ELite) | user-uploaded ICRA 2025 PDF | point-level D3 static/lifelong map maintenance; current-session dynamics removed |
| 4 | DYNEMO-SLAM: Dynamic Entity and Motion-Aware 3D Scene Graph SLAM | user-uploaded arXiv v2 2025 PDF | continuous-run robot/entity factor graph; observed/moved entities; no process-separated D3 |
| 5 | Efficient Long-Term Mapping in Dynamic Environments | user-uploaded IROS 2018 PDF | current-session clutter cleaning plus multi-session 2D pose-graph/local-map update; no D1 history or D2 |
| 6 | ProbPer-LiLo: Probabilistic Persistency Modeling for Life-Long Mapping | user-uploaded RA-L 2026 PDF | recursive D3 static point/voxel-map refinement; dynamic and quasi-static content removed |

Detailed evidence is recorded in:

- `13_SUPERMAP_DYMRO_ELITE_FULL_TEXT_CORRECTION_2026-08-07.md`
- `16_EFFICIENT_MAPPING_PROBPER_FULL_TEXT_CORRECTION_2026-08-07.md`
- the current conversation audit of DYNEMO-SLAM.

## Not counted as complete

The following are **not** counted merely because they were found online, cited,
or summarized previously:

- Khronos
- Panoptic Multi-TSDFs
- POCD
- POV-SLAM
- Changing-SLAM
- General Movable Object Tracking
- LT-Mapper
- ObVi-SLAM
- OASIS-Map
- LTC-Mapping
- GaME
- Perpetua
- Lost & Found
- Gaussian/4D papers
- any other entry from the earlier broad landscape

They remain `PENDING` until their exact PDFs are acquired and audited with the
full checklist above.

## Acquisition policy

The user does **not** need to upload every paper.

- Open-access/arXiv/CVF/RSS/author PDFs can be located and downloaded by the
  assistant from official or author-hosted sources.
- Paywalled papers without an accessible author copy require the user to upload
  the PDF or provide an accessible copy; the assistant cannot use the user's ETH
  institutional login.
- File names are never trusted. Identity is verified from the PDF title page,
  venue, DOI, and publication metadata.

## Honesty rule

Do not report a total full-text count larger than the number listed under
`Complete audits`. Do not claim saturation, novelty closure, or a universal
negative until the direct core set is actually complete and independently
searched again.
