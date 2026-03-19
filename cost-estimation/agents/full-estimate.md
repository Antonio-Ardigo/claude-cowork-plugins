---
name: full-estimate
description: Autonomous agent that produces a complete cost estimation package end-to-end from a scope brief
tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep", "Agent"]
---

# Full Estimate Agent

## Purpose
Autonomously produces a complete cost estimation package from a scope brief without user intervention.

## When to Use
- User provides a scope brief (e.g., "estimate a 100,000 m3 rectangular RC water tank in Saudi Arabia")
- User wants complete deliverables without step-by-step interaction

## Workflow
1. **Parse scope**: Extract structure type, volume, location, design code
2. **Design assumptions**: Load geometry reference, extract dimensions
3. **Quantity takeoff**: Calculate all quantities from geometry
4. **Market rates**: Load appropriate market-*.md
5. **Productivity**: Apply climate factors for location
6. **BOQ**: Build 14-section bill of quantities
7. **Duration**: Calculate from quantities and productivity
8. **Schedule**: Activity list with dependencies, critical path
9. **Resources**: Weekly headcount histogram
10. **Risk**: Risk register + sensitivity on top-5 items
11. **XLSX**: Generate 18-sheet workbook with formulas and charts
12. **Sketches**: Generate 4 engineering sketch PNGs, embed in Drawings
13. **Executive Summary DOCX**: Project overview, costs, schedule, risks
14. **Audit Report DOCX**: Self-audit with formula check + rate verification
15. **QC**: Run 10-point audit checklist, fix any findings
16. **Report**: Summary of outputs and key findings

## Inputs
- Scope brief (natural language)
- Optional: specific parameters, market overrides, custom rates

## Outputs
- XLSX workbook (18+ sheets with charts)
- Executive Summary DOCX
- Audit Report DOCX
- 4 engineering sketch PNGs
