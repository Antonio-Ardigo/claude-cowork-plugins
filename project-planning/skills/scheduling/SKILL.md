---
name: scheduling
description: Project scheduling for engineering and construction. Use when the user asks about CPM, critical path, scheduling, Gantt, float, lead time, lag, fast tracking, crashing, resource loading, procurement-driven schedule, long lead items, construction sequence, milestone chart, level 1 schedule, PERT, schedule risk, phase overlap.
---

# Project Scheduling -- Engineering & Construction

## Critical Path Method (CPM)

### Key Concepts
- **Activity**: A discrete unit of work with a defined duration
- **Dependency types**:
  - FS (Finish-to-Start): B starts after A finishes (most common)
  - SS (Start-to-Start): B starts when A starts
  - FF (Finish-to-Finish): B finishes when A finishes
  - SF (Start-to-Finish): B finishes when A starts (rare)
- **Lead**: Overlap between dependent activities (negative lag)
- **Lag**: Delay between dependent activities (positive lag)
- **Float (Total Float)**: Time an activity can slip without delaying the project end date
- **Free Float**: Time an activity can slip without delaying any successor
- **Critical Path**: The longest path through the network -- zero total float

### Forward / Backward Pass
1. **Forward pass**: Calculate Early Start (ES) and Early Finish (EF) for each activity
2. **Backward pass**: Calculate Late Start (LS) and Late Finish (LF) working backward from project end
3. **Total Float** = LS - ES = LF - EF
4. Activities with Float = 0 are on the critical path

## Procurement-Driven Scheduling

In EPC projects, the schedule is often driven by procurement, not engineering:

### Long Lead Items
Equipment with manufacturing + delivery times > 6 months:
- Gas turbines (12-18 months)
- Large transformers (10-14 months)
- Pressure vessels / reactors (8-14 months)
- Compressors (10-16 months)
- Large pumps (6-10 months)
- Switchgear (8-12 months)

### Scheduling Logic
1. **Construction need date** determines when equipment must arrive on site
2. **Delivery lead time** determines when PO must be placed
3. **Procurement cycle** (RFQ, evaluation, negotiation, PO) adds 2-4 months before manufacturing
4. **Spec readiness date** determines when engineering must complete the specification
5. **Engineering sequence is adjusted** to produce specs for long lead items FIRST

## Schedule Hierarchy

| Level | Name | Detail | Audience |
|-------|------|--------|----------|
| Level 1 | Master Milestone Schedule | Key milestones only (10-20 items) | Executive / Client |
| Level 2 | Summary Schedule | Phase-level activities (50-100 items) | Project Management |
| Level 3 | Control Schedule | Work package level (500-2000 items) | Project Controls |
| Level 4 | Detailed / Execution Schedule | Task-level detail (2000+ items) | Discipline Leads |

## Fast-Tracking vs Crashing

### Fast-Tracking
- Performing activities in parallel that were originally planned sequentially
- Risk: Rework if upstream activity changes affect downstream work

### Crashing
- Adding resources to reduce activity duration
- Risk: Diminishing returns, increased cost, fatigue, quality issues

## Phase Overlap (Concurrent Engineering)

In EPC projects, engineering-procurement-construction phases overlap:
- Engineering starts first but continues into procurement and construction
- Procurement begins once first specifications are ready (long lead items)
- Construction begins once first IFC drawings and materials are available
- More overlap = shorter schedule but more rework risk

## Resource Loading and Leveling

### Resource Loading
- Assign manhours/headcount to each activity
- Generate resource histograms (people over time)
- Identify peak resource requirements

### Resource Leveling
- Smooth resource peaks by shifting non-critical activities within their float
- Critical path activities cannot be shifted -- may require crashing instead

## Key Milestones for EPC Projects

| Milestone | Abbreviation | Meaning |
|-----------|-------------|---------|
| Final Investment Decision | FID | Client authorizes full project spend |
| FEED Complete | -- | Basic design approved, design freeze |
| First Steel | -- | Structural steel erection begins |
| Mechanical Completion | MC | All equipment and piping installed and tested |
| Ready for Start-Up | RFSU | Systems handed over to commissioning |
| Provisional Acceptance Certificate | PAC | Performance test passed, plant accepted |
| Final Acceptance Certificate | FAC | Warranty period complete, final handover |

## Schedule Risk Analysis

### PERT
- Three-point estimates: Optimistic (O), Most Likely (M), Pessimistic (P)
- Expected duration = (O + 4M + P) / 6
- Standard deviation = (P - O) / 6

### Monte Carlo Simulation
- Assign probability distributions to activity durations
- Run 1000+ simulations to generate probability distribution of project completion
- Output: P50, P80, P90 dates
- Identifies which activities contribute most to schedule risk
