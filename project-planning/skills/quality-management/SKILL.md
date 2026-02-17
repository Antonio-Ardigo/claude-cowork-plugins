---
name: quality-management
description: Quality management for engineering and construction projects. Use when the user asks about quality management, QA/QC, quality assurance, quality control, inspection test plan, ITP, hold point, witness point, commissioning, performance test, acceptance criteria, ISO 9001, punch list, quality plan, surveillance, NDE, non-destructive examination.
---

# Quality Management -- Engineering & Construction

## QA vs QC

| Aspect | Quality Assurance (QA) | Quality Control (QC) |
|--------|----------------------|---------------------|
| Focus | Prevention | Detection |
| When | Before and during work | During and after work |
| How | Processes, procedures, audits | Inspections, tests, measurements |
| Output | Quality plan, procedures | Test reports, inspection records |

## Quality Management Plan Structure

1. Quality policy and objectives
2. Organization and responsibilities
3. Applicable codes and standards matrix
4. Inspection and test plans (ITP)
5. Procedures (welding, NDE, concrete, coating)
6. Document control
7. Non-conformance management (NCR process)
8. Audit program
9. Training and qualification
10. Records and traceability

## Inspection and Test Plans (ITP)

### Inspection Types

| Type | Code | Meaning |
|------|------|---------|
| **Hold Point** | H | Work STOPS until inspector verifies and signs off |
| **Witness Point** | W | Inspector notified and invited; work may proceed if not attended |
| **Review Point** | R | Documents reviewed; work may proceed |
| **Surveillance** | S | Random or periodic monitoring |

### ITP Format

| Item | Activity | Acceptance Criteria | Code | Contractor | Client | Third Party | Records |
|------|----------|-------------------|------|-----------|--------|------------|---------|
| 1 | Foundation pour | Slump, strength, cover | ACI 318 | H | W | W | Cube test |
| 2 | Steel welding | Visual + UT | AWS D1.1 | H | W | H | UT report |
| 3 | Hydrostatic test | No leaks at test pressure | ASME B31.3 | H | H | W | Test cert |
| 4 | Cable termination | Megger, continuity | IEC 60502 | H | W | S | Test sheet |

## Codes and Standards Hierarchy

1. **International**: ISO, IEC, ASME, API, AWS, ASTM
2. **National**: BS (UK), DIN (Germany), NF (France), UNI (Italy)
3. **Industry**: NFPA (fire), NACE (corrosion), PED (pressure equipment)
4. **Project-specific**: Client specifications, project standards
5. In case of conflict, more stringent requirement governs

## Commissioning Sequence

### Pre-commissioning
- Mechanical completion verification
- System cleaning and flushing
- Leak testing (pneumatic, hydrostatic)
- Electrical continuity and insulation testing
- Loop checks, cable megger testing

### Commissioning
- Energization (electrical systems)
- Utility systems startup
- Individual equipment testing
- System-by-system startup
- Integrated system testing

### Performance Testing
- Plant operation at design conditions
- Performance guarantee verification (capacity, efficiency, emissions)
- Duration per contract (typically 72h continuous or 30 days cumulative)

### Handover
- PAC upon passing performance test
- Punch list classification:
  - **Category A**: Prevents safe operation -- must close before PAC
  - **Category B**: Does not prevent operation -- close within agreed timeframe
  - **Category C**: Minor / cosmetic -- close during warranty period
- FAC after warranty period and all punch items closed

## Performance Guarantee Testing

| Parameter | Guaranteed Value | Test Method | Duration | Acceptance |
|-----------|-----------------|------------|----------|-----------|
| Output | [value + unit] | Direct measurement | [hours] | >= guaranteed |
| Efficiency | [%] | Input/output | [hours] | >= guaranteed |
| Emissions | [mg/Nm3] | Stack test | [hours] | <= limit |
| Noise | [dB(A)] | Sound level survey | [hours] | <= limit |
| Availability | [%] | Operational record | [days] | >= guaranteed |
