# TTS Reference (edge-tts)

## Default Voice Assignments

| Character | Voice | Style |
|-----------|-------|-------|
| engineer | `en-US-GuyNeural` | Male, professional |
| doctor | `en-US-JennyNeural` | Female, warm and clear |
| architect | `en-US-DavisNeural` | Male, creative tone |
| project_manager | `en-US-JaneNeural` | Female, authoritative |

---

## Available English Voices (edge-tts)

### US English
| Voice | Gender | Style |
|-------|--------|-------|
| `en-US-GuyNeural` | Male | Neutral professional |
| `en-US-DavisNeural` | Male | Conversational |
| `en-US-TonyNeural` | Male | Clear narration |
| `en-US-JennyNeural` | Female | Warm, approachable |
| `en-US-JaneNeural` | Female | Professional |
| `en-US-AriaNeural` | Female | Expressive |
| `en-US-NancyNeural` | Female | Clear |

### British English
| Voice | Gender | Style |
|-------|--------|-------|
| `en-GB-RyanNeural` | Male | British accent |
| `en-GB-SoniaNeural` | Female | British accent |
| `en-GB-LibbyNeural` | Female | British accent |

### Australian English
| Voice | Gender | Style |
|-------|--------|-------|
| `en-AU-WilliamNeural` | Male | Australian accent |
| `en-AU-NatashaNeural` | Female | Australian accent |

---

## Voice Parameters

```python
char = Character(
    "engineer",
    voice="en-US-GuyNeural",
    speaking_rate="+0%",    # Range: -50% to +100%
    pitch="+0Hz",           # Range: -50Hz to +50Hz
    volume="+0%",           # Range: -50% to +50%
)
```

### Rate Examples
- `"+10%"` — Slightly faster (excited, enthusiastic)
- `"-10%"` — Slightly slower (serious, explaining)
- `"+20%"` — Noticeably faster (rushed, urgent)
- `"-20%"` — Deliberately slow (important, measured)

---

## Audio File Format

- Format: WAV (temporary), then embedded in MP4
- Sample rate: 24000 Hz
- Channels: Mono
- Cached in: `cartoon-workspace/audio/<hash>.wav`
- Cache is reused for identical text + voice combinations

---

## Internet Requirement

edge-tts requires an active internet connection to Microsoft's Azure servers.
Audio is cached locally after first generation — re-renders of the same dialogue reuse the cache.

For offline operation, use `preview=True` which skips audio entirely.

---

## Troubleshooting

**edge-tts timeout**: Check internet connection.
**Voice not found**: Use exact voice name from the table above.
**Audio distorted**: Try a different voice or reduce speaking rate.
**No audio in video**: Check that ffmpeg supports audio codec (aac); installed version should be fine.
