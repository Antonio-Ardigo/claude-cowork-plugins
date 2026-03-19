---
name: cost-bases
description: Unit cost rates and pricing for construction cost estimation. Use when the user asks about material prices, labor costs, equipment rental rates, concrete price, rebar price, formwork cost, unit rates, cost per cubic meter, markup percentages, contingency, escalation, OH&P, overhead and profit, market-specific pricing, or when comparing costs between different countries or regions.
---

# Cost Bases -- Unit Prices by Market

## Purpose
Cost bases contain unit prices for materials, labor, and equipment in specific markets. They define HOW MUCH things cost -- independent of productivity (speed) and design (geometry). Each market has its own rate file.

## Structure
- One reference file per market (market-international.md, market-saudi.md, etc.)
- Rates organized by: concrete, rebar, formwork, earthworks, waterproofing, labor, equipment
- All rates include currency, date of pricing, and source reference
- Markups (contingency, escalation, OH&P) vary by market and project phase

## Adding a New Market
1. Copy `market-international.md` to `market-newcountry.md`
2. Update all unit rates with local pricing
3. Update currency conversion
4. Adjust markups for local conditions
5. Add sources to data-sources skill

## Markup Application Order
1. Direct costs (BOQ total)
2. + Contingency (% of direct)
3. + Escalation (% of direct + contingency)
4. + OH&P (% of subtotal above)
5. = Total estimated cost
