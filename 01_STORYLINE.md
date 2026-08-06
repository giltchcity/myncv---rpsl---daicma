# Paper Storyline

Date: 2026-08-06

## Working Thesis

Dense dynamic mapping systems should not treat visible motion, hidden change,
and cross-session change as unrelated special cases. They are three evidence
regimes of the same scene-memory problem. A map element should be retained,
removed, or added according to whether later observations provide presence,
absence, or no information.

## Problem

A robot's environment changes at several time scales:

- people and objects move while the robot watches;
- an object or structural element changes while outside the field of view;
- the robot terminates a run and returns to a changed environment later.

Existing components cover important parts of this problem but leave a practical
gap:

- Khronos unifies short- and long-term changes in a continuous spatio-temporal
  run, but its released workflow is not a persistent session restart protocol.
- Panoptic Multi-TSDFs provides useful active/inactive submap conflict states,
  but primarily assumes externally supplied poses and is not a Khronos-style
  spatio-temporal memory.
- POCD supplies an object stationarity interpretation, but is object-centric and
  does not directly maintain a unified background/global mesh across sessions.

The practical failure is easy to see: naive union leaves stale geometry, while
naive deletion combines the missing or noisy regions from both traversals and
damages unchanged floors and walls.

## Method Lineage and Novelty Boundary

The paper must separate reused capability from our implementation contribution:

```text
Khronos:
  active-window motion detection and tracking
  object fragments and private static-object meshes
  global/background mesh and DSG representation
  ray/free-space presence and absence evidence

Panoptic Multi-TSDFs:
  active/inactive comparison logic
  persistent / absent / unobserved state interpretation
  TSDF conflict/match predicate ported behind DistanceQuery

POCD:
  stationarity-belief motivation
  probabilistic object-update interpretation
  not currently used as an executable backend

Our Base1 layer:
  persistence of final-current scene memory across sessions
  A-prior + B-evidence global-mesh reconciliation
  conservative re-observation-gated deletion and welded addition
  explainable vertex/object decisions and session provenance
  semantic dynamic masking and promotion integrated into Khronos
```

The contribution is therefore not “a new SLAM system from scratch.” It is an
evidence-gated scene-memory and update layer that connects these capabilities
across observation regimes and process-separated sessions.

## Key Insight

Use one conservative state vocabulary for objects and structural geometry:

```text
dynamic_observed | persistent | absent | unobserved | new
```

The distinction between `absent` and `unobserved` is central:

```text
no matching observation != evidence of absence
```

Only reliable free-space or contradictory re-observation may remove inherited
geometry. Otherwise it remains in memory. Current stable geometry may repair or
extend the retained map.

## Three Regimes

### 1. Observed Motion

```text
visible dynamic semantics/geometric motion
-> dynamic measurements
-> Khronos tracker
-> trajectory + temporal bbox + point frames
-> excluded from static TSDF
```

This prevents a tracked or semantically dynamic person from becoming static
ghost geometry. It does not hallucinate motion after the person is out of range.

### 2. Hidden Within-Session Change

```text
old element + later matching surface       -> persistent
old element + later reliable free space    -> absent
old element + no reliable later view       -> unobserved, keep
stable unmatched current surface/object    -> new
```

For a moved chair without observed motion, the honest output is
`absent@A + new@B`, not an invented trajectory.

### 3. Cross-Session Change

```text
saved A current map + A object memory
+ B reconstruction and observations
-> evidence-gated reconciliation
-> updated B current map + updated memory
```

The session boundary changes persistence and provenance, not the state logic.
Session B may itself contain both observed motion and hidden changes.

## Current Method Pipeline

```text
Khronos Session A
-> final current DSG/global mesh
-> object memory and dynamic history

Khronos Session B observations
-> current DSG/global mesh + rays + objects + dynamics

A prior + B evidence
-> classify inherited vertices: persistent / absent / unobserved
-> retain persistent and unobserved prior geometry
-> delete only ray-confirmed absent geometry
-> weld and add genuinely new B geometry
-> apply re-observation-gated object cleanup
-> optionally repair missing object surfaces from private object meshes
-> save updated final-current `.4dmap` and diagnostics
```

## Technical Contribution Candidates

These are candidate contributions, subject to quantitative validation:

1. A unified three-regime scene-memory formulation spanning observed motion,
   hidden change, and process-separated revisits.
2. Conservative cross-session mesh reconciliation using
   persistent/absent/unobserved evidence rather than unconditional union or
   object-distance deletion.
3. Semantic-assisted dynamic masking and tracking integrated into Khronos's
   existing active-window pipeline.
4. Object and structural geometry handled under a shared evidence model, with
   semantics used as a prior/protection cue rather than a deletion command.
5. Explainable per-vertex and per-object diagnostics for every map update.

## Experimental Story

### Experiment A: Observed Human Motion

Compare geometric-only Khronos against semantic masking and semantic-assisted
tracking. Show trajectory duration, semantic identity, and the human-shaped
old-only static mesh component removed by masking.

### Experiment B: Cross-Session Continuation

Show that B begins from A geometry, then partitions inherited vertices into
absent, persistent, and unobserved and adds B-only geometry. Include the
A-to-A idempotence control.

### Experiment C: Deletion Safety

Contrast naive object-distance cleanup with re-observation gating. Demonstrate
that unchanged wall/floor geometry near an object is protected while the
separate ray-confirmed prior-removal path remains active.

### Experiment D: Geometry Connectivity

Compare vertex-only insertion with triangle-aware welded insertion using face
counts and boundary-edge counts. Describe this as connectivity/coverage repair,
not TSDF reintegration.

### Required Final Quantitative Experiment

Use a dataset/protocol whose A/B timestamps map correctly to GT. Report
comparable final-current Background/Object/Change metrics for original Khronos,
naive union, naive cleanup, and the complete evidence-gated method.

## Suggested Paper Structure

1. Introduction
2. Related Work
3. Problem: Three Regimes of Scene Memory
4. Evidence-Gated Scene-Memory Reconciliation
5. Dynamic Semantic Integration
6. Experimental Protocol
7. Results and Ablations
8. Limitations
9. Conclusion
