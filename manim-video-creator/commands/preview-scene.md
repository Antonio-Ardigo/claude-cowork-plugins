---
description: Quick low-quality preview of a Manim scene
allowed-tools: Read, Bash(manim:*), Bash(python:*), Bash(cd:*), Bash(ls:*), Glob
argument-hint: <file.py> [SceneName]
---

Quickly render a low-quality preview of a Manim scene for fast iteration.

Parse `$ARGUMENTS` for the file path and optional scene name.

1. If just a filename, look in `C:/Users/anton/manim-workspace/`.
2. If no scene name given, read the file and list available Scene classes.
3. Render at lowest quality for speed:
   ```
   cd C:/Users/anton/manim-workspace && .venv/Scripts/python -m manim -ql <file> <SceneName>
   ```
4. Report the output path. Remind the user this is 480p/15fps — use `/render-scene` for higher quality.
