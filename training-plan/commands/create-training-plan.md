---
name: create-training-plan
description: Create a customized training plan from a learning goal using Test-Teach-Test methodology
allowed_tools:
  - Read
  - Write
  - Edit
  - Glob
---

You are creating a customized training plan using the **Test-Teach-Test (TTT)** methodology.

The user wants to learn: **$ARGUMENTS**

## Your Task

Generate a complete training plan by following these steps in order:

### Step 1: Refine the Goal

Take the user's input and refine it into a **SMART Goal** (max 15 words):
- Specific: names the exact competency
- Measurable: implies an observable outcome
- Achievable: realistic scope
- Relevant: aligned with the user's intent
- Time-bound: includes a timeframe if the user mentioned one

### Step 1.5: Check Learner Profile

Use Glob to look for `learner_profile.md` in the current directory.

If found, read it and note:
- **Known strengths**: Topics the learner has mastered (passed Initial Test with zero gaps). If any relate to this new goal, plan harder initial tests for those sub-goals.
- **Gap patterns**: Recurring weaknesses. If any relate to this new goal, note them in the Teach Topics of relevant session blueprints so they get proactive coverage.

If no profile exists, proceed normally. The profile will be created after the first /run-session.

Pass these notes forward to Step 3 (Design Session Blueprints) so the blueprints reflect what is already known about the learner.

### Step 2: Decompose into Sub-Goals

Break the SMART goal into **N sub-goals** across 4 axes:

| Axis | Purpose | Count |
|------|---------|-------|
| Motivation | Why this matters | 1+ |
| Key Concepts | Foundational knowledge | **As many as the domain requires** |
| Tools | Practical techniques/frameworks | 0+ (only if relevant) |
| Verification | Proof of mastery | 1+ |

Rules:
- Key Concepts MUST expand -- each covers ONE testable idea
- Each sub-goal is a 15-word SMART statement
- Each sub-goal gets a domain label and difficulty (low/medium/high)
- Sequence: Motivation first -> Key Concepts (dependency order) -> Tools -> Verification last
- Total: typically 4-10+ sub-goals depending on complexity

### Step 3: Design Session Blueprints

For each sub-goal, design a TTT session blueprint:

- **Initial Test**: A practical case the learner must solve immediately (no theory first). Describe the scenario and the task.
- **Pass Criteria**: Concrete, measurable threshold (e.g., "identifies 8 of 10 categories", "calculation within 5%")
- **Teach Topics**: Key concepts, exercises, and known pitfalls/misconceptions to address if gaps are found
- **Final Test**: A DIFFERENT practical case testing the same competencies

If the learner profile indicated strengths or gap patterns relevant to a sub-goal, note them in the blueprint:
- **Profile note (strength):** "Learner has prior mastery in [topic] -- set Initial Test at elevated difficulty"
- **Profile note (gap pattern):** "Learner has recurring gap in [pattern] -- include proactive Quick Check in Teach Topics even if not identified in Initial Test"

### Step 4: Write the Plan File

Use the Write tool to create `<topic>_training_plan.md` in the current directory. Use this exact format:

```markdown
# Training Plan: <Title>
Generated: <date> | Status: in-progress

## Learning Goal
<User's original input>

## SMART Goal
<15-word refined statement>

## Sub-Goals

| # | Axis | Sub-Goal | Domain | Status | Score |
|---|------|----------|--------|--------|-------|
| SG-1 | Motivation | <statement> | <domain> | pending | - |
| SG-2 | Key Concept | <statement> | <domain> | pending | - |
| SG-3 | Key Concept | <statement> | <domain> | pending | - |
| ... | ... | ... | ... | ... | ... |

## Sequence
<dependency notes: which sub-goals must come before others>

## Session Blueprints

### SG-1: <short title>
- **Initial Test:** <practical case description>
- **Pass Criteria:** <measurable threshold>
- **Teach Topics:** <concepts, exercises, pitfalls>
- **Final Test:** <different case, same competencies>

### SG-2: <short title>
...

(repeat for every sub-goal)

## Progress Log
(updated by /run-session)
```

### Step 5: Confirm to the User

After writing the file, present a summary:
- The SMART goal
- The sub-goals table
- The suggested starting sub-goal
- Any learner profile notes that influenced the plan (if profile existed)
- Remind the user to run `/run-session SG-<N>` to start learning

## Important

- Do NOT include theory or teaching content in the plan -- that happens during `/run-session`
- Do NOT skip the session blueprint for any sub-goal
- Practical cases must be realistic scenarios, not abstract questions
- The `<topic>` in the filename should be a short kebab-case slug derived from the goal (e.g., `cost-estimation`, `python-data-analysis`)
