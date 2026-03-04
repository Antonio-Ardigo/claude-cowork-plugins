# Escalation Indices — Reference Guide

## Chemical Engineering Plant Cost Index (CEPCI)

Published monthly in *Chemical Engineering* magazine. Most widely used index for process plant cost escalation.

### CEPCI Components and Weights
| Component | Weight |
|-----------|--------|
| Equipment | 61.8% |
| Construction labor | 21.8% |
| Buildings | 7.2% |
| Engineering | 9.2% |

### Historical CEPCI Values (Annual Averages)
| Year | CEPCI | Annual Change |
|------|-------|--------------|
| 2000 | 394.1 | — |
| 2005 | 468.2 | +3.5%/yr avg |
| 2010 | 550.8 | +3.3%/yr avg |
| 2015 | 556.8 | +0.2%/yr avg |
| 2018 | 603.1 | +2.7%/yr avg |
| 2019 | 607.5 | +0.7% |
| 2020 | 596.2 | -1.9% |
| 2021 | 708.0 | +18.8% |
| 2022 | 816.0 | +15.3% |
| 2023 | 800.8 | -1.9% |
| 2024 | 815.0 | +1.8% (est) |

**Note:** 2021–2022 saw unprecedented spikes due to supply chain disruption and inflation. Use caution when escalating through this period — consider whether the spike was temporary or structural for your specific cost components.

### Usage
```
Cost_target = Cost_base × (CEPCI_target / CEPCI_base)
```

Best for: Chemical plants, refineries, gas processing, petrochemical facilities.

## ENR Construction Cost Index (CCI)

Published weekly by *Engineering News-Record*. Based on 20-city average of construction labor and material costs.

### ENR CCI Components
- 200 hours common labor
- 25 cwt structural steel
- 1,128 board feet lumber
- 22.56 cwt cement

### Historical ENR CCI Values
| Year | ENR CCI | Annual Change |
|------|---------|--------------|
| 2000 | 6,221 | — |
| 2005 | 7,446 | +3.7%/yr avg |
| 2010 | 8,802 | +3.4%/yr avg |
| 2015 | 10,026 | +2.6%/yr avg |
| 2020 | 11,268 | +2.4%/yr avg |
| 2021 | 12,520 | +11.1% |
| 2022 | 13,455 | +7.5% |
| 2023 | 13,880 | +3.2% |
| 2024 | 14,250 | +2.7% (est) |

Best for: General construction, civil works, infrastructure, buildings.

## Nelson-Farrar Refinery Construction Cost Index

Published quarterly in *Oil & Gas Journal*. Specific to petroleum refinery construction.

### Nelson-Farrar Components
- Skilled labor (65% weight)
- Materials and equipment (35% weight)

### Historical Values
| Year | Nelson-Farrar | Annual Change |
|------|--------------|--------------|
| 2000 | 1,542 | — |
| 2010 | 2,141 | +3.3%/yr avg |
| 2015 | 2,310 | +1.5%/yr avg |
| 2020 | 2,410 | +0.9%/yr avg |
| 2023 | 2,820 | +5.3%/yr avg |

Best for: Oil refineries, petroleum facilities.

## IHS CERA Upstream Capital Costs Index (UCCI)

Tracks capital costs in upstream oil and gas globally.

Best for: Oil and gas exploration & production, upstream facilities, offshore platforms.

## RSMeans Construction Cost Data

Published annually by Gordian. Provides city-specific construction cost data for building construction.

Available as:
- City Cost Index (CCI) — relative cost by city (national average = 100)
- Historical Cost Index (HCI) — escalation over time
- Square foot cost data — by building type

Best for: Building construction, commercial/institutional projects.

## Selecting the Right Index

| Project Type | Primary Index | Secondary Index |
|-------------|--------------|-----------------|
| Chemical plant | CEPCI | ENR CCI |
| Oil refinery | Nelson-Farrar | CEPCI |
| Gas processing | CEPCI | Nelson-Farrar |
| Power plant | ENR CCI | CEPCI |
| Water / wastewater | ENR CCI | CEPCI |
| Mining | CEPCI | ENR CCI |
| Commercial building | RSMeans | ENR CCI |
| Civil infrastructure | ENR CCI | RSMeans |
| Upstream oil & gas | IHS CERA UCCI | Nelson-Farrar |

## Best Practices for Escalation

1. **Use the same index consistently** within a single estimate comparison
2. **Consider component-level escalation** for large estimates — labor, equipment, and materials may escalate at different rates
3. **Watch for structural breaks** — indices may not capture step-changes like tariffs, sanctions, or supply chain disruptions
4. **Local vs. national indices** — national indices may not reflect local market conditions; supplement with regional data where available
5. **Forward escalation** — for estimates beyond today, use consensus forecasts and clearly document the assumed escalation rate
6. **Mid-year convention** — when the exact month of expenditure is unknown, use mid-year index values
