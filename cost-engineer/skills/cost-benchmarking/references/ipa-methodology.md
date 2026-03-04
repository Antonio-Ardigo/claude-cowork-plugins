# IPA Benchmarking Methodology

## Overview

IPA (Independent Project Analysis) is a research-based consultancy that maintains the world's largest proprietary database of capital project performance. Their benchmarking methodology is the industry standard for evaluating project cost and schedule outcomes.

## Key Principles

### Peer Group Selection
IPA benchmarks are meaningful only when comparing to appropriate peers:

1. **Industry sector** — oil & gas, chemicals, mining, power, pharma, etc.
2. **Project type** — grassroots, expansion, revamp, infrastructure
3. **Capacity range** — projects within similar order-of-magnitude capacity
4. **Complexity** — measured by equipment count, number of process steps, integration requirements
5. **Region** — adjusted for location factors, but regional norms also matter
6. **Time period** — costs escalated to common year, but market cycle context preserved

### Normalization Process
IPA normalizes all projects to a common basis before comparison:

1. Escalate to common year using appropriate index
2. Adjust to US Gulf Coast basis using location factors
3. Standardize scope boundaries (battery limits, owner's costs, contingency)
4. Normalize capacity to common unit

### Performance Metrics

**Cost Performance:**
- **Cost Ratio** = Actual Cost / Predicted Cost (IPA model)
  - <1.0 = better than predicted
  - 1.0 = as predicted
  - >1.0 = worse than predicted

- **Cost Growth** = (Final Cost - Authorized Budget) / Authorized Budget
  - Industry average: 0–15% for well-defined projects
  - Poor performers: >25% cost growth

**Schedule Performance:**
- **Schedule Ratio** = Actual Duration / Predicted Duration
- **Schedule Slip** = (Actual - Planned) / Planned
  - Industry average: 10–20% slip
  - Best performers: <5% slip

**Predictability:**
- IPA measures how well the estimate predicted the outcome, not just absolute cost
- A low-cost project with 40% cost growth is worse than an average-cost project with 5% growth

## IPA Quartile System

| Quartile | Performance | Meaning |
|----------|------------|---------|
| Q1 (Best) | Top 25% | Excellent execution, well-defined scope, strong team |
| Q2 | 25–50th percentile | Above average, minor issues |
| Q3 | 50–75th percentile | Below average, significant improvement opportunities |
| Q4 (Worst) | Bottom 25% | Major problems — scope changes, poor planning, weak execution |

### What Drives Quartile Performance

IPA research consistently identifies these factors as separating Q1 from Q4:

**Front-End Loading (FEL):**
- Q1 projects have well-developed FEED before authorization
- FEL Index measures completeness of scope definition, design, and planning
- FEL-3 (best defined) projects average 6% cost growth; FEL-1 (poorly defined) average 35%

**Team & Organization:**
- Experienced project director assigned early
- Integrated owner-contractor team
- Stable team composition (low turnover)
- Clear decision-making authority

**Scope Stability:**
- Scope changes after authorization are the #1 driver of cost overruns
- Q1 projects have <5% scope change by value
- Q4 projects often have >20% scope change

## Applying IPA-Style Benchmarking Without IPA Data

If the organization does not subscribe to IPA benchmarking, apply the same principles using internal data:

### Step 1: Build Internal Database
Collect for each completed project:
- Project type, capacity, location
- Authorized budget, final cost
- Planned duration, actual duration
- Scope change log (value of changes as % of original scope)
- FEL maturity assessment at authorization

### Step 2: Normalize
- Escalate all costs to a common reference year
- Adjust all costs to a common reference location
- Standardize scope boundaries

### Step 3: Plot and Analyze
- Cost per unit capacity vs. capacity (log-log scatter plot)
- Cost growth distribution (histogram)
- Schedule slip distribution
- Cost vs. FEL maturity

### Step 4: Identify Regression
- Fit power law: Cost = a × Capacity^n
- Determine confidence intervals
- Mark quartile boundaries

### Step 5: Use for Prediction
- Plot new project against peer database
- Identify predicted cost range (Q1–Q4 band)
- Investigate any deviation drivers

## Cost Competitiveness Assessment

For a specific project, assess cost competitiveness:

```
Competitiveness Score = Normalized_Project_Cost / Industry_Benchmark_Median
```

| Score | Assessment | Action |
|-------|-----------|--------|
| <0.85 | Highly competitive | Verify data — may indicate scope gap |
| 0.85–0.95 | Competitive | Good position, maintain discipline |
| 0.95–1.05 | Average | Look for value engineering opportunities |
| 1.05–1.15 | Above average | Investigate cost drivers, benchmark specific areas |
| >1.15 | Uncompetitive | Major review needed — scope, productivity, or market issues |
