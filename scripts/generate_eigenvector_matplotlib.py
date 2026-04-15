from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "diagrams" / "eigenvectors-matplotlib.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

BG = "#f7f1e8"
CARD = "#fffdf9"
SUB = "#fbf2e8"
LINE = "#d7c7b6"
TEAL = "#2f665f"
ACCENT = "#cc6732"

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


def draw_axes(ax, eigen=False):
    ax.set_xlim(-1.45, 1.45)
    ax.set_ylim(-0.95, 0.95)
    ax.set_aspect("equal")
    ax.axis("off")

    ax.plot([-1.25, 1.25], [0, 0], color=LINE, lw=2.2, zorder=1)
    ax.plot([0, 0], [-0.75, 0.75], color=LINE, lw=2.2, zorder=1)
    ax.scatter([0], [0], s=38, color=ACCENT, zorder=5)

    if eigen:
        ax.plot([-1.05, 1.05], [0, 0], color="#e9b895", lw=8, alpha=0.55, solid_capstyle="round", zorder=2)
        x_end = (-0.62, 0.00)
        ax_end = (0.98, 0.00)
        ax_label = r"$Ax=\lambda x$"
    else:
        x_end = (-0.52, 0.45)
        ax_end = (0.96, 0.58)
        ax_label = "Ax"

    ax.add_patch(FancyArrowPatch((0, 0), x_end, arrowstyle="-|>", mutation_scale=22, lw=5, color=TEAL, zorder=6))
    ax.add_patch(FancyArrowPatch((0, 0), ax_end, arrowstyle="-|>", mutation_scale=22, lw=5, color=ACCENT, zorder=6))
    ax.text(x_end[0] - 0.02, x_end[1] + 0.08, "x", color=TEAL, fontsize=17, weight="bold")
    ax.text(ax_end[0] + 0.03, ax_end[1] + 0.06, ax_label, color=ACCENT, fontsize=17, weight="bold")


def build():
    fig = plt.figure(figsize=(14, 5.6), dpi=220, facecolor=BG)
    canvas = fig.add_axes([0, 0, 1, 1])
    canvas.axis("off")

    rounded(canvas, (0.035, 0.08), (0.93, 0.84), CARD, ec="#e4d5c6", lw=1.6, r=0.045)
    rounded(canvas, (0.09, 0.17), (0.385, 0.66), SUB, r=0.035)
    rounded(canvas, (0.525, 0.17), (0.385, 0.66), SUB, r=0.035)

    left = fig.add_axes([0.125, 0.24, 0.315, 0.52], facecolor="none")
    right = fig.add_axes([0.56, 0.24, 0.315, 0.52], facecolor="none")
    draw_axes(left, eigen=False)
    draw_axes(right, eigen=True)

    fig.savefig(OUT, dpi=220, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    return OUT


if __name__ == "__main__":
    print(build())
