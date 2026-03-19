---
name: design-assumptions
description: Design assumptions for civil and structural cost estimation. Use when the user asks about tank dimensions, concrete grades, rebar cover, load combinations, water depth, freeboard, structural configuration, wall thickness, slab thickness, column grid, expansion joints, design codes, structural design parameters, or geometry for any RC structure.
---

# Design Assumptions -- Civil/Structural Cost Estimation

## Purpose
Design assumptions define WHAT is being built -- geometry, structural grades, load cases, and design parameters. They are independent of WHERE (location/market) or HOW MUCH (cost). Changing design assumptions changes quantities but not unit rates.

## Key Parameters

### Geometry
- Structure type (rectangular, circular, prestressed)
- Cell arrangement (single, 2x2, 2x3, etc.)
- Cell dimensions (length x width x height)
- Wall thickness (external, internal)
- Slab thickness (base, roof)
- Column grid spacing
- Beam dimensions

### Structural Grades
- Concrete: C12/15 (blinding), C30/37 (slabs), C35/45 (water-retaining walls), C40/50 (columns)
- Rebar: B500B (fy=500 MPa) standard, B500C for seismic
- Cover: varies by exposure (50mm water face, 40mm earth, 35mm internal)

### Design Codes
- EN 1992-3: Liquid-retaining structures (Eurocode)
- ACI 350: Environmental engineering concrete (US)
- BS 8007: Design for retaining aqueous liquids (UK, withdrawn)
- SASO: Saudi Arabian Standards Organization (local supplements)

### Load Cases
- Hydrostatic (full tank, empty tank)
- Earth pressure (at-rest, active)
- Surcharge, wind, seismic, thermal

## Workflow
1. User specifies structure type and volume
2. Load matching reference file (rc-tank-rectangular, rc-tank-circular)
3. Extract geometry and calculate gross dimensions
4. Pass to quantity-takeoff skill for measurement
