# Manim Video Creator

Create mathematical animation videos using Manim Community Edition. Describe what you want and get a rendered MP4.

## Components

### Commands

| Command | Description |
|---------|-------------|
| `/create-video <description>` | Create a new Manim animation from a text description |
| `/render-scene <file> [Scene] [--quality]` | Render an existing scene file to video |
| `/preview-scene <file> [Scene]` | Quick 480p preview for fast iteration |

### Skills

- **manim-authoring** — Manim CE 0.20.0 API knowledge, animation patterns, and scene templates. Auto-triggers when discussing video creation, animation, or visualization.

### Agents

- **scene-builder** — Iterative scene design agent for building and refining complex animations.

## Setup

This plugin requires:

- **Manim workspace** at `C:/Users/anton/manim-workspace` with a Python venv
- **Manim CE 0.20.0** installed in the venv
- **ffmpeg** available on PATH
- **MiKTeX** (LaTeX) for mathematical formula rendering

All of these are already configured in the workspace.

## Usage

```
# Create a video from a description
/create-video an animation showing the quadratic formula being derived step by step

# Render an existing scene
/render-scene example_scene.py HelloManim

# Quick preview
/preview-scene example_scene.py SinePlot
```

## Output

Rendered videos are saved to `manim-workspace/media/videos/<filename>/<quality>/`.

| Quality | Flag | Resolution | FPS |
|---------|------|-----------|-----|
| Low | `-ql` | 480p | 15 |
| Medium | `-qm` | 720p | 30 |
| High | `-qh` | 1080p | 60 |
| 4K | `-qk` | 2160p | 60 |
