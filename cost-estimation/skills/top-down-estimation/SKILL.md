---
name: top-down-estimation
description: Top-down cost estimation from market benchmarks and capacity factors. Use when the user asks about parametric estimation, order-of-magnitude costs, capacity-based costing, Market WBS, top-down vs bottom-up comparison, convergence analysis, benchmark rates per unit capacity, or factored estimation methods.
---

# Top-Down Estimation -- Market Benchmark Approach

## Purpose
Top-down estimation derives project cost from published market benchmarks ($/m3 stored, $/MW, $/unit capacity) and discipline-level percentage splits. It is independent of detailed quantities and unit prices. The top-down estimate provides a rapid order-of-magnitude check against the detailed bottom-up BOQ.

## When to Use
- Early-stage feasibility (AACE Class 5/4) when detailed design is not available
- As a parallel check against bottom-up estimates at any project phase
- When comparing projects across markets or time periods
- When validating that a bottom-up estimate is in the right ballpark

## Market WBS vs Trade WBS
The top-down estimate uses a **Market WBS** (7 high-level discipline categories), NOT the 14-section trade-based BOQ used by the bottom-up estimate. The Market WBS groups costs by functional discipline:

| Code | Category | Benchmark Basis |
|------|----------|----------------|
| M1 | Civil/Structural | $/m3 concrete volume |
| M2 | Earthworks | $/m3 excavated volume |
| M3 | Waterproofing | $/m2 treated area |
| M4 | Mechanical/Piping | % of civil |
| M5 | Testing/Commissioning | LS or % of direct |
| M6 | Preliminaries/Indirects | % of direct or $/month |
| M7 | Contractor Markup | % compound |

## Methodology
1. Select asset type and capacity (e.g., RC rectangular tank, 100,000 m3)
2. Look up benchmark rate from capacity-benchmarks.md (e.g., $116/m3 stored for Saudi)
3. Calculate total project cost = capacity x benchmark rate
4. Split into Market WBS categories using discipline breakdown percentages
5. State an explicit assumption for each line item
6. Document basis, source, and date for every benchmark used

## Assumption Documentation Format
Every top-down line item must have:
- **Assumption ID**: TD-A001, TD-A002, etc.
- **Assumption text**: Clear statement of what is assumed
- **Basis**: Source reference (publication, date, comparable project)
- **Impact level**: High / Medium / Low (sensitivity to total cost)

Example:
| ID | Assumption | Basis | Impact |
|----|-----------|-------|--------|
| TD-A001 | Civil/structural = 40% of total | Industry average for RC tanks 50k-200k m3, IMARC 2025 | High |
| TD-A002 | Earthworks assumes sandy soil, no rock | Typical Gulf conditions, geotechnical not confirmed | Medium |

## Convergence with Bottom-Up
After both estimates are complete, the orchestrator builds a convergence matrix:
1. Map Market WBS categories to Trade WBS sections (see market-wbs.md mapping table)
2. Calculate variance = (TD - BU) / BU for each mapped category
3. Flag items exceeding threshold (see market-wbs.md thresholds)
4. Investigate flagged items -- differences typically indicate:
   - Scope gaps (item in one estimate but not the other)
   - Rate discrepancies (benchmark vs actual market price)
   - Quantity errors (assumed vs calculated)
   - Assumption misalignment (different design basis)

## Scaling Rules
- **Six-tenths rule**: Cost2 = Cost1 x (Capacity2 / Capacity1)^0.6
- Applicable for same asset type, same market, capacity ratio < 10x
- Adjust for market location factors after scaling
