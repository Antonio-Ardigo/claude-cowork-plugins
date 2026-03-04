---
description: "Cost estimation methods for EPC and construction projects. Use when the user asks about cost estimation, parametric estimation, factored estimation, bottom-up estimation, unit rate estimation, Lang factors, Hand factors, capacity scaling, six-tenths rule, order-of-magnitude estimate, definitive estimate, three-point estimate, or how to prepare a cost estimate for a capital project."
---

# Cost Estimation Methods

Guide the user through selecting and applying the appropriate cost estimation method for their project phase and available information.

## Estimation Method Selection

Match the estimation method to the project phase and data availability:

| Project Phase | AACE Class | Method | Typical Accuracy |
|---------------|-----------|--------|-----------------|
| Screening / Concept | Class 5 | Analogous / Capacity-scaled | -30% to +50% |
| Feasibility | Class 4 | Parametric / Equipment-factored | -20% to +30% |
| Budget Authorization | Class 3 | Semi-detailed / Unit-rate | -15% to +20% |
| Control | Class 2 | Detailed / Bottom-up | -10% to +15% |
| Bid / Tender | Class 1 | Definitive / Quantity takeoff | -5% to +10% |

## Method 1: Analogous (Capacity-Scaled) Estimation

Scale from a known reference project using the power law:

```
Cost_new = Cost_ref × (Capacity_new / Capacity_ref)^n
```

Where `n` is the scaling exponent (typically 0.6–0.8, commonly 0.6 — the "six-tenths rule").

Apply adjustment factors after scaling:
1. **Time adjustment** — escalate from reference year to current year using CEPCI or appropriate index
2. **Location adjustment** — apply location factor relative to reference location (typically US Gulf Coast = 1.00)
3. **Complexity adjustment** — account for differences in process complexity, materials of construction, site conditions

## Method 2: Parametric (Factored) Estimation

### Lang Factor Method
Multiply total delivered equipment cost by a single factor:

| Plant Type | Lang Factor |
|-----------|-------------|
| Solids processing | 3.10 |
| Mixed solids-fluids | 3.63 |
| Fluids processing | 4.74 |

```
TIC = Equipment_FOB × Lang_Factor
```

### Hand Factor Method
Apply individual factors to each major equipment item based on equipment type. See `references/factor-tables.md` for complete Hand factor tables.

### Module Factor (Bare Module) Method
More granular than Lang — applies material and labor factors per equipment category. Accounts for:
- Direct field labor
- Piping and fittings
- Electrical
- Instrumentation
- Structural steel
- Insulation and paint
- Concrete and foundations

## Method 3: Bottom-Up (Detailed) Estimation

Build the estimate from individual work packages:

1. **Quantity takeoff** — extract quantities from drawings, specs, and data sheets
2. **Unit rate application** — apply labor rates (manhours/unit), material prices, equipment rates
3. **Productivity adjustment** — adjust for site conditions, climate, labor availability, work schedule
4. **Indirect costs** — add construction indirects, temporary facilities, construction equipment
5. **Home office costs** — engineering, procurement, project management
6. **Contingency** — based on estimate maturity and risk assessment

### Unit Rate Structure
```
Unit Cost = (Labor manhours × Blended rate) + Material cost + Equipment cost + Subcontract cost
```

Typical productivity adjustments:
- Hot climate (>40°C): 0.80–0.90 factor
- Cold climate (<-20°C): 0.70–0.85 factor
- Remote/isolated site: 0.75–0.90 factor
- Overtime (>50 hr/week sustained): 0.85–0.95 factor
- Congested work area: 0.85–0.95 factor

## Method 4: Three-Point Estimation

For items with significant uncertainty:

```
Expected = (Optimistic + 4 × Most_Likely + Pessimistic) / 6
Std_Dev = (Pessimistic - Optimistic) / 6
```

Use this to build probability distributions for Monte Carlo simulation when estimating contingency.

## Cost Breakdown Structure (CBS)

Organize estimates using a standard CBS:

**Direct Costs:**
- Process equipment (purchased)
- Bulk materials (piping, electrical, instrumentation, structural, civil)
- Direct construction labor
- Subcontracts

**Indirect Costs:**
- Construction indirects (supervision, QC, HSE, temporary facilities)
- Home office (engineering, procurement, PM, commissioning support)
- Freight and logistics
- Vendor representatives

**Other Costs:**
- Owner's costs (permits, land, insurance, legal)
- Contingency (project and process)
- Escalation allowance

## Contingency Determination

Determine contingency based on estimate class and risk profile:

| AACE Class | Typical Contingency Range |
|-----------|--------------------------|
| Class 5 | 30–50% |
| Class 4 | 20–35% |
| Class 3 | 10–20% |
| Class 2 | 5–15% |
| Class 1 | 3–10% |

Methods:
1. **Deterministic** — percentage of base estimate based on class and historical data
2. **Probabilistic (Monte Carlo)** — assign distributions to key cost items, simulate to determine P50/P80/P90 contingency

Always present contingency as a calculated allowance with a defined confidence level, not a padding factor.

## Worked Examples

See `references/worked-examples.md` for step-by-step examples of each estimation method applied to real project scenarios.
See `references/factor-tables.md` for complete factor tables for parametric estimation.
