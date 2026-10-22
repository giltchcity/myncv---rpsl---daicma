"""Real-room (or simulated, with its exact depth as ground truth) views for fig:qualitative where wavemap's occupancy map visibly loses or keeps surface while all of our maps
match the scene. Ground truth per pixel: the reference mesh of the visit (built from all of its RGB-D frames), so surfaces
the frame itself does not measure still count. A map is wrong at a pixel where its surface is missing or more than 15 cm
off the reference. Reported per frame (every 4th pixel):
  wm      largest connected region wrong for wavemap and right for our occupancy and our TSDF map (share of the image)
  pan     the same for Panoptic Multi-TSDFs against our TSDF map
  tsdf, occ   share of reference pixels where our TSDF / occupancy map is wrong
  person  share of pixels labelled person (ADE20K 12)
  psnr    our and GaME's whole-frame PSNR of the Gaussian maps (paper_figs_20261022/testview/real/table.csv; third visit)
  scan_real_views.py c|b|sim STEP"""
import csv
import json
import sys

import numpy as np
from scipy import ndimage

src = open("/home/jixian/Desktop/FT/CVPR/manuscript/figures/testview/render_views.py").read()
exec(src.split("\nscene = sys.argv[1]")[0])           # GEO, DATA, FT, cubes(), rt
sys.path.insert(0, "/home/jixian/Desktop/FT/runs/update_layer_game_T1_20261006/worktrees/v4_snap")
from update_layer.frames import FlatSession, real_session, synthetic_session  # noqa: E402

ses, step = sys.argv[1], int(sys.argv[2])
SIM = ses == "sim"
geo = GEO["sim"] if SIM else (GEO["real"] if ses == "c" else GEO["realb"])
ref_mesh = None if SIM else f"{FT}/results/abc_eval_v2/geometry/{ses.upper()}_reference_1cm.ply"
fs = FlatSession(synthetic_session("b") if SIM else real_session(ses))
if SIM:
    run_json = "/home/jixian/Desktop/FT/runs/update_layer_game_T1_20261006/syn_u29_aed974e/session_b/run.json"
    held = set(int(x) for x in json.load(open(run_json))["g8_holdout"]["stamps"])
    frames = [i for i in range(len(fs.ids)) if fs.stamp_ns(i) in held][::step]
    table = {int(r["frame"]): r for r in csv.DictReader(open(
        "/home/jixian/Desktop/FT/runs/update_layer_game_T1_20261006/analysis/paper_figs_20261022/testview/sim/table.csv"))}
elif ses == "c":
    run_json = "/home/jixian/Desktop/FT/runs/update_layer_game_T1_20261006/verify_real_5fa93c0/session_c/run.json"
    held = set(int(x) for x in json.load(open(run_json))["g8_holdout"]["stamps"])
    frames = [i for i in range(len(fs.ids)) if fs.stamp_ns(i) in held][::step]
    table = {int(r["frame"]): r for r in csv.DictReader(open(
        "/home/jixian/Desktop/FT/runs/update_layer_game_T1_20261006/analysis/paper_figs_20261022/testview/real/table.csv"))}
else:
    frames = list(range(0, len(fs.ids), step))
    table = {}


def mesh_scene(path):
    V, F, _ = rt.load(path)
    return rt.scene_of(V, F)


def occ_scene(item):
    path, vb, vo = geo[item]
    d = np.load(path)
    parts = [cubes(d["background"], vb)] + ([cubes(d["objects"], vo)] if len(d["objects"]) else [])
    V = np.concatenate([p[0] for p in parts]); off = np.cumsum([0] + [len(p[0]) for p in parts[:-1]])
    F = np.concatenate([p[1] + o for p, o in zip(parts, off)])
    return rt.scene_of(V, F)


scenes = {"wm": occ_scene("occ_wavemap"), "occ": occ_scene("occ_ours"), "tsdf": mesh_scene(geo["tsdf_ours"]),
          "pan": mesh_scene(geo["tsdf_khronos" if SIM else "tsdf_panoptic"])}
if not SIM:
    scenes["ref"] = mesh_scene(ref_mesh)
K = fs.K
rows = []
for i in frames:
    f = fs.load(i)
    sem = f.semantic[::4, ::4] if f.semantic is not None else None
    h, w = f.depth[::4, ::4].shape
    uu, vv = np.meshgrid(np.arange(w) * 4 + K.offset, np.arange(h) * 4 + K.offset)
    dc = np.stack([(uu - K.cx) / K.fx, (vv - K.cy) / K.fy, np.ones_like(uu, dtype=float)], -1).reshape(-1, 3)
    Rw, o = f.T_world_cam[:3, :3], f.T_world_cam[:3, 3]
    dw = dc @ Rw.T; dw /= np.linalg.norm(dw, axis=1, keepdims=True)
    rays = np.concatenate([np.broadcast_to(o, dw.shape), dw], 1).astype(np.float32)
    t = {k: sc.cast_rays(rt.o3d.core.Tensor(rays))["t_hit"].numpy().astype(np.float64).reshape(h, w) for k, sc in scenes.items()}
    if SIM:                                                    # exact depth: z along the axis -> range along the ray
        zc = f.depth[::4, ::4]
        t["ref"] = zc * np.linalg.norm(dc, axis=1).reshape(h, w)
        t["ref"][~np.isfinite(zc) | (zc > 8.0)] = np.nan
    valid = np.isfinite(t["ref"])
    wrong = {k: valid & (~np.isfinite(t[k]) | (np.abs(t[k] - t["ref"]) > 0.15)) for k in ("wm", "occ", "tsdf", "pan")}

    def region(m):
        lab, n = ndimage.label(ndimage.binary_opening(m))
        return float(ndimage.sum(m, lab, range(1, n + 1)).max()) / m.size if n else 0.0
    wm = region(wrong["wm"] & ~wrong["occ"] & ~wrong["tsdf"])
    occ_only = region(wrong["occ"] & ~wrong["wm"])                # where only our occupancy map is wrong (its residue)
    tsdf_only = region(wrong["tsdf"] & ~wrong["pan"])
    rr = t["ref"][valid]
    spread = float(np.percentile(rr, 90) - np.percentile(rr, 10)) if rr.size else 0.0   # small for a view of one wall
    pan = region(wrong["pan"] & ~wrong["tsdf"])
    nv = max(1, valid.sum())
    person = 0.0 if SIM else (float((sem == 12).mean()) if sem is not None else 0.0)
    r = table.get(i, {})
    rows.append(dict(frame=i, wm=wm, pan=pan, occ_only=occ_only, tsdf_only=tsdf_only, spread=spread,
                     tsdf=wrong["tsdf"].sum() / nv, occ=wrong["occ"].sum() / nv, person=person,
                     psnr_ours=float(r.get("psnr_ours", "nan") or "nan"), psnr_game=float(r.get("psnr_game3", "nan") or "nan")))
out = f"{DATA}/scan_views_{ses}.csv"
with open(out, "w", newline="") as fh:
    wr = csv.DictWriter(fh, list(rows[0])); wr.writeheader(); wr.writerows(rows)
ok = [r for r in rows if r["person"] == 0 and r["occ_only"] < 0.01 and r["tsdf_only"] < 0.02 and r["spread"] > 1.5]
ok.sort(key=lambda r: r["wm"], reverse=True)
print(f"{ses}: {len(rows)} frames; {len(ok)} with no visible region wrong only for our maps and a depth spread > 1.5 m")
print("frame   wm     pan    occ_only tsdf_only spread  psnr ours / GaME")
for r in ok[:20]:
    print("%5d  %.3f  %.3f  %.4f   %.4f    %.1f   %.2f / %.2f" % (r["frame"], r["wm"], r["pan"], r["occ_only"], r["tsdf_only"],
                                                          r["spread"], r["psnr_ours"], r["psnr_game"]))
