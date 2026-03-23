# Standard 15-Section BOQ Structure

| Sec | Description | Typical Items | Unit |
|-----|-------------|---------------|------|
| 1 | Preliminaries | Mob, site offices, insurance, HSE, demob | LS, mo |
| 2 | Earthworks | Clearing, excavation, disposal, compaction | m2, m3 |
| 3 | Blinding Concrete | C12/15, 75mm thick | m3 |
| 4 | Base Slab Concrete | C35/45, 400mm thick | m3 |
| 5 | Wall Concrete | C35/45 external, C30/37 internal | m3 |
| 6 | Roof Concrete | C30/37 slab + beams + columns | m3 |
| 7 | Reinforcement | Rebar by element | t |
| 8 | Formwork | By element type | m2 |
| 9 | Waterproofing | Membranes and coatings only (no screed) | m2 |
| 10 | Joints & Waterstops | PVC, sealant, hydrophilic strip | lm |
| 11 | Screeds & Finishes | Floor screed, roof screed, protection boards | m2 |
| 12 | Backfill | Selected fill, compaction | m3 |
| 13 | Mechanical & Piping | Pipes, valves, hatches, ladders | nr, lm, LS |
| 14 | Testing & Commissioning | Hydrostatic (incl water supply), leak repair, disinfection | LS |
| 15 | Sundries | Instrumentation, control panel, access manholes | nr, LS |

## Changes from v1.0 (14-section) to v2.0 (15-section)
- Section 9 split: waterproofing membranes/coatings remain in Sec 9; screeds moved to new Sec 11
- Old Section 11 (Backfill) renumbered to Sec 12
- Old Section 12 (M&E) renumbered to Sec 13
- Old Section 13 (Testing) renumbered to Sec 14, now explicitly includes water supply cost
- Old Section 14 (Sundries) renumbered to Sec 15, now explicitly includes access manholes

## WBS Mapping Update (Market WBS to Trade WBS)
| Market WBS | Maps to Trade WBS Sections |
|------------|---------------------------|
| M1 Civil/Structural | Sec 3 + 4 + 5 + 6 + 7 + 8 |
| M2 Earthworks | Sec 2 + 12 (backfill) |
| M3 Waterproofing | Sec 9 + 10 + 11 (WP + joints + screeds) |
| M4 Mechanical/Piping | Sec 13 |
| M5 Testing/Commissioning | Sec 14 + 15 |
| M6 Preliminaries/Indirects | Sec 1 |

## Row Format
- A: Item ref (e.g., 4.1)
- B: Description
- C: Unit
- D: Quantity
- E: Rate ($/unit)
- F: Amount ($) = D x E

## Summary
- Section totals --> SUBTOTAL (direct costs)
- + Contingency (% of SUBTOTAL) --> subtotal2
- + Escalation (% of subtotal2) --> subtotal3
- + OH&P (% of subtotal3) --> GRAND TOTAL
- **CRITICAL: Markups are COMPOUNDED SEQUENTIALLY, not applied as simple percentages of direct cost.**
