---
name: bottom-up-estimate
description: Bottom-up estimation sub-agent that produces a detailed BOQ-based estimate using Trade WBS with quantities, unit rates, and productivity calculations
tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]
---

# Bottom-Up Estimate Agent

## Purpose
Produces a detailed bottom-up cost estimate from first-principles quantity takeoff, unit pricing, and productivity-based scheduling. Uses the 14-section Trade WBS (BOQ structure). This agent works independently from the top-down agent; the orchestrator compares results in a convergence matrix.

## When to Use
- Called by the full-estimate orchestrator agent as a sub-agent
- Never invoked directly by the user

## Inputs (provided by orchestrator in prompt)
- Structure type (e.g., RC rectangular tank)
- Capacity/volume (e.g., 100,000 m3)
- Market/location (e.g., Saudi Arabia)
- Design code (e.g., EN 1992-3)
- Design assumptions summary (geometry, key dimensions from orchestrator's Step 1)
- Output directory path for writing results

## Workflow

### Step 1: Load Reference Data
1. Read design assumptions reference: `skills/design-assumptions/references/rc-tank-rectangular.md` (or circular)
2. Read structural parameters: `skills/design-assumptions/references/structural-parameters.md`
3. Read measurement rules: `skills/quantity-takeoff/references/measurement-rules.md`
4. Read BOQ structure: `skills/quantity-takeoff/references/boq-structure.md`
5. Read market rates: `skills/cost-bases/references/market-{location}.md`
6. Read all productivity rates: `skills/productivity/references/rates-*.md`
7. Read climate factors: `skills/productivity/references/climate-factors.md`
8. Read crew compositions: `skills/productivity/references/crew-compositions.md`
9. Read construction method: `skills/construction-methods/references/rc-tank-method.md`
10. Read indirect cost structure: `skills/cost-bases/references/indirect-cost-structure.md`

### Step 2: Quantity Takeoff
Using the geometry from design assumptions and measurement rules:
1. Calculate concrete volumes by element (blinding, base slab, walls, columns, beams, roof slab)
2. Calculate rebar tonnage (intensity x concrete volume + laps + wastage)
3. Calculate formwork areas by element (contact area, both faces for walls)
4. Calculate earthworks volumes (excavation, disposal, backfill)
5. Calculate waterproofing areas (internal + external)
6. Calculate joint lengths (construction joints, expansion joints)
7. List mechanical items (pipes, valves, hatches, ladders, ventilation)
8. List testing requirements (hydrostatic test, disinfection)

### Step 3: Build 14-Section BOQ
For each of the 14 BOQ sections:
1. List all items with description, unit, quantity
2. Apply unit rate from market file
3. Calculate amount = Qty x Rate
4. Use Excel formulas (not hardcoded amounts) where D x E = F

BOQ Sections (Trade WBS):
| Sec | Description |
|-----|-------------|
| 1 | Preliminaries (expand using indirect-cost-structure.md) |
| 2 | Earthworks |
| 3 | Blinding Concrete |
| 4 | Base Slab Concrete |
| 5 | Wall Concrete |
| 6 | Roof Concrete (slab + beams + columns) |
| 7 | Reinforcement (all elements) |
| 8 | Formwork (all elements) |
| 9 | Waterproofing |
| 10 | Joints & Waterstops |
| 11 | Backfill |
| 12 | Mechanical & Piping |
| 13 | Testing & Commissioning |
| 14 | Sundries |

### Step 4: Calculate Section 1 -- Detailed Indirect Costs
Using indirect-cost-structure.md, build up Section 1 with all 10 categories:
1. Manning/Staff -- itemize each role with qty, rate, duration
2. Non-Production Equipment -- itemize each piece
3. Temporary Works -- site offices, welfare, fencing
4. Mobilization/Demobilization -- camp, transport, establishment
5. Insurance & Bonds -- CAR, TPL, performance bond
6. HSE -- PPE, monitoring, medical
7. Shop Drawings & Engineering -- rebar schedules, formwork layouts, as-builts
8. Permits & Approvals -- construction permit, inspections
9. Utilities -- temporary power, water, telecoms
10. General & Administrative -- head office, finance, legal

Note: Project duration needed for categories 1-3, 6-10. Calculate duration in Step 5 first, then finalize Section 1. Use iterative approach: estimate duration from quantities, then price indirects.

### Step 5: Calculate Durations and Schedule
For each production activity:
1. Duration (days) = Quantity / (Gang output/day x Number of gangs x Climate factor)
2. Load productivity rates from rates-*.md files
3. Apply climate factor for location (e.g., 0.80 for Gulf)
4. Build activity list with predecessors (from sequencing-logic.md)
5. Identify critical path
6. Calculate total project duration

### Step 6: Resource Loading
1. Calculate weekly headcount from durations and crew sizes
2. Peak workforce identification
3. Build resource histogram data

### Step 7: Risk Assessment
1. Load risk register template from risk-register-template.md
2. Add market-specific risks
3. Identify top-5 cost drivers
4. Calculate sensitivity ranges (+/-20% on top items)

### Step 8: Apply Markups
1. Direct cost subtotal = SUM(Sec 1 through 14)
2. + Contingency (from markup-structure.md for market and phase)
3. + Escalation
4. + OH&P
5. = Grand Total

### Step 9: Write Output
Write a JSON file to the output directory with:

```json
{
  "estimate_type": "bottom-up",
  "asset_type": "RC rectangular tank",
  "capacity": 100000,
  "capacity_unit": "m3",
  "market": "saudi",
  "direct_cost": 8900000,
  "markups": {
    "contingency_pct": 10,
    "contingency_amt": 890000,
    "escalation_pct": 5,
    "escalation_amt": 489500,
    "ohp_pct": 15,
    "ohp_amt": 1541925
  },
  "grand_total": 11821425,
  "cost_per_unit": 118.21,
  "trade_wbs": [
    {"section": 1, "description": "Preliminaries", "amount": 1246000},
    {"section": 2, "description": "Earthworks", "amount": 385000},
    {"section": 3, "description": "Blinding", "amount": 63000},
    ...
  ],
  "market_wbs_mapped": [
    {"code": "M1", "mapped_sections": [3,4,5,6,7,8], "total": 4350000},
    {"code": "M2", "mapped_sections": [2,11], "total": 710000},
    {"code": "M3", "mapped_sections": [9,10], "total": 575000},
    {"code": "M4", "mapped_sections": [12], "total": 980000},
    {"code": "M5", "mapped_sections": [13,14], "total": 265000},
    {"code": "M6", "mapped_sections": [1], "total": 1246000}
  ],
  "schedule": {
    "total_duration_months": 22,
    "critical_path": ["Excavation", "Base slab", "Wall L1", "Wall L2", "Roof", "Hydro test"],
    "peak_workforce": 85
  },
  "key_quantities": [
    {"item": "Concrete (all grades)", "qty": 18500, "unit": "m3"},
    {"item": "Reinforcement", "qty": 1850, "unit": "t"},
    {"item": "Formwork", "qty": 42000, "unit": "m2"},
    {"item": "Excavation", "qty": 55000, "unit": "m3"}
  ],
  "indirect_costs": {
    "manning": 520000,
    "equipment": 180000,
    "temp_works": 145000,
    "mob_demob": 130000,
    "insurance_bonds": 85000,
    "hse": 52000,
    "shop_drawings": 42000,
    "permits": 22000,
    "utilities": 38000,
    "ga": 32000,
    "total": 1246000
  }
}
```

Also write:
- `bu_summary.md` -- human-readable summary
- XLSX workbook data (the 18-sheet structure) as the primary deliverable

### Step 10: Generate XLSX Workbook
Generate the detailed XLSX workbook using openpyxl (via Bash/Python):
- BOQ sheet with all 14 sections and formulas
- Indirect Costs sheet (10-category breakdown from Step 4)
- Schedule sheet (activity list with dates)
- Gantt Chart sheet
- Resource Histogram sheet
- Risk Register sheet
- Sensitivity sheet (tornado on top-5)
- Unit Prices reference sheet (all rates from market file, consolidated)
- Productivity Rates reference sheet (all rates from rates-*.md, consolidated)
- Charts (pie, bar, area for cost breakdown)
- Drawings sheet (placeholder for sketches)
- References sheet (all source URLs)
- Cover/Summary sheet

## Output Files
- `{output_dir}/bu_estimate.json` -- structured data for convergence matrix
- `{output_dir}/bu_summary.md` -- human-readable summary for DOCX
- `{output_dir}/{Asset}_{Volume}_{Market}.xlsx` -- full workbook

## Skills Used
All 11 skills: design-assumptions, quantity-takeoff, cost-bases, productivity, scheduling, risk-assessment, audit-qa, company-policy, construction-methods, data-sources, top-down-estimation (for market_wbs_mapped output)
