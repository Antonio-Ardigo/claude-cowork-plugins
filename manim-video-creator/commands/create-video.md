---
description: Create a Manim animation video from a text description
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(manim:*), Bash(python:*), Bash(cd:*), Bash(ls:*), Bash(cat:*)
argument-hint: <description of the video you want>
model: opus
---

You are creating a Manim Community Edition (v0.20.0) animation video. The user wants: **$ARGUMENTS**

## Workspace

The manim workspace is at `C:/Users/anton/manim-workspace`. All scene files MUST be written there. The virtual environment is at `C:/Users/anton/manim-workspace/.venv`.

## Process

1. **Understand the request.** Break down what the user wants to see animated. Identify the mathematical objects, text, transformations, and flow.

2. **Design the scene.** Plan the animation sequence:
   - What Mobjects are needed (shapes, text, math, axes, graphs, etc.)
   - What animations to use (Create, Write, Transform, FadeIn, FadeOut, Indicate, etc.)
   - Timing and pacing (self.wait, run_time parameters)
   - Layout and positioning (to_edge, next_to, arrange, shift)

3. **Write the scene file.** Create a Python file in the workspace:
   - File name: descriptive snake_case (e.g., `pythagorean_theorem.py`)
   - Class name: descriptive PascalCase (e.g., `PythagoreanTheorem`)
   - Always `from manim import *`
   - Each scene is a class inheriting from `Scene` with a `construct(self)` method
   - Add a module docstring explaining what the scene shows and how to render it

4. **Render the video.** Run manim from the workspace:
   ```
   cd C:/Users/anton/manim-workspace && .venv/Scripts/python -m manim -qm <filename>.py <ClassName>
   ```
   Use `-qm` (720p/30fps) as the default quality. If the user asks for:
   - Quick preview: use `-ql` (480p/15fps)
   - High quality: use `-qh` (1080p/60fps)
   - Production: use `-qk` (4K/60fps)

5. **Check output.** Verify the render succeeded. The output MP4 will be in `media/videos/<filename>/<quality>/`. Report the full path to the user.

6. **Iterate if needed.** If the render fails, read the error, fix the scene code, and re-render.

## Code Quality Rules

- Use descriptive variable names
- Group related animations logically
- Use `VGroup` for related objects
- Use `self.wait()` between major sections for pacing
- Prefer `self.play(anim1, anim2)` for simultaneous animations
- Use `run_time` to control animation speed
- Add color and fill_opacity for visual appeal
- Position objects intentionally — don't let them overlap unintentionally

## Important Manim CE Notes

- Import: `from manim import *` (brings in everything including numpy as `np`)
- Colors: RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE, WHITE, GREY, TEAL, MAROON, GOLD, PINK
- Directions: UP, DOWN, LEFT, RIGHT, UL, UR, DL, DR, ORIGIN
- Constants: PI, TAU, DEGREES
- LaTeX requires MiKTeX (installed at `C:/Users/anton/AppData/Local/Programs/MiKTeX/`)
- ffmpeg is available system-wide

After rendering, tell the user the output file path so they can view the video.
