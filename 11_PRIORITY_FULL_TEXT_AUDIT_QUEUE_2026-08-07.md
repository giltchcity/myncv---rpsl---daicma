# Priority Full-Text Audit Queue

Status: **2026-08-07**

Priority is based on overlap with the canonical D1+D2 / D3 story, not title or
popularity.

## Direct-core queue: complete

The fixed direct-core PDF queue is now complete. The verified total is 28 primary
texts, with details in `17_VERIFIED_PDF_AUDIT_TRACKER_2026-08-07.md`.

Completed direct-core groups:

- dense/sparse D1+D2: Khronos and Changing-SLAM;
- D2 object reasoning: General Movable Objects, LTC-Mapping, SuperMap, GaME;
- D3 object/volume: Panoptic Multi-TSDFs, POCD, POV-SLAM, ObVi-SLAM,
  OASIS-Map, Living Scenes;
- D3 geometry/static maps: Dynamic Pose Graph SLAM, Pomerleau 2014,
  Efficient Long-Term Mapping, LT-Mapper, RBIF, ELite, ProbPer-LiLo,
  LT-Gaussian;
- D1 entity/4D representations: Lost & Found, DYNEMO-SLAM, 4DGS-SLAM,
  4DTAM, DynaGSLAM, 4D Primitive-Mache;
- persistence theory: Perpetua;
- low-relevance robustness control: DYMRO-SLAM.

Detailed audits are in files `13`, `16`, and `18`--`21`.

## Remaining task: bounded citation-chain saturation

The next task is not to add papers for quantity. It is to inspect references and
citing papers of the closest systems and answer one question:

> Does any uncatalogued paper implement a complete D1+D2 session, export the
> required dense object-and-structural scene state, initialize an independent
> later session, reconcile D3, resume D1+D2, and recursively export the next
> prior?

Priority seeds for backward/forward chaining:

1. Khronos and Changing-SLAM;
2. Panoptic Multi-TSDFs, POCD, POV-SLAM, and OASIS-Map;
3. ObVi-SLAM and ProbPer-LiLo;
4. Pomerleau 2014, Dynamic Pose Graph SLAM, LT-Mapper, ELite, and RBIF;
5. GaME and LT-Gaussian;
6. SuperMap and DYNEMO-SLAM.

A newly found paper is promoted to full-text audit only when it introduces a new
state variable, temporal protocol, representation, or recurring session
architecture not already covered by the 28 verified papers.

## Stop rule

The novelty audit may be considered saturated for the submission draft only
when:

1. backward references of all closest seeds have been screened;
2. forward/citing-paper searches have been performed using at least two
   independent query formulations;
3. no new direct neighbour survives title/abstract screening and full-text
   verification;
4. every manuscript novelty sentence is supported by the verified matrix;
5. publication status is refreshed immediately before submission.

## Reading rule

No newly discovered method enters the Introduction or supports a novelty claim
until the original complete text has been checked for:

- input and session protocol;
- state variables and representation;
- update equations;
- retained versus discarded output;
- experiments, metrics, and baselines;
- limitations and future-work boundaries.
