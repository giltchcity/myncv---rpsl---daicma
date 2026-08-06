# Novelty and Method-Space Audit: Persistent D1+D2 Sessions Across D3

Status checked: **2026-08-07**

This is the current author-side novelty audit. It is intentionally stricter than
the manuscript. It records what the literature already contains, what has only
a superficial resemblance to this project, and what methodological territory
remains plausibly defensible.

## 1. Canonical problem

```text
Within each continuously running session:
  D1 = motion is observed while it occurs
  D2 = the scene changes while the robot looks elsewhere

Across completed independent sessions:
  D3 = Session B imports persistent scene memory from completed Session A,
       reconciles A-to-B change, runs its own D1+D2, and exports memory for C
```

D1 and D2 are two observation modes inside one session. D3 is the persistent
interface between complete sessions. An arbitrary sequence split or a software
checkpoint is not a D3 experiment.

## 2. Is the exact three-part problem already proposed?

### Honest answer

We cannot prove a universal negative over all publications. The safe conclusion
from the primary literature audited so far is:

> We found many systems that combine two temporal scales or several adjacent
> capabilities, but did not find a dense metric-semantic system that retains D1
> time-indexed dynamic histories, performs explicit D2 hidden-change reasoning,
> exports a sufficient scene belief at process termination, and initializes an
> independent Session B that again performs D1+D2 before recursively exporting
> its state to Session C.

The broad phrase **“three kinds of dynamics have never been considered
jointly” is not defensible**. Several papers already use nearly equivalent
high-level language:

- Khronos unifies short-term motion and long-term/out-of-view change inside one
  continuous spatio-temporal SLAM problem.
- ELite explicitly models local ephemerality inside one session and global
  ephemerality across sessions, then recursively updates a lifelong map.
- SuperMap builds persistent object identities and a queryable 4D scene graph
  with appearance, disappearance, and relocation.
- DYNEMO-SLAM jointly represents moving agents and intermittently displaced
  objects in an optimizable scene-graph SLAM backend.
- ProbPer-LiLo models object persistency probabilistically and refines maps from
  multiple sessions.

The potential novelty is therefore not the existence of three labels or two
temporal scales. It is the **retained state and recursive inference interface**
that connects complete D1+D2 mapping sessions.

## 3. Strongest novelty neighbours

### 3.1 Khronos — dense D1+D2, no published process-separated bridge

**Status:** RSS 2024, published.

**Implemented state:** robot trajectory, background mesh, object fragments,
dynamic trajectories, temporal object geometry, and global reconciliation.

**What it already establishes:** A dense spatio-temporal metric-semantic map can
jointly represent continuously observed motion and changes revealed after an
observation gap.

**Boundary:** The published problem is indexed over one temporal sequence
`t=0,...,T`. The paper does not evaluate a completed-A export / independent-B
import / B-resumes-D1+D2 / B-exports-to-C protocol.

**Consequence:** The proposed work cannot claim D1 or D2 as new. Its task is to
identify and persist the state needed for Khronos-like inference to recur after
process termination.

### 3.2 ELite — the strongest two-timescale lifelong-map predecessor

**Status:** ICRA 2025, published, DOI 10.1109/ICRA55743.2025.11127618.

**Original formulation:** ELite has local ephemerality `epsilon_l`, the
probability that a point is dynamic within one session, and global ephemerality
`epsilon_g`, the long-term probability that a point is transient. It recursively
updates

```text
M_t = L(M_{t-1}, S_t)
```

from a previous lifelong map and a new session. It performs multi-session
alignment, dynamic-object removal, and map update. It stores a lifelong point
map, a thresholded static map, and a delta map.

**Why it is a serious threat:** It already contributes two temporal scales,
point-wise ray evidence, Bayesian local/global ephemerality, multi-session
alignment, recursive update, change categories, and map history.

**Critical difference:** ELite deliberately discards high-local-ephemerality
points to create a cleaned session map. It does not retain D1 object identities,
trajectories, temporal bounding boxes, or time-indexed geometry. Its local state
is dynamic-versus-static ephemerality, not a D2 model separating observability,
existence, and identity after an unobserved transition. Its principal output is
an up-to-date static/lifelong point map, not a complete dense dynamic scene
history.

**Consequence:** Never claim that a local/global temporal hierarchy, ray-based
Bayesian persistence, recursive session map update, or a lifelong/static/delta
map trio is new by itself.

### 3.3 SuperMap — the strongest persistent semantic-memory neighbour

**Status:** RSS 2026, published.

**Implemented state:** high-frequency geometric SLAM, asynchronous
open-vocabulary detections, 3D-aware instance association/reactivation,
existence confidence, label confidence, stable object identity, spatial and
temporal graph edges, and a queryable 4D scene graph.

**What it already establishes:** Persistent object identity, semantic history,
appearance/disappearance/relocation, stale-content pruning, and language-facing
4D scene memory are not new concepts.

**Boundary found in the public protocol:** Its public demonstration is a
continuous two-hour deployment. The inspected public materials do not establish
a completed Session A exporting a dense scene belief that an independent Session
B imports before resuming full D1+D2 metric-semantic reconstruction. This is an
absence of an evaluated protocol, not a claim that its software could never be
extended to do so.

**Consequence:** The proposed method must go beyond open-vocabulary instance
association and confidence updates. It needs a precise process-boundary belief
and dense geometry update semantics.

### 3.4 ProbPer-LiLo — probabilistic multi-session object persistency

**Status:** IEEE RA-L 2026, published, DOI 10.1109/LRA.2026.3653311.

**Implemented capability verified from public primary metadata:** a discrete
probabilistic factor graph classifies object state; dynamic and quasi-static
objects are removed; static maps from multiple sessions are used for semantic
and geometric map refinement.

**Boundary:** The objective is preservation/refinement of stable localization
structure. The public material inspected does not indicate retention of D1
trajectories or a complete D1+D2 history.

**Consequence:** A factor graph for persistency, quasi-static classification, or
multi-session static-map refinement cannot be the sole novelty.

### 3.5 Panoptic Multi-TSDFs, POCD, and POV-SLAM — dense/object D3 foundations

- **Panoptic Multi-TSDFs:** active/inactive object volumes and
  persistent/absent/unobserved states; a later run starts from an earlier prior;
  short-term tracking is left for future work.
- **POCD:** object TSDFs and Gaussian--Beta stationarity/change beliefs between
  traversals; poses supplied externally; explicit dynamics left for future work.
- **POV-SLAM:** variational joint pose and semi-static object consistency over
  repeated visits.

**Consequence:** The state words `persistent`, `absent`, `unobserved`, object
stationarity, and object-level cross-session association are existing ideas.
The new method needs either a materially richer joint belief or a new way to
carry complete dynamic mapping through the session boundary.

### 3.6 DYNEMO-SLAM and Lost & Found — dynamic entities in scene graphs

**DYNEMO-SLAM status:** preprint as of 2026-08-07.

It stores entity IDs, semantic class, pose, uncertainty, point-cloud fragments,
and time-indexed entity poses in an optimizable hierarchical scene graph. It adds
keyframe--entity, intra-entity, entity--floor, and dynamic-aware loop-closure
constraints for moving agents and displaced objects.

**Lost & Found status:** IEEE RA-L 2025, published.

It observes human-object interactions, estimates the object's 6-DoF trajectory
during the interaction, and updates a transformable 3D scene graph. Prior
interaction history can later locate an object hidden in a drawer.

**Boundary:** These methods provide strong D1 object histories and scene-graph
updates. Their transitions are observed or handled inside one graph/run; they do
not establish the complete recursive dense D1+D2-over-D3 protocol targeted here.

### 3.7 Perpetua — existing multi-hypothesis persistence/emergence theory

**Status:** IROS 2025, published, DOI 10.1109/IROS60139.2025.11247086.

It considers semi-static features whose appearance/disappearance transitions are
not necessarily observed. The state is binary feature presence. It chains
mixtures of persistence and emergence filters, learns parameters online, tracks
multiple temporal hypotheses, handles reappearance, and predicts future feature
state under missing observations.

**Consequence:** A standard persistence filter, emergence filter,
multi-hypothesis survival model, or prediction under missing observations is not
new by itself. Perpetua is not a dense SLAM system and does not model geometry,
identity association, D1 trajectories, or session-map materialization, but it is
a mandatory theoretical baseline for any probabilistic existence model.

### 3.8 LT-Mapper and lifelong map/version-control systems

LT-Mapper, Lifelong 3D Mapping Framework, ELite, LLMF, RBIF, NDT lifelong SLAM,
and industrial lifelong-map systems already provide combinations of:

- multi-session alignment or pose-graph optimization;
- dynamic point removal;
- positive/negative change detection;
- current/base/delta maps;
- map version control and rollback;
- conservative ray/voxel updates;
- long-term coordinate consistency.

**Consequence:** Save/load, map differencing, version control, current-map
maintenance, and conservative union/deletion are engineering requirements, not
sufficient methodological novelty.

## 4. Existing method mechanisms by problem component

### D1: motion observed inside a session

Existing solutions include:

- semantic/geometric rejection of dynamic measurements;
- per-object surfel, TSDF, SDF, octree, Gaussian, or primitive maps;
- robot--object joint bundle adjustment or factor graphs;
- object pose/velocity/shape trajectories and temporal boxes;
- scene-graph entity factors and dynamic-aware loop closure;
- non-rigid canonical/deformation models;
- optical-flow/scene-flow-driven 4D Gaussians;
- motion extrapolation and forecasting through occlusion.

### D2: hidden transition in the same running session

Existing mechanisms include:

- local-motion versus global-jump association;
- fragment association and global reconciliation;
- ray presence/absence verification;
- visibility-aware detections and repeated non-detections;
- inactivity/reactivation and existence-confidence updates;
- persistent/absent/unobserved/new states;
- stale keyframe or contradicted-map removal;
- persistence/emergence filters and multi-hypothesis temporal models;
- same-object-moved versus disappearance/reappearance hypotheses.

### D3: completed-session continuation

Existing mechanisms include:

- multi-session loop closure, registration, and pose-graph alignment;
- prior-run/current-run submap comparison;
- local/global ephemerality and recursive point-map update;
- object stationarity/persistency factor graphs;
- positive/negative change and delta maps;
- map refinement, version control, and rollback;
- persistent semantic/object landmarks across deployments;
- cross-session object correspondence and unknown states;
- old-map/current-scan Gaussian revision.

### Cross-cutting latent variables already used in the literature

- existence/persistence;
- stationarity/ephemerality;
- observability/visibility;
- object identity and association;
- geometry/pose uncertainty;
- semantic-label confidence;
- motion-mode or change-category variables;
- temporal priors and periodicity;
- session alignment and provenance.

## 5. Claims and method directions that must be avoided

The following are not sufficient as the paper's primary method contribution:

1. **A three-label taxonomy.** The literature already separates short/long,
   local/global, moving/quasi-static/persistent, and appearance/disappearance.
2. **Checkpoint/save/load alone.** This proves software persistence, not a new
   scene inference model.
3. **Naive union, overwrite, nearest-neighbour deletion, or ray gating alone.**
   These are essential baselines and implementation components.
4. **A scalar Beta or ephemerality score alone.** POCD and ELite already use
   probabilistic scalar transiency/stationarity updates.
5. **A persistence filter or emergence filter alone.** Perpetua already provides
   mixtures, reappearance, adaptation, and prediction.
6. **An existence-confidence state machine alone.** SuperMap and LTC-Mapping
   already maintain confidence from detections/non-detections.
7. **Object association alone.** OASIS-Map, SuperMap, Living Scenes, DYNEMO, and
   many object-SLAM systems already address it.
8. **Dynamic masking or semantic promotion alone.** This is a supporting D1
   component, not the cross-session contribution.
9. **Current static-map maintenance or map version control alone.** LT-Mapper,
   ELite, Lifelong 3D Mapping, and production lifelong systems already do this.
10. **A representation swap to Gaussians, neural fields, or scene graphs.** A new
    representation without new persistent inference is unlikely to be enough.
11. **Pairwise A/B differencing only.** It does not show a recurring long-term
    system. The experiment must include B's own D1+D2 and preferably Session C.
12. **Combining Khronos with Panoptic/POCD as a pipeline.** A composition of
    existing mechanisms needs a new latent-state formulation, inference rule,
    or experimentally demonstrated capability.

## 6. Defensible method territory

### Core candidate: persistent sufficient scene belief

The most defensible direction is to define the minimum probabilistic state that
a completed dynamic-mapping session must export so that an independent future
session can resume complete D1+D2 inference.

For each object instance or structural surface patch `e`, the boundary memory
should not be a single hard label. A candidate state is

```text
B_e = {
  existence belief,
  observability / coverage belief,
  identity hypotheses,
  geometry or pose posterior,
  semantic belief,
  motion/change-mode belief,
  last-support and last-contradiction times,
  session provenance and supporting evidence
}
```

The important separation is:

```text
not observed != observed absent
identity uncertain != definitely new
not continuously tracked != static
current actionable map != complete historical memory
```

### Hierarchical inference across the two temporal levels

A candidate posterior for session `k` is

```text
p(X^k, T^k, A^k, C^k, M^k | M^{k-1}, Z^k, V^k)
```

where:

- `X^k`: robot states;
- `T^k`: D1 time-indexed dynamic tracks;
- `A^k`: identity/data-association hypotheses;
- `C^k`: existence, observability, and change-mode states;
- `M^k`: exported current scene belief;
- `Z^k`: sensor/semantic observations;
- `V^k`: visibility, ray, and coverage evidence.

It can be factorized conceptually into:

1. **D1 track factors:** observed motion, object pose/geometry, temporal support;
2. **D2 hidden-event factors:** a transition may occur inside the interval
   between last support and first contradictory/new observation;
3. **D3 session-bridge factors:** transform the previous exported belief into
   the initial prior of session `k`, accounting for session alignment, time gap,
   and unresolved hypotheses;
4. **materialization factors/rules:** convert the posterior into a current mesh,
   object layer, dynamic history, and diagnostics without deleting unobserved
   content.

The key novelty would be the bridge and state sufficiency, not rebuilding every
D1/D2 estimator from scratch.

### Preserve multiple identity explanations

For a chair absent at `a` and chair-like geometry new at `b`, the system should
retain at least two hypotheses until evidence resolves them:

```text
H1: same object moved a -> b
H2: old object absent at a + distinct new object at b
```

This differs from inventing a trajectory. It combines observability, identity,
and existence rather than collapsing them into one distance threshold.

### Objects and structural patches under one interface

Existing object-centric systems often cannot represent walls, construction
changes, or non-discrete geometry; point-level lifelong systems lack object
identity. A promising contribution is a common entity interface for objects and
structural patches, while allowing different motion and geometry models.

### Dual output: actionable present plus auditable history

Maintain both:

- a current actionable metric-semantic map for localization/planning;
- an append-only event/evidence/provenance history sufficient to explain and
  revisit past decisions.

This avoids the common choice between a clean static map and a rich dynamic
history.

## 7. Experimental requirements for the novelty claim

The method is not established by an A/B merge alone. A convincing protocol needs:

```text
Session A:
  at least one D1 event
  at least one D2 event
  export memory

Between A and B:
  real environmental interventions

Independent Session B:
  load A memory
  reconcile D3
  contain new D1 and D2 events
  export B memory

Preferably Session C:
  demonstrate recursive memory rather than pairwise differencing
```

Required evaluations:

- D1 trajectory/time-indexed geometry and dynamic-to-static leakage;
- D2 persistent/absent/unobserved/new state accuracy;
- D3 current-map geometry, stale-map removal, new-geometry recall, and
  unobserved-region preservation;
- identity-hypothesis accuracy or calibration;
- A-to-A idempotence and checkpoint equivalence controls;
- A->B->C memory growth, update cost, and error accumulation;
- ablations of observability, identity, existence, semantics, and session bridge.

Core baselines should include Khronos, Panoptic Multi-TSDFs, POCD/POV-SLAM where
compatible, ELite or an equivalent local/global ephemerality baseline, a
Perpetua-style existence filter, ProbPer-LiLo if code/data allow, and simple
union/overwrite/ray-only/hard-state baselines.

## 8. Safe novelty wording

Recommended:

> Existing work either retains rich dynamic histories within a continuously
> running session or maintains/refines maps across deployments. In the primary
> literature we audited, we did not find a dense metric-semantic system that
> exports the sufficient scene belief required for an independently initialized
> session to reconcile inter-session change and resume complete visible-motion
> and hidden-change inference.

Avoid:

> We are the first to model short-, long-, and cross-session dynamics.

Also avoid claiming the final novelty until the method contains more than the
current combination of hard state labels, ray-gated deletion, semantic masking,
and map welding.

## 9. Immediate research decision

Do **not** avoid existing directions merely because individual components exist.
Reuse Khronos D1+D2, ray evidence, object association, and persistence theory as
building blocks. Avoid presenting those blocks as new. Concentrate the research
contribution on:

1. the exported sufficient scene belief;
2. its probabilistic D1/D2/D3 factorization;
3. unresolved identity and observability handling;
4. unified object/structure memory;
5. recursive A->B->C evaluation.

That is the clearest territory not occupied by ELite's cleaned lifelong point
map, SuperMap's semantic 4D object memory, ProbPer-LiLo's stable-map refinement,
Perpetua's feature-existence prediction, or Khronos's continuous-session SMS.
