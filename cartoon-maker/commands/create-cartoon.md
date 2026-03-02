---
description: Create a cartoon sequence video from a natural language description
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python*), Bash(python3*), Bash(pip*), Bash(pip3*), Bash(mkdir*), Bash(cp*), Bash(ls*)
argument-hint: <describe your scene and dialogue in plain English>
model: opus
---

You are creating a cartoon sequence video. The user wants: **$ARGUMENTS**

## Step 0: Detect Environment

Run this first to detect Windows vs Linux (Cowork sandbox):

```bash
python3 -c "import sys, os; p='C:/Users/anton/cartoon-workspace'; print('PLATFORM:', sys.platform); print('WIN_WORKSPACE_EXISTS:', os.path.exists(p))"
```

- **Windows** (`PLATFORM: win32`, workspace exists): `WORKSPACE = C:/Users/anton/cartoon-workspace`
- **Linux/Cowork** (`PLATFORM: linux`): `WORKSPACE = ./cartoon_workspace`

## Step 0b: Linux/Cowork — Bootstrap Workspace (skip if Windows)

If on Linux, run these setup steps:

```bash
mkdir -p cartoon_workspace/audio cartoon_workspace/characters cartoon_workspace/backgrounds cartoon_workspace/media/videos cartoon_workspace/scenes
```

```bash
pip3 install moviepy pillow edge-tts requests --quiet
```

Install espeak-ng for offline TTS audio (works without internet):

```bash
apt-get install -y espeak-ng 2>/dev/null || echo "apt not available, espeak-ng may already be installed"
```

Find and copy the engine from the plugin directory:

```bash
python3 -c "
import shutil, os
CANDIDATES = [
    '/mnt/.claude/cowork_plugins/cache/claude-cowork-plugins/cartoon-maker/0.2.0/scripts/cartoon_engine.py',
    '/mnt/.claude/cowork_plugins/cache/claude-cowork-plugins/cartoon-maker/0.1.0/scripts/cartoon_engine.py',
    '/home/user/.claude/cowork_plugins/cache/claude-cowork-plugins/cartoon-maker/0.2.0/scripts/cartoon_engine.py',
]
for src in CANDIDATES:
    if os.path.exists(src):
        shutil.copy(src, 'cartoon_workspace/cartoon_engine.py')
        print('Copied engine from:', src)
        break
else:
    print('ENGINE_NOT_FOUND')
"
```

If `ENGINE_NOT_FOUND`, use the **Write** tool to write `cartoon_workspace/cartoon_engine.py` by reading the engine from: `/mnt/.claude/cowork_plugins/cache/claude-cowork-plugins/cartoon-maker/0.2.0/scripts/cartoon_engine.py`

Generate backgrounds (offline, no internet needed):

```bash
python3 -c "
import sys
sys.path.insert(0, 'cartoon_workspace')
from cartoon_engine import BACKGROUNDS_DIR, _generate_background
BACKGROUNDS_DIR.mkdir(parents=True, exist_ok=True)
for bg in ['office', 'hospital', 'construction_site', 'meeting_room']:
    path = BACKGROUNDS_DIR / f'{bg}.png'
    if not path.exists():
        img = _generate_background(bg, 1280, 720)
        img.save(str(path))
        print(f'Generated background: {bg}')
    else:
        print(f'Background exists: {bg}')
"
```

## Step 1: Parse the Scene

Read the user's description carefully and identify:
- **Characters** present: `engineer`, `doctor`, `architect`, `project_manager`, `woman`, `baby_lady`
- **Setting/background**: `office`, `hospital`, `construction_site`, `meeting_room`
- **Dialogue**: who says what, in order (keep each line under 120 characters)
- **Title**: short descriptive title

## Step 2: Write the Scene Script

**Windows** — write to `C:/Users/anton/cartoon-workspace/scenes/scene_NAME.py`:

```python
import sys
sys.path.insert(0, 'C:/Users/anton/cartoon-workspace')
from cartoon_engine import CartoonScene, Character, Dialogue

scene = CartoonScene(title="Scene Title", background="meeting_room", resolution=(1280, 720), fps=24)

engineer = Character("engineer", position="left")
doctor   = Character("doctor",   position="right")
scene.add_characters(engineer, doctor)

scene.play([
    Dialogue(engineer, "Hello, let me explain the situation."),
    Dialogue(doctor,   "I understand. What do you propose?"),
])

scene.render(output="C:/Users/anton/cartoon-workspace/media/videos/scene_NAME.mp4")
```

**Linux/Cowork** — write to `./cartoon_workspace/scenes/scene_NAME.py`:

```python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from cartoon_engine import CartoonScene, Character, Dialogue

scene = CartoonScene(title="Scene Title", background="meeting_room", resolution=(1280, 720), fps=24)

engineer = Character("engineer", position="left")
doctor   = Character("doctor",   position="right")
scene.add_characters(engineer, doctor)

scene.play([
    Dialogue(engineer, "Hello, let me explain the situation."),
    Dialogue(doctor,   "I understand. What do you propose?"),
])

scene.render(output="./cartoon_workspace/media/videos/scene_NAME.mp4")
```

**Character names:** `engineer`, `doctor`, `architect`, `project_manager`, `woman`, `baby_lady`
**Positions:** `left`, `center`, `right`
**Backgrounds:** `office`, `hospital`, `construction_site`, `meeting_room`

## Step 3: Run the Scene

**Windows:**
```bash
python C:/Users/anton/cartoon-workspace/scenes/scene_NAME.py
```

**Linux/Cowork:**
```bash
python3 cartoon_workspace/scenes/scene_NAME.py
```

The engine will:
1. Attempt TTS audio via edge-tts (requires internet). If network is unavailable, **automatically switches to silent mode** with word-count-based timing — no action needed.
2. Compose video frames (Pillow)
3. Assemble MP4 (MoviePy)

This takes 30–90 seconds.

## Step 4: Report Output

Tell the user the full path to the MP4 and mention:
- Number of dialogue lines rendered
- Characters in the scene
- Whether audio was generated or silent mode was used

## Troubleshooting

**Setup missing (Linux)**: Re-run Step 0b.
**Background missing**: Run the `_generate_background` snippet from Step 0b.
**`cartoon_engine.py` not found**: Use the Write tool to write it from the plugin's `scripts/cartoon_engine.py`.
**Character not found**: Use exact names: `engineer`, `doctor`, `architect`, `project_manager`, `woman`, `baby_lady`.
**moviepy/pillow import error**: Run `pip3 install moviepy pillow edge-tts requests`.
**TTS unavailable**: Engine automatically uses word-count timing — video renders without audio.
