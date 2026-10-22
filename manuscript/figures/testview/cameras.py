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
          ("realb01830", "real", "b", 1830), ("reala01380", "real", "a", 1380), ("reala01410", "real", "a", 1410),
          ("sima02460", "synthetic", "a", 2460), ("sima01680", "synthetic", "a", 1680), ("sima02490", "synthetic", "a", 2490),
          ("sima00030", "synthetic", "a", 30), ("sima00390", "synthetic", "a", 390), ("sima02250", "synthetic", "a", 2250),
          ("sima03120", "synthetic", "a", 3120), ("sima01860", "synthetic", "a", 1860), ("sima01740", "synthetic", "a", 1740),
          ("sima02550", "synthetic", "a", 2550), ("real04470", "real", "c", 4470), ("real05310", "real", "c", 5310),
          ("real03580", "real", "c", 3580), ("real04230", "real", "c", 4230), ("real06060", "real", "c", 6060),
          ("real05010", "real", "c", 5010), ("real06150", "real", "c", 6150), ("sim02420", "synthetic", "b", 2420),
          ("sim02430", "synthetic", "b", 2430), ("real05370", "real", "c", 5370), ("real01890", "real", "c", 1890),
          ("sim02760", "synthetic", "b", 2760), ("sim00660", "synthetic", "b", 660), ("sim02440", "synthetic", "b", 2440),
          ("realb01150", "real", "b", 1150), ("realb01140", "real", "b", 1140), ("real05320", "real", "c", 5320),
          ("real05330", "real", "c", 5330), ("real03850", "real", "c", 3850), ("real05670", "real", "c", 5670),
          ("sim02810", "synthetic", "b", 2810), ("sim02820", "synthetic", "b", 2820), ("sim02830", "synthetic", "b", 2830),
          ("sim02800", "synthetic", "b", 2800), ("sim02900", "synthetic", "b", 2900), ("sim02910", "synthetic", "b", 2910),
          ("sim02870", "synthetic", "b", 2870), ("sim02700", "synthetic", "b", 2700), ("sim02730", "synthetic", "b", 2730),
          ("sim00720", "synthetic", "b", 720), ("sim02370", "synthetic", "b", 2370), ("sim00640", "synthetic", "b", 640),
          ("sim02690", "synthetic", "b", 2690), ("sim03180", "synthetic", "b", 3180), ("sim03200", "synthetic", "b", 3200),
          ("sim00400", "synthetic", "b", 400), ("sim01830", "synthetic", "b", 1830), ("sim02850", "synthetic", "b", 2850)]
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
