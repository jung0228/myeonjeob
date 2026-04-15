from manim import *


config.pixel_width = 1920
config.pixel_height = 1080
config.frame_width = 14.222
config.frame_height = 8.0

BG = "#F7F0E7"
CARD = "#FFFDF9"
CARD_WARM = "#FBF2E8"
LINE = "#DCC9B8"
TEXT = "#1F1A17"
MUTED = "#6A5E54"
ACCENT = "#CC6732"
ACCENT_DEEP = "#943E1D"
TEAL = "#2F665F"
TEAL_SOFT = "#DCEDEA"
ORANGE_SOFT = "#F8E4D7"
GOLD = "#E8C36A"
FONT = "Malgun Gothic"


def soft_card(width, height, fill, stroke=LINE, radius=0.24, stroke_width=1.6):
    shadow = RoundedRectangle(
        width=width,
        height=height,
        corner_radius=radius,
        fill_color="#EADBCF",
        fill_opacity=0.45,
        stroke_width=0,
    ).shift(DOWN * 0.08 + RIGHT * 0.08)
    card = RoundedRectangle(
        width=width,
        height=height,
        corner_radius=radius,
        fill_color=fill,
        fill_opacity=1,
        stroke_color=stroke,
        stroke_width=stroke_width,
    )
    return VGroup(shadow, card)


class EigenvectorCard(Scene):
    def construct(self):
        self.camera.background_color = BG

        frame = RoundedRectangle(
            width=13.35,
            height=7.35,
            corner_radius=0.34,
            fill_color=CARD,
            fill_opacity=1,
            stroke_color="#E7D7C8",
            stroke_width=1.4,
        )

        halo_left = Circle(radius=1.65, stroke_width=0, fill_color="#F5E5D8", fill_opacity=0.85)
        halo_left.move_to(frame.get_corner(UL) + RIGHT * 1.2 + DOWN * 1.15)
        halo_right = Circle(radius=1.25, stroke_width=0, fill_color="#E3F0EC", fill_opacity=0.8)
        halo_right.move_to(frame.get_corner(UR) + LEFT * 1.25 + DOWN * 1.25)

        eyebrow = Text(
            "LINEAR ALGEBRA VISUAL NOTE",
            font=FONT,
            weight=BOLD,
            font_size=18,
            color=ACCENT_DEEP,
        )
        eyebrow.move_to(frame.get_top() + DOWN * 0.55 + LEFT * 3.75)

        title = Text(
            "고유벡터와 고유값의 핵심",
            font=FONT,
            weight=BOLD,
            font_size=31,
            color=TEXT,
        )
        title.next_to(eyebrow, DOWN, aligned_edge=LEFT, buff=0.16)

        subtitle = Text(
            '핵심은 "방향이 안 바뀐다"보다 "같은 직선 위에 남는다"이다.',
            font=FONT,
            font_size=16,
            color=MUTED,
        )
        subtitle.next_to(title, DOWN, aligned_edge=LEFT, buff=0.14)

        left = self._build_generic_panel()
        right = self._build_eigen_panel()
        left.move_to(frame.get_center() + LEFT * 3.1 + DOWN * 0.45)
        right.move_to(frame.get_center() + RIGHT * 3.1 + DOWN * 0.45)

        connector = Text(
            "같은 행렬이라도 어떤 벡터는 완전히 꺾이고,\n어떤 벡터는 같은 축 위에서 배율만 달라진다.",
            font=FONT,
            font_size=15,
            line_spacing=0.88,
            color=MUTED,
        )
        connector.move_to(frame.get_bottom() + UP * 0.86)

        callout = soft_card(11.8, 0.78, "#FFF5EB")
        callout.move_to(frame.get_bottom() + UP * 0.42)
        callout_title = Text(
            "면접용 핵심 문장",
            font=FONT,
            weight=BOLD,
            font_size=15,
            color=ACCENT_DEEP,
        )
        callout_body = Text(
            "고유벡터는 변환 후에도 같은 직선 위에 남는 벡터이고, 고유값은 그때의 배율이다.",
            font=FONT,
            font_size=14,
            color=TEXT,
        )
        callout_group = VGroup(callout_title, callout_body).arrange(RIGHT, buff=0.26)
        callout_group.move_to(callout)

        self.add(
            halo_left,
            halo_right,
            frame,
            eyebrow,
            title,
            subtitle,
            left,
            right,
            connector,
            callout,
            callout_group,
        )

    def _panel_shell(self, accent_fill, accent_text, heading, summary):
        shell = soft_card(5.75, 3.8, CARD_WARM)
        label_box = RoundedRectangle(
            width=1.76,
            height=0.42,
            corner_radius=0.21,
            fill_color=accent_fill,
            fill_opacity=1,
            stroke_width=0,
        )
        label_text = Text(
            accent_text,
            font=FONT,
            weight=BOLD,
            font_size=15,
            color="#FFF9F3",
        ).move_to(label_box)
        label = VGroup(label_box, label_text)
        label.move_to(shell.get_top() + DOWN * 0.32 + LEFT * 1.55)

        heading_text = Text(
            heading,
            font=FONT,
            weight=BOLD,
            font_size=23,
            color=TEXT,
        )
        heading_text.next_to(label, DOWN, aligned_edge=LEFT, buff=0.18)

        summary_text = Text(
            summary,
            font=FONT,
            font_size=13,
            color=MUTED,
        )
        summary_text.next_to(heading_text, DOWN, aligned_edge=LEFT, buff=0.12)

        return shell, label, heading_text, summary_text

    def _build_generic_panel(self):
        shell, label, heading, summary = self._panel_shell(
            accent_fill=TEAL,
            accent_text="일반 벡터",
            heading="행렬을 곱하면\n대체로 방향도 바뀐다",
            summary="대부분의 벡터는 원래 직선에서 벗어난다.",
        )

        graph = RoundedRectangle(
            width=4.8,
            height=1.72,
            corner_radius=0.2,
            fill_color=CARD,
            fill_opacity=1,
            stroke_color=LINE,
            stroke_width=1.2,
        )
        graph.move_to(shell.get_center() + DOWN * 0.62)

        h = Line(
            graph.get_left() + RIGHT * 0.3,
            graph.get_right() + LEFT * 0.3,
            stroke_color="#D8C8B8",
            stroke_width=2,
        ).move_to(graph.get_center())
        v = Line(
            graph.get_top() + DOWN * 0.18,
            graph.get_bottom() + UP * 0.18,
            stroke_color="#D8C8B8",
            stroke_width=2,
        ).move_to(graph.get_center())

        origin = Dot(graph.get_center(), radius=0.055, color=ACCENT_DEEP)
        x_end = origin.get_center() + LEFT * 1.05 + UP * 0.75
        ax_end = origin.get_center() + RIGHT * 1.45 + UP * 0.86
        x_arrow = Arrow(origin.get_center(), x_end, buff=0, stroke_width=6, color=TEAL)
        ax_arrow = Arrow(origin.get_center(), ax_end, buff=0, stroke_width=6, color=ACCENT)

        x_label = Text("x", font=FONT, weight=BOLD, font_size=15, color=TEAL).next_to(x_arrow.get_end(), UP, buff=0.04)
        ax_label = Text("Ax", font=FONT, weight=BOLD, font_size=15, color=ACCENT).next_to(ax_arrow.get_end(), UR, buff=0.04)

        note_bar = RoundedRectangle(
            width=4.8,
            height=0.52,
            corner_radius=0.18,
            fill_color=TEAL_SOFT,
            fill_opacity=1,
            stroke_width=0,
        )
        note_bar.move_to(shell.get_bottom() + UP * 0.34)
        note_text = Text(
            "x와 Ax가 서로 다른 직선 위에 있다.",
            font=FONT,
            weight=BOLD,
            font_size=13,
            color=TEAL,
        ).move_to(note_bar)

        return VGroup(shell, label, heading, summary, graph, h, v, origin, x_arrow, ax_arrow, x_label, ax_label, note_bar, note_text)

    def _build_eigen_panel(self):
        shell, label, heading, summary = self._panel_shell(
            accent_fill=ACCENT,
            accent_text="고유벡터",
            heading="변환 후에도\n같은 직선 위에 남는다",
            summary="음수라면 반대 방향일 수 있지만 같은 span은 유지된다.",
        )

        graph = RoundedRectangle(
            width=4.8,
            height=1.72,
            corner_radius=0.2,
            fill_color=CARD,
            fill_opacity=1,
            stroke_color=LINE,
            stroke_width=1.2,
        )
        graph.move_to(shell.get_center() + DOWN * 0.62)

        h = Line(
            graph.get_left() + RIGHT * 0.3,
            graph.get_right() + LEFT * 0.3,
            stroke_color="#D8C8B8",
            stroke_width=2,
        ).move_to(graph.get_center())
        v = Line(
            graph.get_top() + DOWN * 0.18,
            graph.get_bottom() + UP * 0.18,
            stroke_color="#D8C8B8",
            stroke_width=2,
        ).move_to(graph.get_center())

        axis = Line(
            graph.get_left() + RIGHT * 0.42,
            graph.get_right() + LEFT * 0.42,
            stroke_color="#E8AF8B",
            stroke_width=5,
        ).move_to(graph.get_center())
        axis_glow = RoundedRectangle(
            width=4.42,
            height=0.36,
            corner_radius=0.18,
            fill_color=ORANGE_SOFT,
            fill_opacity=0.9,
            stroke_width=0,
        ).move_to(graph.get_center())

        origin = Dot(graph.get_center(), radius=0.055, color=ACCENT_DEEP)
        x_end = origin.get_center() + LEFT * 1.0
        ax_end = origin.get_center() + RIGHT * 1.52
        x_arrow = Arrow(origin.get_center(), x_end, buff=0, stroke_width=6, color=TEAL)
        ax_arrow = Arrow(origin.get_center(), ax_end, buff=0, stroke_width=6, color=ACCENT)

        x_label = Text("x", font=FONT, weight=BOLD, font_size=15, color=TEAL).next_to(x_arrow.get_end(), UP, buff=0.04)
        ax_label = Text("Ax = λx", font=FONT, weight=BOLD, font_size=15, color=ACCENT).next_to(ax_arrow.get_end(), UP, buff=0.04)

        note_bar = RoundedRectangle(
            width=4.8,
            height=0.52,
            corner_radius=0.18,
            fill_color=ORANGE_SOFT,
            fill_opacity=1,
            stroke_width=0,
        )
        note_bar.move_to(shell.get_bottom() + UP * 0.34)
        note_text = Text(
            "같은 선 위에 남고, 길이만 배율로 바뀐다.",
            font=FONT,
            weight=BOLD,
            font_size=13,
            color=ACCENT_DEEP,
        ).move_to(note_bar)

        star = Star(
            n=5,
            outer_radius=0.12,
            fill_color=GOLD,
            fill_opacity=1,
            stroke_width=0,
        ).move_to(graph.get_corner(UR) + LEFT * 0.28 + DOWN * 0.26)

        return VGroup(
            shell,
            label,
            heading,
            summary,
            graph,
            axis_glow,
            h,
            v,
            axis,
            origin,
            x_arrow,
            ax_arrow,
            x_label,
            ax_label,
            note_bar,
            note_text,
            star,
        )
