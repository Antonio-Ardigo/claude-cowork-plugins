# EVM Formula Reference

## Foundation Values

| Symbol | Name | Definition |
|--------|------|-----------|
| BAC | Budget at Completion | Total approved budget for the project or WBS element |
| PV | Planned Value | Cumulative budget for work scheduled to date (BCWS) |
| EV | Earned Value | Cumulative budget for work actually completed to date (BCWP) |
| AC | Actual Cost | Cumulative actual cost incurred to date (ACWP) |

## Variance Formulas

| Formula | Result | Favorable |
|---------|--------|-----------|
| CV = EV - AC | Cost Variance | Positive (under budget) |
| SV = EV - PV | Schedule Variance | Positive (ahead of schedule) |
| VAC = BAC - EAC | Variance at Completion | Positive (under budget at finish) |
| CV% = CV / EV × 100 | Cost Variance % | Positive |
| SV% = SV / PV × 100 | Schedule Variance % | Positive |

## Performance Indices

| Formula | Result | Favorable |
|---------|--------|-----------|
| CPI = EV / AC | Cost Performance Index | >1.0 (under budget) |
| SPI = EV / PV | Schedule Performance Index | >1.0 (ahead of schedule) |
| CSI = CPI × SPI | Cost-Schedule Index | >1.0 (overall health) |

## To-Complete Performance Index (TCPI)

TCPI answers: "What CPI must we achieve on remaining work to meet the target?"

**To meet original budget (BAC):**
```
TCPI_BAC = (BAC - EV) / (BAC - AC)
```

**To meet revised estimate (EAC):**
```
TCPI_EAC = (BAC - EV) / (EAC - AC)
```

| TCPI Value | Interpretation |
|-----------|---------------|
| <1.0 | Can relax somewhat — ahead of target |
| 1.0 | Must perform exactly at plan |
| 1.0–1.10 | Challenging but achievable |
| 1.10–1.20 | Very difficult — requires significant improvement |
| >1.20 | Practically unachievable — revise target |

## Estimate at Completion (EAC) Methods

### Method 1: CPI-Based
```
EAC = BAC / CPI
ETC = EAC - AC
```
**When to use:** Current cost efficiency is expected to continue.

### Method 2: CPI × SPI Composite
```
EAC = AC + (BAC - EV) / (CPI × SPI)
ETC = (BAC - EV) / (CPI × SPI)
```
**When to use:** Schedule problems are causing cost overruns (e.g., extended indirect costs, overtime premium).

### Method 3: Remaining Work at Budget Rate
```
EAC = AC + (BAC - EV)
ETC = BAC - EV
```
**When to use:** Variance was a one-time event; remaining work will proceed at budget rate.

### Method 4: Management Bottom-Up ETC
```
EAC = AC + ETC_management
```
**When to use:** Conditions have changed fundamentally; historical performance is not predictive. Requires detailed re-estimation of remaining work.

### Method 5: Weighted CPI/SPI (Custom)
```
EAC = AC + (BAC - EV) / (w1 × CPI + w2 × SPI)
where w1 + w2 = 1.0
```
**When to use:** Custom weighting of cost and schedule influence. Common weights: w1=0.8, w2=0.2 (cost-dominant) or w1=0.5, w2=0.5 (equal weight).

## Schedule Metrics (Time-Based)

Traditional SV becomes unreliable near project end (SV → 0 as EV → BAC regardless of actual schedule status).

**Earned Schedule (ES):**
```
ES = month where cumulative PV = current EV
SV(t) = ES - AT  (time-based schedule variance)
SPI(t) = ES / AT  (time-based schedule performance index)
```
Where AT = Actual Time (current reporting period number).

This gives a time-based schedule measure that remains valid through project completion.

## Threshold and Alert Levels

### ANSI/EIA-748 Suggested Thresholds

| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| CPI | 0.95–1.05 | 0.90–0.95 or 1.05–1.10 | <0.90 or >1.10 |
| SPI | 0.95–1.05 | 0.90–0.95 or 1.05–1.10 | <0.90 or >1.10 |
| CV% | -5% to +5% | -10% to -5% | < -10% |
| SV% | -5% to +5% | -10% to -5% | < -10% |
| TCPI | <1.05 | 1.05–1.15 | >1.15 |

### Action Triggers
- **Any Red metric:** Requires formal Variance Analysis Report (VAR) and corrective action plan
- **Sustained Yellow (3+ periods):** Escalate for management review
- **CPI < 0.90 at 20% complete:** Statistical evidence suggests budget recovery is unlikely
