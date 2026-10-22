"""The map of any time (fig:fourd): our Gaussian map of the simulated apartment queried at a moment, M(t), against the
ground truth rendered by Isaac Sim at the same pose and moment. Poses the camera revisited; maps saved per round, not
refined. GaME keeps only its final map, so it has no map of an earlier time to compare.
  make_fourd.py        writes assets/*.png and fourd.html next to this script (build with build.sh)
Panels: leftover_photo_20261022/fourd3 (panels/<view>_<round>_ours.png, revisit_summary.json for the PSNR over the
whole frame) and the Isaac renders in Synthetic_ABC/final_state_renders_20261022/fourd_fig3/out."""
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
P = "/home/jixian/Desktop/FT/runs/update_layer_game_T1_20261006/analysis/leftover_photo_20261022/fourd3/panels"
G = "/mnt/d/3Study/ETH/FT/Synthetic_ABC/final_state_renders_20261022/fourd_fig3/out"
A = os.path.join(HERE, "assets"); os.makedirs(A, exist_ok=True)

# (key, label, crop box (4:3), [(column label, ground truth, ours, PSNR of ours)])
GROUPS = [
    ("bed", "(a) The bed moved between the visits.", (0, 125, 440, 455),
     [("1st visit, 32 s", f"{G}/r0_a_t032.40_rgb.png", f"{P}/0_2_ours.png", "29.0"),
      ("2nd visit, 76 s", f"{G}/r0_b_t075.60_rgb.png", f"{P}/0_19_ours.png", "26.8")]),
    ("win", "(b) The sofa replaced the lounge chair while the robot looked away.", (40, 0, 613, 430),
     [("2nd visit, 43 s", f"{G}/r4_b_t043.20_rgb.png", f"{P}/4_16_ours.png", "20.7"),
      ("2nd visit, 108 s", f"{G}/r4_b_t108.00_rgb.png", f"{P}/4_22_ours.png", "24.3")]),
]
W = 148
H = round(W * 3 / 4)

heads, gts, ours, labels = ['<div></div>'], ['<div class="rl"><span>Ground truth</span></div>'], \
    ['<div class="rl ours"><span>Ours, map at <i>t</i></span></div>'], ['<div></div>']
for g, (key, label, box, cols) in enumerate(GROUPS):
    if g:
        for lst in (heads, gts, ours, labels):
            lst.append("<div></div>")
    for k, (name, gt, our, psnr) in enumerate(cols):
        for kind, src in (("gt", gt), ("ours", our)):
            Image.open(src).convert("RGB").crop(box).resize((4 * W, 4 * H), Image.LANCZOS).save(f"{A}/{key}{k}_{kind}.png")
        heads.append(f'<div class="head">{name}</div>')
        gts.append(f'<div class="img"><img src="assets/{key}{k}_gt.png"></div>')
        ours.append(f'<div class="img ours"><img src="assets/{key}{k}_ours.png"><span class="psnr">{psnr} dB</span></div>')
    labels.append(f'<div class="label">{label}</div>')
cells = "\n".join(heads + gts + ours + labels)

height_in = (6 + 12 + 3 + H + 3 + H + 3 + 12 + 4) / 96
html = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>The map of any time</title>
<style>
  @page {{ size: 6.875in {height_in:.3f}in; margin: 0; }}
  :root {{ --ours:#BF9000; }}
  * {{ box-sizing: border-box; }}
  html, body {{ margin:0; padding:0; background:#fff; }}
  body {{ width:6.875in; height:{height_in:.3f}in; font-family: "Times New Roman", Times, serif; color:#000;
         -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  .fig {{ display:grid; justify-content:center; padding:6px 6px 4px; column-gap:3px; row-gap:3px;
         grid-template-columns: 12px {W}px {W}px 9px {W}px {W}px; grid-template-rows: 12px {H}px {H}px 12px; }}
  .rl {{ display:flex; align-items:center; justify-content:center; }}
  .rl span {{ transform: rotate(-90deg); white-space:nowrap; font-size:7.4pt; }}
  .rl.ours span {{ font-weight:700; color:var(--ours); }}
  .head {{ font-size:7.6pt; text-align:center; align-self:end; }}
  .img {{ position:relative; overflow:hidden; background:#000; }}
  .img img {{ display:block; width:100%; height:100%; object-fit:cover; }}
  .img.ours {{ outline: 1.4px solid var(--ours); outline-offset: -1.4px; }}
  .psnr {{ position:absolute; right:3px; bottom:3px; font-size:6pt; line-height:1; color:#000;
          background:rgba(255,255,255,.88); border-radius:1px; padding:1.4px 2.6px; }}
  .label {{ grid-column: span 2; font-size:7.4pt; font-style:italic; text-align:center; align-self:start; }}
</style></head>
<body><div class="fig">
{cells}
</div></body></html>
"""
open(os.path.join(HERE, "fourd.html"), "w").write(html)
print("ok", f"{height_in:.2f} in")
