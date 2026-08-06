# Priority Full-Text Audit Queue

Status: **2026-08-07**

Priority is based on overlap with the canonical D1+D2 / D3 story, not title or
popularity.

## Completed correction audit

The following uploaded papers have now been read across the full method,
experiments, figures, and limitations:

- **SuperMap:** continuous-stream semantic object map; relevant to object-level
  D2-like maintenance, not process-separated D3.
- **DYMRO-SLAM:** dynamic-feature rejection for robust localization; low relevance.
- **ELite:** strong point-level D3 lifelong-map update; not D1+D2 and deliberately
  removes D1 dynamic history.

See `13_SUPERMAP_DYMRO_ELITE_FULL_TEXT_CORRECTION_2026-08-07.md`.

## Priority A - can still change the novelty boundary

### A1. ProbPer-LiLo

Resolve from the full paper:

- exact factor-graph variables and temporal links;
- whether observability is distinct from object existence;
- whether the map retains dynamic/quasi-static history or removes it;
- session serialization and recursive update protocol;
- whether structural geometry is represented.

### A2. DYNEMO-SLAM / Dynamic Situational Graphs

Resolve:

- moving agents versus displaced objects;
- time-indexed entity geometry and identity;
- handling of reactivation after long gaps;
- whether any independent-session state is restored;
- how close the entity graph is to Khronos's representation.

### A3. Perpetua

Resolve:

- persistence/emergence filter equations;
- multi-hypothesis state and parameter learning;
- relationship between missing observation and absence;
- how it could serve as a theoretical baseline without being a dense mapper.

### A4. OASIS-Map

Resolve:

- exact cross-session association variables;
- treatment of unknown/unobserved content;
- dependence on an external multi-session SLAM backend;
- publication status before submission.

## Priority B - strong method or baseline relevance

- RBIF: ray/voxel contradiction and conservative deletion;
- LTC-Mapping: visibility and non-detection object confidence;
- LT-Mapper and Lifelong 3D Mapping: multi-session alignment, positive/negative
  changes, version control;
- 4D Primitive-Mache: object permanence inside one video, for D1 representation
  boundaries;
- GaME and LT-Gaussian: representation-adjacent D2/D3.

## Reading rule

No method enters the Introduction or supports a novelty claim until the original
paper has been checked for:

1. input/session protocol;
2. state variables and representation;
3. actual update equations;
4. output retained versus discarded;
5. experiment protocol and metrics;
6. limitations and future-work boundaries.
