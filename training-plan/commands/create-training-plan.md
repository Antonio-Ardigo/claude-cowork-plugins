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

### Step 1.75: Principle Extraction

Before decomposing, identify the domain's **3-5 core principles**. This ensures sub-goals are principle-anchored, not topic-guessed.

| Principle | Statement | Formally | Prerequisites |
|-----------|-----------|---------|---------------|
| <name> | <one clear sentence> | <LaTeX or "—"> | <concepts the learner must already know> |

Rules:
- Order from most fundamental to most derived
- Each principle should be independently testable
- The Prerequisites column feeds Step 2.5 (Prerequisite Tracing)
- If the domain has fewer than 3 principles, it may be too narrow

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
- **Each Key Concept sub-goal MUST map to at least one principle** from Step 1.75. If a sub-goal doesn't trace to a principle, either the principle list is incomplete or the sub-goal is not load-bearing.
- Each sub-goal is a 15-word SMART statement
- Each sub-goal gets a domain label, difficulty, and depth level
- Difficulty is derived (not guessed): low = 1 principle + 0-1 prereq depth, medium = 2-3 principles + 2-3 prereq depth, high = 4+ principles or proofs/derivations required
- Depth level follows difficulty: low -> introductory, medium -> intermediate, high -> advanced
- Sequence: Motivation first -> Key Concepts (dependency order) -> Tools -> Verification last
- Total: typically 4-10+ sub-goals depending on complexity

### Step 2.5: Prerequisite Tracing

Build a prerequisite graph from the principles in Step 1.75:

```
<Goal> (core)
  requires:
    <External Prerequisite> (prerequisite) ← CHECK learner profile
  rests on:
    <Principle 1> (principle) → SG-X
      led to:
        <Principle 2> (principle) → SG-Y
```

Rules:
- **`requires`** = knowledge OUTSIDE this plan (external prerequisites). The learner must already know these.
- **`rests on`** = principles WITHIN this plan. These become hard sub-goal dependencies.
- **`led to`** = derived relationships. If Principle 2 builds on Principle 1, SG-Y depends on SG-X.
- If a `requires` prerequisite is NOT in the learner profile as a known strength, flag it as a WARNING in the plan.
- Every dependency in the Sequence must trace to a graph edge -- no intuited dependencies.

### Step 3: Design Session Blueprints

For each sub-goal, design a TTT session blueprint:

- **Initial Test**: A practical case the learner must solve immediately (no theory first). Describe the scenario and the task.
- **Pass Criteria**: Concrete, measurable threshold (e.g., "identifies 8 of 10 categories", "calculation within 5%")
- **Estimated Depth**: introductory / intermediate / advanced (derived from sub-goal difficulty)
- **Principle**: Which principle(s) from Step 1.75 this sub-goal tests
- **Anticipated CTQs**: 2-4 Critical-To-Quality criteria for this sub-goal. Each CTQ: what must be understood + mastery test + common failure mode (using CTQ failure mode taxonomy: conflation, overgeneralization, missing-prerequisite, procedural-without-conceptual, verbal-without-formal, formal-without-intuitive)
- **Teach Topics**: Key concepts, exercises, and known pitfalls with CTQ failure mode classification (e.g., "[conflation]: confusing indirect costs with contingency", "[procedural-without-conceptual]: applying formula without understanding boundary conditions")
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

## Principle Extraction

| Principle | Statement | Formally | Prerequisites |
|-----------|-----------|---------|---------------|
| <name> | <sentence> | <LaTeX or —> | <prior knowledge> |

## Sub-Goals

| # | Axis | Sub-Goal | Domain | Difficulty | Depth | Principle | Status | Score |
|---|------|----------|--------|-----------|-------|-----------|--------|-------|
| SG-1 | Motivation | <statement> | <domain> | <low/med/high> | <intro/inter/adv> | — | pending | - |
| SG-2 | Key Concept | <statement> | <domain> | <low/med/high> | <intro/inter/adv> | <principle> | pending | - |
| SG-3 | Key Concept | <statement> | <domain> | <low/med/high> | <intro/inter/adv> | <principle> | pending | - |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

## Prerequisite Graph

<Goal> (core)
  requires:
    <External> (prerequisite) ← CHECK learner profile
  rests on:
    <Principle> (principle) → SG-X
      led to:
        <Principle> (principle) → SG-Y

## Sequence
<dependency notes derived from prerequisite graph>

## Session Blueprints

### SG-1: <short title>
- **Initial Test:** <practical case description>
- **Pass Criteria:** <measurable threshold>
- **Estimated Depth:** <introductory/intermediate/advanced>
- **Principle:** <principle name or — for Motivation/Verification>
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | <what must be understood> | <concept> | <verification task> | <failure pattern> |
- **Teach Topics:** <concepts, exercises, pitfalls with CTQ failure mode tags>
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
- The principle extraction table
- The sub-goals table
- Any prerequisite warnings (external prerequisites not confirmed in learner profile)
- The suggested starting sub-goal
- Any learner profile notes that influenced the plan (if profile existed)
- Remind the user to run `/run-session SG-<N>` to start learning

## Important

- Do NOT include theory or teaching content in the plan -- that happens during `/run-session`
- Do NOT skip the session blueprint for any sub-goal
- Practical cases must be realistic scenarios, not abstract questions
- The `<topic>` in the filename should be a short kebab-case slug derived from the goal (e.g., `cost-estimation`, `python-data-analysis`)
- Every sub-goal dependency must trace to the prerequisite graph -- no intuited dependencies
