# Cost Estimation Plugin

Civil and structural cost estimation with strict domain separation. Produces professional XLSX workbooks with charts, Gantt schedules, resource histograms, and DOCX deliverables.

## Key Features
- **6 domain skills**: Design assumptions, productivity rates, cost bases, data sources, company policy, construction methods
- **4 cross-cutting skills**: Quantity takeoff, scheduling, risk assessment, audit/QA
- **Multi-market**: International, Saudi Arabia, UAE, Egypt (swap rate files, keep geometry)
- **Complete deliverables**: 18-sheet XLSX + Executive Summary DOCX + Audit Report DOCX
- **Auditable**: Every number traces to a published source with URL and date

## Commands

| Command | Description |
|---------|-------------|
| `/estimate` | Generate complete estimate for one market |
| `/estimate-multi-market` | Compare same project across markets |
| `/review-estimate` | Audit an existing XLSX estimate |
| `/sensitivity` | Tornado analysis on cost drivers |
| `/method-statement` | Generate construction method statement |

## Skills

### Domain Skills
| Skill | Triggers On |
|-------|------------|
| `design-assumptions` | Tank dimensions, concrete grades, structural config |
| `productivity` | Production rates, gang sizes, climate factors |
| `cost-bases` | Material prices, labor costs, equipment rates |
| `data-sources` | Source URLs, audit trail, references |
| `company-policy` | Report formats, approval thresholds, QC |
| `construction-methods` | Pour sequences, method statements, testing |

### Cross-Cutting Skills
| Skill | Triggers On |
|-------|------------|
| `quantity-takeoff` | BOQ preparation, measurement rules |
| `scheduling` | Gantt charts, durations, critical path |
| `risk-assessment` | Risk register, sensitivity, contingency |
| `audit-qa` | Estimate review, benchmarking, formula checks |

## Agent

| Agent | Description |
|-------|-------------|
| `full-estimate` | Autonomous end-to-end estimation from scope brief |

## Design Principles
1. **Domain isolation**: Change one rate = edit one file
2. **Same geometry, different cost**: Swap market file for multi-market
3. **Auditable trail**: Every number has published source + date + URL
4. **Company policy overrides**: Policy rules always win

## Adding a New Market
1. Copy `skills/cost-bases/references/market-international.md` to `market-newcountry.md`
2. Update all unit rates
3. Add climate factor to `skills/productivity/references/climate-factors.md`
4. Add sources to `skills/data-sources/references/pricing-sources.md`
