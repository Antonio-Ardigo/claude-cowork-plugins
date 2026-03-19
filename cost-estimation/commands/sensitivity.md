---
description: Run sensitivity analysis on an existing estimate -- tornado diagram on top cost drivers
argument-hint: "<path to XLSX> [--parameters concrete,rebar,productivity] [--range 20]"
---

# /sensitivity -- Sensitivity & Tornado Analysis

## Overview
Varies top cost drivers +/-20% to produce a tornado diagram showing cost impact.

## Invocation
```
/sensitivity ./Tank_100000m3_SAUDI.xlsx
/sensitivity ./estimate.xlsx --parameters concrete,rebar --range 25
```

## Workflow
1. Load workbook, read Cost Summary
2. Identify top-5 cost items by value
3. Vary each +/-20% (or specified range)
4. Generate tornado data and chart
5. Break-even analysis on key assumptions
6. Update Sensitivity sheet in XLSX

## Output
- Updated Sensitivity Analysis sheet with tornado chart
