# TSDF prior: what the replacement guard is and is not, 2026-09-21

Follows `23_HANDOFF_2026-09-21.md`, which attributed the prior's coverage loss to
`Backend::replaceInheritedInArchivedBlocks` erasing inherited surface that the
re-integrated TSDF had not reproduced, and called that a located defect rather
than a hypothesis. Two repairs of that guard were implemented and measured. Both
made the map worse. **The attribution is wrong and should be retired.**

## Measured, real stage B, one scorer, 1 cm pseudo-GT

`g` = observed domain (primary). Area is the exported surface area.

| configuration | gP | gR | gF1 | area m2 |
|---|---|---|---|---|
| Khronos | 0.9420 | 0.9864 | 0.9637 | 209.3 |
| Clean | 0.9606 | 0.9722 | 0.9664 | 212.9 |
| Memory, no prior | 0.9518 | 0.9771 | 0.9643 | 341.6 |
| **Memory+Prior, guard as written** | **0.9587** | 0.9740 | **0.9663** | 224.3 |
| Memory+Prior, guard at half a voxel | 0.9120 | 0.9757 | 0.9428 | 275.3 |
| Memory+Prior, face-complete guard | 0.9482 | 0.9751 | 0.9615 | 247.7 |

## Why each repair failed

**Half a voxel instead of one voxel.** The guard erases an inherited vertex when
a session vertex sits within `object_surface_resolution_`. Tightening it to half
that keeps inherited copies 2.5-5 cm from the re-integrated surface: the prior
did reproduce that surface, just not within half a voxel. Precision fell 4.7 pp.
The one-voxel radius is the correct statement of "the TSDF now represents this".

**Face-complete erasure.** Erasing a vertex destroys every face touching it,
including faces reaching into surface the prior did not reproduce, so a vertex
was erased only when all of its faces were themselves fully replaceable. Area
recovered 23.4 m2 and 56 k vertices survived, but **recall rose only 0.11 pp**
while precision fell 1.05 pp. The preserved surface does not earn recall.

## What this rules out

The prior's recall deficit against no-prior memory (0.9771 -> 0.9740, 0.31 pp) is
**not** caused by over-erasure at vertex or face granularity. Surface removed by
the guard is largely surface the reference does not reward. The deficit therefore
sits in the re-integrated TSDF itself: fusing a prior into a 5 cm TSDF does not
reproduce thin and grazing-angle surface that the frozen mesh carried. Any
further attempt belongs in seeding weight, truncation distance or seed density,
not in the replacement guard.

## Standing conclusion

`Memory+Prior` as written on `memory-tsdf-prior` is the best real-data result to
date and should not be modified in this direction: gated F1 0.9663 against
Clean's 0.9664 and Khronos's 0.9637, and unfiltered-with-room-crop 0.9584 against
Khronos's 0.9591, where memory without the prior scores 0.9337. Its cost is
coverage, 341.6 -> 224.3 m2. Report both rows: they are the two ends of a
precision/coverage trade, and the trade itself is the honest finding.

Code state: branch `memory-tsdf-prior`, pushed 2026-09-21. Both repairs above were
reverted; the branch is unmodified. Tests 18/18 and 8/8.
