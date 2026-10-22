"""The two failures of a mapper without an update (fig:problem), in the layout of ChordEdit's Fig. 3: full frames with one
box each, and the boxed regions enlarged below. Gaussian maps of the simulated apartment after its second visit.
  make_problem.py        writes assets/*.png and problem.html next to this script (build with build.sh)
(a) held-out pose 3080 of the second visit: reload = our final map with every Gaussian of the first visit kept (the
    Gaussians the layer ended re-enabled), which shows the moved sofa and side table at both places.
(b) pose 30 of the first visit: restart = GaME from scratch in the second visit, which lacks the ceiling and upper walls
    that the second visit did not observe; the furniture has moved between the visits."""
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
R = "/home/jixian/Desktop/FT/notes/paper_method_experiments_20261019/renders_views"
G = f"{R}/gs_frames"                      # Gaussian renders at frames of the first simulated visit
A = os.path.join(HERE, "assets"); os.makedirs(A, exist_ok=True)

# (key, label, [(column label, source, color class)], full-frame crop (3:2), zoom box in source pixels)
GROUPS = [
    ("a", "(a) Gone, but reloading keeps it.",
     [("Real image", f"{G}/synthetic_b03080_photo.png", "real"), ("Reload", f"{G}/synthetic_b03080_keepall.png", "naive"),
      ("Ours", f"{G}/synthetic_b03080_ours.png", "ours")],
     (0, 27, 680, 480), (150, 120, 430, 400)),
    ("b", "(b) Merely unseen, but restarting drops it.",
     [("Real image", f"{G}/synthetic_a00030_photo.png", "real"), ("Restart", f"{G}/synthetic_a00030_restart.png", "naive"),
      ("Ours", f"{G}/synthetic_a00030_ours.png", "ours")],
     (0, 0, 680, 453), (210, 0, 490, 280)),
]
W = 103                                   # px per image column at 96 px / in (two groups of three on 6.875 in)
H_FULL, H_ZOOM = round(W * 2 / 3), W


def rel(box, frame):
    x0, y0, x1, y1 = frame
    return [100 * (box[0] - x0) / (x1 - x0), 100 * (box[1] - y0) / (y1 - y0),
            100 * (box[2] - box[0]) / (x1 - x0), 100 * (box[3] - box[1]) / (y1 - y0)]


groups_html = []
for key, label, cols, frame, zoom in GROUPS:
    b = rel(zoom, frame)
    heads, fulls, zooms = [], [], []
    for k, (name, src, kind) in enumerate(cols):
        im = Image.open(src).convert("RGB")
        im.crop(frame).resize((3 * W * 2, 3 * H_FULL * 2), Image.LANCZOS).save(f"{A}/{key}{k}_full.png")
        im.crop(zoom).resize((3 * W * 2, 3 * H_ZOOM * 2), Image.LANCZOS).save(f"{A}/{key}{k}_zoom.png")
        heads.append(f'<div class="head {kind}">{name}</div>')
        fulls.append(f'<div class="img"><img src="assets/{key}{k}_full.png"><span class="box {kind}" style="left:{b[0]:.2f}%;'
                     f'top:{b[1]:.2f}%;width:{b[2]:.2f}%;height:{b[3]:.2f}%"></span></div>')
        zooms.append(f'<div class="img zoom {kind}"><img src="assets/{key}{k}_zoom.png"></div>')
    groups_html.append(f'<div class="group">{"".join(heads)}{"".join(fulls)}{"".join(zooms)}'
                       f'<div class="label">{label}</div></div>')

height_in = (6 + 12 + 3 + H_FULL + 4 + H_ZOOM + 3 + 12 + 4) / 96
html = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>Reload and restart</title>
<style>
  @page {{ size: 6.875in {height_in:.3f}in; margin: 0; }}
  :root {{ --real:#2E75B6; --naive:#262626; --ours:#BF9000; }}
  * {{ box-sizing: border-box; }}
  html, body {{ margin:0; padding:0; background:#fff; }}
  body {{ width:6.875in; height:{height_in:.3f}in; font-family: "Times New Roman", Times, serif; color:#000;
         -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  .fig {{ display:flex; justify-content:center; gap:16px; padding:6px 6px 4px; }}
  .group {{ display:grid; grid-template-columns: repeat(3, {W}px); grid-template-rows: 12px {H_FULL}px {H_ZOOM}px 12px;
           column-gap:3px; row-gap:3px; }}
  .head {{ font-size:7.6pt; text-align:center; align-self:end; }}
  .head.ours {{ font-weight:700; color:var(--ours); }}
  .img {{ position:relative; overflow:hidden; background:#000; }}
  .img img {{ display:block; width:100%; height:100%; object-fit:cover; }}
  .box {{ position:absolute; border:1.3px solid; }}
  .box.real {{ border-color:var(--real); }} .box.naive {{ border-color:var(--naive); }} .box.ours {{ border-color:var(--ours); }}
  .zoom {{ border:1.6px solid; }}
  .zoom.real {{ border-color:var(--real); }} .zoom.naive {{ border-color:var(--naive); }} .zoom.ours {{ border-color:var(--ours); }}
  .label {{ grid-column: span 3; font-size:7.4pt; font-style:italic; text-align:center; align-self:start; }}
</style></head>
<body><div class="fig">
{chr(10).join(groups_html)}
</div></body></html>
"""
open(os.path.join(HERE, "problem.html"), "w").write(html)
print("ok", f"{height_in:.2f} in")
