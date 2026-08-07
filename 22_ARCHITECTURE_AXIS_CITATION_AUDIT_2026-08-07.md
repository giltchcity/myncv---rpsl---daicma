# Architecture-Axis Citation Audit

Status: **ACTIVE / bounded citation-chain continuation, 2026-08-07**

This file is the authoritative synthesis layer for the remaining literature
question. It does **not** replace the per-paper full-text audits in files `13`,
`16`, and `18`--`21`, and it does not change the verified count of 28.

## 1. Research story being tested

The paper is not claiming that individual mechanisms such as ray-based deletion,
object association, persistence beliefs, Gaussian map updates, scene graphs, or
relocalization are new.

The architecture-level question is whether a complete dynamic-mapping capability
survives an independent session boundary:

```text
Session A
  D1: observed dynamics with retained temporal history
  D2: hidden/out-of-view change reasoning while A remains active
  -> export persistent scene state
  -> Session A terminates

D3
  environment changes between deployments

Independent Session B
  -> import A state
  -> reconcile A-to-B changes
  -> again execute new D1
  -> again execute new D2
  -> export equivalent state for Session C

Session C
  -> repeat recursively
```

D3 is therefore an **interface between complete D1+D2 sessions**, not a third
change detector.

## 2. What does not count as solving the story

The following are relevant prior capabilities but do not by themselves complete
the target architecture:

- filtering moving objects to maintain a static localization map;
- updating an old map with added/removed geometry;
- pairwise A-versus-B change detection;
- reusing persistent object landmarks for localization;
- loading a previous static/current map without restoring D1 history;
- maintaining a dynamic map in one continuously running process;
- splitting a continuous sequence and restarting software at the cut;
- predicting persistence or recurrence without a complete mapping state;
- sharing one or more implementation mechanisms with our system.

## 3. Architecture checklist

Every candidate must be evaluated on the following axes:

| Axis | Required question |
|---|---|
| A/D1 | Does A retain observed motion as trajectory/time-indexed geometry or an equivalent explicit dynamic history? |
| A/D2 | Does A reason about changes revealed after an observation gap while the same session remains active? |
| Export | What exact scene/dynamic/evidence state survives termination of A? |
| Separation | Does A really terminate and B start independently? |
| D3 | Does B reconcile changes that occurred between sessions rather than simply start a fresh map? |
| B/D1 | After import, can B again model newly observed dynamics? |
| B/D2 | After import, can B again perform hidden-change reasoning within B? |
| Recursion | Can B export the same state contract for Session C? |

Representation density, object identity, structural geometry, semantic state,
and backend state are secondary columns used to determine how close a candidate
is; they are not substitutes for the eight architecture questions.

## 4. Current synthesis of the 28 verified primary texts

### Complete or near-complete intra-session side

**Khronos** is the primary dense D1+D2 seed. It combines short-term observed
motion handling with global reconciliation of changes separated by observation
gaps inside one continuously running spatio-temporal mapping problem. The
verified paper does not provide a process-separated scene-state continuation
protocol in which an independent B restores the complete D1+D2 capability.

**Changing-SLAM** provides a sparse object-level D1+D2 counterpart. It does not
establish process-separated recursive D3 continuation.

**DYNEMO-SLAM, Lost & Found, 4DGS-SLAM, 4DTAM, DynaGSLAM, and 4D
Primitive-Mache** provide rich continuous-sequence/entity D1 representations to
varying degrees, but the verified audits do not establish the full independent
A -> B -> C continuation contract.

### Cross-session/current-map side

**Panoptic Multi-TSDFs, POCD, POV-SLAM, ObVi-SLAM, OASIS-Map, and Living
Scenes** retain richer object/volumetric/cross-time state than static-map-only
methods. In the verified audits, none also preserves a complete D1 temporal
history and demonstrates that an independently initialized B resumes the same
full D1+D2 mapper.

**Dynamic Pose Graph SLAM, Pomerleau 2014, Efficient Long-Term Mapping,
LT-Mapper, RBIF, ELite, ProbPer-LiLo, and LT-Gaussian** establish substantial D3
map maintenance. Their persistent output is primarily a current/static/geometric
map or map-change state rather than a complete D1+D2 dynamic-scene state.

### Strong same-process D2/current-memory neighbours

**GaME, LTC-Mapping, SuperMap, and General Movable Objects** establish important
forms of out-of-view/current-memory/object maintenance. They do not, in the
verified audits, complete the process-separated recursive architecture.

## 5. Current bounded result

Within the **28 verified complete primary texts**, no method has been found that
implements the full chain:

```text
complete D1+D2 Session A
+ persistent export after A terminates
+ independent Session B import
+ D3 reconciliation
+ B resumes complete D1+D2
+ equivalent export for Session C
```

This is a corpus-bounded result, not a universal proof.

The remaining task is therefore not to re-label every mechanism as novel or
non-novel. It is to close the backward/forward citation chain around the methods
closest to either side of this architecture and test whether any uncatalogued
paper actually bridges the two.

## 6. Candidate-promotion rule

Promote a newly discovered paper to full-text audit only when there is plausible
evidence that it crosses the architecture boundary, for example:

- it has rich D1+D2 state **and** serializes/restores that state across sessions;
- it loads a prior cross-session map **and** B contains a genuine dynamic tracker
  and hidden-change process comparable to those in A;
- it explicitly defines recursive state transfer A -> B -> C;
- its experiment truly terminates A and starts B independently rather than using
  a continuous stream.

Do **not** promote a paper merely because it uses a mechanism also present in our
implementation.

## 7. Manuscript wording rule

Allowed before citation-chain closure:

> Within the verified corpus, we have not found a system that recursively carries
> a complete D1+D2 dynamic-mapping capability across an independent D3 session
> boundary.

Not allowed before closure:

- `we are the first`;
- `no prior work`;
- `no existing system`;
- any novelty argument based solely on component-level overlap or absence.

## 8. Relationship to the paper contribution

The final contribution still depends on the method actually delivering the
architecture above. The literature gap alone is not sufficient. The manuscript
must separately prove that the implementation exports enough persistent state,
reconciles D3 correctly, lets B execute new D1 and D2 events, and supports the
same handoff recursively.

The current implementation limitations in `AGENT_HANDOFF.md` and
`03_CLAIMS_AND_EVIDENCE.md` remain binding: map-level continuation must not be
misdescribed as restoration of Khronos's entire live backend unless that has
actually been implemented and validated.
