---
description: Render an existing Manim scene file to video
allowed-tools: Read, Bash(manim:*), Bash(python:*), Bash(cd:*), Bash(ls:*), Glob
argument-hint: <file.py> [SceneName] [--quality ql|qm|qh|qk]
---

Render an existing Manim scene file to video.

## Arguments

Parse `$ARGUMENTS` for:
- **File path** (required): The `.py` file containing the scene. If just a filename, look in `C:/Users/anton/manim-workspace/`.
- **Scene name** (optional): The class name to render. If omitted, list available Scene classes in the file and ask the user which one.
- **Quality** (optional): `--quality ql` (480p), `--quality qm` (720p, default), `--quality qh` (1080p), `--quality qk` (4K).

## Process

1. Read the scene file to verify it exists and identify available Scene classes.
2. If no scene name was given, list the available classes and ask which to render.
3. Render using:
   ```
   cd C:/Users/anton/manim-workspace && .venv/Scripts/python -m manim -<quality> <file> <SceneName>
   ```
   Default quality is `-qm`.
4. If rendering fails, show the error and suggest fixes.
5. Report the output MP4 path on success.
