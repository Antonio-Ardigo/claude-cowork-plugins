---
name: evm-report
description: Calculate EVM metrics from project actuals data. Generate CPI, SPI, EAC forecasts, WBS-level analysis, and performance trend assessment.
allowed_tools:
  - Read
  - Glob
  - Grep
  - Bash
  - Task
---

# EVM Report

Generate an Earned Value Management report from project actuals data. If the user provides a file, read it. Otherwise, ask for the key data.

## Step 1: Gather Data

Collect or extract from file:

**Project-level (minimum required):**
- BAC (Budget at Completion)
- PV (Planned Value to date)
- EV (Earned Value to date)
- AC (Actual Cost to date)
- Reporting period (month/date)
- Percent complete (physical)

**WBS-level (if available):**
- PV, EV, AC per WBS element
- BAC per WBS element

**Historical data (if available for trending):**
- CPI and SPI for previous periods
- Or PV, EV, AC for previous periods

## Step 2: Calculate Core Metrics

Calculate and present:

| Metric | Formula | Value | Status |
|--------|---------|-------|--------|
| Cost Variance (CV) | EV - AC | | Green/Yellow/Red |
| Schedule Variance (SV) | EV - PV | | Green/Yellow/Red |
| CV% | CV/EV × 100 | | |
| SV% | SV/PV × 100 | | |
| CPI | EV / AC | | Green/Yellow/Red |
| SPI | EV / PV | | Green/Yellow/Red |
| TCPI (to BAC) | (BAC-EV)/(BAC-AC) | | |

Use these thresholds:
- Green: 0.95–1.05
- Yellow: 0.90–0.95 or 1.05–1.10
- Red: <0.90 or >1.10

## Step 3: Calculate EAC (Multiple Methods)

Present all applicable EAC methods:

| Method | Formula | EAC | VAC | VAC% |
|--------|---------|-----|-----|------|
| CPI-based | BAC / CPI | | | |
| CPI×SPI composite | AC + (BAC-EV)/(CPI×SPI) | | | |
| Remaining at budget | AC + (BAC-EV) | | | |

Select and recommend the most appropriate method based on project conditions. Explain why.

Calculate ETC (Estimate to Complete) for the recommended method:
```
ETC = EAC - AC
```

## Step 4: WBS-Level Analysis (if data available)

For each WBS element, calculate CPI and SPI. Rank by variance magnitude.

Flag elements exceeding thresholds:
- CV% > ±5%
- SV% > ±10%

For each flagged element, note:
- The magnitude of the variance
- Whether it's a rate issue (unit cost) or quantity issue (productivity)
- Its contribution to overall project variance

Present as a sorted table, worst performers first.

## Step 5: Trend Analysis (if historical data available)

If multiple periods of data are available:
- Plot/tabulate CPI trend over time
- Calculate rolling 3-period CPI
- Identify direction: improving, stable, or declining
- Apply the 20% rule: if project is >20% complete and CPI < 0.90, flag that budget recovery is statistically unlikely

Assess:
- Is current CPI above or below cumulative CPI? (worsening or improving)
- Is CPI stable (σ < 0.05) or volatile?
- Is there a sustained trend (3+ periods in one direction)?

## Step 6: S-Curve Summary

If sufficient data exists, present a tabular S-curve showing PV, EV, and AC by period:

| Period | PV | EV | AC | CPI | SPI |
|--------|----|----|-----|-----|-----|

Describe the visual pattern: Is EV tracking PV? Is AC running above EV? When did divergence begin?

## Step 7: Deliver Report

Present the complete EVM report:

1. **Executive Summary** — one-paragraph health assessment with headline CPI, SPI, and recommended EAC
2. **Core Metrics Table** — all calculated metrics with status indicators
3. **EAC Forecast** — all methods with recommended EAC and rationale
4. **WBS Performance** — flagged elements and their contribution to variance
5. **Trend Assessment** — direction and stability of CPI/SPI
6. **Risk Flags** — any early warning indicators triggered
7. **Recommended Actions** — specific corrective actions based on the analysis

Rate overall project health as: **On Track**, **Watch**, **At Risk**, or **Critical**.
