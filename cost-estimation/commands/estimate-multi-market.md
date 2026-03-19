---
description: Generate the same estimate across multiple markets for side-by-side cost comparison
argument-hint: "<structure type> <volume> --markets <market1,market2,...>"
---

# /estimate-multi-market -- Multi-Market Cost Comparison

## Overview
Produces identical estimates for the same structure across 2+ markets, then generates a comparison summary.

## Invocation
```
/estimate-multi-market RC rectangular tank 100000m3 --markets international,saudi,uae
/estimate-multi-market RC circular tank 50000m3 --markets international,egypt
```

## Workflow
1. Run `/estimate` for each market (same geometry, different rates)
2. Collect: total cost, $/m3, duration, key rate differences
3. Generate comparison table
4. Identify cheapest/most expensive and explain why

## Outputs
- One XLSX + 2 DOCX per market
- Comparison summary table
