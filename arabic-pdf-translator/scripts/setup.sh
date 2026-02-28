#!/usr/bin/env bash
# Setup script for arabic-pdf-translator Claude Code plugin v2.0.0
# Auto-detects Python environment and installs dependencies

echo "=== Arabic PDF Translator v2.0.0 - Setup ==="
echo ""

# --- Step 1: Find Python ---
echo "[1/6] Locating Python environment..."

LETTORE_PYTHON=""
LETTORE_PIP=""

for candidate in \
  "/c/Users/anton/anaconda3/envs/lettore/python.exe" \
  "$HOME/anaconda3/envs/lettore/python.exe" \
  "$(command -v python3 2>/dev/null)" \
  "$(command -v python 2>/dev/null)"; do
  if [ -n "$candidate" ] && [ -f "$candidate" ] 2>/dev/null; then
    LETTORE_PYTHON="$candidate"
    break
  fi
done

if [ -z "$LETTORE_PYTHON" ]; then
    echo "ERROR: No Python found."
    echo ""
    echo "  Option 1: Create lettore conda env:"
    echo "    conda create -n lettore python=3.12"
    echo ""
    echo "  Option 2: Install Python 3.11+ system-wide"
    echo ""
    echo "  NOTE: If running in Cowork VM, the Python pipeline is not available."
    echo "  The plugin will use Native Mode (Claude vision + translation) automatically."
    exit 1
fi

echo "  Python: $LETTORE_PYTHON"

# Derive pip from same environment
PYTHON_DIR="$(dirname "$LETTORE_PYTHON")"
if [ -f "$PYTHON_DIR/../Scripts/pip.exe" ]; then
    LETTORE_PIP="$PYTHON_DIR/../Scripts/pip.exe"
elif [ -f "$PYTHON_DIR/pip" ]; then
    LETTORE_PIP="$PYTHON_DIR/pip"
elif [ -f "$PYTHON_DIR/pip3" ]; then
    LETTORE_PIP="$PYTHON_DIR/pip3"
else
    LETTORE_PIP="$LETTORE_PYTHON -m pip"
fi

echo "  Pip: $LETTORE_PIP"

# --- Step 2: Install/verify arabic-pdf-translator package ---
echo ""
echo "[2/6] Checking arabic-pdf-translator package..."

if "$LETTORE_PYTHON" -c "import arabic_pdf_translator; print(f'  Version: {arabic_pdf_translator.__version__}')" 2>/dev/null; then
    echo "  Package already installed."
else
    SOURCE_DIR="/c/Users/anton/Remote-Project"
    if [ ! -f "$SOURCE_DIR/pyproject.toml" ]; then
        SOURCE_DIR="$HOME/Remote-Project"
    fi

    if [ -f "$SOURCE_DIR/pyproject.toml" ]; then
        echo "  Installing from $SOURCE_DIR..."
        $LETTORE_PIP install -e "$SOURCE_DIR" 2>&1
    else
        echo "  ERROR: Source code not found."
        echo "  Clone it: git clone https://github.com/Antonio-Ardigo/Remote-Project.git ~/Remote-Project"
        exit 1
    fi
fi

# --- Step 3: Install optional translation backends ---
echo ""
echo "[3/6] Installing optional translation backends..."

$LETTORE_PIP install deepl 2>&1 || echo "  (deepl install failed -- optional)"
$LETTORE_PIP install openai 2>&1 || echo "  (openai install failed -- optional)"

# --- Step 4: Check/Install OCR engines ---
echo ""
echo "[4/6] Checking OCR engines..."

# EasyOCR (primary)
if "$LETTORE_PYTHON" -c "import easyocr; print('  EasyOCR: OK (' + easyocr.__version__ + ')')" 2>/dev/null; then
    echo "  EasyOCR is the primary OCR engine."
else
    echo "  Installing EasyOCR (primary OCR engine)..."
    $LETTORE_PIP install easyocr 2>&1 || echo "  WARNING: EasyOCR install failed"
fi

# Tesseract (secondary, optional)
TESSERACT_BIN=""
for tess in \
  "$(command -v tesseract 2>/dev/null)" \
  "/c/Program Files/Tesseract-OCR/tesseract.exe"; do
  if [ -n "$tess" ] && [ -f "$tess" ] 2>/dev/null; then
    TESSERACT_BIN="$tess"
    break
  fi
done

if [ -n "$TESSERACT_BIN" ]; then
    TESS_VERSION=$("$TESSERACT_BIN" --version 2>&1 | head -1)
    echo "  Tesseract found: $TESS_VERSION (secondary engine)"
    # Check for Arabic data
    if "$TESSERACT_BIN" --list-langs 2>&1 | grep -q "^ara$"; then
        echo "  Tesseract Arabic data: OK"
    else
        echo "  WARNING: Tesseract Arabic data not found."
        echo "  Download ara.traineddata from: https://github.com/tesseract-ocr/tessdata_best"
        echo "  Place it in Tesseract's tessdata directory."
    fi
    # Install pytesseract binding if not present
    if ! "$LETTORE_PYTHON" -c "import pytesseract" 2>/dev/null; then
        echo "  Installing pytesseract Python binding..."
        $LETTORE_PIP install pytesseract 2>&1 || echo "  (pytesseract install failed -- optional)"
    fi
else
    echo "  Tesseract: not installed (optional -- EasyOCR is sufficient)"
    # Check if Chocolatey is available for auto-install
    CHOCO_BIN=""
    if command -v choco &> /dev/null; then
        CHOCO_BIN="choco"
    elif [ -f "/c/ProgramData/chocolatey/bin/choco.exe" ]; then
        CHOCO_BIN="/c/ProgramData/chocolatey/bin/choco.exe"
    fi

    if [ -n "$CHOCO_BIN" ]; then
        echo "  Chocolatey detected. To install Tesseract, run in admin PowerShell:"
        echo "    choco install tesseract --yes"
    else
        echo "  To install Tesseract: https://github.com/UB-Mannheim/tesseract/wiki"
    fi
fi

# PaddleOCR (tertiary, optional)
if "$LETTORE_PYTHON" -c "import paddleocr; print('  PaddleOCR: OK')" 2>/dev/null; then
    echo "  PaddleOCR: available (tertiary engine)"
else
    echo "  PaddleOCR: not installed (optional -- install with: pip install paddleocr paddlepaddle)"
fi

# --- Step 5: Verify API keys ---
echo ""
echo "[5/6] Checking API keys..."

"$LETTORE_PYTHON" -c "
import os
keys = [
    ('Claude (Anthropic)', 'ANTHROPIC_API_KEY'),
    ('Google Translate',   'GOOGLE_TRANSLATE_API_KEY'),
    ('DeepL',              'DEEPL_API_KEY'),
    ('OpenAI',             'OPENAI_API_KEY'),
]
any_set = False
for name, key in keys:
    status = 'SET' if os.environ.get(key) else 'not set'
    if os.environ.get(key):
        any_set = True
    print(f'  {name}: {status}')

if not any_set:
    print()
    print('  NOTE: No API keys are set. Pipeline translation needs at least one.')
    print('  Native mode (Claude vision + translation) works without API keys.')
"

# --- Step 6: Verification summary ---
echo ""
echo "[6/6] Verification..."
echo ""

MODE="native only"
if "$LETTORE_PYTHON" -c "import arabic_pdf_translator" 2>/dev/null; then
    MODE="pipeline + native"
fi

echo "  Available modes: $MODE"
echo "  Run '/verify-arabic-setup' for detailed diagnostics"

echo ""
echo "=== Setup complete ==="
echo ""
echo "Usage:"
echo "  /translate-pdf document.pdf                # auto-detects best mode"
echo "  /translate-pdf document.pdf --mode native   # force native mode"
echo "  /translate-text file:arabic_text.txt        # translate text directly"
echo "  /verify-arabic-setup                        # check installation"
echo ""
echo "Set API keys (at least one required for pipeline mode):"
echo "  export ANTHROPIC_API_KEY='sk-ant-...'"
echo "  export OPENAI_API_KEY='sk-...'"
echo "  export DEEPL_API_KEY='...'              # optional"
echo "  export GOOGLE_TRANSLATE_API_KEY='...'   # optional"
