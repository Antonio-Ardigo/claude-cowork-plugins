# Market WBS Structure and Convergence Mapping

## Market WBS -- Top-Down Cost Categories

The Market WBS organizes project cost by functional discipline. Each category has a benchmark basis (how cost is estimated) and a typical percentage range of total project cost.

| Code | Category | Benchmark Basis | Typical % of TOTAL project cost | Notes |
|------|----------|----------------|--------------------------------|-------|
| M1 | Civil/Structural | $/m3 concrete volume | 35-45% | Concrete + rebar + formwork |
| M2 | Earthworks | $/m3 excavated volume | 5-10% | Excavation + backfill + compaction |
| M3 | Waterproofing | $/m2 treated area | 5-8% | Membranes + coatings + joints + waterstops |
| M4 | Mechanical/Piping | % of civil cost | 8-12% | Pipes, valves, hatches, ladders, ventilation |
| M5 | Testing/Commissioning | LS or % of direct | 2-4% | Hydrostatic test, disinfection, handover |
| M6 | Preliminaries/Indirects | % of direct or $/month x duration | 10-15% | Staff, equipment, temp works, mob/demob |
| M7 | Contractor Markup | % compound on subtotal | 15-30% | Contingency + escalation + OH&P |

**Important -- % basis clarification:**
- M1-M6 percentages above are of TOTAL project cost (including markups). They sum to ~70-85%.
- M7 is the remaining ~15-30%.
- For the top-down estimation procedure in capacity-benchmarks.md, M1-M6 percentages are expressed as % of DIRECT cost (before markups), where they sum to 100%. The two sets of percentages are NOT the same -- see capacity-benchmarks.md "Discipline Breakdown Benchmarks" for the direct-cost basis.
- The indirect-cost-structure.md file expresses indirects as 19-37% of DIRECT cost (detailed buildup). This is LARGER than the 10-15% M6 shown here because this table uses % of TOTAL, not % of DIRECT. At ~25% markup, 14% of direct = ~10.5% of total -- consistent.

### Discipline Breakdown by Asset Type (% of TOTAL project cost including markups)

| Category | RC Rect Tank | RC Circular Tank | Pump Station | Pipeline |
|----------|-------------|-----------------|--------------|----------|
| M1 Civil/Structural | 38-42% | 35-40% | 30-35% | 10-15% |
| M2 Earthworks | 6-9% | 5-8% | 8-12% | 25-35% |
| M3 Waterproofing | 5-7% | 5-7% | 3-5% | 2-4% |
| M4 Mechanical/Piping | 8-10% | 8-10% | 20-25% | 35-45% |
| M5 Testing/Commissioning | 2-3% | 2-3% | 3-4% | 2-3% |
| M6 Preliminaries/Indirects | 10-14% | 10-14% | 10-14% | 8-12% |
| M7 Contractor Markup | 18-25% | 18-25% | 18-25% | 18-25% |

Source: Compiled from industry data, IPA benchmarks, AACE cost reference series. Date: Q4 2025.

---

## WBS Mapping -- Market WBS to Trade WBS

This mapping enables the convergence matrix. Each Market WBS category maps to one or more Trade WBS sections (the 14-section BOQ used by the bottom-up estimate).

| Market WBS | Code | Maps to Trade WBS Sections | Trade WBS Description |
|------------|------|---------------------------|----------------------|
| Civil/Structural | M1 | Sec 3 + 4 + 5 + 6 + 7 + 8 | Blinding + Base slab + Walls + Roof + Rebar + Formwork |
| Earthworks | M2 | Sec 2 + 11 | Earthworks + Backfill |
| Waterproofing | M3 | Sec 9 + 10 | Waterproofing + Joints & Waterstops |
| Mechanical/Piping | M4 | Sec 12 | M&E / Piping |
| Testing/Commissioning | M5 | Sec 13 + 14 | Testing & Commissioning + Sundries |
| Preliminaries/Indirects | M6 | Sec 1 | Preliminaries |
| Contractor Markup | M7 | Markup rows | Contingency + Escalation + OH&P |

### Mapping Notes
- M1 aggregates all structural concrete, reinforcement, and formwork regardless of element type
- M2 includes both cut (excavation) and fill (backfill) -- net earthworks
- M3 includes both internal (cementitious) and external (bituminous) waterproofing plus all joint treatments
- M7 maps to the compound markup rows below the BOQ subtotal, not a BOQ section

---

## Convergence Thresholds

After computing variance = (TD_amount - BU_amount) / BU_amount for each mapped category:

| Category | Acceptable Variance | Action if Exceeded |
|----------|--------------------|--------------------|
| **Total project cost** | +/- 15% | Mandatory investigation |
| M1 Civil/Structural | +/- 10% | Check unit rates and rebar intensity |
| M2 Earthworks | +/- 20% | Check excavation depth and soil assumptions |
| M3 Waterproofing | +/- 15% | Check area calculations and specification |
| M4 Mechanical/Piping | +/- 25% | Check scope completeness (M&E often underestimated) |
| M5 Testing/Commissioning | +/- 30% | Check test requirements and commissioning scope |
| M6 Preliminaries/Indirects | +/- 20% | Check duration and staffing level |
| M7 Contractor Markup | N/A (not in convergence matrix) | Checked separately: verify markup %s match company policy in markup-structure.md |

### Convergence Status Flags
- **CONVERGED**: Variance within threshold -- no action needed
- **INVESTIGATE**: Variance exceeds threshold -- review assumptions and rates
- **SCOPE GAP**: Category present in one estimate but zero/missing in the other

### Common Causes of Non-Convergence
1. **Scope mismatch**: Top-down includes items not yet detailed in bottom-up (or vice versa)
2. **Rate basis difference**: Benchmark rate includes items that bottom-up prices separately
3. **Quantity error**: Geometry or measurement rule produces unexpected quantities
4. **Market timing**: Benchmark from different date than current unit prices
5. **Design maturity**: Top-down assumes typical design; bottom-up may have non-standard features
