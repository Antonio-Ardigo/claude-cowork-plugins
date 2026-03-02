# Scene Script Format Reference

## Minimal Scene

```python
import sys
sys.path.insert(0, 'C:/Users/anton/cartoon-workspace')
from cartoon_engine import CartoonScene, Character, Dialogue

scene = CartoonScene(title="My Scene", background="office")

eng = Character("engineer", position="left")
doc = Character("doctor",   position="right")
scene.add_characters(eng, doc)

scene.play([
    Dialogue(eng, "Good morning, doctor."),
    Dialogue(doc, "Good morning! What's on the agenda today?"),
])

scene.render(output="C:/Users/anton/cartoon-workspace/media/videos/my_scene.mp4")
```

---

## Full CartoonScene Options

```python
scene = CartoonScene(
    title="Scene Title",          # Shown as title card at start (optional)
    background="office",          # Background key (see backgrounds below)
    resolution=(1280, 720),       # (width, height) — default 1280x720
    fps=24,                       # Frames per second — default 24
    preview=False,                # True = skip audio, fast render
    show_title=True,              # Show title card at beginning
    title_duration=2.0,           # Seconds to show title card
    pause_between=0.5,            # Pause seconds between dialogue lines
    character_scale=0.7,          # Character size relative to frame height
)
```

---

## Character Options

```python
char = Character(
    name="engineer",              # Must match: engineer|doctor|architect|project_manager
    position="left",              # left|center-left|center|center-right|right
    voice="en-US-GuyNeural",     # Override default voice (optional)
    speaking_rate="+0%",          # TTS rate: +10% faster, -10% slower (optional)
)
```

---

## Dialogue Options

```python
# Simple dialogue
Dialogue(char, "Text to speak and show in speech bubble.")

# With pause after
Dialogue(char, "Important statement.", pause=1.5)   # Extra 1.5s after this line

# Narration (no character, text shown at bottom)
Dialogue(None, "Meanwhile, at the construction site...")
```

---

## Background Keys

| Key | Description |
|-----|-------------|
| `office` | Corporate office, warm grey, windows |
| `hospital` | Hospital corridor, blue/white, red cross |
| `construction_site` | Outdoor site, yellow/orange sky, scaffolding |
| `meeting_room` | Conference room, neutral, long table |

---

## Positioning Layouts

### 2 Characters
```python
char1 = Character("engineer",      position="left")
char2 = Character("doctor",        position="right")
```

### 3 Characters
```python
char1 = Character("engineer",         position="left")
char2 = Character("architect",        position="center")
char3 = Character("project_manager",  position="right")
```

### 4 Characters
```python
char1 = Character("engineer",         position="left")
char2 = Character("doctor",           position="center-left")
char3 = Character("architect",        position="center-right")
char4 = Character("project_manager",  position="right")
```

---

## Multi-Scene Videos

To chain multiple scenes into one video, render each separately then combine:

```python
# scene_part1.py
scene1 = CartoonScene(title="Part 1", background="office")
# ... dialogue ...
scene1.render(output=".../part1.mp4")

# scene_part2.py
scene2 = CartoonScene(title="Part 2", background="hospital")
# ... dialogue ...
scene2.render(output=".../part2.mp4")
```

Then concatenate with MoviePy if needed (not yet built-in to engine).

---

## File Naming Conventions

- Scene scripts: `scenes/scene_<descriptive_name>.py`
- Output videos: `media/videos/<descriptive_name>.mp4`
- Preview videos: `media/videos/preview_<descriptive_name>.mp4`
- Use snake_case, no spaces
