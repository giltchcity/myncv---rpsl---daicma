# Authoritative Storyline and Taxonomy Re-Audit

Status checked: **2026-08-06**

This file is the authoritative taxonomy for the Introduction, Related Work, and
all literature audits. If an older note uses `D1`, `D2`, or `D3` differently,
this file takes precedence.

## The story, stated three times

1. **D1 and D2 are the two dynamic-observation modes inside one continuously
   running SLAM session. D3 is the persistent connection between completed
   independent sessions.**
2. **D1 and D2 are the two dynamic-observation modes inside one continuously
   running SLAM session. D3 is the persistent connection between completed
   independent sessions.**
3. **D1 and D2 are the two dynamic-observation modes inside one continuously
   running SLAM session. D3 is the persistent connection between completed
   independent sessions.**

The hierarchy is therefore:

```text
Session A
  D1: the robot observes motion continuously
  D2: change occurs while the robot looks elsewhere, but A is still running
  -> export persistent scene memory M_A

A-to-B boundary
  D3: the environment changes after A has completed and before B starts

Session B imports M_A
  reconcile D3 changes
  run new D1 events
  run new D2 events
  -> export persistent scene memory M_B
```

D3 is not a third motion detector. It is not produced by cutting one continuous
sequence and restarting at the cut. A checkpoint/recovery experiment is useful
as a software control, but it is not evidence for inter-session environmental
change.

## Hard classification rules

A paper may be labeled **D1** only if it estimates or explicitly handles motion
observed during the current continuous sequence. A method that merely rejects
moving pixels is D1-related robustness, not a D1 scene-history method.

A paper may be labeled **D2** only if the old and new observations belong to the
same still-running mapping process and the transition occurs during an
observation gap. `Long-term`, `out-of-view`, or `abrupt` does not by itself imply
D2; the session structure must be checked.

A paper may be labeled **D3 system** only if a completed earlier run/session
produces persistent state that is used by a later independent run/session. A
pairwise change detector or prior-map editing module is at most a **D3
component** unless it defines the recurring session-memory interface.

A complete target system must satisfy:

```text
D1 + D2 inside every session
plus
D3 persistence and reconciliation across sessions
```

## Re-audited classification of the current citations

| Method | Correct role | D1 | D2 | D3 | Critical boundary |
|---|---|---:|---:|---:|---|
| Co-Fusion | dense rigid-object tracking/reconstruction | yes | no | no | continuous live RGB-D only |
| MaskFusion | instance-aware rigid-object tracking | yes | no | no | non-rigid people removed |
| DynaSLAM | dynamic-input robust static mapping | handled by rejection | no | no | no retained dynamic history |
| Dynablox | moving-point detection | detector | no | no | no object trajectory/identity |
| DynoSAM | joint robot/object motion estimation | yes | no | no | current dynamic sequence |
| Bore et al. 2019 | partially observed movable-object tracking | partial | object-level D2 | not established | no dense scene map |
| Changing-SLAM | sparse single-session changing-scene SLAM | yes | yes | no demonstrated D3 | continuous sequences; localization evaluation |
| Khronos | dense single-session spatio-temporal SLAM | yes | yes | no published continuation protocol | one temporal problem over t=0,...,T |
| Pomerleau et al. 2014 | point-level repeated-survey map maintenance | point velocity only | no explicit D2 state | D3 predecessor/component | no objects, semantics, dense free space, or history |
| Lázaro et al. 2018 | multi-session 2D local-map maintenance | no | no | yes | no dynamic-object history |
| Panoptic Multi-TSDFs | dense long-term submap consistency | no | not its main setting | yes | run 2 starts from run 1 prior; D1 left future work |
| POCD | object-level semi-static mapping between traversals | no | no | yes | external localization; explicit dynamics future work |
| POV-SLAM | joint localization and semi-static consistency | no complete D1 | no | yes | repeated visits/month-separated trajectories |
| ObVi-SLAM | persistent object landmarks for localization | no | no | yes | static-object localization map |
| Living Scenes | cross-time object matching/reconstruction | no | no | D3 reconstruction component | not online SLAM/background memory |
| OASIS-Map | cross-session object association/change states | no | no | D3 component | under-review preprint; external multi-session SLAM poses |
| Gaussian Splatting SLAM / SplaTAM | static Gaussian SLAM | no | no | no | static scene assumption |
| WildGS-SLAM / Gassidy | dynamic-input robust static Gaussian maps | rejected/suppressed | no | no | moving entities not preserved |
| 4DGS-SLAM / D4DGS / DynaGSLAM / Flow4DGS / RU4D | continuous 4D Gaussian reconstruction | yes | no established D2 | no | sequence-level temporal motion |
| GaME | online Gaussian update after out-of-view changes | no dynamic history | yes | no published process-separated D3 | poses/segmentation supplied externally |
| LT-Gaussian | old Gaussian map + later LiDAR update | no | no | D3 map-update component | no unobserved state or D1+D2 session |
| GS-LTS | long-term service-scene Gaussian editing | no | no | D3 map-update component | preprint; explicitly excludes real-time dynamics |
| GS-DIFF | primitive-space comparison of two Gaussian scenes | no | no | D3 change-detection component only | not SLAM, memory continuation, or map update |

## Original-text anchors for the closest works

### Khronos: D1 + D2 inside one continuous problem

- RSS 2024, Introduction, PDF p. 2: short-term dynamics are objects currently
  moving in front of the camera; long-term changes occur while the robot is not
  directly observing the scene.
- Problem statement, PDF p. 3: object and robot states are indexed over
  `t = 0, 1, ..., T`, and the current estimate reasons about prior times
  `t <= T`.
- The paper discusses multi-session change detection as related work, but does
  not present a completed-A export / independent-B import experiment.

Allowed conclusion: **Khronos is the main dense D1+D2 single-session base.**

### Panoptic Multi-TSDFs: D3 without D1

- Map management, PDF p. 4: inactive submaps have
  `persistent`, `unobserved`, and `absent` change states.
- Evaluation, PDF pp. 4--5: the Flat dataset contains two trajectories with
  changes between runs; the second trajectory is evaluated from a prior map
  built in the first run.
- Conclusion, PDF p. 7: accounting for short-term dynamics is future work.

Allowed conclusion: **Panoptic is a strong dense D3 representation/update
baseline, not a D1+D2 dynamic SLAM system.**

### POCD and POV-SLAM: D3

- POCD, Introduction, PDF p. 1: changed object locations are considered between
  robot traversals and may occur while the robot is offline.
- POCD assumptions, PDF p. 4: changes are additions, removals, or planar object
  motion between traversals; robot poses are obtained externally.
- POCD discussion, PDF p. 10: explicit handling of dynamics is future work.
- POV-SLAM, experiments, PDF p. 11: two trajectories captured four months apart
  are stitched to introduce scene changes.

Allowed conclusion: **POCD/POV-SLAM are D3 methods. They are not D2 simply
because the intermediate motion was unobserved.**

### GaME versus long-term Gaussian update

- GaME defines changes outside the current view and continuously adapts one
  online Gaussian map. No process-separated A-memory/B-import protocol is
  evaluated. It is classified as D2.
- LT-Gaussian uses an old-time Gaussian map and new-time LiDAR stream, aligns
  them, detects emerging/disappearing points, and uses the processed old map as
  a prior. It is a D3 map-update component.
- GS-LTS explicitly states that it focuses on medium-term changes rather than
  real-time moving objects or human interactions. It is a D3 editing component,
  not a system combining D1+D2+D3.

## Corrections to earlier wording

The following phrasings are prohibited:

- `D1, D2, and D3 are three parallel dynamic regimes.`
- `Any out-of-view or long-term change is D3.`
- `POCD/POV-SLAM are D2 because motion was not observed.`
- `Any two-map change detector is a D3 SLAM system.`
- `Long-term point tracking in a 4D Gaussian sequence means cross-session memory.`

Use instead:

> D1 and D2 are complementary observation modes within each continuously
> running dynamic-mapping session. D3 is the persistent scene-memory interface
> that connects completed sessions, while every newly initialized session again
> performs D1 and D2.

## Manuscript status after this re-audit

The Introduction and Related Work were rewritten on 2026-08-06 to use this
hierarchy. The older full-text evidence ledgers remain useful for source quotes,
method assumptions, and limitations, but any shorthand coverage label in those
files must be interpreted according to this authoritative re-audit.
