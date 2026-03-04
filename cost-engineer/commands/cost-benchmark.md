---
name: cost-benchmark
description: Compare project costs against industry benchmarks. Normalize for location, time, and scope, then assess cost competitiveness.
allowed_tools:
  - Read
  - Glob
  - Grep
  - Bash
  - Task
---

# Cost Benchmark

Compare a project's costs against industry benchmarks. If the user provides a file, read it. Otherwise, ask for the key project parameters.

## Step 1: Gather Project Data

Collect or extract from file:
- **Project type** (e.g., SWRO desalination, CCGT power, gas processing, refinery unit)
- **Capacity** (with units — e.g., 100,000 m³/day, 400 MW, 500 MMSCFD)
- **Total Installed Cost (TIC)** or Estimated Total Cost
- **Location** (country/region)
- **Estimate base date** (year)
- **Currency**
- **Scope boundaries** (battery limits, utilities, owner's costs included?)
- **Estimate class** (if known)

## Step 2: Normalize to Common Basis

Normalize the project cost to US Gulf Coast, current-year USD:

1. **Currency conversion** — convert to USD at the estimate base-date exchange rate
2. **Location adjustment** — divide by the location factor to get USGC-equivalent cost
3. **Time adjustment** — escalate from base year to current year using the appropriate index (CEPCI for process, ENR CCI for civil)

```
Normalized_Cost = (TIC_local / Location_Factor) × (Index_current / Index_base)
```

Show the calculation steps explicitly.

## Step 3: Calculate Benchmark Metrics

Calculate the primary cost metric for comparison:
- **Cost per unit capacity** — e.g., USD/m³/day, USD/MW, USD/tonne/year, USD/bbl/day

```
Unit_Cost = Normalized_TIC / Capacity
```

## Step 4: Compare Against Benchmarks

Compare the normalized unit cost against:
- Industry benchmark ranges (from the cost-benchmarking skill knowledge)
- IPA quartile bands if available
- Historical project data if the user provides it

Present as a table:

| Metric | Project | Industry Q1 | Industry Median | Industry Q3 |
|--------|---------|-------------|-----------------|-------------|

## Step 5: Assess Competitiveness

Rate the project's cost position:
- **Below Q1**: Exceptional — flag for verification (may indicate scope gaps)
- **Q1–Q2**: Competitive
- **Q2–Q3**: Average — identify optimization areas
- **Above Q3**: Above market — investigate drivers

## Step 6: Identify Cost Drivers

If the project is above median, investigate which CBS categories are driving the premium:
- Compare each major category (equipment, bulk materials, labor, engineering, indirects) as % of TIC against benchmarks
- Identify the top 2–3 categories where the project deviates most
- Suggest specific areas to investigate for cost reduction

## Step 7: Deliver Report

Present a clear benchmarking report:

1. **Project Summary** — type, capacity, location, TIC
2. **Normalization Steps** — show each adjustment clearly
3. **Benchmark Comparison Table** — normalized cost vs. industry ranges
4. **Competitiveness Rating** — quartile position with explanation
5. **Cost Driver Analysis** — where the project deviates from norms
6. **Recommendations** — specific areas for investigation or value engineering

Include caveats about benchmark limitations (scope differences, market timing, data age).
