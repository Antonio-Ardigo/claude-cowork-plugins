---
name: risk-management
description: Risk management for engineering and construction projects. Use when the user asks about risk management, risk register, risk assessment, probability impact matrix, risk response, Monte Carlo, risk mitigation, HAZOP, risk identification, contingency allocation, risk scoring, risk appetite, risk-to-WBS mapping, schedule risk.
---

# Risk Management -- Engineering & Construction

## Risk Management Process

1. **Identify**: What could go wrong? What opportunities exist?
2. **Assess**: How likely? What impact?
3. **Respond**: What will we do about it?
4. **Monitor**: Track, reassess, identify new risks

Risk management is embedded at every toll gate, not a one-time exercise.

## Risk Identification Techniques

| Technique | Description | Best For |
|-----------|-----------|---------|
| Brainstorming | Team generates risks in open session | General identification |
| Checklists | Review against standard categories | Ensuring completeness |
| HAZOP | Systematic process deviation study | Process safety |
| SWIFT | Structured What-If Technique | Broader scope, quicker |
| Expert interviews | One-on-one with SMEs | Specialized technical risks |
| Lessons learned | Past project post-mortems | Recurring risks |

### Standard Risk Categories (EPC)
- Technical, Commercial, Schedule, Regulatory/Permit, HSE, Political/Country, Force Majeure, Financial

## Qualitative Risk Assessment

### Probability-Impact Matrix (5x5)

|  | Very Low (1) | Low (2) | Medium (3) | High (4) | Very High (5) |
|---|---|---|---|---|---|
| **Very High (5)** | 5 | 10 | 15 | 20 | 25 |
| **High (4)** | 4 | 8 | 12 | 16 | 20 |
| **Medium (3)** | 3 | 6 | 9 | 12 | 15 |
| **Low (2)** | 2 | 4 | 6 | 8 | 10 |
| **Very Low (1)** | 1 | 2 | 3 | 4 | 5 |

- Green (1-4): Low -- monitor
- Yellow (5-9): Medium -- mitigate
- Orange (10-15): High -- active management
- Red (16-25): Critical -- escalate, may be go/no-go factor

### Probability Scale

| Rating | Probability | Meaning |
|--------|-----------|---------|
| 1 | < 5% | Very unlikely |
| 2 | 5-20% | Unlikely |
| 3 | 20-50% | Possible |
| 4 | 50-80% | Likely |
| 5 | > 80% | Almost certain |

### Impact Scale

| Rating | Cost Impact | Schedule Impact |
|--------|-----------|----------------|
| 1 | < 1% of budget | < 1 week |
| 2 | 1-5% | 1-4 weeks |
| 3 | 5-10% | 1-3 months |
| 4 | 10-20% | 3-6 months |
| 5 | > 20% | > 6 months |

## Risk Response Strategies

| Strategy | Description | When to Use |
|----------|-----------|------------|
| **Avoid** | Eliminate risk by changing the plan | Unacceptable risk, can be designed out |
| **Mitigate** | Reduce probability or impact | Can be reduced to acceptable level |
| **Transfer** | Shift to another party (insurance, contract) | Better managed by another party |
| **Accept** | Acknowledge and prepare contingency | Cost of response exceeds benefit |

## Risk Register Structure

| Field | Description |
|-------|-----------|
| Risk ID | Unique identifier (R-001) |
| Description | Clear risk event statement |
| Category | Technical / Commercial / Schedule / Permit / HSE |
| Cause | Root cause or trigger |
| Consequence | What happens if materialized |
| Probability | 1-5 |
| Impact | 1-5 |
| Score | P x I |
| Owner | Responsible person |
| Response | Avoid / Mitigate / Transfer / Accept |
| Actions | Specific response actions |
| Status | Open / In Progress / Closed / Materialized |
| WBS Reference | Affected work packages |

## Contingency-Risk Linkage

1. List risks with cost impact
2. Estimate range (min, most likely, max)
3. Apply probability: Expected Value = P x Impact
4. Sum = risk-based contingency
5. Compare with AACE percentage-based contingency
6. Use higher, or run Monte Carlo

## Risk Reviews at Toll Gates

| Gate | Risk Focus |
|------|-----------|
| G0 | Project-level risks per alternative. Risk profile influences selection. |
| G1 | Initial register. Technical, commercial, schedule, permit risks. |
| G2 | Updated register. Quantify key risks. Link to WBS and schedule. Size contingency. |
| G3 | Final review. Residual risk. Contingency adequacy. Go/no-go input. |
