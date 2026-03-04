# Factor Tables for Parametric Estimation

## Lang Factors (Total Installed Cost / Delivered Equipment Cost)

| Plant Type | Lang Factor | Source |
|-----------|-------------|--------|
| Solids processing | 3.10 | Lang (1947), updated |
| Mixed solids-fluids | 3.63 | Lang (1947), updated |
| Fluids processing | 4.74 | Lang (1947), updated |
| Battery limits addition (grass roots) | 4.0–5.0 | Industry average |
| Battery limits addition (brownfield) | 4.5–6.0 | Industry average |

## Hand Factors (by Equipment Type)

Hand factors are applied to individual equipment items and vary by equipment type:

| Equipment Type | Hand Factor | Notes |
|---------------|-------------|-------|
| Boilers | 1.8 | Includes foundations, piping, electrical, insulation |
| Compressors (centrifugal) | 2.5 | Includes driver, foundations, piping |
| Compressors (reciprocating) | 2.3 | Includes driver, foundations, piping |
| Cooling towers | 1.5 | Includes basin, piping, electrical |
| Distillation columns | 4.0 | Includes internals, piping, instrumentation |
| Dryers | 2.5 | Includes ducting, electrical |
| Evaporators | 2.5 | Includes piping, instrumentation |
| Filters | 2.0 | Includes piping, electrical |
| Furnaces / Heaters | 2.0 | Includes refractory, piping, instrumentation |
| Heat exchangers (S&T) | 3.5 | Includes piping, foundations, insulation |
| Heat exchangers (air-cooled) | 2.5 | Includes structural, electrical, piping |
| Mixers / agitators | 2.0 | Includes mounting, electrical |
| Pressure vessels | 3.5 | Includes internals, piping, foundations |
| Pumps (centrifugal) | 4.0 | Includes driver, piping, electrical, foundations |
| Pumps (positive displacement) | 3.5 | Includes driver, piping, electrical, foundations |
| Reactors | 4.0 | Includes internals, piping, instrumentation |
| Storage tanks (atmospheric) | 2.0 | Includes foundations, piping, instrumentation |
| Storage tanks (pressure) | 3.0 | Includes foundations, piping, instrumentation |
| Turbines (gas) | 2.0 | Includes intake/exhaust, foundations, electrical |
| Turbines (steam) | 2.0 | Includes condensing, foundations, electrical |

## Chilton Factors (Component-Level Breakdown)

Breakdown of installed cost as percentage of delivered equipment cost:

| Cost Component | Fluids Processing | Solids Processing |
|---------------|-------------------|-------------------|
| Delivered equipment | 100% | 100% |
| Equipment installation | 39% | 39% |
| Piping (installed) | 31% | 10% |
| Instrumentation (installed) | 13% | 9% |
| Electrical (installed) | 10% | 10% |
| Buildings | 29% | 18% |
| Yard improvements | 10% | 5% |
| Service facilities | 55% | 25% |
| **Subtotal Direct** | **287%** | **216%** |
| Engineering & supervision | 32% | 33% |
| Construction expense | 34% | 35% |
| **Subtotal Indirect** | **66%** | **68%** |
| Contractor fee | 17% | 14% |
| Contingency | 34% | 28% |
| **Total Fixed Capital** | **404%** | **326%** |

## Module (Bare Module) Factors

Guthrie-style bare module factors for equipment installed in a typical US Gulf Coast plant:

| Equipment Type | Base Bare Module Factor (Carbon Steel) | Material Factor (SS316) | Material Factor (Titanium) | Pressure Factor (>40 bar) |
|---------------|---------------------------------------|------------------------|---------------------------|---------------------------|
| Heat exchangers (S&T) | 3.17 | 1.7 | 3.0 | 1.3 |
| Pressure vessels | 3.05 | 1.7 | 3.5 | 1.5 |
| Pumps + motor | 3.30 | 1.6 | 2.8 | 1.2 |
| Compressors + driver | 2.15 | 1.3 | N/A | 1.1 |
| Trayed columns | 4.16 | 1.7 | 3.0 | 1.3 |
| Packed columns | 3.80 | 1.5 | 2.5 | 1.2 |
| Storage tanks | 1.80 | 1.5 | 2.5 | N/A |

**Bare Module Cost = Equipment Purchase Cost × Base BMF × Material Factor × Pressure Factor**

## Capacity Scaling Exponents

| Equipment / Facility Type | Scaling Exponent (n) | Typical Range |
|--------------------------|---------------------|---------------|
| General chemical plant | 0.60 | 0.55–0.70 |
| Refinery units | 0.65 | 0.60–0.70 |
| Power generation (thermal) | 0.75 | 0.70–0.80 |
| Gas processing | 0.65 | 0.60–0.70 |
| Desalination (SWRO) | 0.80 | 0.75–0.85 |
| Water treatment | 0.70 | 0.65–0.75 |
| Pumps | 0.35 | 0.30–0.40 |
| Compressors | 0.46 | 0.40–0.55 |
| Heat exchangers | 0.59 | 0.50–0.65 |
| Pressure vessels | 0.62 | 0.55–0.70 |
| Tanks (atmospheric) | 0.51 | 0.45–0.60 |
| Distillation columns | 0.62 | 0.55–0.70 |
| Reactors | 0.56 | 0.50–0.65 |

**Cost_new = Cost_ref × (Capacity_new / Capacity_ref)^n**

Note: Exponents are less reliable at extreme scale ratios (>5× or <0.2×). For scale ratios outside 0.5×–2.0×, consider step-change effects (parallel trains, different technology).
