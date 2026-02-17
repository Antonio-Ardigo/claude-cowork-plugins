---
description: Generate a toll-gate project plan -- scope, 3 alternatives, FEED, AACE cost, schedule, procurement, constructability, VE, risk, permits, and Design Freeze verification
argument-hint: "<project description>"
---

# /project-plan -- Toll-Gate Project Planning

Generate a structured engineering/construction project plan following a **toll gate (stage-gate) process** from concept (G0) through Design Freeze (G3). Produces Excel workbooks at each gate with cost estimates, schedules, scope, quality, procurement plans, risk registers, and permit tracking.

**Important**: This command assists with project planning workflows for engineering and construction projects. Outputs are preliminary planning documents and should be reviewed by qualified project management professionals.

## Invocation

```
/project-plan <project description>
/project-plan
```

If no project description is provided, prompt the user.

## Toll Gate Framework

The entire workflow follows a stage-gate process. Each gate has defined deliverables, a verification checkpoint, and a **go / no-go / recycle** decision. Risk management is embedded at every gate. An Excel workbook (.xlsx) is produced at each gate.

| Gate | Phase | 3D Model | AACE Class | Gate Deliverables |
|------|-------|----------|------------|-------------------|
| G0 | Concept Screening | -- | Class 5 (+50/-30%) | Feasibility, 3 alternatives, selection |
| G1 | Pre-FEED / Conceptual | ~10% | Class 4 (+/-30%) | Preliminary design, quick cost estimate, schedule, long lead items |
| G2 | Basic Design (FEED) | ~30% | Class 3 (+/-15-20%) | Specs, procurement packages, WBS, constructability, VE |
| G3 | **Design Freeze** | ~60% | Class 2 (+/-10-15%) | **FEED frozen. Verification: cost, schedule, scope, quality, permits. RFQs issued.** |

**Critical rule at G3**: FEED scope is frozen. This freeze enables procurement to issue RFQs for long lead items with confidence that specifications will not change. Any post-freeze change requires a formal change order with cost/schedule impact assessment.

---

## Workflow

### Step 1 -- Project Intake

Accept the project description. Gather the following via structured questions:

1. **Project name** and one-sentence objective
2. **Major deliverables** and scope boundaries (inclusions and exclusions)
3. **Site / location / geography** (country, region, site conditions)
4. **Constraints**: budget ceiling, target completion date, regulatory/permitting environment, environmental restrictions
5. **Stakeholders**: client, contractor, key subcontractors, authorities
6. **Contract type**: lump-sum, cost-plus, design-build, EPC, EPCM
7. **Industry sector**: oil & gas, power generation, renewables, infrastructure, industrial, water/wastewater, mining

If the user provides partial context, proceed with what is available and note assumptions.

#### Output Format

```
## Project Data Sheet

| Field | Value |
|-------|-------|
| Project Name | [name] |
| Objective | [one sentence] |
| Location | [site, region, country] |
| Contract Type | [EPC / EPCM / lump-sum / cost-plus / design-build] |
| Industry Sector | [sector] |
| Budget Ceiling | [amount or TBD] |
| Target Completion | [date or duration] |
| Key Constraints | [regulatory, environmental, site-specific] |
| Stakeholders | [client, contractor, authorities] |
| Assumptions | [any assumptions made due to missing info] |
```

---

### Step 2 -- Requirements & Performance Guarantees

Define three categories of requirements:

**Performance Guarantees:**
- Capacity / throughput / output
- Efficiency / heat rate / conversion rate
- Availability / uptime
- Design life (years)
- Environmental limits (emissions, noise, discharge, waste)
- Utility consumption (power, water, fuel)

**Quality Standards:**
- Applicable codes and standards (ASME, API, IEC, EN, local building codes)
- Certifications required
- Inspection level (third-party, client witness, self-certification)
- Warranty terms

**Regulatory Requirements:**
- Permits required (list all -- environmental, construction, fire, security, temporary works)
- Environmental impact assessment (EIA/ESIA) status
- Safety standards (HAZOP, SIL classification)
- Local content requirements (if applicable)

#### Output Format

```
## Requirements Register

| ID | Requirement | Category | Target Value | Verification Method |
|----|------------|----------|-------------|-------------------|
| REQ-001 | [description] | Performance | [value + unit] | [test / analysis / inspection] |
| REQ-002 | [description] | Quality | [standard ref] | [certification / audit] |
| REQ-003 | [description] | Regulatory | [permit type] | [authority approval] |
```

---

### Step 3 -- G0: Three Alternatives (Synthetic Comparison)

Generate 3 distinct approaches using **Conservative / Balanced / Aggressive** archetypes:

**For each alternative, provide:**
- Design concept (2-3 sentences describing the technical approach)
- Top-2-level WBS (major packages only)
- AACE Class 5 cost range
- Rough schedule (total months)
- Risk profile (top 3 risks with H/M/L rating)
- Quality approach (minimum code / exceed code / premium)

#### Comparison Table

```
## Alternative Comparison (G0 -- Class 5)

| Dimension | A -- Conservative | B -- Balanced | C -- Aggressive |
|-----------|------------------|---------------|-----------------|
| Design concept | Proven technology, standard config | Optimized conventional | Advanced / innovative |
| Scope | Minimum viable | Full scope | Enhanced scope |
| Cost range (Class 5) | [EUR X-Y M] | [EUR X-Y M] | [EUR X-Y M] |
| Duration | [X months] | [X months] | [X months] |
| Risk level | Low tech / higher CAPEX | Balanced | High tech / lower unit cost |
| Quality approach | Meet minimum code | Exceed code, standard QA | Premium QA/QC |
| Key trade-off | [one sentence] | [one sentence] | [one sentence] |
```

**Embedded risk session:** For each alternative, present:

```
### Risk Profile -- Alternative [A/B/C]

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| [risk 1] | H/M/L | H/M/L | [action] |
| [risk 2] | H/M/L | H/M/L | [action] |
| [risk 3] | H/M/L | H/M/L | [action] |
```

**Gate G0 Decision:** Ask the user to select Alternative A, B, C, or a hybrid combination. Confirm selection before proceeding.

#### G0 Excel Workbook

Generate `[ProjectName]_G0_Concept.xlsx` with these sheets:

| Sheet | Content |
|-------|---------|
| Cover | Project data sheet, gate info, date, prepared by |
| Requirements | Requirements register table |
| Alternatives | Three-alternative comparison table |
| Cost_Estimate | Class 5 cost ranges per alternative |
| Schedule | High-level duration estimates per alternative |
| Scope | Scope definition and boundaries per alternative |
| Quality | Quality approach per alternative |
| Permits | Permit inventory -- identify all required permits, map to gates |
| Risk_G0 | Preliminary risk register (per alternative) |
| Decision | Gate G0 decision record (selected alternative, rationale) |

---

### Step 4 -- G1: Pre-FEED (+/-30% Design & Quick Cost Estimate)

For the selected alternative, produce:

**4a -- Preliminary Design (+/-30%)**
- Process / functional description
- Block flow diagram (described textually)
- Major equipment list with preliminary sizing
- Design basis and assumptions
- Plot plan concept (area allocation)

**4b -- Quick Cost Estimate (AACE Class 4, +/-30%)**

```
## Cost Estimate -- G1 (AACE Class 4, +/-30%)

| Cost Category | Estimate | Low (-30%) | High (+30%) |
|--------------|----------|-----------|------------|
| Major Equipment | [EUR] | [EUR] | [EUR] |
| Bulk Materials | [EUR] | [EUR] | [EUR] |
| Civil / Structural | [EUR] | [EUR] | [EUR] |
| Piping | [EUR] | [EUR] | [EUR] |
| Electrical | [EUR] | [EUR] | [EUR] |
| Instrumentation & Control | [EUR] | [EUR] | [EUR] |
| Insulation / Painting | [EUR] | [EUR] | [EUR] |
| Engineering (FEED + Detail) | [EUR] | [EUR] | [EUR] |
| Procurement Management | [EUR] | [EUR] | [EUR] |
| Construction | [EUR] | [EUR] | [EUR] |
| Commissioning / Startup | [EUR] | [EUR] | [EUR] |
| Owner's Costs | [EUR] | [EUR] | [EUR] |
| Contingency | [EUR] | [EUR] | [EUR] |
| **TOTAL** | **[EUR]** | **[EUR]** | **[EUR]** |
```

**4c -- Preliminary Schedule**
- Phase-level milestone chart (engineering, procurement, construction, commissioning)
- Total duration estimate
- Key milestones: FID, FEED complete, first equipment delivery, mechanical completion, PAC

**4d -- Long Lead Item Identification**

```
## Long Lead Items Register

| Item | Lead Time (months) | Estimated Cost | Spec Priority | Procurement Risk |
|------|-------------------|---------------|--------------|-----------------|
| [equipment] | [months] | [EUR] | [High/Med] | [description] |
```

Items with lead time > 6 months. This list drives procurement prioritization -- engineering must produce specs for these items first.

**4e -- Initial Risk Register**

```
## Risk Register -- G1

| ID | Risk Description | Category | Prob | Impact | Score | Owner | Mitigation |
|----|-----------------|----------|------|--------|-------|-------|-----------|
| R-001 | [description] | Tech/Commercial/Schedule/Permit | H/M/L | H/M/L | [1-9] | [role] | [action] |
```

**4f -- Permit Status**
- Update permit tracking register from G0
- Environmental permit: EIA preparation status
- Planning permission: pre-application discussions

**Gate G1 Decision:** Present findings and ask for go / no-go / recycle decision.

#### G1 Excel Workbook

Generate `[ProjectName]_G1_PreFEED.xlsx` with these sheets:

| Sheet | Content |
|-------|---------|
| Cover | Project data sheet, gate info |
| Design_Basis | Design basis and assumptions |
| Equipment_List | Major equipment with preliminary sizing |
| Cost_Estimate | AACE Class 4 cost breakdown (+/-30%), all categories |
| Schedule | Phase-level milestone chart, total duration |
| Scope | Scope baseline (preliminary), deliverables list |
| Quality | Applicable codes/standards matrix, quality approach |
| Permits | Permit tracking register -- submissions started, environmental/planning status |
| Temporary_Works | Camp preliminary design, excavation plan, temp facilities |
| Long_Lead_Items | Long lead item register with lead times |
| Risk_Register | Initial risk register |
| Decision | Gate G1 decision record |

---

### Step 5 -- G2: Basic Design (FEED -- 30% Model)

Develop the full FEED deliverables:

**5a -- Preliminary Design (FEED Level)**
- Process description with basis of design
- Major systems and subsystems breakdown
- Key equipment list with specifications (capacity, materials, design conditions)
- Interface matrix (system-to-system dependencies)
- Design assumptions register

**5b -- WBS (3-Level, Linked to Procurement)**
- Deliverable-oriented decomposition following the 100% rule
- 3 hierarchical levels with work packages
- Each work package: ID, description, deliverable, responsible party, procurement package reference
- WBS-to-procurement package mapping table

```
## Work Breakdown Structure

### Level 1: [Project Name]
  ### 1.0 Project Management
    1.1 Project Controls
    1.2 Document Management
    1.3 HSE Management
  ### 2.0 Engineering
    2.1 Process Engineering
    2.2 Mechanical Engineering
    2.3 Civil / Structural
    2.4 Electrical
    2.5 Instrumentation & Control
    2.6 Piping
  ### 3.0 Procurement
    3.1 Major Equipment
    3.2 Bulk Materials
    3.3 Subcontracts
  ### 4.0 Construction
    4.1 Site Preparation
    4.2 Civil Works
    4.3 Structural Steel
    4.4 Mechanical Installation
    4.5 Piping Installation
    4.6 Electrical Installation
    4.7 Instrumentation Installation
  ### 5.0 Commissioning & Startup
    5.1 Pre-commissioning
    5.2 Commissioning
    5.3 Performance Testing
    5.4 Handover

## WBS-to-Procurement Mapping

| WBS ID | Work Package | Procurement Package | Supply Chain | Lead Time |
|--------|-------------|-------------------|-------------|-----------|
| 3.1.1 | [package] | PP-001 | Global/Regional/Local | [months] |
```

**5c -- Procurement Strategy & Plan**

Procurement packages derived from WBS and equipment specifications.

```
## Supply Chain Classification

| Package | Supply Chain | Sourcing Strategy | Qualified Vendors (AVL) | Pre-Qual Required? |
|---------|-------------|-------------------|------------------------|-------------------|
| [name] | Global | Competitive (3+ OEMs) | [count] | [Yes/No] |
| [name] | Regional | Frame agreement | [count] | [Yes/No] |
| [name] | Local | Competitive (local) | [count] | [Yes/No] |
```

Supply chain categories:
- **Global**: Specialized OEMs, worldwide sourcing (e.g., turbines, compressors, high-pressure pumps)
- **Regional**: Multiple suppliers within region (e.g., structural steel, piping, transformers)
- **Local**: Site-proximity contractors/suppliers (e.g., civil works, concrete, earthworks)

**Vendor Pre-Qualification Trigger:** Check the company Approved Vendor List (AVL) against the procurement strategy. If fewer than 3 qualified vendors exist for any package at the required supply chain level, **pre-qualification must start immediately** -- do not wait for FEED completion. Critical for:
- Local supply chain packages where qualified local vendors may be missing
- Specialized global packages where AVL may be outdated
- Regional packages in new geographies with no prior relationships

**Vendor Qualification Refresh:** Even for AVL vendors, a refresh is recommended during procurement:
- Latest audited balance sheet / financial health review
- Current order backlog and capacity commitment assessment
- Updated HSE and quality certifications
- Recent project references and performance record
- Company commitment letter (willingness to meet project schedule, terms, warranty)

```
## Time-Phased Procurement Plan

| Package | Supply Chain | Spec Ready | Pre-Qual | RFQ Issue | Tech Eval | PO Award | Delivery | Lead Time |
|---------|-------------|-----------|----------|-----------|-----------|----------|----------|-----------|
| [LLI 1] | Global | [date] | [date] | [date] | [date] | [date] | [date] | [months] |
| [LLI 2] | Global | [date] | [date] | [date] | [date] | [date] | [date] | [months] |
| [Std Equip] | Regional | [date] | [date] | [date] | [date] | [date] | [date] | [months] |
| [Bulk Mat] | Regional | [date] | [date] | [date] | [date] | [date] | [date] | [months] |
| [Civil] | Local | [date] | [date] | [date] | [date] | [date] | [date] | [months] |
```

**5d -- Cost Estimate (AACE Class 3, +/-15-20%)**
- Cost-loaded WBS table with low / expected / high per line item
- Direct costs: equipment, bulk materials, civil, piping, electrical, I&C, insulation/painting
- Indirect costs: engineering, procurement management, construction management, temporary facilities
- Owner's costs, contingency (per AACE RP 40R-08)
- Total with accuracy range

```
## Cost Estimate -- G2 (AACE Class 3, +/-15-20%)

| WBS ID | Description | Estimate | Low | High |
|--------|-----------|----------|-----|------|
| 2.0 | Engineering | [EUR] | [EUR] | [EUR] |
| 3.1 | Major Equipment | [EUR] | [EUR] | [EUR] |
| 3.2 | Bulk Materials | [EUR] | [EUR] | [EUR] |
| 4.1 | Site Preparation | [EUR] | [EUR] | [EUR] |
| 4.2 | Civil Works | [EUR] | [EUR] | [EUR] |
| ... | ... | ... | ... | ... |
| -- | Contingency | [EUR] | [EUR] | [EUR] |
| **--** | **TOTAL** | **[EUR]** | **[EUR]** | **[EUR]** |
```

**5e -- Schedule (CPM)**
- Engineering, procurement, construction, commissioning phases
- Milestone schedule with durations and dependencies
- Critical path identification
- ASCII bar chart (months along horizontal axis, activities along vertical)
- Key decision gates: FID, mechanical completion, RFSU (Ready for Start-Up), PAC (Provisional Acceptance Certificate)
- **Procurement-driven scheduling**: Long lead item delivery dates drive construction sequence; engineering priorities adjusted to feed procurement plan first

**5f -- Constructability Review**
- Modularization assessment (shop vs field fabrication trade-offs)
- Site access, laydown areas, logistics
- Lift study requirements (heavy lifts)
- Construction sequence and method statements (high level)
- **Temporary works design**: construction camp (accommodation, offices, canteen, utilities, waste), excavation preliminary design (geotechnical survey, shoring, dewatering, spoil disposal), temporary roads, laydown areas, fencing, temporary utilities
- Constructability issues register with recommendations

**5g -- Value Engineering**
- Function analysis (what does each system DO vs what does it COST)
- VE proposals: alternative, estimated savings, impact on performance/quality/schedule
- Lifecycle cost comparison where applicable (CAPEX vs OPEX, NPV)
- VE decision log: accepted / rejected / deferred with rationale

```
## Value Engineering Log

| ID | System | Current Design | VE Proposal | Savings | Impact | Decision |
|----|--------|---------------|------------|---------|--------|----------|
| VE-001 | [system] | [current] | [alternative] | [EUR] | [perf/qual/schedule] | Accepted/Rejected/Deferred |
```

**5h -- Risk Management Session**
- Updated risk register from G1
- Qualitative risk assessment: probability-impact matrix (5x5)
- Top 10 risks ranked by score
- Risk response plan: avoid, mitigate, transfer, accept
- Risk-to-WBS mapping (which work packages are affected by each risk)
- Contingency allocation linked to risk exposure

**5i -- Permits & Approvals Status**
- Permit tracking register updated with all required permits and current status
- Environmental permit: EIA submitted / approved / conditional
- Planning/zoning permission: status
- Construction permit: application prepared based on FEED design
- Temporary works permit: camp and excavation design submitted
- Fire fighting permit: fire protection design submitted
- Security permit: site security plan submitted
- Critical path assessment: which permits are on critical path, expected approval dates vs construction start
- Permit conditions register: conditions from approved permits to be satisfied

```
## Permit Tracking Register

| ID | Permit Type | Authority | Submitted | Expected Approval | Status | Conditions | Critical Path? |
|----|------------|-----------|-----------|------------------|--------|-----------|---------------|
| PER-001 | Environmental (EIA) | [authority] | [date] | [date] | [status] | [conditions] | [Yes/No] |
| PER-002 | Construction | [authority] | [date] | [date] | [status] | [conditions] | [Yes/No] |
| PER-003 | Temporary Works | [authority] | [date] | [date] | [status] | [conditions] | [Yes/No] |
| PER-004 | Fire Safety | [authority] | [date] | [date] | [status] | [conditions] | [Yes/No] |
| PER-005 | Security | [authority] | [date] | [date] | [status] | [conditions] | [Yes/No] |
```

**Gate G2 Decision:** Present all FEED deliverables. Ask for go / no-go / recycle decision. If go, proceed to Design Freeze.

#### G2 Excel Workbook

Generate `[ProjectName]_G2_FEED.xlsx` with these sheets:

| Sheet | Content |
|-------|---------|
| Cover | Project data sheet, gate info |
| Design_Summary | FEED-level design, systems breakdown |
| Equipment_Specs | Equipment list with specifications |
| WBS | 3-level WBS with work packages |
| Procurement_Strategy | Supply chain classification, vendor status, sourcing strategy |
| Procurement_Plan | Time-phased procurement plan |
| Vendor_PreQual | AVL gap analysis, pre-qualification status |
| Cost_Estimate | AACE Class 3 cost-loaded WBS (+/-15-20%) |
| Schedule_CPM | CPM schedule, milestones, critical path |
| Scope | Scope register, WBS completeness check |
| Quality | Quality plan, ITP framework, codes matrix |
| Permits | Permit status -- construction, fire, security permits |
| Temporary_Works | Camp, excavation, temp roads, laydown design |
| Constructability | Constructability issues register |
| Value_Engineering | VE proposals and decision log |
| Risk_Register | Updated risk register with response plan |
| Decision | Gate G2 decision record |

---

### Step 6 -- G3: Design Freeze & Verification

**FEED scope is frozen at this gate.** This freeze enables:
- RFQs for long lead items issued with final specifications
- Procurement commitments made with confidence that specs will not change
- Any post-freeze change requires a formal change order with cost/schedule impact assessment

**Formal verification across six dimensions:**

**6a -- Cost Verification**
- Updated estimate (AACE Class 2, +/-10-15%)
- Comparison: G1 estimate vs G2 estimate vs G3 estimate (cost trend)
- Contingency adequacy check
- Value engineering savings incorporated

```
## Cost Trend -- G1 to G3

| Category | G1 (Class 4) | G2 (Class 3) | G3 (Class 2) | Variance G1-G3 |
|----------|-------------|-------------|-------------|---------------|
| Equipment | [EUR] | [EUR] | [EUR] | [%] |
| ... | ... | ... | ... | ... |
| **TOTAL** | **[EUR]** | **[EUR]** | **[EUR]** | **[%]** |
| Accuracy | +/-30% | +/-15-20% | +/-10-15% | -- |
```

**6b -- Schedule Verification**
- Updated CPM schedule
- Critical path confirmed
- Long lead item delivery dates confirmed against construction need dates
- Float analysis on non-critical paths
- Schedule risk assessment

**6c -- Scope Verification**
- Scope baseline frozen
- WBS complete and approved
- All procurement packages defined with specifications
- Scope exclusions documented
- Interface agreements confirmed

**6d -- Quality Verification**
- Quality plan finalized
- Applicable codes/standards matrix confirmed
- Inspection & Test Plan (ITP) framework: hold points, witness points
- Performance guarantee test protocol defined
- Commissioning sequence outlined

**6e -- Permits Verification**
- All required permits status: approved / conditional / pending / not yet submitted
- Permit conditions register: all conditions listed with closure plan
- Critical path impact: any permit delays that block construction start
- Temporary works permits: camp and excavation approved for mobilization
- Unapproved permits flagged as go/no-go blockers

**6f -- Risk Verification**
- Final risk register reviewed
- Residual risk assessment post-mitigation
- Contingency vs risk exposure reconciliation
- Permit risk included
- Risk-based go / no-go recommendation

#### Output: Gate G3 Decision Package

```
## G3 Design Freeze -- Verification Summary

| Dimension | Status | Key Finding | Go/No-Go |
|-----------|--------|------------|----------|
| Cost | [Green/Yellow/Red] | [summary] | [Go/Conditional/No-Go] |
| Schedule | [Green/Yellow/Red] | [summary] | [Go/Conditional/No-Go] |
| Scope | [Green/Yellow/Red] | [summary] | [Go/Conditional/No-Go] |
| Quality | [Green/Yellow/Red] | [summary] | [Go/Conditional/No-Go] |
| Permits | [Green/Yellow/Red] | [summary] | [Go/Conditional/No-Go] |
| Risk | [Green/Yellow/Red] | [summary] | [Go/Conditional/No-Go] |
| **OVERALL** | **[status]** | **[recommendation]** | **[Go/No-Go/Recycle]** |
```

#### G3 Excel Workbook

Generate `[ProjectName]_G3_DesignFreeze.xlsx` with these sheets:

| Sheet | Content |
|-------|---------|
| Cover | Project data sheet, gate info, **FEED FROZEN** |
| Cost_Verification | AACE Class 2 estimate, G1-G2-G3 cost trend |
| Schedule_Verification | Updated CPM, critical path, float analysis |
| Scope_Verification | Frozen scope baseline, WBS complete, procurement packages defined |
| Quality_Verification | Quality plan, codes matrix, ITP framework, performance test protocol |
| Permits_Verification | All permits status, conditions register, critical path impact |
| Risk_Verification | Final risk register, residual risk, contingency reconciliation |
| Procurement_RFQ | RFQ-ready packages with frozen specifications |
| Executive_Summary | 1-page summary with go/no-go recommendation |
| Decision | Gate G3 decision record |

---

### Step 7 -- Consolidated Project Plan

Produce a consolidated project plan document combining all outputs from G0 through G3:

```
## Project Plan: [Name]

**Date**: [date]  |  **Gate**: G3 Design Freeze  |  **AACE Class**: 2
**Accuracy**: +/-10-15%  |  **Status**: FEED Frozen

### Executive Summary
[2-3 paragraphs: project objective, selected alternative, key cost/schedule/scope numbers, go/no-go recommendation]

### 1. Project Data Sheet
### 2. Requirements Register
### 3. Alternative Selection Summary (G0)
### 4. Design Summary (G1-G2)
### 5. Work Breakdown Structure
### 6. Procurement Strategy & Plan (long lead items highlighted)
### 7. Cost Estimate (trend from G1 through G3)
### 8. Schedule (critical path and procurement dates)
### 9. Constructability Assessment
### 10. Value Engineering Log
### 11. Risk Register
### 12. Quality Plan
### 13. Permits & Approvals Status
### 14. Design Freeze Verification Summary (six-dimension matrix)
### 15. Gate Decision (Go / No-Go / Recycle with conditions)
```

---

## Excel Workbook Generation

At each toll gate, generate the workbook using Python with openpyxl. Apply:
- **Header formatting**: Bold headers, frozen top row, auto-filter on data columns
- **Conditional formatting**: Red/Yellow/Green for risk levels, cost variances, permit status
- **Column widths**: Auto-sized to content
- **Cover sheet**: Project name, gate identifier, date, prepared by, AACE class, accuracy range
- **Consistent layout**: All workbooks follow the same formatting conventions

Use the Bash tool to execute Python code that creates the .xlsx files. Save workbooks to the current working directory.

## Notes

- If the user provides only partial information, proceed with what is available and flag assumptions prominently
- Currency defaults to EUR unless the user specifies otherwise
- For cost estimates, always state the AACE class and accuracy range
- Long lead items (>6 months) must always be identified and highlighted in the procurement plan
- The vendor pre-qualification trigger (< 3 qualified vendors on AVL) is a critical action item -- flag it prominently
- Vendor qualification refresh is recommended even for AVL-listed vendors during procurement
- Permits are often on the critical path -- always assess their impact on the schedule
- Temporary works (camp, excavation) require preliminary design at G1 and are a permit prerequisite
- Risk management is not a standalone exercise -- it is embedded at every gate
- At G3, the decision to freeze FEED is irrevocable without a formal change order process
