# Connectors -- Arabic PDF Translator

This plugin has a dual-mode architecture. **Native mode** works without any external connections. **Pipeline mode** requires external tools.

## Native Mode (zero dependencies)

Native mode uses Claude's built-in vision and language capabilities. It requires:
- Claude Code's Read tool (reads PDF pages as images)
- Claude Code's Write tool (saves output files)
- No Python, no OCR binaries, no API keys

## Pipeline Mode Connectors

| System | Purpose | Required? | Install |
|--------|---------|-----------|---------|
| Python 3.11+ (lettore conda env) | Runtime for OCR and translation pipeline | Yes (pipeline mode) | `conda create -n lettore python=3.12` |
| arabic_pdf_translator package | Core OCR + translation code | Yes (pipeline mode) | `pip install -e ~/Remote-Project` |
| EasyOCR | Primary Arabic OCR engine (deep learning) | Yes (pipeline mode) | Installed with package |
| Tesseract OCR + Arabic data | Secondary OCR engine (LSTM) | Optional | `choco install tesseract` + ara.traineddata |
| PaddleOCR + PaddlePaddle | Tertiary OCR engine | Optional | `pip install paddleocr paddlepaddle` |

## Translation API Keys

At least one is required for pipeline mode translation. Native mode uses Claude directly (no API key needed).

| Provider | Environment Variable | Purpose |
|----------|---------------------|---------|
| Anthropic Claude | `ANTHROPIC_API_KEY` | Best for literary, formal, and culturally nuanced text |
| Google Cloud Translation | `GOOGLE_TRANSLATE_API_KEY` | High-volume NMT, good for technical text |
| DeepL | `DEEPL_API_KEY` | Fluency-focused, good for business correspondence |
| OpenAI GPT-4o | `OPENAI_API_KEY` | Good for colloquial Arabic and mixed dialect |

## Environment-Specific Notes

- **Windows host**: Use `/c/Users/anton/anaconda3/envs/lettore/python.exe` directly (`conda` not available in bash)
- **Tesseract path**: `C:\Program Files\Tesseract-OCR\tesseract.exe` (installed via Chocolatey)
- **Cowork VM**: Python pipeline unavailable; plugin automatically uses native mode
- **No NVIDIA GPU**: EasyOCR runs on CPU (`easyocr_gpu: False` in config)

## Currently Active

- **File system**: Saves translation output as .json, .md, or .txt
- **Python pipeline**: Available when lettore conda env has arabic_pdf_translator installed
- **Claude vision**: Always available as native-mode fallback
