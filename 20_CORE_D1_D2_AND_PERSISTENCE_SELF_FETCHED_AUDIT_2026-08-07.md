# Self-Fetched Full-Text Audit: D1/D2 and Persistence Neighbours

Status checked: **2026-08-07**

This audit covers four independently acquired full PDFs. Each paper was read
through its problem definition, assumptions, representation, method, equations,
experiments, figures/tables, limitations, and conclusion.

Project taxonomy:

```text
D1 = observed motion retained as trajectory/time-indexed geometry
D2 = a hidden transition during an observation gap in the same running session
D3 = completed Session A transfers state to independent Session B
```

## 1. Changing-SLAM

**Paper:** *Visual Localization and Mapping in Dynamic and Changing
Environments*, Journal of Intelligent & Robotic Systems, 2023.

### Actual problem

Changing-SLAM is a real-time RGB-D visual SLAM system based on ORB-SLAM3. It
explicitly distinguishes:

- dynamic environments: objects moving in front of the camera;
- changing environments: objects moved, removed, replaced, or added after the
  region has already been mapped and while outside the camera field of view.

The experiments use continuous RGB-D sequences. The system does not define a
completed Session-A export and independent Session-B import.

### Representation and D1 mechanism

The geometric map remains an ORB-SLAM3 sparse MapPoint map. MapObjects group
MapPoints and store:

- semantic class and unique ID;
- current and initial bounding boxes;
- associated MapPoints;
- 3D centroid and dimensions;
- a persistence belief.

Short-term association uses same-class bounding-box IoU between consecutive
frames. An EKF tracks each object's 3D centroid and velocity. The object is
classified as moving through a class-dependent velocity threshold, and its
keypoints are filtered from camera tracking.

This is a D1 robustness/tracking mechanism, but the final scene representation
is not a dense time-indexed object history. The stated outputs are the camera
trajectory and a sparse outlier-cleaned metric-semantic map.

### D2 mechanism

A recursive binary Bayes filter estimates whether a MapObject remains at its
initialized location. The belief is reduced when the object is not detected
where it was previously observed. Long-term association compares same-class
object centroids with a distance threshold. Matched candidates are merged; low
belief makes their MapPoints inactive; new unmatched candidates create new
MapObjects.

The PUC-USP dataset consists of six continuous sequences: Static, OneChair,
Vanishing, Changing, Shift, and Replacing. Objects are moved, removed, replaced,
or added outside the field of view during the same recording. The main metric is
camera ATE and the principal demonstrated benefit is preventing tracking loss and
wrong loop closures.

### Limitations

The method does not handle deformable or articulation-changing objects and is
restricted to detector classes. Association is primarily same-class centroid
proximity; there is no dense structural reconciliation, explicit free-space
state, or persistent identity hypothesis across large displacement.

### Correct relationship

```text
D1: yes as online centroid/velocity tracking and feature filtering,
    but no dense retained trajectory/history output
D2: yes, sparse object-level within-session persistence/change reasoning
D3: no
```

Changing-SLAM is a genuine D1+D2 visual-SLAM predecessor at sparse object level.
It rules out a claim that nobody has combined visible motion and hidden
within-session object rearrangement. It does not solve process-separated dense
D3 continuation.

## 2. Detection and Tracking of General Movable Objects in Large 3D Maps

**Paper:** Nils Bore et al., IEEE Transactions on Robotics, 2019; arXiv full
manuscript 1712.08409.

### Actual task

The paper is an object detection and multi-target tracking system operating over
an existing large 3D map. The robot observes only one local region at a time;
objects may be moved while the robot is elsewhere. It focuses on semi-static
objects rather than continuously observed agents.

The tracker assumes a closed world:

- the initial object instances and positions are supplied;
- no object fully enters or leaves the environment;
- measurements contain 2D position and visual descriptor information;
- the robot's observation location is known.

It is not a SLAM system and does not maintain dense background geometry.

### Motion and association model

Each object has a continuous position/descriptor state and a discrete location.
The model separates:

- local Gaussian motion near the current location;
- rare global `jumps` to another location;
- measurement-to-object association;
- no-measurement states when the object is outside the current observed region
  or occluded.

A Rao--Blackwellized particle filter samples discrete jumps, locations, and
associations, while Kalman filters analytically update the continuous local
states. The method explicitly retains uncertainty over multiple visually similar
objects and unknown locations.

### Change detection and experiments

Forward and backward scene differencing detects objects that appear or disappear
between precisely registered depth observations; detections can be propagated
through nearby frames. Experiments use controlled object rearrangements,
simulation, and a robot deployment. Performance is evaluated with multi-object
tracking accuracy and sensitivity to object number, jump frequency, measurement
probability, and feature ambiguity.

The real deployment contains no observed motion between the spatial regions; it
mainly validates tracking stability under intermittent observations. Failures
occur when visually similar objects exchange locations or descriptors overlap.

### Correct relationship

```text
D1: not the focus; no continuous dynamic-geometry reconstruction
D2: yes, probabilistic object identity/location tracking across same-run
    observation gaps and global jumps
D3: no explicit process-separated session-memory protocol
```

This paper is a strong D2 identity-association theory neighbour. Local/global
motion, jump hypotheses, unknown locations, and Rao--Blackwellized association
are existing ideas. It does not produce a current dense metric-semantic map or
handle object birth/death and structural geometry.

## 3. Perpetua

**Paper:** *Perpetua: Multi-Hypothesis Persistence Modeling for Semi-Static
Environments*, accepted at IROS 2025.

### Actual task

Perpetua is not SLAM or mapping. It estimates and predicts the binary
presence/absence state of a feature under repeated, noisy, and potentially
missing observations. Transitions may occur while unobserved.

For a feature:

```text
X_t in {0,1} = present / absent
Y_t in {0,1} = noisy observation
```

The output is a continuous-time belief about current or future presence.
Geometry, identity association, object pose, scene reconstruction, and map
materialization are outside scope.

### Method

Perpetua addresses limitations of a single Bayesian persistence filter:

- only one temporal hypothesis;
- disappearance treated as permanent;
- fixed prior parameters.

It introduces:

- mixtures of persistence filters for disappearance dynamics;
- mixtures of emergence filters for reappearance dynamics;
- a state machine switching between persistence and emergence;
- EM learning of mixture parameters from noisy observations;
- AIC selection of mixture complexity;
- prediction at arbitrary future times.

### Experiments and limitations

The method is evaluated in a simulated room and on parking-space occupancy data
captured every five minutes for more than 30 days. Metrics are persistence-belief
MAE, balanced accuracy, and F1, with tests for future prediction and observation
sparsity. Data association is not explicitly addressed; the authors state that
its errors can only be absorbed through the false-positive/false-negative
observation model. Newly observed features may initially have unidentifiable
parameters.

### Correct relationship

```text
D1: no
D2: provides existence theory applicable to unobserved transitions
D3: not a session/map system; temporal observations may span arbitrary time
```

Perpetua prevents claiming multi-hypothesis persistence/emergence, reappearance,
or learned survival priors as a standalone novelty. It is a theoretical
component, not a solution to dense dynamic scene memory.

## 4. Lost & Found

**Paper:** *Lost & Found: Tracking Changes from Egocentric Observations in 3D
Dynamic Scene Graphs*, IEEE RA-L 2025.

### Actual task and inputs

Lost & Found begins with a prior static point-cloud reconstruction segmented into
object and drawer nodes. It processes egocentric Aria-glasses recordings with:

- known device/camera poses;
- 3D hand positions;
- RGB observations;
- hand-object interaction predictions;
- an initial aligned scene graph.

It detects observed pick-and-place interaction intervals and estimates the
object's 6-DoF pose throughout the interaction.

### Method and scene graph

The scene graph stores object geometry, centroids, and relations such as
`close-to`, `part-of`, and `contains`. During an interaction:

- interaction start/end are inferred from hand-object detections, distances,
  hand velocities, a look-ahead window, and thresholds;
- projected 3D object points are tracked in 2D;
- PnP estimates orientation from 2D--3D correspondences;
- 3D hand motion and a fixed grasp offset estimate translation;
- object nodes and graph relations are updated online.

The output is a real trajectory for an observed interaction and an updated
transformable scene graph. Applications include teach-and-repeat and retrieving
an object previously placed inside a closed drawer.

### Experiments and limitations

The method compares full trajectories and final poses against BundleTrack,
BundleSDF, FoundationPose, and head-pose baselines. It improves translation and
orientation errors in the recorded pick-and-place dataset.

The paper explicitly states:

- the object must remain in the egocentric camera field of view;
- severe deformation and tracking loss are problematic;
- experiments only cover changes occurring within the egocentric observations;
- re-scan-based updates and long-term scene-graph consistency are future work;
- uncertainty over object motion is not modeled.

### Correct relationship

```text
D1: yes, observed human-object interaction trajectory and graph update
D2: no; object must remain observed
D3: no
```

Lost & Found is a strong D1 scene-graph update reference, not a hidden-change or
cross-session system. It shows that observed object trajectories and relational
scene-graph edits are existing mechanisms.

## 5. Cross-paper implications

| Paper | Main representation | D1 | D2 | D3 | Primary output |
|---|---|---:|---:|---:|---|
| Changing-SLAM | sparse ORB MapPoints + MapObjects | partial/yes | yes | no | robust camera trajectory + sparse semantic map |
| General Movable Objects | probabilistic object tracker over fixed 3D map | no | yes | no | object identity/location posteriors |
| Perpetua | feature presence belief | no | theory component | no map protocol | current/future persistence probability |
| Lost & Found | transformable object scene graph | yes | no | no | observed 6-DoF interaction trajectory + graph update |
| Project target | dense metric-semantic current map + dynamic history | yes | yes | yes | recursive complete scene memory |

The closest established single-session combination is now clearly
Changing-SLAM at sparse object-map level and Khronos at dense
spatio-temporal metric-semantic level. The cross-session gap must therefore be
stated as continuation of a complete D1+D2 scene state, not as the first
combination of visible and hidden dynamics.
