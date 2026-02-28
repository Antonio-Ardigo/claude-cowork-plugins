#!/usr/bin/env bash
# Setup script for arabic-pdf-translator Claude Code plugin
# Installs the Python package into the lettore conda environment

set -e

echo "=== Arabic PDF Translator - Setup ==="
echo ""

# Locate the lettore Python environment
LETTORE_PYTHON="/c/Users/anton/anaconda3/envs/lettore/python.exe"
LETTORE_PIP="/c/Users/anton/anaconda3/envs/lettore/Scripts/pip.exe"

if [ ! -f "$LETTORE_PYTHON" ]; then
    echo "ERROR: lettore conda environment not found."
    echo "  Expected Python at: $LETTORE_PYTHON"
    echo "  Create it: conda create -n lettore python=3.12"
    exit 1
fi

echo "  Using Python: $LETTORE_PYTHON"

# Check source code exists
SOURCE_DIR="/c/Users/anton/Remote-Project"
if [ ! -f "$SOURCE_DIR/pyproject.toml" ]; then
    echo "ERROR: Source code not found at $SOURCE_DIR"
    echo "  Clone it: git clone https://github.com/Antonio-Ardigo/Remote-Project.git ~/Remote-Project"
    exit 1
fi

echo "[1/4] Installing arabic-pdf-translator package..."
"$LETTORE_PIP" install -e "$SOURCE_DIR" 2>&1

echo ""
echo "[2/4] Installing optional translation backends..."
"$LETTORE_PIP" install openai deepl 2>&1 || echo "  (Some optional backends failed -- this is OK)"

echo ""
echo "[3/4] Checking Tesseract OCR..."
if command -v tesseract &> /dev/null; then
    TESS_VERSION=$(tesseract --version 2>&1 | head -1)
    echo "  Tesseract found: $TESS_VERSION"
    # Check for Arabic data
    if tesseract --list-langs 2>&1 | grep -q "ara"; then
        echo "  Arabic language data: OK"
    else
        echo "  WARNING: Arabic language data not found."
        echo "  Install: download ara.traineddata from https://github.com/tesseract-ocr/tessdata"
        echo "  Place in: $(tesseract --print-parameters 2>&1 | grep tessdata | head -1 || echo 'tessdata directory')"
    fi
else
    echo "  WARNING: Tesseract not found."
    echo "  Install via: choco install tesseract"
    echo "  Or download from: https://github.com/UB-Mannheim/tesseract/wiki"
fi

echo ""
echo "[4/4] Verifying installation..."
"$LETTORE_PYTHON" -c "
import arabic_pdf_translator
print(f'  Package version: {arabic_pdf_translator.__version__}')

import os
print('  API keys:')
for name, key in [('ANTHROPIC_API_KEY','Claude'), ('GOOGLE_TRANSLATE_API_KEY','Google'), ('DEEPL_API_KEY','DeepL'), ('OPENAI_API_KEY','OpenAI')]:
    status = 'SET' if os.environ.get(name) else 'not set'
    print(f'    {key}: {status}')
"

echo ""
echo "=== Setup complete ==="
echo ""
echo "Usage:"
echo "  /translate-pdf document.pdf"
echo "  /translate-text file:arabic_text.txt"
echo ""
echo "Set API keys (at least one required):"
echo "  export ANTHROPIC_API_KEY='sk-ant-...'"
echo "  export GOOGLE_TRANSLATE_API_KEY='...'"
echo "  export DEEPL_API_KEY='...'"
echo "  export OPENAI_API_KEY='sk-...'"
