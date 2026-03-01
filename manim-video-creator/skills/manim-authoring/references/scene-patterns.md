# Scene Patterns — Manim CE 0.20.0

Common patterns for building effective Manim animations.

## Pattern 1: Title Card + Content

```python
class TitleAndContent(Scene):
    def construct(self):
        title = Text("My Topic", font_size=60, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.scale(0.6).to_edge(UP))

        # Now build content below the title
        content = MathTex(r"E = mc^2", font_size=72)
        self.play(Write(content))
        self.wait(1)
```

## Pattern 2: Step-by-Step Equation Derivation

```python
class Derivation(Scene):
    def construct(self):
        steps = [
            MathTex(r"(a+b)^2"),
            MathTex(r"(a+b)(a+b)"),
            MathTex(r"a^2 + ab + ba + b^2"),
            MathTex(r"a^2 + 2ab + b^2"),
        ]

        self.play(Write(steps[0]))
        for i in range(1, len(steps)):
            self.play(TransformMatchingTex(steps[i-1], steps[i]))
            self.wait(0.5)
        self.wait(1)
```

## Pattern 3: Side-by-Side Comparison

```python
class Comparison(Scene):
    def construct(self):
        left_title = Text("Before", color=RED).to_edge(UP).shift(3*LEFT)
        right_title = Text("After", color=GREEN).to_edge(UP).shift(3*RIGHT)
        divider = Line(UP*3, DOWN*3, color=GREY)

        left_content = Circle(color=RED).shift(3*LEFT)
        right_content = Square(color=GREEN).shift(3*RIGHT)

        self.play(Write(left_title), Write(right_title), Create(divider))
        self.play(Create(left_content), Create(right_content))
        self.wait(1)
```

## Pattern 4: Animated Graph / Function Plot

```python
class AnimatedPlot(Scene):
    def construct(self):
        axes = Axes(x_range=[-4, 4, 1], y_range=[-2, 2, 1],
                    axis_config={"include_numbers": True})
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(labels))

        graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        graph_label = axes.get_graph_label(graph, label=r"\sin(x)")
        self.play(Create(graph), Write(graph_label), run_time=2)

        # Animate a dot along the curve
        t = ValueTracker(-4)
        dot = always_redraw(lambda: Dot(
            axes.c2p(t.get_value(), np.sin(t.get_value())), color=YELLOW
        ))
        self.add(dot)
        self.play(t.animate.set_value(4), run_time=4, rate_func=linear)
        self.wait(1)
```

## Pattern 5: Geometric Proof / Construction

```python
class GeometricConstruction(Scene):
    def construct(self):
        # Build step by step
        triangle = Polygon([-2,-1,0], [2,-1,0], [0,1.5,0],
                           color=WHITE, fill_opacity=0.1)
        self.play(Create(triangle))

        # Add labels
        a_label = MathTex("A").next_to(triangle.get_vertices()[0], DL)
        b_label = MathTex("B").next_to(triangle.get_vertices()[1], DR)
        c_label = MathTex("C").next_to(triangle.get_vertices()[2], UP)
        self.play(Write(a_label), Write(b_label), Write(c_label))

        # Highlight a side
        side = Line(triangle.get_vertices()[0], triangle.get_vertices()[1], color=YELLOW)
        brace = Brace(side, DOWN)
        brace_text = brace.get_tex("a")
        self.play(Create(side), GrowFromCenter(brace), Write(brace_text))
        self.wait(1)
```

## Pattern 6: Bar Chart with Changing Values

```python
class DynamicChart(Scene):
    def construct(self):
        chart = BarChart(
            values=[2, 5, 3, 8, 1],
            bar_names=["A", "B", "C", "D", "E"],
            y_range=[0, 10, 2],
            bar_colors=[BLUE, GREEN, RED, YELLOW, PURPLE],
        )
        self.play(Create(chart))
        self.wait(0.5)

        # Animate value change
        self.play(chart.animate.change_bar_values([7, 3, 9, 4, 6]))
        self.wait(1)
```

## Pattern 7: Text Highlighting / Annotation

```python
class Annotation(Scene):
    def construct(self):
        formula = MathTex(r"F", r"=", r"m", r"a", font_size=72)
        self.play(Write(formula))
        self.wait(0.5)

        # Highlight specific parts
        box_f = SurroundingRectangle(formula[0], color=RED)
        label_f = Text("Force", font_size=24, color=RED).next_to(box_f, UP)
        self.play(Create(box_f), Write(label_f))

        box_m = SurroundingRectangle(formula[2], color=BLUE)
        label_m = Text("Mass", font_size=24, color=BLUE).next_to(box_m, DOWN)
        self.play(Create(box_m), Write(label_m))
        self.wait(1)
```

## Pattern 8: Moving Camera (Zoom & Pan)

```python
class ZoomScene(MovingCameraScene):
    def construct(self):
        # Start with overview
        plane = NumberPlane()
        dots = VGroup(*[Dot(point=[x, y, 0], color=YELLOW)
                        for x in range(-3, 4) for y in range(-2, 3)])
        self.add(plane, dots)
        self.wait(0.5)

        # Zoom into a region
        self.play(self.camera.frame.animate.scale(0.3).move_to([1, 1, 0]),
                  run_time=2)
        self.wait(1)

        # Zoom back out
        self.play(self.camera.frame.animate.scale(1/0.3).move_to(ORIGIN),
                  run_time=2)
        self.wait(0.5)
```

## Pattern 9: 3D Surface

```python
class Surface3D(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70*DEGREES, theta=-45*DEGREES)

        axes = ThreeDAxes()
        surface = Surface(
            lambda u, v: axes.c2p(u, v, np.sin(u) * np.cos(v)),
            u_range=[-PI, PI], v_range=[-PI, PI],
            resolution=(30, 30),
        )
        surface.set_style(fill_opacity=0.7)
        surface.set_fill_by_value(axes=axes, colorscale=[
            (BLUE, -1), (GREEN, 0), (RED, 1)
        ])

        self.play(Create(axes), Create(surface), run_time=3)
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(5)
```

## Pattern 10: Progressive Reveal with Bullets

```python
class BulletReveal(Scene):
    def construct(self):
        title = Text("Key Points", font_size=48, color=BLUE).to_edge(UP)
        self.play(Write(title))

        points = [
            "First important point",
            "Second crucial detail",
            "Third key takeaway",
        ]

        bullets = VGroup()
        for i, point in enumerate(points):
            bullet = Text(f"• {point}", font_size=32)
            bullets.add(bullet)

        bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        bullets.next_to(title, DOWN, buff=0.8)

        for bullet in bullets:
            self.play(FadeIn(bullet, shift=RIGHT*0.5), run_time=0.5)
            self.wait(0.3)

        self.wait(1)
```

## Tips for Good Animations

1. **Pacing**: Use `self.wait(0.5)` between sections; don't rush transitions
2. **Colors**: Use contrasting colors for related/compared elements
3. **Layout**: Use `to_edge()`, `next_to()`, `arrange()` for clean positioning
4. **Emphasis**: Use `Indicate()` or `SurroundingRectangle` to draw attention
5. **Transitions**: `FadeOut(*self.mobjects)` to clear the scene between sections
6. **run_time**: Slow down complex animations (2-3s), speed up simple ones (0.3-0.5s)
7. **Groups**: Always use `VGroup` for related objects — easier to move/transform
8. **Labels**: Add text labels near mathematical objects for clarity
