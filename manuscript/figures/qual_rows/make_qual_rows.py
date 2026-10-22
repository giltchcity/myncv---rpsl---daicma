"""Qualitative comparison (fig:qualitative), one row per held-out view, one column per method, in two blocks: the real room
after its third visit and the simulated apartment after its second. Each representation's baseline is its published
update on the real room (Panoptic Multi-TSDFs, GaME, wavemap) and Khronos for the TSDF on the simulated apartment.
  make_qual_rows.py        writes assets/*.png and qual_rows.html next to this script (build with build.sh)
TSDF and occupancy renders: figures/testview/render_views.py (colors from the nearest reference surface); Gaussian renders:
the final maps after the refinement that follows the last visit (paper_figs_20261022/testview, leftover_photo_20261022/picks)."""
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
R = "/home/jixian/Desktop/FT/notes/paper_method_experiments_20261019/renders_views"
TR = "/home/jixian/Desktop/FT/runs/update_layer_game_T1_20261006/analysis/paper_figs_20261022/testview/real"
TS = "/home/jixian/Desktop/FT/runs/update_layer_game_T1_20261006/analysis/paper_figs_20261022/testview/sim"
PK = "/home/jixian/Desktop/FT/runs/update_layer_game_T1_20261006/analysis/leftover_photo_20261022/picks/real"
A = os.path.join(HERE, "assets"); os.makedirs(A, exist_ok=True)


def real_row(f, box, gs):
    return (f"real{f}", box, [f"{R}/photos/real0{f}.png", f"{R}/renders/real0{f}_tsdf_panoptic.png",
                              f"{R}/renders/real0{f}_tsdf_ours.png", f"{gs}/frame0{f}_{'game_row3' if gs == TR else 'game'}.png",
                              f"{gs}/frame0{f}_ours.png", f"{R}/renders/real0{f}_occ_wavemap.png",
                              f"{R}/renders/real0{f}_occ_ours.png"])


def sim_row(f, box, gs=None):
    photo, game, ours = ((f"{TS}/frame0{f}_photo.png", f"{TS}/frame0{f}_game_row3.png", f"{TS}/frame0{f}_ours.png") if gs is None
                         else (f"{gs}/synthetic_b0{f}_photo.png", f"{gs}/synthetic_b0{f}_game.png", f"{gs}/synthetic_b0{f}_ours.png"))
    return (f"sim{f}", box, [photo, f"{R}/renders/sim0{f}_tsdf_khronos.png", f"{R}/renders/sim0{f}_tsdf_ours.png", game, ours,
                             f"{R}/renders/sim0{f}_occ_wavemap.png", f"{R}/renders/sim0{f}_occ_ours.png"])


V = f"{R}/gs_frames"                       # renders of the final Gaussian maps at frames picked by scan_real_views.py
REAL_5320 = ("real5320", (275, 40, 845, 420),
             [f"{R}/photos/real05320.png", f"{R}/renders/real05320_tsdf_panoptic.png", f"{R}/renders/real05320_tsdf_ours.png",
              f"{V}/real_c05320_game.png", f"{V}/real_c05320_ours.png", f"{R}/renders/real05320_occ_wavemap.png",
              f"{R}/renders/real05320_occ_ours.png"])
BLOCKS = [("Real room", ["Panoptic", "GaME", "wavemap"],
           [real_row("4940", (120, 228, 528, 500), TR), REAL_5320]),
          ("Sim. apartment", ["Khronos", "GaME", "wavemap"],
           [sim_row("3080", (0, 27, 680, 480)), sim_row("3200", (0, 0, 680, 453), f"{R}/gs_frames")])]
W = 86
H = round(W * 2 / 3)
OURS = [False, False, True, False, True, False, True]

cells = []
for b, (block, base, rows) in enumerate(BLOCKS):
    cells += ['<div></div>', '<div></div>', '<div></div>',
              '<div class="grp" style="grid-column: span 2">TSDF</div>', '<div></div>',
              '<div class="grp" style="grid-column: span 2">3D Gaussians</div>', '<div></div>',
              '<div class="grp" style="grid-column: span 2">Occupancy</div>']
    names = ["Real image", base[0], "Ours", base[1], "Ours", base[2], "Ours"]
    head = ['<div></div>']
    for k, n in enumerate(names):
        if k in (1, 3, 5):
            head.append('<div></div>')
        head.append(f'<div class="head{" ours" if OURS[k] else ""}">{n}</div>')
    cells += head
    for r, (key, box, srcs) in enumerate(rows):
        row = [f'<div class="blk" style="grid-row: span 1">{"<span>" + block + "</span>" if r == 0 else ""}</div>']
        for k, src in enumerate(srcs):
            name = f"{key}_{k}"
            im = Image.open(src).convert("RGB")
            if im.size != (958, 532) and key.startswith("real"):
                im = im.resize((958, 532), Image.LANCZOS)
            im.crop(box).resize((6 * W, 6 * H), Image.LANCZOS).save(f"{A}/{name}.jpg", quality=93)
            if k in (1, 3, 5):
                row.append('<div></div>')
            row.append(f'<div class="img{" ours" if OURS[k] else ""}"><img src="assets/{name}.jpg"></div>')
        cells += row

n_img = sum(len(r) for _, _, r in BLOCKS)
height_px = 6 + len(BLOCKS) * (12 + 12) + n_img * H + (len(BLOCKS) * 2 + n_img - 1) * 3 + 5
cols = f"14px {W}px 6px {W}px {W}px 6px {W}px {W}px 6px {W}px {W}px"
html = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>Qualitative comparison</title>
<style>
  @page {{ size: 6.875in {height_px / 96:.3f}in; margin: 0; }}
  :root {{ --ours:#BF9000; --rule:#A5A5A5; }}
  * {{ box-sizing: border-box; }}
  html, body {{ margin:0; padding:0; background:#fff; }}
  body {{ width:6.875in; height:{height_px / 96:.3f}in; font-family: "Times New Roman", Times, serif; color:#000;
         -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  .fig {{ display:grid; justify-content:center; padding:6px 6px 3px; column-gap:2px; row-gap:3px;
         grid-template-columns: {cols}; grid-auto-rows: auto; }}
  .grp {{ font-size:7.4pt; font-style:italic; text-align:center; border-bottom:0.6pt solid var(--rule); line-height:11px; }}
  .head {{ font-size:7.4pt; text-align:center; line-height:12px; }}
  .head.ours {{ font-weight:700; color:var(--ours); }}
  .img {{ position:relative; height:{H}px; overflow:hidden; background:#000; }}
  .img img {{ display:block; width:100%; height:100%; object-fit:cover; }}
  .img.ours {{ outline: 1.3px solid var(--ours); outline-offset: -1.3px; }}
  .blk {{ position:relative; }}
  .blk span {{ position:absolute; left:50%; top:{H + 2}px; transform: translate(-50%, -50%) rotate(-90deg); white-space:nowrap;
              font-size:7.4pt; font-weight:700; }}
</style></head>
<body><div class="fig">
{chr(10).join(cells)}
</div></body></html>
"""
open(os.path.join(HERE, "qual_rows.html"), "w").write(html)
print("ok", f"{height_px / 96:.2f} in")
