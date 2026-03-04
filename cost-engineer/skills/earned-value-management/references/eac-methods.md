# EAC Method Selection Guide

## Decision Framework

Use this decision tree to select the most appropriate EAC method:

### Question 1: Has the nature of the remaining work fundamentally changed?
- **Yes** → Use Method 4 (Management Bottom-Up ETC)
- **No** → Continue to Question 2

### Question 2: Are schedule delays driving cost overruns?
(e.g., extended site indirects, overtime, acceleration costs)
- **Yes** → Use Method 2 (CPI × SPI Composite)
- **No** → Continue to Question 3

### Question 3: Is the cost variance an isolated event or ongoing trend?
- **Isolated event** (e.g., one-time equipment re-purchase, single scope change absorbed) → Use Method 3 (Remaining at Budget)
- **Ongoing trend** → Use Method 1 (CPI-Based)

### Question 4: Is CPI stable over recent periods?
- **Stable (σ < 0.05)** → Method 1 gives reliable forecast
- **Unstable (σ > 0.05)** → Consider Method 5 (Weighted) or Method 4 (Bottom-Up)

## Method Comparison Table

| Method | Best For | Limitation | Reliability |
|--------|---------|-----------|-------------|
| CPI-based | Steady-state performance | Doesn't account for schedule | High (>20% complete) |
| CPI×SPI composite | Schedule-driven overruns | May double-count if schedule isn't causing cost | Medium-High |
| Remaining at budget | One-time variances | Optimistic if problems persist | Low |
| Management bottom-up | Changed conditions | Labor-intensive, subject to bias | Depends on quality |
| Weighted CPI/SPI | Custom situations | Requires judgment on weights | Medium |

## EAC Presentation Best Practice

Always present multiple EAC methods in parallel:

```
EAC Summary (Period 12):
                          EAC         VAC         VAC%
  Method 1 (CPI):        $112.5M     -$12.5M     -12.5%
  Method 2 (CPI×SPI):    $118.2M     -$18.2M     -18.2%
  Method 3 (Budget):     $105.3M     -$5.3M      -5.3%
  Method 4 (Mgmt ETC):   $110.0M     -$10.0M     -10.0%

  Recommended EAC:        $112.5M (Method 1 — CPI stable at 0.89 for 6 periods)
  BAC:                    $100.0M
```

### Range Presentation
For management reporting, present EAC as a range:
- **Optimistic:** Method 3 or best-case method
- **Most Likely:** Selected primary method
- **Pessimistic:** Method 2 or worst-case method

This provides decision-makers with the uncertainty band, not just a single number.

## EAC Validation Checks

After calculating EAC, validate:

1. **Reasonableness:** Does the EAC pass the "smell test"? Is it consistent with what the team is experiencing on the ground?
2. **Trend consistency:** Is the EAC direction consistent with CPI trend? (Rising CPI should yield improving EAC)
3. **Completeness:** Does EAC include all remaining scope, including approved but unpriced changes?
4. **Risk exposure:** Does EAC account for known risks that haven't materialized yet?
5. **Schedule alignment:** Is the EAC schedule assumption consistent with the current schedule forecast?

## When CPI Is Not Predictive

CPI may not predict future performance when:

- **Remaining work is fundamentally different** from completed work (e.g., engineering complete, construction starting)
- **Market conditions have changed** (e.g., labor market tightened, material prices spiked)
- **Corrective actions have been implemented** that genuinely change cost drivers
- **Scope changes have been authorized** that alter the cost profile

In these cases, Method 4 (Management Bottom-Up) is most appropriate, supplemented by Method 1 as a cross-check.

## Monthly EAC Update Process

1. Update PV, EV, AC for current period
2. Calculate CPI, SPI, and other metrics
3. Run all EAC methods
4. Select recommended EAC with justification
5. Compare to prior month EAC — explain any change >2%
6. Update EAC forecast in project controls system
7. Report to management with VAR for significant changes
