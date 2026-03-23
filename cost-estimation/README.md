# Cost Estimation Plugin (v2.0)

Civil and structural cost estimation with dual-path architecture. A top-down agent (market benchmarks) and a bottom-up agent (detailed BOQ) run independently, then converge in a comparison matrix to spot discrepancies. Produces professional XLSX workbooks (~24 sheets with charts, Gantt, convergence matrix) and DOCX deliverables.

## Key Features
- **Dual-path estimation**: Top-down (Market WBS, 7 categories) + Bottom-up (Trade WBS, 14-section BOQ)
- **Convergence matrix**: Compares TD vs BU by mapped WBS categories, flags variances
- **Main quantities Pareto**: Items covering 80% of cost with stated assumptions
- **Detailed indirect costs**: 10-category breakdown (manning, equipment, shop drawings, mob/demob, insurance, HSE, permits, utilities, G&A)
- **Reference sheets**: Consolidated unit prices and productivity rates in single source-of-truth sheets
- **7 domain skills**: Design assumptions, productivity rates, cost bases, data sources, company policy, construction methods, top-down estimation
- **4 cross-cutting skills**: Quantity takeoff, scheduling, risk assessment, audit/QA
- **Multi-market**: International, Saudi Arabia, UAE, Egypt (swap rate files, keep geometry)
- **Complete deliverables**: ~24-sheet XLSX + Executive Summary DOCX + Audit Report DOCX
- **Auditable**: Every number traces to a published source with URL and date

## Commands

| Command | Description |
|---------|-------------|
| `/estimate` | Generate dual-path estimate (TD + BU + convergence) for one market |
| `/estimate-multi-market` | Compare same project across markets with convergence per market |
| `/review-estimate` | Audit an existing XLSX estimate |
| `/sensitivity` | Tornado analysis on cost drivers |
| `/method-statement` | Generate construction method statement |

## Agents

| Agent | Description |
|-------|-------------|
| `full-estimate` | Orchestrator: launches TD + BU agents, compiles convergence + Pareto + indirects |
| `top-down-estimate` | Market benchmark estimate using Market WBS with documented assumptions |
| `bottom-up-estimate` | Detailed BOQ estimate using Trade WBS with quantities, rates, productivity |

## Skills

### Domain Skills (7)
| Skill | Triggers On |
|-------|------------|
| `design-assumptions` | Tank dimensions, concrete grades, structural config |
| `productivity` | Production rates, gang sizes, climate factors |
| `cost-bases` | Material prices, labor costs, equipment rates |
| `data-sources` | Source URLs, audit trail, references |
| `company-policy` | Report formats, approval thresholds, QC |
| `construction-methods` | Pour sequences, method statements, testing |
| `top-down-estimation` | Market benchmarks, capacity factors, Market WBS, convergence |

### Cross-Cutting Skills (4)
| Skill | Triggers On |
|-------|------------|
| `quantity-takeoff` | BOQ preparation, measurement rules |
| `scheduling` | Gantt charts, durations, critical path |
| `risk-assessment` | Risk register, sensitivity, contingency |
| `audit-qa` | Estimate review, benchmarking, formula checks |

## XLSX Workbook Structure (~24 sheets)

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

## Design Principles
1. **Dual-path estimation**: Top-down and bottom-up run independently, converge to spot issues
2. **Domain isolation**: Change one rate = edit one file
3. **Same geometry, different cost**: Swap market file for multi-market
4. **Auditable trail**: Every number has published source + date + URL
5. **Company policy overrides**: Policy rules always win
6. **Assumptions documented**: Every estimate line has a stated assumption with ID, basis, and impact

## Adding a New Market
1. Copy `skills/cost-bases/references/market-international.md` to `market-newcountry.md`
2. Update all unit rates with local pricing
3. Add climate factor to `skills/productivity/references/climate-factors.md`
4. Add location adjustment factor to `skills/top-down-estimation/references/capacity-benchmarks.md`
5. Add sources to `skills/data-sources/references/pricing-sources.md`
