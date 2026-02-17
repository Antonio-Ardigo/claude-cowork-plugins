---
name: ctq-methodology
description: Critical-To-Quality methodology for concept learning. Use when the user asks about CTQ, critical to quality, mastery criteria, learning requirements, concept prerequisites, what must I understand, knowledge dependencies, concept mastery verification, or how to know if I truly understand something.
---

# CTQ Methodology Skill

You apply Critical-To-Quality (CTQ) analysis to concept learning. In manufacturing, CTQ identifies the measurable characteristics that define product quality. In learning, CTQ identifies the specific understandings that define genuine mastery of a concept.

## What is a Learning CTQ?

A **learning CTQ** is a specific understanding or ability that is **necessary** to claim you truly know a concept. It is not a topic to study -- it is a verifiable criterion.

**Good CTQ**: "Can derive the relationship between entropy and the number of microstates"
**Bad CTQ**: "Understand entropy" (too vague, not verifiable)

## CTQ Derivation Method

### Step 1: Trace from Principles

For each core principle of a concept, ask: "What specific understanding does this principle require?" The answer is a CTQ.

| Principle | -> | CTQ |
|-----------|---|-----|
| Energy is conserved | -> | Can track energy transformations across heat, work, and internal energy in a closed system |
| Entropy never decreases | -> | Can determine the direction of a spontaneous process using entropy change |

### Step 2: Trace from Innovations

For each key innovation, ask: "What must you understand about this innovation to use it correctly?"

| Innovation | -> | CTQ |
|-----------|---|-----|
| Boltzmann's $S = k_B \ln W$ | -> | Can calculate entropy from microstate counting for a simple system |
| Carnot's theorem | -> | Can prove why no real engine exceeds Carnot efficiency |

### Step 3: Identify Failure Modes

For each CTQ, ask: "How do people typically get this wrong?" Common patterns:

| Failure Pattern | Description |
|----------------|-------------|
| **Conflation** | Mixing up two related but distinct concepts (e.g., heat vs. temperature) |
| **Overgeneralization** | Applying a principle beyond its valid domain (e.g., using ideal gas law for liquids) |
| **Missing prerequisite** | Lacking a foundational understanding (e.g., trying to learn QM without linear algebra) |
| **Procedural without conceptual** | Can follow the steps but cannot explain why they work |
| **Verbal without formal** | Can describe in words but cannot write the equation |
| **Formal without intuitive** | Can manipulate symbols but cannot explain what the result means physically |

## Standard CTQ Table Format

```
| CTQ | Source | Mastery Test | Common Failure Mode |
|-----|--------|-------------|---------------------|
| [specific understanding] | Principle N / Innovation N | [question or task that verifies mastery] | [how people typically get this wrong] |
```

### Column Definitions

- **CTQ**: A precise, verifiable statement of what you must understand. Start with "Can..." for abilities or use a declarative statement for knowledge.
- **Source**: Which principle or innovation from the concept explanation this CTQ traces back to. Use "Principle N" or "Innovation N" to reference specific sections.
- **Mastery Test**: A concrete question, calculation, or task that someone who truly understands this would be able to complete. Should be specific enough to grade pass/fail.
- **Common Failure Mode**: The most frequent way people fail this CTQ. Use the failure pattern categories above when applicable.

## Examples Across Domains

### Physics: Newtonian Mechanics

| CTQ | Source | Mastery Test | Common Failure Mode |
|-----|--------|-------------|---------------------|
| Can draw a correct free-body diagram for any system | Newton's Third Law | Draw FBD for a book on an accelerating elevator | Conflation: confusing weight with normal force |
| Can apply F=ma to multi-body systems | Newton's Second Law | Solve for acceleration of Atwood machine | Procedural: plugging into formula without choosing coordinate system |

### Computer Science: Big-O Notation

| CTQ | Source | Mastery Test | Common Failure Mode |
|-----|--------|-------------|---------------------|
| Can determine time complexity of nested loops | Definition of O(f(n)) | Analyze a triple-nested loop with varying bounds | Overgeneralization: assuming all nested loops are O(n^k) |
| Can explain why O(n log n) beats O(n^2) for large n | Asymptotic analysis | Show crossover point for merge sort vs insertion sort | Formal without intuitive: knows the ranking but cannot explain the growth rates |

### Biology: Natural Selection

| CTQ | Source | Mastery Test | Common Failure Mode |
|-----|--------|-------------|---------------------|
| Can distinguish selection from drift | Mechanism of selection | Explain why a trait might spread without being adaptive | Overgeneralization: attributing all trait changes to selection |
| Can identify the unit of selection | Darwinian principle | Argue whether group selection or gene-level selection explains altruism | Conflation: mixing up selection at different levels (gene, individual, group) |

## CTQ in Learning Paths

CTQs feed into the `/library path` command:
- A concept's prerequisites can be expressed as CTQs from an earlier concept
- A learning path is complete when all CTQs at each step can be verified before moving to the next
- Gaps in a learning path correspond to CTQs that no existing concept file addresses
