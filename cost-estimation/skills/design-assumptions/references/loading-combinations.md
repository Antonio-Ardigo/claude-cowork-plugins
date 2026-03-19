# Loading Combinations

## Load Cases
| Load | Symbol | Value | Code |
|------|--------|-------|------|
| Hydrostatic (full) | Hw | gamma_w x H (10 kN/m3 x 5.92m) | EN 1991-4 |
| Hydrostatic (empty) | - | Check flotation uplift | EN 1997-1 |
| Earth pressure (at rest) | Ko | 0.5 x gamma_soil x H_backfill | EN 1997-1 |
| Earth pressure (active) | Ka | 0.33 x gamma_soil x H_backfill | EN 1997-1 |
| Backfill unit weight | gamma_s | 18 kN/m3 | Typical |
| Surcharge on backfill | q | 10 kPa (traffic/construction) | EN 1991-1-1 |
| Roof live load | qk | 1.5 kN/m2 (maintenance) | EN 1991-1-1 |
| Wind pressure | w | Per EN 1991-1-4 (location-dependent) | EN 1991-1-4 |
| Seismic | a_g | Per EN 1998-4 (zone-dependent) | EN 1998-4 |
| Thermal gradient | dT | +/-20C on exposed walls | EN 1991-1-5 |

## ULS Load Combinations (EN 1990)
- **Persistent**: 1.35G + 1.50Q (dead + live)
- **Hydrostatic**: 1.20Hw + 1.35G + 1.50Q (favorable/unfavorable)
- **Seismic**: 1.0G + 1.0AEd + 0.3Q

## SLS Load Combinations
- **Characteristic**: 1.0G + 1.0Q
- **Quasi-permanent**: 1.0G + 0.3Q + 0.5T (for crack width check)
- **Crack width check**: Under quasi-permanent combination, max 0.2mm

## Critical Load Cases for Tanks
1. **Full tank + no backfill**: Maximum wall bending (outward)
2. **Empty tank + full backfill**: Maximum wall bending (inward) + flotation
3. **Adjacent cell full, this cell empty**: Differential pressure on internal wall
4. **Seismic + full tank**: Sloshing + inertia forces
5. **Thermal**: Summer heating of exposed walls above water line

## Importance Factor
- Water supply (essential service): gamma_I = 1.2
- Industrial (non-critical): gamma_I = 1.0
