---
description: Create a cartoon sequence video from a natural language description
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python:*), Bash(cd:*), Bash(ls:*), Bash(pip:*)
argument-hint: <describe your scene and dialogue in plain English>
model: opus
---

You are creating a cartoon sequence video. The user wants: **$ARGUMENTS**

## Workspace

The cartoon workspace is at `C:/Users/anton/cartoon-workspace`. All scene files MUST be written there.

## Process

### Step 0: Check Setup

Before anything else, verify the workspace is ready:
```
ls C:/Users/anton/cartoon-workspace/cartoon_engine.py
ls C:/Users/anton/cartoon-workspace/characters/engineer/standing.png
```

If either is missing, run setup first:
```
cd C:/Users/anton/cartoon-workspace && python setup_cartoon.py
```

### Step 1: Parse the Scene

Read the user's description carefully and identify:
- **Characters** present: engineer, doctor, architect, project_manager (use exact names)
- **Setting/background**: office, hospital, construction_site, meeting_room (pick closest match)
- **Dialogue**: who says what, in order
- **Title**: short descriptive title for the scene

### Step 2: Write the Scene Script

Create a Python scene script at `C:/Users/anton/cartoon-workspace/scenes/scene_XXXX.py` (use a short descriptive name).

Use this exact format:

```python
# scenes/scene_NAME.py — Cartoon scene
import sys
sys.path.insert(0, 'C:/Users/anton/cartoon-workspace')
from cartoon_engine import CartoonScene, Character, Dialogue

scene = CartoonScene(
    title="Scene Title Here",
    background="office",          # office | hospital | construction_site | meeting_room
    resolution=(1280, 720),
    fps=24
)

engineer = Character("engineer", position="left")
doctor   = Character("doctor",   position="right")
# architect = Character("architect", position="center")
# project_manager = Character("project_manager", position="right")

scene.add_characters(engineer, doctor)

scene.play([
    Dialogue(engineer, "First line of dialogue here."),
    Dialogue(doctor,   "Response here."),
    Dialogue(engineer, "Continue as needed."),
])

scene.render(output="C:/Users/anton/cartoon-workspace/media/videos/scene_NAME.mp4")
```

**Rules:**
- Character names: `engineer`, `doctor`, `architect`, `project_manager`
- Positions: `left`, `center`, `right` (if 2 chars: left + right; if 3: left + center + right)
- Background must match exactly: `office`, `hospital`, `construction_site`, `meeting_room`
- Each `Dialogue()` entry is one spoken line — keep lines under 120 characters
- The `output` path must be under `C:/Users/anton/cartoon-workspace/media/videos/`

### Step 3: Run the Scene

```
cd C:/Users/anton/cartoon-workspace && python scenes/scene_NAME.py
```

Wait for it to complete. The engine will:
1. Generate audio for each line (edge-tts, requires internet)
2. Compose video frames (Pillow)
3. Assemble MP4 (MoviePy)

This takes 30-90 seconds depending on number of dialogue lines.

### Step 4: Report Output

Tell the user the full path to the MP4 file. Example:
> Your cartoon is ready: `C:/Users/anton/cartoon-workspace/media/videos/scene_NAME.mp4`

Also mention:
- How many lines of dialogue were rendered
- Which characters appeared
- How to re-run or modify the scene

## Troubleshooting

**Setup missing**: Run `python setup_cartoon.py` first.

**edge-tts error**: Requires internet connection. Check connectivity.

**Character not found**: Use exact names: `engineer`, `doctor`, `architect`, `project_manager`.

**Background not found**: Use exact names: `office`, `hospital`, `construction_site`, `meeting_room`.

**moviepy/pillow import error**: Run `pip install moviepy pillow edge-tts requests` in the workspace.

**Audio sync issues**: Reduce dialogue line length (under 100 chars works best).

If any error occurs, read the full traceback, fix the scene script, and re-run.
