# Full-manuscript readability revision — 24 September 2026

## Scope and source

The manuscript was rewritten from commit `35605d90b77d75ee7ddf120b6bb91425ed54182f` on `codex/initial-paper-workspace`. The complete reading order is now abstract, introduction, related work, method, experiments, limitations, and conclusion. The working title is **Continuing Dense Dynamic Maps Across Deployments**.

This is an editorial revision of the reported method and results, not an implementation update or an experiment rerun. The historical section exports under `paper_sections_20260923/` remain unchanged. `manuscript/main.tex` is the canonical paper.

## Review provenance: do not call these three independent-agent reviews

Three full-paper self-review passes were performed by the writing assistant: (1) first-reader comprehension and hidden context, (2) source fidelity and claim-to-evidence consistency, and (3) the assembled reading proof and page layout. These are distinct editing passes, not three isolated models, and do not erase the assistant's conversation context.

An independent Firecrawl `spark-2` agent was actually invoked with only eight pinned manuscript URLs and a first-reader audit instruction. Job `01a0cf91-de72-77a0-91ec-bc7ae358b5f4` returned **zero sources read** because retrieval failed with `Unauthorized: Invalid token`, including its GitHub blob/contents fallbacks. Its empty output is not counted as a review. **Independent full-manuscript reviews completed: 0. Self-review passes completed: 3.**

## What changed for the reader

| Earlier wording or structure | Reader-facing replacement |
|---|---|
| An opening taxonomy of D1/D2/D3 | A returning robot, a moved chair, an occluded cabinet, and room surfaces not seen again |
| Repeated `process-separated D3 continuation` | An independently started deployment loads previous scene state and updates it with new observations |
| `Khronos-style D1 geometry` | Reconstructed object surfaces and the trajectory observed by the tracker |
| `session copy`, `candidate`, `hand-off` introduced together | Explain an imported old state, a separate new reconstruction, and the choice to refine or replace |
| `support`, `seen through`, `foreign` without a reader model | Depth agreement, a ray measured behind the expected surface, occlusion, and instance-label agreement are explained before state updates |
| `protocol v1` | An explicit represented-surface fraction and the 50% / 10 cm decision rule |
| `G1` and `G2` | Room-crop geometry and observed-region geometry, with their different reference coverage explained |
| `Ours, no memory` | `Ours, from scratch`: run the same method without importing previous-deployment state |
| Disappearances `come for free` | Absence from a rebuilt map can be scored as disappearance even without an explicit deletion decision |
| `ours 1.00 represented` | A represented-surface fraction with a referenced definition |
| Unexplained previous/current software versions | Removed from the result narrative and retained below as a traceability check |
| Dataset-by-dataset result inventory | Questions about retained coverage, obsolete states, an exact reference, and public-data failure cases |
| Broad claims that public-data ordering always agrees | Retain the non-rigid 3RScan failure and explain the scope of the three selected cases |

The new method notation distinguishes physical identity from geometric state, current output from recorded history, and object evidence accumulation from background mesh maintenance. No D1/D2/D3 aliases are required by the revised section text. A reader still needs ordinary computer-vision knowledge, but no project conversation should be needed to understand the stated task and pipeline.

## Three review passes and fixes

### Pass 1 — First-reader comprehension

Read all seven revised sections. Defined reconciliation at its first substantive use; made the saved state explicit; distinguished closing a current state from deleting its history; defined the sample count and nearest-surface distance next to the evaluation equation. Clarified that 30 reliable cells gates comparison of two reconstructed states, whereas an absence update can have one judged reliable cell. Replaced conversational explanations in related work with affirmative descriptions of DAAAM and LT-Mem. Flagged the exact statistical recursion and final closure semantics as missing specifications instead of supplying invented formulas.

### Pass 2 — Source fidelity

Compared the full rewrite against the pinned draft. Restored the declared B/C development split and the Bonn duration description. Corrected an accidental narrowing from scene geometry to background-only geometry. Kept the actual 5 cm sensor tolerance, 10 cm state-comparison tolerance, static-class exceptions, and imported-reliability assumption. Did not pretend that an uncertainty-derived threshold, automatic re-identification, probabilistic background fusion, or restart equivalence had been implemented. Removed an unsupported interpretation of the word `pending`. Withheld the incomplete observed-region gap from the quantitative argument because its comparator is unspecified, preserving the original value below.

### Pass 3 — Complete proof and page navigation

Read the assembled paper and inspected rendered pages. Checked that task, inputs, outputs, and measurement categories precede the details that use them. Checked all captions and method names against the text. Initial wide tables floated into the conclusion/references; their declarations were moved earlier and the final float barrier prevents spillover. The final standalone reading proof is eight pages, has resolved citations and cross-references, and has no detected overlapping content or overfull-box warnings. It is a reading proof using the same section text, **not a certified build of the retained official CVPR author kit**.

## Numerical preservation

The four source result tables were compared programmatically with the rewrite. All **152 numerical entries** and all missing-value markers match, with the same method/run associations. The checks cover 11 real-room rows, 4 cross-deployment rows, 6 synthetic rows, and 9 3RScan rows. Bold emphasis was removed and descriptive headers were introduced; measurements were not recomputed or corrected. P/R/F1 values remain the evaluator outputs, not newly calculated harmonic means of the rounded table entries.

This does not independently verify the experiments. The original draft's claim that results come from one code version is retained as a report of the experimental setup; that exact implementation/run manifest is still needed.

## Source gaps that prose cannot honestly resolve

The following items require implementation details or experiment records. They are not claimed to be solved by this editorial pass.

| Item | Exact unresolved question / needed evidence | Treatment in revised paper |
|---|---|---|
| Absence likelihood | Exact Beta fitting/shrinkage equations, treatment of f=0/1, one-sided score, cumulative-sum reset, fresh-coverage denominator, and model update timing | Preserve the described mechanism; no invented recursion or false 1% guarantee |
| End-of-deployment closure | Does `absence pending` mean a deferred confirmed decision or an unresolved hypothesis? What exact condition and time close it? | Describe a final update pass and flag its interaction with the absence detector |
| Positive support / spatial site | Which geometric and identity predicates constitute support and a distinct site in each branch? | Explain the sensor-versus-mesh distinction; keep exact implementation predicate as a required specification |
| Imported reliability | Are all imported cells marked reliable, or only an exported validated subset? | Retain the reported current assumption rather than claiming fresh validation |
| Background verifier | Exact depth tolerance, ray sources, temporal gating, and interaction with object-state closure | Distinguish it from the object detector; do not substitute the object's 5 cm threshold |
| Evaluator correction | What did `non-reviewed corrected` change? What averaging, sampling, and association code produced the online P/R/F1? | Call it a duration-weighted evaluator based on Khronos, state the 2 m gate, preserve all reported scores |
| Derived reference protocols | Exact 3RScan discriminative-surface selection, visibility computation, observed-domain mask, residue tolerance, and Bonn 3D mask-linking recipe | Explain their purpose; require code/configuration for exact reproduction |
| Run identity and data splits | The commit, full configuration, scene IDs, input-label provenance, and run manifests for the reported tables; corroboration of the declared B/C split | Preserve the manuscript's reported setup; no claim of independent rerun |
| Compression | Which archives and denominator support the reported approximately 30x ratio? What are absolute size, save/load time, and growth? | Retain the qualified reported factor; do not imply bounded growth or real-time transfer |
| Missing comparisons | No-memory hidden-change scores, complete observed-region results, component ablations, automatic identity, alignment perturbations, or continuous-versus-restart control | Keep missing entries and limitations; no fabricated results |

## Original inline claims withheld pending traceability

These values or assertions appeared outside the source tables and were not made into standalone evidence in the revised narrative:

- `visible-motion and mixed-visibility state scores are 100/85.7 and 100/100`: metric definitions and pairing are not specified.
- `both our previous and current versions lose 0.9 pp` with a 0.5 m gate: neither version is pinned and this is not a complete baseline comparison.
- A table turning in place ending at `18.7 s instead of 76.7 s`: the reference variant and event/decision time convention are not identified.
- Observed-domain geometry gap `2.6--3.3 pp`: the comparator and complete per-method scores are absent. It is not used to explain away the measured room-crop loss.
- `one code version`, deterministic event counts, and measured `0.1--0.2 pp` / `0.1 pp` variation: the variation is described as observed run-to-run spread, not a statistical confidence interval. Determinism requires a reproducibility record.

The retained real-room chair annotation discrepancy is still counted as a miss. The selected non-rigid 3RScan failure is still visible. No source-table number was deleted to hide a negative result.

## Build and scope

The original `cvpr.sty` and `.bst` files are unchanged. `main.tex` includes the new abstract, limitations, conclusion, and the primary-text DAAAM/LT-Mem bibliography additions. The supplemental `reading_copy.tex` is a separate standalone proof wrapper, not a replacement author kit. No official submission page-limit or target-year compliance claim is made. Before submission, verify the target template and resolve the factual specifications above from the matching implementation.
