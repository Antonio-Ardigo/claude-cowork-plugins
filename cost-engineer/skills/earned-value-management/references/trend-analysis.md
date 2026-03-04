# EVM Trend Analysis & Early Warning Indicators

## CPI Trending

### Rolling Average CPI
Calculate rolling 3-period and 6-period CPI averages to smooth volatility:

```
CPI_rolling_3 = Average(CPI_current, CPI_prev1, CPI_prev2)
CPI_rolling_6 = Average(CPI_current ... CPI_prev5)
```

### CPI Stability
```
CPI_stability = Standard Deviation of CPI over last 6 periods
```

| Stability (σ) | Interpretation |
|---------------|---------------|
| <0.03 | Very stable — EAC forecast is reliable |
| 0.03–0.05 | Moderately stable — EAC has moderate uncertainty |
| 0.05–0.10 | Unstable — investigate cause, EAC has wide uncertainty |
| >0.10 | Highly volatile — CPI-based EAC is unreliable |

### CPI Direction Indicator
Compare current period CPI to cumulative CPI:
- **Current CPI > Cumulative CPI** → performance is improving
- **Current CPI < Cumulative CPI** → performance is worsening
- **Trend over 3+ periods in one direction** → systematic shift, not noise

## Research-Based Rules of Thumb

These findings are validated by IPA, DoD, and NASA project databases:

### The 20% Rule
"CPI rarely improves by more than 10% after a project is 20% complete."
- At 20% complete, cumulative CPI is a strong predictor of final CPI
- If CPI = 0.85 at 20%, expect final CPI of 0.85–0.93 (5–10% improvement at most)
- Recovery plans that assume >15% CPI improvement should be challenged

### The Stability Point
"CPI stabilizes between 20–30% complete and rarely changes significantly thereafter."
- Early CPI volatility (first 10–15%) is normal — small EV and AC amounts create noise
- After 30% complete, if CPI < 0.90, budget overrun is virtually certain
- Management actions after 50% complete have limited impact on final CPI

### The No-Return Threshold
"If cumulative CPI < 0.80 at any point after 20% complete, recovery to CPI = 1.0 is statistically impossible."
- This finding is consistent across thousands of projects in DoD databases
- At this point, focus on damage limitation and realistic re-baselining
- Continuing to report EAC = BAC when CPI < 0.80 is not credible

## Early Warning Indicators

### Leading Indicators (Predict future problems)
| Indicator | Warning Threshold | What It Signals |
|-----------|------------------|----------------|
| Engineering change volume | >2 changes/week increasing | Scope instability |
| RFI (Request for Information) rate | Rising trend | Design quality issues |
| Procurement PO placement vs. plan | >10% behind plan | Procurement delays ahead |
| Workforce mobilization vs. plan | <90% of planned | Construction delay ahead |
| Vendor expediting actions | Increasing | Equipment delivery risk |
| Permit status | Behind critical path | Regulatory delay risk |

### Lagging Indicators (Confirm existing problems)
| Indicator | Warning Threshold | What It Confirms |
|-----------|------------------|-----------------|
| CPI < 0.95 for 3+ periods | Sustained underperformance | Cost overrun trend |
| SPI < 0.95 for 3+ periods | Sustained delay | Schedule slip trend |
| TCPI > 1.10 | Increasingly difficult | Budget recovery unlikely |
| Change order backlog growing | >30 days processing time | Change management bottleneck |
| Rework rate > 5% | Quality system failing | Cost and schedule impact |

## Trend Charts to Produce Monthly

### Chart 1: CPI & SPI Time Series
- X-axis: Reporting period (month)
- Y-axis: Index value
- Lines: Cumulative CPI, cumulative SPI, current-period CPI, current-period SPI
- Bands: Green (0.95–1.05), Yellow (0.90–0.95), Red (<0.90)

### Chart 2: EAC Trend
- X-axis: Reporting period
- Y-axis: EAC value (USD)
- Lines: EAC Method 1, Method 2, Management EAC
- Reference line: BAC

### Chart 3: S-Curve
- X-axis: Time (months)
- Y-axis: Cumulative value (USD or %)
- Curves: PV (baseline), EV (progress), AC (spend)
- Forecast extension: EAC projection to completion

### Chart 4: TCPI Trend
- X-axis: Reporting period
- Y-axis: TCPI value
- Lines: TCPI to BAC, TCPI to EAC
- Threshold lines: 1.10 (challenging), 1.20 (practically impossible)

## Corrective Action Framework

When trends indicate problems:

### Cost Overrun (CPI < 0.95)
1. Identify which WBS elements are driving the variance
2. Determine root cause: rate variance (unit cost) vs. quantity variance (productivity)
3. For rate variance: renegotiate contracts, substitute materials, re-source
4. For quantity variance: improve supervision, adjust methods, increase crew quality
5. Document corrective actions and expected CPI improvement
6. Monitor weekly until CPI stabilizes above threshold

### Schedule Delay (SPI < 0.95)
1. Identify critical path activities that are slipping
2. Determine root cause: resource availability, productivity, prerequisite delays
3. Assess float consumption — is the delay on the critical path?
4. Options: add resources, resequence work, authorize overtime, fast-track
5. Evaluate cost of acceleration vs. cost of delay
6. Update schedule forecast and communicate

### Combined (CSI < 0.90)
1. This is a project in trouble — escalate to senior management
2. Conduct comprehensive review of scope, cost, and schedule
3. Consider re-baselining if scope has fundamentally changed
4. Assess whether the project remains viable
5. Implement recovery plan with weekly tracking
