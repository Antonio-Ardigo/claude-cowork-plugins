# Project Planning Plugin

Engineering and construction project planning with a toll gate (stage-gate) process from concept through Design Freeze.

## Command

### `/project-plan`

Generate a structured project plan following 9 steps across 4 toll gates:

| Step | Phase | Key Output |
|------|-------|-----------|
| 1 | Typical Configuration | Plant cost curves, equipment cost curves, typical duration, market analysis |
| 2 | Project Differences | Site-specific gap analysis, cost/schedule adjustments vs typical |
| 3 | Project Intake | Project data sheet with benchmark references |
| 4 | Requirements | Performance guarantees, quality standards, regulatory |
| 5 (G0) | Concept | 3 alternatives (Conservative/Balanced/Aggressive), benchmark comparison, selection |
| 6 (G1) | Pre-FEED | +/-30% design, AACE Class 4 cost estimate (with benchmark delta), long lead items |
| 7 (G2) | FEED (Basic Design) | WBS, procurement plan, Class 3 cost, CPM schedule, constructability, VE |
| 8 (G3) | Design Freeze | FEED frozen, 6-dimension verification (with benchmark comparison), RFQs issued |
| 9 | Consolidated Plan | Full project plan document combining all steps |

Each gate produces an Excel workbook (.xlsx) with structured sheets for cost, schedule, scope, quality, permits, risk, and benchmark comparisons.

**Usage:**
```
/project-plan 100,000 m3/d SWRO desalination plant, Arabian Gulf, EPC lump-sum
/project-plan 50 MW solar PV plant, Southern Italy, EPC lump-sum
/project-plan
```

## Skills (Auto-Triggered)

| Skill | Triggered By |
|-------|-------------|
| desalination-process-design | Desalination, SWRO, RO, MSF, MED, membrane, brine, intake, outfall |
| plant-cost-curves | Plant cost curve, typical CAPEX, cost per m3/d, cost per MW, benchmark cost, typical duration |
| equipment-cost-curves | Equipment cost, budget price, equipment delivery, lead time, pump cost, turbine cost |
| project-management | EVM, toll gate, FEED, design freeze, project phases |
| scheduling | CPM, critical path, Gantt, float, long lead items |
| cost-engineering | AACE, Class 1-5 estimates, Lang factors, contingency |
| wbs-procurement | WBS, procurement packages, RFQ, supply chain, AVL |
| quality-management | QA/QC, ITP, hold points, commissioning, ISO 9001 |
| constructability | Modularization, heavy lifts, site logistics, temporary works |
| value-engineering | VE, function analysis, FAST diagram, lifecycle cost |
| risk-management | Risk register, probability-impact matrix, Monte Carlo |
| permits-approvals | Construction permit, EIA, fire/security permits, temporary works |

## Key Features

- **Typical configuration benchmarking**: Establish industry baseline before project-specific analysis
- **Plant cost curves**: CAPEX per unit capacity for desalination, power, process, mining plants
- **Equipment cost curves**: Budget prices and delivery times for major equipment categories
- **Price market analysis**: Research recent similar projects to validate benchmarks
- **Delivery time market analysis**: Current equipment lead times vs typical curves
- **Project-specific gap analysis**: Quantified cost/schedule deltas from typical configuration
- **Procurement-driven scheduling**: Long lead items drive engineering priorities
- **Supply chain classification**: Global/Regional/Local with vendor pre-qualification triggers
- **AACE cost classification**: Class 5 through Class 2 with progressive refinement
- **Benchmark comparison at every gate**: Cost and schedule estimates always compared to typical
- **Design Freeze at G3**: FEED scope frozen to enable RFQ issuance
- **Risk embedded at every gate**: Not standalone -- integrated into each decision point
- **Permits tracking**: Environmental, construction, fire, security, temporary works
- **Excel workbooks**: Structured deliverables at each gate with benchmark sheets

## Requirements

- Python 3.12+ with `openpyxl` installed (for Excel workbook generation)
- Claude Code with plugin support enabled
