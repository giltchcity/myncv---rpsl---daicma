"""Cells of the two showcase figures as separate images, and the LaTeX that places them (no composed figure).
  export_cells.py      writes cells/*.jpg, current.tex and history.tex next to this script"""
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
M = "/home/jixian/Desktop/FT/notes/paper_method_experiments_20261019/fig_materials_20261023"
CELLS = os.path.join(HERE, "cells")
REL = "figures/showcase/cells"

CURRENT = [("Real room", [("realb_02920", (80, 0, 878, 532)), ("realb_03000", (40, 0, 838, 532))]),
           ("Sim.\\ apartment", [("sim_02850", (0, 14, 680, 467)), ("sim_00400", (0, 27, 680, 480))]),
           ("Flat", [("flat_00228", (0, 53, 640, 480)), ("flat_00218", (0, 40, 640, 467))])]
COLS = [("rgb", False), ("khronos", False), ("panoptic", False), ("ours_tsdf", True), ("game", False),
        ("ours_gs", True), ("wavemap", False), ("ours_occ", True)]
MOMENTS = [("t1_visit1_118.8s", "1st visit, 118.8\\,s", "before the change"),
           ("t2_visit1_139.5s", "1st visit, 139.5\\,s", "a chair moved out of view"),
           ("t3_visit2_108.0s", "2nd visit, 108.0\\,s", "after the changes between visits")]
HROWS = [("gt", "Ground truth", "gtblue", False), ("khronos_snapshot", "Khronos", "black", False),
         ("ours_tsdf", "Ours (TSDF)", "oursgold", True), ("ours_gs_round", "Ours (Gaussians)", "oursgold", True)]
HBOX = (0, 30, 680, 370)

HEAD = r"""\providecolor{oursgold}{HTML}{BF9000}\providecolor{gtblue}{HTML}{2E75B6}\providecolor{timepurple}{HTML}{7030A0}
\ifdefined\shw\else\newlength{\shw}\newlength{\shh}\fi
"""


def save(src, box, name):
    Image.open(src).convert("RGB").crop(box).save(os.path.join(CELLS, name), quality=92)
    return f"{REL}/{name}"


def cell(path, ours):
    img = f"\\includegraphics[width=\\shw]{{{path}}}" if not ours else \
        f"{{\\setlength{{\\fboxsep}}{{0pt}}\\setlength{{\\fboxrule}}{{0.8pt}}\\fcolorbox{{oursgold}}{{white}}" \
        f"{{\\includegraphics[width=\\dimexpr\\shw-1.6pt\\relax]{{{path}}}}}}}"
    return img


def current():
    out = [HEAD, r"\begin{figure*}[t]", r"\centering\footnotesize",
           r"\setlength{\shw}{0.1165\textwidth}\setlength{\shh}{0.0777\textwidth}",
           r"\setlength{\tabcolsep}{0.6pt}\renewcommand{\arraystretch}{0}",
           r"\begin{tabular}{@{}c@{\hspace{3pt}}cccccccc@{}}",
           r" & & \multicolumn{3}{c}{\textit{TSDF}} & \multicolumn{2}{c}{\textit{3D Gaussians}} & "
           r"\multicolumn{2}{c}{\textit{Occupancy}} \\[2pt]",
           r"\cmidrule(lr){3-5}\cmidrule(lr){6-7}\cmidrule(l){8-9}\noalign{\vskip 2pt}",
           r" & Image & Khronos & Panoptic & \textcolor{oursgold}{\textbf{Ours}} & GaME & "
           r"\textcolor{oursgold}{\textbf{Ours}} & wavemap & \textcolor{oursgold}{\textbf{Ours}} \\[3pt]"]
    for d, (label, views) in enumerate(CURRENT):
        for i, (key, box) in enumerate(views):
            row = []
            if i == 0:
                row.append(f"\\raisebox{{-\\dimexpr\\shh+0.6pt\\relax}}[0pt][0pt]{{\\rotatebox{{90}}"
                           f"{{\\makebox[\\dimexpr2\\shh+1.2pt\\relax][c]{{{label}}}}}}}")
            else:
                row.append("")
            for m, ours in COLS:
                row.append(cell(save(f"{M}/current_maps/{key}_{m}.png", box, f"{key}_{m}.jpg"), ours))
            gap = "1.2pt" if i == 0 else ("4pt" if d < len(CURRENT) - 1 else "0pt")
            out.append(" & ".join(row) + f" \\\\[{gap}]")
    out += [r"\end{tabular}",
            r"\caption{Current maps at held-out views, two per dataset: the real room after its second visit, and the simulated",
            r"apartment and Flat after their second.}",
            r"\label{fig:supp_current}", r"\end{figure*}"]
    open(os.path.join(HERE, "current.tex"), "w").write("\n".join(out) + "\n")


def history():
    out = [HEAD, r"\begin{figure*}[t]", r"\centering\footnotesize",
           r"\setlength{\shw}{0.29\textwidth}",
           r"\setlength{\tabcolsep}{0.8pt}\renewcommand{\arraystretch}{0}",
           r"\begin{tabular}{@{}r@{\hspace{4pt}}ccc@{}}"]
    head = [""] + [f"\\shortstack{{\\textcolor{{timepurple}}{{{h}}}\\\\[1pt]\\textit{{\\color{{gray}}{n}}}}}"
                   for _, h, n in MOMENTS]
    out.append(" & ".join(head) + r" \\[4pt]")
    for r, (key, label, color, ours) in enumerate(HROWS):
        lab = f"\\textcolor{{{color}}}{{{'\\textbf{' + label + '}' if ours else label}}}"
        row = [f"\\raisebox{{0.5\\dimexpr0.5\\shw\\relax}}{{{lab}}}"]
        for tag, _, _ in MOMENTS:
            src = f"{M}/history_4d/sim_03560_{tag}_{key}.png"
            if key == "gt" and tag.startswith("t2"):
                src = f"{M}/history_4d/sim_03560_t2_visit1_139.5s_gt_from129.6s.png"
            row.append(cell(save(src, HBOX, f"hist_{tag[:2]}_{key}.jpg"), ours))
        out.append(" & ".join(row) + (r" \\[1.5pt]" if r < len(HROWS) - 1 else r" \\"))
    out += [r"\end{tabular}",
            r"\caption{The map of three moments at one pose of the simulated apartment: ground truth, Khronos, and our TSDF and",
            r"Gaussian maps.}",
            r"\label{fig:supp_history}", r"\end{figure*}"]
    open(os.path.join(HERE, "history.tex"), "w").write("\n".join(out) + "\n")


if __name__ == "__main__":
    os.makedirs(CELLS, exist_ok=True)
    current()
    history()
    print(len(os.listdir(CELLS)), "cells")
