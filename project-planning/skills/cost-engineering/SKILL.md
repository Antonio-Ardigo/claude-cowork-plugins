---
name: cost-engineering
description: Cost engineering for engineering and construction projects. Use when the user asks about AACE, cost estimate, cost engineering, contingency, accuracy range, Class 1 estimate, Class 2 estimate, Class 3 estimate, Class 4 estimate, Class 5 estimate, parametric estimate, factored estimate, equipment cost, bulk material cost, Lang factor, Hand factor, installation factor, cost breakdown, CBS, escalation, contingency determination, 18R-97.
---

# Cost Engineering -- AACE Classification & Estimation Methods

## AACE International Recommended Practice 18R-97

| Class | End Usage | Project Definition | Methodology | Accuracy (Low) | Accuracy (High) |
|-------|-----------|-------------------|-------------|----------------|-----------------|
| **Class 5** | Concept screening | 0% to 2% | Parametric, analogous, judgment | -20% to -50% | +30% to +100% |
| **Class 4** | Study / feasibility | 1% to 15% | Equipment-factored, parametric | -15% to -30% | +20% to +50% |
| **Class 3** | Budget / authorization | 10% to 40% | Semi-detailed unit costs | -10% to -20% | +10% to +30% |
| **Class 2** | Control / bid / tender | 30% to 70% | Detailed unit costs, vendor quotes | -5% to -15% | +5% to +20% |
| **Class 1** | Check estimate / definitive | 50% to 100% | Detailed takeoffs, firm quotes | -3% to -10% | +3% to +15% |

### Mapping to Toll Gates
| Gate | Phase | Typical AACE Class |
|------|-------|--------------------|
| G0 | Concept screening | Class 5 |
| G1 | Pre-FEED | Class 4 |
| G2 | FEED / Basic Design | Class 3 |
| G3 | Design Freeze | Class 2 |

## Estimation Methods

### Analogous Estimation
- Based on actual cost of similar completed projects
- Adjusted for capacity, location, time (escalation), complexity
- Best for: Class 5, early concept stage

### Parametric / Factored Estimation

**Capacity-Factored (Six-Tenths Rule):**
Cost_new = Cost_reference x (Capacity_new / Capacity_reference)^n
Where n is typically 0.6-0.8 (economies of scale).

**Equipment-Factored (Lang / Hand Factors):**

| Factor | Definition | Typical Range |
|--------|-----------|---------------|
| **Lang Factor** | Total installed cost / Equipment purchase cost | 3.0 - 5.0 |
| **Hand Factor** | Installation cost / Equipment purchase cost | 1.5 - 3.5 |

Lang factors by plant type:
- Solids processing: 3.0 - 3.5
- Mixed solids-fluids: 3.5 - 4.0
- Fluids processing: 4.0 - 5.0

**Equipment-Factored Breakdown:**

| Cost Component | Factor (% of Equipment Cost) |
|---------------|------------------------------|
| Equipment (FOB) | 100% (base) |
| Equipment installation | 40-50% |
| Piping | 30-60% |
| Instrumentation | 10-20% |
| Electrical | 10-15% |
| Civil / Structural | 15-30% |
| Insulation / Painting | 5-10% |
| Engineering | 15-25% |
| Construction indirects | 10-20% |
| Contingency | 15-30% |

### Bottom-Up Estimation
- Detailed quantity takeoff from drawings and specifications
- Unit rates applied to each quantity, vendor quotes for major equipment
- Best for: Class 2-1, detailed design stage

## Cost Breakdown Structure (CBS)

### Direct Costs
| Category | Description |
|----------|-----------|
| Major Equipment | Purchased equipment (FOB or delivered) |
| Bulk Materials | Piping, cable, instruments, steel, concrete |
| Civil / Structural | Foundations, buildings, structural steel erection |
| Piping | Pipe fabrication and installation |
| Electrical | Cable installation, termination, testing |
| Instrumentation & Control | Instrument installation, DCS/PLC, calibration |
| Insulation / Painting | Thermal insulation, fireproofing, coating |

### Indirect Costs
| Category | Description |
|----------|-----------|
| Engineering | FEED + detailed design, 3D modeling, drawings |
| Procurement Management | Sourcing, expediting, inspection, logistics |
| Construction Management | Site supervision, planning, QA/QC |
| Temporary Facilities | Camp, offices, temporary utilities, roads |
| Construction Equipment | Cranes, scaffolding, tools, consumables |

### Other Costs
| Category | Description |
|----------|-----------|
| Owner's Costs | Project management, legal, insurance, permits, land |
| Contingency | Provision for known unknowns |
| Management Reserve | Provision for unknown unknowns (not in baseline) |
| Escalation | Price increases over the project duration |

## Contingency Determination (AACE RP 40R-08)

### Deterministic Method
- Class 5: 30-50%, Class 4: 20-30%, Class 3: 10-20%, Class 2: 5-15%, Class 1: 3-10%

### Probabilistic Method (Recommended for G2+)
1. Identify risks with cost impact
2. Assign probability and cost impact ranges
3. Run Monte Carlo simulation
4. Contingency = P50 (or P80 for conservative) minus base estimate

## Cost Trending

| Gate | AACE Class | Estimate | Accuracy | Contingency |
|------|-----------|----------|----------|-------------|
| G1 | Class 4 | [EUR] | +/-30% | [EUR] ([%]) |
| G2 | Class 3 | [EUR] | +/-15-20% | [EUR] ([%]) |
| G3 | Class 2 | [EUR] | +/-10-15% | [EUR] ([%]) |

Significant cost growth between gates (>10% real increase) requires investigation.

## Escalation and Currency
- Apply escalation indices to future-year expenditures
- Multi-currency projects require forex risk assessment
- Fix exchange rates at estimate date, add forex contingency
