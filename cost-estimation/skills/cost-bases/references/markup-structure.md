# Markup Structure

## Markups by Market
| Markup | International | Saudi/Gulf | Egypt | Rationale |
|--------|--------------|------------|-------|-----------|
| Contingency | 8% | 10% | 12% | Scope uncertainty, ground risk |
| Escalation | 3% | 5% | 8% | Material price trend, currency |
| OH&P | 12% | 15% | 10% | Contractor overhead + profit |
| **Total** | **~23%** | **~30%** | **~30%** | Cumulative on direct costs |

## Contingency by Project Phase
| Phase | Range | Typical | Accuracy |
|-------|-------|---------|----------|
| Concept/Feasibility | 20-30% | 25% | +/-50% |
| Pre-FEED | 15-20% | 18% | +/-30% |
| FEED | 10-15% | 12% | +/-20% |
| Detailed Design | 7-10% | 8% | +/-15% |
| Post-Tender | 3-5% | 4% | +/-10% |

## OH&P Components
| Component | International | Saudi |
|-----------|--------------|-------|
| Head office | 3-4% | 3-4% |
| Site overhead | 4-6% | 5-7% |
| Profit | 4-6% | 4-6% |
| Bonds/insurance | 1-2% | 1.5-2.5% |
| Saudization | - | 1% |
| Worker camp | - | 1-2% |

## Application Order -- COMPOUND SEQUENTIAL (not simple)

**CRITICAL: Each markup is applied to the running subtotal, NOT to the original direct cost.**

1. Direct costs (BOQ total) = SUBTOTAL
2. + Contingency (% of SUBTOTAL) --> subtotal2 = SUBTOTAL x (1 + contingency%)
3. + Escalation (% of subtotal2) --> subtotal3 = subtotal2 x (1 + escalation%)
4. + OH&P (% of subtotal3) --> GRAND TOTAL = subtotal3 x (1 + ohp%)
5. = GRAND TOTAL

### Compound Factor Calculation
Grand Total = Direct x (1 + contingency) x (1 + escalation) x (1 + OH&P)

### Worked Example -- Saudi Market
- Direct cost: $8,722,000
- Contingency 10%: $8,722,000 x 1.10 = $9,594,200
- Escalation 5%: $9,594,200 x 1.05 = $10,073,910
- OH&P 15%: $10,073,910 x 1.15 = **$11,584,997** (Grand Total)
- Compound factor: 1.10 x 1.05 x 1.15 = **1.3283**
- Effective total markup: 32.83% (not 30% simple sum)

### WRONG (Simple Percentages) -- DO NOT USE
- ~~Contingency: 10% of $8,722,000 = $872,200~~
- ~~Escalation: 5% of $8,722,000 = $436,100~~
- ~~OH&P: 15% of $8,722,000 = $1,308,300~~
- ~~Total markups: $2,616,600 (simple 30%)~~
- This underestimates markups by ~$245K on a $8.7M project
