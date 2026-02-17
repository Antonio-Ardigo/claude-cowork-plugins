---
name: wbs-procurement
description: Work breakdown structure and procurement for engineering and construction. Use when the user asks about WBS, work breakdown structure, procurement strategy, procurement plan, procurement package, RFQ, request for quotation, sourcing, long lead, supply chain, vendor evaluation, scope of supply, pre-qualification, approved vendor list, AVL, vendor management, material requisition, equipment datasheet, purchase order, expediting.
---

# WBS & Procurement -- Engineering & Construction

## Work Breakdown Structure (WBS)

### Decomposition Principles

**100% Rule**: The WBS must capture 100% of the project scope. Nothing is left out, nothing is counted twice.

**Deliverable-Oriented**: Decompose by what is produced (deliverables), not by how work is done (activities).

**Mutual Exclusivity**: Each element appears in only one place in the WBS.

**Progressive Elaboration**: WBS detail increases as the project progresses:
- G0/G1: 2 levels (major systems)
- G2: 3 levels (work packages)
- G3+: 4-6 levels (detailed tasks)

### Standard EPC WBS (3 Levels)

```
1.0 Project Management
  1.1 Project Controls
  1.2 Document Management
  1.3 HSE Management
  1.4 Quality Management

2.0 Engineering
  2.1 Process Engineering
  2.2 Mechanical Engineering
  2.3 Civil / Structural Engineering
  2.4 Electrical Engineering
  2.5 Instrumentation & Control
  2.6 Piping Engineering

3.0 Procurement
  3.1 Major Equipment
  3.2 Bulk Materials
  3.3 Subcontracts

4.0 Construction
  4.1 Site Preparation & Earthworks
  4.2 Civil Works
  4.3 Structural Steel
  4.4 Mechanical Installation
  4.5 Piping Fabrication & Installation
  4.6 Electrical Installation
  4.7 Instrumentation Installation
  4.8 Insulation & Painting

5.0 Commissioning & Startup
  5.1 Pre-commissioning
  5.2 Commissioning
  5.3 Performance Testing
  5.4 Handover & Closeout

6.0 Temporary Works
  6.1 Construction Camp
  6.2 Temporary Utilities
  6.3 Temporary Roads & Laydown
```

### Work Package Definition
Each work package must include: WBS ID, description, deliverable, responsible party, procurement package reference, estimated cost, estimated duration, acceptance criteria.

## Supply Chain Classification

| Classification | Description | Examples | Typical Lead Time |
|---------------|-----------|---------|------------------|
| **Global** | Specialized OEMs, worldwide sourcing | Turbines, compressors, high-pressure pumps | 8-18 months |
| **Regional** | Multiple suppliers within region | Transformers, structural steel, piping | 3-10 months |
| **Local** | Site-proximity contractors/suppliers | Civil works, concrete, earthworks | 1-4 months |

## Procurement Strategy

### Sourcing Strategies

| Strategy | When to Use | Minimum Vendors |
|----------|-----------|----------------|
| **Competitive bid** | Standard equipment/materials, >3 qualified vendors | 3+ |
| **Single source** | Proprietary technology, sole supplier | 1 |
| **Frame agreement** | Repetitive purchases, bulk materials | 1-3 |
| **Pre-qualified list** | Critical, quality-sensitive, safety-critical | 3+ (pre-screened) |

### Vendor Pre-Qualification Trigger

Check the company Approved Vendor List (AVL) against the procurement strategy. If fewer than 3 qualified vendors exist for any package at the required supply chain level, **pre-qualification must start immediately** -- parallel to FEED, not after.

**Critical situations:**
- Local packages in new geographies (no established local relationships)
- Specialized global packages where AVL may be outdated
- Regional packages where existing vendors lack capacity

**Pre-qualification assessment areas:**
1. Technical capability
2. Quality management system (ISO 9001, industry certifications)
3. HSE record and management system
4. Financial stability (audited accounts)
5. Capacity and current backlog
6. Relevant experience and references
7. Delivery performance history

### Vendor Qualification Refresh

Even for AVL vendors, a refresh is recommended during procurement:
- **Latest audited balance sheet**: Financial health review, going concern
- **Current order backlog**: Capacity commitment -- can they deliver on time?
- **Updated HSE certifications**: ISO 14001, ISO 45001
- **Updated quality certifications**: ISO 9001, ASME stamps, PED
- **Recent project references**: Performance on comparable projects (last 2-3 years)
- **Company commitment letter**: Written confirmation of willingness to meet schedule, terms, warranty, resource allocation

## Procurement Plan

### Procurement Cycle Timeline

| Activity | Typical Duration |
|----------|-----------------|
| Specification development | 4-8 weeks |
| RFQ preparation and issue | 1-2 weeks |
| Vendor quotation period | 4-6 weeks |
| Technical evaluation | 2-4 weeks |
| Commercial evaluation | 2-4 weeks |
| PO award | 1-2 weeks |
| Manufacturing | 3-18 months |
| Inspection and testing | 1-4 weeks |
| Shipping and delivery | 2-8 weeks |

### Long Lead Item Prioritization
1. Identify items with total procurement cycle > 6 months
2. Calculate required PO date = construction need date - lead time
3. Calculate required spec date = PO date - procurement cycle
4. Engineering produces specs for long lead items first

### FEED-to-Procurement Handoff
At Design Freeze (G3), FEED scope is frozen:
- Equipment specifications finalized and approved
- RFQs issued with frozen specs
- Any post-freeze change requires formal change order

## Vendor Evaluation Scoring

| Criteria | Weight | Vendor A | Vendor B | Vendor C |
|----------|--------|---------|---------|---------|
| Technical compliance | 30% | [score] | [score] | [score] |
| Price | 25% | [score] | [score] | [score] |
| Delivery | 20% | [score] | [score] | [score] |
| Quality / References | 15% | [score] | [score] | [score] |
| Commercial terms | 10% | [score] | [score] | [score] |
| **Weighted Total** | **100%** | **[total]** | **[total]** | **[total]** |
