# Financial Formulas for Lifecycle Cost Analysis

## Net Present Value (NPV)

### Basic Formula
```
NPV = Σ (CF_t / (1 + r)^t)  for t = 0 to n
```

Where:
- CF_t = net cash flow in period t (negative for costs, positive for revenue/savings)
- r = discount rate per period
- n = number of periods
- t = 0 is the present (initial investment, typically negative)

### Expanded Form
```
NPV = -C_0 + CF_1/(1+r)^1 + CF_2/(1+r)^2 + ... + CF_n/(1+r)^n
```

### For Lifecycle Cost Comparison (Costs Only)
When comparing alternatives with equal output, revenue cancels out:
```
NPV_cost = C_0 + Σ (OPEX_t + Replacement_t - Salvage_t) / (1+r)^t
```
Choose the alternative with the **lowest** NPV of costs.

### Present Value Factors

**Single payment present value factor:**
```
PVF = 1 / (1 + r)^n
```

**Uniform series present value factor (annuity):**
```
USPVF = (1 - (1+r)^-n) / r
```

Use USPVF when annual costs are constant:
```
PV_annual_cost = Annual_Cost × USPVF
```

## Internal Rate of Return (IRR)

The discount rate at which NPV = 0:
```
0 = Σ (CF_t / (1 + IRR)^t)  for t = 0 to n
```

Solve iteratively (no closed-form solution for n > 2).

### IRR Caveats
- Multiple IRRs possible if cash flow changes sign more than once
- IRR doesn't account for project scale — a 50% IRR on $1M is not comparable to 20% IRR on $100M
- For mutually exclusive projects of different sizes, **use NPV, not IRR**
- Modified IRR (MIRR) addresses reinvestment rate assumption issues

### Modified IRR (MIRR)
```
MIRR = (FV_positive / PV_negative)^(1/n) - 1
```
Where:
- FV_positive = future value of all positive cash flows reinvested at the finance rate
- PV_negative = present value of all negative cash flows discounted at the finance rate
- n = number of periods

## Payback Period

### Simple Payback
```
Payback = Initial_Investment / Annual_Net_Cash_Flow
```
Only valid when annual cash flows are uniform.

For non-uniform cash flows: find the year where cumulative cash flow turns positive.

### Discounted Payback
Find the year where cumulative **discounted** cash flow turns positive:
```
Year t where: Σ (CF_i / (1+r)^i) > 0  for i = 0 to t
```

Discounted payback is always longer than simple payback.

## Equivalent Annual Cost (EAC)

Converts a lump-sum NPV into an equivalent annual cost stream. Essential when comparing alternatives with different service lives.

```
EAC = NPV × r / (1 - (1+r)^-n)
```

Or equivalently:
```
EAC = NPV / USPVF
```

### Example
Alternative A: NPV = $50M over 20-year life, r = 8%
```
EAC_A = 50M × 0.08 / (1 - 1.08^-20) = 50M × 0.1019 = $5.09M/year
```

Alternative B: NPV = $35M over 15-year life, r = 8%
```
EAC_B = 35M × 0.08 / (1 - 1.08^-15) = 35M × 0.1168 = $4.09M/year
```

Choose B — lower equivalent annual cost despite higher NPV per year of life.

## Escalation and Inflation

### Real vs. Nominal
```
(1 + nominal_rate) = (1 + real_rate) × (1 + inflation_rate)
```

Approximately: `nominal ≈ real + inflation` (for small rates)

**Rules:**
- Use **real** discount rate with **constant-money** (real) cash flows
- Use **nominal** discount rate with **current-money** (nominal) cash flows
- **Never mix** real rates with nominal cash flows or vice versa

### Differential Escalation
Some cost components escalate faster or slower than general inflation:
```
Real_escalation_rate = Component_escalation - General_inflation
```

| Component | Typical Real Escalation |
|-----------|----------------------|
| Energy | +1% to +3% (historically above inflation) |
| Labor | 0% to +1% (roughly tracks inflation) |
| Technology/membranes | -2% to -5% (declining due to tech improvement) |
| Chemicals | 0% to +2% |
| Maintenance parts | 0% to +1% |

## Sensitivity Analysis Formulas

### Breakeven Analysis
Find the value of a variable where NPV = 0:
```
Set NPV(x) = 0, solve for x
```

### Tornado Diagram Data
For each variable, calculate:
```
NPV_low = NPV with variable at low bound (all others at base)
NPV_high = NPV with variable at high bound (all others at base)
Swing = |NPV_high - NPV_low|
```
Rank variables by swing — largest swing = most sensitive parameter.

### Scenario Analysis
| Scenario | Assumption |
|----------|-----------|
| Optimistic | All variables at favorable bound simultaneously |
| Base | All variables at most likely values |
| Pessimistic | All variables at unfavorable bound simultaneously |

**Note:** Optimistic/pessimistic scenarios are extreme — they represent the corners of the uncertainty space, not realistic single outcomes. Present them as bookends, not predictions.

## Discount Rate Quick Reference

### Weighted Average Cost of Capital (WACC)
```
WACC = (E/V × Re) + (D/V × Rd × (1-T))
```
Where:
- E = market value of equity
- D = market value of debt
- V = E + D (total value)
- Re = cost of equity
- Rd = cost of debt
- T = corporate tax rate

### Social Discount Rate (Public Projects)
Government and regulatory bodies often specify the discount rate:
- US OMB Circular A-94: 7% real (general) or 3% real (cost-effectiveness of public investment)
- UK HM Treasury Green Book: 3.5% real
- World Bank: 10–12% for developing countries

### Risk Premium Adjustment
```
Discount_rate = Risk-free rate + Project risk premium
```

| Project Risk | Premium Above Risk-Free |
|-------------|------------------------|
| Low (replacement/brownfield) | 2–4% |
| Medium (expansion) | 4–8% |
| High (grassroots, new technology) | 8–15% |
| Very high (frontier, unproven) | 15–25% |
