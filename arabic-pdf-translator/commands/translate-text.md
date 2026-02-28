---
description: Translate Arabic text directly -- 4-method ensemble translation with quality comparison
argument-hint: "<arabic text or 'file:path'>"
---

# /translate-text -- Direct Arabic Text Translation

Translate Arabic text directly (no PDF/OCR) using the 4-method ensemble translation pipeline with quality evaluation.

## Invocation

```
/translate-text <arabic text>
/translate-text file:<path-to-text-file>
```

Examples:
```
/translate-text file:extracted_arabic.txt
```

If no text is provided, prompt the user to paste Arabic text or provide a file path.

## Workflow

### Step 1: Get the Arabic Text

Parse `$ARGUMENTS`:
- If it starts with `file:`, read the file at the specified path
- Otherwise, treat the entire argument as Arabic text to translate

If no arguments provided, ask the user to provide Arabic text.

### Step 2: Validate Environment

Run via Bash:

```
/c/Users/anton/anaconda3/envs/lettore/python.exe -c "import arabic_pdf_translator; print('OK')"
```

If not installed, direct user to run the setup script.

Check available API keys:
```
/c/Users/anton/anaconda3/envs/lettore/python.exe -c "
import os
available = [m for m, k in [
    ('Claude', 'ANTHROPIC_API_KEY'), ('Google', 'GOOGLE_TRANSLATE_API_KEY'),
    ('DeepL', 'DEEPL_API_KEY'), ('OpenAI', 'OPENAI_API_KEY')
] if os.environ.get(k)]
print(f'Available methods: {available}')
"
```

### Step 3: Run Translation

Write the Arabic text to a temporary file, then invoke the Python API:

```
/c/Users/anton/anaconda3/envs/lettore/python.exe -c "
import json, sys
from arabic_pdf_translator.pipeline import ArabicPDFTranslator
from arabic_pdf_translator.config import TranslationConfig

config = TranslationConfig(force_multi_method=True)
translator = ArabicPDFTranslator(config)

text = open('/tmp/arabic_input.txt', 'r', encoding='utf-8').read()
best, all_results, quality = translator.translate_text(text)

output = {
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

### Step 4: Present Results

Display results in a clear comparison format:

1. **Best Translation** (winning method + score):
   > [translated text]

2. **Method Comparison Table**:
   | Method | Score | Confidence | Latency | Status |
   |--------|-------|------------|---------|--------|
   | Claude | 0.92  | 0.90       | 2.3s    | OK     |
   | DeepL  | 0.88  | 0.85       | 1.1s    | OK     |
   | ...    | ...   | ...        | ...     | ...    |

3. **Quality Details**: Whether Claude-as-judge was used, reasoning for selection

4. **All Translations**: Show each method's full translation for user comparison

### Step 5: Offer Actions

Ask the user if they want to:
- Save the best translation to a file
- Save the full comparison report as JSON
- Use a specific method's translation instead of the winner
- Translate additional text

## Notes

- Uses `force_multi_method=True` by default to always compare all available methods
- Long texts are automatically chunked by sentence boundaries with context overlap
- The quality evaluator scores on: accuracy (30%), fluency (25%), completeness (25%), consistency (10%), cross-agreement (10%)
