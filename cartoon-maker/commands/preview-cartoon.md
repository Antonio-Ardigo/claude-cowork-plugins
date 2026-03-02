---
description: Quick low-quality preview of a cartoon scene from a natural language description
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python:*), Bash(cd:*), Bash(ls:*), Bash(pip:*)
argument-hint: <describe your scene and dialogue in plain English>
model: opus
---

You are creating a **quick preview** cartoon video (640×360, no audio). The user wants: **$ARGUMENTS**

## Workspace

The cartoon workspace is at `C:/Users/anton/cartoon-workspace`.

## Process

### Step 0: Check Setup

Verify workspace is ready:
```
ls C:/Users/anton/cartoon-workspace/cartoon_engine.py
```
If missing, run: `cd C:/Users/anton/cartoon-workspace && python setup_cartoon.py`

### Step 1: Parse the Scene

Identify characters, setting, and dialogue from the user's description.

### Step 2: Write Preview Scene Script

Create `C:/Users/anton/cartoon-workspace/scenes/preview_XXXX.py`:

```python
# scenes/preview_NAME.py — Quick preview (no audio)
import sys
sys.path.insert(0, 'C:/Users/anton/cartoon-workspace')
from cartoon_engine import CartoonScene, Character, Dialogue

scene = CartoonScene(
    title="Preview",
    background="office",
    resolution=(640, 360),    # Low resolution for speed
    fps=15,
    preview=True              # Skips audio generation
)

engineer = Character("engineer", position="left")
doctor   = Character("doctor",   position="right")

scene.add_characters(engineer, doctor)

scene.play([
    Dialogue(engineer, "First line."),
    Dialogue(doctor,   "Response."),
])

scene.render(output="C:/Users/anton/cartoon-workspace/media/videos/preview_NAME.mp4")
```

### Step 3: Run Preview

```
cd C:/Users/anton/cartoon-workspace && python scenes/preview_NAME.py
```

Preview renders in ~10-20 seconds (no audio generation, lower resolution).

### Step 4: Report

Tell the user the preview path and suggest using `/create-cartoon` for the full quality version with audio.
