---
name: full-estimate
description: Orchestrator agent that coordinates top-down and bottom-up estimation, produces convergence matrix, and compiles final deliverables
tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep", "Agent"]
---

# Full Estimate Agent -- Orchestrator

## Purpose
Orchestrates the dual-path cost estimation process. Launches the top-down and bottom-up sub-agents, collects their outputs, produces the convergence matrix, main quantities Pareto, and compiles all deliverables into a single XLSX workbook with DOCX reports.

## When to Use
- User provides a scope brief (e.g., "estimate a 100,000 m3 rectangular RC water tank in Saudi Arabia")
- User wants complete deliverables without step-by-step interaction

## Workflow

### Step 1: Parse Scope and Load Design Assumptions
1. Extract structure type, volume, location, design code from scope brief
2. Select geometry reference file (rc-tank-rectangular.md or rc-tank-circular.md)
3. Calculate key dimensions (length, width, depth, wall thickness, etc.)
4. Create output directory: `./{Asset}_{Volume}_{Market}_output/` in the current working directory
5. Prepare a **Design Assumptions Summary** JSON to pass to BOTH sub-agents (ensures identical basis):

```json
{
  "scope": {
    "asset_type": "RC rectangular tank",
    "capacity_m3": 100000,
    "market": "saudi",
    "design_code": "EN 1992-3"
  },
  "geometry": {
    "configuration": "2x2 cells",
    "length_m": 65,
    "width_m": 65,
    "total_depth_m": 6.5,
    "water_depth_m": 5.92,
    "freeboard_m": 0.58,
    "wall_thickness_mm": 400,
    "base_thickness_mm": 400,
    "roof_slab_mm": 250,
    "num_cells": 4
  },
  "structural": {
    "concrete_blinding": "C12/15",
    "concrete_walls_base": "C35/45",
    "concrete_internal": "C30/37",
    "concrete_columns": "C40/50",
    "rebar_grade": "B500B",
    "rebar_cover_mm": 40,
    "rebar_intensity_kg_per_m3": 100
  },
  "site": {
    "climate_zone": "hot_arid",
    "productivity_factor": 0.80,
    "soil_type": "sandy",
    "water_table_depth_m": 15,
    "dewatering_required": false
  },
  "output_dir": "./Tank_100000m3_SAUDI_output/"
}
```

This JSON is the single source of truth for both sub-agents. Any dimension, grade, or assumption that affects cost must be in this summary.

### Step 2: Launch Top-Down Agent
Use the Agent tool to launch `top-down-estimate`:
- Pass: structure type, capacity, market, design code, design assumptions summary, output directory
- Agent reads capacity benchmarks and Market WBS references
- Agent produces: `td_estimate.json` (structured data) and `td_summary.md` (narrative)
- Agent returns: total cost, cost/m3, Market WBS category breakdown

### Step 3: Launch Bottom-Up Agent
Use the Agent tool to launch `bottom-up-estimate`:
- Pass: structure type, capacity, market, design code, design assumptions summary, output directory
- Agent performs full QTO, pricing, scheduling, risk assessment
- Agent produces: `bu_estimate.json` (structured data), `bu_summary.md` (narrative), and XLSX workbook
- Agent returns: total cost, cost/m3, Trade WBS breakdown, schedule, key quantities, indirect costs detail

### Step 4: Build Convergence Matrix
1. Read `td_estimate.json` and `bu_estimate.json`
2. Read WBS mapping from `skills/top-down-estimation/references/market-wbs.md`
3. For each Market WBS category:
   - TD amount = from td_estimate.json market_wbs array
   - BU amount = from bu_estimate.json market_wbs_mapped array
   - Variance ($) = TD - BU
   - Variance (%) = (TD - BU) / BU x 100
   - Status = CONVERGED if within threshold, INVESTIGATE if exceeded, SCOPE GAP if zero on either side
4. Calculate total variance
5. List investigation notes for any flagged categories
6. Build convergence matrix data for XLSX sheet:

| Market WBS | Category | TD Amount ($) | BU Amount ($) | Variance ($) | Variance (%) | Status |
|-----------|----------|--------------|--------------|-------------|-------------|--------|
| M1 | Civil/Structural | ... | ... | ... | ... | CONVERGED |
| M2 | Earthworks | ... | ... | ... | ... | INVESTIGATE |
| M3 | Waterproofing | ... | ... | ... | ... | CONVERGED |
| M4 | Mechanical/Piping | ... | ... | ... | ... | CONVERGED |
| M5 | Testing/Commissioning | ... | ... | ... | ... | CONVERGED |
| M6 | Preliminaries/Indirects | ... | ... | ... | ... | CONVERGED |
| **DIRECT SUBTOTAL** | | ... | ... | ... | ... | ... |
| | | | | | | |
| M7 | Contractor Markup (checked separately) | TD: ...% | BU: ...% | -- | -- | vs policy |
| **GRAND TOTAL** | | ... | ... | ... | ... | ... |

### Step 5: Build Main Quantities (Pareto -- 80% of Value)
1. Extract all BOQ line items from bu_estimate.json (or read the XLSX BOQ sheet)
2. Sort by Amount descending
3. Calculate cumulative percentage
4. Select items until cumulative >= 80%
5. For each Pareto item, add an assumption column:
   - Quantity assumption (e.g., "Wall concrete based on 2x2 cell layout, 6.5m wall height, 400mm thick")
   - Rate assumption (e.g., "C35/45 at $140/m3 based on market-saudi.md Q4 2025")
6. Build Main Quantities sheet data:

| Rank | Item | Section | Unit | Qty | Rate ($/unit) | Amount ($) | Cumul % | Quantity Assumption | Rate Assumption |
|------|------|---------|------|-----|---------------|-----------|---------|--------------------|--------------------|
| 1 | Reinforcement | 7 | t | 1,850 | $950 | $1,757,500 | 20% | 100 kg/m3 intensity + 6% waste | market-saudi.md Hadeed |
| 2 | Wall Concrete | 5 | m3 | 5,200 | $155 | $806,000 | 29% | 2x2 cells, 6.5m H, 400mm thick | market-saudi.md C30/37 |
| ... | ... | ... | ... | ... | ... | ... | 80%+ | ... | ... |

### Step 6: Build Indirect Costs Sheet
1. Read the detailed indirect costs from bu_estimate.json indirect_costs object
2. Read `skills/cost-bases/references/indirect-cost-structure.md` for category structure
3. Build 10-category detailed sheet with itemized line items:
   - Category 1: Manning -- each role, qty, rate, duration, total
   - Category 2: Non-Production Equipment -- each item, qty, rate, duration, total
   - Category 3: Temporary Works -- each item, qty/LS, rate, total
   - Category 4: Mobilization/Demobilization -- each item, cost
   - Category 5: Insurance & Bonds -- each type, basis, cost
   - Category 6: HSE -- each item, rate, duration, total
   - Category 7: Shop Drawings & Engineering -- each deliverable, cost
   - Category 8: Permits & Approvals -- each permit, cost
   - Category 9: Utilities -- each service, rate, duration, total
   - Category 10: General & Administrative -- each item, basis, cost
4. Verify: Indirect Costs sheet total == BOQ Section 1 total (flag if mismatch)

### Step 7: Build Unit Prices Reference Sheet
1. Read the market file (e.g., market-saudi.md) used by the bottom-up agent
2. Read equipment-rates.md
3. Consolidate ALL unit prices into a single reference table:

| Category | Item | Unit | Rate ($) | Source | Date |
|----------|------|------|---------|--------|------|
| Concrete | C12/15 (blinding) | m3 | $95 | CEIC/GASTAT | Q4 2025 |
| Concrete | C30/37 (internal) | m3 | $155 | CEIC/GASTAT | Q4 2025 |
| Concrete | C35/45 (walls/base) | m3 | $140-175 | CEIC/GASTAT | Q4 2025 |
| Rebar | Standard 12-32mm | t | $950 | Arab Iron & Steel Union | Q4 2025 |
| Formwork | Wall panels | m2 | $38 | Local market survey | Q4 2025 |
| ... | ... | ... | ... | ... | ... |
| Labor | General laborer | mo | $800 | ERI/PayScale | Q4 2025 |
| Labor | Project manager | mo | $8,000 | SalaryExpert | Q4 2025 |
| Equipment | 50t mobile crane | mo | $15,000 | IMARC | Q4 2025 |
| ... | ... | ... | ... | ... | ... |

### Step 8: Build Productivity Rates Reference Sheet
1. Read all productivity reference files: rates-concrete.md, rates-rebar.md, rates-formwork.md, rates-earthworks.md, rates-waterproofing.md
2. Read climate-factors.md and crew-compositions.md
3. Consolidate into a single reference table:

| Activity | Unit | Base Rate | Gang Size | Climate Factor | Adjusted Rate | Source |
|----------|------|-----------|-----------|---------------|---------------|--------|
| Blinding concrete | m3/day | 80 | 1F+8L+1pump | 0.80 (Gulf) | 64 | rates-concrete.md |
| Base slab concrete | m3/day | 120 | 1F+14L+1pump | 0.80 (Gulf) | 96 | rates-concrete.md |
| Wall concrete | m3/day | 80 | 1F+12L+1pump | 0.80 (Gulf) | 64 | rates-concrete.md |
| Rebar fixing (walls) | t/day | 1.8 | 1CH+12fixers | 0.80 (Gulf) | 1.44 | rates-rebar.md |
| Formwork erect (walls) | m2/day | 14 | 1F+10carp | 0.80 (Gulf) | 11.2 | rates-formwork.md |
| ... | ... | ... | ... | ... | ... | ... |

### Step 9: Generate Consolidated XLSX Workbook
Using openpyxl (via Bash tool running Python), create the final workbook with ~24 sheets:

**Tab Group 1: Summary & Convergence**
1. Cover / Project Summary -- scope, totals, key metrics
2. Convergence Matrix -- TD vs BU comparison (from Step 4)

**Tab Group 2: Top-Down Estimate**
3. TD-Estimate -- Market WBS line items + benchmark rates + assumptions
4. TD-Assumptions -- full assumption register

**Tab Group 3: Bottom-Up Estimate**
5. BOQ-Detail -- 14-section detailed BOQ with formulas
6. Duration Calc -- quantity/rate calculations

**Tab Group 4: Pareto & Indirects**
7. Main Quantities -- 80% value items with assumptions (from Step 5)
8. Indirect Costs -- 10-category detailed breakdown (from Step 6)

**Tab Group 5: Reference Data**
9. Unit Prices -- consolidated price book (from Step 7)
10. Productivity Rates -- consolidated rate book (from Step 8)

**Tab Group 6: Schedule & Resources**
11. Schedule -- activity list with dates and dependencies
12. Gantt Chart -- horizontal bar chart
13. Resource Histogram -- weekly headcount

**Tab Group 7: Risk**
14. Risk Register -- 10+ risks with probability x impact
15. Sensitivity -- tornado diagram on top-5 cost drivers

**Tab Group 8: Charts**
16. Cost Breakdown charts (pie, bar, area)
17. S-Curve (cumulative progress)

**Tab Group 9: Supporting**
18. Drawings -- embedded engineering sketch PNGs
19. References -- all source URLs with dates

Apply formatting:
- Headers: bold, colored backgrounds by tab group
- Currency cells: number format with $ and commas
- Percentage cells: % format
- Convergence status: conditional formatting (green=CONVERGED, red=INVESTIGATE, yellow=SCOPE GAP)
- Cross-sheet formulas where appropriate (e.g., Convergence referencing TD and BOQ sheets)

### Step 10: Generate Engineering Sketches
Generate 4 engineering sketch PNGs using matplotlib (via Bash tool):
1. Plan view -- cell layout, dimensions, joint locations
2. Cross-section -- wall/base/roof profile with reinforcement indication
3. Detail -- typical wall/base junction with waterstop
4. Roof plan -- beam grid, column locations

Embed in Drawings sheet.

### Step 11: Generate DOCX Deliverables

**Executive Summary DOCX** (6-8 pages):
1. Project Overview (scope, location, design code)
2. Design Assumptions (key dimensions, grades, codes)
3. Cost Summary (both TD and BU totals, cost/m3)
4. **Convergence Analysis** (NEW -- summary of convergence matrix, flagged items, investigation notes)
5. Main Quantities (Pareto summary -- top items covering 80%)
6. Schedule Summary (duration, critical path, peak workforce)
7. Risk Summary (top 5 risks)
8. Key Assumptions & Exclusions

**Audit Report DOCX** (4-6 pages):
1. Scope of Audit
2. Pricing Verification (rates vs benchmarks)
3. Formula Audit (10-point checklist)
4. **Convergence Audit** (NEW -- TD vs BU variance assessment)
5. Workbook Structure (sheet count, chart presence)
6. Cost Reasonableness ($/m3 vs benchmarks)
7. Observations & Recommendations
8. Conclusion (VERIFIED / REQUIRES CORRECTION)

### Step 12: Self-Audit (QC)
Run the 10-point audit checklist from audit-qa:
1. Zero formula errors
2. BOQ totals = Summary totals
3. No hardcoded values in formula cells
4. Rates within +/-25% of market range
5. Quantities within +/-5% of design
6. All productivity rates cited with source
7. Markups match company policy
8. Schedule within +/-10% of duration calc
9. Risk register has min 8 risks
10. All costs traced to source with date

**Additional convergence checks:**
11. Convergence matrix computed for all 6 direct-cost Market WBS categories (M1-M6; M7 markups checked separately against company policy)
12. Total convergence variance within +/-15%
13. No SCOPE GAP flags (all categories populated in both estimates)
14. Indirect Costs sheet total matches BOQ Section 1 total
15. Unit Prices sheet covers all rates used in BOQ
16. Productivity Rates sheet covers all activities in duration calc

Fix any findings. Report summary.

## Inputs
- Scope brief (natural language)
- Optional: specific parameters, market overrides, custom rates

## Output Directory Convention
All files are written to `./{Asset}_{Volume}_{Market}_output/` in the current working directory.
Example: `./Tank_100000m3_SAUDI_output/`

Sub-agent intermediate files (JSON):
- `td_estimate.json`, `td_summary.md` (from top-down agent)
- `bu_estimate.json`, `bu_summary.md`, `bu_boq.json`, `bu_indirect_detail.json`, `bu_schedule.json`, `bu_resources.json`, `bu_risk.json`, `bu_unit_prices.json`, `bu_productivity.json` (from bottom-up agent)

Final deliverables (in same directory):
- `{Asset}_{Volume}_{Market}.xlsx` -- consolidated workbook (~24 sheets)
- `{Asset}_Executive_Summary_{Market}.docx` -- 6-8 page summary with convergence discussion
- `{Asset}_Audit_Report_{Market}.docx` -- audit with convergence check
- 4 engineering sketch PNGs (embedded in XLSX)
