# Priority Full-Text Audit Queue

Status: **2026-08-07**

This queue converts the broad search into a controlled reading plan. Priority is
based on potential overlap with the canonical story, not paper popularity.

## Priority A - possible novelty boundary changes

### A1. SuperMap (RSS 2026)

**Why urgent:** The official paper/project describes a persistent open-vocabulary
4D scene graph with stable object identities, existence-and-label confidence,
appearance/disappearance/relocation, temporal edges, and a two-hour real-robot
run. This is the closest newly found semantic scene-memory system.

**Questions to resolve from the full PDF:**

1. Is the system evaluated only as one continuous process, or does it serialize
   and import state across independent processes/sessions?
2. Does it reconstruct D1 motion trajectories or only object observation and
   relocation history?
3. How are disappearance, occlusion, non-observation, and re-activation
   mathematically distinguished?
4. Is its dense geometric layer maintained as current history or only used to
   anchor the instance graph?
5. What exactly are `DualMap` and Khronos comparisons in its change benchmark?
6. Can its code ingest RGB-D/Khronos-style data and become an object-state
   baseline?

**Provisional classification:** strong D2/scene-memory neighbour; strict D3 not
yet established.

### A2. ProbPer-LiLo (RA-L 2026)

**Why urgent:** It explicitly uses a discrete probabilistic factor graph to
classify object persistency, remove dynamic/quasi-static objects, and refine 3D
maps from multiple sessions. It may be the closest recent mathematical D3
competitor.

**Questions:**

1. What are the discrete variables, factors, measurements, and inference method?
2. Does `persistency` represent existence, stationarity, or suitability for a
   static localization map?
3. Does it preserve changed objects or deliberately remove all dynamic and
   quasi-static content?
4. How are unobserved areas treated?
5. Does each new session update one persistent map recursively?
6. Is code or the multi-campus dataset released?

**Verified status:** IEEE RA-L 11(3), 2530-2537, 2026; DOI
`10.1109/LRA.2026.3653311`.

### A3. SuperMap versus Khronos versus our P-SMS

After A1/A2, produce a three-column claim matrix covering:

- continuous D1 trajectory geometry;
- same-session D2 hidden change;
- strict process-separated D3;
- dense background current map;
- object identity/history;
- absent versus unobserved;
- session serialization;
- pose/change joint estimation;
- recursive A -> B -> C operation.

## Priority B - scene-graph and persistent dynamic representations

### B1. DYNEMO-SLAM / Dynamic Situational Graphs

Inspect whether displaced objects are handled as observed trajectories, pose
jumps, persistent landmarks, or graph re-association. Confirm publication status
of both variants and whether the IROS 2025 paper supersedes the arXiv system.

### B2. 4D Primitive-Mache

Resolve the exact meaning of `persistent`: replayable object permanence inside a
single video versus persistent map state across robot deployments. Inspect its
motion extrapolation after invisibility and whether it provides a useful D1/D2
representation idea without being SLAM D3.

### B3. LTC-Mapping

Audit the non-detection model, vertex visibility test, confidence decay,
occlusion handling, and whether experiments constitute D2, D3, or a session-
agnostic continuous object map.

### B4. 3D VSG and Scene Graph Memory

Separate predictive semantic variability / object search memory from map
maintenance. Extract mathematical priors that could improve association or
re-observation scheduling without misclassifying these systems as SLAM.

## Priority C - recent geometric D3 systems

### C1. RBIF (IROS 2024)

Compare its probabilistic ray-bundle interference to Khronos RayVerificator and
our hard absence gate. Determine whether it is the best traditional geometric
baseline or mathematical source for safe deletion.

### C2. LLMF (2026)

Inspect the global-to-local BEV/FV projection, session alignment assumptions,
change mask, update policy, and nine-month/32-run evaluation. Likely engineering
D3 baseline rather than dynamic scene-history competitor.

### C3. Lifelong 3D Mapping Framework (2025 preprint)

Inspect map version control and positive/negative changes. The ability to
reconstruct arbitrary past session maps may be relevant to memory compression
and history queries.

### C4. SLAM-RAMU (2024)

Determine whether autonomous map update preserves multiple histories or simply
replaces a localization map, and whether its implementation is reproducible.

## Priority D - Gaussian representatives retained in manuscript

Read/update full ledgers for exactly these roles:

1. WildGS-SLAM - dynamic suppression/static map;
2. 4DTAM - non-rigid D1;
3. 4D Gaussian Splatting SLAM - D1 Gaussian SLAM;
4. DynaGSLAM - real-time D1 and motion prediction;
5. GaME - D2 map evolution;
6. LT-Gaussian - D3 map-update component;
7. GS-LTS - optional D3 semantic editor preprint.

Other Gaussian works remain watchlist candidates unless the final method or
experiments adopt their representation or metrics.

## Priority E - mathematical temporal map models

- Occupancy Grid Models for Changing Environments;
- FreMEn;
- Spatio-Temporal Hilbert Maps;
- Bayesian Hilbert Maps;
- long-term navigation with ARMA map prediction;
- Maps of Dynamics for long-term motion prediction.

Goal: identify principled mechanisms for time-conditioned priors, uncertainty,
periodic recurrence, active revisit scheduling, or belief compression. These are
method-inspiration sources, not direct P-SMS baselines.

## Evidence template for each completed audit

```text
Citation and publication status
Exact PDF/version/hash
Problem and session definition
Inputs and pose assumptions
Map/state variables
Actual update equations
D1 capability
D2 capability
D3 capability
Experiments and metrics
Limitations/future work
Original short quotes with page/section
Allowed manuscript conclusion
Prohibited overstatement
Baseline feasibility
```
