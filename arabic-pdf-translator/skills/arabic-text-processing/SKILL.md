---
name: arabic-text-processing
description: Arabic text normalization, RTL handling, Unicode ranges, diacritics, and script-specific processing. Use when the user asks about Arabic text normalization, RTL text handling, Arabic diacritics, tashkeel removal, alef normalization, Arabic Unicode ranges, Arabic punctuation, text direction markers, bidirectional text, Arabic ligatures, Arabic character encoding, or Arabic NLP preprocessing.
version: 1.0.0
---

# Arabic Text Processing Skill

You are an expert in Arabic text processing, normalization, and Unicode handling. You understand the complexities of Arabic script in digital systems and the specific processing needed for NLP and OCR applications.

## Arabic Unicode Ranges

Arabic text is encoded across several Unicode blocks:

| Block | Range | Description |
|-------|-------|-------------|
| Arabic | U+0600 - U+06FF | Core Arabic script (letters, diacritics, digits) |
| Arabic Supplement | U+0750 - U+077F | Additional characters for African languages |
| Arabic Extended-A | U+08A0 - U+08FF | Quranic annotations, African Arabic |
| Arabic Presentation Forms-A | U+FB50 - U+FDFF | Ligatures and contextual forms |
| Arabic Presentation Forms-B | U+FE70 - U+FEFF | Positional variant forms |

### Arabic Detection

To check if text is primarily Arabic, count characters in these ranges and check if they exceed 30% of total characters. The regex pattern:
```
[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]
```

## Diacritical Marks (Tashkeel)

Arabic diacritics (harakat) modify pronunciation but are often optional in modern text:

| Mark | Unicode | Name | Description |
|------|---------|------|-------------|
| fathah | U+064E | Fat-hah | Short "a" vowel above |
| dammah | U+064F | Dammah | Short "u" vowel above |
| kasrah | U+0650 | Kasrah | Short "i" vowel below |
| sukun | U+0652 | Sukun | No vowel (consonant stop) |
| shadda | U+0651 | Shaddah | Gemination (doubled consonant) |
| tanwin fath | U+064B | Tanwin Fathatan | "-an" ending |
| tanwin damm | U+064C | Tanwin Dammatan | "-un" ending |
| tanwin kasr | U+064D | Tanwin Kasratan | "-in" ending |

### Tashkeel Removal
For normalization (search, comparison), remove diacritics in range U+064B to U+065F:
```python
import re
text = re.sub(r'[\u064B-\u065F]', '', text)
```

**When to preserve tashkeel**: Quranic text, children's books, language learning materials, disambiguation of homographs.

## Character Normalization

### Alef Variants
Arabic has multiple alef forms that should often be normalized:

| Character | Unicode | Name | Normalizes to |
|-----------|---------|------|---------------|
| alef with madda | U+0622 | Alef Madda | U+0627 (alef) |
| alef with hamza above | U+0623 | Alef Hamza Above | U+0627 (alef) |
| alef with hamza below | U+0625 | Alef Hamza Below | U+0627 (alef) |

### Yaa Variants
| Character | Unicode | Name | Normalizes to |
|-----------|---------|------|---------------|
| alef maqsura | U+0649 | Alef Maqsura | U+064A (ya) |
| Persian yeh | U+06CC | Yeh | U+064A (ya) |

### Taa Marbuta
| Character | Unicode | Name | Normalizes to |
|-----------|---------|------|---------------|
| taa marbuta | U+0629 | Taa Marbuta | U+0647 (ha) |

**Normalization order**: Always remove diacritics first, then normalize character forms. This prevents diacritic-dependent normalization errors.

## Right-to-Left (RTL) Handling

### Unicode Directional Markers

| Marker | Unicode | Purpose |
|--------|---------|---------|
| RLM | U+200F | Right-to-Left Mark (invisible, forces RTL context) |
| LRM | U+200E | Left-to-Right Mark (invisible, forces LTR context) |
| RLE | U+202B | Right-to-Left Embedding (deprecated, use isolates) |
| RLO | U+202E | Right-to-Left Override |
| RLI | U+2067 | Right-to-Left Isolate (recommended) |
| PDF | U+202C | Pop Directional Formatting |
| PDI | U+2069 | Pop Directional Isolate |

### Bidirectional Text Rules
- Arabic text naturally flows RTL based on Unicode Bidirectional Algorithm (UBA)
- Numbers within Arabic text remain LTR (handled automatically)
- Mixed Arabic/Latin text requires explicit directional markers at boundaries
- For OCR output, prepend U+200F to Arabic-dominant lines to ensure correct display

### Common RTL Issues in OCR
1. **Reversed line order**: Some OCR engines return Arabic lines in LTR visual order
2. **Mixed directionality**: Numbers and Latin words embedded in Arabic can get reordered
3. **Paragraph detection**: OCR may split RTL paragraphs at line breaks instead of logical boundaries

## Arabic Punctuation

Arabic uses distinct punctuation marks:

| Latin | Arabic | Unicode | Name |
|-------|--------|---------|------|
| , | ، | U+060C | Arabic comma |
| ; | ؛ | U+061B | Arabic semicolon |
| ? | ؟ | U+061F | Arabic question mark |
| . | . | U+002E | Same as Latin (period) |
| ! | ! | U+0021 | Same as Latin (exclamation) |

In Arabic text, commas and question marks should be Arabic variants. The postprocessor converts Latin punctuation to Arabic equivalents when surrounded by Arabic characters.

## Valid Single-Character Arabic Words

These single Arabic characters are valid standalone words and should NOT be removed during OCR cleanup:

| Character | Name | Meaning |
|-----------|------|---------|
| و | waw | "and" (conjunction) |
| أ | alef with hamza | question particle |
| إ | alef with hamza below | "to" (in some constructs) |
| ا | alef | (rare standalone use) |
| ب | ba | "by/with" (preposition) |
| ف | fa | "so/then" (conjunction) |
| ل | lam | "for" (preposition) |
| ك | kaf | "like/as" (preposition) |

## Text Similarity for Arabic

When comparing Arabic text (e.g., for cross-method agreement in translation evaluation):
- Use Jaccard coefficient on word sets: `|A intersection B| / |A union B|`
- Normalize both texts first (remove diacritics, normalize alef/ya)
- Word tokenization: split on whitespace (Arabic words are space-delimited despite connected letters)
- For more sophisticated comparison, use character n-grams (trigrams) to capture partial word matches
