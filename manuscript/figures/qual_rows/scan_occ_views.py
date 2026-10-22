"""Held-out views where wavemap's occupancy map visibly departs from the image and ours does not (fig:qualitative). Each
map's 2 cm cells are cast once into a ray-casting scene; every STEP-th held-out frame is cast at every 4th pixel and
compared with its measured depth (pixels away from depth discontinuities): a pixel is wrong for a map when the map shows
no surface there or one more than 15 cm off. Score: the largest connected region wrong for wavemap and right for ours.
  scan_occ_views.py real|synthetic STEP [SESSION]        prints the best frames (SESSION b of the real room: its frames,
                                                         every STEP-th, against the maps at the end of that visit)"""
import json
import sys

import numpy as np
from scipy import ndimage

src = open("/home/jixian/Desktop/FT/CVPR/manuscript/figures/testview/render_views.py").read()
exec(src.split("\nscene = sys.argv[1]")[0])           # GEO, DATA, cubes(), rt
sys.path.insert(0, "/home/jixian/Desktop/FT/runs/update_layer_game_T1_20261006/worktrees/v4_snap")
from update_layer.frames import FlatSession, real_session, synthetic_session  # noqa: E402

ds, step = sys.argv[1], int(sys.argv[2])
key = {"real": "real", "synthetic": "sim"}[ds]
ses = sys.argv[3] if len(sys.argv) > 3 else {"real": "c", "synthetic": "b"}[ds]
if ds == "real" and ses == "b":                               # the maps at the end of the second visit
    GEO["real"]["occ_wavemap"] = (f"{DATA}/occ/realb_row3.npz", 0.02, 0.02)
    GEO["real"]["occ_ours"] = (f"{DATA}/occ/realb_row4.npz", 0.02, 0.02)
run = {"real": "verify_real_5fa93c0", "synthetic": "syn_u29_aed974e"}[ds]
fs = FlatSession({"real": real_session, "synthetic": synthetic_session}[ds](ses))
rj = f"/home/jixian/Desktop/FT/runs/update_layer_game_T1_20261006/{run}/session_{ses}/run.json"
import os
if os.path.exists(rj) and (json.load(open(rj)).get("g8_holdout") or {}).get("stamps"):
    held = set(int(x) for x in json.load(open(rj))["g8_holdout"]["stamps"])
    frames = [i for i in range(len(fs.ids)) if fs.stamp_ns(i) in held][::step]
else:
    frames = list(range(0, len(fs.ids), 10))[::step]


def scene_of_occ(item):
    path, vb, vo = GEO[key][item]
    d = np.load(path)
    parts = [cubes(d["background"], vb)] + ([cubes(d["objects"], vo)] if len(d["objects"]) else [])
    V = np.concatenate([p[0] for p in parts]); off = np.cumsum([0] + [len(p[0]) for p in parts[:-1]])
    F = np.concatenate([p[1] + o for p, o in zip(parts, off)])
    return rt.scene_of(V, F)


scenes = {k: scene_of_occ(k) for k in ("occ_wavemap", "occ_ours")}
K = fs.K
res = []
for i in frames:
    f = fs.load(i)
    dep = f.depth[::4, ::4]
    h, w = dep.shape
    uu, vv = np.meshgrid(np.arange(w) * 4 + K.offset, np.arange(h) * 4 + K.offset)
    dc = np.stack([(uu - K.cx) / K.fx, (vv - K.cy) / K.fy, np.ones_like(uu, dtype=float)], -1).reshape(-1, 3)
    Rw, o = f.T_world_cam[:3, :3], f.T_world_cam[:3, 3]
    dw = dc @ Rw.T; n = np.linalg.norm(dw, axis=1, keepdims=True); dw /= n
    rays = np.concatenate([np.broadcast_to(o, dw.shape), dw], 1).astype(np.float32)
    meas = np.isfinite(dep) & (dep > 0)
    dd = np.where(meas, dep, 0)
    g = np.zeros_like(meas); g[:, 1:] |= np.abs(np.diff(dd, axis=1)) > 0.10; g[1:, :] |= np.abs(np.diff(dd, axis=0)) > 0.10
    g = ndimage.binary_dilation(g, iterations=1)
    ok = meas & ~g
    err = {}
    for k, sc in scenes.items():
        t = sc.cast_rays(rt.o3d.core.Tensor(rays))["t_hit"].numpy().astype(np.float64)
        z = (t / n[:, 0]).reshape(h, w)
        err[k] = ok & (~np.isfinite(z) | (np.abs(z - dep) > 0.15))
    only = err["occ_wavemap"] & ~err["occ_ours"]
    lab, nl = ndimage.label(ndimage.binary_opening(only))
    big = int(ndimage.sum(only, lab, range(1, nl + 1)).max()) if nl else 0
    m = max(1, ok.sum())
    res.append((big / m, err["occ_wavemap"].sum() / m, err["occ_ours"].sum() / m, i, fs.ids[i]))
res.sort(reverse=True)
print(ds, "frames scanned:", len(res))
print("largest region wrong only for wavemap | wavemap wrong | ours wrong | index | frame")
for r in res[:15]:
    print("%.3f  %.3f  %.3f  %d  %s" % r)
