"""Where an occupancy map lost a surface that still exists, at a held-out view (fig:qualitative): pixels whose measured
depth shows a surface that our occupancy map reproduces (within 8 cm) but wavemap's map does not (no cell along the ray,
or the first cell more than 15 cm behind the measured surface). Same camera, crop and cubes as render_views.py.
  occ_loss.py SCENE        writes DATA/renders/<SCENE>_occ_{ours,wavemap}_err.npy: measured pixels (away from depth
                           discontinuities) where the map shows no surface or one more than 15 cm off the measured depth"""
import json
import sys

import numpy as np

src = open("/home/jixian/Desktop/FT/CVPR/manuscript/figures/testview/render_views.py").read()
exec(src.split("\nscene = sys.argv[1]")[0])           # GEO, DATA, cubes(), rt (render_tsdf)
sys.path.insert(0, "/home/jixian/Desktop/FT/runs/update_layer_game_T1_20261006/worktrees/v4_snap")
from update_layer.frames import FlatSession, real_session, synthetic_session  # noqa: E402

STEP = {"real": 2, "sim": 1}
scene = sys.argv[1]
dataset = next(k for k in GEO if scene.startswith(k))
cam = json.load(open("/home/jixian/Desktop/FT/CVPR/manuscript/figures/testview/cameras.json"))[scene]
ses = {"real": "c", "sim": "b"}[dataset] if not scene.startswith(("realb", "sima")) else scene[len(dataset)]
fs = FlatSession({"real": real_session, "sim": synthetic_session}[dataset](ses))
i = fs.ids.index(cam["frame"])
K, s = fs.K, STEP[dataset]


def crop_axis(c, offset, full, step):
    best = None
    for first in range(0, 64):
        cs = (c - offset - first) / step
        n = int(round(2 * cs + 1))
        if n < 2 or first + step * (n - 1) > full - 1:
            continue
        err = abs((n - 1) / 2 - cs)
        if best is None or err < best[0] - 1e-9 or (abs(err - best[0]) < 1e-9 and n > best[2]):
            best = (err, first, n)
    return best[1], best[2]


(top, rows), (left, cols) = crop_axis(K.cy, K.offset, K.height, s), crop_axis(K.cx, K.offset, K.width, s)
depth = fs.load(i).depth[top:top + s * (rows - 1) + 1:s, left:left + s * (cols - 1) + 1:s]   # z along the optical axis

W, H = cam["width"], cam["height"]
T = np.asarray(cam["T_world_cam"], dtype=np.float64)
R, origin = T[:3, :3], T[:3, 3]
uu, vv = np.meshgrid(np.arange(W) + 0.5, np.arange(H) + 0.5)
d_cam = np.stack([(uu - cam["cx"]) / cam["fx"], (vv - cam["cy"]) / cam["fy"], np.ones_like(uu)], -1).reshape(-1, 3)
d = d_cam @ R.T
norm = np.linalg.norm(d, axis=1, keepdims=True); d /= norm
eye = origin


def z_of(item):
    path, vb, vo = GEO[dataset][item]
    dd = np.load(path)
    far = lambda q: q[np.linalg.norm(q - eye, axis=1) > 0.2]
    parts = [cubes(far(dd["background"]), vb)] + ([cubes(far(dd["objects"]), vo)] if len(dd["objects"]) else [])
    V = np.concatenate([p[0] for p in parts]); off = np.cumsum([0] + [len(p[0]) for p in parts[:-1]])
    F = np.concatenate([p[1] + o for p, o in zip(parts, off)])
    rays = np.concatenate([np.broadcast_to(origin, d.shape), d], 1).astype(np.float32)
    t = rt.scene_of(V, F).cast_rays(rt.o3d.core.Tensor(rays))["t_hit"].numpy().astype(np.float64)
    return (t / norm[:, 0]).reshape(H, W)                  # range -> z


z_ours, z_wm = z_of("occ_ours"), z_of("occ_wavemap")
meas = np.isfinite(depth) & (depth > 0)
dz = np.zeros_like(depth); dz[~meas] = 0
g = np.zeros(depth.shape, bool)                               # depth discontinuities and their neighbourhood
dep = np.where(meas, depth, 0)
g[:, 1:] |= np.abs(np.diff(dep, axis=1)) > 0.10
g[1:, :] |= np.abs(np.diff(dep, axis=0)) > 0.10
from scipy import ndimage
g = ndimage.binary_dilation(g, iterations=3)
for name, z in (("ours", z_ours), ("wavemap", z_wm)):
    err = meas & ~g & (~np.isfinite(z) | (np.abs(z - depth) > 0.15))
    np.save(f"{DATA}/renders/{scene}_occ_{name}_err.npy", err)
    print(scene, name, "differs from the image (> 15 cm or missing) on %.3f of measured pixels" % (err.sum() / max(1, meas.sum())))
