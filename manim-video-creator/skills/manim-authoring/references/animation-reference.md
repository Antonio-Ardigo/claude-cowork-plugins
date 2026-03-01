# Animation Reference — Manim CE 0.20.0

## Creation Animations

```python
self.play(Create(mobject))              # Draw stroke then fill
self.play(Write(text))                  # Handwriting effect for Text/MathTex
self.play(DrawBorderThenFill(mobject))  # Draw outline, then fill
self.play(FadeIn(mobject))              # Simple fade in
self.play(FadeIn(mobject, shift=UP))    # Fade in from direction
self.play(GrowFromCenter(mobject))      # Scale up from center
self.play(GrowFromPoint(mob, point))    # Scale up from specific point
self.play(GrowFromEdge(mob, LEFT))      # Grow from an edge
self.play(SpinInFromNothing(mobject))   # Spin in while growing
self.play(GrowArrow(arrow))            # Specifically for Arrow objects
self.play(AddTextLetterByLetter(text)) # Typewriter effect
```

## Removal Animations

```python
self.play(FadeOut(mobject))              # Simple fade out
self.play(FadeOut(mobject, shift=DOWN))  # Fade out toward direction
self.play(Uncreate(mobject))             # Reverse of Create
self.play(ShrinkToCenter(mobject))       # Scale down to nothing
self.play(RemoveTextLetterByLetter(text))# Reverse typewriter
```

## Transform Animations

```python
# Morphs source into target (source becomes target)
self.play(Transform(source, target))

# Replaces source with target (cleaner for subsequent references)
self.play(ReplacementTransform(source, target))

# Match LaTeX parts by tex strings
self.play(TransformMatchingTex(tex1, tex2))

# Match shapes by similarity
self.play(TransformMatchingShapes(group1, group2))

# Animated property changes via .animate
self.play(mob.animate.shift(RIGHT))
self.play(mob.animate.set_color(RED))
self.play(mob.animate.scale(2))
self.play(mob.animate.rotate(PI/4))
self.play(mob.animate.set_opacity(0.5))

# Chain .animate transforms
self.play(mob.animate.shift(UP).scale(1.5).set_color(BLUE))
```

## Movement Animations

```python
self.play(mob.animate.move_to(ORIGIN))
self.play(mob.animate.shift(2 * RIGHT + UP))
self.play(mob.animate.to_edge(UP))
self.play(mob.animate.to_corner(UR))
self.play(mob.animate.next_to(other, RIGHT, buff=0.5))
self.play(MoveAlongPath(mob, path))     # Follow a VMobject path
self.play(Rotate(mob, angle=PI))        # Rotate in place
self.play(Rotate(mob, angle=PI, about_point=ORIGIN))  # Rotate about point
```

## Emphasis Animations

```python
self.play(Indicate(mob))               # Brief scale+color flash
self.play(Wiggle(mob))                 # Wiggle side to side
self.play(Flash(point))                # Flash of light at point
self.play(Circumscribe(mob))           # Draw circle around
self.play(FocusOn(point))              # Focus ring on point
self.play(ShowPassingFlash(mob))       # Light sweep along path
self.play(ApplyWave(mob))             # Wave distortion
```

## Timing & Grouping

```python
# Control speed
self.play(Create(mob), run_time=2)

# Pause
self.wait(1)  # Wait 1 second

# Simultaneous animations
self.play(Create(a), Write(b), FadeIn(c))

# Staggered animations
self.play(AnimationGroup(
    Create(a), Create(b), Create(c),
    lag_ratio=0.3  # Each starts 0.3 of previous duration later
))

# Succession (one after another in single play call)
self.play(Succession(
    Create(a), Create(b), Create(c)
))

# Rate functions (easing)
self.play(Create(mob), rate_func=smooth)          # Default
self.play(Create(mob), rate_func=linear)
self.play(Create(mob), rate_func=rush_into)
self.play(Create(mob), rate_func=rush_from)
self.play(Create(mob), rate_func=there_and_back)
self.play(Create(mob), rate_func=wiggle)
```

## Updaters

```python
# Value tracker for dynamic animations
t = ValueTracker(0)
dot = always_redraw(lambda: Dot(axes.c2p(t.get_value(), np.sin(t.get_value()))))
self.play(t.animate.set_value(2*PI), run_time=3)

# Add updater to existing object
label.add_updater(lambda m: m.next_to(dot, UP))

# Remove updater
label.clear_updaters()
```

## Camera Animations (MovingCameraScene)

```python
class MyScene(MovingCameraScene):
    def construct(self):
        self.play(self.camera.frame.animate.scale(0.5))  # Zoom in
        self.play(self.camera.frame.animate.move_to(point))  # Pan
        self.play(self.camera.frame.animate.set_width(8))  # Set width
```

## 3D Animations (ThreeDScene)

```python
class My3DScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.play(Create(surface))
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=60*DEGREES, theta=30*DEGREES, run_time=2)
```
