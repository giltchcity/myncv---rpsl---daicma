"""Colored reference points of a simulated session for the geometry renders: the session's RGB-D frames back-projected
(every STEP-th frame, every 4th pixel) and averaged per 2 cm voxel; the real room has its reference meshes instead.
  colorref.py synthetic|flat SESSION STEP OUT.npz"""
import sys

import numpy as np

sys.path.insert(0, "/home/jixian/Desktop/FT/runs/update_layer_game_T1_20261006/worktrees/v4_snap")
from update_layer.frames import FlatSession, backproject, flat_session, synthetic_session  # noqa: E402

ds, ses, step, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
fs = FlatSession({"synthetic": synthetic_session, "flat": flat_session}[ds](ses))
V = 0.02
acc = {}
for i in range(0, len(fs.ids), step):
    f = fs.load(i, color=True)
    mask = np.zeros(f.depth.shape, bool); mask[::4, ::4] = True
    p, v, u = backproject(f, mask)
    key = np.floor(p / V).astype(np.int64)
    key, inv = np.unique(key, axis=0, return_inverse=True)
    inv = inv.reshape(-1)
    s = np.zeros((len(key), 4)); np.add.at(s, inv, np.c_[f.color[v, u] / 255.0, np.ones(len(u))])
    for k, row in zip(map(tuple, key), s):
        a = acc.get(k)
        acc[k] = row if a is None else a + row
    if i % (20 * step) == 0:
        print(i, len(fs.ids), len(acc), flush=True)
keys = np.array(list(acc.keys()), dtype=np.int64)
sums = np.array(list(acc.values()))
np.savez_compressed(out, points=((keys + 0.5) * V).astype(np.float32), colors=(sums[:, :3] / sums[:, 3:]).astype(np.float32))
print("points", len(keys))
