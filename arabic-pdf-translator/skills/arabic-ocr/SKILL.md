---
name: arabic-ocr
description: Arabic OCR preprocessing, multi-engine text extraction, and Arabic-specific post-processing. Use when the user asks about Arabic OCR, extracting text from Arabic PDFs, scanned Arabic documents, Tesseract for Arabic, EasyOCR Arabic, PaddleOCR Arabic, image preprocessing for OCR, deskewing, denoising, binarization, CLAHE contrast, OCR engine comparison, Arabic text extraction from images, or multi-engine OCR consensus.
version: 1.0.0
---

# Arabic OCR Skill

You are an expert in Optical Character Recognition for Arabic script. You understand the unique challenges of Arabic OCR (right-to-left text, connected letters, diacritical marks, ligatures) and the multi-engine approach used by the arabic_pdf_translator pipeline.

## The 7-Stage Preprocessing Pipeline

Arabic script requires specialized image preprocessing to achieve high OCR accuracy. The pipeline processes images in this order:

### Stage 1: Grayscale Conversion
- Convert to single channel using `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)`
- Removes color information that adds noise to OCR

### Stage 2: Upscaling
- If image height < 2000px, upscale using cubic interpolation (`cv2.INTER_CUBIC`)
- Arabic diacritical dots need sufficient resolution to be recognized
- Target: at least 2000px height for reliable dot detection

### Stage 3: Denoising
- `cv2.fastNlMeansDenoising(h=8, templateWindowSize=7, searchWindowSize=21)`
- **Critical for Arabic**: Parameters are deliberately gentle (h=8 instead of higher) to preserve small dots (nuqat) that distinguish letters like ba/ta/tha
- Aggressive denoising destroys diacritics

### Stage 4: Contrast Enhancement (CLAHE)
- Contrast Limited Adaptive Histogram Equalization
- `clipLimit=2.0, tileGridSize=(8,8)`
- Handles uneven illumination common in scanned documents
- Improves visibility of faded ink while preventing over-enhancement

### Stage 5: Deskewing
- Detects text line angle via Hough line transform
- Rotates image if angle > 0.5 degrees
- Even small rotation significantly degrades Arabic OCR because connected letter shapes depend on baseline alignment

### Stage 6: Adaptive Binarization
- `cv2.adaptiveThreshold` with Gaussian method
- `blockSize=31, C=10` -- tuned for Arabic script stroke width
- Handles local illumination variations better than global thresholding

### Stage 7: Morphological Cleanup
- Opening + closing with 2x2 kernel
- Removes small noise specks while preserving Arabic dots
- Small kernel (2x2) is critical -- larger kernels destroy dots

## Multi-Engine OCR

The pipeline runs multiple OCR engines and selects the best result by confidence-weighted text length.

### Tesseract OCR
- **Configuration**: OEM 3 (LSTM neural net), PSM 6 (uniform block of text), lang="ara"
- **Strengths**: Good baseline, mature Arabic support, handles structured documents well
- **Weaknesses**: Struggles with decorative fonts and heavily diacritized text
- **Output**: Word-level confidences (0-100 scale, normalized to 0-1)

### EasyOCR
- **Configuration**: Languages=["ar"], GPU flag configurable
- **Strengths**: Better with varied fonts, handles mixed Arabic/Latin text
- **Weaknesses**: Slower than Tesseract, paragraph detection can merge lines
- **Output**: Text blocks with per-block confidence, paragraph mode for RTL ordering

### PaddleOCR
- **Configuration**: lang="ar", use_angle_cls=True (handles rotated text)
- **Strengths**: Strong with modern Arabic typefaces, good angle detection
- **Weaknesses**: Smaller Arabic training set than Tesseract
- **Output**: Line-level results with bounding boxes and confidence

### Engine Selection Logic
- Run all configured engines
- Score each: `score = text_length * confidence`
- If top engine's confidence > (second best - 0.15), prefer the more confident one
- This favors quality over quantity -- a shorter but higher-confidence result wins over a longer but uncertain one

## Arabic Post-Processing

After OCR, Arabic-specific cleanup is applied:

### Character Confusion Pairs
Common OCR errors for Arabic script:

| OCR Output | Correct Character | Description |
|-----------|------------------|-------------|
| U+06A9 (keheh) | U+0643 (kaf) | Persian vs Arabic kaf |
| U+06CC (yeh) | U+064A (ya) | Persian vs Arabic ya |
| U+0649 (alef maqsura) | U+064A (ya) | Context-dependent correction |

### Processing Steps
1. **Noise removal**: Strip non-Arabic characters except digits and common punctuation
2. **Character confusion fixing**: Apply confusion pair mappings
3. **Broken word repair**: Reconnect single-character fragments, fix broken "al-" prefix
4. **Whitespace normalization**: Collapse multiple spaces/newlines
5. **Punctuation correction**: Convert Latin punctuation to Arabic equivalents (, -> ، ; -> ؛ ? -> ؟)
6. **Isolated character removal**: Remove standalone characters unless they're valid Arabic single-letter words (wa, alef, ba, fa, lam, kaf)
7. **RTL line ordering**: Ensure Arabic lines have RTL Unicode markers (U+200F or U+202B)

### Multi-Engine Consensus Merging
When multiple engines return results, consensus merging picks the longest valid line per position across engines, preferring longer text that passed post-processing.

## Recommendations by Document Type

| Document Type | Recommended DPI | Engines | Notes |
|--------------|----------------|---------|-------|
| Clean printed PDF | 300 | Tesseract | Fast, sufficient quality |
| Scanned book | 400 | Tesseract + EasyOCR | Higher DPI for aging paper |
| Handwritten | 400+ | EasyOCR + PaddleOCR | Skip Tesseract for handwriting |
| Mixed Arabic/English | 300 | EasyOCR | Best multilingual support |
| Low-quality scan | 400-600 | All three | Use ensemble for noisy input |
| Diacritized text (Quran) | 400 | Tesseract + EasyOCR | Gentle preprocessing, preserve tashkeel |

## Native Mode OCR via Claude Vision

When the Python OCR pipeline is unavailable (e.g., in the Cowork VM), Claude's built-in vision capabilities serve as a fallback for reading Arabic text from PDF page images.

### How It Works
- The Read tool presents PDF pages as images to Claude
- Claude reads the Arabic text directly using its multimodal understanding
- No image preprocessing is applied (no deskewing, denoising, binarization)

### Strengths
- Works without any Python dependencies or OCR binaries
- Good with clean, printed Arabic text at reasonable resolution
- Handles mixed Arabic/Latin text well
- Can understand context and disambiguate characters

### Limitations
- No multi-engine consensus (single-pass reading)
- May miss fine diacritical marks (nuqat, tashkeel) especially on small or faded text
- No confidence-weighted scoring across engines
- Handwritten Arabic is significantly harder than for trained OCR models
- No image preprocessing means noisy/skewed scans produce worse results

### Self-Assessment Guidelines
When using native mode OCR, assess reading confidence per page:
- **0.90+**: Clean printed text, modern typeface, good resolution
- **0.75-0.89**: Readable but some characters uncertain (faded ink, small font, decorative script)
- **0.60-0.74**: Multiple uncertain characters, possible misreadings of similar letters (ba/ta/tha)
- **Below 0.60**: Significant portions illegible -- recommend pipeline mode with higher DPI
