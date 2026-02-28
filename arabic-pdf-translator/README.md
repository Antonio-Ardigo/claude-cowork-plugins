# Arabic PDF Translator Plugin

Claude Code plugin for Arabic PDF OCR and ensemble translation.

## What It Does

Translates Arabic text from scanned or digital PDFs to English using:
- **Multi-engine OCR**: Tesseract + EasyOCR + PaddleOCR with Arabic-tuned preprocessing
- **4-method ensemble translation**: Claude, Google Cloud, DeepL, OpenAI GPT-4o
- **Quality evaluation**: Heuristic scoring + Claude-as-judge arbitration

## Setup

```bash
bash ~/.claude/plugins/marketplaces/claude-cowork-plugins/arabic-pdf-translator/scripts/setup.sh
```

Set at least one API key:
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
export GOOGLE_TRANSLATE_API_KEY="..."
export DEEPL_API_KEY="..."
export OPENAI_API_KEY="sk-..."
```

## Commands

| Command | Description |
|---------|-------------|
| `/translate-pdf <path>` | Translate an Arabic PDF with OCR + ensemble translation |
| `/translate-text <text>` | Translate Arabic text directly (no OCR) |

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

## Requirements

- Python 3.11+ in `lettore` conda environment
- Source code at `~/Remote-Project/` (cloned from GitHub)
- At least one translation API key
- Tesseract OCR with Arabic data (for OCR features)
