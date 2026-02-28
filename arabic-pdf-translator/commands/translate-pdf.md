---
description: Translate an Arabic PDF -- multi-engine OCR, 4-method ensemble translation, quality evaluation
argument-hint: "<pdf-path> [--pages 1,3,5-10] [--dpi 300] [--force-multi] [--methods claude,deepl]"
---

# /translate-pdf -- Arabic PDF OCR & Translation

Translate Arabic text from a scanned or digital PDF using multi-engine OCR and ensemble translation with automatic quality evaluation.

## Invocation

```
/translate-pdf <pdf-path> [options]
```

Examples:
```
/translate-pdf document.pdf
/translate-pdf ~/Documents/arabic_contract.pdf --force-multi
/translate-pdf scan.pdf --pages 1,3,5-10 --dpi 400
/translate-pdf report.pdf --methods claude,deepl -o result.json
```

If no PDF path is provided, prompt the user to supply one.

## Workflow

### Step 1: Parse Arguments

Parse `$ARGUMENTS` to extract:
- **pdf_path** (required): Path to the PDF file. `$1` is the PDF path.
- **--pages**: Page selection (1-indexed, e.g., "1,3,5-10"). Optional.
- **--dpi**: Rendering DPI for scanned PDFs (default: 300). Use 400 for poor quality scans.
- **--force-multi**: Always run all 4 translation methods and compare. Flag, no value.
- **--methods**: Comma-separated list of methods to use: claude, google, deepl, openai.
- **--ocr-engines**: Comma-separated OCR engines: tesseract, easyocr, paddleocr.
- **--quality-threshold**: Ensemble trigger level: strict, moderate, relaxed, always.
- **-o / --output**: Output file path (.txt, .json, .md).
- **--save-intermediate**: Save per-page OCR and all translation variants.
- **-v / --verbose**: Verbose logging.

### Step 2: Validate Environment

Run the following checks via Bash:

1. **Verify PDF exists**:
   ```
   ls -la "<pdf_path>"
   ```
   If the file doesn't exist, tell the user and stop.

2. **Check the Python package is installed**:
   ```
   /c/Users/anton/anaconda3/envs/lettore/python.exe -c "import arabic_pdf_translator; print(arabic_pdf_translator.__version__)"
   ```
   If not installed, tell the user to run the setup:
   ```
   bash ~/.claude/plugins/marketplaces/claude-cowork-plugins/arabic-pdf-translator/scripts/setup.sh
   ```

3. **Check available API keys**:
   ```
   /c/Users/anton/anaconda3/envs/lettore/python.exe -c "
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
   Report which keys are available. At least one is required. If none are set, tell the user to export their API keys.

### Step 3: Build and Run the Translation Command

Construct the CLI command from parsed arguments:

```
/c/Users/anton/anaconda3/envs/lettore/python.exe -m arabic_pdf_translator "<pdf_path>" [options] -o /tmp/arabic_translation_result.json --save-intermediate
```

Always use JSON output (`-o ...json`) so results can be parsed programmatically. Add `--save-intermediate` for full diagnostics.

Run the command via Bash. This may take several minutes for multi-page documents. Use a timeout of 600000ms (10 minutes) for large PDFs.

### Step 4: Present Results

After the command completes, read the JSON output file and present:

1. **Summary**: Total pages translated, total processing time, overall confidence
2. **Per-page results**:
   - Page number
   - OCR confidence score
   - Winning translation method and its quality score
   - If ensemble was used: comparison table of all methods with scores
3. **Full translation text**: The combined English translation
4. **Quality insights**: Which pages had low confidence, which methods disagreed, where Claude-as-judge was invoked

### Step 5: Offer Output Options

Ask the user if they want to:
- **Save as Markdown**: Write a formatted .md file with headers per page
- **Save as plain text**: Just the translation
- **Save as JSON**: Full structured output with all metadata
- **Copy to clipboard**: The translation text

Format the output file name as: `<original_name>_translated_<date>.<ext>`

## Error Handling

- **Missing dependencies**: Direct user to run `scripts/setup.sh`
- **No API keys**: List which keys to set and how (`export ANTHROPIC_API_KEY="..."`)
- **OCR failure**: Suggest increasing DPI (`--dpi 400`) or trying different engines
- **Translation timeout**: Suggest translating fewer pages (`--pages 1-5`)
- **Low quality scores**: Suggest `--force-multi` to compare all methods

## Notes

- The pipeline runs OCR engines in sequence and translation methods in parallel (ThreadPoolExecutor)
- For best results, set all 4 API keys and use `--force-multi`
- DPI 300 is good for clean scans; use 400+ for degraded or low-resolution documents
- The Claude-as-judge arbitration activates automatically when top methods score within 0.1 of each other
