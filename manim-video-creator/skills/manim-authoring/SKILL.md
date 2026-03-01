---
name: manim-authoring
description: >
  Manim Community Edition animation authoring knowledge. Use when the user asks to
  "create a video", "make an animation", "animate", "visualize", "render a scene",
  "manim", or needs guidance on Manim CE API, animation patterns, or mathematical
  visualization techniques.
version: 0.1.0
---

# Manim CE Authoring Guide

Domain knowledge for creating mathematical animations with Manim Community Edition 0.20.0.

## Workspace Setup

- **Workspace**: `C:/Users/anton/manim-workspace`
- **Python venv**: `C:/Users/anton/manim-workspace/.venv` (Python 3.13)
- **Manim version**: 0.20.0 (Community Edition)
- **LaTeX**: MiKTeX at `C:/Users/anton/AppData/Local/Programs/MiKTeX/`
- **ffmpeg**: Available system-wide (8.0.1)

## Scene Structure

Every Manim animation is a Scene class:

```python
from manim import *

class MyScene(Scene):
    def construct(self):
        # Create objects
        # Animate them
        # self.play(...) to animate
        # self.wait() for pauses
```

Render with: `cd C:/Users/anton/manim-workspace && .venv/Scripts/python -m manim -qm file.py ClassName`

## Quality Levels

| Flag | Resolution | FPS | Use case |
|------|-----------|-----|----------|
| `-ql` | 480p | 15 | Quick preview |
| `-qm` | 720p | 30 | Standard |
| `-qh` | 1080p | 60 | High quality |
| `-qk` | 4K | 60 | Production |

Output goes to `media/videos/<filename>/<quality>/`.

## Core Mobject Types

- **Shapes**: Circle, Square, Rectangle, Triangle, Polygon, Line, Arrow, Arc, Dot, Annulus, Star
- **Text**: Text (plain), MathTex (LaTeX inline), Tex (LaTeX block), MarkupText (Pango)
- **Math**: MathTex for formulas, Brace, BraceBetweenPoints, SurroundingRectangle
- **Graphing**: Axes, NumberPlane, NumberLine, BarChart, FunctionGraph
- **3D**: ThreeDScene, Surface, Sphere, Cube, Cylinder, Cone, Arrow3D (requires ThreeDScene)
- **Groups**: VGroup (for grouping related Mobjects), AnimationGroup
- **Tables**: Table, MathTable, IntegerTable, DecimalTable

## Core Animations

**Creation**: Create, Write, DrawBorderThenFill, FadeIn, GrowFromCenter, SpinInFromNothing
**Removal**: FadeOut, Uncreate, ShrinkToCenter
**Transform**: Transform, ReplacementTransform, TransformMatchingTex, TransformMatchingShapes
**Movement**: shift, move_to, next_to, to_edge, to_corner
**Emphasis**: Indicate, Wiggle, Flash, Circumscribe, FocusOn
**Updaters**: always_redraw, add_updater for dynamic objects

## Positioning

- Absolute: `obj.move_to(ORIGIN)`, `obj.move_to([2, 1, 0])`
- Relative: `obj.next_to(other, RIGHT, buff=0.5)`
- Edge: `obj.to_edge(UP)`, `obj.to_corner(UL)`
- Shift: `obj.shift(2*RIGHT + UP)`
- Arrange groups: `VGroup(...).arrange(RIGHT, buff=1)`

## Animation Patterns

**Sequential**: Separate `self.play()` calls
**Simultaneous**: `self.play(anim1, anim2)` in one call
**Staggered**: `AnimationGroup(*anims, lag_ratio=0.2)`
**With run_time**: `self.play(Create(obj), run_time=2)`
**Animate syntax**: `self.play(obj.animate.shift(RIGHT).set_color(RED))`

## Detailed References

- **`references/animation-reference.md`** — Complete animation catalog with examples
- **`references/mobject-reference.md`** — All Mobject types, properties, and methods
- **`references/scene-patterns.md`** — Common scene templates and composition patterns
