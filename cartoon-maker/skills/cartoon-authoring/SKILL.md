---
name: cartoon-authoring
description: >
  Cartoon scene authoring knowledge for the cartoon-maker plugin. Use when the user asks to
  "create a cartoon", "make an animation", "produce a scene", "add a character", "write dialogue",
  or needs help with the cartoon_engine.py API, character placement, voice assignment, or
  background selection.
version: 0.1.0
---

# Cartoon-Maker Authoring Guide

Domain knowledge for creating cartoon sequence videos with the cartoon-maker engine.

## Workspace Setup

- **Workspace**: `C:/Users/anton/cartoon-workspace`
- **Engine**: `C:/Users/anton/cartoon-workspace/cartoon_engine.py`
- **Characters**: `C:/Users/anton/cartoon-workspace/characters/<name>/`
- **Backgrounds**: `C:/Users/anton/cartoon-workspace/backgrounds/`
- **Output**: `C:/Users/anton/cartoon-workspace/media/videos/`
- **Scenes**: `C:/Users/anton/cartoon-workspace/scenes/`

## Scene Structure

```python
import sys
sys.path.insert(0, 'C:/Users/anton/cartoon-workspace')
from cartoon_engine import CartoonScene, Character, Dialogue

scene = CartoonScene(
    title="My Scene",
    background="office",      # office | hospital | construction_site | meeting_room
    resolution=(1280, 720),   # or (640, 360) for preview
    fps=24                    # or 15 for preview
)

# Add characters (2-4 supported)
char = Character("engineer", position="left")
scene.add_characters(char)

# Define dialogue
scene.play([
    Dialogue(char, "Hello world!"),
])

# Render to MP4
scene.render(output="C:/Users/anton/cartoon-workspace/media/videos/my_scene.mp4")
```

Run with: `cd C:/Users/anton/cartoon-workspace && python scenes/my_scene.py`

## Characters

See `references/characters.md` for full character specs, visual descriptions, and voice mappings.

| Name | Visual Description | Voice |
|------|-------------------|-------|
| `engineer` | Hard hat, orange safety vest | en-US-GuyNeural |
| `doctor` | White coat, stethoscope | en-US-JennyNeural |
| `architect` | Black turtleneck, T-square ruler | en-US-DavisNeural |
| `project_manager` | Business suit, clipboard | en-US-JaneNeural |

## Positions

| Characters | Positions Used |
|-----------|----------------|
| 2 | `left`, `right` |
| 3 | `left`, `center`, `right` |
| 4 | `left`, `center-left`, `center-right`, `right` |

## Backgrounds

| Key | Scene | Colors |
|-----|-------|--------|
| `office` | Corporate office | Warm grey, window |
| `hospital` | Hospital corridor | Light blue/white, cross |
| `construction_site` | Building site | Yellow/orange, scaffolding |
| `meeting_room` | Conference room | Neutral, table |

## Dialogue Guidelines

- Each `Dialogue(character, "text")` = one spoken line with TTS audio
- Keep lines under 120 characters for speech bubble fit
- 1-2 sentences per line for natural pacing
- The speaker "steps forward" slightly — other characters dim
- Audio is generated via edge-tts (requires internet)

## Scene Rendering

- **Full quality**: resolution=(1280, 720), fps=24, ~30-90 seconds
- **Preview**: resolution=(640, 360), fps=15, preview=True, ~10-20 seconds (no audio)

## Detailed References

- **`references/characters.md`** — Character specs, DiceBear parameters, voice options
- **`references/scene-format.md`** — Complete scene script format with all options
- **`references/tts-reference.md`** — edge-tts voices, languages, and audio parameters
