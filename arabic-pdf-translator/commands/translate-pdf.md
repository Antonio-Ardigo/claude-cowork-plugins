---
description: Translate an Arabic PDF -- dual-mode: pipeline (multi-engine OCR + ensemble) or native (Claude vision + translation)
argument-hint: "<pdf-path> [--pages 1,3,5-10] [--mode auto|pipeline|native] [--dpi 300] [--force-multi]"
---

# /translate-pdf -- Arabic PDF OCR & Translation

Translate Arabic text from a scanned or digital PDF using either the full Python pipeline (multi-engine OCR + ensemble translation) or Claude's native vision and language capabilities.

## Invocation

```
/translate-pdf <pdf-path> [options]
```

Examples:
```
/translate-pdf document.pdf
/translate-pdf ~/Documents/arabic_contract.pdf --force-multi
/translate-pdf scan.pdf --pages 1,3,5-10 --dpi 400
/translate-pdf report.pdf --mode native
/translate-pdf report.pdf --methods claude,deepl -o result.json
```

If no PDF path is provided, prompt the user to supply one.

## Workflow

### Step 1: Parse Arguments

Parse `$ARGUMENTS` to extract:
- **pdf_path** (required): Path to the PDF file. `$1` is the PDF path.
- **--mode**: Execution mode: `auto` (default), `pipeline`, or `native`.
- **--pages**: Page selection (1-indexed, e.g., "1,3,5-10"). Optional.
- **--dpi**: Rendering DPI for scanned PDFs (default: 300). Use 400 for poor quality scans.
- **--force-multi**: Always run all translation methods and compare. Flag, no value.
- **--methods**: Comma-separated list of methods to use: claude, google, deepl, openai.
- **--ocr-engines**: Comma-separated OCR engines: easyocr, tesseract, paddleocr, claude_vision, qari.
- **--quality-threshold**: Ensemble trigger level: strict, moderate, relaxed, always.
- **-o / --output**: Output file path (.txt, .json, .md).
- **--save-intermediate**: Save per-page OCR and all translation variants.
- **-v / --verbose**: Verbose logging.

### Step 2: Verify PDF Exists

Check the PDF file exists:
```
ls -la "<pdf_path>"
```
If the file doesn't exist, tell the user and stop.

### Step 3: Detect Execution Mode

If `--mode native` was specified, skip to Step 5 (Native Mode).
If `--mode pipeline` was specified, skip the auto-detection and go directly to Step 4 (Pipeline Mode). If the Python environment is not found, STOP with a clear error.

For `--mode auto` (the default), probe for the Python pipeline:

Run the following via Bash. Try each candidate in order and stop at the first success:

```bash
# Candidate 1: Windows conda (host machine)
/c/Users/anton/anaconda3/envs/lettore/python.exe -c "import arabic_pdf_translator; print('PIPELINE_OK')" 2>/dev/null

# Candidate 2: Home directory conda
$HOME/anaconda3/envs/lettore/python.exe -c "import arabic_pdf_translator; print('PIPELINE_OK')" 2>/dev/null

# Candidate 3: System python3
python3 -c "import arabic_pdf_translator; print('PIPELINE_OK')" 2>/dev/null

# Candidate 4: System python
python -c "import arabic_pdf_translator; print('PIPELINE_OK')" 2>/dev/null
```

If any candidate prints `PIPELINE_OK`, record that binary as `PYTHON_BIN` and proceed to Step 4 (Pipeline Mode).

If none succeed, proceed to Step 5 (Native Mode).

Report the mode to the user:
- Pipeline: "Pipeline detected at `<PYTHON_BIN>`. Using multi-engine OCR + ensemble translation."
- Native: "Python pipeline not available. Using Claude vision + translation (native mode)."

---

### Step 4: Pipeline Mode

Use the discovered `PYTHON_BIN` variable for all commands (never hardcode).

#### 4a. Check Available API Keys

```bash
$PYTHON_BIN -c "
import os
keys = {
    'ANTHROPIC_API_KEY': bool(os.environ.get('ANTHROPIC_API_KEY')),
    'GOOGLE_TRANSLATE_API_KEY': bool(os.environ.get('GOOGLE_TRANSLATE_API_KEY')),
    'DEEPL_API_KEY': bool(os.environ.get('DEEPL_API_KEY')),
    'OPENAI_API_KEY': bool(os.environ.get('OPENAI_API_KEY')),
}
available = [k for k, v in keys.items() if v]
missing = [k for k, v in keys.items() if not v]
print(f'Available: {available}')
print(f'Missing: {missing}')
"
```

Report which keys are available. At least one is required. If none are set, tell the user to export their API keys and stop.

#### 4b. Run the Translation Pipeline

Construct the CLI command from parsed arguments:

```bash
$PYTHON_BIN -m arabic_pdf_translator "<pdf_path>" [options] -o $HOME/arabic_translation_result.json --save-intermediate
```

Always use JSON output so results can be parsed programmatically. Add `--save-intermediate` for full diagnostics.

Run via Bash with a timeout of 600000ms (10 minutes) for large PDFs.

#### 4c. Present Pipeline Results

Read the JSON output file and present:

1. **Mode indicator**: `[Pipeline Mode - Multi-engine OCR + Ensemble Translation]`
2. **Summary**: Total pages translated, total processing time, overall confidence
3. **Per-page results**:
   - Page number
   - OCR confidence score
   - Winning translation method and its quality score
   - If ensemble was used: comparison table of all methods with scores
4. **Full translation text**: The combined English translation
5. **Quality insights**: Which pages had low confidence, which methods disagreed, where Claude-as-judge was invoked

Proceed to Step 6 (Output Options).

---

### Step 5: Native Mode

When the Python pipeline is unavailable (or `--mode native` was requested), use Claude's built-in capabilities. This mode produces structured output matching the same schema as pipeline mode.

#### 5a. Read PDF Pages

Use the Read tool to read the PDF file. Claude Code's Read tool can read PDFs natively and present each page visually. If `--pages` was specified, read only those pages (use the `pages` parameter, e.g., `pages: "1-5"`). Read at most 20 pages per Read call.

For documents with more than 20 pages, batch the reads.

#### 5b. Extract Arabic Text (Per Page)

For each page image, carefully examine the visual content and extract all Arabic text:

- Read the Arabic script from right to left
- Preserve line breaks and paragraph structure
- Note any diacritical marks (tashkeel) visible
- Capture numbers, dates, and proper nouns
- Note any non-Arabic text (headers, page numbers, Latin text)
- If any portion is illegible, note it as `[illegible]`

#### 5c. Translate to English (Per Page)

Apply the arabic-translation skill guidelines:
- Preserve meaning, register, and tone
- Handle idioms and cultural expressions appropriately
- Maintain paragraph structure
- Translate proper nouns phonetically where appropriate
- Note any passages where you are uncertain about the reading or meaning

#### 5d. Self-Assess Quality (Per Page)

Rate confidence on a 0.0-1.0 scale for each page:
- **0.90-1.00**: Clean printed text, clearly legible, confident in reading and translation
- **0.75-0.89**: Minor uncertainties (faded ink, small text, ambiguous word)
- **0.60-0.74**: Multiple uncertain passages, possible misreadings
- **Below 0.60**: Significant portions unreadable -- recommend pipeline mode with higher DPI

#### 5e. Build Structured Output

Construct a JSON result object and save it:

```json
{
  "mode": "native",
  "source_file": "<pdf_path>",
  "total_pages": N,
  "pages": [
    {
      "page_number": 1,
      "ocr_text": "<Arabic text extracted via vision>",
      "ocr_confidence": 0.85,
      "ocr_method": "claude_vision",
      "best_translation": "<English translation>",
      "translation_method": "claude_native",
      "quality_scores": {
        "reading_confidence": 0.85,
        "translation_confidence": 0.90,
        "completeness": 0.95
      },
      "processing_notes": "Clean printed text, no significant issues."
    }
  ],
  "full_translation": "<all pages combined>",
  "total_processing_time": 0,
  "summary": {
    "mode": "native",
    "total_pages_processed": N,
    "pages_with_arabic_text": M,
    "average_confidence": 0.87,
    "limitations": [
      "Single translation method (no ensemble comparison)",
      "OCR via vision model (may miss fine diacritical marks)",
      "No cross-method quality validation"
    ]
  }
}
```

Write this JSON to `$HOME/arabic_translation_result.json` (or the user-specified `-o` path).

#### 5f. Present Native Mode Results

1. **Mode indicator**: `[Native Mode - Claude Vision + Translation]`
2. **Summary**: Total pages, average confidence, any problem pages
3. **Per-page results**: Page number, confidence score, any notes about difficult passages
4. **Full translation text**: The combined English translation
5. **Limitations note**: Remind user that pipeline mode offers multi-engine OCR and ensemble translation for higher accuracy

---

### Step 6: Offer Output Options

Ask the user if they want to:
- **Save as Markdown**: Write a formatted .md file with headers per page
- **Save as plain text**: Just the translation
- **Save as JSON**: Full structured output with all metadata
- **Copy to clipboard**: The translation text

Format the output file name as: `<original_name>_translated_<date>.<ext>`

## Error Handling

- **--mode pipeline but no Python**: Stop with clear error. Suggest running `/verify-arabic-setup --fix`.
- **No API keys (pipeline mode)**: List which keys to set and how (`export ANTHROPIC_API_KEY="..."`). If no keys at all, suggest `--mode native` which needs no API keys.
- **`RuntimeError: No OCR engines available`**: Install EasyOCR: `pip install easyocr`. Or use `--ocr-engines easyocr`.
- **`RuntimeError: No translation methods available`**: Set at least one API key or use `--mode native`.
- **`ImportError: pytesseract`**: Tesseract is optional. Re-run with `--ocr-engines easyocr`.
- **`openai.AuthenticationError` (401)**: Invalid OpenAI API key. Remove it (`unset OPENAI_API_KEY`) or use `--methods claude,deepl,google`.
- **OCR failure (pipeline mode)**: Suggest increasing DPI (`--dpi 400`) or trying different engines
- **Translation timeout**: Suggest translating fewer pages (`--pages 1-5`)
- **Low quality scores**: Suggest `--force-multi` to compare all methods
- **Large PDF in native mode**: Process in batches of 20 pages maximum per Read call

## Quick Reference

```
/translate-pdf document.pdf                           # auto-detect mode
/translate-pdf document.pdf --mode native             # force native (no Python needed)
/translate-pdf scan.pdf --dpi 400                     # better quality for poor scans
/translate-pdf doc.pdf --force-multi -o out.json      # compare all methods
/translate-pdf doc.pdf --pages 1-5                    # translate first 5 pages
/translate-pdf doc.pdf --methods claude,deepl          # use specific methods
/translate-pdf doc.pdf --ocr-engines easyocr           # EasyOCR only (skip Tesseract)
/translate-pdf doc.pdf --ocr-engines claude_vision     # handwritten docs (needs ANTHROPIC_API_KEY)
/translate-pdf doc.pdf --ocr-engines qari              # handwritten docs (local, no API key)
/translate-pdf doc.pdf --ocr-engines qari,easyocr      # handwriting + printed consensus
```

## Notes

- **Auto mode** is the default and recommended. It uses the pipeline when available, native mode otherwise.
- In pipeline mode, OCR engines run in sequence and translation methods run in parallel (ThreadPoolExecutor)
- In native mode, Claude's vision capabilities work on both printed and handwritten Arabic text
- For best pipeline results, set all 4 API keys and use `--force-multi`
- DPI 300 is good for clean scans; use 400+ for degraded or low-resolution documents
- Claude-as-judge arbitration activates automatically when top methods score within 0.1 of each other
- Default OCR engine is EasyOCR (primary). Tesseract is optional and adds multi-engine consensus.
- For **handwritten Arabic**, use `--ocr-engines claude_vision` (API) or `--ocr-engines qari` (local). Traditional engines (EasyOCR, Tesseract) fail on cursive handwriting.
- Qari-OCR first run downloads ~4GB model. Inference takes 30-120s per page on CPU.
