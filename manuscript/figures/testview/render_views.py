"""Geometry renders at the held-out cameras of fig:testview (cameras.json): the final TSDF meshes and the final occupancy
maps (one cube per occupied cell: wavemap's 2 cm cells, the elements' centres; none within 0.2 m of the camera), with the ray caster and light rig
of renders_tsdf/render_tsdf.py; rays that hit nothing are black, as in the Gaussian renders. Colors: the nearest colored
reference point within 10 cm, this run's reference first, then the earlier runs' (real room: the reference meshes;
simulated: colorref.py), then this run's within 30 cm; farther surface stays neutral gray.
  render_views.py SCENE [ITEM ...]        writes DATA/renders/SCENE_ITEM.png"""
import json
import os
import sys

import numpy as np
from PIL import Image
from scipy.spatial import cKDTree

sys.path.insert(0, "/home/jixian/Desktop/FT/notes/paper_method_experiments_20261019/renders_tsdf")
import render_tsdf as rt  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
FT = "/home/jixian/Desktop/FT"
DATA = f"{FT}/notes/paper_method_experiments_20261019/renders_views"   # refs/ (colorref.py), occ/ (occ_points.py), renders/
WT = f"{FT}/wt_takeover_runs"
GEO = {
    "sim": {"tsdf_khronos": f"{FT}/datasets/synthetic_ab/evaluation_complete_20260917/khronos/session_b/state/mesh.ply",
            "tsdf_ours": f"{WT}/superseded/hist1/replay_tk_synthetic_b/present.ply",
            "occ_wavemap": (f"{DATA}/occ/sim_row3.npz", 0.02, 0.02), "occ_ours": (f"{DATA}/occ/sim_row4.npz", 0.02, 0.02),
            "occ_restart": (f"{DATA}/occ/sim_row1.npz", 0.02, 0.02), "occ_reload": (f"{DATA}/occ/sim_row2.npz", 0.02, 0.02)},
    "flat": {"tsdf_khronos": f"{WT}/eval/khronos_flat_b/geometry_viewer.ply", "tsdf_ours": f"{WT}/eval/tk_flat_b/geometry_viewer.ply"},
    "real": {"tsdf_khronos": f"{FT}/eval/results/real/khronos/c/geometry/mesh_viewer.ply",
             "tsdf_panoptic": f"{FT}/eval/results/real/panoptic/c/geometry/mesh_viewer.ply",
             "tsdf_ours": f"{WT}/superseded/d1/eval/tk_real_c/real_abc/exports/takeover_c/geometry_viewer.ply",
             "occ_wavemap": (f"{DATA}/occ/real_row3.npz", 0.02, 0.02), "occ_ours": (f"{DATA}/occ/real_row4.npz", 0.02, 0.02),
             "occ_restart": (f"{DATA}/occ/real_row1.npz", 0.02, 0.02), "occ_reload": (f"{DATA}/occ/real_row2.npz", 0.02, 0.02)},
}
REFS = {"sim": [f"{DATA}/refs/synthetic_b.npz", f"{DATA}/refs/synthetic_a.npz"],
        "flat": [f"{DATA}/refs/flat_b.npz", f"{DATA}/refs/flat_a.npz"],
        "real": [f"{FT}/results/abc_eval_v2/geometry/{s}_reference_1cm.ply" for s in "CBA"]}
RADIUS, FAR, GRAY = 0.10, 0.30, np.array([0.80, 0.80, 0.80])   # FAR: last, this run's reference only
DIRS = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]])


def cubes(points, vox):
    """Vertices, faces and cell centre per face of the cell faces that border an empty cell."""
    ijk = np.unique(np.floor(points / vox).astype(np.int64), axis=0)
    lo = ijk.min(0) - 1
    dims = ijk.max(0) - lo + 2
    code = lambda a: ((a[:, 0] - lo[0]) * dims[1] + (a[:, 1] - lo[1])) * dims[2] + (a[:, 2] - lo[2])
    occupied = np.sort(code(ijk))
    V, F, C = [], [], []
    for d in DIRS:
        nb = code(ijk + d)
        k = np.searchsorted(occupied, nb)
        exposed = ijk[~((k < len(occupied)) & (occupied[np.minimum(k, len(occupied) - 1)] == nb))]
        axis = int(np.nonzero(d)[0][0])
        u, v = [a for a in range(3) if a != axis]
        base = exposed + (d > 0)                                  # the face's corner on the far side along d
        quad = []
        for du, dv in ((0, 0), (1, 0), (1, 1), (0, 1)):
            q = base.copy().astype(np.float64); q[:, u] += du; q[:, v] += dv
            quad.append(q * vox)
        n0 = sum(len(x) for x in V)
        V.append(np.stack(quad, 1).reshape(-1, 3))
        i = n0 + 4 * np.arange(len(exposed))[:, None]
        F.append(np.concatenate([i + [0, 1, 2], i + [0, 2, 3]]))
        C.append(np.concatenate([(exposed + 0.5) * vox] * 2))
    return np.concatenate(V), np.concatenate(F).astype(np.int64), np.concatenate(C)


def load_refs(dataset):
    refs = []
    for p in REFS[dataset]:
        if p.endswith(".npz"):
            d = np.load(p); refs.append((cKDTree(d["points"]), d["colors"].astype(np.float64)))
        else:
            V, _, C = rt.load(p); refs.append((cKDTree(V), C))
    return refs


def colors_at(refs, p):
    col = np.tile(GRAY, (len(p), 1)); todo = np.ones(len(p), bool)
    for (tree, C), r in [(ref, RADIUS) for ref in refs] + [(refs[0], FAR)]:
        idx = np.nonzero(todo)[0]
        if not len(idx):
            break
        d, i = tree.query(p[idx], distance_upper_bound=r)
        ok = np.isfinite(d)
        col[idx[ok]] = C[i[ok]]; todo[idx[ok]] = False
    return col


def render(V, F, albedo_of, cam, lit=0.55, bg=0.0):
    """render_tsdf.render without the crop box, on a background of value bg."""
    face_n = np.cross(V[F[:, 1]] - V[F[:, 0]], V[F[:, 2]] - V[F[:, 0]])
    vertex_n = rt.smooth_normals(V, F, face_n)
    unit_face_n = face_n / np.maximum(np.linalg.norm(face_n, axis=1, keepdims=True), 1e-12)
    W, H = cam["width"], cam["height"]
    T = np.asarray(cam["T_world_cam"], dtype=np.float64)
    R, origin = T[:3, :3], T[:3, 3]
    offsets = (np.arange(rt.SSAA) + 0.5) / rt.SSAA
    uu, vv = np.meshgrid((np.arange(W)[:, None] + offsets[None]).reshape(-1), (np.arange(H)[:, None] + offsets[None]).reshape(-1))
    d = np.stack([(uu - cam["cx"]) / cam["fx"], (vv - cam["cy"]) / cam["fy"], np.ones_like(uu)], -1).reshape(-1, 3) @ R.T
    d /= np.linalg.norm(d, axis=1, keepdims=True)
    rays = np.concatenate([np.broadcast_to(origin, d.shape), d], 1).astype(np.float32)
    ans = rt.scene_of(V, F).cast_rays(rt.o3d.core.Tensor(rays))
    t = ans["t_hit"].numpy().astype(np.float64)
    hit = np.isfinite(t)
    f = ans["primitive_ids"].numpy()[hit].astype(np.int64)
    uv = ans["primitive_uvs"].numpy()[hit].astype(np.float64)
    a, b = uv[:, 0:1], uv[:, 1:2]
    n = (1 - a - b) * vertex_n[F[f, 0]] + a * vertex_n[F[f, 1]] + b * vertex_n[F[f, 2]]
    norm = np.linalg.norm(n, axis=1, keepdims=True)
    n = np.where(norm > 0.3, n / np.maximum(norm, 1e-12), unit_face_n[f])
    n *= -np.sign(np.sum(n * d[hit], axis=1, keepdims=True) + 1e-12)
    key = R @ np.array([-0.45, -0.75, -1.0]) / np.linalg.norm([-0.45, -0.75, -1.0])
    shade = 0.30 + 0.48 * np.abs(np.sum(n * d[hit], axis=1)) + 0.26 * np.clip(n @ key, 0, None)
    shade = 1.0 - lit + lit * shade
    rgb = np.full((len(d), 3), float(bg))
    rgb[hit] = np.clip(albedo_of(f, origin + d[hit] * t[hit, None], uv) * shade[:, None], 0, 1)
    img = rgb.reshape(H, rt.SSAA, W, rt.SSAA, 3).mean((1, 3))
    return (img * 255 + 0.5).astype(np.uint8)


scene = sys.argv[1]
dataset = next(k for k in GEO if scene.startswith(k))
cam = json.load(open(f"{HERE}/cameras.json"))[scene]
items = sys.argv[2:] or list(GEO[dataset])
refs = load_refs(dataset)
os.makedirs(f"{DATA}/renders", exist_ok=True)
for item in items:
    src = GEO[dataset][item]
    if isinstance(src, tuple):
        d = np.load(src[0])
        eye = np.asarray(cam["T_world_cam"])[:3, 3]
        far = lambda q: q[np.linalg.norm(q - eye, axis=1) > 0.2]
        parts = [cubes(far(d["background"]), src[1])] + ([cubes(far(d["objects"]), src[2])] if len(d["objects"]) else [])
        V = np.concatenate([p[0] for p in parts]); off = np.cumsum([0] + [len(p[0]) for p in parts[:-1]])
        F = np.concatenate([p[1] + o for p, o in zip(parts, off)])
        face_col = colors_at(refs, np.concatenate([p[2] for p in parts]))
        albedo = lambda f, p, uv: face_col[f]
    else:
        V, F, _ = rt.load(src)
        albedo = lambda f, p, uv: colors_at(refs, p)
    Image.fromarray(render(V, F, albedo, cam)).save(f"{DATA}/renders/{scene}_{item}.png")
    print(scene, item, len(F), "faces", flush=True)
