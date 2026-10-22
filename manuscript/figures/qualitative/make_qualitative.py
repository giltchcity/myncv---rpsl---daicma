"""Qualitative results on the real room after the third visit (fig:qualitative): insets of the final maps, written as HTML.
  make_qualitative.py        writes assets/*.png and qualitative.html next to this script (build with build.sh)"""
import os
import numpy as np
from PIL import Image
from scipy import ndimage

HERE = os.path.dirname(os.path.abspath(__file__))
FT = "/home/jixian/Desktop/FT"
T = f"{FT}/notes/paper_method_experiments_20261019/renders_tsdf/real_oblique_v2_color"
G = f"{FT}/runs/update_layer_game_T1_20261006/analysis/paper_figs_20261022/real"
O = f"{FT}/notes/paper_method_experiments_20261019/renders_occ"
A = os.path.join(HERE, "assets"); os.makedirs(A, exist_ok=True)

ROWS = [("TSDF", {"scratch": f"{T}/khronos_c_color.png", "update": f"{T}/panoptic_c_color.png",
                  "ours": f"{T}/ours_c_color.png", "ref": f"{T}/reference_c_color.png", "refa": f"{T}/reference_a_color.png"},
         ("Khronos, per run", "Panoptic Multi-TSDFs")),
        ("3D Gaussians", {"scratch": f"{G}/game_row1_C_end.png", "update": f"{G}/game_row3_C_end.png",
                          "ours": f"{G}/ours_C_end.png", "ref": f"{T}/reference_c_color.png", "refa": f"{T}/reference_a_color.png"},
         ("GaME, from scratch", "GaME")),
        ("Occupancy", {"scratch": f"{O}/occ_row1_C_end_color.png", "update": f"{O}/occ_row3_C_end_color.png",
                       "ours": f"{O}/occ_row4_C_end_color.png", "ref": f"{T}/reference_c_color.png", "refa": f"{T}/reference_a_color.png"},
         ("wavemap, from scratch", "wavemap"))]
FLOOR = (450, 380, 990, 690)                  # where objects moved between runs B and C
KEPT = (1060, 40, 1320, 300)                  # surfaces that the third visit did not observe
ROOM = (300, 40, 1500, 980)
GHOST = {"TSDF": (845, 420, 950, 556), "3D Gaussians": (484, 592, 588, 668)}


def load(path):
    a = np.asarray(Image.open(path).convert("RGBA")).astype(np.float32) / 255
    if a[..., 3].min() > 0.99:                                   # white background
        a[..., 3] = (a[..., :3].min(2) < 0.95).astype(np.float32)
    rgb = a[..., :3] * a[..., 3:4] + (1 - a[..., 3:4])
    return rgb, a[..., 3] > 0.5


def save(rgb, box, name, scale=2):
    im = Image.fromarray((np.clip(rgb, 0, 1) * 255).astype(np.uint8)).crop(box)
    im.resize((im.width * scale // 2, im.height * scale // 2), Image.LANCZOS).save(f"{A}/{name}.png")


def rel(b, box):
    """A bounding box in percent of an inset."""
    x0, y0, x1, y1 = box
    return [100 * (b[0] - x0) / (x1 - x0), 100 * (b[1] - y0) / (y1 - y0), 100 * (b[2] - b[0]) / (x1 - x0),
            100 * (b[3] - b[1]) / (y1 - y0)]


marks = {}
for name, files, _ in ROWS:
    key = name.split()[0].lower().replace("3d", "gs")
    imgs = {k: load(v) for k, v in files.items()}
    for k, (rgb, _) in imgs.items():
        save(rgb, FLOOR, f"{key}_{k}_floor")
        save(rgb, KEPT, f"{key}_{k}_kept")
    save(imgs["ours"][0], ROOM, f"{key}_overview", scale=1)
    m = {}
    if name in GHOST:
        m["update_floor"] = ("red", rel(GHOST[name], FLOOR))
    else:                                                        # occupancy: floor cells the update cleared
        hole = imgs["ours"][1] & ~imgs["update"][1]
        sub = np.zeros_like(hole); x0, y0, x1, y1 = FLOOR; sub[y0:y1, x0:x1] = hole[y0:y1, x0:x1]
        sub = ndimage.binary_opening(sub, iterations=2)
        lab, n = ndimage.label(ndimage.binary_dilation(sub, iterations=10))
        if n:
            sizes = ndimage.sum(sub, lab, range(1, n + 1)); ys, xs = np.where(lab == 1 + int(np.argmax(sizes)))
            m["update_floor"] = ("blue", rel((xs.min() - 6, ys.min() - 6, xs.max() + 6, ys.max() + 6), FLOOR))
    miss = imgs["ours"][1] & ~ndimage.binary_dilation(imgs["scratch"][1], iterations=6)
    sub = np.zeros_like(miss); x0, y0, x1, y1 = KEPT; sub[y0:y1, x0:x1] = miss[y0:y1, x0:x1]
    sub = ndimage.binary_opening(sub, iterations=3)
    if sub.any():
        lab, n = ndimage.label(ndimage.binary_dilation(sub, iterations=8))
        sizes = ndimage.sum(sub, lab, range(1, n + 1)); ys, xs = np.where(lab == 1 + int(np.argmax(sizes)))
        m["scratch_kept"] = ("blue", rel((max(xs.min(), x0), max(ys.min(), y0), min(xs.max(), x1), min(ys.max(), y1)), KEPT))
    marks[key] = m


def mark(spec):
    if not spec:
        return ""
    color, (x, y, w, h) = spec
    return (f'<span class="mark {color}" style="left:{x:.1f}%;top:{y:.1f}%;width:{w:.1f}%;height:{h:.1f}%"></span>')


fr = FLOOR[3] - FLOOR[1]; fw = FLOOR[2] - FLOOR[0]
ov = {k: rel(b, ROOM) for k, b in (("floor", FLOOR), ("kept", KEPT))}
rows_html = []
for name, files, (scr, upd) in ROWS:
    key = name.split()[0].lower().replace("3d", "gs")
    m = marks[key]
    cells = [f'<div class="rowlabel"><span>{name}</span></div>',
             f'<div class="card ov"><img src="assets/{key}_overview.png">'
             f'<span class="box floor" style="left:{ov["floor"][0]:.1f}%;top:{ov["floor"][1]:.1f}%;width:{ov["floor"][2]:.1f}%;height:{ov["floor"][3]:.1f}%"></span>'
             f'<span class="box kept" style="left:{ov["kept"][0]:.1f}%;top:{ov["kept"][1]:.1f}%;width:{ov["kept"][2]:.1f}%;height:{ov["kept"][3]:.1f}%"></span></div>',
             f'<div class="card fl"><img src="assets/{key}_update_floor.png">{mark(m.get("update_floor"))}<span class="chip">{upd}</span></div>',
             f'<div class="card fl now"><img src="assets/{key}_ours_floor.png"><span class="chip">Ours</span></div>',
             f'<div class="card fl"><img src="assets/{key}_ref_floor.png"><span class="chip light">Reference</span></div>',
             '<div></div>',
             f'<div class="card kp"><img src="assets/{key}_scratch_kept.png">{mark(m.get("scratch_kept"))}<span class="chip">{scr.split(",")[0]}</span></div>',
             f'<div class="card kp now"><img src="assets/{key}_ours_kept.png"><span class="chip">Ours</span></div>',
             f'<div class="card kp"><img src="assets/{key}_refa_kept.png"><span class="chip light">1st-visit ref.</span></div>']
    rows_html.append("\n".join(cells))

H_ROW = 62
html = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>Qualitative results</title>
<style>
  @page {{ size: 6.875in 2.42in; margin: 0; }}
  :root {{ --ink:#000000; --rule:#A5A5A5; --teal:#BF9000; --red:#404040; --blue:#7030A0; }}
  * {{ box-sizing: border-box; }}
  html, body {{ margin:0; padding:0; background:#fff; }}
  body {{ width:6.875in; height:2.42in; font-family: "Times New Roman", Times, serif; color: var(--ink);
         -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  .fig {{ display:grid; padding:6px 6px; row-gap:6px; column-gap:4px; align-items:stretch;
         grid-template-columns: 14px {int(H_ROW * 1.28)}px repeat(3, {int(H_ROW * fw / fr)}px) 6px repeat(3, {H_ROW}px);
         grid-template-rows: 13px repeat(3, {H_ROW}px); }}
  .group {{ font-size:7.4pt; font-weight:700; display:flex; align-items:center; white-space:nowrap;
           border-bottom: 0.65pt solid var(--rule); margin-bottom:2px; }}
  .rowlabel {{ display:flex; align-items:center; justify-content:center; }}
  .rowlabel span {{ transform: rotate(-90deg); white-space:nowrap; font-size:7.2pt; font-weight:700; }}
  .card {{ position:relative; border-radius:2px; overflow:hidden; background:#fff; outline: 0.5px solid #BFBFBF; }}
  .card img {{ display:block; width:100%; height:100%; object-fit:cover; }}
  .card.now {{ outline: 1.2px solid var(--teal); }}
  .chip {{ position:absolute; left:2px; top:2px; font-size:5.8pt; line-height:1; color:var(--ink);
          background:rgba(255,255,255,.9); border-radius:1px; padding:1.2px 2.4px 1.4px; white-space:nowrap; }}
  .now .chip {{ color: var(--teal); font-weight:700; }}
  .chip.light {{ font-style: italic; }}
  .mark {{ position:absolute; border-radius:50%; border:1.2px dashed; }}
  .mark.red {{ border-color: var(--red); }}  .mark.blue {{ border-color: var(--blue); }}
  .box {{ position:absolute; border:1px solid; border-radius:1px; }}
  .box.floor {{ border-color: var(--red); }}  .box.kept {{ border-color: var(--blue); }}
</style></head>
<body><div class="fig">
<div></div><div class="group">Final map</div>
<div class="group" style="grid-column: span 3; color: var(--red)">Where objects moved</div><div></div>
<div class="group" style="grid-column: span 3; color: var(--blue)">Not observed in the 3rd visit</div>
{chr(10).join(rows_html)}
</div></body></html>
"""
open(os.path.join(HERE, "qualitative.html"), "w").write(html)
print("ok", marks)
