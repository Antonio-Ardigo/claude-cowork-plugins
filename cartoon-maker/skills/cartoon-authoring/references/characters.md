# Character Reference

## Built-in Characters

### Engineer
- **Key**: `engineer`
- **Visual**: Hard hat (yellow), orange safety vest, work trousers, boots
- **Accessories**: Rolled-up blueprints under arm or clipboard
- **DiceBear seed**: `engineer-hardhat-01`
- **Voice**: `en-US-GuyNeural` (male, professional)
- **Personality hint**: Technical, precise, practical
- **Typical phrases**: "According to the specs...", "The load-bearing capacity...", "We need to verify..."

### Doctor
- **Key**: `doctor`
- **Visual**: White coat, stethoscope around neck, scrubs underneath
- **Accessories**: Clipboard with patient notes
- **DiceBear seed**: `doctor-whitecoat-01`
- **Voice**: `en-US-JennyNeural` (female, clear and warm)
- **Personality hint**: Empathetic, methodical, safety-focused
- **Typical phrases**: "From a medical perspective...", "Patient safety requires...", "The clinical evidence shows..."

### Architect
- **Key**: `architect`
- **Visual**: Black turtleneck, dark trousers, glasses
- **Accessories**: T-square ruler, architectural drawings
- **DiceBear seed**: `architect-black-01`
- **Voice**: `en-US-DavisNeural` (male, creative tone)
- **Personality hint**: Creative, detail-oriented, aesthetic-conscious
- **Typical phrases**: "The design intent is...", "Spatially, we should...", "The facade needs to..."

### Project Manager
- **Key**: `project_manager`
- **Visual**: Business suit (navy), professional blouse, smart shoes
- **Accessories**: Clipboard with project schedule, pen
- **DiceBear seed**: `pm-suit-01`
- **Voice**: `en-US-JaneNeural` (female, authoritative)
- **Personality hint**: Organized, deadline-focused, diplomatic
- **Typical phrases**: "According to the schedule...", "The budget requires...", "Let's align on the timeline..."

---

## Character Asset Paths

```
cartoon-workspace/characters/
├── engineer/
│   ├── standing.png      # Default neutral pose
│   ├── talking.png       # Speaking pose (slight lean forward)
│   └── gesturing.png     # Pointing/explaining pose
├── doctor/
│   ├── standing.png
│   ├── talking.png
│   └── gesturing.png
├── architect/
│   ├── standing.png
│   ├── talking.png
│   └── gesturing.png
└── project_manager/
    ├── standing.png
    ├── talking.png
    └── gesturing.png
```

Assets are downloaded from DiceBear during setup. Each PNG is 300×450px (portrait, transparent background).

---

## DiceBear API Parameters (for regenerating assets)

Base URL: `https://api.dicebear.com/9.x/open-peeps/png`

| Character | URL Parameters |
|-----------|---------------|
| engineer | `seed=engineer-hardhat&size=300&clothingColor=f97316&accessories=glasses&face=calm` |
| doctor | `seed=doctor-coat&size=300&clothingColor=ffffff&accessories=variant01&face=smile` |
| architect | `seed=architect-black&size=300&clothingColor=1f2937&accessories=glasses2&face=serious` |
| project_manager | `seed=pm-suit&size=300&clothingColor=1e3a5f&face=smile` |

---

## Adding Custom Characters

To add a new character type, place PNG files (300×450px, transparent bg) in:
`cartoon-workspace/characters/<new_name>/standing.png`
`cartoon-workspace/characters/<new_name>/talking.png`

Then use: `Character("new_name", position="left", voice="en-US-GuyNeural")`

---

## Voice Override

Default voices can be overridden per-scene:
```python
char = Character("engineer", position="left", voice="en-GB-RyanNeural")
```

See `tts-reference.md` for available voices.
