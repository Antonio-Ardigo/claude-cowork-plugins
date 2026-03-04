---
description: "Lifecycle cost analysis for EPC and construction capital projects. Use when the user asks about lifecycle cost, LCC, LCCA, total cost of ownership, TCO, CAPEX vs OPEX, NPV, net present value, IRR, internal rate of return, payback period, discounted cash flow, DCF, whole-life cost, operating cost estimation, maintenance cost, replacement cost, or comparing alternatives on a lifecycle cost basis."
---

# Lifecycle Cost Analysis

Guide the user through lifecycle cost analysis (LCCA) for capital projects — comparing alternatives on a total cost of ownership basis over the asset's economic life.

## LCCA Framework

Lifecycle cost includes all costs from initial investment through disposal:

```
LCC = CAPEX + PV(OPEX) + PV(Replacement) - PV(Salvage)
```

Where PV = present value of future costs discounted to a common base date.

## CAPEX Breakdown

Capital expenditure for EPC projects:

| Category | Components | Typical % of TIC |
|----------|-----------|-----------------|
| Process equipment | Vessels, pumps, compressors, heat exchangers | 15–30% |
| Bulk materials | Piping, electrical, instrumentation, structural, civil | 20–35% |
| Construction labor | Direct craft labor, productivity allowances | 15–25% |
| Construction indirects | Supervision, temp facilities, equipment, QC, HSE | 8–15% |
| Engineering | Process, mechanical, electrical, civil, instrumentation | 8–15% |
| Procurement | Procurement staff, expediting, inspection | 2–5% |
| Project management | PM team, controls, document management | 3–6% |
| Owner's costs | Permits, land, insurance, legal, financing | 5–10% |
| Contingency | Based on estimate class and risk assessment | 5–30% |

## OPEX Categories

Annual operating costs by category:

### Fixed OPEX (Independent of Production Rate)
- **Staff labor** — operations, maintenance, management, admin
- **Insurance** — typically 0.5–1.5% of replacement value per year
- **Property tax** — varies by jurisdiction
- **Fixed maintenance** — planned shutdowns, preventive maintenance contracts
- **Overheads** — corporate allocations, IT, legal, accounting

### Variable OPEX (Scales with Production)
- **Energy** — electricity, fuel, steam (often the largest OPEX item)
- **Raw materials / consumables** — chemicals, catalysts, membranes, filters
- **Maintenance (variable)** — wear parts, consumables, unplanned repairs
- **Waste disposal** — residuals, effluent treatment, solid waste
- **Logistics** — product transport, raw material delivery

### OPEX Benchmarks
See `references/opex-benchmarks.md` for typical OPEX rates by facility type (USD/unit output/year).

## Financial Metrics

### Net Present Value (NPV)

```
NPV = -CAPEX + Σ (Net_Cash_Flow_t / (1 + r)^t)  for t = 1 to n
```

Where:
- r = discount rate (real or nominal — be consistent)
- n = analysis period (years)
- Net_Cash_Flow_t = Revenue_t - OPEX_t - Replacement_t + Salvage_t

**Decision rule:** NPV > 0 means the project creates value. When comparing alternatives, choose the highest NPV.

### Internal Rate of Return (IRR)

The discount rate at which NPV = 0. Solve iteratively:

```
0 = -CAPEX + Σ (Net_Cash_Flow_t / (1 + IRR)^t)
```

**Decision rule:** IRR > hurdle rate means the project is acceptable. When comparing alternatives, be cautious — IRR can mislead with mutually exclusive projects of different sizes. Prefer NPV.

### Payback Period

**Simple payback:**
```
Payback = CAPEX / Annual_Net_Cash_Flow
```

**Discounted payback:** year at which cumulative discounted cash flow turns positive.

Payback is a risk indicator (shorter = less exposure), not a profitability measure. Do not use payback alone for investment decisions.

### Discount Rate Selection

| Context | Typical Real Discount Rate |
|---------|--------------------------|
| Public sector / government | 3–7% |
| Regulated utility | 5–8% |
| Private sector (low risk) | 8–12% |
| Private sector (high risk) | 12–20% |
| Oil & gas major | 10–15% |

Use **real** discount rate with **real** (constant-money) cash flows, or **nominal** rate with **nominal** (current-money) cash flows. Never mix.

See `references/financial-formulas.md` for detailed calculation procedures and examples.

## Sensitivity Analysis

Test how results change when key assumptions vary:

**Key variables to test:**
- Discount rate (±2–3 percentage points)
- Energy prices (±20–30%)
- CAPEX (±10–20%)
- OPEX (±10–15%)
- Production/demand volume (±10–20%)
- Asset life (±5 years)
- Escalation rate (±1–2%)

**Presentation:**
- Tornado diagram — rank variables by impact on NPV
- Spider plot — show NPV vs. each variable across its range
- Scenario analysis — optimistic, base, pessimistic cases
- Breakeven analysis — at what value of each variable does NPV = 0?

## Replacement & Renewal Scheduling

Account for major equipment replacements over the asset life:

| Equipment Type | Typical Life | Replacement Cost % of Original |
|---------------|-------------|-------------------------------|
| RO membranes | 5–7 years | 15–25% of SWRO CAPEX |
| Pumps (major) | 15–20 years | 3–8% of plant CAPEX |
| Heat exchangers | 15–25 years | 2–5% of plant CAPEX |
| Instrumentation / DCS | 10–15 years | 5–10% of plant CAPEX |
| Electrical equipment | 20–30 years | 3–7% of plant CAPEX |
| Civil / structural | 30–50 years | Maintenance, not replacement |

## Comparing Alternatives

When comparing alternatives on a lifecycle cost basis:

1. Define alternatives with equivalent output / service level
2. Define common analysis period and discount rate
3. Estimate CAPEX for each alternative
4. Estimate annual OPEX for each alternative
5. Include replacement costs at appropriate intervals
6. Calculate NPV of lifecycle cost for each alternative
7. Present results with sensitivity analysis
8. Document all assumptions

**Important:** If alternatives have different service lives, use either:
- Common multiple of service lives, or
- Equivalent Annual Cost (EAC) = NPV × (r / (1 - (1+r)^-n))
