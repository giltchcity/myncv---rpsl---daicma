# Claims and Evidence Register

Date: 2026-08-06

Use this file to prevent evidence from one experiment or metric from being
silently reused for another claim.

## Evidence Levels

- **DIRECT**: read from the exact implementation output or a controlled
  comparison with fixed input.
- **PIPELINE**: proves execution/data flow, but not performance improvement.
- **QUALITATIVE**: visually supported; requires a quantitative metric before a
  paper performance claim.
- **DESIGN**: specified but not fully implemented or validated.
- **NOT PROVED**: explicitly unavailable under the current experiment.

## Claim Table

| Candidate claim | Level | Evidence | Allowed wording |
|---|---|---|---|
| Session B output begins from Session A global geometry | DIRECT | A-to-A idempotence and first-B-checkpoint counters in the July 30 run | “Base1 initializes reconciliation from the saved A global mesh.” |
| Unobserved inherited geometry is retained | DIRECT | Cross-session per-vertex states/counters | “The reconciler distinguishes unobserved from absent and retains unobserved prior geometry.” |
| Confirmed absent prior geometry can still be deleted | DIRECT | v5 B checkpoints delete 600-3403 ray-confirmed prior vertices | “Protection does not disable evidence-supported removal.” |
| Current B geometry repairs/adds missing coverage | DIRECT | v5 adds 170-14702 B vertices; welded topology retains more faces | “Current observations extend and reconnect retained prior geometry.” |
| Re-observation gating prevents object-near structural over-deletion | DIRECT for B03 | Old cleanup removed 2939 candidates; gated cleanup protected 2938 supported + 1 unobserved | “The gate prevents this measured object-proximity failure case.” |
| Semantic masking removes one human-shaped static residual | DIRECT controlled comparison | 138-vertex old-only component, 0.369 x 0.446 x 1.331 m | “Configured Human semantics prevent the identified residual from entering the static mesh.” |
| Semantic promotion extends the principal Human track | DIRECT controlled comparison | 114 -> 170 samples; endpoint 11.62 -> 14.52 s | “Semantic promotion extends the reliable tracked interval.” |
| Dynamic person remains tracked for all visible frames | NOT PROVED | Later intervals are mostly outside 5 m and one short interval fails allocation confidence | Do not claim. |
| Dynamic-residue distance cleanup improves the map | DISPROVED for tested setting | 119 candidates were protected floor; unsafe deletion reduced F1 | Report as a failure/ablation. |
| Current Base1 improves official Khronos final-current background F1 | NOT PROVED; historical test negative | Historical delta F1 was negative at 5/10/20/50 cm | Do not claim improvement yet. |
| Office reversed A/B has official comparable change P/R/F1 | NOT PROVED | Retimed B does not match stock GT query time | Describe as pipeline/qualitative A/B only. |
| Base1 performs native Khronos backend restart | NOT PROVED / false description | PGMO, active window, ray hash, and backend threads are not restored | Call it reconciliation-level continuation. |
| Structural patches support full persistent/absent/new updates | DESIGN | Unified model exists; full patch updater does not | Present as method extension/future implementation unless completed. |
| The merge produces a more accurate high-resolution surface | NOT PROVED | Current method welds/adds mesh topology; no TSDF reintegration metric | Say coverage/connectivity repair, not super-resolution. |

## Quantitative Facts Safe to Reuse

### Office A/B input gate

- A: 600 source images, 13 saved map times, 79 MB final map.
- B: 601 source images, 13 saved map times, 150 MB final map.
- Playback rate: 1. The earlier rate-5 A run is invalid.

### Unified cross-session continuation, earlier final run

- A prior global vertices: 36,594.
- B evidence vertices: 31,904.
- Prior states: 2,441 absent, 23,678 persistent, 10,475 unobserved.
- B surface inserted: 14,851 vertices.
- Final unified map: 49,467 vertices, 58,599 faces.
- Welded version: same vertices, 63,546 faces; boundary edges reduced from
  25,977 to 24,789.

### Latest v5 re-observation gate

At B checkpoint 3:

- prior A vertices: 39,610;
- prior ray-confirmed absent: 2,786;
- B vertices added: 1,981;
- old object cleanup removed: 2,939;
- gated cleanup removed: 0;
- gated protection: 2,938 current-supported + 1 unobserved;
- final gated global vertices: 38,817.

Across all 13 B checkpoints:

- prior ray-confirmed deletion remains 600-3,403 vertices;
- B additions range from 170 to 14,702 vertices;
- final checkpoint protects 6,524 current-supported and 181 unobserved object
  cleanup candidates.

### Historical official final-current evaluation

This result belongs to an older naive cleanup implementation:

| Threshold | Original F1 | Improved F1 | Delta |
|---|---:|---:|---:|
| 0.05 m | 0.661083 | 0.659948 | -0.001135 |
| 0.10 m | 0.868643 | 0.867127 | -0.001516 |
| 0.20 m | 0.929074 | 0.928610 | -0.000464 |
| 0.50 m | 0.974225 | 0.974177 | -0.000048 |

Do not attach these numbers to the latest v5 method; v5 requires its own valid
GT-aligned evaluation.

## Missing Evidence Before Submission

1. Valid GT-time-aligned A/B final-current evaluation.
2. Original Khronos vs naive union vs naive deletion vs complete method.
3. Structural-change quantitative test beyond object neighborhoods.
4. Repeated runs or deterministic input proof for any stochastic comparison.
5. Runtime and memory overhead of reconciliation.
6. A dataset/protocol that contains genuine process-separated changes rather
   than only the reversed Office demonstration.

