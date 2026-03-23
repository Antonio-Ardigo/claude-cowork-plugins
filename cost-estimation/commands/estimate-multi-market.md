---
description: Generate the same dual-path estimate across multiple markets for side-by-side cost comparison with convergence analysis per market
argument-hint: "<structure type> <volume> --markets <market1,market2,...>"
---

# /estimate-multi-market -- Multi-Market Cost Comparison

## Overview
Produces identical dual-path estimates (top-down + bottom-up with convergence) for the same structure across 2+ markets, then generates a comparison summary including convergence data per market.

## Invocation
```
/estimate-multi-market RC rectangular tank 100000m3 --markets international,saudi,uae
/estimate-multi-market RC circular tank 50000m3 --markets international,egypt
```

## Workflow
1. Run `/estimate` for each market (same geometry, different rates and benchmarks)
   - Each market produces both top-down and bottom-up estimates
   - Each market produces a convergence matrix
2. Collect per market: TD total, BU total, convergence variance, $/m3, duration, key rate differences
3. Generate comparison summary table with convergence status per market
4. Identify cheapest/most expensive and explain why (rate differences, productivity factors, markup levels)
5. Flag any market where convergence variance exceeds threshold -- may indicate market-specific data issues

## Comparison Table Format
| Metric | International | Saudi | UAE |
|--------|-------------|-------|-----|
| TD Total ($) | ... | ... | ... |
| BU Total ($) | ... | ... | ... |
| Convergence Variance | ... | ... | ... |
| Convergence Status | CONVERGED | INVESTIGATE | CONVERGED |
| Final $/m3 | ... | ... | ... |
| Duration (months) | ... | ... | ... |
| Peak Workforce | ... | ... | ... |

## Outputs
- One XLSX (~24 sheets) + 2 DOCX per market
- Cross-market comparison summary table
- Convergence status per market
