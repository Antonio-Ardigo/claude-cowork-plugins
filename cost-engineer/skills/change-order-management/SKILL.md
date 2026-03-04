---
description: "Change order management and cost impact analysis for EPC and construction projects. Use when the user asks about change orders, variation orders, cost impact analysis, change order pricing, direct cost impact, indirect cost impact, markup, overhead, change management, MOC, management of change, contract variation, claim pricing, or evaluating the cost of a proposed change."
---

# Change Order Management

Guide the user through evaluating, pricing, and analyzing the cost impact of change orders (variations) on EPC and construction projects.

## Change Order Classification

Classify changes by source and impact:

### By Source
- **Owner-directed** — scope additions, design changes, acceleration
- **Design development** — engineering evolution within original scope (may or may not be a change depending on contract)
- **Site conditions** — differing site conditions, unforeseen subsurface
- **Force majeure** — weather, regulatory changes, labor disputes
- **Contractor-initiated** — value engineering proposals, means & methods changes

### By Impact Level
| Level | Cost Impact | Schedule Impact | Approval |
|-------|-----------|----------------|----------|
| Minor | <0.5% of contract value | No critical path impact | Project manager |
| Moderate | 0.5–2% of contract value | <2 weeks critical path | Project director |
| Major | >2% of contract value | >2 weeks critical path | Steering committee |

## Cost Impact Analysis

### Direct Costs

Break down the direct cost impact by category:

**Labor:**
```
Labor Cost = Manhours × Blended Labor Rate
```
- Estimate additional manhours by trade/discipline
- Apply appropriate labor rate (straight time, overtime, shift differential)
- Account for learning curve if new scope type
- Consider crew size and duration (mobilization/demobilization costs)

**Materials:**
```
Material Cost = Quantity × Unit Price + Freight + Waste Allowance
```
- Obtain vendor quotes or use recent purchase prices
- Include freight, handling, and storage costs
- Add waste/damage allowance (typically 3–10% depending on material)
- Account for lead time and expediting costs if schedule-critical

**Equipment (Construction Plant):**
```
Equipment Cost = (Hours × Hourly Rate) + Mobilization/Demobilization
```
- Crane time, heavy equipment, scaffolding, temporary power
- Include mob/demob if equipment not already on site

**Subcontract:**
- Obtain subcontractor quotations where applicable
- Verify scope alignment and markup structure
- Check against subcontract change clause and rates schedule

### Indirect Costs

Indirect costs arise when a change extends the project duration:

**Extended General Conditions:**
```
Extended Indirects = Daily Indirect Rate × Additional Days
```

Typical components of daily indirect rate:
- Site supervision and management staff
- Temporary facilities (offices, laydown, utilities)
- Construction equipment (cranes on standby, scaffolding)
- QC/QA staff and testing
- HSE staff and equipment
- Security
- Site services (catering, transport, medical)

**Home Office Extended Services:**
- Project management time
- Engineering support during extended construction
- Procurement and expediting

### Markup Structure

Apply markups per contract terms:

| Component | Typical Range | Basis |
|-----------|-------------|-------|
| Overhead | 8–15% | On direct costs |
| Profit | 5–10% | On direct costs + overhead |
| Bond premium | 0.5–2% | On total including profit |
| Insurance | 1–3% | On total including profit |
| Contingency | 0–5% | On direct costs (if contractually allowed) |

**Important:** Verify the contract-specific markup percentages. Do not assume standard rates — they vary significantly by contract.

### Compound Markup Calculation
```
Subtotal_1 = Direct Costs
Subtotal_2 = Subtotal_1 × (1 + Overhead%)
Subtotal_3 = Subtotal_2 × (1 + Profit%)
Subtotal_4 = Subtotal_3 × (1 + Bond%)
Total = Subtotal_4 × (1 + Insurance%)
```

Markups are applied sequentially, not stacked on the base.

## Change Order Pricing Format

Present change orders in a structured format:

```
1. Description of Change
2. Reason / Justification
3. Direct Cost Breakdown
   a. Labor (by trade)
   b. Materials (itemized)
   c. Equipment
   d. Subcontracts
4. Indirect Cost Impact
   a. Extended general conditions
   b. Extended home office
5. Markups
   a. Overhead
   b. Profit
   c. Bond / Insurance
6. Total Change Order Value
7. Schedule Impact (days on critical path)
8. Supporting Documentation
```

See `references/pricing-format.md` for a detailed pricing template.
See `references/markup-rates.md` for typical markup rates by contract type and region.

## Cumulative Impact Assessment

When multiple changes occur, assess cumulative effects:

- **Stacking** — multiple concurrent changes in the same area cause interference
- **Ripple effects** — one change triggers rework or redesign in adjacent systems
- **Productivity loss** — frequent changes disrupt work flow and reduce efficiency (studies show 10–30% productivity loss with high change frequency)
- **Acceleration costs** — if changes consume float, acceleration may be needed to maintain completion date

## Reasonableness Checks

After pricing, verify reasonableness:

1. **Cost per manhour** — is the blended rate consistent with contract rates?
2. **Manhour estimate** — compare to similar past work or industry norms
3. **Material pricing** — verify against recent purchase orders or vendor quotes
4. **Indirect cost ratio** — is the indirect-to-direct ratio reasonable for the scope?
5. **Markup percentages** — do they match the contract terms?
6. **Total cost per unit** — compare cost/m², cost/tonne, cost/meter against benchmarks
