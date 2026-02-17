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

### Step 1 -- Typical Project Configuration

**Purpose:** Before analyzing the specific project, establish the industry baseline. Research what a "typical" project of this type and size looks like in terms of configuration, cost, and duration. This step provides the reference frame against which the specific project will be compared.

**1a -- Identify the Plant Type and Typical Configuration**

Based on the project description, identify:
- **Plant type and technology**: e.g., SWRO desalination, CCGT power plant, solar PV, gas processing, wastewater treatment
- **Typical process configuration**: Standard process flow, major systems, typical equipment lineup for this plant type and capacity
- **Design basis norms**: Industry-standard design parameters (recovery rate, efficiency, availability, etc.)
- **Typical battery limits**: What is normally included/excluded in EPC scope for this plant type

Use the `desalination-process-design` skill (or equivalent process knowledge for other plant types) to describe the standard configuration.

**1b -- Plant Cost Curves (Typical CAPEX)**

Using the `plant-cost-curves` skill, look up the **typical capital cost range** for this plant type and capacity:
- CAPEX per unit capacity (e.g., USD/m3/d for desalination, USD/kW for power)
- Total CAPEX range (low-mid-high)
- Scaling exponent for capacity-factored estimates
- Location factor adjustment for the project region

```
## Typical Plant Cost Benchmark

| Parameter | Value |
|-----------|-------|
| Plant type | [type] |
| Capacity | [value + unit] |
| Benchmark CAPEX range | [USD X - Y per unit] |
| Benchmark total CAPEX | [USD X - Y M] |
| Location factor | [factor] |
| Location-adjusted CAPEX | [USD X - Y M] |
| Source basis | Plant cost curves (mid-2020s, industry benchmark) |
```

**1c -- Typical Project Duration**

Using the `plant-cost-curves` skill, look up the **typical EPC duration** for this plant type and capacity:
- Engineering phase duration (months)
- Procurement phase duration (months)
- Construction phase duration (months)
- Total EPC duration range (months)

```
## Typical Project Duration Benchmark

| Phase | Duration (months) |
|-------|------------------|
| Engineering | [X - Y] |
| Procurement | [X - Y] |
| Construction | [X - Y] |
| Total EPC | [X - Y] |
| Notes | [any relevant notes on duration drivers] |
```

**1d -- Key Equipment Cost Curves (Typical)**

Using the `equipment-cost-curves` skill, list the **major equipment items** for this plant type with their typical budget prices and delivery times:

```
## Key Equipment -- Typical Cost & Delivery

| Equipment | Specification | Budget Price (USD) | Typical Delivery (months) |
|-----------|-------------|-------------------|--------------------------|
| [item 1] | [key spec] | [range] | [range] |
| [item 2] | [key spec] | [range] | [range] |
| [item 3] | [key spec] | [range] | [range] |
| ... | ... | ... | ... |
```

This equipment list establishes the typical delivery times that will drive procurement scheduling in later steps.

**1e -- Price Market Analysis (Recent Similar Projects)**

Research and present **recent comparable projects** (last 3-5 years) of similar type, capacity, and region to benchmark cost and identify market trends:

```
## Price Market Analysis -- Recent Similar Projects

| Project | Location | Capacity | Year | EPC Cost | Cost/Unit | Contract Type | Notes |
|---------|----------|----------|------|----------|-----------|--------------|-------|
| [name/ref] | [location] | [capacity] | [year] | [USD M] | [USD/unit] | [EPC/EPCM] | [key note] |
| [name/ref] | [location] | [capacity] | [year] | [USD M] | [USD/unit] | [EPC/EPCM] | [key note] |
| [name/ref] | [location] | [capacity] | [year] | [USD M] | [USD/unit] | [EPC/EPCM] | [key note] |
```

Identify market trends:
- Are prices trending up or down vs the cost curve benchmarks?
- Vendor backlog status: tight market or slack market?
- Material price trends (steel, copper, membranes, specialty alloys)
- Regional construction labor market conditions

**1f -- Delivery Time Market Analysis**

Research and present **current delivery times** for key equipment based on recent market conditions:

```
## Delivery Time Market Analysis

| Equipment | Typical Delivery (curve) | Current Market Delivery | Trend | Notes |
|-----------|------------------------|------------------------|-------|-------|
| [item 1] | [months] | [months] | [shorter/same/longer] | [vendor backlog, capacity] |
| [item 2] | [months] | [months] | [shorter/same/longer] | [notes] |
| [item 3] | [months] | [months] | [shorter/same/longer] | [notes] |
```

Flag items where current delivery exceeds typical curves -- these may require early procurement action or alternative sourcing.

#### Output: Typical Configuration Summary

Combine all above into a single reference document that will be used throughout the project plan as the "baseline benchmark."

---

### Step 2 -- Specific Project Differences

**Purpose:** Identify what makes THIS specific project different from the typical configuration established in Step 1. These differences drive cost premiums/savings, schedule adjustments, and project-specific risks.

**2a -- Site-Specific Differences**

Compare the project site against typical assumptions:

| Factor | Typical Assumption | This Project | Impact |
|--------|-------------------|-------------|--------|
| Location / accessibility | Standard infrastructure | [actual] | [cost/schedule impact] |
| Climate / weather | Temperate, no extreme | [actual] | [construction productivity] |
| Geotechnical conditions | Standard bearing capacity | [actual] | [foundation cost] |
| Seismic zone | Low seismicity | [actual] | [structural design premium] |
| Labor availability | Moderate, skilled | [actual] | [productivity, cost] |
| Existing infrastructure | Utilities available at BL | [actual] | [tie-in cost, scope] |
| Environmental sensitivity | Standard EIA required | [actual] | [permit complexity, timeline] |

**2b -- Scope Differences from Typical Configuration**

Identify scope items that differ from the standard configuration:

```
## Scope Differences vs Typical Configuration

| Item | Typical Configuration | This Project | Cost Impact | Schedule Impact |
|------|---------------------|-------------|------------|----------------|
| [item] | [standard approach] | [project-specific] | [+/- EUR or %] | [+/- months] |
| [item] | [included/excluded] | [different scope] | [+/- EUR or %] | [+/- months] |
```

Examples of common differences:
- Higher/lower capacity than benchmark range
- Non-standard materials (corrosion, temperature, regulatory)
- Additional systems not in typical scope (e.g., ZLD for brine, battery storage)
- Reduced scope (e.g., intake/outfall by others)
- Different redundancy philosophy (N+1 vs N+2)
- Special regulatory requirements (local content, specific codes)

**2c -- Cost Impact of Differences**

Quantify the total cost impact of project-specific differences relative to the typical cost curve:

```
## Cost Adjustment -- Typical to Project-Specific

| Adjustment | Basis | Impact (USD M) |
|-----------|-------|---------------|
| Location factor (vs USGC baseline) | [factor] | [+/- USD M] |
| Scope additions | [list] | [+ USD M] |
| Scope reductions | [list] | [- USD M] |
| Material premiums | [specifics] | [+ USD M] |
| Regulatory/permitting premiums | [specifics] | [+ USD M] |
| Market conditions adjustment | [tight/slack] | [+/- USD M] |
| **Net adjustment** | -- | **[+/- USD M]** |
| **Adjusted CAPEX range** | -- | **[USD X - Y M]** |
```

**2d -- Schedule Impact of Differences**

Quantify the total schedule impact:

```
## Schedule Adjustment -- Typical to Project-Specific

| Adjustment | Typical Duration | This Project | Delta (months) |
|-----------|-----------------|-------------|---------------|
| Engineering complexity | [months] | [months] | [+/-] |
| Procurement (market delivery) | [months] | [months] | [+/-] |
| Construction (site conditions, labor) | [months] | [months] | [+/-] |
| Permitting timeline | [months] | [months] | [+/-] |
| **Adjusted total EPC duration** | **[months]** | **[months]** | **[+/-]** |
```

#### Output Format

```
## Project-Specific Assessment Summary

| Dimension | Typical Benchmark | This Project (Adjusted) | Key Difference |
|-----------|------------------|------------------------|---------------|
| CAPEX | [USD X - Y M] | [USD X - Y M] | [main driver] |
| Duration | [X - Y months] | [X - Y months] | [main driver] |
| Key risk | [typical risk] | [project-specific risk] | [why different] |
```

This assessment becomes the foundation for all subsequent steps -- cost estimates, schedules, and risk assessments will reference both the typical benchmarks AND the project-specific adjustments.

---

### Step 3 -- Project Intake

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
| Typical Benchmark CAPEX | [from Step 1] |
| Adjusted CAPEX Range | [from Step 2] |
| Typical Benchmark Duration | [from Step 1] |
| Adjusted Duration Range | [from Step 2] |
| Assumptions | [any assumptions made due to missing info] |
```

---

### Step 4 -- Requirements & Performance Guarantees

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

### Step 5 -- G0: Three Alternatives (Synthetic Comparison)

Generate 3 distinct approaches using **Conservative / Balanced / Aggressive** archetypes:

**For each alternative, provide:**
- Design concept (2-3 sentences describing the technical approach)
- Top-2-level WBS (major packages only)
- AACE Class 5 cost range
- Rough schedule (total months)
- Risk profile (top 3 risks with H/M/L rating)
- Quality approach (minimum code / exceed code / premium)
- **Comparison to typical configuration**: How each alternative relates to the industry benchmark from Step 1

#### Comparison Table

```
## Alternative Comparison (G0 -- Class 5)

| Dimension | A -- Conservative | B -- Balanced | C -- Aggressive |
|-----------|------------------|---------------|-----------------|
| Design concept | Proven technology, standard config | Optimized conventional | Advanced / innovative |
| Scope | Minimum viable | Full scope | Enhanced scope |
| Cost range (Class 5) | [EUR X-Y M] | [EUR X-Y M] | [EUR X-Y M] |
| vs Typical benchmark | [+/- %] | [+/- %] | [+/- %] |
| Duration | [X months] | [X months] | [X months] |
| vs Typical duration | [+/- months] | [+/- months] | [+/- months] |
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
| Typical_Config | Typical configuration summary, plant cost curve, equipment cost curves, typical duration (from Step 1) |
| Market_Analysis | Price market analysis, delivery time market analysis, recent similar projects (from Step 1) |
| Project_Differences | Specific project differences, cost and schedule adjustments (from Step 2) |
| Requirements | Requirements register table |
| Alternatives | Three-alternative comparison table (with benchmark comparison) |
| Cost_Estimate | Class 5 cost ranges per alternative |
| Schedule | High-level duration estimates per alternative |
| Scope | Scope definition and boundaries per alternative |
| Quality | Quality approach per alternative |
| Permits | Permit inventory -- identify all required permits, map to gates |
| Risk_G0 | Preliminary risk register (per alternative) |
| Decision | Gate G0 decision record (selected alternative, rationale) |

---

### Step 6 -- G1: Pre-FEED (+/-30% Design & Quick Cost Estimate)

For the selected alternative, produce:

**6a -- Preliminary Design (+/-30%)**
- Process / functional description
- Block flow diagram (described textually)
- Major equipment list with preliminary sizing
- Design basis and assumptions
- Plot plan concept (area allocation)
- **Comparison to typical configuration**: Note deviations from the standard process design (from Step 1)

**6b -- Quick Cost Estimate (AACE Class 4, +/-30%)**

```
## Cost Estimate -- G1 (AACE Class 4, +/-30%)

| Cost Category | Estimate | Low (-30%) | High (+30%) | Typical Benchmark | Delta vs Benchmark |
|--------------|----------|-----------|------------|------------------|-------------------|
| Major Equipment | [EUR] | [EUR] | [EUR] | [EUR] | [%] |
| Bulk Materials | [EUR] | [EUR] | [EUR] | [EUR] | [%] |
| Civil / Structural | [EUR] | [EUR] | [EUR] | [EUR] | [%] |
| Piping | [EUR] | [EUR] | [EUR] | [EUR] | [%] |
| Electrical | [EUR] | [EUR] | [EUR] | [EUR] | [%] |
| Instrumentation & Control | [EUR] | [EUR] | [EUR] | [EUR] | [%] |
| Insulation / Painting | [EUR] | [EUR] | [EUR] | [EUR] | [%] |
| Engineering (FEED + Detail) | [EUR] | [EUR] | [EUR] | [EUR] | [%] |
| Procurement Management | [EUR] | [EUR] | [EUR] | [EUR] | [%] |
| Construction | [EUR] | [EUR] | [EUR] | [EUR] | [%] |
| Commissioning / Startup | [EUR] | [EUR] | [EUR] | [EUR] | [%] |
| Owner's Costs | [EUR] | [EUR] | [EUR] | [EUR] | [%] |
| Contingency | [EUR] | [EUR] | [EUR] | [EUR] | [%] |
| **TOTAL** | **[EUR]** | **[EUR]** | **[EUR]** | **[EUR]** | **[%]** |
```

Any line item deviating >20% from the typical benchmark must be explained (scope difference, site condition, market premium, etc.).

**6c -- Preliminary Schedule**
- Phase-level milestone chart (engineering, procurement, construction, commissioning)
- Total duration estimate
- Key milestones: FID, FEED complete, first equipment delivery, mechanical completion, PAC
- **Comparison to typical duration benchmark** (from Step 1): Explain any delta

**6d -- Long Lead Item Identification**

```
## Long Lead Items Register

| Item | Lead Time (months) | Typical Lead Time | Market Lead Time | Estimated Cost | Typical Cost | Spec Priority | Procurement Risk |
|------|-------------------|------------------|-----------------|---------------|-------------|--------------|-----------------|
| [equipment] | [months] | [months] | [months] | [EUR] | [EUR] | [High/Med] | [description] |
```

Items with lead time > 6 months. This list drives procurement prioritization -- engineering must produce specs for these items first. Lead times cross-referenced against equipment cost curves (Step 1) and delivery time market analysis (Step 1).

**6e -- Initial Risk Register**

```
## Risk Register -- G1

| ID | Risk Description | Category | Prob | Impact | Score | Owner | Mitigation |
|----|-----------------|----------|------|--------|-------|-------|-----------|
| R-001 | [description] | Tech/Commercial/Schedule/Permit | H/M/L | H/M/L | [1-9] | [role] | [action] |
```

**6f -- Permit Status**
- Update permit tracking register from G0
- Environmental permit: EIA preparation status
- Planning permission: pre-application discussions

**Gate G1 Decision:** Present findings and ask for go / no-go / recycle decision.

#### G1 Excel Workbook

Generate `[ProjectName]_G1_PreFEED.xlsx` with these sheets:

| Sheet | Content |
|-------|---------|
| Cover | Project data sheet, gate info |
| Benchmark_Comparison | Cost vs typical benchmark, duration vs typical benchmark, key equipment vs typical cost/delivery |
| Design_Basis | Design basis and assumptions |
| Equipment_List | Major equipment with preliminary sizing, budget prices vs equipment cost curves |
| Cost_Estimate | AACE Class 4 cost breakdown (+/-30%), all categories, with benchmark delta column |
| Schedule | Phase-level milestone chart, total duration, with benchmark comparison |
| Scope | Scope baseline (preliminary), deliverables list |
| Quality | Applicable codes/standards matrix, quality approach |
| Permits | Permit tracking register -- submissions started, environmental/planning status |
| Temporary_Works | Camp preliminary design, excavation plan, temp facilities |
| Long_Lead_Items | Long lead item register with lead times (typical vs market) |
| Risk_Register | Initial risk register |
| Decision | Gate G1 decision record |

---

### Step 7 -- G2: Basic Design (FEED -- 30% Model)

Develop the full FEED deliverables:

**7a -- Preliminary Design (FEED Level)**
- Process description with basis of design
- Major systems and subsystems breakdown
- Key equipment list with specifications (capacity, materials, design conditions)
- Interface matrix (system-to-system dependencies)
- Design assumptions register

**7b -- WBS (3-Level, Linked to Procurement)**
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

**7c -- Procurement Strategy & Plan**

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

**7d -- Cost Estimate (AACE Class 3, +/-15-20%)**
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

**7e -- Schedule (CPM)**
- Engineering, procurement, construction, commissioning phases
- Milestone schedule with durations and dependencies
- Critical path identification
- ASCII bar chart (months along horizontal axis, activities along vertical)
- Key decision gates: FID, mechanical completion, RFSU (Ready for Start-Up), PAC (Provisional Acceptance Certificate)
- **Procurement-driven scheduling**: Long lead item delivery dates drive construction sequence; engineering priorities adjusted to feed procurement plan first

**7f -- Constructability Review**
- Modularization assessment (shop vs field fabrication trade-offs)
- Site access, laydown areas, logistics
- Lift study requirements (heavy lifts)
- Construction sequence and method statements (high level)
- **Temporary works design**: construction camp (accommodation, offices, canteen, utilities, waste), excavation preliminary design (geotechnical survey, shoring, dewatering, spoil disposal), temporary roads, laydown areas, fencing, temporary utilities
- Constructability issues register with recommendations

**7g -- Value Engineering**
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

**7h -- Risk Management Session**
- Updated risk register from G1
- Qualitative risk assessment: probability-impact matrix (5x5)
- Top 10 risks ranked by score
- Risk response plan: avoid, mitigate, transfer, accept
- Risk-to-WBS mapping (which work packages are affected by each risk)
- Contingency allocation linked to risk exposure

**7i -- Permits & Approvals Status**
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

### Step 8 -- G3: Design Freeze & Verification

**FEED scope is frozen at this gate.** This freeze enables:
- RFQs for long lead items issued with final specifications
- Procurement commitments made with confidence that specs will not change
- Any post-freeze change requires a formal change order with cost/schedule impact assessment

**Formal verification across six dimensions:**

**8a -- Cost Verification**
- Updated estimate (AACE Class 2, +/-10-15%)
- Comparison: G1 estimate vs G2 estimate vs G3 estimate (cost trend)
- **Comparison to typical benchmark** (from Step 1): Final CAPEX vs plant cost curve
- Contingency adequacy check
- Value engineering savings incorporated

```
## Cost Trend -- G1 to G3 (with Benchmark)

| Category | Typical Benchmark | G1 (Class 4) | G2 (Class 3) | G3 (Class 2) | Variance G1-G3 | Variance vs Benchmark |
|----------|------------------|-------------|-------------|-------------|---------------|---------------------|
| Equipment | [EUR] | [EUR] | [EUR] | [EUR] | [%] | [%] |
| ... | ... | ... | ... | ... | ... | ... |
| **TOTAL** | **[EUR]** | **[EUR]** | **[EUR]** | **[EUR]** | **[%]** | **[%]** |
| Accuracy | Curve range | +/-30% | +/-15-20% | +/-10-15% | -- | -- |
```

**8b -- Schedule Verification**
- Updated CPM schedule
- Critical path confirmed
- Long lead item delivery dates confirmed against construction need dates
- Float analysis on non-critical paths
- Schedule risk assessment
- **Comparison to typical duration benchmark** (from Step 1)

**8c -- Scope Verification**
- Scope baseline frozen
- WBS complete and approved
- All procurement packages defined with specifications
- Scope exclusions documented
- Interface agreements confirmed

**8d -- Quality Verification**
- Quality plan finalized
- Applicable codes/standards matrix confirmed
- Inspection & Test Plan (ITP) framework: hold points, witness points
- Performance guarantee test protocol defined
- Commissioning sequence outlined

**8e -- Permits Verification**
- All required permits status: approved / conditional / pending / not yet submitted
- Permit conditions register: all conditions listed with closure plan
- Critical path impact: any permit delays that block construction start
- Temporary works permits: camp and excavation approved for mobilization
- Unapproved permits flagged as go/no-go blockers

**8f -- Risk Verification**
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
| Cost_Verification | AACE Class 2 estimate, G1-G2-G3 cost trend, benchmark comparison |
| Schedule_Verification | Updated CPM, critical path, float analysis, benchmark comparison |
| Scope_Verification | Frozen scope baseline, WBS complete, procurement packages defined |
| Quality_Verification | Quality plan, codes matrix, ITP framework, performance test protocol |
| Permits_Verification | All permits status, conditions register, critical path impact |
| Risk_Verification | Final risk register, residual risk, contingency reconciliation |
| Procurement_RFQ | RFQ-ready packages with frozen specifications |
| Executive_Summary | 1-page summary with go/no-go recommendation |
| Decision | Gate G3 decision record |

---

### Step 9 -- Consolidated Project Plan

Produce a consolidated project plan document combining all outputs from Step 1 through G3:

```
## Project Plan: [Name]

**Date**: [date]  |  **Gate**: G3 Design Freeze  |  **AACE Class**: 2
**Accuracy**: +/-10-15%  |  **Status**: FEED Frozen

### Executive Summary
[2-3 paragraphs: project objective, selected alternative, key cost/schedule/scope numbers, benchmark comparison, go/no-go recommendation]

### 1. Typical Project Configuration (Baseline Benchmark)
  1.1 Standard plant configuration and process design
  1.2 Plant cost curves -- typical CAPEX for this plant type/capacity
  1.3 Typical project duration (engineering, procurement, construction)
  1.4 Key equipment cost curves and typical delivery times

### 2. Market Analysis
  2.1 Price market analysis -- recent similar projects (last 3-5 years)
  2.2 Delivery time market analysis -- current equipment lead times vs typical

### 3. Specific Project Differences
  3.1 Site-specific differences vs typical assumptions
  3.2 Scope differences from standard configuration
  3.3 Cost impact of differences (location, scope, materials, market)
  3.4 Schedule impact of differences

### 4. Project Data Sheet
### 5. Requirements Register
### 6. Alternative Selection Summary (G0)
### 7. Design Summary (G1-G2)
### 8. Work Breakdown Structure
### 9. Procurement Strategy & Plan (long lead items highlighted)
### 10. Cost Estimate (trend from G1 through G3, with typical benchmark comparison)
### 11. Schedule (critical path, procurement dates, with typical duration comparison)
### 12. Constructability Assessment
### 13. Value Engineering Log
### 14. Risk Register
### 15. Quality Plan
### 16. Permits & Approvals Status
### 17. Design Freeze Verification Summary (six-dimension matrix)
### 18. Gate Decision (Go / No-Go / Recycle with conditions)
```

---

## Excel Workbook Generation

At each toll gate, generate the workbook using Python with openpyxl. Apply:
- **Header formatting**: Bold headers, frozen top row, auto-filter on data columns
- **Conditional formatting**: Red/Yellow/Green for risk levels, cost variances, permit status, benchmark deviations
- **Column widths**: Auto-sized to content
- **Cover sheet**: Project name, gate identifier, date, prepared by, AACE class, accuracy range
- **Consistent layout**: All workbooks follow the same formatting conventions

Use the Bash tool to execute Python code that creates the .xlsx files. Save workbooks to the current working directory.

## Notes

- If the user provides only partial information, proceed with what is available and flag assumptions prominently
- Currency defaults to EUR unless the user specifies otherwise
- For cost estimates, always state the AACE class and accuracy range
- **Typical configuration benchmarks (Step 1) must be established before any project-specific analysis begins**
- **All cost estimates and schedules must include comparison to the typical benchmark**
- **Market analysis (price and delivery time) informs contingency and procurement risk at every gate**
- Long lead items (>6 months) must always be identified and highlighted in the procurement plan
- Equipment cost curves and delivery time benchmarks must be cross-referenced with current market conditions
- The vendor pre-qualification trigger (< 3 qualified vendors on AVL) is a critical action item -- flag it prominently
- Vendor qualification refresh is recommended even for AVL-listed vendors during procurement
- Permits are often on the critical path -- always assess their impact on the schedule
- Temporary works (camp, excavation) require preliminary design at G1 and are a permit prerequisite
- Risk management is not a standalone exercise -- it is embedded at every gate
- At G3, the decision to freeze FEED is irrevocable without a formal change order process
