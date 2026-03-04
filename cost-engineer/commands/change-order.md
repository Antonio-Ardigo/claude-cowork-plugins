---
name: change-order
description: Evaluate a proposed change order for cost impact. Calculate direct costs, indirect costs, markups, and total change value.
allowed_tools:
  - Read
  - Glob
  - Grep
  - Bash
  - Task
---

# Change Order Evaluation

Evaluate a proposed change order and calculate its cost impact. If the user provides a file or description, work from that. Otherwise, ask for the change details.

## Step 1: Understand the Change

Gather or extract:
- **Description** of what is changing
- **Reason** (owner-directed, design error, site conditions, regulatory, etc.)
- **Scope** — work added and work deleted (if any)
- **Contract type** (lump sum, unit rate, cost-reimbursable)
- **Contract-specified markup rates** (if known)

## Step 2: Calculate Direct Costs

Break down by category:

**Labor:**
- Identify trades required and estimated manhours per trade
- Apply labor rates (use contract rates if specified, otherwise regional rates)
- Apply productivity factors if applicable (climate, overtime, congestion)

**Materials:**
- List materials required with quantities and unit prices
- Add freight allowance
- Add waste/damage allowance (typically 3–10%)

**Equipment (construction plant):**
- Identify required equipment and duration
- Apply hourly/daily rates
- Include mobilization/demobilization if equipment not on site

**Subcontracts:**
- Include subcontractor quotations if available
- Identify markup applicability per contract terms

Present in a clear table.

## Step 3: Calculate Indirect Costs

If the change extends the project duration:
- **Estimate additional days on the critical path** (ask the user if not clear)
- **Calculate extended general conditions:** daily indirect rate × additional days
- **Calculate extended home office costs** if applicable

If the change does NOT extend the project: state that no indirect cost impact applies and explain why.

## Step 4: Apply Markups

Apply markups sequentially per contract terms:
1. Overhead % on (direct + indirect costs)
2. Profit % on subtotal
3. Bond premium % on subtotal
4. Insurance % on subtotal

If contract rates are not specified, use typical rates and note that they should be verified against the contract.

Show the calculation step by step.

## Step 5: Reasonableness Check

Verify the pricing:
- Is the cost/manhour consistent with contract rates?
- Are material prices consistent with recent market data?
- Is the indirect-to-direct ratio reasonable?
- Does the total cost per unit of work compare favorably with benchmarks?

Flag anything that looks unreasonable.

## Step 6: Deliver Evaluation

Present the change order evaluation using the standard pricing format:

1. **Change Description & Reason**
2. **Direct Cost Breakdown** (labor, materials, equipment, subcontracts)
3. **Indirect Cost Impact** (extended general conditions, home office)
4. **Markups** (overhead, profit, bond, insurance)
5. **Total Change Order Value**
6. **Schedule Impact** (days on critical path, if applicable)
7. **Reasonableness Assessment**
8. **Recommendation** — approve as-is, negotiate specific items, or request additional backup
