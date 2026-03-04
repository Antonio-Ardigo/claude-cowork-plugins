---
description: "Earned Value Management for EPC and construction projects. Use when the user asks about earned value, EVM, CPI, SPI, EAC, ETC, TCPI, cost performance index, schedule performance index, estimate at completion, S-curve, earned value analysis, project performance measurement, variance analysis, ANSI 748, EVM forecasting, cost variance, schedule variance, or project cost and schedule tracking."
---

# Earned Value Management (EVM)

Guide the user through EVM analysis — from basic metrics to WBS-level drill-down, forecasting, and trend analysis. Follows ANSI/EIA-748 principles adapted for EPC/construction.

## Core EVM Metrics

### Foundation Values

| Metric | Symbol | Definition |
|--------|--------|-----------|
| Budget at Completion | BAC | Total authorized budget |
| Planned Value | PV | Budgeted cost of work scheduled (BCWS) |
| Earned Value | EV | Budgeted cost of work performed (BCWP) |
| Actual Cost | AC | Actual cost of work performed (ACWP) |

### Variance Metrics

| Metric | Formula | Interpretation |
|--------|---------|---------------|
| Cost Variance | CV = EV - AC | Positive = under budget |
| Schedule Variance | SV = EV - PV | Positive = ahead of schedule |
| CV% | CV / EV × 100 | Cost efficiency as percentage |
| SV% | SV / PV × 100 | Schedule efficiency as percentage |

### Performance Indices

| Metric | Formula | Interpretation |
|--------|---------|---------------|
| Cost Performance Index | CPI = EV / AC | >1.0 = under budget |
| Schedule Performance Index | SPI = EV / PV | >1.0 = ahead of schedule |
| To-Complete Performance Index | TCPI = (BAC - EV) / (BAC - AC) | Required future CPI to finish on budget |

See `references/evm-formulas.md` for the complete formula reference.

## Estimate at Completion (EAC)

Multiple methods exist — select based on project circumstances:

### Method 1: CPI-Based (Most Common)
```
EAC = BAC / CPI
```
Assumes remaining work will be performed at the same cost efficiency as to date. Best when current cost performance is representative of future performance.

### Method 2: CPI × SPI Composite
```
EAC = AC + (BAC - EV) / (CPI × SPI)
```
Accounts for both cost and schedule performance. Use when schedule delays are driving cost overruns (e.g., extended indirect costs).

### Method 3: Management Estimate (Bottom-Up ETC)
```
EAC = AC + ETC_management
```
Management re-estimates the remaining work. Use when conditions have fundamentally changed and historical performance is no longer predictive.

### Method 4: Original Budget
```
EAC = AC + (BAC - EV)
```
Assumes remaining work will be performed at budgeted rates. Only valid if variance is a one-time event that won't recur.

See `references/eac-methods.md` for decision guidance on selecting the right EAC method.

## WBS-Level Analysis

Drill down from project level to WBS elements:

1. **Identify problem areas** — rank WBS elements by CV and SV magnitude
2. **Apply thresholds** — flag elements exceeding ±5% CV or ±10% SV
3. **Root cause analysis** — for each flagged element:
   - Is the variance due to rate (unit cost) or quantity (productivity)?
   - Is it a timing issue (will self-correct) or a real overrun?
   - What corrective actions are available?
4. **Variance Analysis Report (VAR)** — document each significant variance with:
   - Cause category (scope change, pricing, productivity, schedule, other)
   - Corrective action plan
   - Impact on EAC

## S-Curve Analysis

S-curves plot cumulative PV, EV, and AC over time:

- **PV curve** — the plan baseline (should follow characteristic S-shape)
- **EV curve** — actual progress in budget terms
- **AC curve** — actual spend

**Reading the S-curve:**
- EV below PV = behind schedule
- AC above EV = over budget
- Gap between AC and EV = cost variance at that point in time
- Convergence of EV toward BAC = project nearing completion

## Trend Analysis & Performance Trending

Track CPI and SPI over time to identify trends:

**Rules of thumb (validated by IPA and DoD research):**
- CPI rarely improves by more than 10% after a project is 20% complete
- If CPI < 0.90 at 20% complete, recovery to budget is statistically unlikely
- Declining CPI trend over 3+ periods signals systemic issues

**Trend indicators:**
- Plot rolling 3-period CPI and SPI
- Calculate CPI stability (standard deviation of last 6 periods)
- Compare current CPI to cumulative CPI — if current < cumulative, performance is worsening

See `references/trend-analysis.md` for trending techniques and early warning indicators.

## EVM for Construction

Construction-specific EVM considerations:

### Progress Measurement Methods
- **Milestones (weighted)** — assign value to defined milestones (best for procurement, commissioning)
- **Percent complete (subjective)** — supervisor estimates (acceptable for short-duration activities only)
- **Units completed** — physical count × unit value (best for repetitive work: pipe, cable, concrete)
- **Earned standards** — manhours earned per unit installed vs. budget (best for direct craft labor)
- **Level of effort** — time-based earning (only for support activities: QC, HSE, supervision)

### Typical WBS for EPC EVM
- Engineering (by discipline)
- Procurement (by package / PO)
- Construction (by area / system / discipline)
- Commissioning (by system)
- Project management / controls

### Reporting Frequency
- Weekly: craft labor productivity, short-interval schedule
- Monthly: full EVM report with variance analysis
- Quarterly: EAC update with management review
