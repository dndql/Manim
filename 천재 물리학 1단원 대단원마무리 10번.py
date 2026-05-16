from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_rate = 60

class animation1(Scene):
    def construct(self):
        # 물체 선언 부분
        q1 = Text("충돌 후 공의 속력은?", font="Bookk Myungjo", font_size=90)
        q2 = Text("버스와 공의 역학적 에너지는 보존되며,", font="Bookk Myungjo", font_size=35, color="#D1D1D1")
        q3 = Text("공의 질량은 버스의 질량에 비해 무시할 수 있을 만큼 작다.", font="Bookk Myungjo", font_size=35, color="#D1D1D1")
        p1 = MarkupText("버스의 질량: M\n공의 질량: m\n충돌 후 버스의 속력: v<sub>1</sub>\n충돌 후 공의 속력: v<sub>2</sub>", font="Bookk Myungjo", font_size=50, line_spacing=1.5)
        p2 = MarkupText("이라 하자", font="Bookk Myungjo", font_size=50, line_spacing=1.5)
        p3 = Text("운동량 공식", font="Bookk Myungjo", font_size=65)
        p4 = Text("운동량 = 질량 × 속도", font="Bookk Myungjo", font_size=45)
        p5 = MathTex(r"p = m \times v").scale(2)
        p6 = Text("운동량 보존 법칙에 따라", font="Bookk Myungjo", font_size=70)
        p7 = Text("(충돌 전) 버스의 운동량 + (충돌 전) 공의 운동량 \n = (충돌 후) 버스의 운동량 + (충돌 후) 공의 운동량", font="Bookk Myungjo", font_size=45, line_spacing=1.2)
        p8 = MathTex(r"M \times 20 + m \times (- 10) = Mv_1 + mv_2").scale(1.5)
        p9 = Text("운동에너지 공식", font="Bookk Myungjo", font_size=65)
        p10 = MathTex(r"K = \frac{1}{2}mv^{2}").scale(1.5)
        p11 = Text("역학적 에너지 보존 법칙에 따라", font="Bookk Myungjo", font_size=70)
        p12 = MathTex(r"\frac{1}{2}M \times 20^{2} + \frac{1}{2}m \times (-10)^{2} = \frac{1}{2}Mv_1^{2} + \frac{1}{2}mv_2^{2}").scale(1.4)
        p13 = Text("식 정리", font="Bookk Myungjo", font_size=75)
        p8_1 = MathTex(r"20M - 10m = Mv_1 + mv_2").scale(1.5)
        p8_2 = MathTex(r"M(20-v_1) = m(v_2+10)").scale(1.5)
        p12_1 = MathTex(r"20^{2}M+10^{2}m = Mv_1^{2} + mv_2^{2}").scale(1.5)
        p12_2 = MathTex(r"M(20^{2} - v_1^{2}) = m(v_1^{2} - 10^{2})").scale(1.5)
        p14 = Text("아래 식을 위의 식으로 나누면", font="Bookk Myungjo", font_size=75)
        p15 = MathTex(r"\frac{M(20+v_1)(20-v_1)}{M(20-v_1)} = \frac{M(v_2+10)(v_2-10)}{M(v_2+10)}").scale(1.2)
        p15_1 = MathTex(r"20+v_1 = v_2-10").scale(1.5)
        p15_2 = MathTex(r"v_1 = v_2-30").scale(1.5)
        p16 = Text("아래 식을 위의 식에 대입", font="Bookk Myungjo", font_size=75)
        p17 = MathTex(r"M(20-v_2+30) = m(v_2+10)").scale(1.5)
        p17_1 = MathTex(r"50M-Mv_2 = mv_2+10m").scale(1.5)
        p17_2 = MathTex(r"(M+m)v_2 = 50M-10m").scale(1.5)
        p17_3 = MathTex(r"v_2 = \frac{50M-10m}{M+m}").scale(1.5)
        p18 = Text("공의 질량(m)은 버스의 질량(M)에 비해", font="Bookk Myungjo", font_size=55)
        p18_1 = Text("무시할 수 있을 만큼 작다.", font="Bookk Myungjo", font_size=55)
        p19 = MathTex(r"\frac{m}{M}").scale(1.4)
        p20 = Text("은 0으로 수렴", font="Bookk Myungjo", font_size=65)
        p21 = MathTex(r"v_2 = \frac{50 - \frac{m}{M} \times 10}{1 + \frac{m}{M}}").scale(1.5)
        p21_1 = MathTex(r"v_2 = \frac{50}{1}").scale(1.5)
        p21_2 = MathTex(r"v_2 = 50").scale(1.5)
        Answer = Text("충돌 후 공의 속력: 50m/s", font="Bookk Myungjo", font_size=80)

        Bus = ImageMobject("./Bus").scale(0.45)
        Ball = Circle(color="#DEDEDE", fill_opacity=1).scale(0.4)
        BusArrow = Arrow(start=LEFT, end=RIGHT, tip_length=0.5).scale(1.9)
        BusVelo = Text("20m/s", font="Bookk Myungjo", font_size=55)
        BallArrow = Arrow(start=RIGHT, end=LEFT, tip_length=0.5)
        BallVelo = Text("10m/s", font="Bookk Myungjo", font_size=55)
        Arrow1 = Arrow(start=UP, end=DOWN, tip_length=0.5).scale(0.8)


        # self.camera.background_color = "Green"
        
        #시작
        self.wait(1)

        #초기 위치 설정
        Bus.move_to(LEFT*4)
        Ball.move_to(RIGHT*5.5)
        BusVelo.move_to(UP*1)
        BallArrow.move_to(RIGHT*3.9)
        BallVelo.move_to(RIGHT*3.9 + UP*1)

        q1.move_to(UP*5)
        q2.move_to(UP*4)
        q3.move_to(UP*3.5)

        p1.move_to(UP*1.8 + LEFT*3)
        p2.move_to(UP*1.8 + RIGHT*4.5)
        # p3.move_to()
        p4.move_to(DOWN)
        p5.move_to(DOWN*1.2)
        p6.move_to(DOWN*3)
        p7.move_to(DOWN*5)
        p8.move_to(DOWN*4.5)
        p8_1.move_to(DOWN)
        p8_2.move_to(DOWN)
        p9.move_to(DOWN*1.5)
        p10.move_to(DOWN*3)
        p11.move_to(DOWN*5.5)
        p12.move_to(DOWN*7)
        p12_1.move_to(DOWN*3)
        p12_2.move_to(DOWN*3)
        p13.move_to(DOWN*6.5)
        p14.move_to(DOWN*6.5)
        p15.move_to(DOWN*3)
        p15_1.move_to(DOWN*3)
        p15_2.move_to(DOWN*3)
        p16.move_to(DOWN*6.5)
        p17.move_to(DOWN)
        p17_1.move_to(DOWN)
        p17_2.move_to(DOWN)
        p17_3.move_to(DOWN)
        p18.move_to(DOWN*4)
        p18_1.move_to(DOWN*5)
        p19.move_to(LEFT*2.5 + DOWN*8)
        p20.move_to(RIGHT*0.5 + DOWN*8)
        Arrow1.move_to(DOWN*6.5)
        p21.move_to(DOWN)
        p21_1.move_to(DOWN)
        p21_2.move_to(DOWN)
        Answer.move_to(DOWN)

        #버스 공 화살표 나타나기
        self.play(FadeIn(Bus, Ball), run_time=0.2, rate_func=rush_from)
        self.wait(0.1)
        self.play(Write(BusArrow), Write(BusVelo), Write(BallArrow), Write(BallVelo), run_time=0.4)

        self.wait(0.5)

        self.play(LaggedStart(Write(q1), Write(q2, run_time=0.5), Write(q3, run_time=0.5), lag_ratio=0.6))

        self.wait(1)

        # 문제 설명 끝

        # 문제를 적당한 위치로 이동
        self.play(Group(q1, q2, q3).animate.move_to(UP*9.5), Group(Bus, Ball, BusVelo, BusArrow, BallVelo, BallArrow).animate.shift(UP*6))

    
        self.play(LaggedStart(Write(p1, run_time=1.2), Write(p2, run_time=0.4), lag_ratio=0.8))
        self.wait(0.5)

        self.play(FadeOut(p2), p1.animate.shift(UP))

        self.play(Write(p3), Write(p4))
        self.wait(0.3)
        self.play(Transform(p4, p5))

        #운동량 설명 시작
        self.wait(0.5)
        self.play(Write(p6), Write(p7))
        self.wait(1)

        self.play(ReplacementTransform(p7, p8))

        self.play(LaggedStart(FadeOut(Group(p3, p4, p6)), p8.animate.shift(UP*5), lag_ratio=0.5))
        
        # 운동에너지 설명 시작
        self.play(Write(p9), Write(p10))
        self.play(Write(p11), Write(p12))

        self.wait(1.5)
        self.play(FadeOut(Group(p9, p10, p11)), p12.animate.shift(UP*4), p8.animate.shift(DOWN*1.5))

        #식 정리 시작
        self.play(FadeIn(p13), run_time=0.5)

        self.play(ReplacementTransform(p8, p8_1), ReplacementTransform(p12, p12_1))
        self.play(ReplacementTransform(p8_1, p8_2), ReplacementTransform(p12_1, p12_2))

        #식끼리 나누기

        self.play(FadeOut(p13), run_time=0.5)
        self.play(FadeIn(p14), run_time=0.5)

        self.wait(0.5)
        self.play(ReplacementTransform(p12_2, p15), p8_2.animate.shift(UP))
        self.wait(0.5)
        self.play(ReplacementTransform(p15, p15_1))
        self.play(ReplacementTransform(p15_1, p15_2))

        self.wait(0.5)
        self.play(FadeOut(p14), run_time=0.5)
        self.play(FadeIn(p16), p8_2.animate.shift(DOWN))

        # 마지막 대입
        self.play(ReplacementTransform(p15_2, p17), ReplacementTransform(p8_2, p17))
        self.wait(0.5)
        self.play(ReplacementTransform(p17, p17_1))
        self.play(ReplacementTransform(p17_1, p17_2))
        self.play(ReplacementTransform(p17_2, p17_3))

        #극한 사용해 최종 결과 구하기
        self.wait(0.5)
        self.play(FadeOut(p16), run_time=0.5)
        self.play(FadeIn(p18), FadeIn(p18_1), run_time=0.5)
        
        self.wait(1)
        self.play(Write(Arrow1))

        self.wait(0.2)
        self.play(Write(p19), Write(p20), run_time=0.5)

        self.wait(0.5)
        self.play(ReplacementTransform(p17_3, p21))
        self.wait(0.5)
        self.play(ReplacementTransform(p21, p21_1))
        self.play(ReplacementTransform(p21_1, p21_2))
        self.wait(0.2)
        self.play(ReplacementTransform(p21_2, Answer))

        self.wait(1.5)

        self.play(Unwrite(p1), Unwrite(p18), Unwrite(p18_1), Unwrite(p19), Unwrite(p20), Unwrite(Arrow1), run_time=1)
        self.play(Group(q1, q2, q3).animate.move_to(UP*5), Group(Bus, Ball, BusVelo, BusArrow, BallVelo, BallArrow).animate.shift(DOWN*5), Answer.animate.shift(DOWN*1.5))
        

        # self.play(Write(BusVelo))

        
