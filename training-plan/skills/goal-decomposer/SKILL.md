---
description: "Learning goal decomposition into SMART sub-goals. Use when the user asks to create a training plan, break down a learning goal, decompose objectives, define sub-goals, structure a learning path from a high-level goal, or identify what sub-topics need to be learned for a given goal."
---

# Goal Decomposer — Domain Knowledge

Reference knowledge for decomposing a learning goal into structured, testable sub-goals.

## What This Skill Does

Takes a free-form learning goal and produces:

1. A refined **SMART Goal** (max 15 words)
2. **N sub-goals** decomposed across 4 axes
3. A suggested **sequence** with dependencies

## The 4 Decomposition Axes

| Axis | Purpose | Typical Count | Position in Sequence |
|------|---------|---------------|---------------------|
| **Motivation** | Why this matters. Engagement, relevance, real-world impact. | 1 (sometimes 2) | First — sets context |
| **Key Concepts** | Foundational knowledge. Theory, definitions, principles. | **As many as the domain requires** (2-8+) | Middle — bulk of learning |
| **Tools** | Practical techniques, frameworks, software, resources. | 0-3 (only if tooling is relevant) | After concepts that require them |
| **Verification** | Integrative proof of mastery. Combines multiple concepts. | 1-2 | Last — capstone |

### Critical Rule: Sub-Goal Expansion

The axes are **decomposition directions**, NOT fixed slots. Specifically:

- **Key Concepts MUST expand** into as many sub-goals as the domain requires. A simple goal may have 2 Key Concept sub-goals; a complex goal may have 8+.
- Each Key Concept sub-goal covers **one testable idea** — if a concept has multiple independent parts, split it.
- Motivation and Verification typically have 1 sub-goal each, but can have more.
- Tools sub-goals exist ONLY if the goal involves specific tooling (software, frameworks, instruments).

## SMART Statement Format

Each sub-goal is expressed as a 15-word SMART statement:

- **Specific**: names the exact competency
- **Measurable**: implies an observable outcome
- **Achievable**: scoped to one learning unit
- **Relevant**: clearly connected to the main goal
- **Time-bound**: implicitly — each is a single TTT session

### Examples

Good: `"Identify and classify all cost components in an EPC project estimate accurately"`
Good: `"Apply unit-rate estimation to civil quantities with less than 5% calculation error"`
Bad: `"Understand cost estimation"` (too vague, not measurable)
Bad: `"Learn everything about piping, structural, and electrical estimation"` (too broad — split into separate sub-goals)

## Output Format

When decomposing a goal, produce this structure:

```markdown
## SMART Goal
<15-word refined statement>

## Sub-Goals

| # | Axis | Sub-Goal | Domain | Difficulty |
|---|------|----------|--------|------------|
| SG-1 | Motivation | <15-word statement> | <domain label> | low/medium/high |
| SG-2 | Key Concept | <15-word statement> | <domain label> | low/medium/high |
| SG-3 | Key Concept | <15-word statement> | <domain label> | low/medium/high |
| ... | ... | ... | ... | ... |
| SG-N | Verification | <15-word statement> | <domain label> | high |

## Sequence
- SG-1 has no prerequisites
- SG-2 requires SG-1
- SG-3 requires SG-2
- SG-4 can run in parallel with SG-3
- ...
- SG-N requires all previous sub-goals
```

## Sequencing Rules

1. **Motivation first** — always. Brief, but sets the "why."
2. **Key Concepts ordered by dependency** — foundational before advanced. If concept B requires understanding concept A, A comes first.
3. **Independent concepts can be parallel** — if two Key Concept sub-goals don't depend on each other, note that in the sequence.
4. **Tools after the concepts they serve** — don't teach the tool before the learner understands what it does.
5. **Verification last** — it integrates everything. Always depends on all prior sub-goals.

## Testability Check

Before finalizing, verify each sub-goal passes this check:

> "Can I design a practical case (scenario, exercise, or problem) that a competent person could solve, and that would FAIL if the specific knowledge in this sub-goal is missing?"

If yes → good sub-goal.
If no → too vague, too broad, or not independently testable. Refine or split.
