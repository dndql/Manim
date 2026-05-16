from manim import *
from scipy.optimize import brentq

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_rate = 60


class vnfdl(Scene):
    def construct(self):
        qjsgh = Text("대수 서답형 10번", font="Bookk Myungjo", font_size=75)

        q0 = Text("방정식", font="Bookk Myungjo", font_size=50)
        q1 = MathTex(r"|9^{x}-3|-2^{x+k}=0").scale(1.4)
        q2 = Text("의", font="Bookk Myungjo", font_size=50)
        q3 = Text("서로 다른 두 근", font="Bookk Myungjo", font_size=50)
        q4 = MathTex(r"\alpha, \beta").scale(1.4)
        q5 = Text("에 대하여", font="Bookk Myungjo", font_size=50)
        q6 = MathTex(r"\alpha < 0 < \beta < 2").scale(1.4)
        q7 = Text("를 만족시키는", font="Bookk Myungjo", font_size=50)
        q8 = Text("자연수 k 중 최솟값을 a라 하자", font="Bookk Myungjo", font_size=50)
        q9 = Text("두 집합", font="Bookk Myungjo", font_size=50)
        q10 = MathTex(r"A = \{x|x^{2}-9x+8 \le 0\}").scale(1.4)
        q11 = MathTex(r"B = \{x|(log_a{x})^{2}-2mlog_a{x}+m^{2}-1 \le 0\}").scale(1.4)
        q12 = Text("에 대하여", font="Bookk Myungjo", font_size=50)
        q13 = MathTex(r"A \cap B \neq \varnothing").scale(1.4)
        q14 = Text("을 만족시키는", font="Bookk Myungjo", font_size=50)
        q15 = Text("정수 m의 합을 구하시오.", font="Bookk Myungjo", font_size=50)


        p1 = Text("1. k 값 구하기", font="Bookk Myungjo", font_size=50)
        p2 = MathTex(r"|9^{x}-3|-2^{x+k}=0").scale(1.4)
        p3 = MathTex(r"|9^{x}-3|", r"=", r"2^{x+k}").scale(1.4)
        p4 = Text("두 그래프의 교점의 x좌표가 방정식의 해", font="Bookk Myungjo", font_size=50)
        p5 = MathTex(r"\alpha, \beta").scale(1.4)
        p6 = Text("의 범위를 만족시키는 k 값의 범위:", font="Bookk Myungjo", font_size=50)
        p7_1 = MathTex(r"1 < ").scale(1.4)
        p7_2 = MathTex(r"k").scale(1.4)
        p7_3 = MathTex(r" < 4.29").scale(1.4)
        qjadnl = MathTex(r"\alpha < 0 < \beta < 2")

        yRan = ValueTracker(40)
        ax1 = always_redraw(lambda: Axes(
            x_range=[-2, 3], 
            y_range=[-1, yRan.get_value(), 20 if yRan.get_value() > 50 else 5], 
            x_length=10,
            y_length=8,
            axis_config={"include_tip": True}
        ).add_coordinates().move_to(DOWN)) # 여기에 위치 고정!

        ax2 = Axes(
            x_range=[-2, 3], 
            y_range=[-1, 100, 10], 
            x_length=10,
            y_length=10,
            axis_config={"include_tip": True} # 화살표 표시
        ).add_coordinates()

        def get_roots(k_val):
            f = lambda x: abs(9**x - 3) - 2**(x + k_val)
    
            try:
                # 알파는 무조건 0보다 작은 구간에서만 찾음
                alpha = brentq(f, -2, 0.5) 
                # 베타는 무조건 0보다 큰 구간에서만 찾음
                beta = brentq(f, 0.5, 3)
                return alpha, beta
            except:
                # 근을 못 찾는 구간(k가 너무 작을 때) 에러 방지
                return -0.5, 0.5

        #글자들 위치 이동 및 기본 설정
        qjsgh.move_to(UP*7.5)
        qjsgh.to_edge(LEFT)

        q0.move_to(UP*6)
        q1.move_to(UP*6 + LEFT*1.5)
        q2.move_to(UP*6 + RIGHT*1.75)

        q3.move_to(UP*5)
        q4.move_to(UP*5 + LEFT*1.5)
        q5.move_to(UP*5 + RIGHT*0.5)

        q6.move_to(UP*4)
        q7.move_to(UP*4)
        q8.move_to(UP*3)

        q9.move_to(UP)
        q11.move_to(DOWN)
        q12.move_to(DOWN*2)
        
        q13.move_to(DOWN*4)
        q14.move_to(DOWN*4 + LEFT*1.25)
        q15.move_to(DOWN*5)

        q0.to_edge(LEFT)
        q3.to_edge(LEFT)
        q6.to_edge(LEFT)
        q8.to_edge(LEFT)
        q9.to_edge(LEFT)
        q10.to_edge(LEFT)
        q11.to_edge(LEFT)
        q12.to_edge(LEFT)
        q13.to_edge(LEFT)
        q15.to_edge(LEFT)

        p1.move_to(UP*6)
        p2.move_to(UP*4)
        p3.move_to(UP*4)
        p4.move_to(DOWN*8)

        p5.move_to(DOWN*8.5 + LEFT*4.75)
        p6.move_to(DOWN*8.5 + RIGHT*0.75)
        qjadnl.move_to(DOWN*7.5)

        p7_1.move_to(DOWN*9.5 + LEFT)
        p7_2.move_to(DOWN*9.5)

        p1.to_edge(LEFT)

        p3.set_color_by_tex("|9^{x}-3|", BLUE)
        p3.set_color_by_tex("2^{x+k}", YELLOW)


        # self.camera.background_color = "Green"

        #문제 설명 나타나기
        self.wait(0.5)
        self.play(FadeIn(Group(qjsgh, q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15)))

        #문제 적당한 위치로 옮기기
        gq1 = Group(q0, q1, q2, q3, q4, q5, q6, q7, q8)
        gq2 = Group(q9, q10, q11, q12, q13, q14, q15)
        self.wait(2.5)
        self.play(FadeOut(qjsgh), gq1.animate.shift(UP*6).scale(0.58, about_edge=LEFT), gq2.animate.shift(UP*11.65).scale(0.58, about_edge=RIGHT).to_edge(RIGHT))


        self.play(Write(p1))
        self.play(Write(p2))
        self.wait(0.5)
        self.play(ReplacementTransform(p2, p3))

        # 그래프 그리기
        k = ValueTracker(-2)
        k_val = DecimalNumber(k.get_value(), num_decimal_places=2).scale(2)
        k_text = Text("k = ").scale(1.4)
        k_val.add_updater(lambda m: m.set_value(k.get_value())) # 숫자가 실시간으로 업데이트되도록
        k_val.move_to(DOWN*6 + RIGHT*1.1)
        k_text.move_to(DOWN*6 + LEFT)
        intersections = always_redraw(
            lambda: VGroup(*[
                VGroup(
                    # 1. 교점에 점 찍기
                    Dot(ax1.c2p(x, 2**(x + k.get_value())), color=RED, radius=0.08),
                    # 2. x축으로 내리는 점선
                    DashedLine(
                        start=ax1.c2p(x, 2**(x + k.get_value())), 
                        end=ax1.c2p(x, 0), 
                        color=GRAY,
                        stroke_width=2
                    ),
                    # 3. 알파, 베타 라벨
                    MathTex(tex).scale(1.2).next_to(ax1.c2p(x, 0), DOWN)
                )
                for x, tex in zip(get_roots(k.get_value()), [r"\alpha", r"\beta"])
            ])
        )


        graph1 = always_redraw(lambda: ax1.plot(
            lambda x: abs(9**x - 3), 
            # yRan에 맞춰 |9^x - 3| <= yRan 되는 x 상한을 동적으로 계산
            x_range=[-2, min(2.5, np.log(yRan.get_value() + 3) / np.log(9))], 
            color=BLUE
        ))

        graph2 = always_redraw(
            lambda: ax1.plot(
                lambda x: 2**(x + k.get_value()), 
                # 2^(x+k) <= yRan 이 되는 x 상한: x <= log2(yRan) - k
                x_range=[-2, min(2.5, np.log2(max(1, yRan.get_value())) - k.get_value())], 
                color=YELLOW
            )
        )

        self.play(Create(ax1), run_time=1)
        # self.play(Create(graph1), Create(graph2), Write(k_val), Write(k_text), run_time=0.5)

        self.play(
            Create(graph1), 
            FadeIn(graph2), 
            Write(k_val), 
            Write(k_text), 
            run_time=0.5
        )

        self.play(Write(p4), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(intersections))
        # k가 변함에 따라 그래프와 알파, 베타가 같이 움직임
        self.play(k.animate.set_value(3), run_time=1)
        self.wait(0.5)
        self.play(k.animate.set_value(0), run_time=1)
        self.play(ReplacementTransform(p4, VGroup(p5, p6)), FadeIn(p7_2), FadeIn(qjadnl))
        self.play(k.animate.set_value(1), run_time=2)
        self.play(FadeIn(p7_1))
        

        self.play(
            yRan.animate.set_value(100),
            # k.animate.set_value(4.29), # k값도 함께 변경한다면
            run_time=2
        )
        

