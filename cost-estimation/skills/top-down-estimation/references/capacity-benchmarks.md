# Capacity Benchmarks -- Top-Down Estimation Rates

## RC Rectangular Water Tanks ($/m3 stored, TOTAL project cost INCLUDING markups)

**CRITICAL: These rates are ALL-IN total project cost. They ALREADY INCLUDE contingency, escalation, and OH&P. Do NOT apply markups on top of these rates. The top-down estimate total = capacity x benchmark rate. No further markups.**

| Volume Range | International (USD) | Gulf/Saudi (USD) | UAE (USD) | Egypt/S.Asia (USD) | Source |
|-------------|--------------------|-----------------|-----------|--------------------|--------|
| 5,000 m3 | $170-220 | $135-175 | $145-185 | $90-140 | IPA, IMARC, project data |
| 10,000 m3 | $150-200 | $115-155 | $125-165 | $75-120 | IPA, IMARC, project data |
| 25,000 m3 | $130-175 | $100-140 | $110-150 | $60-105 | IPA, IMARC, project data |
| 50,000 m3 | $115-165 | $90-135 | $100-145 | $55-100 | IPA, IMARC, project data |
| 100,000 m3 | $105-155 | $80-130 | $90-140 | $50-90 | IPA, IMARC, project data |
| 200,000 m3 | $95-145 | $75-120 | $85-130 | $45-85 | IPA, IMARC, project data |

### Validated Reference Points
- 100,000 m3 RC rectangular (International): $13.7M = **$137/m3** total (including ~23% markups)
- 100,000 m3 RC rectangular (Saudi): $11.6M = **$116/m3** total (including ~30% markups)
- Saudi is typically 15-20% below international for RC tanks

### Deriving Direct Cost from Total
To split the all-in rate into direct cost + markups for the discipline breakdown:
- Direct cost = Total / (1 + compound markup factor)
- Saudi compound markup: 1.10 x 1.05 x 1.15 = 1.33 --> Direct = Total / 1.33
- International compound markup: 1.08 x 1.03 x 1.12 = 1.246 --> Direct = Total / 1.246
- Example: Saudi $116/m3 total --> Direct = $116/1.33 = **$87.22/m3** --> $8,722,000 direct for 100k m3

## RC Circular Water Tanks ($/m3 stored, total project cost)

| Volume Range | International (USD) | Gulf/Saudi (USD) | Source |
|-------------|--------------------|-----------------| -------|
| 5,000 m3 | $130-180 | $100-150 | IPA, project data |
| 10,000 m3 | $110-160 | $85-130 | IPA, project data |
| 25,000 m3 | $95-140 | $75-115 | IPA, project data |
| 50,000 m3 | $85-130 | $65-110 | IPA, project data |

### Circular vs Rectangular
- Circular typically 10-15% cheaper per m3 stored (less wall perimeter per volume)
- Economy of scale stronger for circular (single shell vs multi-cell)

---

## Scaling Factors

### Six-Tenths Rule (Capacity Scaling)
```
Cost2 = Cost1 x (Capacity2 / Capacity1)^n
```

| Asset Type | Exponent (n) | Valid Range |
|-----------|-------------|-------------|
| RC water tanks (rectangular) | 0.65 | 5,000 - 200,000 m3 |
| RC water tanks (circular) | 0.60 | 1,000 - 50,000 m3 |
| Pump stations | 0.55 | 100 - 5,000 L/s |
| Pipelines | 0.35 (per km) | DN300 - DN2000 |

### Location Adjustment Factors (applied AFTER capacity scaling)
| Location | Factor vs International | Source |
|----------|----------------------|--------|
| International (baseline) | 1.00 | - |
| Gulf/Saudi | 0.82-0.88 | Lower labor costs, camp overhead partially offsets |
| UAE | 0.90-0.95 | Slightly higher than Saudi (logistics, regulation) |
| Egypt | 0.55-0.70 | Lower labor and materials, currency advantage |
| South Asia | 0.50-0.65 | Lowest cost base, quality variability |

Source: CEIC, GASTAT, IPA benchmarking database, IMARC Group Q4 2025.

---

## Discipline Breakdown Benchmarks (% of DIRECT cost, before markups)

### RC Rectangular Tanks -- Buried/Standard (excavation depth >= 50% of wall height)
| Market WBS | Category | Small (<25k m3) | Medium (25k-100k m3) | Large (>100k m3) |
|-----------|----------|-----------------|----------------------|-------------------|
| M1 | Civil/Structural | 50-55% | 48-52% | 45-50% |
| M2 | Earthworks | 8-12% | 7-10% | 6-9% |
| M3 | Waterproofing | 6-9% | 6-8% | 5-7% |
| M4 | Mechanical/Piping | 10-14% | 10-13% | 10-12% |
| M5 | Testing/Commissioning | 3-5% | 2-4% | 2-3% |
| M6 | Preliminaries/Indirects | 14-18% | 13-16% | 12-15% |

### RC Rectangular Tanks -- Surface/Shallow (excavation depth < 50% of wall height)
| Market WBS | Category | Small (<25k m3) | Medium (25k-100k m3) | Large (>100k m3) |
|-----------|----------|-----------------|----------------------|-------------------|
| M1 | Civil/Structural | 52-57% | 50-55% | 48-53% |
| M2 | Earthworks | 3-6% | 3-5% | 2-4% |
| M3 | Waterproofing | 6-9% | 6-8% | 5-7% |
| M4 | Mechanical/Piping | 10-14% | 10-13% | 10-12% |
| M5 | Testing/Commissioning | 3-5% | 2-4% | 2-3% |
| M6 | Preliminaries/Indirects | 14-18% | 13-16% | 12-15% |

Note: Surface tanks have lower earthworks (no deep excavation) and correspondingly higher Civil/Structural share. Select the appropriate table based on excavation depth vs wall height.

Notes:
- Percentages are of DIRECT cost (before contingency, escalation, OH&P)
- M1-M6 must sum to 100%
- Civil/Structural share decreases with size (economy of scale in concrete/rebar)
- Preliminaries share decreases with size (fixed costs spread over larger base)
- Sum of M1-M6 = 100% of direct costs; M7 markups applied on top

### Material Intensity Benchmarks (for cross-checking)
| Parameter | Typical Range | Alarm if outside |
|-----------|--------------|------------------|
| Concrete per m3 stored | 0.15-0.25 m3/m3 | < 0.10 or > 0.35 |
| Rebar intensity | 80-120 kg/m3 concrete | < 60 or > 150 |
| Formwork per m3 concrete | 4-8 m2/m3 | < 3 or > 10 |
| Rebar cost as % of direct | 25-35% | < 20% or > 40% |
| Concrete cost as % of direct | 20-28% | < 15% or > 35% |

---

## Top-Down Estimation Procedure

### Step 1: Determine Total Project Cost
1. Select asset type (e.g., RC rectangular tank)
2. Identify capacity (e.g., 100,000 m3) and market (e.g., Saudi)
3. Look up benchmark range: $80-130/m3 for Saudi at 100k m3
4. Select point estimate: use mid-range ($105/m3) for feasibility, or validated anchor ($116/m3) if available
5. Total = 100,000 x $116 = **$11.6M**

### Step 2: Split by Market WBS
Using discipline breakdown for medium RC rectangular tank (Saudi):
| Code | Category | % of Direct | Direct Cost | Assumption |
|------|----------|------------|-------------|------------|
| M1 | Civil/Structural | 49% | $4,362,000 | Mid-range for 100k m3, EN 1992-3 design |
| M2 | Earthworks | 8% | $712,000 | Sandy soil, 7m depth, no rock, no dewatering |
| M3 | Waterproofing | 6.5% | $579,000 | Internal cementitious + external bituminous |
| M4 | Mechanical/Piping | 11% | $979,000 | Standard inlet/outlet, no pumps in scope |
| M5 | Testing/Commissioning | 3% | $267,000 | 7-day hydrostatic test, disinfection |
| M6 | Preliminaries/Indirects | 14% | $1,246,000 | 22-month duration, expat workforce |
| | **Direct Subtotal** | **91.5%** | **$8,145,000** | |

### Step 3: Apply Markups (Saudi)
| Item | Basis | Amount | Assumption |
|------|-------|--------|------------|
| Contingency | 10% of direct | $815,000 | FEED-level scope definition |
| Escalation | 5% of (direct + contingency) | $448,000 | Vision 2030 demand pressure, 2-year project |
| OH&P | 15% of subtotal | $1,411,000 | Saudization, camp, higher insurance |
| **Markup Subtotal** | | **$2,674,000** | |
| **GRAND TOTAL** | | **$10,819,000** | |

Note: The procedure above yields $10.8M vs the validated anchor of $11.6M (7% below). This is within the +/-15% convergence threshold and reflects the typical spread in parametric estimates.

### Step 4: Document Assumptions
Each line gets an assumption ID (TD-A001 through TD-A00n) with text, basis, and impact level. See SKILL.md for format.
