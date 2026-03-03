---
description: "Concept explanation methodology for TTT sessions. Use when generating teaching content during the Teach phase, when a learner requests a deep-dive into a taught principle, when gaps involve distinguishing two concepts (comparison), or when generating concept maps and CTQ mastery criteria."
---

# Concept Explainer -- Domain Knowledge

Reference knowledge for generating rich, principle-first concept explanations within TTT sessions. Replaces simple teaching blocks with structured concept breakdowns when appropriate, while preserving the gap-driven, one-at-a-time delivery model of TTT.

## The 6-Section Concept Explanation Structure

Every concept explanation follows this structure. Sections may be abbreviated or omitted based on the adaptive depth logic below.

### Section 1: The Problem

What observation, need, or contradiction made this concept necessary?

- What was broken, paradoxical, or limiting?
- What did people try before, and why did it fail?
- What was at stake -- practical, theoretical, or both?

Write 1-3 paragraphs in plain language. The learner should feel the tension the concept resolves.

**Within TTT**: Frame the problem in terms of the learner's gap. "You got this wrong because [gap]. Here's why that matters..."

### Section 2: Core Principles (3-5 principles)

For each principle:

```markdown
### Principle N: [Name]
**Statement**: [One clear sentence]
**Formally**: $$[LaTeX equation]$$
**Example**: [Concrete, vivid illustration]
```

Order from most fundamental to most derived. At `introductory` level, omit the **Formally** line.

### Section 3: Key Innovations (2-4 innovations)

```markdown
### [Innovation Name] ([Person/Group], [Year/Era])
**What**: [What was introduced or discovered]
**Why it mattered**: [What problem it solved, what it unlocked]
**Example**: [Concrete worked illustration]
```

Order chronologically or by logical dependency.

### Section 4: Intuitive Formalization

NOT the most general form -- minimum math needed to make predictions.

```markdown
### Starting Point
[The simplest mathematical statement, with all terms defined]

### Building Up
[Step-by-step development, each step grounded in earlier examples]

### Key Equations
| Name | Equation | What it tells you |
|------|----------|-------------------|
| [name] | $[LaTeX]$ | [plain-language meaning] |
```

At `introductory` level, this section is a brief paragraph with minimal notation.

### Section 5: CTQ Mapping

```markdown
| CTQ | Source | Mastery Test | Common Failure Mode |
|-----|--------|-------------|---------------------|
| [specific understanding] | Principle N / Innovation N | [question or task] | [failure pattern] |
```

See the CTQ Derivation Method and Failure Mode Taxonomy below for how to populate this table.

### Section 6: Conceptual Map

Markdown nested-list visualization of the concept's structure. See the Concept Map Format section below.

---

## Depth Levels

| Level | Math | Principles | Innovations | CTQ |
|-------|------|-----------|------------|-----|
| **introductory** | Minimal notation, intuition-first | 3, plain-language statements only | 2, brief | Short table (2-3 rows) |
| **intermediate** | Full LaTeX throughout | 3-5 with full LaTeX formalization | 2-4 with worked examples | Full table with mastery tests |
| **advanced** | Proofs, edge cases, competing forms | 5 with derivations and proofs | 4 with detailed proofs | Advanced failure modes + edge cases |

Default within TTT sessions: **intermediate**.

---

## Adaptive Teaching: When to Use What

### Abbreviated Concept Explanation (for simple gaps)

When a gap is narrow, concrete, and does not involve deep conceptual misunderstanding:

```markdown
---

**The Problem**
<1-2 sentences: why this gap matters, framed in the learner's context>

**Core Principles**
<1-2 principles, plain language, no LaTeX>

**Quick Check** (CTQ: [source principle])
<CTQ-derived verification question>
(Expected answer: <answer>)
(Watch for: <failure mode>)

---
```

Total length: comparable to the old 6-part teaching block.

### Full Concept Explanation (for complex gaps)

When a gap involves conceptual confusion, wrong mental models, or multi-layered misunderstanding, deliver all 6 sections at the appropriate depth level.

### Concept Comparison (for conflation gaps)

When the gap involves confusing two related concepts, use the comparison format (see Concept Comparison Protocol below) instead of a standard explanation.

### Decision Criteria

A gap is **complex** if ANY of these apply:

1. The gap matches a CTQ failure mode pattern (conflation, overgeneralization, missing prerequisite, procedural-without-conceptual)
2. The gap is flagged as a persistent pattern in the learner profile (2+ occurrences)
3. The gap involves a prerequisite the learner is missing
4. The gap was a "verbal-without-formal" or "formal-without-intuitive" failure

A gap is a **conflation** specifically if the learner confused two related but distinct concepts.

Otherwise, the gap is **simple** -- use the abbreviated form.

---

## LaTeX Conventions

All mathematical expressions use LaTeX notation:

- Inline: `$...$`
- Display (centered, separate line): `$$...$$`
- Variables in prose: `$x$`, `$\theta$`, `$\mathbf{v}$`

**Standard notation reference:**

| Category | Notation |
|----------|----------|
| Vectors | `$\mathbf{v}$`, `$\vec{x}$` |
| Matrices | `$\mathbf{A}$`, `\begin{pmatrix}...\end{pmatrix}` |
| Partial derivatives | `$\frac{\partial f}{\partial x}$` |
| Integrals | `$\int_a^b f(x)\,dx$` |
| Summations | `$\sum_{i=1}^{n}$` |
| Greek letters | `$\alpha$`, `$\beta$`, `$\theta$`, `$\lambda$` |
| Set notation | `$\in$`, `$\subset$`, `$\cup$`, `$\cap$` |
| Probability | `$P(A|B)$`, `$\mathbb{E}[X]$` |
| Norms | `$\|x\|$`, `$\|A\|_F$` |

At `introductory` level, use minimal notation and explain every symbol on first use.

---

## CTQ Derivation Method

CTQ (Critical-To-Quality) criteria define what the learner MUST understand to claim mastery. They are verifiable -- not topics to study, but criteria to meet.

**Good CTQ**: "Can derive the relationship between entropy and the number of microstates"
**Bad CTQ**: "Understand entropy" (too vague, not verifiable)

### Step 1: Trace from Principles

| Principle | -> | CTQ |
|-----------|-----|-----|
| Energy is conserved | -> | Can track energy transformations across heat, work, and internal energy in a closed system |
| Direct vs indirect costs | -> | Can classify any project cost line item as direct or indirect with justification |

### Step 2: Trace from Innovations

| Innovation | -> | CTQ |
|-----------|-----|-----|
| Boltzmann's $S = k_B \ln W$ | -> | Can calculate entropy from microstate counting for a simple system |
| Earned Value Method | -> | Can compute CPI and SPI from BCWP, BCWS, and ACWP |

### Step 3: Identify Failure Modes

For each CTQ, identify the most likely way a learner will fail it. See the Failure Mode Taxonomy below.

---

## CTQ Failure Mode Taxonomy

| Failure Pattern | Description | Example |
|----------------|-------------|---------|
| **Conflation** | Mixing up two related but distinct concepts | Confusing indirect costs with contingency |
| **Overgeneralization** | Applying a principle beyond its valid domain | Assuming all nested loops are $O(n^k)$ |
| **Missing prerequisite** | Lacking foundational understanding needed for this concept | Cannot classify costs because unfamiliar with WBS |
| **Procedural without conceptual** | Can follow steps but cannot explain why they work | Applies the formula correctly but cannot explain when it breaks |
| **Verbal without formal** | Can describe in words but cannot write the equation | Explains entropy conceptually but cannot write $S = k_B \ln W$ |
| **Formal without intuitive** | Can manipulate symbols but cannot explain what results mean | Solves the integral but cannot interpret the physical meaning |

When identifying gaps in the EVALUATE phase, classify each gap using this taxonomy:
- "Gap [conflation]: confused indirect costs with contingency"
- "Gap [procedural-without-conceptual]: applied formula correctly but cannot explain why it works"

---

## CTQ-Enhanced Quick Check Design

Quick Checks are now derived from CTQ mastery tests:

```markdown
**Quick Check** (CTQ: [source principle or innovation])
[Question from the CTQ's Mastery Test column]
(Expected answer: [answer])
(Watch for: [failure mode pattern from CTQ table])
```

The Quick Check question comes directly from the CTQ table's "Mastery Test" column. The "Watch for" line alerts the evaluator to the most likely failure mode for this specific check.

---

## Concept Comparison Protocol

Triggered when a gap is classified as **conflation** -- the learner confused two related but distinct concepts.

### Format

```markdown
---

## [Concept A] vs [Concept B]

### What They Share
| Shared Principle | In [Concept A] | In [Concept B] |
|-----------------|----------------|----------------|
| [principle] | [how it manifests] | [how it manifests] |

### Where They Diverge
| Dimension | [Concept A] | [Concept B] |
|-----------|-------------|-------------|
| Core assumption | [what A assumes] | [what B assumes] |
| Primary strength | [where A excels] | [where B excels] |
| Typical use case | [when to use A] | [when to use B] |

### CTQ: The Critical Distinction
| CTQ | Mastery Test | Failure Mode |
|-----|-------------|-------------|
| Can distinguish [A] from [B] in [context] | [specific test] | Conflation: [specific confusion] |

**Quick Check** (CTQ: distinction)
[Question that specifically tests the A vs B distinction]
(Expected answer: [answer])
(Watch for: conflation -- [specific confusion to watch for])

---
```

### When to Use

Use instead of a standard teaching block when:
- The gap is classified as [conflation]
- The learner explicitly confused two specific concepts
- The evaluation identified "confused X with Y" as a gap

---

## Deep-Dive Protocol

During a TTT session, the learner may request deeper explanation of a principle just taught.

### How It Works

1. Identify the principle or innovation to expand (from the most recent teaching block or concept map)
2. Generate a full 6-section explanation for that specific principle, at the session's depth level
3. Frame Section 1 (The Problem) in context of the parent concept: "Within [parent concept], [this principle] matters because..."
4. Deliver the deep-dive inline -- it does NOT interrupt the session
5. After the deep-dive, return to the TTT flow (next gap, or Phase 3.5 if all gaps done)

### Rules

- Deep-dives are offered, never forced: mention the option once after the first teaching block
- Only one deep-dive per teaching block (prevent rabbit holes)
- The deep-dive is included in the session transcript and concept file
- Deep-dives can chain: a deep-dive may reveal new principles the learner can further explore

---

## Concept Map Format

### Node Types

| Type | Meaning | Usage |
|------|---------|-------|
| **(core)** | Central concept being mapped | Exactly one per map |
| **(principle)** | Foundational truth or constraint | The 3-5 load-bearing ideas |
| **(innovation)** | Conceptual breakthrough or key contribution | Creative leaps that built the concept |
| **(application)** | Practical use or derived concept | Where theory meets reality |
| **(prerequisite)** | Required prior knowledge | What you need before this concept |
| **(shared)** | Common to both concepts in a comparison | Only used in comparison maps |

### Relationship Labels

| Label | Meaning | Direction |
|-------|---------|-----------|
| `rests on` | Built on these principles | core -> principle |
| `requires` | Needs these prerequisites | core -> prerequisite |
| `led to` | Produced these innovations | principle -> innovation |
| `enables` | Enables these applications | innovation -> application |
| `generalizes` | Generalization of the child | parent -> child |
| `is a special case of` | Specialization | child -> parent |
| `contrasts with` | In tension or opposition | sibling <-> sibling |
| `equivalent to` | Different formulations of same idea | sibling <-> sibling |

### Structure

```markdown
## Concept Map: [Topic]

- **[Topic]** (core): [one-line description]
  - requires:
    - **[Prerequisite]** (prerequisite): [description]
  - rests on:
    - **[Principle 1]** (principle): [description]
      - led to:
        - **[Innovation A]** (innovation): [description]
          - enables:
            - **[Application X]** (application): [description]
    - **[Principle 2]** (principle): [description]
  - enables:
    - **[Application Y]** (application): [description]
```

### Design Rules

1. Start from the core concept at the top level
2. Group children by relationship type: `requires` first, then `rests on`, then `enables`
3. Every principle and innovation from the teaching blocks MUST appear in the map
4. Nest innovations under their parent principle using `led to`
5. Add 2-4 applications showing practical impact
6. Add 1-3 prerequisites for context
7. Keep descriptions to one line

### Depth Scaling

| Depth | Total Nodes | Levels | Include |
|-------|------------|--------|---------|
| shallow | 5-8 | 2 | Core + immediate principles/innovations |
| standard | 10-15 | 3 | + applications + some prerequisites |
| deep | 15-25 | 4 | + cross-connections + secondary applications + all prerequisites |

Default for TTT sessions: **standard** (10-15 nodes).

### Comparison Maps

For conflation gaps, use a three-section map:

```markdown
- **Shared Foundation**
  - **[Shared Principle]** (shared): [description]
- **[Concept A]** (core): [description]
  - rests on:
    - **[Shared Principle]** (shared): see above
    - **[A-only Principle]** (principle): [description]
- **[Concept B]** (core): [description]
  - rests on:
    - **[Shared Principle]** (shared): see above
    - **[B-only Principle]** (principle): [description]
```

---

## Concept File Export Format

Every Teach phase that delivers content generates a concept file during the RECORD phase.

### Filename

`concept-<domain>-<topic>.md` in kebab-case.
- Example: `concept-cost-engineering-direct-vs-indirect-costs.md`
- Example: `concept-physics-entropy.md`

### YAML Frontmatter

```yaml
---
title: "Concept Report: [Topic]"
domain: [domain in kebab-case]
date: [YYYY-MM-DD]
type: ttt-session
session: SG-[N]
plan: [training plan filename]
level: [introductory/intermediate/advanced]
tags: [domain, topic, sub-goal-title]
---
```

The `type: ttt-session` field distinguishes files generated during TTT from standalone `/explain` files.

### Content

The file contains:
1. All teaching blocks delivered during Phase 3 (abbreviated or full)
2. The concept map from Phase 3.5 (if generated)
3. The CTQ table aggregated from all teaching blocks
4. A "Session Context" section noting the plan, sub-goal, initial test result, and gaps found

### Compatibility

These files are structurally compatible with concept-builder's `/library` command. If concept-builder is also installed, its `/library list`, `/library search`, and `/library path` commands will find and index these files.
