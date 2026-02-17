---
name: project-management
description: Project management fundamentals for engineering and construction. Use when the user asks about project management, EVM, earned value, project controls, stage gate, toll gate, project lifecycle, FEED, front-end engineering, project phases, FID, design maturity, design freeze, project execution plan, change control, baseline management.
---

# Project Management -- Engineering & Construction

## Project Lifecycle Phases

| Phase | Purpose | Key Deliverables | Design Maturity |
|-------|---------|-----------------|----------------|
| **Concept / Feasibility** | Determine if the project is viable | Feasibility study, alternatives analysis | 0-5% |
| **Pre-FEED (Conceptual)** | Define the selected concept | Preliminary design, Class 4 estimate | ~10% (3D model) |
| **FEED (Basic Design)** | Develop to investment decision quality | P&IDs, equipment specs, Class 3 estimate | ~30% (3D model) |
| **Detailed Design** | Produce construction-ready documents | IFC drawings, MTO, Class 2/1 estimate | 60-90% (3D model) |
| **Procurement** | Acquire equipment and materials | POs, vendor documents, expediting | -- |
| **Construction** | Build the facility | Installed systems, QC records | -- |
| **Commissioning & Startup** | Verify and hand over | Performance test results, PAC | 100% |

## Stage-Gate (Toll Gate) Process

### Gate Structure
- **Gate 0 (G0)**: Concept selection -- choose among alternatives, approve feasibility
- **Gate 1 (G1)**: Pre-FEED complete -- approve conceptual design, Class 4 estimate (+/-30%)
- **Gate 2 (G2)**: FEED complete -- approve basic design, Class 3 estimate (+/-15-20%)
- **Gate 3 (G3)**: Design Freeze -- freeze FEED scope, Class 2 estimate (+/-10-15%), authorize procurement and construction

### Gate Decisions
At each gate, a review committee evaluates deliverables and decides:
- **Go**: Proceed to next phase
- **No-Go**: Stop the project (kill decision)
- **Recycle**: Return to current phase for rework before re-submitting

### Gate Criteria
Each gate requires demonstration of readiness across dimensions:
- Cost estimate accuracy appropriate for the phase
- Schedule baseline established and achievable
- Scope defined to the required level
- Quality and codes compliance confirmed
- Risk identified and mitigated to acceptable levels
- Permits on track

## Design Maturity and 3D Model Percentage

| Model % | Meaning | Typical Phase |
|---------|---------|---------------|
| 10% | Major equipment placed, preliminary routing | Pre-FEED |
| 30% | Equipment, main pipe routing, structural steel, cable trays | FEED / Basic Design |
| 60% | All piping, supports, small-bore, clash-checked | Design Freeze |
| 90% | All details, isometrics extracted, MTO complete | Detailed Design |
| 100% | As-built, red-line markups incorporated | Construction complete |

## Design Freeze

Design Freeze (typically at G3) is the point at which the FEED scope is formally frozen:
- **Purpose**: Enable procurement to issue RFQs with confidence that specifications will not change
- **What is frozen**: Equipment specifications, P&IDs, layout, material specifications, design basis
- **What requires a change order after freeze**: Any modification to frozen deliverables must go through a formal Management of Change (MOC) process with cost/schedule impact assessment
- **Why it matters**: Without a freeze, procurement cannot commit to vendor contracts, and the project risks continuous scope creep

## Earned Value Management (EVM)

### Core Metrics
| Metric | Formula | Meaning |
|--------|---------|---------|
| **PV** (Planned Value) | Budget x planned % complete | What should have been done |
| **EV** (Earned Value) | Budget x actual % complete | What was actually accomplished |
| **AC** (Actual Cost) | Actual expenditure | What was actually spent |
| **SV** (Schedule Variance) | EV - PV | Ahead (+) or behind (-) schedule |
| **CV** (Cost Variance) | EV - AC | Under (+) or over (-) budget |
| **SPI** (Schedule Performance Index) | EV / PV | >1 = ahead, <1 = behind |
| **CPI** (Cost Performance Index) | EV / AC | >1 = under budget, <1 = over |
| **EAC** (Estimate at Completion) | BAC / CPI | Projected total cost |
| **TCPI** (To-Complete Performance Index) | (BAC - EV) / (BAC - AC) | Required efficiency to finish on budget |

### Interpretation
- SPI > 1.0 and CPI > 1.0: Project performing well
- SPI < 0.8 or CPI < 0.8: Significant concern, corrective action needed
- CPI rarely improves after 20% completion -- early trends are predictive

## Project Controls

### Baseline Management
- **Cost baseline**: Approved budget at gate approval (BAC)
- **Schedule baseline**: Approved CPM schedule at gate approval
- **Scope baseline**: Approved WBS and deliverables list

### Change Control
All changes to baselines must go through:
1. Change request submitted with justification
2. Impact assessment: cost, schedule, scope, quality, risk
3. Approval by authorized level (project manager, steering committee, client)
4. Baseline updated if approved
5. Change log maintained

### Progress Measurement Methods
- **Milestones**: Binary 0/100 (complete or not)
- **Percent complete**: Engineering judgment or physical measurement
- **Weighted milestones**: Key milestones weighted by effort
- **Units complete**: For repetitive work (e.g., meters of pipe welded)
- **Level of effort**: Time-based for support activities
