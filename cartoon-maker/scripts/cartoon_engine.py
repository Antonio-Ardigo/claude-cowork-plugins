"""
cartoon_engine.py — Core rendering engine for the cartoon-maker plugin.

Creates cartoon sequence MP4 videos from structured scene definitions.

Pipeline:
  1. Load character PNGs from characters/<name>/
  2. Generate audio via edge-tts per dialogue line → WAV files in audio/
  3. Compose video frames: Pillow draws background + characters + speech bubbles
  4. MoviePy assembles frames + audio → MP4

Render a scene:
  cd C:/Users/anton/cartoon-workspace
  python scenes/my_scene.py
"""

import os
import sys
import math
import hashlib
import asyncio
import textwrap
import tempfile
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

WORKSPACE = Path(__file__).parent
CHARACTERS_DIR = WORKSPACE / "characters"
BACKGROUNDS_DIR = WORKSPACE / "backgrounds"
AUDIO_DIR = WORKSPACE / "audio"
MEDIA_DIR = WORKSPACE / "media" / "videos"

for d in [AUDIO_DIR, MEDIA_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Character configuration
# ---------------------------------------------------------------------------

CHARACTER_VOICES = {
    "engineer":        "en-US-GuyNeural",
    "doctor":          "en-US-JennyNeural",
    "architect":       "en-US-DavisNeural",
    "project_manager": "en-US-JaneNeural",
    "woman":           "en-US-AriaNeural",
    "baby_lady":       "en-US-JennyNeural",
}

BUILTIN_CHARACTERS = set(CHARACTER_VOICES.keys())

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

class Character:
    """Represents a character in the scene.

    Built-in characters (use by name):
        engineer, doctor, architect, project_manager

    Custom characters (any name, with optional attributes):
        Character("sharon", gender="female", skin_tone="dark", age="adult")
        Character("cyra",   gender="female", skin_tone="dark", age="baby")

    skin_tone: "light" | "medium" | "tan" | "dark" | "deep"
    gender:    "female" | "male" | "neutral"
    age:       "baby" | "child" | "adult" | "elder"
    """

    def __init__(
        self,
        name: str,
        position: str = "left",
        voice: Optional[str] = None,
        speaking_rate: str = "+0%",
        pitch: str = "+0Hz",
    ):
        valid_positions = ["left", "center-left", "center", "center-right", "right"]
        if position not in valid_positions:
            raise ValueError(
                f"Invalid position '{position}'. Choose from: {valid_positions}"
            )
        self.name = name
        self.position = position
        self.voice = voice or CHARACTER_VOICES.get(name, "en-US-AriaNeural")
        self.speaking_rate = speaking_rate
        # Raise pitch for baby_lady
        self.pitch = "+10Hz" if name == "baby_lady" and pitch == "+0Hz" else pitch

    def __repr__(self):
        return f"Character({self.name!r}, position={self.position!r})"


class Dialogue:
    """One line of spoken dialogue."""

    def __init__(
        self,
        character: Optional[Character],
        text: str,
        pause: float = 0.3,
    ):
        self.character = character  # None = narration (text at bottom, no audio char)
        self.text = text
        self.pause = pause  # Extra pause after this line (seconds)

    def __repr__(self):
        char_name = self.character.name if self.character else "NARRATOR"
        return f"Dialogue({char_name}, {self.text!r})"


class CartoonScene:
    """Full cartoon scene: characters + background + dialogue → MP4."""

    def __init__(
        self,
        title: str = "",
        background: str = "office",
        resolution: tuple = (1280, 720),
        fps: int = 24,
        preview: bool = False,
        show_title: bool = True,
        title_duration: float = 2.0,
        pause_between: float = 0.5,
        character_scale: float = 0.65,
    ):
        valid_bgs = ["office", "hospital", "construction_site", "meeting_room"]
        if background not in valid_bgs:
            raise ValueError(
                f"Unknown background '{background}'. Choose from: {valid_bgs}"
            )
        self.title = title
        self.background = background
        self.resolution = resolution
        self.fps = fps
        self.preview = preview
        self.show_title = show_title and bool(title)
        self.title_duration = title_duration
        self.pause_between = pause_between
        self.character_scale = character_scale
        self._characters: list[Character] = []
        self._dialogue: list[Dialogue] = []

    def add_characters(self, *characters: Character):
        """Add one or more characters to the scene."""
        for c in characters:
            self._characters.append(c)

    def play(self, dialogue: list[Dialogue]):
        """Set the dialogue sequence for the scene."""
        self._dialogue = list(dialogue)

    def render(self, output: str = ""):
        """Render the scene to an MP4 file."""
        if not output:
            output = str(MEDIA_DIR / "cartoon_output.mp4")
        output = str(output)
        os.makedirs(os.path.dirname(output), exist_ok=True)

        print(f"[cartoon-maker] Rendering scene: {self.title or 'Untitled'}")
        print(f"[cartoon-maker] Characters: {[c.name for c in self._characters]}")
        print(f"[cartoon-maker] Dialogue lines: {len(self._dialogue)}")
        print(f"[cartoon-maker] Preview mode: {self.preview}")

        # Generate audio files (unless preview)
        audio_files = []
        if not self.preview:
            print("[cartoon-maker] Generating audio...")
            audio_files = _generate_audio(self._dialogue)

        # Build video clips
        print("[cartoon-maker] Compositing frames...")
        clips = _build_clips(
            scene=self,
            dialogue=self._dialogue,
            audio_files=audio_files,
        )

        # Assemble and write MP4
        print(f"[cartoon-maker] Writing MP4 to {output} ...")
        _assemble_mp4(clips, output, self.fps)

        print(f"[cartoon-maker] Done! Output: {output}")
        return output


# ---------------------------------------------------------------------------
# Audio generation
# ---------------------------------------------------------------------------

def _audio_cache_path(voice: str, text: str, rate: str, pitch: str) -> Path:
    key = f"{voice}|{text}|{rate}|{pitch}"
    h = hashlib.md5(key.encode()).hexdigest()
    return AUDIO_DIR / f"{h}.mp3"


def _generate_audio(dialogue: list[Dialogue]) -> list[Optional[str]]:
    """Generate audio for each dialogue line. Returns list of mp3 paths (or None for narration)."""
    results = []
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        results = loop.run_until_complete(_generate_audio_async(dialogue))
    finally:
        loop.close()
    return results


async def _generate_audio_async(dialogue: list[Dialogue]) -> list[Optional[str]]:
    try:
        import edge_tts
    except ImportError:
        print("[cartoon-maker] edge-tts not installed — running in silent mode (word-count timing).")
        return [None] * len(dialogue)

    results = []
    tts_offline = False  # Set True on first network error; skip remaining lines

    for i, line in enumerate(dialogue):
        if line.character is None:
            results.append(None)
            continue

        if tts_offline:
            results.append(None)
            continue

        char = line.character
        path = _audio_cache_path(char.voice, line.text, char.speaking_rate, char.pitch)

        if not path.exists():
            print(f"  Generating audio [{i+1}/{len(dialogue)}]: {char.name} — {line.text[:50]}...")
            try:
                communicate = edge_tts.Communicate(
                    text=line.text,
                    voice=char.voice,
                    rate=char.speaking_rate,
                    pitch=char.pitch,
                )
                await communicate.save(str(path))
            except Exception as e:
                err = str(e).lower()
                if any(w in err for w in ["connect", "network", "timeout", "ssl", "name or service"]):
                    print(f"  [INFO] TTS network unavailable — switching to silent mode (word-count timing).")
                    tts_offline = True
                else:
                    print(f"  [WARNING] TTS failed for line {i+1}: {e}")
                results.append(None)
                continue
        else:
            print(f"  Using cached audio [{i+1}/{len(dialogue)}]: {char.name}")

        results.append(str(path))

    return results


# ---------------------------------------------------------------------------
# Video frame compositing
# ---------------------------------------------------------------------------

def _build_clips(scene: CartoonScene, dialogue: list[Dialogue], audio_files: list):
    """Build a list of (image_array, duration_seconds, audio_path) tuples."""
    from PIL import Image

    W, H = scene.resolution
    bg_img = _load_background(scene.background, W, H)

    # Load character images
    char_imgs = {}
    for c in scene._characters:
        char_imgs[c.name] = _load_character(c, H, scene.character_scale)

    # Title card
    clips = []
    if scene.show_title:
        title_frame = _render_title_card(bg_img.copy(), scene.title, W, H)
        clips.append((title_frame, scene.title_duration, None))

    # Intro frame (all characters standing, no speech)
    if scene._characters:
        intro_frame = _render_frame(
            bg=bg_img.copy(),
            characters=scene._characters,
            char_imgs=char_imgs,
            active_character=None,
            text="",
            char_name="",
            W=W, H=H,
        )
        clips.append((intro_frame, 1.0, None))

    # Dialogue frames
    for i, (line, audio_path) in enumerate(zip(dialogue, audio_files)):
        # Get audio duration — fall back to word-count estimate in silent mode
        audio_dur = _get_audio_duration(audio_path) if audio_path else _estimate_duration(line.text)
        frame_dur = audio_dur + scene.pause_between

        if line.character is None:
            # Narration
            frame = _render_frame(
                bg=bg_img.copy(),
                characters=scene._characters,
                char_imgs=char_imgs,
                active_character=None,
                text=line.text,
                char_name="",
                W=W, H=H,
                is_narration=True,
            )
        else:
            frame = _render_frame(
                bg=bg_img.copy(),
                characters=scene._characters,
                char_imgs=char_imgs,
                active_character=line.character,
                text=line.text,
                char_name=_display_name(line.character.name),
                W=W, H=H,
            )

        clips.append((frame, frame_dur, audio_path))

        # Brief pause frame after each line
        if line.pause > 0:
            pause_frame = _render_frame(
                bg=bg_img.copy(),
                characters=scene._characters,
                char_imgs=char_imgs,
                active_character=None,
                text="",
                char_name="",
                W=W, H=H,
            )
            clips.append((pause_frame, line.pause, None))

    # Outro frame
    outro_frame = _render_frame(
        bg=bg_img.copy(),
        characters=scene._characters,
        char_imgs=char_imgs,
        active_character=None,
        text="",
        char_name="",
        W=W, H=H,
    )
    clips.append((outro_frame, 1.5, None))

    return clips


def _get_audio_duration(audio_path: Optional[str]) -> float:
    """Get duration of an MP3 file in seconds. Returns 0.0 if unavailable."""
    if not audio_path or not os.path.exists(audio_path):
        return 0.0
    try:
        from moviepy import AudioFileClip
        clip = AudioFileClip(audio_path)
        dur = clip.duration
        clip.close()
        return dur
    except Exception:
        return 0.0


def _estimate_duration(text: str) -> float:
    """Estimate speech duration from word count (~130 words/min = 2.2 words/sec)."""
    words = len(text.split())
    return max(words / 2.2, 1.5)


def _display_name(name: str) -> str:
    return name.replace("_", " ").title()


# ---------------------------------------------------------------------------
# Frame rendering (Pillow)
# ---------------------------------------------------------------------------

def _load_background(bg_name: str, W: int, H: int):
    """Load or generate background image."""
    from PIL import Image
    path = BACKGROUNDS_DIR / f"{bg_name}.png"
    if path.exists():
        img = Image.open(path).convert("RGBA").resize((W, H))
    else:
        print(f"  [WARNING] Background '{bg_name}.png' not found, using generated fallback.")
        img = _generate_background(bg_name, W, H)
    return img


def _load_character(char, H: int, scale: float):
    """Load character PNG or generate procedurally. Accepts a Character object or name string."""
    from PIL import Image
    name = char.name if hasattr(char, 'name') else char
    char_h = int(H * scale)
    for variant in ["standing.png", "talking.png"]:
        path = CHARACTERS_DIR / name / variant
        if path.exists():
            img = Image.open(path).convert("RGBA")
            ratio = char_h / img.height
            char_w = int(img.width * ratio)
            return img.resize((char_w, char_h), Image.LANCZOS)
    return _generate_placeholder_character(name, H, scale)


def _render_frame(
    bg,
    characters: list,
    char_imgs: dict,
    active_character: Optional[Character],
    text: str,
    char_name: str,
    W: int,
    H: int,
    is_narration: bool = False,
):
    """Render a single frame as a PIL Image."""
    from PIL import Image, ImageDraw, ImageFont

    frame = bg.copy()

    # Position map for characters
    positions = _character_positions(characters, W, H)

    # Draw characters
    for char in characters:
        img = char_imgs.get(char.name)
        if img is None:
            continue

        x, y = positions[char.name]

        # Dim non-speaking characters
        if active_character and char.name != active_character.name:
            dimmed = img.copy()
            r, g, b, a = dimmed.split()
            a = a.point(lambda v: int(v * 0.45))
            dimmed = Image.merge("RGBA", (r, g, b, a))
            # Slightly shrink non-speaking chars
            scale = 0.92
            nw, nh = int(img.width * scale), int(img.height * scale)
            dimmed = dimmed.resize((nw, nh), Image.LANCZOS)
            px = x - nw // 2
            py = y - nh
            frame.paste(dimmed, (px, py), dimmed)
        else:
            # Active or neutral — full size, slight lift
            lift = 8 if active_character and char.name == active_character.name else 0
            px = x - img.width // 2
            py = y - img.height - lift
            frame.paste(img, (px, py), img)

    # Convert to RGB for drawing text on top
    frame_rgb = Image.new("RGB", (W, H), (255, 255, 255))
    frame_rgb.paste(frame, mask=frame.split()[3] if frame.mode == 'RGBA' else None)

    draw = ImageDraw.Draw(frame_rgb)

    # Draw speech bubble + text
    if text:
        if is_narration:
            _draw_narration_bar(draw, text, W, H)
        elif active_character:
            speaker_x, _ = positions[active_character.name]
            _draw_speech_bubble(draw, text, char_name, speaker_x, W, H)

    return frame_rgb


def _character_positions(characters: list, W: int, H: int) -> dict:
    """Compute (center_x, bottom_y) for each character based on position field."""
    position_map = {
        "left":         0.18,
        "center-left":  0.35,
        "center":       0.50,
        "center-right": 0.65,
        "right":        0.82,
    }
    ground_y = int(H * 0.88)
    result = {}
    for char in characters:
        x_frac = position_map.get(char.position, 0.5)
        result[char.name] = (int(W * x_frac), ground_y)
    return result


def _draw_speech_bubble(draw, text: str, char_name: str, speaker_x: int, W: int, H: int):
    """Draw a speech bubble with the dialogue text."""
    from PIL import ImageFont

    # Bubble geometry
    bubble_w = int(W * 0.55)
    bubble_x = max(10, min(speaker_x - bubble_w // 2, W - bubble_w - 10))
    bubble_y = int(H * 0.05)
    padding = 16
    corner_r = 14
    tail_h = 18

    # Wrap text
    font_size = max(18, int(H * 0.032))
    font = _get_font(font_size)
    name_font = _get_font(int(font_size * 0.85), bold=True)

    wrapped = textwrap.fill(text, width=max(20, bubble_w // (font_size // 2 + 1)))
    lines = wrapped.split("\n")
    line_h = font_size + 6
    text_h = len(lines) * line_h + (name_font.size + 8 if char_name else 0)
    bubble_h = text_h + padding * 2 + tail_h

    # Clamp bubble position
    bubble_x = max(10, min(bubble_x, W - bubble_w - 10))

    # White rounded rectangle
    _draw_rounded_rect(draw,
        [bubble_x, bubble_y, bubble_x + bubble_w, bubble_y + bubble_h],
        corner_r, fill=(255, 255, 255, 230), outline=(60, 60, 60), outline_width=2
    )

    # Tail (triangle pointing down toward speaker)
    tail_x = max(bubble_x + 20, min(speaker_x, bubble_x + bubble_w - 20))
    draw.polygon([
        (tail_x - 12, bubble_y + bubble_h - 2),
        (tail_x + 12, bubble_y + bubble_h - 2),
        (tail_x, bubble_y + bubble_h + tail_h),
    ], fill=(255, 255, 255), outline=(60, 60, 60))

    # Character name (bold, colored)
    cy = bubble_y + padding
    if char_name:
        name_color = _char_name_color(char_name)
        draw.text((bubble_x + padding, cy), char_name + ":", font=name_font, fill=name_color)
        cy += name_font.size + 8

    # Dialogue text
    for line in lines:
        draw.text((bubble_x + padding, cy), line, font=font, fill=(20, 20, 20))
        cy += line_h


def _draw_narration_bar(draw, text: str, W: int, H: int):
    """Draw a narration bar at the bottom of the frame."""
    from PIL import ImageFont
    font_size = max(18, int(H * 0.030))
    font = _get_font(font_size)
    bar_h = font_size * 2 + 24
    bar_y = H - bar_h - 10
    draw.rectangle([0, bar_y, W, H], fill=(0, 0, 0, 180))
    wrapped = textwrap.fill(text, width=80)
    draw.text((W // 2, bar_y + bar_h // 2), wrapped, font=font, fill=(255, 255, 220), anchor="mm")


def _draw_rounded_rect(draw, coords, radius, fill, outline, outline_width=2):
    """Draw a rounded rectangle using Pillow."""
    x0, y0, x1, y1 = coords
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill, outline=outline, width=outline_width)


def _char_name_color(name: str) -> tuple:
    colors = {
        "Engineer":        (180, 90, 0),
        "Doctor":          (0, 100, 160),
        "Architect":       (60, 60, 60),
        "Project Manager": (80, 0, 120),
    }
    return colors.get(name, (40, 40, 40))


def _render_title_card(bg, title: str, W: int, H: int):
    """Render a title card frame."""
    from PIL import Image, ImageDraw, ImageFont
    frame = bg.copy()
    # Dark overlay
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 160))
    frame.paste(overlay, mask=overlay)
    frame_rgb = frame.convert("RGB")
    draw = ImageDraw.Draw(frame_rgb)
    font = _get_font(int(H * 0.07), bold=True)
    draw.text((W // 2, H // 2), title, font=font, fill=(255, 255, 240), anchor="mm")
    return frame_rgb


def _get_font(size: int, bold: bool = False):
    """Load a system font at the given size, fallback to default."""
    from PIL import ImageFont
    font_paths = [
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibri.ttf",
        "C:/Windows/Fonts/segoeui.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    bold_paths = [
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/calibrib.ttf",
        "C:/Windows/Fonts/segoeuib.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]
    paths = bold_paths if bold else font_paths
    for path in paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


# ---------------------------------------------------------------------------
# Procedural character generation (fallback if PNGs not downloaded)
# ---------------------------------------------------------------------------

def _generate_placeholder_character(name: str, H: int, scale: float):
    """Draw a simple but recognizable stick-figure-style character as fallback."""
    from PIL import Image, ImageDraw, ImageFont

    char_h = int(H * scale)
    char_w = int(char_h * 0.6)
    img = Image.new("RGBA", (char_w, char_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Color scheme per character
    colors = {
        "engineer":        {"skin": (255, 213, 170), "outfit": (245, 130, 32),  "hat": (255, 215, 0)},
        "doctor":          {"skin": (255, 213, 170), "outfit": (230, 230, 255), "hat": (220, 220, 220)},
        "architect":       {"skin": (255, 213, 170), "outfit": (40, 40, 60),    "hat": (40, 40, 60)},
        "project_manager": {"skin": (255, 213, 170), "outfit": (30, 58, 95),    "hat": (30, 58, 95)},
        "woman":           {"skin": (110, 65, 35),   "outfit": (255, 80, 140),  "hat": (25, 15, 8)},
        "baby_lady":       {"skin": (110, 65, 35),   "outfit": (255, 182, 193), "hat": (25, 15, 8)},
    }
    c = colors.get(name, {"skin": (255, 213, 170), "outfit": (100, 100, 200), "hat": (50, 50, 100)})

    cx = char_w // 2
    u = char_h // 10  # unit

    # Body
    draw.ellipse([cx - u*1.3, u*1, cx + u*1.3, u*3.6], fill=c["skin"])           # Head
    draw.rounded_rectangle([cx - u*1.5, u*3.8, cx + u*1.5, u*7.5], radius=6, fill=c["outfit"])  # Torso
    draw.rectangle([cx - u*1.4, u*7.5, cx - u*0.3, u*9.8], fill=c["outfit"])     # Left leg
    draw.rectangle([cx + u*0.3, u*7.5, cx + u*1.4, u*9.8], fill=c["outfit"])     # Right leg

    # Arms
    draw.line([(cx - u*1.5, u*4.2), (cx - u*3, u*5.8)], fill=c["skin"], width=max(3, u//2))
    draw.line([(cx + u*1.5, u*4.2), (cx + u*3, u*5.8)], fill=c["skin"], width=max(3, u//2))

    # Profession-specific accessories
    if name == "engineer":
        # Hard hat
        draw.ellipse([cx - u*1.6, u*0.5, cx + u*1.6, u*2.0], fill=c["hat"])
        draw.rectangle([cx - u*1.9, u*1.6, cx + u*1.9, u*2.1], fill=c["hat"])
        # Orange vest stripes
        draw.rectangle([cx - u*1.4, u*4.0, cx + u*1.4, u*4.4], fill=(255, 200, 0))
        draw.rectangle([cx - u*1.4, u*5.5, cx + u*1.4, u*5.9], fill=(255, 200, 0))

    elif name == "doctor":
        # White coat lapels
        draw.polygon([
            (cx - u*1.5, u*3.8), (cx - u*0.3, u*5.0), (cx - u*1.5, u*7.5)
        ], fill=(250, 250, 255))
        draw.polygon([
            (cx + u*1.5, u*3.8), (cx + u*0.3, u*5.0), (cx + u*1.5, u*7.5)
        ], fill=(250, 250, 255))
        # Stethoscope
        draw.arc([cx - u*1.0, u*3.5, cx + u*1.0, u*5.5], 200, 340, fill=(80, 80, 80), width=max(2, u//3))
        draw.ellipse([cx - u*0.3, u*5.3, cx + u*0.3, u*5.9], fill=(80, 80, 80))

    elif name == "architect":
        # Black glasses
        draw.rectangle([cx - u*1.1, u*1.8, cx - u*0.2, u*2.4], outline=(20, 20, 20), width=2)
        draw.rectangle([cx + u*0.2, u*1.8, cx + u*1.1, u*2.4], outline=(20, 20, 20), width=2)
        draw.line([(cx - u*0.2, u*2.1), (cx + u*0.2, u*2.1)], fill=(20, 20, 20), width=2)
        # Rolled blueprints under arm
        draw.ellipse([cx - u*3.2, u*5.5, cx - u*2.5, u*6.3], fill=(200, 200, 255), outline=(100, 100, 200))
        draw.rectangle([cx - u*3.3, u*5.8, cx - u*1.5, u*6.0], fill=(200, 200, 255))

    elif name == "project_manager":
        # Tie
        draw.polygon([
            (cx - u*0.3, u*3.9), (cx + u*0.3, u*3.9),
            (cx + u*0.5, u*5.5), (cx, u*6.5), (cx - u*0.5, u*5.5)
        ], fill=(150, 30, 30))
        # Clipboard
        draw.rectangle([cx + u*1.8, u*4.0, cx + u*3.2, u*6.5], fill=(220, 180, 120), outline=(160, 120, 60))
        draw.rectangle([cx + u*2.0, u*4.3, cx + u*3.0, u*4.6], fill=(200, 160, 100))
        draw.line([(cx + u*2.0, u*5.0), (cx + u*3.0, u*5.0)], fill=(80, 60, 40), width=2)
        draw.line([(cx + u*2.0, u*5.5), (cx + u*3.0, u*5.5)], fill=(80, 60, 40), width=2)
        draw.line([(cx + u*2.0, u*6.0), (cx + u*3.0, u*6.0)], fill=(80, 60, 40), width=2)

    elif name == "woman":
        # Young woman — side braids, cropped top + jeans
        hair = c["hat"]
        braid_color = (35, 20, 8)
        # Side braids hanging down
        draw.rounded_rectangle([cx - u*2.2, u*1.2, cx - u*1.4, u*5.5], radius=4, fill=braid_color)
        draw.rounded_rectangle([cx + u*1.4, u*1.2, cx + u*2.2, u*5.5], radius=4, fill=braid_color)
        # Bead at end of each braid
        draw.ellipse([cx - u*2.0, u*5.3, cx - u*1.6, u*5.7], fill=(200, 170, 50))
        draw.ellipse([cx + u*1.6, u*5.3, cx + u*2.0, u*5.7], fill=(200, 170, 50))
        # Top hair
        draw.ellipse([cx - u*1.3, u*0.8, cx + u*1.3, u*2.0], fill=braid_color)
        # Cropped top (bright youthful colour)
        draw.rounded_rectangle([cx - u*1.5, u*3.8, cx + u*1.5, u*6.0], radius=5, fill=c["outfit"])
        # Jeans
        draw.rectangle([cx - u*1.4, u*6.0, cx - u*0.2, u*9.8], fill=(50, 80, 160))
        draw.rectangle([cx + u*0.2, u*6.0, cx + u*1.4, u*9.8], fill=(50, 80, 160))
        # Small gold hoop earrings
        draw.ellipse([cx - u*1.3, u*2.1, cx - u*0.9, u*2.5], outline=(200, 170, 50), width=2)
        draw.ellipse([cx + u*0.9, u*2.1, cx + u*1.3, u*2.5], outline=(200, 170, 50), width=2)

    elif name == "baby_lady":
        # Baby proportions — oversized head, tiny body
        draw.ellipse([cx - u*1.6, u*0.5, cx + u*1.6, u*4.0], fill=c["skin"])
        draw.rounded_rectangle([cx - u, u*4.2, cx + u, u*6.8], radius=6, fill=c["outfit"])
        draw.rectangle([cx - u*0.9, u*6.8, cx - u*0.2, u*8.5], fill=c["outfit"])
        draw.rectangle([cx + u*0.2, u*6.8, cx + u*0.9, u*8.5], fill=c["outfit"])
        draw.line([(cx - u, u*4.6), (cx - u*2, u*5.8)], fill=c["skin"], width=max(2, u//3))
        draw.line([(cx + u, u*4.6), (cx + u*2, u*5.8)], fill=c["skin"], width=max(2, u//3))
        # Hair bow
        draw.polygon([(cx - u*0.6, u*0.4), (cx, u*0.6), (cx - u*1.4, u*1.0)], fill=(255, 100, 150))
        draw.polygon([(cx + u*0.6, u*0.4), (cx, u*0.6), (cx + u*1.4, u*1.0)], fill=(255, 100, 150))
        draw.ellipse([cx - u*0.25, u*0.5, cx + u*0.25, u*0.9], fill=(255, 100, 150))
        # Baby face — big eyes + rosy cheeks
        eye_y = int(u * 2.0)
        draw.ellipse([cx - u*1.0, eye_y, cx - u*0.3, eye_y + int(u*0.7)], fill=(40, 25, 10))
        draw.ellipse([cx + u*0.3, eye_y, cx + u*1.0, eye_y + int(u*0.7)], fill=(40, 25, 10))
        draw.ellipse([cx - u*1.4, u*2.6, cx - u*0.6, u*3.2], fill=(220, 100, 100, 80))
        draw.ellipse([cx + u*0.6, u*2.6, cx + u*1.4, u*3.2], fill=(220, 100, 100, 80))
        draw.arc([cx - u*0.6, u*2.8, cx + u*0.6, u*3.6], 20, 160, fill=(150, 60, 40), width=max(2, u//4))
        return img  # baby face already drawn — skip generic face below

    # Face (eyes + smile) for all non-baby characters
    eye_y = int(u * 2.2)
    draw.ellipse([cx - u, eye_y, cx - u//2, eye_y + u//2], fill=(40, 40, 40))
    draw.ellipse([cx + u//2, eye_y, cx + u, eye_y + u//2], fill=(40, 40, 40))
    draw.arc([cx - u*0.8, u*2.5, cx + u*0.8, u*3.2], 20, 160, fill=(80, 40, 20), width=max(2, u//4))

    return img


# ---------------------------------------------------------------------------
# Background generation
# ---------------------------------------------------------------------------

def _generate_background(name: str, W: int, H: int):
    """Generate a simple colored background for the given setting."""
    from PIL import Image, ImageDraw
    img = Image.new("RGBA", (W, H), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    if name == "office":
        # Warm grey walls, wooden floor
        draw.rectangle([0, 0, W, int(H * 0.75)], fill=(210, 205, 195))
        draw.rectangle([0, int(H * 0.75), W, H], fill=(160, 120, 80))
        # Windows
        for wx in [int(W * 0.15), int(W * 0.55)]:
            draw.rectangle([wx, int(H*0.1), wx+120, int(H*0.55)], fill=(180, 210, 240), outline=(140, 120, 100), width=4)
            draw.line([(wx+60, int(H*0.1)), (wx+60, int(H*0.55))], fill=(140, 120, 100), width=3)
            draw.line([(wx, int(H*0.33)), (wx+120, int(H*0.33))], fill=(140, 120, 100), width=3)
        # Floor line
        draw.rectangle([0, int(H*0.75), W, int(H*0.77)], fill=(120, 90, 55))

    elif name == "hospital":
        # Light blue/white corridor
        draw.rectangle([0, 0, W, int(H * 0.78)], fill=(230, 240, 250))
        draw.rectangle([0, int(H * 0.78), W, H], fill=(220, 220, 220))
        # Red cross sign
        cx, cy, cs = int(W * 0.85), int(H * 0.18), 35
        draw.rectangle([cx - cs//3, cy - cs, cx + cs//3, cy + cs], fill=(220, 30, 30))
        draw.rectangle([cx - cs, cy - cs//3, cx + cs, cy + cs//3], fill=(220, 30, 30))
        # Door
        draw.rectangle([int(W*0.42), int(H*0.38), int(W*0.58), int(H*0.78)], fill=(200, 175, 140), outline=(160, 130, 100), width=3)
        draw.ellipse([int(W*0.543), int(H*0.56), int(W*0.557), int(H*0.58)], fill=(200, 160, 30))
        # Baseboard
        draw.rectangle([0, int(H*0.77), W, int(H*0.80)], fill=(200, 200, 200))

    elif name == "construction_site":
        # Sky, ground, scaffolding
        draw.rectangle([0, 0, W, int(H * 0.65)], fill=(210, 175, 100))  # warm sky
        draw.rectangle([0, int(H * 0.65), W, H], fill=(140, 115, 80))   # dirt ground
        # Scaffolding
        for sx in [int(W*0.05), int(W*0.65)]:
            for gy in range(int(H*0.15), int(H*0.65), int(H*0.14)):
                draw.rectangle([sx, gy, sx + int(W*0.22), gy + 8], fill=(210, 160, 50))
            for vx in [sx, sx + int(W*0.11), sx + int(W*0.22)]:
                draw.rectangle([vx, int(H*0.15), vx + 8, int(H*0.65)], fill=(190, 145, 45))
        # Safety barrier
        draw.rectangle([0, int(H*0.82), W, int(H*0.86)], fill=(255, 165, 0))
        for bx in range(0, W, 60):
            draw.rectangle([bx, int(H*0.82), bx+30, int(H*0.86)], fill=(20, 20, 20))

    elif name == "meeting_room":
        # Neutral walls, conference table
        draw.rectangle([0, 0, W, int(H * 0.72)], fill=(235, 228, 218))
        draw.rectangle([0, int(H * 0.72), W, H], fill=(100, 75, 50))
        # Conference table
        tw, th = int(W * 0.65), int(H * 0.14)
        tx, ty = (W - tw) // 2, int(H * 0.62)
        draw.ellipse([tx, ty, tx + tw, ty + th], fill=(140, 100, 65), outline=(100, 70, 40), width=3)
        # Whiteboard
        draw.rectangle([int(W*0.3), int(H*0.08), int(W*0.7), int(H*0.42)], fill=(245, 245, 240), outline=(160, 150, 140), width=4)
        draw.rectangle([int(W*0.32), int(H*0.10), int(W*0.68), int(H*0.40)], fill=(250, 250, 248))

    return img


# ---------------------------------------------------------------------------
# MP4 assembly
# ---------------------------------------------------------------------------

def _assemble_mp4(clips: list, output: str, fps: int):
    """Assemble a list of (PIL_image, duration, audio_path) into an MP4."""
    try:
        from moviepy import ImageClip, AudioFileClip, CompositeAudioClip, concatenate_videoclips
    except ImportError:
        print("[ERROR] moviepy not installed. Run: pip install moviepy")
        sys.exit(1)

    import numpy as np

    video_clips = []
    for frame_img, duration, audio_path in clips:
        arr = np.array(frame_img.convert("RGB"))
        clip = ImageClip(arr, duration=duration)

        if audio_path and os.path.exists(audio_path):
            try:
                audio = AudioFileClip(audio_path)
                # Only clip audio duration if strictly needed — never extend beyond actual duration
                safe_dur = min(audio.duration, duration)
                audio = audio.subclipped(0, safe_dur)
                clip = clip.with_audio(audio)
            except Exception as e:
                print(f"  [WARNING] Could not attach audio: {e}")

        video_clips.append(clip)

    final = concatenate_videoclips(video_clips, method="compose")
    final.write_videofile(
        output,
        fps=fps,
        codec="libx264",
        audio_codec="aac",
        logger=None,
    )
    final.close()
