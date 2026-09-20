# Real-Data Geometry: Root Cause and What the Numbers Can Support

Date: 2026-09-20. All numbers re-scored today with one validated pipeline
(clean B/C, A4 B/C, official Khronos B re-scored to within 0.02 pp of records).

## Verified table (real A/B/C, 1cm same-sensor pseudo-GT, F1@5cm)

| Protocol | Stage | Ours | Khronos | Panoptic | clean (ours, from scratch) |
|---|---|---|---|---|---|
| Evidence-gated (scored only where the session's rays exposed the point) | B | **0.9643** | 0.9637 | 0.8866 | 0.9664 |
| Evidence-gated | C | **0.9552** | 0.9526 | 0.8845 | 0.9529 |
| Plain, room crop, full map | B | 0.9337 | 0.9591 | – | 0.9616 |
| Plain, room crop, full map | C | 0.9393 | 0.9468 | – | 0.9467 |
| Plain, room crop, current layer only (session-built surface) | B | 0.9591 | 0.9591 | – | 0.9616 |

Synthetic A/B (true rendered GT, plain F1@5cm, whole scene): ours 0.9760, Khronos 0.8364,
Panoptic 0.9210 at stage B (Khronos recall collapses to 0.7406 without cross-session memory).

## Where the plain-metric gap comes from (stage B, in-room surface samples)

| Category | Ours | clean | Khronos |
|---|---|---|---|
| Agrees with session B measurement | 89.74% | 95.72% | 93.79% |
| No ray of session B exposed it (unjudgable) | **5.95%** | 0.46% | 0.61% |
| Session B rays passed through it, yet kept (harmful) | 0.70% | 0.44% | 1.13% |
| Session B measured a surface here, ours >5cm off | 3.26% | 2.99% | 3.92% |

On every category the pseudo-GT can adjudicate, our map is cleaner than Khronos.
The whole gap is the unjudgable 5.95%, of which 91.7% is backed by session A's
measurement: it is retained memory, and the plain metric charges it as error 1:1
(5.94 pp of unjudgable surface vs 5.98 pp of precision difference to clean).

## The pseudo-GT's own cross-session consistency (static surface, co-observed)

| Pair | ≤5cm | ≤10cm | ≤20cm | median | p90 |
|---|---|---|---|---|---|
| A→B | 89.8% | 97.1% | 99.0% | 1.3cm | 5.1cm |
| B→C | 88.3% | 97.1% | 98.8% | 2.0cm | 5.3cm |
| A→C | 85.2% | 96.8% | 98.7% | 2.0cm | 6.3cm |

Aligning A's static GT to B's with rigid / affine / quadratic / 1.5 m piecewise-affine
models leaves 9.0 / 8.6 / 8.2 / 6.1% beyond 5 cm: the disagreement is high-frequency
reconstruction noise, not smooth drift. A per-session same-sensor pseudo-GT therefore
cannot adjudicate cross-session geometry at 5 cm.

## What this supports

1. Geometric accuracy claims belong to the synthetic dataset (true GT): +14.0 pp over
   Khronos, +5.5 pp over Panoptic at stage B.
2. On real data, under the evidence-gated protocol (the one consistent with
   "non-observation is not absence"), the method is level with or above both
   published baselines at both stages, and above from-scratch at stage C.
3. The plain single-session protocol penalizes retained unobserved memory by
   construction, at every threshold (B@20cm still -1.5 pp): report it as the cost
   of the design principle, with the decomposition above, not as accuracy.
4. Do not claim: "higher geometric accuracy than Khronos on real data". The margin
   (+0.06 pp at B) is inside the pseudo-GT's own noise.

## Tried and rejected today (code reverted, main unaffected)

- Deleting inherited surface occluded by its replacement: +0.13 pp plain F1, weakens
  the retention principle, not worth it.
- Union / persistent references: a naive union rewards stale object poses; rejected.
- Room crops: correct only when oriented to the room (44.5 deg); gain +1.8 pp, does
  not change the ranking.
