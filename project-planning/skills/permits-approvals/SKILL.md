---
name: permits-approvals
description: Permits and approvals for engineering and construction projects. Use when the user asks about permits, approvals, construction permit, environmental permit, EIA, fire permit, security permit, temporary works permit, building permit, planning permission, permit to work, camp, site establishment, excavation permit, zoning, regulatory approval, authority having jurisdiction.
---

# Permits & Approvals -- Engineering & Construction

## Overview

Permits are authorizations from governmental or regulatory authorities required before certain project activities can begin. They follow the design toll gate process but require external approvals the project team does not control -- making them a frequent critical path risk.

## Permit Types and Staging

| Permit | Typical Gate | Authority | Prerequisites | Typical Duration |
|--------|-------------|-----------|---------------|-----------------|
| **Environmental (EIA/ESIA)** | G0-G1 | Environmental agency | EIA study | 6-18 months |
| **Planning / Zoning** | G1 | Local planning authority | Conceptual design, site plan | 3-12 months |
| **Construction (Building)** | G2-G3 | Building authority | FEED design, structural calculations | 2-6 months |
| **Temporary Works** | G1-G2 | Local authority / site owner | Camp layout, excavation plan | 1-3 months |
| **Fire Safety** | G2 | Fire department | Fire protection design, egress plan | 1-4 months |
| **Security** | G2 | Security authority / client | Security plan, access control | 1-2 months |
| **Occupational Health** | G2 | Labor authority | HSE plan, welfare facilities | 1-2 months |
| **Electrical Connection** | G1-G2 | Grid operator | Load study, connection design | 3-12 months |
| **Water Discharge** | G1-G2 | Water authority | Discharge assessment | 3-6 months |

## Environmental Impact Assessment (EIA)

The EIA is often the longest-lead permit item:

1. **Screening**: Determine if EIA is required
2. **Scoping**: Define assessment scope (stakeholder consultation)
3. **Baseline studies**: Ecology, air, noise, water, soil, socio-economic
4. **Impact assessment**: Construction and operational phase impacts
5. **Mitigation measures**: Avoid, reduce, or offset impacts
6. **Public consultation**: Stakeholder engagement, public hearings
7. **Submission and review**: Authority processes the EIA report
8. **Decision**: Approved / conditional / rejected

**Timeline risk**: Baseline ecological surveys may be season-dependent (e.g., bird nesting in spring). Missing a season = 12-month delay.

## Temporary Works

Require preliminary design at G1 and detailed design by G2:

### Construction Camp
- **Accommodation**: Peak workforce x 1.2 margin
- **Offices**: PM, engineering, QA/QC, client, contractor
- **Canteen/kitchen**: Sized for peak workforce
- **Utilities**: Power, water, wastewater treatment, telecom
- **Waste management**: Domestic, construction, hazardous -- segregation and licensed disposal
- **Medical**: First aid, clinic (proportional to workforce and remoteness)
- **Recreation**: Sports, entertainment, prayer rooms
- **Security**: Perimeter fencing, gates, CCTV

### Excavation
- **Geotechnical survey**: Required before design
- **Excavation plan**: Cut/fill volumes, slope stability
- **Shoring**: Sheet piles, soldier piles, trench boxes for deep excavations
- **Dewatering**: Groundwater pumping if water table is high
- **Spoil management**: On-site reuse or off-site disposal
- **Existing utilities**: Underground services survey -- locate and protect

### Temporary Utilities
- Power: generators or temporary grid connection
- Water: municipal, borehole, or tanker delivery
- Drainage: stormwater management, silt fencing, settlement ponds
- Roads: compacted gravel or concrete panels for heavy transport

## Permit Tracking Register

| ID | Permit Type | Authority | Submitted | Expected Approval | Actual Approval | Status | Conditions | Responsible | Critical Path? |
|----|------------|-----------|----------|------------------|----------------|--------|-----------|-------------|---------------|
| PER-001 | [type] | [authority] | [date] | [date] | [date] | [status] | [list] | [name] | Yes/No |

### Status Definitions
- **Not Started**: Application not yet prepared
- **Pre-Application**: Informal discussions with authority
- **Submitted**: Formal application filed
- **Under Review**: Authority is processing
- **Additional Info Requested**: Authority needs more data
- **Approved**: Granted unconditionally
- **Conditional**: Granted with conditions
- **Rejected**: Denied (re-application or appeal needed)

## Permit-to-Gate Mapping

| Gate | Required Permits Status |
|------|------------------------|
| G0 | EIA screening confirms feasibility |
| G1 | EIA study commenced. Planning: pre-application discussions. |
| G2 | EIA submitted. Planning submitted. Temp works: design submitted. |
| G3 | Environmental: approved/conditional. Construction: submitted. Temp works: approved. Fire/security: submitted. |

## Critical Path Impact

Permits are often on the critical path because:
- Project team does not control approval timelines
- Authority review delayed by workload, politics, public opposition
- Missing prerequisites (seasonal surveys) cause 12-month delays
- Permit conditions may require design changes

**Schedule must include**: preparation durations, review durations (realistic, not optimistic), buffer for additional info requests, appeal process if rejection is a risk.

## Permit Conditions Management

1. Extract all conditions into dedicated register
2. Assign responsible person per condition
3. Define closure criteria and evidence
4. Track: open / in progress / closed / overdue
5. Report to authority as required
6. Non-compliance = stop-work orders or fines
