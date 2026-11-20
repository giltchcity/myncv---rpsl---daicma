# Rebuttal preparation: likely reviewer questions

Each question gets one sentence and one place in the paper. Add a row when a new question comes up.

| Question | Answer (ready to paste) | Where |
|---|---|---|
| Change confirmation is delayed | A change while the camera looks away cannot be known before its site is seen again; a state ends at the round that confirms it, the first time any method could know of it. Across BedRoom, Home and Flat, 51 of the 65 earlier states ended by the change test end in the round their site is first seen clearly; the other 14 take 12.9 s on average (at most 32.5 s). These count earlier states ended by the test, not the reference events of Tab. S2 (a move counts there as two events, and 11 further states end when the object is found elsewhere). | Supp. A; main Limitations; wt_takeover_runs/confirm_delay/confirm_delay.txt |
| Old Gaussians are trained by conflicting views before confirmation | A Gaussian of an earlier visit is updated by the current visit only once its evidence finds it unchanged. | Supp. Tab. S1 |
| What about 100 visits / storage | The stored history is measured: 244 rounds over three BedRoom visits take 8.4 MB (occupancy), 231 MB (TSDF) and 316 MB (3D Gaussians), in addition to the final map. | Supp. C, Map history |
| History is evaluated online, not queried afterwards | All held-out frames are rendered after the second visit, from the final 4D map queried at their capture time. | Supp. D, Rendering over time |
| Relies on ground-truth masks | With OneFormer masks, Flat keeps mesh F1 at 89.8 and PSNR at 27.56 dB (change F1 72.7); associating by geometry instead of identities gives 28.14 dB against 28.43 dB. | Main ablation table; Supp. Tab. S12 |
| Predicted masks on real data | With the same OneFormer masks on BedRoom (TSDF), ours stays above Khronos on all three scores (mesh/object/change F1 95.8/42.8/52.4 vs 87.7/26.9/48.8) with zero false changes; the misses come from the segmentation (OneFormer mIoU 38.1% on the 12 object classes). | Rebuttal only; run in wt_takeover_runs/bedroom_predicted_20261121 |
| Only an integration of existing parts | One decision drives all three map types; removing its effect on the geometry alone lowers change F1 from 83.3 to 68.8 and PSNR by 4.64 dB. | Main ablations |
| The 3.26 dB gain is over-attributed | Treating old keyframes as current costs 5.74 dB and dropping them costs 5.00 dB; GaME drops 194 of its 442 keyframes on Flat. | Main ablations; main 3DGS results |
| Only one real room | Eight real room chains of 3RScan, BedRoom over three visits, and two real Aria rooms. | Main experiments; Supp. B |
| Reproducibility | Repeated runs give identical TSDF and occupancy scores; Gaussian PSNR varies by about 0.1 dB, at most 0.2 dB. | Supp. C, Metrics |
| Eq. (2) diverges at a see-through fraction of 0 or 1 | Before scoring, the fraction is clipped to [max(0.005, m), 0.995], with m the mean of the model it is scored against. | Supp. A |
| No coverage weights: change F1 94.9 implies no false positive, yet two static objects are ended | A false positive is an unchanged object missing from the map at the end of a visit; an object ended by mistake and rebuilt within the visit lowers object F1 instead. | Supp. C, Metrics; Tab. S8 |
| History queries use later information, unlike snapshot baselines | Each held-out frame is rendered from the mapping round at or before its capture time, built only from the frames up to that time, as GaME's maps saved at the same times are. | Supp. D, Rendering over time |
| Motions in view are not in change F1 | On Home's three motions in view (six events), ours reaches change F1 90.9 against 66.7 for Khronos (TSDF); on Khronos's dynamic-object metric, 73.6 and 73.9 against 0.9 and 27.4. | Supp. D, Changes by kind |
| Not real time | Online here means frames are processed in order as they arrive, without access to later frames; the main paper's Limitations state that Gaussian maps are not yet real time. | Main runtime table; main Limitations |
| 28.12 vs 28.43 dB on Flat | The main rendering table uses SAM masks (28.12); Tab. S4 and the ablations use ground-truth instances (28.43). | Supp. Tab. S4 caption |
