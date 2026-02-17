---
name: desalination-process-design
description: Desalination equipment process basic design for water treatment and desalination projects. Use when the user asks about desalination, reverse osmosis, RO, SWRO, multi-stage flash, MSF, multi-effect distillation, MED, membrane, permeate, brine, recovery rate, specific energy consumption, pretreatment, intake, outfall, remineralization, post-treatment, desalination plant, seawater, brackish water, TDS, salt rejection, flux, fouling, cleaning in place, CIP.
---

# Desalination Equipment -- Process Basic Design

## Technology Selection

### Major Desalination Technologies

| Technology | Abbreviation | Typical Capacity | SEC (kWh/m3) | Recovery Rate | Feed Water |
|-----------|-------------|-----------------|-------------|--------------|-----------|
| Seawater Reverse Osmosis | SWRO | 1,000 - 500,000 m3/d | 3.0 - 4.5 | 40% - 50% | Seawater (35,000 mg/L TDS) |
| Brackish Water RO | BWRO | 500 - 100,000 m3/d | 0.5 - 2.5 | 75% - 90% | Brackish (1,000-15,000 mg/L TDS) |
| Multi-Stage Flash | MSF | 5,000 - 75,000 m3/d | 10 - 16 (thermal + electric) | 20% - 35% | Seawater |
| Multi-Effect Distillation | MED | 5,000 - 50,000 m3/d | 6 - 12 (thermal + electric) | 25% - 40% | Seawater |
| MED with TVC | MED-TVC | 5,000 - 65,000 m3/d | 7 - 14 (thermal + electric) | 25% - 40% | Seawater |
| Electrodialysis Reversal | EDR | 100 - 20,000 m3/d | 1.0 - 3.0 | 80% - 95% | Brackish |

### Technology Selection Criteria

| Factor | SWRO | MSF | MED |
|--------|------|-----|-----|
| Capital cost (per m3/d) | Lower | Higher | Moderate |
| Energy cost | Electrical only | Thermal + electrical | Thermal + electrical |
| Waste heat available? | Not required | Major advantage | Major advantage |
| Feed water quality sensitivity | High (needs pretreatment) | Low (robust) | Low (robust) |
| Scaling tendency | Managed by pretreatment | Managed by top brine temp | Managed by top brine temp |
| Product water quality | 200 - 500 mg/L TDS | 5 - 25 mg/L TDS | 5 - 25 mg/L TDS |
| Typical plant life | 20 - 25 years | 25 - 30 years | 25 - 30 years |
| Membrane replacement | Every 5 - 7 years | N/A | N/A |

## SWRO Process Basic Design

### Process Flow -- Typical SWRO Plant

```
Seawater Intake --> Screening --> Pretreatment --> HP Pumps --> RO Membranes --> Permeate
                                                                    |
                                                              Energy Recovery
                                                                    |
                                                                  Brine --> Outfall

Permeate --> Post-treatment (Remineralization + Disinfection) --> Product Water Storage --> Distribution
```

### Intake Systems

| Type | Description | Typical Application |
|------|-----------|-------------------|
| Open intake (surface) | Seawater channel or pipeline from coast | Large plants > 50,000 m3/d |
| Beach well | Vertical or horizontal wells in coastal aquifer | Small-medium plants < 20,000 m3/d |
| Subsurface intake | Horizontal directional drilling (HDD) below seabed | Medium plants, environmentally sensitive |

### Pretreatment

**Conventional pretreatment:**
- Coagulation/flocculation (ferric chloride or aluminum sulfate)
- Multimedia gravity filters (sand + anthracite)
- Cartridge filters (5 micron nominal)
- Chemical dosing: antiscalant, sodium bisulfite (dechlorination), acid (pH adjustment)

**Membrane pretreatment (UF/MF):**
- Ultrafiltration or microfiltration membranes
- SDI < 3 consistently achievable
- Reduced chemical consumption
- Higher capital cost, lower operating cost
- Preferred for challenging feed water (high turbidity, algal blooms)

### RO System Design Parameters

| Parameter | Typical SWRO Value |
|-----------|--------------------|
| Feed pressure | 55 - 70 bar |
| Recovery rate | 40% - 50% (single pass) |
| Salt rejection | 99.5% - 99.8% |
| Permeate flux | 13 - 17 LMH (L/m2/h) |
| Membrane type | Spiral wound, 8" or 16" elements |
| Membrane material | Thin-film composite polyamide |
| Elements per vessel | 6 - 8 |
| Trains | Multiple parallel trains (N+1 redundancy) |
| Energy recovery device | Isobaric (PX) or turbocharger |
| SEC with ERD | 3.0 - 3.5 kWh/m3 |

### Two-Pass RO (When Required)

Required when product water boron or TDS must be very low:
- First pass: standard SWRO (35,000 --> ~300 mg/L TDS)
- Second pass: BWRO on first-pass permeate (~300 --> <10 mg/L TDS)
- Boron rejection enhanced by raising pH to 9.5 - 10 in second pass
- Increases SEC by 0.5 - 1.0 kWh/m3

### Post-Treatment

| Process | Purpose | Method |
|---------|---------|--------|
| Remineralization | Add hardness and alkalinity for corrosion control | Lime + CO2, or limestone contactor |
| pH adjustment | Raise pH to 7.5 - 8.5 | Sodium hydroxide or lime |
| Disinfection | Pathogen control | Chlorination (sodium hypochlorite) |
| Fluoridation | Dental health (if required by regulation) | Sodium fluoride |

### Brine Disposal

| Method | Description | Suitability |
|--------|-----------|------------|
| Ocean outfall | Diffuser pipe discharging to sea | Coastal plants, most common |
| Deep well injection | Injection into deep saline aquifer | Inland plants |
| Evaporation ponds | Solar evaporation | Arid climate, small plants |
| Zero liquid discharge (ZLD) | Crystallizer + evaporator | High-value water, strict regulation |

## Key Equipment List -- SWRO Plant

| Equipment | Quantity Basis | Key Sizing Parameters |
|-----------|--------------|---------------------|
| Intake pumps | N+1 per train | Flow rate, head, material (duplex SS) |
| Screening system | Coarse + fine screens | Bar spacing, flow capacity |
| UF/MF membranes (if used) | Per pretreatment capacity | Flux rate, backwash frequency |
| Media filters (if conventional) | Per filtration capacity | Loading rate (8-12 m/h), bed depth |
| Cartridge filter housings | Per RO train | 5 micron, flow capacity |
| High-pressure pumps | Per RO train | Flow, pressure (55-70 bar), efficiency |
| Energy recovery devices | Per RO train | Brine flow, pressure exchange efficiency |
| RO membrane elements | Per design capacity | Element count = capacity / (flux x element area) |
| RO pressure vessels | Per element count | 6-8 elements per vessel |
| Chemical dosing systems | Per chemical type | Antiscalant, acid, bisulfite, coagulant, NaOH, NaOCl |
| Remineralization system | Per product capacity | Limestone contactor or lime + CO2 |
| Product water tanks | Per storage requirement | Typically 4-8 hours of production capacity |
| Product water pumps | N+1 | Distribution flow rate and head |
| CIP system | 1 per plant (or per 2 trains) | CIP tank, pump, heater, chemical tanks |
| Brine outfall | 1 per plant | Diffuser design, dilution modeling |

## MSF Process Basic Design

### Process Stages

- Typical 18-24 stages (heat recovery + heat rejection)
- Top brine temperature: 90-110 degC
- Flash range: 2-4 degC per stage
- Gain output ratio (GOR): 8-12 kg distillate per kg steam
- Main consumables: antiscalant, acid, antifoam

### Key Equipment -- MSF

| Equipment | Description |
|-----------|-----------|
| Brine heater | Shell-and-tube, heated by LP steam |
| Flash chambers | Multiple stages, tube bundles for heat recovery |
| Ejectors / vacuum system | Maintain vacuum in flash chambers |
| Brine recirculation pumps | Large-capacity, corrosion-resistant |
| Distillate pumps | Product water extraction |
| Chemical dosing | Antiscalant, acid, antifoam, deaeration |

## MED Process Basic Design

### Process Arrangement

- Typical 8-16 effects
- Top brine temperature: 65-70 degC (LT-MED) or up to 130 degC (HT-MED)
- GOR: 8-16 kg distillate per kg steam
- Often combined with TVC (Thermo-Vapor Compressor) to boost GOR
- Lower scaling tendency than MSF due to lower top brine temperature

## Design Basis Document -- Desalination

A desalination process basic design package must include:

1. **Feed water analysis**: Full chemical analysis, seasonal variation, temperature range
2. **Product water specification**: TDS, boron, specific ions, WHO/local standards
3. **Plant capacity**: Nominal, peak, turn-down ratio
4. **Availability**: Target uptime (typically 90-95% annual)
5. **Design life**: Typically 20-30 years
6. **Energy source**: Grid power, cogeneration, renewable, waste heat
7. **Environmental constraints**: Brine discharge limits, intake impingement/entrainment
8. **Site conditions**: Seawater temperature (min/max), turbidity, algal bloom frequency
9. **Redundancy philosophy**: N+1 trains, standby equipment
10. **Expansion provision**: Future capacity increase allowance
