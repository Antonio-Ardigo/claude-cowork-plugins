# Worked Examples — Cost Estimation Methods

## Example 1: Analogous (Capacity-Scaled) Estimation

**Scenario:** Estimate the cost of a 100,000 m³/day SWRO desalination plant. A similar 50,000 m³/day plant was built in 2020 for USD 150M (USGC basis).

**Step 1: Apply scaling exponent**
```
Cost_2020 = 150M × (100,000 / 50,000)^0.80
Cost_2020 = 150M × 2.00^0.80
Cost_2020 = 150M × 1.741
Cost_2020 = USD 261.2M (in 2020 dollars, USGC)
```

**Step 2: Escalate to current year (2025)**
Using CEPCI: 2020 index = 596, 2025 index = 830 (approximate)
```
Cost_2025 = 261.2M × (830 / 596)
Cost_2025 = 261.2M × 1.393
Cost_2025 = USD 363.8M (in 2025 dollars, USGC)
```

**Step 3: Apply location factor**
Project location: Middle East (factor = 0.95)
```
Cost_ME = 363.8M × 0.95
Cost_ME = USD 345.6M
```

**Step 4: Accuracy range (Class 5)**
```
Low:  345.6M × 0.70 = USD 242M
High: 345.6M × 1.50 = USD 518M
Point estimate: USD 346M
```

---

## Example 2: Equipment-Factored (Lang) Estimation

**Scenario:** Estimate TIC for a fluids processing plant. Total delivered equipment cost = USD 25M.

**Step 1: Apply Lang factor**
Fluids processing: Lang factor = 4.74
```
TIC = 25M × 4.74 = USD 118.5M
```

**Step 2: Verify with component breakdown (Chilton)**
```
Delivered equipment:           USD 25.0M (100%)
Equipment installation:         9.8M (39%)
Piping:                         7.8M (31%)
Instrumentation:                3.3M (13%)
Electrical:                     2.5M (10%)
Buildings:                      7.3M (29%)
Yard improvements:              2.5M (10%)
Service facilities:            13.8M (55%)
  Subtotal Direct:             72.0M
Engineering & supervision:      8.0M (32%)
Construction expense:           8.5M (34%)
  Subtotal Indirect:           16.5M
Contractor fee:                 4.3M (17%)
Contingency:                    8.5M (34%)
  Total Fixed Capital:        101.3M
```

Note: Chilton method gives USD 101M vs. Lang USD 119M — this range is typical. Use the average or the method with better calibration to your historical data.

---

## Example 3: Hand Factor Estimation

**Scenario:** Estimate installed cost for a process unit with the following major equipment:

| Equipment | Purchased Cost | Hand Factor | Installed Cost |
|-----------|---------------|-------------|---------------|
| 3 × Centrifugal pumps | USD 450K | 4.0 | USD 1,800K |
| 2 × S&T heat exchangers | USD 800K | 3.5 | USD 2,800K |
| 1 × Distillation column | USD 1,200K | 4.0 | USD 4,800K |
| 2 × Pressure vessels | USD 600K | 3.5 | USD 2,100K |
| 1 × Compressor + driver | USD 2,000K | 2.5 | USD 5,000K |
| **Total** | **USD 5,050K** | | **USD 16,500K** |

Effective overall factor: 16,500 / 5,050 = 3.27

Add:
- Engineering & procurement (12%): USD 1,980K
- Project management (5%): USD 825K
- Contingency (15%): USD 2,896K
- **Total Installed Cost: USD 22,201K**

---

## Example 4: Bottom-Up Unit Rate Estimation

**Scenario:** Estimate the cost of installing 5,000 linear meters of 6" carbon steel pipe in a process plant.

**Step 1: Unit rate buildup**
```
Piping installation (6" CS, Schedule 40):
  Labor:    3.5 MH/LM × USD 65/MH = USD 227.50/LM
  Material: pipe + fittings + supports = USD 85.00/LM
  Welding consumables:                = USD 12.00/LM
  Equipment (crane, welding):         = USD 18.00/LM
  Unit rate (direct):                 = USD 342.50/LM
```

**Step 2: Apply quantity**
```
Direct cost = 5,000 LM × USD 342.50/LM = USD 1,712,500
```

**Step 3: Apply productivity factor**
Hot climate, remote site: 0.85
```
Adjusted labor = USD 227.50 / 0.85 = USD 267.65/LM
Adjusted unit rate = USD 267.65 + 85.00 + 12.00 + 18.00 = USD 382.65/LM
Adjusted direct cost = 5,000 × USD 382.65 = USD 1,913,250
```

**Step 4: Add indirects and contingency**
```
Construction indirects (15%): USD 287K
Contingency (10%):           USD 220K
Total installed cost:        USD 2,420K
```

---

## Example 5: Three-Point Estimation for Contingency

**Scenario:** A Class 3 estimate totals USD 200M. Key risk items identified:

| Risk Item | Optimistic | Most Likely | Pessimistic | Expected | Std Dev |
|-----------|-----------|-------------|-------------|----------|---------|
| Equipment pricing | -5% | 0% | +15% | +1.7% | 3.3% |
| Labor productivity | -3% | +5% | +20% | +6.2% | 3.8% |
| Bulk material quantities | -2% | +3% | +12% | +3.7% | 2.3% |
| Subcontract pricing | -5% | +2% | +10% | +2.2% | 2.5% |
| Design development | 0% | +3% | +8% | +3.3% | 1.3% |

**Combined expected impact:** +17.1% of base estimate = USD 34.2M
**Combined std dev:** √(3.3² + 3.8² + 2.3² + 2.5² + 1.3²) = 6.1%

**Contingency at P80 (80% confidence):**
P80 = Expected + 0.84 × Std Dev = 17.1% + 0.84 × 6.1% = 22.2%
Contingency = USD 200M × 22.2% = **USD 44.4M**

**Contingency at P50 (50% confidence):**
P50 = Expected value = 17.1%
Contingency = USD 200M × 17.1% = **USD 34.2M**
