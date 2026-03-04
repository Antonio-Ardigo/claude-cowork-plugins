---
name: analyze-estimate
description: Read a cost estimate file (Excel .xlsx) and check for gaps, outliers, consistency, and completeness against AACE standards.
allowed_tools:
  - Read
  - Glob
  - Grep
  - Bash
  - Task
---

# Analyze Cost Estimate

Analyze a cost estimate file provided by the user. If no file path is given, ask for it.

## Step 1: Read the File

Read the Excel file using the available tools. Identify all sheets and their purpose (summary, detail, backup, assumptions).

## Step 2: Identify Estimate Structure

Determine:
- Estimate class (Class 1–5 per AACE 18R-97) based on level of detail and project phase
- Cost Breakdown Structure (CBS) used
- Whether the estimate covers direct costs, indirect costs, contingency, and escalation
- Base date and currency

## Step 3: Completeness Check

Check against standard CBS categories:

**Direct Costs — verify presence of:**
- Process equipment (purchased/delivered)
- Bulk materials (piping, electrical, instrumentation, structural, civil)
- Direct construction labor
- Subcontracts

**Indirect Costs — verify presence of:**
- Construction indirects (supervision, temp facilities, QC, HSE)
- Home office costs (engineering, procurement, PM)
- Freight and logistics
- Vendor representatives

**Other Costs — verify presence of:**
- Owner's costs
- Contingency (with basis stated)
- Escalation allowance (if estimate spans >12 months)

Flag any missing categories as gaps.

## Step 4: Outlier Detection

For each major cost category:
- Calculate the percentage of total installed cost (TIC)
- Compare against typical ranges for the project type
- Flag any category that is significantly above or below the expected range

Typical ranges for process plants:
- Equipment: 15–30% of TIC
- Piping: 8–15%
- Electrical: 5–10%
- Instrumentation: 6–12%
- Civil/structural: 8–15%
- Construction labor: 15–25%
- Engineering: 8–15%
- Contingency: 5–30% (depending on class)

## Step 5: Consistency Checks

- Verify unit rates are consistent across similar items
- Check that labor rates match the stated location and year
- Verify escalation assumptions are reasonable and consistently applied
- Check that contingency is appropriate for the stated estimate class
- Verify quantities are plausible (cross-check major items against capacity/scope)

## Step 6: Present Findings

Deliver a structured report:

1. **Estimate Summary** — class, base date, currency, total value, scope description
2. **CBS Breakdown** — table showing each category, its value, and % of TIC
3. **Completeness Assessment** — missing categories or underdeveloped areas
4. **Outliers** — items outside expected ranges with explanation
5. **Consistency Issues** — any internal inconsistencies found
6. **Contingency Assessment** — is contingency appropriate for the estimate class?
7. **Recommendations** — prioritized list of items to address to improve estimate quality

Rate the overall estimate quality as: **Well-developed**, **Adequate**, **Needs improvement**, or **Significant gaps**.
