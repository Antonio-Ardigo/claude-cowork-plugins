---
description: Side-by-side comparison of two concepts -- shared principles, divergences, CTQ comparison, and unified map
argument-hint: "<concept A> vs <concept B> [--domain <domain>]"
---

# /compare -- Side-by-Side Concept Comparison

Compare two concepts, theories, or systems side-by-side using the core-principles framework. Highlights shared principles, divergent innovations, different CTQ tradeoffs, and produces a unified conceptual map showing both.

## Invocation

```
/compare <concept A> vs <concept B>
/compare <concept A> and <concept B>
/compare <concept A> vs <concept B> --domain <domain>
```

Examples:
```
/compare entropy vs enthalpy
/compare gradient descent vs genetic algorithms --domain optimization
/compare Lagrangian mechanics vs Hamiltonian mechanics
/compare capitalism vs socialism --domain economics
/compare supervised learning vs unsupervised learning --domain machine-learning
```

If only one concept is provided, prompt the user for the second. The `vs` or `and` separator is flexible -- parse both.

## Workflow

### Step 1: Accept and Scope Both Concepts

Parse two concept names from the argument. Determine the domain:
- If `--domain` is provided, use it for both
- If not provided, infer from the concepts
- If the two concepts belong to different domains, note this explicitly and use the broader domain or `general`

Check if `/explain` files already exist for either concept in the current directory. If they do, read them to reuse their analysis. If not, analyze each concept fresh.

### Step 2: Shared Principles

Identify principles that are foundational to **both** concepts. For each shared principle:
- State the principle
- Describe how it manifests or is applied in Concept A
- Describe how it manifests or is applied in Concept B
- Note any differences in emphasis or interpretation

#### Output Format

```
## 1. Shared Principles

| Principle | In [Concept A] | In [Concept B] |
|-----------|----------------|----------------|
| [principle name] | [how it manifests] | [how it manifests] |

### [Principle Name]
[Deeper explanation of how this principle connects both concepts]
```

### Step 3: Divergences

Identify where the two concepts fundamentally differ -- different assumptions, different domains of applicability, different conclusions from similar premises, different tradeoffs.

#### Output Format

```
## 2. Where They Diverge

| Dimension | [Concept A] | [Concept B] |
|-----------|-------------|-------------|
| Core assumption | [what A assumes] | [what B assumes] |
| Primary strength | [where A excels] | [where B excels] |
| Limitation | [where A fails] | [where B fails] |
| Typical use case | [when to use A] | [when to use B] |

### Key Divergence: [Most Important Difference]
[Detailed explanation of the fundamental difference and why it matters]
```

### Step 4: CTQ Comparison

Side-by-side CTQ tables showing what you must understand to master each concept. Highlight:
- **Overlapping CTQs**: Understanding requirements shared by both
- **Unique CTQs**: Requirements specific to only one concept

#### Output Format

```
## 3. CTQ Comparison

### Shared Mastery Requirements
| CTQ | For [Concept A] | For [Concept B] |
|-----|-----------------|-----------------|
| [shared requirement] | [A's version] | [B's version] |

### Unique to [Concept A]
| CTQ | Mastery Test | Why A Needs This |
|-----|-------------|-----------------|
| [requirement] | [test] | [reason] |

### Unique to [Concept B]
| CTQ | Mastery Test | Why B Needs This |
|-----|-------------|-----------------|
| [requirement] | [test] | [reason] |
```

### Step 5: Unified Conceptual Map

Generate a single markdown nested-list map showing **both** concepts, their shared elements, and unique elements.

Use the standard concept-builder node types plus **(shared)** for nodes common to both:
- **(core)**: Each concept's central node
- **(principle)**, **(innovation)**, **(application)**, **(prerequisite)**: Standard types
- **(shared)**: Principles, prerequisites, or applications that both concepts have in common

Structure the map with shared nodes at the top level, then each concept branching below:

```
- **Shared Foundation**
  - **[Shared Principle]** (shared): [description]
- **[Concept A]** (core): [description]
  - rests on:
    - **[Shared Principle]** (shared): see above
    - **[A-specific Principle]** (principle): [description]
  - enables:
    - **[A-specific Application]** (application): [description]
- **[Concept B]** (core): [description]
  - rests on:
    - **[Shared Principle]** (shared): see above
    - **[B-specific Principle]** (principle): [description]
  - enables:
    - **[B-specific Application]** (application): [description]
```

### Step 6: Synthesis and Export

End with a brief synthesis:
- **When to choose A over B** (and vice versa)
- **When they complement each other** (if applicable)
- **The deeper question**: What does comparing these two concepts reveal about the domain?

**File output**: Save as `concept-compare-<nameA>-vs-<nameB>.md` in the current working directory.

**YAML frontmatter**:
```yaml
---
title: "Concept Comparison: [A] vs [B]"
domain: [domain]
date: [YYYY-MM-DD]
type: compare
concepts: [concept-a, concept-b]
tags: [domain, concept-a, concept-b, comparison]
---
```

## Notes

- If existing `/explain` files exist for either concept, reference and build on their analysis rather than starting from scratch
- The comparison should be balanced -- do not favor one concept over the other unless there is a clear empirical or logical reason
- If the two concepts are not meaningfully comparable (e.g., "entropy vs. democracy"), explain why the comparison is problematic and suggest better pairings
- At the `advanced` level, include a section on historical debates between proponents of each concept
