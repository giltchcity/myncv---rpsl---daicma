"""The cameras of the held-out frames in fig:testview, as the Gaussian renders see them (GaME's crop: principal point at
the image centre, every STEP-th pixel), in the format of renders_tsdf/render_tsdf.py (opencv axes, T_world_cam
camera-to-world in the dataset's common world frame, pixel centres at u + 0.5), and each frame's photo with the same crop.
  cameras.py        writes cameras.json next to this script and PHOTOS/<name>.png"""
import json
import os
import sys

import numpy as np
from PIL import Image

sys.path.insert(0, "/home/jixian/Desktop/FT/runs/update_layer_game_T1_20261006/worktrees/v4_snap")
from update_layer.frames import FlatSession, flat_session, real_session, synthetic_session  # noqa: E402

STEP = {"synthetic": 1, "real": 2, "flat": 1}       # game.py STEP
FRAMES = [("sim02090", "synthetic", "b", 2090), ("sim02990", "synthetic", "b", 2990), ("sim03080", "synthetic", "b", 3080),
          ("sim01870", "synthetic", "b", 1870), ("sim00390", "synthetic", "b", 390),
          ("flat00229", "flat", "b", 229), ("real04940", "real", "c", 4940), ("real04740", "real", "c", 4740),
          ("real04850", "real", "c", 4850), ("realb02790", "real", "b", 2790), ("realb03000", "real", "b", 3000),
          ("realb01830", "real", "b", 1830), ("reala01380", "real", "a", 1380), ("reala01410", "real", "a", 1410)]
PHOTOS = "/home/jixian/Desktop/FT/notes/paper_method_experiments_20261019/renders_views/photos"   # the frame, cropped as above


def crop_axis(c, offset, full, step):
    """game.Crop: the first sample and the sample count that put the principal point at the image centre."""
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


out = {}
for name, ds, ses, i in FRAMES:
    spec = {"synthetic": synthetic_session, "flat": flat_session, "real": real_session}[ds](ses)
    fs = FlatSession(spec)
    K, s = fs.K, STEP[ds]
    (top, rows), (left, cols) = crop_axis(K.cy, K.offset, K.height, s), crop_axis(K.cx, K.offset, K.width, s)
    rgb = fs.load(i, color=True).color
    os.makedirs(PHOTOS, exist_ok=True)
    Image.fromarray(rgb[top:top + s * (rows - 1) + 1:s, left:left + s * (cols - 1) + 1:s]).save(f"{PHOTOS}/{name}.png")
    out[name] = dict(name=name, width=cols, height=rows, fx=K.fx / s, fy=K.fy / s, cx=cols / 2.0, cy=rows / 2.0,
                     T_world_cam=fs.pose(i).tolist(), frame=fs.ids[i])
    print(name, cols, rows, round(K.fx / s, 2))
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cameras.json"), "w"), indent=1)
