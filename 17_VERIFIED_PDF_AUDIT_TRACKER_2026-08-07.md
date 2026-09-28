# Verified PDF Audit Tracker

Status: **2026-08-07**

This tracker is the only authoritative count of papers whose complete primary
texts have actually been opened and read end-to-end under the project's audit
protocol.

## Current verified count

```text
SELF-FETCHED + COMPLETE: 22
  official/direct PDF or complete publisher paper: 21
  author-uploaded complete full-text rendering:      1 (RBIF)
USER-UPLOADED + COMPLETE: 6
DIRECT-CORE QUEUE PENDING: 0
TOTAL COMPLETE: 28
```

`RBIF` is counted separately because its complete author-uploaded paper rendering
was read, but ResearchGate rate limiting blocked retrieval of the PDF bytes. The
formal title, venue, authors, and DOI were independently verified. This source
mode must remain visible whenever the audit count is reported.

## Completion criteria

A paper may be marked `COMPLETE` only when all of the following are recorded:

1. verified title, authors, venue/status, and source identity;
2. exact problem definition and temporal/session protocol;
3. inputs, external assumptions, and supplied poses/labels;
4. state variables and map representation;
5. method equations and update rules;
6. what information is removed, compressed, or not represented;
7. experiments, datasets, metrics, and baselines;
8. limitations and future work;
9. D1/D2/D3 classification under the project's definitions;
10. exact page/section/equation/figure support;
11. overlap with the project and claims it does or does not threaten.

## Independently acquired and complete

| # | Paper | Actual relationship |
|---:|---|---|
| 1 | Khronos, RSS 2024 | complete dense single-session D1+D2; no process-separated D3 |
| 2 | Panoptic Multi-TSDFs, ICRA 2022 | dense D3 object/submap state; D1 future work |
| 3 | POCD, RSS 2022 | object-level D3 change/stationarity belief; external poses; no retained D1 |
| 4 | POV-SLAM, RSS 2023 | joint pose/object-consistency D3; no complete D1 history |
| 5 | LT-Mapper, ICRA 2022 | D3 geometric current-map maintenance; moving content removed |
| 6 | ObVi-SLAM, RA-L 2024 | recursive deployment object prior; static landmarks only |
| 7 | Changing-SLAM, JINT 2023 | sparse object-level D1+D2; no process-separated D3 |
| 8 | General Movable Objects, T-RO 2019 | probabilistic D2 object tracking; not SLAM or dense mapping |
| 9 | Perpetua, IROS 2025 | feature-existence theory; no geometry or SLAM |
| 10 | Lost & Found, RA-L 2025 | observed D1 interaction trajectory and graph update; no D2/D3 |
| 11 | LTC-Mapping, Sensors 2022 | visibility/non-detection object maintenance in one stream; no D1/D3 |
| 12 | GaME, CVPR 2026 | dense Gaussian D2 update in one continuous process; no D1/D3 |
| 13 | OASIS-Map, preprint 2026 | object-level D3 association and change labels; external session SLAM |
| 14 | Living Scenes, CVPR 2024 | offline cross-time object association/registration/reconstruction |
| 15 | Dynamic Pose Graph SLAM, IROS 2012 | active 2D current map plus scan-level change history; D3 |
| 16 | Pomerleau et al., ICRA 2014 | repeated-survey point maintenance plus instantaneous point velocity |
| 17 | RBIF, IROS 2024 | probabilistic ray/voxel D3 geometry update; no semantic/dynamic history |
| 18 | 4D Gaussian Splatting SLAM, ICCV 2025 | continuous-sequence Gaussian D1 |
| 19 | 4DTAM, CVPR 2025 | continuous non-rigid Gaussian D1 |
| 20 | DynaGSLAM, WACV 2026 | online Gaussian D1 using external DynoSAM poses |
| 21 | 4D Primitive-Mache, CVPR 2026 | persistent/replayable D1 within one monocular video |
| 22 | LT-Gaussian, IEEE IV 2025 | old-Gaussian-map/current-LiDAR D3 revision component |

Detailed audits:

- `18_KHRONOS_SELF_FETCHED_FULL_TEXT_AUDIT_2026-08-07.md`
- `19_CORE_D3_SELF_FETCHED_FULL_TEXT_AUDIT_2026-08-07.md`
- `20_CORE_D1_D2_AND_PERSISTENCE_SELF_FETCHED_AUDIT_2026-08-07.md`
- `21_REMAINING_DIRECT_CORE_FULL_TEXT_AUDIT_2026-08-07.md`

## User-uploaded and complete

| # | Paper | Actual relationship |
|---:|---|---|
| 1 | SuperMap, RSS 2026 | continuous semantic/object map; object-level D2-like changes; no D3 |
| 2 | DYMRO-SLAM, IEEE Access 2025 | dynamic-feature rejection/localization only |
| 3 | ELite, ICRA 2025 | point-level D3 lifelong/static/delta maps; current dynamics removed |
| 4 | DYNEMO-SLAM, arXiv v2 2025 | continuous robot/entity factor graph; no process-separated D3 |
| 5 | Efficient Long-Term Mapping, IROS 2018 | current-run clutter cleaning plus multi-session 2D map update |
| 6 | ProbPer-LiLo, RA-L 2026 | recursive D3 static map refinement; non-static content removed |

Detailed audits:

- `13_SUPERMAP_DYMRO_ELITE_FULL_TEXT_CORRECTION_2026-08-07.md`
- `16_EFFICIENT_MAPPING_PROBPER_FULL_TEXT_CORRECTION_2026-08-07.md`

## Direct-core completion status

The fixed twelve-paper direct-core remainder has been completed. Across the 28
verified papers, the following combination has not appeared in one system:

```text
retained D1 trajectories/time-indexed geometry
+ explicit same-session D2 observability/absence reasoning
+ dense object and structural current map
+ process-separated D3 export/import
+ independent B session that resumes D1+D2 and exports for C
```

This is a result for the verified set, not a universal proof. Before authorizing
a final `to the best of our knowledge` sentence, the next step is a bounded
citation-chain saturation pass: inspect references and citing papers of the
closest systems and fully audit only genuinely new direct neighbours.

## Acquisition policy

- Open-access/arXiv/CVF/RSS/PMLR/NeurIPS/author papers are acquired directly.
- A complete publisher or author-hosted full-text rendering may be used when PDF
  bytes are blocked, but the source mode must be disclosed.
- Paywalled papers without an accessible author version require a user-provided
  copy; institutional credentials are not available to the assistant.
- File names and abstracts never determine identity or D1/D2/D3 coverage.

## Honesty rule

Do not report a count larger than the totals above. The retracted file
`15_SATURATED_CORE_FULL_TEXT_NOVELTY_AUDIT_2026-08-07.md` must never be cited as
completed evidence.
