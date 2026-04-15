from manim import *


BG = "#FBF4EA"
PANEL = "#FFFDF9"
LINE = "#E5D6C8"
TEXT = "#1F1A17"
MUTED = "#675E57"
ACCENT = "#C65D2E"
DEEP = "#8E3513"
TEAL = "#2F5D56"
SOFT = "#F3E6D8"
FONT = "Malgun Gothic"


class EigenvectorCard(Scene):
    def construct(self):
        self.camera.background_color = BG

        outer = RoundedRectangle(
            width=13.3,
            height=7.1,
            corner_radius=0.28,
            fill_color=PANEL,
            fill_opacity=1,
            stroke_color=LINE,
            stroke_width=1.5,
        )
        outer.move_to(ORIGIN)

        eyebrow = Text(
            "LINEAR ALGEBRA VISUAL NOTE",
            font=FONT,
            weight=BOLD,
            font_size=20,
            color=DEEP,
        )
        eyebrow.align_to(outer, UL).shift(RIGHT * 0.45 + DOWN * 0.45)

        title = Text(
            "고유벡터와 고유값을 그림으로 이해하기",
            font=FONT,
            weight=BOLD,
            font_size=30,
            color=TEXT,
        ).next_to(eyebrow, DOWN, aligned_edge=LEFT, buff=0.2)

        subtitle = Text(
            '핵심은 "방향이 안 바뀐다"보다 "같은 직선 위에 남는다"이다.',
            font=FONT,
            font_size=17,
            color=MUTED,
        ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.15)

        main_panel = RoundedRectangle(
            width=12.25,
            height=3.65,
            corner_radius=0.26,
            fill_color="#FBF2E8",
            fill_opacity=1,
            stroke_color=LINE,
            stroke_width=1.3,
        )
        main_panel.next_to(subtitle, DOWN, buff=0.45)

        divider = Line(
            main_panel.get_top() + DOWN * 0.48,
            main_panel.get_bottom() + UP * 0.48,
            stroke_color="#E7D7C7",
            stroke_width=2,
        )
        divider.move_to(main_panel.get_center())

        left_group = self._comparison_side(
            title="일반 벡터",
            subtitle="행렬을 곱하면 방향과 크기가 함께 바뀜",
            accent=TEAL,
            mode="generic",
            note="x와 Ax가 서로 다른 직선 위에 있다.",
        )
        right_group = self._comparison_side(
            title="고유벡터",
            subtitle="변환 후에도 같은 직선 위에 남고 배율만 달라짐",
            accent=ACCENT,
            mode="eigen",
            note="같은 직선 위에 남고, 배율만 달라진다.",
        )

        left_group.move_to(main_panel.get_center() + LEFT * 2.18)
        right_group.move_to(main_panel.get_center() + RIGHT * 2.18)

        footer = RoundedRectangle(
            width=11.9,
            height=0.62,
            corner_radius=0.18,
            fill_color=SOFT,
            fill_opacity=1,
            stroke_width=0,
        )
        footer.next_to(main_panel, DOWN, buff=0.35)
        footer_title = Text("면접용 핵심 문장", font=FONT, weight=BOLD, font_size=15, color=DEEP)
        footer_body = Text(
            "고유벡터는 변환 후에도 같은 직선 위에 남는 벡터이고, 고유값은 그때의 배율이다.",
            font=FONT,
            font_size=14,
            color=MUTED,
        )
        footer_group = VGroup(footer_title, footer_body).arrange(RIGHT, buff=0.26)
        footer_group.move_to(footer)
        footer_group.scale(0.94)
        footer_group.move_to(footer)

        self.add(
            outer,
            eyebrow,
            title,
            subtitle,
            main_panel,
            divider,
            left_group,
            right_group,
            footer,
            footer_group,
        )

    def _comparison_side(self, title, subtitle, accent, mode, note):
        chip = RoundedRectangle(
            width=1.54,
            height=0.38,
            corner_radius=0.19,
            fill_color=accent,
            fill_opacity=1,
            stroke_width=0,
        )
        chip_text = Text(title, font=FONT, weight=BOLD, font_size=15, color=PANEL).move_to(chip)
        heading = Text(title, font=FONT, weight=BOLD, font_size=23, color=TEXT)
        heading.next_to(chip, DOWN, aligned_edge=LEFT, buff=0.18)
        sub = Text(subtitle, font=FONT, font_size=13.3, color=MUTED)
        sub.next_to(heading, DOWN, aligned_edge=LEFT, buff=0.12)

        box = RoundedRectangle(
            width=4.35,
            height=1.5,
            corner_radius=0.16,
            fill_color="#FFF9F1",
            fill_opacity=1,
            stroke_color=LINE,
            stroke_width=1.2,
        )
        box.next_to(sub, DOWN, aligned_edge=LEFT, buff=0.34)

        h = Line(box.get_left() + RIGHT * 0.3, box.get_right() + LEFT * 0.3, stroke_color="#D4C4B2", stroke_width=2)
        v = Line(box.get_top() + DOWN * 0.22, box.get_bottom() + UP * 0.22, stroke_color="#D4C4B2", stroke_width=2)
        h.move_to(box.get_center())
        v.move_to(box.get_center())
        origin = Dot(box.get_center(), radius=0.052, color=DEEP)

        if mode == "generic":
            x_end = origin.get_center() + LEFT * 1.05 + UP * 0.63
            ax_end = origin.get_center() + RIGHT * 1.4 + UP * 0.72
            x_label_pos = UL
            ax_label_text = "Ax"
        else:
            base = Line(box.get_left() + RIGHT * 0.48, box.get_right() + LEFT * 0.48, stroke_color="#E0A284", stroke_width=4.2)
            base.move_to(box.get_center())
            x_end = origin.get_center() + LEFT * 1.02
            ax_end = origin.get_center() + RIGHT * 1.45
            x_label_pos = UP
            ax_label_text = "Ax = λx"

        x_arrow = Arrow(origin.get_center(), x_end, buff=0, stroke_width=6, max_tip_length_to_length_ratio=0.14, color=TEAL)
        ax_arrow = Arrow(origin.get_center(), ax_end, buff=0, stroke_width=6, max_tip_length_to_length_ratio=0.14, color=ACCENT)
        x_label = Text("x", font=FONT, weight=BOLD, font_size=14, color=TEAL).next_to(x_arrow.get_end(), x_label_pos, buff=0.04)
        ax_label = Text(ax_label_text, font=FONT, weight=BOLD, font_size=14, color=ACCENT).next_to(ax_arrow.get_end(), UP if mode == "eigen" else UR, buff=0.04)

        note_title = Text("핵심", font=FONT, weight=BOLD, font_size=13.4, color=DEEP)
        note_body = Text(note, font=FONT, font_size=12.6, color=MUTED)
        note_group = VGroup(note_title, note_body).arrange(RIGHT, buff=0.18)
        note_group.next_to(box, DOWN, aligned_edge=LEFT, buff=0.22)

        items = [chip, chip_text, heading, sub, box, h, v, origin, x_arrow, ax_arrow, x_label, ax_label, note_group]
        if mode == "eigen":
            items.insert(8, base)
        return VGroup(*items)
