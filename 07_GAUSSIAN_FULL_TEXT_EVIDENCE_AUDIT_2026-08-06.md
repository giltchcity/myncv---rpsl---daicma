# Gaussian Dynamic and Long-Term Mapping: Full-Text Evidence Audit

Status checked: **2026-08-06**

This is an internal author document supporting the Gaussian subsection in
`manuscript/sec/2_related_work.tex`. The audit distinguishes three different uses
of the word `dynamic`:

- **GS-static/robust:** dynamic observations are suppressed to recover a static
  Gaussian map;
- **GS-D1/4D:** motion observed in a continuous sequence is represented with
  time-dependent Gaussians;
- **GS-D2/D3/evolving:** an old Gaussian representation is revised after an
  out-of-view or cross-visit scene change.

These categories must not be merged. Removing a moving person is not the same as
preserving the person's trajectory, and updating two completed Gaussian maps is
not a complete multi-session dynamic SLAM system.

Short excerpts below are accompanied by the original section and PDF page. The
manuscript uses paraphrases rather than relying on isolated abstract wording.

---

## 1. Gaussian Splatting SLAM

**Citation:** Matsuki et al., CVPR 2024.  
**Status:** Published.  
**Full text:** arXiv:2312.06741 / CVF Open Access.  
**Audited:** problem statement, tracking, mapping, experiments, limitations.

**Original evidence:**
> “utilises Gaussians as the only 3D representation”

**Location:** Abstract, PDF p. 1.

**Implemented capability:** Online monocular SLAM that directly optimizes camera
poses and one explicit Gaussian map. The scene is treated as static.

**Allowed conclusion:** A foundational Gaussian SLAM system establishing the
static-map tracking/mapping formulation used by later dynamic extensions.

**Do not write:** That it models moving-object trajectories, out-of-view changes,
or cross-session memory.

**Coverage:** GS-static; D1 no; D2 no; D3 no.

---

## 2. SplaTAM

**Citation:** Keetha et al., CVPR 2024.  
**Status:** Published.  
**Full text:** arXiv:2312.02126 / CVF Open Access.  
**Audited:** representation, silhouette-based tracking/mapping, map expansion,
experiments, limitations.

**Original evidence:**
> “3D Gaussians to enable high-fidelity reconstruction from a single unposed RGB-D camera”

**Location:** Abstract, PDF p. 1.

**Implemented capability:** Dense online RGB-D tracking and Gaussian-map
expansion. It does not introduce a dynamic-scene state model.

**Allowed conclusion:** A static Gaussian SLAM foundation.

**Coverage:** GS-static; D1 no; D2 no; D3 no.

---

## 3. WildGS-SLAM

**Citation:** Zheng et al., CVPR 2025.  
**Status:** Published.  
**Full text:** arXiv:2504.03886 / CVF Open Access.  
**Audited:** system overview, uncertainty module, tracking/mapping losses,
datasets, failure cases.

**Original evidence:**
> “building a 3D Gaussian map ... of the static scene”

**Location:** Fig. 2 description, Sec. 3 overview.

**What it does:** A DINOv2-conditioned uncertainty MLP downweights dynamic
regions in dense bundle adjustment and Gaussian-map optimization.

**Important limitation from the paper:** Its failure analysis reports that a
person can remain in the map when no clean observation of the static background
is available.

**Allowed conclusion:** Strong dynamic-input robustness, but an
**anti-dynamic/static-map** method. It removes or downweights dynamic distractors
instead of retaining their trajectories or temporal geometry.

**Coverage:** Robust current-session tracking; D1 history no; D2 no; D3 no.

---

## 4. Gassidy

**Citation:** Wen et al., ICRA 2025.  
**Status:** Published.  
**Full text:** arXiv:2411.15476.  
**Audited:** Sec. III system, rendering-loss-flow classifier, keyframe mapping,
TUM/Bonn experiments, conclusion.

**Original evidence:**
> “resulting in a cleanly constructed scene without dynamic object disturbances”

**Location:** Sec. III-A, system overview.

**What it does:** Instance masks separate object and background Gaussians;
photometric-geometric loss flows and a Gaussian mixture model identify dynamic
objects. Dynamic Gaussians are pruned from optimization, while later keyframes
can reconstruct uncovered static regions.

**Allowed conclusion:** A published Gaussian dense-SLAM method for filtering
unpredictable dynamic disturbances and improving camera tracking/static-map
rendering.

**Do not write:** That it reconstructs or stores the motion of the pruned objects.
Its map-quality metrics are PSNR/SSIM/LPIPS, not dynamic-history accuracy.

**Coverage:** GS-static/robust; D1 history no; D2 no; D3 no.

---

## 5. 4D Gaussian Splatting SLAM

**Citation:** Li et al., ICCV 2025.  
**Status:** Published.  
**Full text:** arXiv:2503.16710 / CVF Open Access.  
**Audited:** static/dynamic decomposition, deformation representation, optical
flow supervision, tracking/mapping, experiments and conclusion.

**Original evidence:**
> “Instead of removing dynamic objects as distractors”

**Location:** Abstract, PDF p. 1.

**What it does:** Splits primitives into static and dynamic sets, uses sparse
control points and an MLP deformation field for dynamic Gaussians, and supervises
motion using reconstructed optical flow between neighboring frames.

**Allowed conclusion:** A strong GS-D1 method that jointly tracks the camera and
constructs a 4D radiance field from a continuous RGB-D sequence.

**Do not write:** That it infers an abrupt rearrangement with no observed
intermediate motion, or that it imports a completed map into a new session.

**Coverage:** D1 yes; D2 no; D3 no.

---

## 6. D4DGS-SLAM

**Citation:** Sun, Lo and Hu, IROS 2025.  
**Status:** Published.  
**Full text:** arXiv:2504.04844.  
**Audited:** 4D Gaussian representation, LEAP-based InfoModule, tracking,
mapping, evaluation and conclusion.

**Original evidence:**
> “visibility, dynamic status, and reliability of visibility”

**Location:** Sec. III-B, PDF p. 3.

**What it does:** Represents the current dynamic scene using 4D Gaussians. LEAP
predicts per-point trajectories, visibility, dynamic labels and reliability
across a consecutive image sequence; stable static points support camera
tracking, while dynamic information affects Gaussian regularization.

**Allowed conclusion:** A GS-D1 SLAM system with an explicit spatio-temporal map
and continuous-sequence visibility estimates.

**Boundary:** Its `long-term point tracking` means tracking across frames in the
current sequence, not persistent scene memory across completed robot sessions.

**Coverage:** D1 yes; D2 no; D3 no.

---

## 7. DynaGSLAM

**Citation:** Li et al., WACV 2026.  
**Status:** Published.  
**Full text:** arXiv:2503.11979 / CVF Open Access.  
**Audited:** task decomposition, prerequisites, dynamic Gaussian flow,
addition/deletion management, motion forecasting and experiments.

**Original evidence:**
> “use its estimated camera poses without modification”

**Location:** Sec. 5 prerequisites, referring to DynoSAM localization.

**What it does:** Uses optical flow, motion segmentation and DynoSAM camera
poses, then separately manages static and dynamic Gaussians and predicts their
motion. Existing dynamic Gaussians must satisfy current observability and
longevity gates; otherwise they are deleted.

**Allowed conclusion:** An online photorealistic GS-D1 mapping system for
observed moving objects.

**Important boundary:** Despite the title's use of SLAM, the released method
separates localization and mapping and adopts DynoSAM poses unchanged. Its
`unobserved dynamic Gaussian` deletion is not the conservative persistent
`unobserved` state required by this project.

**Coverage:** D1 yes; D2 no; D3 no.

---

## 8. Flow4DGS-SLAM

**Citation:** Wang and Lee, CVPR 2026.  
**Status:** Published.  
**Full text:** arXiv:2604.22339 / CVF Open Access.  
**Audited:** ego-motion flow decomposition, hybrid 4D representation, temporal
center propagation, opacity/rotation model, tracking and experiments.

**Original evidence:**
> “We separate the 3D Gaussians into static and dynamic”

**Location:** Sec. 3.2, PDF p. 4.

**What it does:** Builds a motion mask by fitting camera ego-motion to optical
flow, represents dynamic Gaussians with explicit keyframe centers propagated by
3D scene flow, and models temporal opacity and rotation with Gaussian mixtures.
Camera tracking uses the static Gaussian rendering.

**Allowed conclusion:** A recent high-performance GS-D1 method for continuous
observed motion and dynamic reconstruction.

**Coverage:** D1 yes; D2 no; D3 no.

---

## 9. RU4D-SLAM

**Citation:** Zhao et al., CVPR Findings 2026.  
**Status:** Published in CVPR Findings.  
**Full text:** arXiv:2602.20807 / CVF Open Access.  
**Audited:** uncertainty model, semantic reweighting, adaptive opacity/deformation,
experiments, conclusion and limitations.

**Original evidence:**
> “introduces temporal factors into spatial 3D representation”

**Location:** Abstract, PDF p. 1.

**What it does:** Extends uncertainty-aware tracking to motion blur and dynamic
regions and uses the uncertainty to initialize and guide time-varying Gaussian
opacity/deformation.

**Important limitation from the paper:** The conclusion states that achieving
real-time performance remains future work.

**Allowed conclusion:** A robust 4D Gaussian reconstruction/SLAM method for
observed dynamics and degraded imagery, not a long-term scene-memory system.

**Coverage:** D1 yes; D2 no; D3 no.

---

## 10. Gaussian Mapping for Evolving Scenes (GaME)

**Citation:** Yugay et al., CVPR 2026.  
**Status:** Published.  
**Full text:** arXiv:2506.06909 / CVF Open Access.  
**Audited:** problem definition, dynamic scene adaptation, keyframe management,
input assumptions, synthetic/real experiments, limitations.

**Original evidence:**
> “the scene evolving through changes out of view”

**Location:** Abstract, PDF p. 1.

**What it does:** Detects contradictions between new observations and an online
Gaussian representation, adds new Gaussians, removes old geometry, and masks or
removes stale keyframe observations.

**Boundary:** The method receives camera poses and panoptic segmentation from
external systems. It focuses on out-of-view evolving-scene reconstruction, not
visible moving-object trajectories. The paper does not define a completed
Session-A memory package imported by an independent Session B.

**Allowed conclusion:** The closest published Gaussian D2 method and a major
dense evolving-map baseline.

**Coverage:** D2 yes; D1 no; D3 process-separated continuation not established.

---

## 11. LT-Gaussian

**Citation:** Cheng et al., IEEE IV 2025.  
**Status:** Published.  
**Full text:** arXiv:2508.01704 / IEEE IV paper.  
**Audited:** multimodal map construction, map alignment, structural change
detection, update module, nuScenes revisit benchmark and conclusion.

**Original evidence:**
> “emerging and disappearing points are selected ... [with] ICP-based registration and kNN-based search”

**Location:** Fig. 3 caption and Sec. III-B, PDF p. 4.

**What it does:** Aligns an old Gaussian map to current LiDAR using ICP, labels
new LiDAR points and unmatched old Gaussian positions through kNN thresholds,
removes disappearing primitives, and optimizes an updated rendering map using
the old map as a prior.

**Allowed conclusion:** A published D3-style Gaussian-map update method with a
large nuScenes revisit benchmark.

**Do not write:** That it jointly estimates visible dynamic-object trajectories,
that it distinguishes `unobserved` from `absent`, or that it is a full
metric-semantic dynamic SLAM system. Its evaluation is primarily rendering
quality and update time.

**Coverage:** D3 map update yes; D1 no; D2 no explicit state model.

---

## 12. GS-LTS

**Citation:** Fu et al., arXiv:2503.17733.  
**Status:** **Preprint; not peer reviewed as of 2026-08-06.**  
**Full text:** arXiv PDF.  
**Audited:** system/task formulation, semantic Gaussian engine, single-view
change detection, active update policy, benchmark, limitations.

**Original evidence:**
> “focuses on medium-term changes, not real-time dynamics”

**Location:** Limitations, PDF p. 8.

**What it does:** Compares a current egocentric RGB-D observation against a
rendered semantic Gaussian reference, classifies addition/removal/relocation,
uses a rule-based policy to collect multi-view observations, and edits/fine-tunes
the affected Gaussian region.

**Allowed conclusion:** A highly relevant concurrent D3/evolving-map preprint
for long-term service robots.

**Important boundary:** It explicitly excludes moving objects and human
interactions, receives current poses, focuses on small/medium-term object changes,
and is not a complete dynamic SLAM system.

**Coverage:** D3/evolving update; D1 no; D2 not a running D1+D2 SLAM formulation.

---

## 13. GS-DIFF

**Citation:** Galappaththige et al., arXiv:2605.07203.  
**Status:** **Preprint; not peer reviewed as of 2026-08-06.**  
**Full text:** arXiv PDF.  
**Audited:** task setting, primitive drift, observability, structural/appearance
scores, PASLCD experiments and conclusion.

**Original evidence:**
> “comparing two independently reconstructed 3DGS scenes directly in primitive space”

**Location:** Introduction, PDF p. 2.

**What it does:** Compares two completed Gaussian reconstructions, models
geometric and photometric reconstruction drift, and weights primitive-space
comparison using Fisher-information observability. It distinguishes structural
from appearance-only changes.

**Allowed conclusion:** A mathematically relevant Gaussian change detector,
especially for primitive observability and representation non-uniqueness.

**Do not write:** That it performs SLAM, updates the map, preserves scene memory,
or tracks moving objects. Its output is a change mask/score between two
reconstructions.

**Coverage:** D3 change detection only; D1 no; D2 no; map update no.

---

## Resulting Gaussian landscape

| Gaussian family | Representative methods | What is preserved | D1 | D2 | D3 |
|---|---|---|---:|---:|---:|
| Static-map robust GS-SLAM | WildGS-SLAM, Gassidy | static Gaussian map | no history | no | no |
| 4D Gaussian SLAM | 4DGS-SLAM, D4DGS-SLAM, DynaGSLAM, Flow4DGS-SLAM, RU4D-SLAM | observed temporal Gaussian motion | yes | no | no |
| Evolving Gaussian maps | GaME | latest online Gaussian state | no | yes | not process-separated |
| Long-term Gaussian update | LT-Gaussian, GS-LTS | revised old map | no | partial | yes |
| Gaussian change detection | GS-DIFF | change scores between maps | no | no | detection only |

The literature therefore contains strong Gaussian realizations of each side of
the project, but no audited method currently carries a complete D1+D2 dynamic
mapping process through a persistent D3 session boundary and restarts the same
process in the next session.

## Preprint watchlist not yet used for manuscript claims

The following recent works were located but are not cited until their full text,
status and overlap are audited to the same standard:

- D2GSLAM: 4D Dynamic Gaussian Splatting SLAM, arXiv:2512.09411;
- Dy3DGS-SLAM, arXiv:2506.05965;
- ADD-SLAM, arXiv:2505.19420;
- GLAM-SLAM, arXiv:2607.21416 (large-scale but principally static);
- GS-DIFF status should be checked again because its PDF states that code and
  annotations will be released upon acceptance.
