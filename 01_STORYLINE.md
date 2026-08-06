# Paper Storyline

Date: 2026-08-06

## Canonical Thesis

Long-term dynamic SLAM has a two-level temporal structure:

```text
inside every continuously running session:
  D1 = motion observed while it happens
  D2 = change occurring while the robot looks elsewhere

across completed independent sessions:
  D3 = persistent scene-memory continuation and inter-session reconciliation
```

D1 and D2 are not separate long-term systems. They are the two observation modes
of dynamic mapping inside one session. D3 is not a third detector. It is the
persistent interface that connects complete D1+D2 sessions:

```text
Session A runs D1 + D2
-> export M_A
-> environment changes between sessions
-> Session B imports M_A and reconciles D3
-> Session B concurrently runs new D1 + D2
-> export M_B
-> Session C ...
```

## Problem

A robot's environment changes at two levels.

### Level 1: single-session dynamic mapping

- **D1:** people or objects move while the robot watches. The motion itself is
  observed and can be represented as a trajectory, temporal bounding boxes,
  timestamps, and time-indexed geometry.
- **D2:** an object or structural element changes while outside the field of
  view, but the same SLAM session remains active. When the robot returns, the
  system sees only the old and new states and must distinguish persistent,
  absent, unobserved, and new content without inventing a trajectory.

Khronos is the primary dense D1+D2 base: its active temporal window handles D1,
while its global reconciliation handles D2 in one continuous spatio-temporal
mapping problem.

### Level 2: cross-session continuation

- **D3:** Session A terminates, the environment changes while the robot is
  absent, and an independently started Session B must load persistent memory
  from A and update it.

Session B does not merely perform pairwise change detection. It is again a full
dynamic mapping session, so B must reconcile A-to-B changes while simultaneously
processing new D1 and D2 events. The same requirement repeats for Session C and
later deployments.

A temporal cut in one continuous sequence is not D3. Restarting at the cut is a
checkpoint/recovery control unless the data represent a genuinely independent
revisit and the earlier completed scene state is used as the prior.

## Existing Components and the Gap

- **Khronos:** dense D1+D2 inside one continuously running spatio-temporal SLAM
  problem; no published process-separated scene-memory continuation protocol.
- **Panoptic Multi-TSDFs:** dense D3-style prior-run/current-run volumetric
  consistency with persistent/absent/unobserved states; short-term dynamics are
  explicitly future work.
- **POCD / POV-SLAM:** D3 object-level semi-static mapping across traversals;
  POCD uses external localization, while POV-SLAM jointly estimates pose and
  object consistency. Neither preserves complete D1 temporal histories.
- **Recent 4D Gaussian SLAM:** strong D1 photorealistic reconstruction from
  continuous sequences, but no established D2 hidden-change state or D3 memory.
- **GaME:** strong Gaussian D2 update after out-of-view changes, but no D1
  dynamic histories and no published process-separated D3 continuation.
- **LT-Gaussian / GS-LTS:** D3 map-revision components, but not complete sessions
  that also run D1+D2.

The practical gap is therefore not that no method has ever handled more than one
kind of change. The missing capability is a recurring system in which a complete
dense D1+D2 session exports persistent scene memory, a later independent session
uses that memory to reconcile D3, and the later session again performs D1+D2.

## Method Lineage and Novelty Boundary

The paper must separate reused capability from the final contribution:

```text
Khronos:
  active-window D1 motion detection and tracking
  fragment construction and private static-object meshes
  global/background mesh and DSG representation
  ray/free-space evidence and D2 reconciliation

Panoptic Multi-TSDFs:
  prior/current submap comparison
  persistent / absent / unobserved state semantics
  TSDF conflict/match predicates

POCD / POV-SLAM:
  D3 object stationarity and pose/change ambiguity

Current Base1 layer:
  persistence of final-current scene memory across sessions
  A-prior + B-evidence global-mesh reconciliation
  conservative re-observation-gated deletion and welded addition
  explainable vertex/object decisions and session provenance
  semantic dynamic masking and promotion integrated into Khronos
```

The final method innovation is still under development. The paper must not claim
that the current combination of these components is already sufficient novelty.
The target contribution is the persistent representation and inference mechanism
that makes complete D1+D2 mapping recur across D3 boundaries.

## Key Scene Reasoning

For D2 and D3 reconciliation, the distinction between `absent` and `unobserved`
is central:

```text
no matching observation != evidence of absence
```

```text
old element + later matching surface       -> persistent
old element + later reliable free space    -> absent
old element + no reliable later view       -> unobserved, keep
stable unmatched current surface/object    -> new
```

For a moved chair whose transition was not observed, the honest output is
`absent@old + new@new` unless identity association is reliable. D1 is different:
when the motion is observed continuously, the output can be a real trajectory.

## Current Pipeline

```text
Khronos Session A
  run D1 + D2
  -> final current DSG/global mesh
  -> object memory and dynamic history
  -> persistent memory M_A

Independent Khronos Session B
  load M_A
  reconcile A-to-B D3 changes using B evidence
  concurrently run B's D1 + D2
  -> updated current map and memory M_B
```

The current implementation restores and reconciles saved map state. It is not a
native hot restart of Khronos's full active window, PGMO graph, live ray hash, or
backend threads.

## Technical Contribution Candidates

Subject to method development and quantitative validation:

1. A P-SMS problem formulation with D1+D2 inside each session and persistent D3
   continuation across sessions.
2. A principled persistent scene-memory representation and update mechanism that
   preserves sufficient state for complete dynamic mapping to recur after
   process termination.
3. Conservative dense map reconciliation that distinguishes absence from lack
   of observation and updates object and structural geometry without naive union
   or overwrite.
4. A unified evaluation protocol that tests D1 and D2 inside each session and D3
   across independent sessions.

Semantic-assisted masking/tracking, explainable per-element diagnostics, and
welded topology are supporting system components unless later experiments show
that one merits a separate contribution.

## Experimental Story

### Experiment A: D1 within a session

Compare geometric-only Khronos against semantic masking and semantic-assisted
tracking. Evaluate trajectory duration, dynamic representation, and
static-map contamination.

### Experiment B: D2 within the same session

Use a continuous session in which the robot observes an old state, looks away,
and returns after a hidden change. Evaluate persistent/absent/unobserved/new
reasoning without claiming an unobserved trajectory.

### Experiment C: D3 across independent sessions

Session A ends and exports memory. The environment is modified. Session B starts
independently, loads A memory, reconciles inter-session changes, and contains its
own new D1 and D2 events. A Session C experiment is preferable to demonstrate
recurring memory rather than pairwise differencing.

### Safety and representation ablations

- naive union versus prior replacement versus evidence-gated update;
- absence versus unobserved protection;
- distance-only cleanup versus re-observation gating;
- vertex insertion versus topology-aware welding;
- hard state versus the finalized probabilistic/inference method.

## Suggested Paper Structure

1. Introduction
2. Related Work
3. Problem: Single-Session D1+D2 and Persistent D3 Continuation
4. Persistent Scene-Memory Representation and Inference
5. Dense Map Materialization and Dynamic Integration
6. Experimental Protocol
7. Results and Ablations
8. Limitations
9. Conclusion
