---
description: Translate Arabic text directly -- dual-mode: pipeline (4-method ensemble) or native (Claude translation)
argument-hint: "<arabic text or 'file:path'> [--mode auto|pipeline|native] [--force-multi]"
---

# /translate-text -- Direct Arabic Text Translation

Translate Arabic text directly (no PDF/OCR) using either the 4-method ensemble translation pipeline or Claude's native language capabilities.

## Invocation

```
/translate-text <arabic text>
/translate-text file:<path-to-text-file>
/translate-text file:extracted_arabic.txt --mode native
```

If no text is provided, prompt the user to paste Arabic text or provide a file path.

## Workflow

### Step 1: Get the Arabic Text

Parse `$ARGUMENTS`:
- If it starts with `file:`, read the file at the specified path using the Read tool
- Otherwise, treat the entire argument as Arabic text to translate
- Parse optional flags: `--mode auto|pipeline|native`, `--force-multi`

If no arguments provided, ask the user to provide Arabic text.

### Step 2: Detect Execution Mode

If `--mode native` was specified, skip to Step 4 (Native Mode).
If `--mode pipeline` was specified, go to Step 3 (Pipeline Mode). If Python not found, STOP with error.

For `--mode auto` (default), probe for the Python pipeline:

```bash
# Try each candidate in order, stop at first success:
/c/Users/anton/anaconda3/envs/lettore/python.exe -c "import arabic_pdf_translator; print('PIPELINE_OK')" 2>/dev/null
$HOME/anaconda3/envs/lettore/python.exe -c "import arabic_pdf_translator; print('PIPELINE_OK')" 2>/dev/null
python3 -c "import arabic_pdf_translator; print('PIPELINE_OK')" 2>/dev/null
python -c "import arabic_pdf_translator; print('PIPELINE_OK')" 2>/dev/null
```

If any candidate succeeds, record it as `PYTHON_BIN` and use Step 3 (Pipeline Mode).
Otherwise, use Step 4 (Native Mode).

Report the mode to the user.

---

### Step 3: Pipeline Mode

#### 3a. Write Arabic text to temporary file

Save the Arabic text to a temporary file:
```bash
# Write text to temp file (use Write tool, not Bash)
```
Use the Write tool to write the Arabic text to `/tmp/arabic_input.txt`.

#### 3b. Run Ensemble Translation

```bash
$PYTHON_BIN -c "
import json, sys
from arabic_pdf_translator.pipeline import ArabicPDFTranslator
from arabic_pdf_translator.config import TranslationConfig

config = TranslationConfig(force_multi_method=True)
translator = ArabicPDFTranslator(config)

text = open('/tmp/arabic_input.txt', 'r', encoding='utf-8').read()
best, all_results, quality = translator.translate_text(text)

output = {
    'mode': 'pipeline',
    'best_method': best.method,
    'best_translation': best.translated_text,
    'best_confidence': best.confidence,
    'all_methods': {}
}

for r in all_results:
    output['all_methods'][r.method] = {
        'translation': r.translated_text,
        'confidence': r.confidence,
        'latency_seconds': r.latency_seconds,
        'error': r.error,
    }

if quality:
    output['quality_scores'] = quality.scores
    output['best_method_by_quality'] = quality.best_method
    output['quality_reasoning'] = quality.reasoning
    output['judge_used'] = quality.judge_used

print(json.dumps(output, ensure_ascii=False, indent=2))
"
```

#### 3c. Present Pipeline Results

1. **Mode indicator**: `[Pipeline Mode - Ensemble Translation]`
2. **Best Translation** (winning method + score):
   > [translated text]

3. **Method Comparison Table**:
   | Method | Score | Confidence | Latency | Status |
   |--------|-------|------------|---------|--------|
   | Claude | 0.92  | 0.90       | 2.3s    | OK     |
   | ...    | ...   | ...        | ...     | ...    |

4. **Quality Details**: Whether Claude-as-judge was used, reasoning for selection
5. **All Translations**: Show each method's full translation for user comparison

Proceed to Step 5 (Actions).

---

### Step 4: Native Mode

When the Python pipeline is unavailable (or `--mode native` was requested).

#### 4a. Translate the Text

Translate the Arabic text to English, applying the arabic-translation skill guidelines:
- Preserve meaning, register, and tone
- Handle idioms and cultural expressions
- Maintain paragraph structure
- Note any ambiguous passages

#### 4b. Self-Assess Quality

Rate your translation on three dimensions (0.0-1.0):
- **Accuracy**: How confident you are the meaning is preserved
- **Fluency**: How natural the English reads
- **Completeness**: Whether anything was missed or added

#### 4c. Build Structured Output

```json
{
  "mode": "native",
  "best_method": "claude_native",
  "best_translation": "<English translation>",
  "best_confidence": 0.88,
  "quality_scores": {
    "accuracy": 0.90,
    "fluency": 0.92,
    "completeness": 0.95
  },
  "limitations": [
    "Single translation method (no ensemble comparison)",
    "No cross-method quality validation"
  ],
  "ambiguous_passages": ["<any noted ambiguities>"]
}
```

#### 4d. Present Native Mode Results

1. **Mode indicator**: `[Native Mode - Claude Translation]`
2. **Translation**: The full English translation
3. **Confidence scores**: Accuracy, fluency, completeness
4. **Ambiguous passages**: Any noted uncertainties
5. **Note**: "For ensemble comparison with multiple methods, install the Python pipeline and use `--mode pipeline`."

---

### Step 5: Offer Actions

Ask the user if they want to:
- Save the best translation to a file
- Save the full comparison report as JSON
- Use a specific method's translation instead of the winner (pipeline mode only)
- Translate additional text

## Notes

- Pipeline mode uses `force_multi_method=True` by default to always compare all available methods
- Long texts are automatically chunked by sentence boundaries with context overlap
- The quality evaluator scores on: accuracy (30%), fluency (25%), completeness (25%), consistency (10%), cross-agreement (10%)
- Native mode provides single-method translation with self-assessment -- good for quick translations
- Pipeline mode provides multi-method comparison -- best for important documents
