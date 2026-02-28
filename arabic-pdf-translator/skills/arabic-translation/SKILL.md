---
name: arabic-translation
description: Arabic-to-English ensemble translation, quality evaluation, and method comparison. Use when the user asks about Arabic translation methods, translation quality evaluation, Claude-as-judge, ensemble translation, comparing translation APIs, Arabic translation accuracy, translation confidence scoring, heuristic quality evaluation, cross-method agreement, or choosing between Claude, Google, DeepL, and OpenAI for translation.
version: 1.0.0
---

# Arabic Translation Ensemble Skill

You are an expert in machine translation for Arabic, with deep knowledge of the 4-method ensemble approach, quality evaluation methodology, and the specific challenges of Arabic-to-English translation.

## The 4 Translation Methods

### 1. Claude (Anthropic)
- **Model**: claude-sonnet-4-20250514
- **Approach**: LLM-based contextual translation with detailed system prompt
- **Strengths**: Cultural awareness, idiomatic output, handles ambiguous constructions, preserves register (formal/informal)
- **Weaknesses**: Higher latency, more expensive per token
- **Base confidence**: 0.90 (0.92 if clean stop)
- **Best for**: Literary text, formal documents, culturally nuanced content
- **Retry**: 3 attempts with exponential backoff (base 2s)

### 2. Google Cloud Translation
- **Approach**: Neural machine translation (NMT)
- **Backend**: google.cloud.translate_v2 (official) or direct HTTP API
- **Strengths**: High throughput, consistent quality, good for technical text
- **Weaknesses**: Less culturally nuanced, can be literal
- **Base confidence**: 0.82 (0.85 if detected language matches source)
- **Best for**: Technical documents, high-volume translation
- **Retry**: 3 attempts with exponential backoff (base 1s)

### 3. DeepL
- **Approach**: Neural MT focused on fluency
- **Backend**: Official deepl.Translator or HTTP API (auto-detects free vs pro key by ":fx" suffix)
- **Language mapping**: ar -> AR, en -> EN-US
- **Strengths**: Excellent fluency, natural-sounding output, preserve_formatting option
- **Weaknesses**: Smaller Arabic training data than Google
- **Base confidence**: 0.85-0.88 depending on backend
- **Best for**: Business correspondence, fluency-critical output

### 4. OpenAI GPT-4o
- **Approach**: LLM-based with temperature=0.3 for consistency
- **Strengths**: Good contextual understanding, handles colloquial Arabic well
- **Weaknesses**: Occasional hallucination, may add explanatory notes
- **Base confidence**: 0.87 (0.89 if clean finish)
- **Best for**: Colloquial text, social media, mixed dialect content

## Ensemble Workflow

```
1. Run primary method (first available)
        |
        v
2. Check confidence against threshold
        |
   >= threshold ---------> Return single result
        |
   < threshold (or force_multi_method=True)
        |
        v
3. Run ALL methods in parallel (ThreadPoolExecutor)
        |
        v
4. Heuristic scoring (5 dimensions)
        |
        v
5. Cross-method agreement analysis
        |
        v
6. Top 2 within 0.1? --> Claude-as-judge arbitration
        |
        v
7. Final blend: 60% judge + 40% heuristic --> Winner
```

### Quality Thresholds

| Level | Threshold | Behavior |
|-------|-----------|----------|
| STRICT | 0.85 | Ensemble if primary confidence < 85% |
| MODERATE | 0.70 | Ensemble if primary confidence < 70% (default) |
| RELAXED | 0.55 | Ensemble only for low-confidence results |
| ALWAYS | 1.00 | Always run ensemble regardless of confidence |

## Quality Evaluation

### 5 Scoring Dimensions

| Dimension | Weight | What It Measures |
|-----------|--------|-----------------|
| **Accuracy** | 30% | Untranslated Arabic detection, self-reported confidence |
| **Fluency** | 25% | Sentence structure, length variety, capitalization |
| **Completeness** | 25% | Length ratio (0.5-2.0x source), sentence count preservation |
| **Consistency** | 10% | Trigram uniqueness (no repetitive phrases) |
| **Cross-agreement** | 10% | Jaccard similarity to other methods' output |

### Heuristic Scoring Details

**Completeness scoring**:
- Length ratio = len(translation) / len(source)
- Ideal range: 0.5 to 2.0 (Arabic-to-English typically expands)
- Score drops steeply outside this range
- Also checks sentence count preservation

**Accuracy scoring**:
- Regex `[\u0600-\u06FF]` detects untranslated Arabic in output
- Penalizes proportionally to amount of remaining Arabic
- Blends with the translator's self-reported confidence

**Fluency assessment**:
- Base: 0.75
- +0.10 if average sentence length is 8-25 words (natural English)
- +0.05 for sentence length variance (not all same length)
- +0.10 * capitalization_ratio (proper English capitalization)

**Consistency assessment**:
- Extracts word trigrams from translation
- unique_trigrams / total_trigrams ratio
- Higher ratio = less repetition = better
- Adds 0.1 bonus

**Cross-agreement**:
- For each translation, compute Jaccard similarity with every other method
- Average similarity = agreement score
- Methods that agree with the majority score higher

### Claude-as-Judge Arbitration

Activated when the top 2 methods' heuristic scores are within 0.1 of each other.

**Judge evaluates on 5 dimensions (1-10 scale)**:
1. Accuracy -- faithfulness to source meaning
2. Fluency -- natural English prose
3. Completeness -- nothing omitted, nothing added
4. Terminology -- correct domain-specific terms
5. Register -- matches the formality level of the source

**Final score blending**:
- 60% judge evaluation + 40% heuristic scoring
- This prevents the judge from overriding strong heuristic signals while giving it decisive power when heuristics are inconclusive

## Text Chunking for Long Documents

When source text exceeds 3000 characters:

1. Split by Arabic sentence boundaries: `.` `!` `?` `،` `؟` `\n`
2. Accumulate sentences up to `max_chunk_chars` (3000)
3. Overlap: last `chunk_overlap_chars` (200) characters carry to next chunk
4. Each chunk gets context from previous chunk's translation for coherence
5. Chunks translated independently, then concatenated

## Method Selection Guidance

| Scenario | Recommended Setup |
|----------|------------------|
| Single document, need accuracy | `--force-multi` with all 4 keys |
| Batch processing, need speed | `--methods google --no-ensemble` |
| Legal/formal documents | `--methods claude,deepl --quality-threshold strict` |
| Low budget, one API key | Use whichever key you have; Claude preferred |
| Research/comparison | `--force-multi --save-intermediate` for full analysis |
