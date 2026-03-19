---
description: Audit an existing XLSX cost estimate against benchmarks and quality standards
argument-hint: "<path to existing XLSX>"
---

# /review-estimate -- Estimate Audit & Review

## Overview
Reviews an existing XLSX workbook, checking formulas, rates, quantities, and benchmarks. Produces an Audit Report DOCX.

## Invocation
```
/review-estimate C:/path/to/Tank_100000m3_FINAL.xlsx
/review-estimate ./estimate.xlsx
```

## Workflow
1. Load workbook, identify sheets and structure
2. Formula audit: check all cells for errors
3. BOQ-Summary reconciliation
4. Rate verification against market benchmarks
5. Quantity spot-check (3-5 key items)
6. $/m3 benchmark comparison
7. Markup check against policy
8. Completeness check (18 sheets, charts, references)
9. Generate Audit Report DOCX

## Output
- Audit Report DOCX with findings and PASS/FAIL status
