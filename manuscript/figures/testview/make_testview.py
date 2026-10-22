"""Final maps after the last run, rendered at held-out camera poses of that run (fig:testview): the real image, then per
representation the baseline's map and ours, written as HTML.
  make_testview.py        writes assets/*.jpg and testview.html next to this script (build with build.sh)
3D Gaussians: the refined final maps (paper_figs_20261022/testview; PSNR over the whole frame, its candidates.md).
TSDF and occupancy: render_views.py at the same cameras (cameras.py)."""
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
T = "/home/jixian/Desktop/FT/runs/update_layer_game_T1_20261006/analysis/paper_figs_20261022/testview"
R = "/home/jixian/Desktop/FT/notes/paper_method_experiments_20261019/renders_views/renders"
A = os.path.join(HERE, "assets"); os.makedirs(A, exist_ok=True)

# (dataset folder, frame, label, 3:2 crop box, TSDF baseline (render key, name), PSNR of GaME, PSNR of ours, occupancy)
ROWS = [("sim", "02090", "Simulated apartment", (0, 27, 680, 480), ("khronos", "Khronos"), "21.07", "34.16", True),
        ("sim", "03080", "Simulated apartment", (0, 27, 680, 480), ("khronos", "Khronos"), "21.66", "31.87", True),
        ("real", "04940", "Real room", (120, 228, 528, 500), ("panoptic", "Panoptic"), "22.88", "25.12", True),
        ("flat", "00229", "Flat", (0, 27, 640, 454), ("khronos", "Khronos"), "21.38", "24.94", False)]
W_CELL, GAP, SEP = 86, 3, 5                       # px: image width, gap inside a group, extra gap between groups
H_CELL = round(W_CELL * 2 / 3)


def asset(src, box, name):
    im = Image.open(src).convert("RGB").crop(box)
    im.resize((420, 280), Image.LANCZOS).save(f"{A}/{name}.jpg", quality=92)
    return f"assets/{name}.jpg"


def card(img, chip, ours=False, psnr=None, light=False):
    psnr = f'<span class="psnr">{psnr} dB</span>' if psnr else ""
    kind = "light" if light else ("ours" if ours else "")
    return (f'<div class="card{" now" if ours else ""}"><img src="{img}">'
            f'<span class="chip {kind}">{chip}</span>{psnr}</div>')


cells = []
for d, f, label, box, (tb, tname), p_game, p_ours, occ in ROWS:
    key = f"{d}{f}"
    cells += [card(asset(f"{T}/{d}/frame{f}_photo.png", box, f"{key}_photo"), label, light=True), "<div></div>",
              card(asset(f"{T}/{d}/frame{f}_game_row3.png", box, f"{key}_gs_game"), "GaME", psnr=p_game),
              card(asset(f"{T}/{d}/frame{f}_ours.png", box, f"{key}_gs_ours"), "Ours", ours=True, psnr=p_ours), "<div></div>",
              card(asset(f"{R}/{key}_tsdf_{tb}.png", box, f"{key}_tsdf_base"), tname),
              card(asset(f"{R}/{key}_tsdf_ours.png", box, f"{key}_tsdf_ours"), "Ours", ours=True), "<div></div>"]
    cells += ([card(asset(f"{R}/{key}_occ_wavemap.png", box, f"{key}_occ_base"), "wavemap"),
               card(asset(f"{R}/{key}_occ_ours.png", box, f"{key}_occ_ours"), "Ours", ours=True)] if occ
              else ["<div></div>", "<div></div>"])

cols = f"{W_CELL}px {SEP}px " + f" {SEP}px ".join([f"{W_CELL}px {W_CELL}px"] * 3)
n = len(ROWS)
height_px = 12 + 13 + GAP + n * H_CELL + (n - 1) * 4
head = ('<div class="head">Real image</div><div></div>'
        '<div class="head group">3D Gaussians</div><div></div>'
        '<div class="head group">TSDF</div><div></div>'
        '<div class="head group">Occupancy</div>')
html = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>Held-out views</title>
<style>
  @page {{ size: 6.875in {height_px / 96:.3f}in; margin: 0; }}
  :root {{ --ink:#000000; --gray:#7F7F7F; --rule:#A5A5A5; --ours:#BF9000; --blue:#2E75B6; --memory:#7030A0; }}
  * {{ box-sizing: border-box; }}
  html, body {{ margin:0; padding:0; background:#fff; }}
  body {{ width:6.875in; height:{height_px / 96:.3f}in; font-family: "Times New Roman", Times, serif; color:var(--ink);
         -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  .fig {{ display:grid; padding:6px; column-gap:{GAP}px; row-gap:4px; justify-content:center;
         grid-template-columns: {cols}; grid-template-rows: 13px repeat({n}, {H_CELL}px); }}
  .head {{ font-size:7.4pt; font-weight:700; display:flex; align-items:center; justify-content:center; white-space:nowrap;
          border-bottom: 0.65pt solid var(--rule); margin-bottom:2px; }}
  .head.group {{ grid-column: span 2; }}
  .card {{ position:relative; border-radius:2px; overflow:hidden; background:#000; outline: 0.5px solid #BFBFBF; }}
  .card img {{ display:block; width:100%; height:100%; object-fit:cover; }}
  .card.now {{ outline: 1.2px solid var(--ours); }}
  .chip {{ position:absolute; left:2px; top:2px; font-size:5.8pt; line-height:1; color:var(--ink); border-radius:1px;
          padding:1.2px 2.4px 1.4px; white-space:nowrap; background:rgba(255,255,255,.9); }}
  .chip.ours {{ color: var(--ours); font-weight:700; }}
  .chip.light {{ font-style: italic; }}
  .psnr {{ position:absolute; right:2px; bottom:2px; font-size:5.8pt; line-height:1; color:var(--ink);
          background:rgba(255,255,255,.9); border-radius:1px; padding:1.2px 2.4px 1.4px; }}
  .now .psnr {{ color: var(--ours); font-weight:700; }}
</style></head>
<body><div class="fig">
{head}
{chr(10).join(cells)}
</div></body></html>
"""
open(os.path.join(HERE, "testview.html"), "w").write(html)
print("ok", f"{height_px / 96:.2f} in")
