from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "diagrams" / "eigenvectors-matplotlib.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

BG = "#f7f1e8"
CARD = "#fffdf9"
SUB = "#fbf2e8"
LINE = "#d8c8b8"
TEXT = "#1f1a17"
MUTED = "#6a5e54"
ACCENT = "#cc6732"
ACCENT_DEEP = "#943e1d"
TEAL = "#2f665f"

plt.rcParams["font.family"] = ["Malgun Gothic", "DejaVu Sans", "sans-serif"]
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
    return patch


def axis_with_vectors(ax, eigen=False):
    ax.set_xlim(-1.5, 1.7)
    ax.set_ylim(-1.0, 1.2)
    ax.axis("off")
    ax.plot([-1.25, 1.45], [0, 0], color=LINE, lw=2, zorder=1)
    ax.plot([0, 0], [-0.8, 1.0], color=LINE, lw=2, zorder=1)
    ax.scatter([0], [0], s=40, color=ACCENT_DEEP, zorder=5)

    if eigen:
        ax.plot([-1.1, 1.35], [0, 0], color="#e8b08d", lw=6, alpha=0.6, solid_capstyle="round", zorder=2)
        x_end = (-0.65, 0.0)
        ax_end = (1.1, 0.0)
        ax_label = "Ax = λx"
    else:
        x_end = (-0.75, 0.62)
        ax_end = (1.15, 0.82)
        ax_label = "Ax"

    ax.add_patch(FancyArrowPatch((0, 0), x_end, arrowstyle="-|>", mutation_scale=26, lw=5, color=TEAL, zorder=6))
    ax.add_patch(FancyArrowPatch((0, 0), ax_end, arrowstyle="-|>", mutation_scale=26, lw=5, color=ACCENT, zorder=6))
    ax.text(x_end[0] - 0.02, x_end[1] + 0.07, "x", color=TEAL, fontsize=18, weight="bold")
    ax.text(ax_end[0] + 0.02, ax_end[1] + 0.06, ax_label, color=ACCENT, fontsize=18, weight="bold")


def build():
    fig = plt.figure(figsize=(16, 9), dpi=170, facecolor=BG)
    canvas = fig.add_axes([0, 0, 1, 1])
    canvas.axis("off")

    rounded(canvas, (0.04, 0.06), (0.92, 0.86), CARD, ec="#e5d6c8", lw=1.6, r=0.04, z=1)
    canvas.text(0.09, 0.86, "LINEAR ALGEBRA VISUAL NOTE", fontsize=18, weight="bold", color=ACCENT_DEEP)
    canvas.text(0.09, 0.80, "고유벡터와 고유값 한눈에 보기", fontsize=34, weight="bold", color=TEXT)
    canvas.text(0.09, 0.74, '핵심: "방향이 안 바뀜"보다 "같은 직선 위에 남음"', fontsize=21, color=MUTED)

    rounded(canvas, (0.10, 0.24), (0.39, 0.42), SUB, r=0.03)
    rounded(canvas, (0.51, 0.24), (0.39, 0.42), SUB, r=0.03)

    rounded(canvas, (0.11, 0.615), (0.10, 0.035), TEAL, ec=TEAL, lw=0, r=0.02)
    rounded(canvas, (0.52, 0.615), (0.10, 0.035), ACCENT, ec=ACCENT, lw=0, r=0.02)
    canvas.text(0.137, 0.621, "일반 벡터", fontsize=14, weight="bold", color="#fff9f3")
    canvas.text(0.547, 0.621, "고유벡터", fontsize=14, weight="bold", color="#fff9f3")

    canvas.text(0.11, 0.55, "대체로 방향도 바뀐다", fontsize=28, weight="bold", color=TEXT)
    canvas.text(0.11, 0.515, "행렬 적용 후 원래 선에서 벗어남", fontsize=17, color=MUTED)
    canvas.text(0.52, 0.55, "같은 선 위에 남는다", fontsize=28, weight="bold", color=TEXT)
    canvas.text(0.52, 0.515, "부호가 바뀌면 반대 방향일 수 있음", fontsize=17, color=MUTED)

    left_plot = fig.add_axes([0.13, 0.29, 0.33, 0.18], facecolor="#fffaf4")
    right_plot = fig.add_axes([0.54, 0.29, 0.33, 0.18], facecolor="#fffaf4")
    axis_with_vectors(left_plot, eigen=False)
    axis_with_vectors(right_plot, eigen=True)

    rounded(canvas, (0.11, 0.23), (0.35, 0.04), "#d7e6e2", ec="#d7e6e2", lw=0, r=0.02)
    rounded(canvas, (0.52, 0.23), (0.35, 0.04), "#f5dfd0", ec="#f5dfd0", lw=0, r=0.02)
    canvas.text(0.18, 0.238, "x와 Ax는 서로 다른 직선", fontsize=16, weight="bold", color=TEAL)
    canvas.text(0.58, 0.238, "같은 직선 + 길이(배율)만 변화", fontsize=16, weight="bold", color=ACCENT_DEEP)

    rounded(canvas, (0.09, 0.08), (0.82, 0.07), "#fff2e8", ec="#ead4c2", lw=1.2, r=0.03)
    canvas.text(0.16, 0.105, "면접 한 줄:", fontsize=20, weight="bold", color=ACCENT_DEEP)
    canvas.text(0.30, 0.105, "고유벡터는 같은 직선 위에 남는 벡터, 고유값은 그때의 배율.", fontsize=20, color=TEXT)

    fig.savefig(OUT, dpi=170, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    return OUT


if __name__ == "__main__":
    print(build())
