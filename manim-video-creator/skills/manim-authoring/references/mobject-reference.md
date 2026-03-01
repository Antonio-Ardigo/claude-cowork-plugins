# Mobject Reference — Manim CE 0.20.0

## Shapes (VMobject subclasses)

```python
# Basic shapes
Circle(radius=1, color=BLUE, fill_opacity=0.5)
Square(side_length=2, color=GREEN, fill_opacity=0.5)
Rectangle(width=4, height=2, color=RED, fill_opacity=0.5)
Triangle(color=YELLOW, fill_opacity=0.5)
RoundedRectangle(corner_radius=0.3, width=4, height=2)
Polygon(*vertices)  # e.g. Polygon([-1,-1,0], [1,-1,0], [0,1,0])
RegularPolygon(n=6, color=TEAL)  # Hexagon
Star(n=5, color=GOLD, fill_opacity=0.8)
Annulus(inner_radius=0.5, outer_radius=1, color=PURPLE)
Ellipse(width=4, height=2, color=ORANGE)

# Lines and arrows
Line(start=LEFT, end=RIGHT, color=WHITE)
Arrow(start=LEFT, end=RIGHT, color=YELLOW)
DoubleArrow(start=LEFT, end=RIGHT)
DashedLine(start=LEFT, end=RIGHT)
Vector([1, 2, 0])  # Arrow from origin
Dot(point=ORIGIN, color=RED, radius=0.08)
Arc(radius=1, start_angle=0, angle=PI/2)
CurvedArrow(start_point=LEFT, end_point=RIGHT)
```

## Text

```python
# Plain text
Text("Hello World", font_size=48, color=WHITE)
Text("Bold", weight=BOLD)
Text("Italic", slant=ITALIC)
Text("Custom Font", font="Courier New")
MarkupText('<span color="red">colored</span> text')  # Pango markup

# LaTeX
MathTex(r"E = mc^2", font_size=60)
MathTex(r"\int_0^1 x^2 \, dx = \frac{1}{3}")
Tex(r"This is \textbf{bold} \LaTeX")

# LaTeX with subparts for TransformMatchingTex
MathTex(r"a^2", r"+", r"b^2", r"=", r"c^2")  # Each arg is a submobject

# Title
Title("My Animation")

# Bulleted list
BulletedList("Point 1", "Point 2", "Point 3")
```

## Graphing

```python
# 2D Axes
axes = Axes(
    x_range=[-5, 5, 1],      # [min, max, step]
    y_range=[-3, 3, 1],
    x_length=10,               # Screen width
    y_length=6,                # Screen height
    axis_config={"include_numbers": True, "include_tip": True},
)

# Plot a function
graph = axes.plot(lambda x: x**2, color=BLUE, x_range=[-2, 2])
label = axes.get_graph_label(graph, label="x^2")

# Number plane (grid)
plane = NumberPlane(
    x_range=[-5, 5, 1],
    y_range=[-3, 3, 1],
    background_line_style={"stroke_opacity": 0.4}
)

# Number line
nline = NumberLine(x_range=[-5, 5, 1], include_numbers=True)

# Bar chart
chart = BarChart(
    values=[3, 5, 2, 8, 4],
    bar_names=["A", "B", "C", "D", "E"],
    bar_colors=[RED, GREEN, BLUE, YELLOW, PURPLE],
    y_range=[0, 10, 2],
)

# Parametric curve
curve = axes.plot_parametric_curve(
    lambda t: [np.cos(t), np.sin(t), 0],
    t_range=[0, 2*PI],
    color=RED
)

# Implicit curve
curve = axes.plot_implicit_curve(
    lambda x, y: x**2 + y**2 - 1,
    color=YELLOW
)

# Area under curve
area = axes.get_area(graph, x_range=[0, 2], color=BLUE, opacity=0.3)

# Riemann rectangles
rects = axes.get_riemann_rectangles(graph, x_range=[0, 2], dx=0.2)

# Coordinate labels
dot = Dot(axes.c2p(2, 4))  # coords_to_point
coord_label = axes.get_axis_labels(x_label="x", y_label="f(x)")
```

## Tables

```python
table = Table(
    [["A", "B"], ["C", "D"]],
    row_labels=[Text("R1"), Text("R2")],
    col_labels=[Text("C1"), Text("C2")],
    include_outer_lines=True,
)

# Highlight cells
table.add_highlighted_cell((1, 1), color=GREEN)
```

## Groups

```python
# Group related objects
group = VGroup(circle, square, triangle)
group.arrange(RIGHT, buff=0.5)         # Arrange horizontally
group.arrange(DOWN, buff=0.3)          # Arrange vertically
group.arrange_in_grid(rows=2, cols=3)  # Grid layout

# Scale, move, color entire group
group.scale(0.5)
group.shift(2 * LEFT)
group.set_color(RED)
```

## Common Properties (all Mobjects)

```python
mob.set_color(RED)
mob.set_fill(BLUE, opacity=0.5)
mob.set_stroke(WHITE, width=2)
mob.set_opacity(0.7)
mob.scale(2)
mob.rotate(PI/4)
mob.flip(axis=RIGHT)
mob.stretch(factor=2, dim=0)  # Stretch horizontally
mob.get_center()
mob.get_top() / get_bottom() / get_left() / get_right()
mob.get_width() / get_height()
mob.copy()                    # Deep copy
mob.set_z_index(1)           # Layering
```

## Decorators & Braces

```python
brace = Brace(mob, direction=DOWN)
brace_label = brace.get_text("Width = 4")
# or: brace.get_tex(r"w = 4")

SurroundingRectangle(mob, color=YELLOW, buff=0.2)
Underline(mob)
BackgroundRectangle(mob, color=BLACK, fill_opacity=0.8)
Cross(mob)  # Red X through a mobject
```

## 3D Mobjects (require ThreeDScene)

```python
Sphere(radius=1)
Cube(side_length=2)
Cylinder(radius=1, height=2)
Cone(base_radius=1, height=2)
Arrow3D(start=[0,0,0], end=[1,1,1])
Line3D(start=[0,0,0], end=[1,1,1])
Torus(major_radius=2, minor_radius=0.5)
Surface(
    lambda u, v: [u, v, np.sin(u)*np.cos(v)],
    u_range=[-PI, PI],
    v_range=[-PI, PI],
    resolution=(30, 30),
)
```
