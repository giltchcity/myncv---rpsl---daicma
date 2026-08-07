# Priority Full-Text Audit Queue

Status: **2026-08-07**

Priority is based on overlap with the canonical **session architecture**, not on
whether a paper contains an individual mechanism that we also use.

## Verified corpus: 35 complete primary texts

The original fixed direct-core queue is complete, and seven additional bridge
candidates have now been fully re-audited under the architecture checklist. The
authoritative verified total is therefore **35 complete primary texts**, with
details in `17_VERIFIED_PDF_AUDIT_TRACKER_2026-08-07.md`.

The seven promoted/re-audited neighbours are:

- CubifyGS;
- DynaMem;
- CogniMap3D;
- DovSG;
- DynamicGSG;
- DGSG-Mind;
- DREAM.

Their complete architecture-axis audit is recorded in
`23_SEVEN_NEIGHBOURS_ARCHITECTURE_REAUDIT_2026-08-07.md`.

The completed corpus covers, among other things:

- complete or partial single-session D1+D2 systems;
- rich continuous D1 representations;
- object-level and dense D2/current-map maintenance;
- D3 static/geometric map maintenance;
- D3 object/volumetric state transfer and change reasoning;
- multi-visit static-scene memory retrieval and update;
- prior-Gaussian-map relocalization and later object-level revision;
- persistence and temporal-belief models.

These categories describe **capability coverage**, not novelty claims.

## The only remaining literature question

The remaining citation-chain work asks one architecture-level question:

> Does any uncatalogued system run a complete D1+D2 dynamic-mapping Session A,
> preserve sufficient scene state after A terminates, initialize an independent
> Session B from that state, reconcile D3, let B again run the complete D1+D2
> mapping process, and export the same kind of state recursively for Session C?

The target chain is:

```text
Session A
  complete D1 + D2
  -> export persistent dynamic scene state
  -> A terminates

D3 boundary
  environment may change while the robot/process is absent

Independent Session B
  -> import A state
  -> reconcile A-to-B changes
  -> run new D1 + D2 events
  -> export B state

Session C
  -> repeat
```

A paper is a direct architectural threat only if it crosses the boundary between
**rich intra-session dynamic mapping** and **persistent cross-session
continuation**. Sharing ray deletion, object matching, Gaussian updates,
persistence beliefs, scene graphs, or relocalization is not by itself evidence
that the paper solves this recurring architecture.

## Mandatory architecture checklist for every new candidate

For each candidate, answer these questions from the complete primary text:

1. **A/D1:** Does Session A retain observed object/entity motion as trajectory,
   temporal geometry, or an equivalent explicit D1 history rather than merely
   filtering dynamics?
2. **A/D2:** While A remains active, does it reason about changes revealed after
   an observation gap rather than only frame-to-frame motion?
3. **Export:** What exact state survives the end of A? Static map only, object
   priors, current geometry, dynamic histories, observability/evidence state,
   backend state, or something else?
4. **Process separation:** Does A actually terminate and B start independently,
   or is the experiment one continuous process/sequence with a temporal split?
5. **D3:** How are changes between A and B reconciled, including the distinction
   between absence and lack of observation where applicable?
6. **B/D1:** After loading A, can B again represent newly observed motion as D1?
7. **B/D2:** After loading A, can B again perform the same hidden-change D2
   reasoning within B?
8. **Recursion:** Does B export the same state contract for C, or is the method
   only pairwise A-versus-B comparison/update?

Record the representation density and whether both objects and structural
geometry are retained, but do not confuse those details with the architecture
question above.

## Priority seeds for remaining backward/forward chaining

1. **Khronos and Changing-SLAM:** strongest verified single-session D1+D2 seeds.
2. **Panoptic Multi-TSDFs, POCD, POV-SLAM, OASIS-Map, and ObVi-SLAM:** strongest
   verified cross-session object/volumetric-state seeds.
3. **CogniMap3D and DGSG-Mind:** strongest newly verified bridge-side seeds;
   CogniMap3D has genuine multi-visit static memory, while DGSG-Mind has
   prior-Gaussian-map relocalization and later dynamic revision without
   continuous online SLAM but lacks integrated tracking.
4. **Dynamic Pose Graph SLAM, LT-Mapper, ELite, ProbPer-LiLo, RBIF, and
   LT-Gaussian:** recursive/current-map D3 seeds.
5. **DYNEMO-SLAM and the verified continuous 4D methods:** rich D1/state-history
   seeds.
6. **GaME, SuperMap, DynaMem, DovSG, DynamicGSG, CubifyGS, and DREAM:** strong
   same-process/current-memory neighbours that may expose forward citations to a
   genuine bridge.

A newly discovered paper is promoted to a full audit when its title/abstract and
available method description make it plausible that it bridges **both sides** of
the architecture. Do not promote papers merely to increase the corpus size.

## Stop rule

The architecture search is sufficiently saturated for submission positioning
only when:

1. backward references of all closest seeds have been screened;
2. forward/citing-paper searches have been performed with at least two
   independent query formulations;
3. every plausible bridge paper has been checked from the complete primary text
   using the eight-question checklist above;
4. no surviving paper completes the A -> D3 -> B -> C chain;
5. every manuscript positioning sentence is consistent with the resulting
   architecture matrix; and
6. publication status is refreshed immediately before submission.

Until then, the allowed conclusion is bounded:

> Within the verified corpus, no system has been found that recursively carries
> a complete D1+D2 dynamic-mapping capability across an independent D3 session
> boundary.

Do not turn this into an absolute `first ever` or universal-negative statement.

## Reading rule

A title or abstract may screen a candidate, but it never determines coverage.
For any promoted paper, the complete primary text must be checked for:

- temporal/session protocol;
- inputs and supplied poses/labels;
- state variables and map representation;
- retained versus discarded dynamic history;
- export/import state across process boundaries;
- update equations and change evidence;
- experiments and whether B is truly independent;
- limitations and future-work boundaries.
