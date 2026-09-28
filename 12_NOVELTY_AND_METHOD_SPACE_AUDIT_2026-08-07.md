# Corrected Novelty and Method-Space Audit

Status checked: **2026-08-07**

This file supersedes the earlier version of the novelty audit. The correction was
triggered by a full-text reread of SuperMap, DYMRO-SLAM, and ELite. In particular,
the earlier audit overestimated their overlap by treating words such as
`spatio-temporal`, `persistent`, and `lifelong` as if they were equivalent to the
project's D1/D2/D3 taxonomy.

For detailed source-grounded corrections, read
`13_SUPERMAP_DYMRO_ELITE_FULL_TEXT_CORRECTION_2026-08-07.md`.

## 1. Canonical problem

```text
Within each continuously running session:
  D1 = motion is observed while it occurs
  D2 = a change occurs while the robot looks elsewhere

Across completed independent sessions:
  D3 = Session B imports persistent scene state from completed Session A,
       reconciles A-to-B change, runs its own D1+D2, and exports state for C
```

D1 and D2 are two observation modes in one dynamic-mapping session. D3 is the
interface connecting complete sessions. An arbitrary sequence cut is not D3.

## 2. Honest novelty conclusion

The phrase **“nobody has considered three kinds of dynamics”** is too broad.
Prior work contains most individual ingredients:

- dense D1 trajectories and dynamic geometry;
- D2 fragment/object association across observation gaps;
- visibility, free-space, persistence, absence, and non-detection evidence;
- cross-session map alignment and point/object map updates;
- point-wise ephemerality, object stationarity, and delta maps;
- continuous object-centric semantic scene graphs.

However, the three uploaded papers do **not** already solve this project's exact
problem:

- SuperMap is one continuous-stream object-centric semantic SLAM system;
- DYMRO-SLAM is dynamic-feature filtering for robust localization;
- ELite is point-level D3 lifelong-map maintenance that removes D1 dynamics.

The safe conclusion remains:

> In the primary literature audited so far, we did not find a dense
> metric-semantic SLAM system in which a completed D1+D2 session exports the
> state needed by an independently started session to reconcile D3, resume D1
> and D2, and recursively export the next persistent state while retaining both
> dynamic history and current structural geometry.

This is a literature-based `to the best of our knowledge` claim, not a proof of a
universal negative.

## 3. Corrected closest-method ranking

### 3.1 Khronos: closest problem and representation base

Khronos already solves dense single-session D1+D2:

- active-window tracking and time-indexed dynamic entities;
- background mesh and object fragments;
- global reconciliation across observation gaps;
- ray/free-space evidence.

Its published formulation is one continuously running problem over
`t=0,...,T`. The paper does not provide a process-separated A-export/B-import
protocol that resumes the complete estimator.

**Implication:** D1 and D2 are inherited capabilities, not new contributions.

### 3.2 Panoptic Multi-TSDFs / POCD / POV-SLAM: closest D3 state and inference

These methods supply dense or object-level cross-session mechanisms:

- prior/current volumetric submaps;
- persistent, absent, and unobserved states;
- object stationarity/change beliefs;
- repeated-visit pose and object consistency.

They do not preserve the complete D1 trajectories and temporal geometry of every
new session.

**Implication:** hard state names, object stationarity, and cross-session object
updates are not new by themselves.

### 3.3 ELite: strong point-level D3 baseline, not the same hierarchy

ELite performs:

- multi-session LiDAR map alignment;
- local point ephemerality estimated from rays;
- removal of current-session dynamic points;
- recursive global ephemerality and lifelong/static/delta maps.

Its local ephemerality is a dynamic-versus-static removal score. It does not
represent D1 trajectories or D2 hidden transitions and identities. ELite is
therefore a strong D3 geometry baseline, but it does not propose the same
D1+D2-over-D3 system.

**Implication:** ray-based point ephemerality and recursive point-map update are
existing mechanisms, but they do not invalidate the full scene-memory problem.

### 3.4 SuperMap: relevant semantic-object mapper, not a D3 predecessor

SuperMap formally processes one continuous RGB-D/point-cloud sequence and
updates pose, instance IDs, and object map at every time step. It maintains:

- open-vocabulary instance association;
- observable/unobservable/disappeared point evidence;
- Bayesian semantic fusion;
- spatial and temporal scene-graph edges;
- object additions/removals in a ten-minute continuous experiment.

Its own limitations state that highly dynamic object tracking remains weak. It
does not export a completed dense session state to an independent new process.

**Implication:** SuperMap is relevant to instance identity, semantic confidence,
and object-level D2-like maintenance, but it is not a major threat to D3
continuation novelty.

### 3.5 DYMRO-SLAM: low relevance

DYMRO-SLAM removes dynamic features using Mask R-CNN and improves ORB-SLAM3
tracking using optical flow. It evaluates camera ATE/APE and runtime. It does not
store dynamic-object trajectories, scene changes, or multi-session memory.

**Implication:** it belongs only to a broad dynamic-robust localization category
and should not shape the core method or claim.

## 4. Existing method mechanisms by component

### D1 mechanisms already established

- semantic/geometric dynamic-feature filtering;
- per-object surfel, TSDF, SDF, octree, Gaussian, or primitive maps;
- joint robot/object bundle adjustment and factor graphs;
- pose, velocity, shape, trajectory, and temporal box estimation;
- rigid and non-rigid 4D reconstruction.

### D2 mechanisms already established

- local motion versus global jump association;
- object/fragment reactivation after observation gaps;
- ray presence/absence and visibility reasoning;
- detections versus repeated non-detections;
- persistent/absent/unobserved/new states;
- stale map/keyframe removal;
- existence confidence and semantic confidence.

### D3 mechanisms already established

- multi-session alignment and loop closure;
- prior/current submap comparison;
- positive/negative change detection;
- point-wise ephemerality and object stationarity;
- lifelong/static/delta maps;
- map version control and rollback;
- persistent object landmarks and cross-session association.

## 5. Method claims to avoid

The following are insufficient as a primary contribution:

1. naming D1, D2, and D3;
2. save/load or checkpoint support alone;
3. naive union, overwrite, distance deletion, or ray deletion alone;
4. one scalar persistence/ephemerality score;
5. object association or semantic confidence alone;
6. dynamic masking or promotion alone;
7. a base/current/delta map trio alone;
8. swapping TSDFs for Gaussians or scene graphs;
9. combining Khronos with Panoptic/POCD without new inference;
10. an A/B pairwise experiment without B's own D1+D2 and preferably Session C.

## 6. Defensible method territory

The strongest remaining question is:

> What state must a completed dense D1+D2 mapping session persist so that an
> independent later session can correctly continue, rather than merely compare
> or clean two maps?

The persistent state should preserve at least:

```text
current dense object/structural geometry
D1 dynamic histories that should not enter the static map
object memory and semantic state
visibility / re-observation evidence
last support and contradiction evidence
session provenance
unresolved associations when the method actually supports them
```

The important distinctions are:

```text
not observed != observed absent
observed motion != hidden transition
clean current map != complete dynamic memory
same semantic label != proven same instance
```

The method does not need to rebuild Khronos's D1/D2 estimator. A defensible
contribution can be the **session-boundary state definition and update rule** that
lets those capabilities recur while maintaining a correct current dense map.

A richer probabilistic identity-hypothesis model is one possible extension, but
it should not be claimed as the established method until implemented and
validated. The current paper should not promise latent variables that are absent
from the code.

## 7. Required evidence

The final evaluation should demonstrate:

```text
Session A:
  D1 event
  D2 event
  export persistent state

A-to-B gap:
  real environmental intervention

Independent Session B:
  load A state
  reconcile D3
  process new D1 and D2
  export B state

Preferably Session C:
  demonstrate recursive continuation and bounded error accumulation
```

Metrics should separate:

- D1 trajectory/history and dynamic-to-static leakage;
- D2 persistent/absent/unobserved/new decisions;
- D3 stale removal, new geometry, and unobserved preservation;
- dense current-map quality;
- update time and memory growth.

## 8. Current safest positioning

> Khronos provides dense D1+D2 mapping within one continuous session, while
> Panoptic Multi-TSDFs, POCD/POV-SLAM, ELite, and related lifelong systems
> provide different cross-session map-update mechanisms. We study how to persist
> and reconcile the complete object-and-structure scene state so that an
> independently started session can update D3 and continue D1+D2.
