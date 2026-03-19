---
description: Generate a construction method statement for a specific activity
argument-hint: "<activity> [--project <context>] [--climate hot|temperate|cold]"
---

# /method-statement -- Construction Method Statement Generator

## Overview
Generates a professional method statement DOCX for a specific construction activity.

## Invocation
```
/method-statement "concrete placement walls" --project "100000m3 RC tank" --climate hot
/method-statement "earthworks excavation"
/method-statement "hydrostatic testing"
```

## Workflow
1. Load construction-methods references for the activity
2. Tailor to project specifics and climate
3. Generate DOCX with sections:
   - Scope of Work
   - Resources (labor, equipment, materials)
   - Procedure (step-by-step)
   - Quality Control
   - Health & Safety
   - Environmental Considerations
   - References

## Output
- Method statement DOCX
