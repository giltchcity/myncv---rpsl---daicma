"""The final map of an occupancy run (its timeline at the last stamp, the scene surfels_final.ply is written from): the
background cells and the object cells as points.
  occ_points.py RUN_DIR SESSION OUT.npz"""
import sys

import numpy as np

sys.path.insert(0, "/home/jixian/Desktop/FT/runs/update_layer_game_T1_20261006/worktrees/wavemap_v4")
from update_layer.eval.scenelist import load_timeline  # noqa: E402

run, ses, out = sys.argv[1:4]
tl = load_timeline(f"{run}/session_{ses}/timeline.pkl")
scene = tl.scene(tl.stamps()[-1])
obj = [o.points for o in scene.objects if len(o.points)]
np.savez_compressed(out, background=np.asarray(scene.background, np.float32),
                    objects=np.concatenate(obj).astype(np.float32) if obj else np.zeros((0, 3), np.float32))
print(run.split("/")[-1], ses, len(scene.background), sum(len(o) for o in obj), len(obj), "objects")
