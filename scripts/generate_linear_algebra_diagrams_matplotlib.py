from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Ellipse


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "diagrams"
OUT_DIR.mkdir(parents=True, exist_ok=True)

BG = "#f7f1e8"
CARD = "#fffdf9"
SUB = "#fbf2e8"
LINE = "#d7c7b6"
TEAL = "#2f665f"
ACCENT = "#cc6732"
DEEP = "#943e1d"

plt.rcParams["font.family"] = ["DejaVu Sans", "sans-serif"]
plt.rcParams["axes.unicode_minus"] = False


def rounded(ax, xy, wh, fc, ec=LINE, lw=1.4, r=0.03, z=1):
    patch = FancyBboxPatch(
        xy,
        wh[0],
        wh[1],
        boxstyle=f"round,pad=0.012,rounding_size={r}",
        linewidth=lw,
        edgecolor=ec,
        facecolor=fc,
        transform=ax.transAxes,
        zorder=z,
    )
    ax.add_patch(patch)


def draw_xy(ax):
    ax.set_xlim(-1.45, 1.45)
    ax.set_ylim(-1.0, 1.0)
    ax.axis("off")
    ax.set_aspect("equal")
    ax.plot([-1.25, 1.25], [0, 0], color=LINE, lw=2.2, zorder=1)
    ax.plot([0, 0], [-0.8, 0.8], color=LINE, lw=2.2, zorder=1)
    ax.scatter([0], [0], s=36, color=ACCENT, zorder=4)


def eigenvectors():
    fig = plt.figure(figsize=(14, 5.6), dpi=220, facecolor=BG)
    canvas = fig.add_axes([0, 0, 1, 1])
    canvas.axis("off")
    rounded(canvas, (0.035, 0.08), (0.93, 0.84), CARD, ec="#e4d5c6", lw=1.6, r=0.045)
    rounded(canvas, (0.09, 0.17), (0.385, 0.66), SUB, r=0.035)
    rounded(canvas, (0.525, 0.17), (0.385, 0.66), SUB, r=0.035)

    left = fig.add_axes([0.125, 0.24, 0.315, 0.52], facecolor="none")
    right = fig.add_axes([0.56, 0.24, 0.315, 0.52], facecolor="none")

    draw_xy(left)
    x_end = (-0.52, 0.45)
    ax_end = (0.96, 0.58)
    left.add_patch(FancyArrowPatch((0, 0), x_end, arrowstyle="-|>", mutation_scale=22, lw=5, color=TEAL, zorder=6))
    left.add_patch(FancyArrowPatch((0, 0), ax_end, arrowstyle="-|>", mutation_scale=22, lw=5, color=ACCENT, zorder=6))
    left.text(x_end[0] - 0.02, x_end[1] + 0.08, "x", color=TEAL, fontsize=17, weight="bold")
    left.text(ax_end[0] + 0.03, ax_end[1] + 0.06, "Ax", color=ACCENT, fontsize=17, weight="bold")

    draw_xy(right)
    right.plot([-1.05, 1.05], [0, 0], color="#e9b895", lw=8, alpha=0.55, solid_capstyle="round", zorder=2)
    x_end2 = (-0.62, 0.00)
    ax_end2 = (0.98, 0.00)
    right.add_patch(FancyArrowPatch((0, 0), x_end2, arrowstyle="-|>", mutation_scale=22, lw=5, color=TEAL, zorder=6))
    right.add_patch(FancyArrowPatch((0, 0), ax_end2, arrowstyle="-|>", mutation_scale=22, lw=5, color=ACCENT, zorder=6))
    right.text(x_end2[0] - 0.02, x_end2[1] + 0.08, "x", color=TEAL, fontsize=17, weight="bold")
    right.text(ax_end2[0] + 0.03, ax_end2[1] + 0.06, r"$Ax=\lambda x$", color=ACCENT, fontsize=17, weight="bold")

    out = OUT_DIR / "eigenvectors-matplotlib.png"
    fig.savefig(out, dpi=220, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    return out


def diagonalization():
    fig = plt.figure(figsize=(14, 3.6), dpi=220, facecolor=BG)
    canvas = fig.add_axes([0, 0, 1, 1])
    canvas.axis("off")
    rounded(canvas, (0.03, 0.12), (0.94, 0.76), CARD, ec="#e4d5c6", lw=1.6, r=0.05)

    boxes = [
        (0.09, 0.30, 0.18, 0.40, "#efe6dc"),
        (0.39, 0.30, 0.22, 0.40, "#f3e2d5"),
        (0.72, 0.30, 0.18, 0.40, "#e8efe9"),
    ]
    for x, y, w, h, c in boxes:
        rounded(canvas, (x, y), (w, h), c, r=0.04)

    canvas.text(0.16, 0.50, "A", color=DEEP, fontsize=34, weight="bold", ha="center")
    canvas.text(0.50, 0.50, "PΛP⁻¹", color=ACCENT, fontsize=34, weight="bold", ha="center")
    canvas.text(0.81, 0.50, "Aⁿ", color=TEAL, fontsize=34, weight="bold", ha="center")

    canvas.add_patch(FancyArrowPatch((0.27, 0.50), (0.39, 0.50), arrowstyle="-|>", mutation_scale=28, lw=4, color=ACCENT, transform=canvas.transAxes))
    canvas.add_patch(FancyArrowPatch((0.61, 0.50), (0.72, 0.50), arrowstyle="-|>", mutation_scale=28, lw=4, color=TEAL, transform=canvas.transAxes))

    out = OUT_DIR / "diagonalization-matplotlib.png"
    fig.savefig(out, dpi=220, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    return out


def svd():
    fig = plt.figure(figsize=(14, 3.8), dpi=220, facecolor=BG)
    canvas = fig.add_axes([0, 0, 1, 1])
    canvas.set_xlim(0, 1)
    canvas.set_ylim(0, 1)
    canvas.axis("off")
    rounded(canvas, (0.03, 0.11), (0.94, 0.78), CARD, ec="#e4d5c6", lw=1.6, r=0.05)

    rail_y = 0.50
    canvas.plot([0.09, 0.91], [rail_y, rail_y], color=LINE, lw=3.0)

    nodes = [(0.18, "Vt", TEAL), (0.50, "Sigma", ACCENT), (0.82, "U", DEEP)]
    for x, label, color in nodes:
        rounded(canvas, (x - 0.07, 0.35), (0.14, 0.30), "#f6ecdf", r=0.08)
        canvas.text(x, 0.50, label, color=color, fontsize=34, weight="bold", ha="center", va="center")

    canvas.add_patch(FancyArrowPatch((0.25, rail_y), (0.43, rail_y), arrowstyle="-|>", mutation_scale=26, lw=4, color=ACCENT))
    canvas.add_patch(FancyArrowPatch((0.57, rail_y), (0.75, rail_y), arrowstyle="-|>", mutation_scale=26, lw=4, color=TEAL))

    out = OUT_DIR / "svd-matplotlib.png"
    fig.savefig(out, dpi=220, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    return out


def pca():
    fig = plt.figure(figsize=(14, 4.6), dpi=220, facecolor=BG)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis("off")
    rounded(ax, (0.03, 0.08), (0.94, 0.84), CARD, ec="#e4d5c6", lw=1.6, r=0.05)

    plot = fig.add_axes([0.12, 0.18, 0.76, 0.62], facecolor=SUB)
    plot.set_xlim(-3.4, 3.4)
    plot.set_ylim(-2.5, 2.5)
    plot.axis("off")

    rng = np.random.default_rng(42)
    cov = np.array([[2.0, 1.25], [1.25, 1.0]])
    pts = rng.multivariate_normal([0, 0], cov, size=180)
    plot.scatter(pts[:, 0], pts[:, 1], s=20, color="#cf7a49", alpha=0.25, edgecolors="none")

    plot.add_patch(Ellipse((0, 0), width=4.8, height=1.6, angle=33, facecolor="#e8b08d", alpha=0.25, edgecolor="none"))
    plot.add_patch(FancyArrowPatch((0, 0), (2.3, 1.5), arrowstyle="-|>", mutation_scale=24, lw=5, color=ACCENT))
    plot.add_patch(FancyArrowPatch((0, 0), (-0.9, 1.4), arrowstyle="-|>", mutation_scale=24, lw=4, color=TEAL))
    plot.text(2.38, 1.56, "PC1", color=ACCENT, fontsize=20, weight="bold")
    plot.text(-1.05, 1.48, "PC2", color=TEAL, fontsize=18, weight="bold")

    out = OUT_DIR / "pca-matplotlib.png"
    fig.savefig(out, dpi=220, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    return out


if __name__ == "__main__":
    for p in (eigenvectors(), diagonalization(), svd(), pca()):
        print(p)
