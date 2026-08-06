# Verified PDF Audit Tracker

Status: **2026-08-07**

This tracker is the only authoritative count of papers that have actually been
held as full PDFs and read end-to-end under the project's audit protocol.

## Current verified count

```text
SELF-FETCHED + COMPLETE: 0
USER-UPLOADED + COMPLETE: 6
SELF-FETCHED + PENDING: 1 (Khronos)
```

The six completed PDFs were all uploaded by the user. No paper has yet been both
independently acquired by the assistant and fully audited. This corrects earlier
ambiguous wording that counted user-uploaded PDFs without separating acquisition
source.

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

## User-uploaded and complete

| # | Paper | Actual relationship |
|---:|---|---|
| 1 | SuperMap: A Spatio-Temporal SLAM System for Visual-Language Navigation | continuous-stream semantic/object map; D2-like object changes; no process-separated D3 |
| 2 | DYMRO-SLAM: A Robust Stereo Visual SLAM for Dynamic Environments Leveraging Mask R-CNN and Optical Flow | dynamic-feature rejection and localization; no retained D1/D2/D3 scene memory |
| 3 | Ephemerality Meets LiDAR-Based Lifelong Mapping (ELite) | point-level D3 static/lifelong map maintenance; current-session dynamics removed |
| 4 | DYNEMO-SLAM: Dynamic Entity and Motion-Aware 3D Scene Graph SLAM | continuous-run robot/entity factor graph; no process-separated D3 |
| 5 | Efficient Long-Term Mapping in Dynamic Environments | current-session clutter cleaning plus multi-session 2D pose-graph/local-map update; no D1 history or D2 |
| 6 | ProbPer-LiLo: Probabilistic Persistency Modeling for Life-Long Mapping | recursive D3 static point/voxel-map refinement; dynamic and quasi-static content removed |

## Independently fetched but pending

- **Khronos, RSS 2024:** official arXiv PDF successfully opened through the web
  PDF reader on 2026-08-07. It is not complete until all pages, equations,
  experiments, figures, and limitations are audited and recorded.

## Acquisition policy

The user does **not** need to upload every paper.

- Open-access, arXiv, CVF, RSS, PMLR, NeurIPS, and author-hosted PDFs must be
  acquired by the assistant using the web PDF reader.
- The local container currently cannot resolve external hosts reliably, so a PDF
  may be read through the web PDF interface without being saved as a local file.
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