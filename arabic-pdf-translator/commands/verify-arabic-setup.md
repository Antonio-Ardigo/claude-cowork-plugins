---
description: Verify the Arabic PDF Translator installation -- check Python, OCR engines, API keys, and report which mode is available
argument-hint: "[--fix]"
---

# /verify-arabic-setup -- Installation Diagnostics

Run a comprehensive check of all Arabic PDF Translator dependencies and report status.

## Invocation

```
/verify-arabic-setup
/verify-arabic-setup --fix
```

## Workflow

### Step 1: Parse Arguments

- `--fix`: If specified, attempt to fix problems (install missing packages). Without this flag, only report.

### Step 2: Check Python Environment

Run via Bash:
```bash
PYTHON_BIN=""
for candidate in \
  "/c/Users/anton/anaconda3/envs/lettore/python.exe" \
  "$HOME/anaconda3/envs/lettore/python.exe" \
  "$(command -v python3 2>/dev/null)" \
  "$(command -v python 2>/dev/null)"; do
  if [ -n "$candidate" ] && [ -f "$candidate" ] 2>/dev/null; then
    PYTHON_BIN="$candidate"
    VERSION=$("$candidate" --version 2>&1)
    echo "PYTHON_FOUND:$candidate:$VERSION"
    break
  fi
done
if [ -z "$PYTHON_BIN" ]; then
  echo "PYTHON_FOUND:none:N/A"
fi
```

### Step 3: Check Package and Modules

If Python was found, run via Bash:
```bash
"$PYTHON_BIN" -c "
import importlib, json
checks = {}

# Core package
try:
    import arabic_pdf_translator
    checks['arabic_pdf_translator'] = arabic_pdf_translator.__version__
except ImportError:
    checks['arabic_pdf_translator'] = None

# OCR engines
for mod in ['easyocr', 'pytesseract', 'paddleocr']:
    try:
        m = importlib.import_module(mod)
        checks[mod] = getattr(m, '__version__', 'installed')
    except ImportError:
        checks[mod] = None

# Translation backends
for mod in ['anthropic', 'openai', 'deepl']:
    try:
        m = importlib.import_module(mod)
        checks[mod] = getattr(m, '__version__', 'installed')
    except ImportError:
        checks[mod] = None

# Image processing
for mod_name, import_name in [('OpenCV', 'cv2'), ('numpy', 'numpy'), ('Pillow', 'PIL'), ('PyMuPDF', 'fitz')]:
    try:
        m = importlib.import_module(import_name)
        checks[mod_name] = getattr(m, '__version__', 'installed')
    except ImportError:
        checks[mod_name] = None

print(json.dumps(checks))
"
```

### Step 4: Check Tesseract Binary

Run via Bash:
```bash
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
  TESS_VER=$("$TESSERACT_BIN" --version 2>&1 | head -1)
  echo "TESSERACT:$TESS_VER"
  if "$TESSERACT_BIN" --list-langs 2>&1 | grep -q "^ara$"; then
    echo "TESSERACT_ARABIC:yes"
  else
    echo "TESSERACT_ARABIC:no"
  fi
else
  echo "TESSERACT:not_installed"
fi
```

### Step 5: Check API Keys

Run via Bash:
```bash
for key in ANTHROPIC_API_KEY GOOGLE_TRANSLATE_API_KEY DEEPL_API_KEY OPENAI_API_KEY; do
  val=$(printenv "$key" 2>/dev/null || true)
  if [ -n "$val" ]; then
    echo "APIKEY:$key:set"
  else
    echo "APIKEY:$key:missing"
  fi
done
```

### Step 6: Build Status Report

Combine all results into an ASCII table. Use this exact format:

```
=== Arabic PDF Translator v2.0.0 -- Installation Diagnostics ===

Mode:        [Pipeline Mode available / Native Mode only]
Python:      [path] ([version])

+---------------------------+-----------+----------+
| Component                 | Status    | Version  |
+---------------------------+-----------+----------+
| arabic_pdf_translator     | OK / MISS | x.y.z    |
| EasyOCR                   | OK / MISS | x.y.z    |
| Tesseract OCR             | OK / MISS | x.y.z    |
| Tesseract Arabic data     | OK / MISS | --       |
| PaddleOCR                 | OK / MISS | --       |
| OpenCV                    | OK / MISS | x.y.z    |
| PyMuPDF (fitz)            | OK / MISS | x.y.z    |
| numpy                     | OK / MISS | x.y.z    |
| Pillow                    | OK / MISS | x.y.z    |
+---------------------------+-----------+----------+

+---------------------------+-----------+
| Translation API Key       | Status    |
+---------------------------+-----------+
| ANTHROPIC_API_KEY         | set / --  |
| GOOGLE_TRANSLATE_API_KEY  | set / --  |
| DEEPL_API_KEY             | set / --  |
| OPENAI_API_KEY            | set / --  |
+---------------------------+-----------+

Recommendations:
  - [list any actions needed]
```

After the table, add recommendations based on what is missing:
- If no Python: "Install lettore conda env: conda create -n lettore python=3.12"
- If package missing: "Install package: pip install -e ~/Remote-Project"
- If Tesseract missing: "Optional: choco install tesseract (admin PowerShell)"
- If Arabic data missing: "Download ara.traineddata to Tesseract tessdata directory"
- If no API keys: "Pipeline translation needs at least one API key. Native mode works without keys."
- If everything OK: "All systems operational. Pipeline mode and native mode both available."

### Step 7: Fix Mode (if --fix)

If the user passed `--fix`, attempt automatic fixes in this order:

1. **Package not installed**: `$PYTHON_BIN -m pip install -e /c/Users/anton/Remote-Project`
2. **EasyOCR missing**: `$PYTHON_BIN -m pip install easyocr`
3. **pytesseract missing**: `$PYTHON_BIN -m pip install pytesseract`
4. **Tesseract binary missing**: `powershell.exe -Command "Start-Process choco -ArgumentList 'install','tesseract','--yes' -Verb RunAs -Wait"` (requires admin)
5. **Arabic traineddata missing**: Download from GitHub to tessdata directory
6. **Translation backends missing**: `$PYTHON_BIN -m pip install openai deepl`

After fixes, re-run the diagnostic to confirm results.

Report what was fixed and what requires manual intervention (admin rights for Tesseract, API keys must be set by user).
