# cartoon-maker Plugin

Create cartoon sequence videos with human characters from natural language descriptions.

## Features

- **Human characters** — Engineer, Doctor, Architect, Project Manager with distinct visual styles (Open Peeps hand-drawn style)
- **Natural language input** — Describe your scene and dialogue in plain English
- **Synchronized audio** — Each character has a unique neural TTS voice (Microsoft edge-tts)
- **Multiple settings** — Office, hospital, construction site, meeting room backgrounds
- **MP4 output** — 1280×720 video ready to play or share

## Quick Start

```
/create-cartoon The engineer and doctor meet at the hospital to discuss the new wing project.
Engineer says: "We need to finalize the structural layout before construction starts."
Doctor replies: "Patient flow and safety are our top priorities in the design."
Engineer: "I'll have the updated drawings ready by Thursday."
Doctor: "Perfect. Let's review them with the architect on Friday."
```

## Commands

| Command | Description |
|---------|-------------|
| `/create-cartoon <description>` | Full quality 1280×720 MP4 with synchronized audio |
| `/preview-cartoon <description>` | Quick 640×360 preview, no audio, renders in ~10-20s |

## Characters

| Character | Visual | Voice |
|-----------|--------|-------|
| Engineer | Hard hat, orange vest | en-US-GuyNeural |
| Doctor | White coat, stethoscope | en-US-JennyNeural |
| Architect | Black turtleneck, T-square | en-US-DavisNeural |
| Project Manager | Business suit, clipboard | en-US-JaneNeural |

## Backgrounds

`office` · `hospital` · `construction_site` · `meeting_room`

## Requirements

- **Internet**: Required for TTS audio (edge-tts)
- **Python**: 3.9+ (uses the system Python or venv)
- **Dependencies**: `moviepy`, `pillow`, `edge-tts`, `requests` (installed during setup)
- **Storage**: ~50MB for character assets + generated videos

## Workspace

All files are stored at `C:/Users/anton/cartoon-workspace/`:
- `cartoon_engine.py` — Core rendering engine
- `characters/` — Character PNG assets
- `backgrounds/` — Background images
- `scenes/` — Generated scene scripts
- `media/videos/` — Output MP4 files

## First Time Setup

The first `/create-cartoon` command automatically runs setup if needed. You can also run manually:
```
python C:/Users/anton/cartoon-workspace/setup_cartoon.py
```

## Technology Stack

| Component | Tool |
|-----------|------|
| Character art | DiceBear Open Peeps (CC0) → local PNG |
| Video composition | MoviePy 2.0 + Pillow |
| Text-to-speech | edge-tts (Microsoft neural voices) |
| Speech bubbles | Pillow ImageDraw |
| Final encoding | ffmpeg (via MoviePy) |
