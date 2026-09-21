# Precision / recall, not F1: where the real-data numbers actually stand

Date: 2026-09-21. Real room-18 chain, 1 cm same-sensor pseudo-GT, threshold 5 cm.
Every row below is the same scorer, the same reference, the same sampling.
Script: `scratchpad/table.py`, raw output `scratchpad/table.log`.

Sampling is density based: one dense sample per 5 mm^2 of surface, then a
fixed-origin 2 cm voxel union. A larger map is therefore **not** sampled more
sparsely than a smaller one, so a recall change between rows is a real change
in coverage and never a sampling artefact.

Three domains are reported side by side:

* `g` gated: the observed domain, >= 3 valid depth rays of this session place
  the sample in front of, or <= 10 cm behind, the measured surface.
* `p` plain: every sample, no conditioning at all.
* `c` crop: plain, restricted to the room body (0.5--99.5 percentile box of the
  reference vertices).

## Stage B

| map | area m2 | gP | gR | gF1 | pP | pR | pF1 | cP | cR | cF1 |
|---|---|---|---|---|---|---|---|---|---|---|
| official Khronos | 209.3 | 0.9420 | 0.9864 | 0.9637 | 0.9389 | 0.9786 | 0.9583 | 0.9379 | 0.9813 | 0.9591 |
| ours, from scratch | 212.9 | 0.9606 | 0.9722 | **0.9664** | 0.9580 | 0.9631 | **0.9606** | 0.9572 | 0.9660 | **0.9616** |
| ours, memory (main, rule) | 341.6 | 0.9518 | 0.9771 | 0.9643 | 0.8865 | 0.9706 | 0.9267 | 0.8974 | 0.9730 | 0.9337 |
| ours, memory (TSDF prior) | 224.3 | 0.9587 | 0.9740 | 0.9663 | 0.9456 | 0.9652 | 0.9553 | 0.9491 | 0.9679 | 0.9584 |
| ours, memory (c54e6fa) | 248.4 | 0.9428 | 0.9757 | 0.9589 | 0.8678 | 0.9687 | 0.9155 | 0.8798 | 0.9712 | 0.9232 |

## Stage C

| map | area m2 | gP | gR | gF1 | pP | pR | pF1 | cP | cR | cF1 |
|---|---|---|---|---|---|---|---|---|---|---|
| official Khronos | 299.1 | 0.9197 | 0.9879 | 0.9526 | 0.9160 | 0.9752 | 0.9447 | 0.9151 | 0.9808 | 0.9468 |
| ours, from scratch | 337.7 | 0.9264 | 0.9809 | 0.9529 | 0.9246 | 0.9640 | 0.9439 | 0.9238 | 0.9708 | 0.9467 |
| ours, memory (main, rule) | 534.0 | 0.9247 | 0.9877 | **0.9552** | 0.8959 | 0.9760 | 0.9343 | 0.9009 | 0.9811 | 0.9393 |
| ours, memory (TSDF prior) | 368.6 | 0.9241 | 0.9840 | 0.9531 | 0.9192 | 0.9673 | 0.9426 | 0.9204 | 0.9741 | 0.9465 |
| ours, memory (c54e6fa) | 383.8 | 0.9113 | 0.9881 | 0.9482 | 0.8757 | 0.9751 | 0.9228 | 0.8809 | 0.9803 | 0.9279 |

## What this settles

1. **"Our foundation is below Khronos" is false as stated.** Our from-scratch
   map already has the higher F1 at both stages (B 0.9664 vs 0.9637, C 0.9529
   vs 0.9526) in the gated domain, and the higher plain F1 at B (0.9606 vs
   0.9583). What is true is that we sit at a different point on the
   precision/recall curve: **-1.4 pp recall, +1.9 pp precision** at B. Lowering
   our evidence threshold to match Khronos would move us along that same curve,
   not above it. The goal is to gain recall *without* giving the precision back.

2. **c54e6fa is a verified regression and has been replaced.** Its `try_to_lock`
   always fails in the terminal round, so the live-graph memory registration was
   always skipped and the exported mesh kept the unregistered copy of every
   inherited vertex: plain P 0.9456 -> 0.8678, carried surface 224.3 -> 248.4 m2.
   Replaced by bf88666, which threads `finalize_pending` through instead.

3. **The TSDF prior removed almost all of the duplicate-surface cost.** Carried
   area over from-scratch: rule-based memory +128.7 m2, TSDF prior +11.4 m2.
   Plain precision loss over from-scratch: -7.15 pp vs -1.24 pp.

4. **Memory currently buys almost nothing on this reference.** TSDF prior over
   from-scratch: B +0.18 pp recall for -0.19 pp precision, C +0.31 pp recall for
   -0.23 pp precision. On the synthetic pair, where the GT is the true scene at
   the true time, the same mechanism is worth +14 pp F1 over Khronos. The
   difference is a property of the reference, not of the map: the B pseudo-GT is
   built from B's own observations and cannot reward surface that only A saw.
   Both numbers get reported; neither replaces the other.

## Where the recall difference lives

`scratchpad/by_support.py`, gated stage-B reference split by how many valid
depth rays of this session cover each sample:

| rays | 3-4 | 5-9 | 10-19 | 20-39 | 40-79 | 80+ |
|---|---|---|---|---|---|---|
| share of reference | 5.2% | 13.7% | 23.6% | 32.1% | 25.1% | 0.3% |
| R official Khronos | 0.9818 | 0.9835 | 0.9866 | 0.9883 | 0.9863 | 0.9904 |
| R ours, from scratch | 0.9578 | 0.9713 | 0.9640 | 0.9704 | 0.9855 | 0.9892 |
| R ours, TSDF prior | 0.9591 | 0.9725 | 0.9693 | 0.9711 | 0.9857 | 0.9892 |
| share of the 1.42 pp gap | 8.8% | 11.8% | 37.5% | 40.5% | 1.4% | 0.0% |

This **refutes** the hypothesis carried over from the foundation-gap workflow
that the deficit is the thinly observed surface. Only 8.8% of it is in the
least observed bucket. 78% of it sits at 10-39 rays, which is ordinarily well
observed surface, and the deficit closes by itself above 40 rays. Khronos is
flat at ~0.986 everywhere; we have a dip in the middle of the distribution.

Memory recovers 0.18 pp of the 1.42 pp, i.e. 13% of the gap.

## The evidence threshold is not the cause either

Two from-scratch stage-B runs, same binary, one config change between them
(`scratchpad/run_clean.sh`):

| stage B | area m2 | gP | gR | gF1 | pP | pR | pF1 |
|---|---|---|---|---|---|---|---|
| `c0_clean_ctrl` (control) | 212.9 | 0.9606 | 0.9722 | 0.9664 | 0.9580 | 0.9631 | 0.9606 |
| `c1_minweight` (5 -> 0.0001) | 216.1 | 0.9591 | 0.9733 | 0.9661 | 0.9549 | 0.9661 | 0.9605 |

The control reproduces the older `clean_B` export to four decimals in all nine
numbers and to the face (488296), so the pipeline is deterministic and the
provenance question is closed.

Restoring the upstream default recovers **0.11 pp of the 1.42 pp** recall gap
for -0.15 pp precision, and F1 goes slightly down. The fork's own comment on
that field turns out to be correct: the static scene is observed from many views
and keeps its weights well above 5. **Hypothesis refuted; leave the field alone.**

## The cause: we delete our own background, official Khronos never does

`change_detection.background` is `Uninitialized` in the official run
(`config.txt:256`). Official Khronos therefore never marks a background vertex
absent and never removes one. Our fork runs `RayBackgroundChangeDetector`, and
`ChangeMerger::merge` deletes every vertex it marks `kAbsent`. In the
from-scratch stage-B control that is **7923 of 157725 background vertices, 5.0%**,
with `BACKGROUND_STATE_CLOSURE` firing 441 times.

Layer split (`scratchpad/by_layer.py`), gated stage-B reference:

| map | area m2 | R whole | R background only | R objects only |
|---|---|---|---|---|
| official Khronos | 209.3 | 0.9864 | **0.9832** | 0.3863 |
| ours, from scratch | 212.9 | 0.9722 | **0.9650** | 0.3326 |
| ours, TSDF prior | 224.3 | 0.9740 | 0.9670 | 0.3311 |

Our background mesh and theirs have the same face count (196320 vs 196315), yet
theirs covers 1.8 pp more of the reference, and **94.2% of the surface we miss,
Khronos covers with its background layer alone**. It is not the object layer.

What that missed surface looks like, over the 4465 gated reference samples
Khronos reaches and we do not (1.47% of the reference):

| | missed set | whole gated reference |
|---|---|---|
| >= 3 rays measured **free space** through it | **81.1%** | 9.4% |
| >= 3 rays measured **a surface** at it | 66.1% | 97.8% |
| session A reconstructed it | 27.5% | - |
| our carried map reaches it | 13.2% | - |

So the surface we lose is precisely the surface whose evidence is **contested**:
at least 47% of it has both free-space rays and surface-supporting rays from the
same session. Our absence rule sides with the free-space rays and deletes; the
pseudo-GT, built from the same depth images, keeps it.

This also explains the shape of the dip. Recall by number of separate visits
(gaps longer than the 10 s active-window duration start a new visit,
`scratchpad/by_visits.py`):

| visits | 1 | 2 | 3 | 4 | 5+ |
|---|---|---|---|---|---|
| share of reference | 17.1% | 38.5% | 27.7% | 12.5% | 4.2% |
| R official Khronos | 0.9896 | 0.9923 | 0.9837 | 0.9701 | 0.9858 |
| R ours, from scratch | 0.9835 | 0.9809 | 0.9662 | 0.9459 | 0.9642 |
| gap | 0.61 pp | 1.14 pp | 1.75 pp | 2.42 pp | 2.16 pp |

Our deficit grows monotonically with revisit count while Khronos's does not.
More separate visits means more opportunities for one visit's rays to contradict
another's, which is exactly when an absence rule fires on contested evidence.

Part of this is correct behaviour that the metric cannot reward: where an object
really did move during B, deleting the background surface it used to occlude is
right, and our 4D map still holds that surface in the earlier time steps, but
the pseudo-GT is the union of everything B's sensor ever saw and the score looks
at one final mesh. Part of it is over-deletion on contested evidence. The
diagnostic that separates them is `c2_nobgcd_20260921`, a from-scratch stage-B
run with only the background change detector turned off (parity with official
Khronos). It is a measurement of the deletion's cost, not a proposed
configuration: within-session background change is a contribution, not something
to switch off.

## Why the deletion fires on contested evidence, and the fix

`RayChangeDetector::detectChanges` discretizes the ray evidence into 5 s buckets,
slides a 5-bucket (25 s) window, and **returns at the first window whose rays are
more than 60% empty** (`ray_change_detector.cpp:149-153`, before this change).
Scanning forward, that question is "has this surface disappeared?", and returning
early answers it from the earliest window that happens to look empty. It never
looks at what the session measured afterwards. A grazing stretch of trajectory, or
25 s of depth noise on an oblique wall, therefore deletes surface that the same
session goes on measuring for another minute.

The same file's sibling path already refuses to do this. `markClosedObjectBackground`
computes `last_geometric_support` and drops, through `remove_past`, every absent
and inconclusive stamp at or before it, so only absence *after* the last support
can remove a vertex (`closed_object_background.cpp:96-120`). The generic detector
did not have that requirement.

The change: a forward absence verdict is held pending instead of returned, and is
discarded as soon as a later window is confidently present. Backward scanning,
which asks when a surface first *appeared* and where later presence is exactly
what is expected, keeps returning on the first absence it finds. This introduces
no new parameter and no threshold; it makes the generic detector obey the rule the
closed-object path already obeys, which is the direct reading of the project's own
principle that a missing observation is not evidence of absence.

Covered by `tests/test_absence_requires_no_later_presence.cpp`:

* T1 present 30 s then empty 30 s, never seen again -> absent (unchanged).
* T2 same, then measured again for 60 s -> **not** absent, persistent instead.
* T3 present 60 s then empty 30 s -> absent, with the persistent verdict predating it.
* T4 empty, present, empty -> the surviving verdict is the trailing absence.
* T5 empty then present: forward discards the absence, backward still reports it.

## Surface audit, from scratch vs carried memory

`memory_audit.py`, in-room samples of each map, categorised by what this
session's own rays say about each one:

| category | from scratch | TSDF prior | min_weight ablation |
|---|---|---|---|
| agrees with this session | 95.72% | 94.91% | 95.43% |
| no ray of this session exposed it | 0.46% | 1.12% | 0.62% |
| rays passed through it, we kept it | 0.44% | 0.67% | 0.49% |
| session measured a surface, ours >5cm off | **2.99%** | **2.90%** | 3.04% |
| observed but unexplained | 0.39% | 0.39% | 0.42% |

Two things worth stating plainly. The 2.99% of genuinely misplaced surface is
**already there without any memory**, and memory *reduces* it (2.90%). And of the
1.24 pp plain precision that memory costs, 0.66 pp is surface that no ray of this
session ever exposed, which the reference cannot adjudicate either way, and
0.23 pp is surface this session's rays actually contradict. Only the latter is
unambiguously our error.
