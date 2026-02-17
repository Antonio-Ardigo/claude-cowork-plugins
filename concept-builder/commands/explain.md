---
description: Full concept breakdown -- problem, principles, innovations, math, CTQ, and conceptual map
argument-hint: "<concept name> [--domain <domain>] [--level introductory|intermediate|advanced]"
---

# /explain -- Concept Builder

Explain any concept from any domain through a structured seven-step workflow: identify the problem, establish core principles, trace key innovations, build an intuitive formalization, map critical-to-quality factors, generate a conceptual map, and export a comprehensive report as a Markdown file.

## Philosophy

*Learn like the pioneers -- core principles first, formalism second.*

Don't teach conclusions. Rebuild the reasoning. Start with the problem that forced the concept into existence, establish the foundational principles, trace the key innovations, then formalize -- only after the reader knows *why* every symbol is there.

## Invocation

```
/explain <concept>
/explain <concept> --domain <domain>
/explain <concept> --level advanced
/explain <concept> --domain physics --level introductory
```

Examples:
```
/explain entropy
/explain gradient descent --domain machine-learning
/explain Nash equilibrium --domain game-theory --level advanced
/explain natural selection --domain biology --level introductory
/explain Fourier transform --domain mathematics
```

If no concept is provided, prompt the user to supply one.

## Workflow

### Step 1: Accept and Scope the Concept

Accept the concept to explain. It may be provided as:
- **A named concept**: e.g., "entropy", "gradient descent", "Nash equilibrium"
- **A question**: e.g., "How does natural selection work?"
- **A broad topic**: e.g., "thermodynamics" (narrow down with the user if needed)

Parse optional flags:
- `--domain <domain>`: The field this concept belongs to. If not provided, infer from the concept name. If ambiguous, ask the user. Use kebab-case for the domain (e.g., `machine-learning`, `quantum-mechanics`, `game-theory`). If truly cross-domain, use `general`.
- `--level <level>`: One of `introductory`, `intermediate`, `advanced`. Default: `intermediate`.

If the concept is ambiguous or too broad, ask the user to clarify scope. For broad topics, propose a focused starting point and offer to cover related subtopics via `/deep-dive`.

### Step 2: The Problem (Section 1)

Explain **what problem, need, or contradiction** made this concept necessary. This is the motivational hook -- the reader should feel the tension that the concept resolves.

Address:
- **What was broken**: The observation, limitation, paradox, or open question that demanded a new idea
- **Why existing approaches failed**: What people tried before and why it was insufficient
- **The stakes**: What was at risk -- practical, theoretical, or both

Write 1-3 paragraphs using plain language. No jargon, no formulas. The reader should understand *why they should care* before encountering any technical content.

#### Output Format

```
## 1. The Problem

### What was broken
[The limitation, paradox, or question that motivated this concept]

### Why existing approaches failed
[What people tried before, and why it didn't work]

### The stakes
[What was at stake -- practical, theoretical, or both]
```

### Step 3: Core Principles (Section 2)

Identify the **3-5 foundational truths or constraints** that the concept rests on. These are the load-bearing ideas -- if you understand these, the rest follows.

For each principle:
1. **Plain-language statement**: One clear sentence anyone can understand
2. **Formal expression**: One LaTeX equation that captures the principle (at `intermediate` and `advanced` levels)
3. **Concrete example**: A specific, vivid illustration that makes the principle tangible

The principles should be ordered from most fundamental to most derived. Each subsequent principle should build on or constrain the previous ones.

#### LaTeX Notation Guide

**IMPORTANT**: All mathematical expressions MUST use LaTeX notation. Use `$...$` for inline math and `$$...$$` for display (block) equations.

Standard notation:
- Vectors: `$\mathbf{v}$`, `$\vec{x}$`
- Matrices: `$\mathbf{A}$`, `\begin{pmatrix}...\end{pmatrix}`
- Partial derivatives: `$\frac{\partial f}{\partial x}$`
- Integrals: `$\int_a^b f(x)\,dx$`
- Summations: `$\sum_{i=1}^{n}$`
- Greek letters: `$\alpha$`, `$\beta$`, `$\theta$`, `$\lambda$`
- Set notation: `$\in$`, `$\subset$`, `$\cup$`, `$\cap$`
- Probability: `$P(A|B)$`, `$\mathbb{E}[X]$`
- Norms: `$\|x\|$`, `$\|A\|_F$`
- Subscripts/superscripts: `$x_i$`, `$x^{(k)}$`

All equations in Sections 2, 3, 4, and the final report MUST use LaTeX. Inline references to variables in prose sections should also use inline LaTeX `$...$`.

#### Output Format

```
## 2. Core Principles

### Principle 1: [Name]
**Statement**: [One clear sentence]
**Formally**: $$[LaTeX equation]$$
**Example**: [Concrete, vivid illustration]

### Principle 2: [Name]
**Statement**: [One clear sentence]
**Formally**: $$[LaTeX equation]$$
**Example**: [Concrete, vivid illustration]

[Repeat for 3-5 principles]
```

### Step 4: Key Innovations (Section 3)

Identify the **2-4 key innovations or breakthroughs** that built the concept from its principles. These are the creative leaps -- the moments where someone saw a connection others missed.

For each innovation:
1. **Who**: The person or group who introduced it (and approximately when)
2. **What it solved**: The specific problem or gap this innovation addressed
3. **Worked example**: A concrete illustration of the innovation in action, with enough detail that the reader could reproduce the reasoning

The innovations should be ordered chronologically or by logical dependency.

#### Output Format

```
## 3. Key Innovations

### [Innovation Name] ([Person/Group], [Year/Era])
**What**: [What was introduced or discovered]
**Why it mattered**: [What problem it solved, what it unlocked]
**Example**: [Concrete worked illustration]

[Repeat for 2-4 innovations]
```

### Step 5: Intuitive Formalization (Section 4)

Present the **simplest mathematically sound version** of the full theory. This is NOT the most general or rigorous formulation -- it is the minimum math needed to make predictions, grounded in the examples from Sections 2-3.

Structure:
1. **Starting point**: The single most important equation or relationship, stated with all terms defined
2. **Building up**: Step-by-step development from simple to useful, each step motivated by an example or principle from earlier sections
3. **Key equations table**: Summary of central equations with plain-language descriptions
4. **The full picture** (optional): Where the simplified version breaks down and what the full formalism adds -- only at `intermediate` and `advanced` levels

The goal: a reader who understood Sections 2-3 should be able to follow every step here. No "it can be shown that" -- every step must be justified.

#### Output Format

```
## 4. Intuitive Formalization

### Starting Point
[The simplest mathematical statement, with all terms defined]

### Building Up
[Step-by-step development, each step grounded in earlier examples]

### Key Equations
| Name | Equation | What it tells you |
|------|----------|-------------------|
| [name] | $[LaTeX]$ | [plain-language meaning] |

### The Full Picture
[Where the simplified version fails, and what the full formalism adds]
```

### Step 6: CTQ Mapping (Section 5)

Construct a **Critical-To-Quality** map for mastering this concept. In a learning context, a CTQ is a specific understanding that is necessary to claim you truly know the concept.

Derive each CTQ from the principles and innovations in Sections 2-3. For each CTQ:
- **What you must understand**: The specific knowledge or ability
- **Source**: Which principle or innovation it traces back to
- **Mastery test**: A concrete question or task that verifies understanding
- **Common failure mode**: The typical way people get this wrong

#### Output Format

```
## 5. Critical to Quality -- What You Must Understand

| CTQ | Source | Mastery Test | Common Failure Mode |
|-----|--------|-------------|---------------------|
| [understanding requirement] | Principle N / Innovation N | [question or task to verify] | [typical misunderstanding] |
```

### Step 7: Conceptual Map, Summary Report, and Export

#### 7a: Conceptual Map (Section 6)

Generate a markdown nested-list map linking principles, innovations, applications, and prerequisites. The map uses indentation and relationship labels to show the concept's structure.

**Node types** (marked in parentheses after each node name):
- **(core)**: The central concept being explained
- **(principle)**: Foundational principles from Section 2
- **(innovation)**: Key innovations from Section 3
- **(application)**: Practical applications or derived concepts
- **(prerequisite)**: Required prior knowledge

**Relationship labels** use a controlled vocabulary as prefixes: `rests on`, `led to`, `enables`, `requires`, `generalizes`, `is a special case of`, `contrasts with`, `equivalent to`.

Each node gets a bold name, its type in parentheses, and a one-line description after a colon.

#### Output Format

```
## 6. Conceptual Map

- **[Concept Name]** (core): [one-line description]
  - rests on:
    - **[Principle 1]** (principle): [one-line description]
      - led to:
        - **[Innovation A]** (innovation): [one-line description]
          - enables:
            - **[Application X]** (application): [one-line description]
    - **[Principle 2]** (principle): [one-line description]
      - led to:
        - **[Innovation B]** (innovation): [one-line description]
  - requires:
    - **[Prerequisite 1]** (prerequisite): [one-line description]
    - **[Prerequisite 2]** (prerequisite): [one-line description]
  - enables:
    - **[Application Y]** (application): [one-line description]
```

Guidelines for building the map:
- Start from the core concept at the top level
- Group children by relationship type (`rests on`, `requires`, `enables`)
- Every principle and innovation from Sections 2-3 MUST appear in the map
- Add 2-4 applications and 1-3 prerequisites to round out the picture
- Keep descriptions to one line each -- this is a map, not an essay

#### 7b: Compile and Export

Compile all six sections into a single comprehensive report and save it as a `.md` file.

1. **Filename**: `concept-<domain>-<concept-name>.md` in kebab-case
   - Example: `concept-physics-entropy.md`, `concept-machine-learning-gradient-descent.md`
2. **Location**: Save to the user's current working directory
3. **YAML frontmatter**:
   ```
   ---
   title: "Concept Report: [Concept Name]"
   domain: [domain]
   date: [YYYY-MM-DD]
   type: explain
   level: [introductory/intermediate/advanced]
   tags: [domain, concept-name, related-topics]
   ---
   ```
4. **Content**: The full report with all LaTeX formulas preserved using `$...$` and `$$...$$` notation
5. **Footer**: Append a "Further Reading" section with suggested resources and a "Next Steps" section suggesting 2-3 nodes from the conceptual map as good `/deep-dive` targets

This export step is NOT optional -- every `/explain` invocation MUST produce a `.md` file as its final deliverable. Provide the user with a direct link to the file after saving.

## Depth Levels

| Level | Math Depth | Principles | Innovations | CTQ Detail |
|-------|-----------|-----------|------------|-----------|
| **introductory** | Minimal notation, intuition-first. Equations only where essential. | 3 principles, plain-language statements only | 2 innovations, brief | Short CTQ table |
| **intermediate** | Full LaTeX throughout. Standard notation for the field. | 3-5 principles with full LaTeX formalization | 2-4 innovations with worked examples | Full CTQ table with mastery tests |
| **advanced** | Proofs, edge cases, competing formulations. Multiple representations. | 5 principles with derivations and proofs | 4 innovations with detailed proofs | CTQ + advanced failure modes + edge cases |

Default to **intermediate** unless the user specifies otherwise.

## Notes

- This command works for ANY domain -- physics, biology, mathematics, computer science, economics, philosophy, engineering, art theory, linguistics, or any other field
- If a concept spans multiple domains (e.g., "information entropy" bridges physics and CS), acknowledge both and let the user choose which framing to emphasize
- Always distinguish between what is empirically established and what is conjectured or debated
- When multiple formulations exist (e.g., Lagrangian vs. Newtonian mechanics), present the most accessible one first and mention alternatives
- Cite key sources where appropriate -- seminal papers, standard textbooks, foundational experiments
- If the concept has prerequisites the reader may not know, flag them explicitly and suggest they run `/explain` on those first
