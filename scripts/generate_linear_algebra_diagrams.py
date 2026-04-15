from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "diagrams"
OUT_DIR.mkdir(parents=True, exist_ok=True)


BG = "#fff8f1"
PANEL = "#fffdf9"
SUBPANEL = "#fbf1e4"
LINE = "#e4d2bf"
TEXT = "#1f1a17"
MUTED = "#675e57"
ACCENT = "#c65d2e"
DEEP = "#8e3513"
TEAL = "#2f5d56"
SOFT = "#f2e3d5"


plt.rcParams["font.family"] = ["Malgun Gothic", "DejaVu Sans", "sans-serif"]
plt.rcParams["axes.unicode_minus"] = False


def rounded_panel(ax, xy, width, height, radius=0.04, fc=PANEL, ec=LINE, lw=1.4):
    patch = FancyBboxPatch(
        xy,
        width,
        height,
        boxstyle=f"round,pad=0.012,rounding_size={radius}",
        linewidth=lw,
        facecolor=fc,
        edgecolor=ec,
        transform=ax.transAxes,
        clip_on=False,
        zorder=0,
    )
    ax.add_patch(patch)
    return patch


def draw_vector_axes(ax, mode="generic"):
    ax.set_xlim(-1.4, 1.8)
    ax.set_ylim(-1.1, 1.3)
    ax.set_aspect("equal")
    ax.axis("off")

    ax.plot([-1.2, 1.55], [0, 0], color="#d4c2af", lw=1.5, zorder=1)
    ax.plot([0, 0], [-0.9, 1.1], color="#d4c2af", lw=1.5, zorder=1)
    ax.scatter([0], [0], s=28, color=DEEP, zorder=5)

    if mode == "generic":
      x_end = (-0.65, 0.52)
      ax_end = (1.0, 0.74)
    else:
      x_end = (-0.7, 0.0)
      ax_end = (1.15, 0.0)
      ax.plot([-1.0, 1.35], [0, 0], color="#e0a284", lw=4.5, solid_capstyle="round", zorder=2)

    ax.annotate("", xy=x_end, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", lw=4.5, color=TEAL), zorder=6)
    ax.annotate("", xy=ax_end, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", lw=4.5, color=ACCENT), zorder=6)
    ax.text(x_end[0] - 0.05, x_end[1] + 0.08, "x", color=TEAL, fontsize=14, fontweight="bold")
    label = "Ax" if mode == "generic" else r"$Ax=\lambda x$"
    ax.text(ax_end[0] + 0.03, ax_end[1] + 0.08, label, color=ACCENT, fontsize=14, fontweight="bold")


def generate_eigenvectors():
    fig = plt.figure(figsize=(12, 7), facecolor=BG)
    canvas = fig.add_axes([0, 0, 1, 1])
    canvas.set_axis_off()

    rounded_panel(canvas, (0.035, 0.055), 0.93, 0.87, radius=0.03, fc=PANEL, ec="#eadbca", lw=1.2)
    canvas.text(0.06, 0.9, "LINEAR ALGEBRA VISUAL NOTE", fontsize=16, fontweight="bold", color=DEEP)
    canvas.text(0.06, 0.845, "고유벡터와 고유값을 그림으로 이해하기", fontsize=28, fontweight="bold", color=TEXT)
    canvas.text(0.06, 0.8, '핵심은 "방향이 안 바뀐다"보다 "같은 직선 위에 남는다"이다.', fontsize=15, color=MUTED)

    left = fig.add_axes([0.08, 0.23, 0.37, 0.48], facecolor="none")
    right = fig.add_axes([0.55, 0.23, 0.37, 0.48], facecolor="none")
    for ax in (left, right):
        rounded_panel(ax, (0, 0), 1, 1, radius=0.04, fc=SUBPANEL, ec=LINE)
        ax.set_axis_off()

    left.text(0.06, 0.9, "일반 벡터", fontsize=18, fontweight="bold", color=TEAL, transform=left.transAxes)
    left.text(0.06, 0.82, "행렬을 곱하면 방향과 크기가 함께 바뀜", fontsize=12.5, color=MUTED, transform=left.transAxes)
    left_plot = fig.add_axes([0.128, 0.325, 0.26, 0.23], facecolor="#fff8f0")
    draw_vector_axes(left_plot, "generic")
    left.text(0.06, 0.12, "핵심", fontsize=12.5, fontweight="bold", color=DEEP, transform=left.transAxes)
    left.text(0.16, 0.12, "x와 Ax가 서로 다른 직선 위에 있다.", fontsize=12.5, color=MUTED, transform=left.transAxes)

    right.text(0.06, 0.9, "고유벡터", fontsize=18, fontweight="bold", color=ACCENT, transform=right.transAxes)
    right.text(0.06, 0.82, "변환 후에도 같은 직선 위에 남고 배율만 달라짐", fontsize=12.5, color=MUTED, transform=right.transAxes)
    right_plot = fig.add_axes([0.598, 0.325, 0.26, 0.23], facecolor="#fff8f0")
    draw_vector_axes(right_plot, "eigen")
    right.text(0.06, 0.12, "핵심", fontsize=12.5, fontweight="bold", color=DEEP, transform=right.transAxes)
    right.text(0.16, 0.12, "고유벡터는 같은 직선 위에 남고, 고유값은 그 배율이다.", fontsize=12.5, color=MUTED, transform=right.transAxes)

    bar = FancyBboxPatch(
        (0.06, 0.09),
        0.88,
        0.055,
        boxstyle="round,pad=0.008,rounding_size=0.02",
        facecolor=SOFT,
        edgecolor="none",
        transform=canvas.transAxes,
    )
    canvas.add_patch(bar)
    canvas.text(0.075, 0.106, "면접용 핵심 문장", fontsize=13.5, fontweight="bold", color=DEEP)
    canvas.text(0.2, 0.106, "고유벡터는 변환 후에도 같은 직선 위에 남는 벡터이고, 고유값은 그때의 배율이다.", fontsize=13.2, color=MUTED)

    out = OUT_DIR / "eigenvectors.svg"
    fig.savefig(out, format="svg", bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    return out


if __name__ == "__main__":
    generated = [generate_eigenvectors()]
    for path in generated:
        print(path)
