# Location Factors — Detailed Reference

## Basis
All factors are relative to **US Gulf Coast (USGC) = 1.00**. Factors represent total installed cost adjustments including labor productivity, material availability, logistics, and regulatory environment.

## Factors by Region and Country

### North America
| Location | Factor | Notes |
|----------|--------|-------|
| US Gulf Coast (TX, LA) | 1.00 | Baseline |
| US Midwest | 1.00–1.10 | Higher labor rates, similar productivity |
| US West Coast | 1.15–1.30 | Highest US labor rates, stringent regulations |
| US Northeast | 1.10–1.25 | Union labor, higher living costs |
| US Rocky Mountain | 1.05–1.15 | Remote access, altitude considerations |
| Canada (Alberta) | 1.10–1.25 | Remote premium, climate, exchange rate |
| Canada (Ontario) | 1.05–1.15 | Moderate labor, urban infrastructure |
| Mexico | 0.75–0.95 | Lower labor, import duties, logistics |

### Europe
| Location | Factor | Notes |
|----------|--------|-------|
| UK | 1.15–1.30 | High labor rates, mature market |
| Netherlands | 1.20–1.35 | High labor, excellent infrastructure |
| Germany | 1.20–1.40 | High labor, strict regulations |
| Spain | 1.00–1.15 | Moderate labor, good infrastructure |
| Italy | 1.05–1.20 | Variable productivity, regional differences |
| Scandinavia | 1.30–1.50 | Highest European labor rates, climate |
| Eastern Europe (Poland, Romania) | 0.80–1.00 | Lower labor, developing infrastructure |
| Turkey | 0.80–0.95 | Competitive labor, regional logistics hub |

### Middle East
| Location | Factor | Notes |
|----------|--------|-------|
| Saudi Arabia (Eastern Province) | 0.85–1.00 | Established infrastructure, imported labor |
| Saudi Arabia (remote) | 0.95–1.15 | Desert premium, logistics |
| UAE (Abu Dhabi / Dubai) | 0.90–1.10 | Good infrastructure, imported labor |
| Qatar | 0.90–1.10 | Concentrated industrial zone |
| Oman | 0.90–1.10 | Moderate infrastructure |
| Kuwait | 0.90–1.05 | Established infrastructure |
| Bahrain | 0.90–1.05 | Small market, good logistics |
| Iraq | 1.10–1.40 | Security premium, limited infrastructure |

### Asia-Pacific
| Location | Factor | Notes |
|----------|--------|-------|
| Japan | 1.20–1.45 | High labor, high quality, seismic design |
| South Korea | 0.90–1.10 | Competitive EPC, high-quality fabrication |
| China (coastal) | 0.65–0.85 | Low labor, large domestic supply chain |
| China (interior) | 0.75–0.95 | Logistics premium over coastal |
| India | 0.60–0.80 | Lowest labor cost, variable productivity |
| Southeast Asia (Singapore) | 1.00–1.15 | High-cost city-state, imported labor |
| Southeast Asia (Malaysia, Thailand) | 0.75–0.90 | Moderate labor, developing infrastructure |
| Southeast Asia (Indonesia, Vietnam) | 0.70–0.85 | Low labor, limited local capability |
| Australia (metro) | 1.30–1.50 | Very high labor rates, strong unions |
| Australia (remote/mining) | 1.50–2.00 | Extreme remote premium, FIFO workforce |
| New Zealand | 1.10–1.25 | Moderate market, limited local capacity |

### Africa
| Location | Factor | Notes |
|----------|--------|-------|
| South Africa | 0.85–1.05 | Most developed African market |
| North Africa (Egypt, Algeria) | 0.80–1.00 | Moderate labor, variable infrastructure |
| West Africa (Nigeria) | 1.10–1.40 | Security premium, logistics challenges |
| East Africa (Kenya, Tanzania) | 1.00–1.30 | Limited infrastructure, import dependency |
| Sub-Saharan (remote) | 1.20–1.60 | Extreme logistics, limited everything |

### South America
| Location | Factor | Notes |
|----------|--------|-------|
| Brazil (São Paulo / coastal) | 0.90–1.10 | Largest LatAm market, complex regulation |
| Brazil (interior/Amazon) | 1.10–1.40 | Remote, logistics, environmental |
| Chile | 0.90–1.10 | Mining-oriented, developed market |
| Argentina | 0.80–1.00 | Volatile economy, good engineering base |
| Colombia | 0.80–1.00 | Developing market |
| Peru | 0.85–1.05 | Mining-oriented, altitude considerations |

## Factor Breakdown by Cost Component

Location factors vary by cost component. Typical breakdown for overall factor of X:

| Component | Factor Sensitivity | Driver |
|-----------|-------------------|--------|
| Imported equipment (FOB) | 0.95–1.05 | Freight, duties only |
| Locally sourced equipment | 0.50–1.50 | Local manufacturing capability |
| Bulk materials (imported) | 0.90–1.20 | Freight, duties, handling |
| Bulk materials (local) | 0.60–1.40 | Local availability and quality |
| Construction labor | 0.30–2.50 | Largest variation factor |
| Construction indirects | 0.50–2.00 | Camp, logistics, security |
| Engineering (home office) | 0.80–1.20 | Source country of engineering |
| Engineering (local) | 0.40–1.50 | Local engineering capability |

**Key insight:** Equipment costs are relatively stable globally (global supply chain). Labor and indirect costs drive most of the location variation.

## Applying Location Factors

### Method 1: Single Overall Factor
```
Cost_location = Cost_USGC × Location_Factor
```
Quick but imprecise. Acceptable for Class 5 estimates.

### Method 2: Component-Level Factors
Break the estimate into components and apply separate factors to each:
```
Cost_location = Σ (Component_USGC × Component_Factor)
```
More accurate. Required for Class 3 and better estimates.

### Method 3: First-Principles Adjustment
For Class 1–2 estimates, don't use location factors. Instead:
- Use local labor rates and productivity data
- Obtain local material and equipment quotes
- Estimate actual freight and logistics costs
- Include local regulatory and compliance costs
