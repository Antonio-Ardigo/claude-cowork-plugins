# Arabic PDF Translator

Dual-mode Arabic document translation -- works everywhere, from full pipeline to zero dependencies.

## Key Features

- **Dual-mode architecture**: Pipeline mode (Python OCR + ensemble translation) or Native mode (Claude vision + translation)
- **Auto-detection**: Automatically selects the best available mode based on environment
- **Multi-engine OCR**: EasyOCR (primary), Tesseract, PaddleOCR with 7-stage Arabic preprocessing
- **4-method ensemble**: Claude, Google Cloud, DeepL, OpenAI GPT-4o with quality evaluation
- **Claude-as-judge**: Arbitration when translation methods produce close results
- **Zero-dependency fallback**: Native mode needs no Python, no OCR binaries, no API keys

## Quick Start

```
/translate-pdf document.pdf                     # auto-detect best mode
/translate-pdf document.pdf --mode native       # force Claude vision mode
/translate-text "Arabic text here"              # translate text directly
/verify-arabic-setup                            # check what is installed
```

## Setup (Optional -- for Pipeline Mode)

Native mode works immediately with no setup. For pipeline mode:

```bash
bash ~/.claude/plugins/marketplaces/claude-cowork-plugins/arabic-pdf-translator/scripts/setup.sh
```

Set at least one API key for pipeline translation:
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
export OPENAI_API_KEY="sk-..."      # optional
export DEEPL_API_KEY="..."          # optional
export GOOGLE_TRANSLATE_API_KEY="..." # optional
```

## Commands

| Command | Description |
|---------|-------------|
| `/translate-pdf <path>` | Translate an Arabic PDF with OCR + ensemble translation |
| `/translate-text <text>` | Translate Arabic text directly (no OCR) |
| `/verify-arabic-setup` | Verify installation and report available capabilities |

## Skills

| Skill | Triggers On |
|-------|------------|
| `arabic-ocr` | Arabic OCR, image preprocessing, Tesseract/EasyOCR/PaddleOCR |
| `arabic-translation` | Translation methods, ensemble, quality evaluation, Claude-as-judge |
| `arabic-text-processing` | Arabic normalization, RTL, diacritics, Unicode |

## Agent

| Agent | Triggers On |
|-------|------------|
| `pdf-translator` | "Translate this Arabic PDF", "OCR this Arabic document" |

## File Structure

```
arabic-pdf-translator/
+-- .claude-plugin/
|   +-- plugin.json
+-- README.md
+-- CONNECTORS.md
+-- agents/
|   +-- pdf-translator.md
+-- commands/
|   +-- translate-pdf.md
|   +-- translate-text.md
|   +-- verify-arabic-setup.md
+-- scripts/
|   +-- setup.sh
+-- skills/
    +-- arabic-ocr/
    |   +-- SKILL.md
    +-- arabic-text-processing/
    |   +-- SKILL.md
    +-- arabic-translation/
        +-- SKILL.md
```

## Requirements

### Native Mode (zero dependencies)
- Claude Code (CLI or Cowork) -- that's it

### Pipeline Mode
- Python 3.11+ in `lettore` conda environment
- `arabic_pdf_translator` package installed from `~/Remote-Project/`
- At least one translation API key
- EasyOCR (primary OCR engine, installed with package)
- Tesseract OCR v5.5+ with Arabic data (optional, secondary engine)

## Changelog

### v2.0.0 (2026-02-28)
- **New**: `/verify-arabic-setup` command for installation diagnostics
- **New**: `CONNECTORS.md` documenting external integrations
- **Improved**: `setup.sh` can install Tesseract via Chocolatey (not just check)
- **Improved**: Agent environment detection reports OCR engines and API key status
- **Improved**: Better error recovery for Tesseract-not-installed, invalid API keys
- **Improved**: Native mode emphasized as first-class (not just fallback)
- **Improved**: EasyOCR is documented as primary engine (Tesseract optional)
- **Improved**: Default OCR engines changed from tesseract,easyocr to easyocr
- **Improved**: pytesseract moved to optional dependency in pyproject.toml
- **Fixed**: Default output paths use $HOME instead of /tmp/ for Windows compatibility
- **Fixed**: EasyOCR paragraph=True bug documented (already fixed in v1.1.0 engine.py)

### v1.1.0 (2026-02-28)
- Fixed EasyOCR paragraph mode returning (bbox, text) instead of (bbox, text, conf)
- Changed to detail=1, paragraph=False in engine.py

### v1.0.0 (2026-02-28)
- Initial release with dual-mode architecture
- Pipeline mode: EasyOCR + Tesseract + PaddleOCR, 4-method ensemble translation
- Native mode: Claude vision + translation
