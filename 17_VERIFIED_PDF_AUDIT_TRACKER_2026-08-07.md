# Verified PDF Audit Tracker

Status: **2026-08-07**

This tracker is the only authoritative count of papers whose complete primary
texts have actually been opened and read end-to-end under the project's audit
protocol.

## Current verified count

```text
SELF-FETCHED + COMPLETE: 29
  direct PDF / complete official primary-text HTML: 28
  author-uploaded complete full-text rendering:       1 (RBIF)
USER-UPLOADED + COMPLETE: 6
DIRECT-CORE / PROMOTED QUEUE PENDING: 0
TOTAL COMPLETE: 35
```

`RBIF` is counted separately because its complete author-uploaded paper rendering
was read, but ResearchGate rate limiting blocked retrieval of the PDF bytes. The
formal title, venue, authors, and DOI were independently verified. This source
mode must remain visible whenever the audit count is reported.

The seven papers added after the original 28-paper corpus were all re-read using
the architecture-axis checklist and are documented in
`23_SEVEN_NEIGHBOURS_ARCHITECTURE_REAUDIT_2026-08-07.md`.

## Interpretation rule

The `Actual relationship` column below is a capability summary, **not a novelty
checklist**. A paper sharing ray deletion, object association, persistence
beliefs, map revision, scene graphs, Gaussian updates, relocalization, or any
other component with our system does not by itself threaten the research story.

The architecture-level question is tracked in
`22_ARCHITECTURE_AXIS_CITATION_AUDIT_2026-08-07.md`:

```text
complete D1+D2 Session A
-> persistent export after A terminates
-> independent Session B import
-> D3 reconciliation
-> B again executes complete D1+D2
-> equivalent export for Session C
```

Do not infer a component-level novelty claim from this tracker.

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
10. exact section/equation/figure support where available;
11. the A -> D3 -> B -> C architecture checklist for promoted bridge candidates.

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
| 23 | CubifyGS, IROS 2026 | continuous object-centric Gaussian lifecycle maintenance; cross-session asset merging is future work; no complete D1+D2 restoration |
| 24 | DynaMem, ICRA 2025 | continuous online dynamic voxel memory with add/remove updates; no retained D1 trajectory and no process-separated D3 |
| 25 | CogniMap3D, ICLR 2026 | genuine multi-visit static-scene memory retrieval/update; tracks dynamic regions inside video but excludes them from persistent memory |
| 26 | DovSG, RA-L 2025 | continuously updated object scene graph across consecutive tasks without manual resets; no independent D3 boundary |
| 27 | DynamicGSG, IROS 2025 | continuous posed-RGB-D/VIO Gaussian scene-graph update; no retained D1 history or independent restart |
| 28 | DGSG-Mind, preprint 2026 | strong prior-Gaussian-map relocalization and D2-like revision; integrated tracking is future work, so no complete D1+D2 restoration |
| 29 | DREAM, preprint 2026 | continuous online voxel memory plus pose-graph-aware historical reintegration; no D1 entity history or process-separated D3 |

Detailed audits:

- `18_KHRONOS_SELF_FETCHED_FULL_TEXT_AUDIT_2026-08-07.md`
- `19_CORE_D3_SELF_FETCHED_FULL_TEXT_AUDIT_2026-08-07.md`
- `20_CORE_D1_D2_AND_PERSISTENCE_SELF_FETCHED_AUDIT_2026-08-07.md`
- `21_REMAINING_DIRECT_CORE_FULL_TEXT_AUDIT_2026-08-07.md`
- `23_SEVEN_NEIGHBOURS_ARCHITECTURE_REAUDIT_2026-08-07.md`

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

## Architecture result after 35 complete primary texts

Across the 35 verified complete primary texts, the following **architecture** has
not appeared in one system:

```text
retained D1 trajectories/time-indexed geometry
+ explicit same-session D2 observability/absence reasoning
+ persistent export after Session A terminates
+ independent Session B import and D3 reconciliation
+ Session B again executes D1+D2
+ Session B exports the same state contract for Session C
```

The seven newly promoted papers materially strengthen the right-hand side of the
landscape:

- CogniMap3D provides genuine multi-visit retrieval/relocalization/update of a
  persistent **static** scene memory;
- DGSG-Mind provides strong later-observation relocalization against an existing
  Gaussian map and local dynamic revision without requiring continuous online
  SLAM, but its integrated tracking module is explicitly future work;
- CubifyGS, DynaMem, DovSG, DynamicGSG, and DREAM provide strong continuous
  dynamic/current-memory maintenance without the complete independent-session
  bridge.

Dense object-plus-structural scene state is an important representation property
of our target, but the literature search must not be reduced to checking isolated
representation mechanisms.

This remains a result for the verified corpus, not a universal proof. Before
authorizing a final absolute or `first ever` claim, the bounded architecture-
focused backward/forward citation-chain stop rule in files `11` and `22` still
applies.

## Acquisition policy

- Open-access/arXiv/CVF/RSS/PMLR/NeurIPS/author papers are acquired directly.
- A complete official or author-hosted primary-text HTML rendering may be used
  when it contains the full paper; source mode must remain disclosed.
- A complete publisher or author-hosted full-text rendering may be used when PDF
  bytes are blocked, but the source mode must be disclosed.
- Paywalled papers without an accessible author version require a user-provided
  copy; institutional credentials are not available to the assistant.
- File names and abstracts never determine identity or D1/D2/D3 coverage.

## Honesty rule

Do not report a count larger than **35** unless a newly added paper has met the
completion criteria above. The old unsupported 38-paper saturation claim is
withdrawn and must never be used as evidence.
