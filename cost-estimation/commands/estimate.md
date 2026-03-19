---
description: Generate a complete cost estimate with XLSX workbook (18 sheets, charts, Gantt) and DOCX deliverables
argument-hint: "<structure type> <volume> <location> [--code EN|ACI]"
---

# /estimate -- Cost Estimation Generator

## Overview
Produces a complete cost estimate package for a single market: 18-sheet XLSX workbook with charts, Executive Summary DOCX, and Audit Report DOCX.

## Invocation
```
/estimate RC rectangular tank 100000m3 Saudi Arabia
/estimate RC circular tank 50000m3 international
/estimate RC rectangular tank 200000m3 UAE --code ACI
```

## Workflow
1. **Collect inputs**: Structure type, volume, location, design code (default EN 1992-3)
2. **Load design assumptions**: Select reference file (rc-tank-rectangular or rc-tank-circular)
3. **Quantity takeoff**: Calculate all quantities using measurement rules
4. **Apply rates**: Load market-specific rates from cost-bases
5. **Adjust productivity**: Apply climate/location factors
6. **Build BOQ**: 14-section bill of quantities with Excel formulas
7. **Calculate duration**: Duration = Qty / (Rate x Gangs x Factor)
8. **Build schedule**: Activity list with dependencies, Gantt chart
9. **Resource histogram**: Weekly headcount loading
10. **Risk assessment**: Risk register + sensitivity (top 5 items +/-20%)
11. **Generate charts**: Pie, bar, area, Gantt, histogram
12. **Generate XLSX**: 18-sheet workbook
13. **Generate Executive Summary DOCX**: 5-7 page document
14. **Generate Audit Report DOCX**: Formula audit + rate verification
15. **Self-audit**: Run audit-qa checklist, fix issues

## Outputs
- `[Asset]_[Volume]_[Market].xlsx`
- `[Asset]_Executive_Summary_[Market].docx`
- `[Asset]_Audit_Report_[Market].docx`

## Skills Used
All 10 skills: design-assumptions, quantity-takeoff, cost-bases, productivity, scheduling, risk-assessment, audit-qa, company-policy, construction-methods, data-sources
