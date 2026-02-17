# Project Planning Plugin

Engineering and construction project planning with a toll gate (stage-gate) process from concept through Design Freeze.

## Command

### `/project-plan`

Generate a structured project plan following 4 toll gates:

| Gate | Phase | Key Output |
|------|-------|-----------|
| G0 | Concept | 3 alternatives (Conservative/Balanced/Aggressive), selection |
| G1 | Pre-FEED | +/-30% design, AACE Class 4 cost estimate, long lead items |
| G2 | FEED (Basic Design) | WBS, procurement plan, Class 3 cost, CPM schedule, constructability, VE |
| G3 | Design Freeze | FEED frozen, 6-dimension verification, RFQs issued |

Each gate produces an Excel workbook (.xlsx) with structured sheets for cost, schedule, scope, quality, permits, and risk.

**Usage:**
```
/project-plan 50 MW solar PV plant, Southern Italy, EPC lump-sum
/project-plan
```

## Skills (Auto-Triggered)

| Skill | Triggered By |
|-------|-------------|
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

- **Procurement-driven scheduling**: Long lead items drive engineering priorities
- **Supply chain classification**: Global/Regional/Local with vendor pre-qualification triggers
- **AACE cost classification**: Class 5 through Class 2 with progressive refinement
- **Design Freeze at G3**: FEED scope frozen to enable RFQ issuance
- **Risk embedded at every gate**: Not standalone -- integrated into each decision point
- **Permits tracking**: Environmental, construction, fire, security, temporary works
- **Excel workbooks**: Structured deliverables at each gate

## Requirements

- Python 3.12+ with `openpyxl` installed (for Excel workbook generation)
- Claude Code with plugin support enabled
