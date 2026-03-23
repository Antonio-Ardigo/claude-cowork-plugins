---
description: Generate a complete dual-path cost estimate with convergence matrix, XLSX workbook (~24 sheets, charts, Gantt) and DOCX deliverables
argument-hint: "<structure type> <volume> <location> [--code EN|ACI]"
---

# /estimate -- Dual-Path Cost Estimation Generator

## Overview
Produces a complete cost estimate package for a single market using both top-down (market benchmarks) and bottom-up (detailed BOQ) approaches. The orchestrator compiles a convergence matrix comparing both estimates, a Pareto analysis of main quantities, detailed indirect costs, and consolidated reference sheets for unit prices and productivity rates.

## Invocation
```
/estimate RC rectangular tank 100000m3 Saudi Arabia
/estimate RC circular tank 50000m3 international
/estimate RC rectangular tank 200000m3 UAE --code ACI
```

## Workflow
1. **Parse scope**: Extract structure type, volume, location, design code (default EN 1992-3)
2. **Design assumptions**: Load geometry reference, calculate key dimensions
3. **Launch top-down agent**: Market benchmark estimate using Market WBS (7 categories) with documented assumptions
4. **Launch bottom-up agent**: Detailed BOQ estimate using Trade WBS (14 sections) with quantities, unit rates, productivity, schedule, risk
5. **Convergence matrix**: Compare TD vs BU by mapped WBS categories, flag variances exceeding thresholds
6. **Main quantities (Pareto)**: Extract items covering 80% of cost with assumptions for each
7. **Indirect costs breakdown**: Expand preliminaries into 10 categories (manning, equipment, shop drawings, mob/demob, insurance, HSE, permits, utilities, G&A)
8. **Unit prices reference**: Consolidate all rates into single reference sheet
9. **Productivity rates reference**: Consolidate all rates with climate adjustments into single reference sheet
10. **Generate XLSX**: ~24-sheet workbook with formulas, charts, cross-references
11. **Generate DOCX**: Executive Summary (with convergence discussion) + Audit Report (with convergence check)
12. **Self-audit**: Run QC checklist including convergence verification

## Outputs
- `[Asset]_[Volume]_[Market].xlsx` (~24 sheets including convergence matrix, Pareto, indirects, unit prices, productivity rates)
- `[Asset]_Executive_Summary_[Market].docx` (6-8 pages with convergence analysis)
- `[Asset]_Audit_Report_[Market].docx` (audit with convergence check)

## XLSX Sheet Structure
| Group | Sheets |
|-------|--------|
| Summary | Cover, Convergence Matrix |
| Top-Down | TD-Estimate, TD-Assumptions |
| Bottom-Up | BOQ-Detail, Duration Calc |
| Pareto & Indirects | Main Quantities, Indirect Costs |
| References | Unit Prices, Productivity Rates |
| Schedule | Schedule, Gantt Chart, Resource Histogram |
| Risk | Risk Register, Sensitivity |
| Charts | Cost Breakdown, S-Curve |
| Supporting | Drawings, References/Sources |

## Skills Used
All 11 skills: design-assumptions, quantity-takeoff, cost-bases, productivity, scheduling, risk-assessment, audit-qa, company-policy, construction-methods, data-sources, top-down-estimation
