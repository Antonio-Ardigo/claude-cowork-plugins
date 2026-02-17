---
name: concept-maps
description: Standard conceptual map format for concept-builder. Use when the user asks about concept maps, knowledge graphs, concept visualization, dependency graphs, topic maps, or conceptual outlines. Also use when generating any structured map of relationships between ideas, principles, or theories for educational or conceptual purposes.
---

# Concept Maps Skill

You produce structured conceptual maps as markdown nested lists. Maps show how principles, innovations, applications, and prerequisites relate to each other within a concept or topic.

## Map Format

Maps are markdown nested lists. Each node has a **bold name**, a type in parentheses, and a one-line description after a colon. Relationships are shown as labeled groups of children.

### Example

```markdown
- **Thermodynamics** (core): Study of energy, heat, work, and their transformations
  - requires:
    - **Calculus** (prerequisite): Derivatives and integrals for state functions
    - **Classical Mechanics** (prerequisite): Newton's laws and conservation principles
  - rests on:
    - **Zeroth Law** (principle): Thermal equilibrium is transitive -- defines temperature
    - **First Law** (principle): Energy is conserved -- heat and work are interchangeable
      - led to:
        - **Carnot's Theorem** (innovation): No engine more efficient than a reversible one
          - enables:
            - **Heat Engine Design** (application): Upper bounds on thermal efficiency
    - **Second Law** (principle): Entropy of an isolated system never decreases
      - led to:
        - **Boltzmann's Statistical Mechanics** (innovation): $S = k_B \ln W$ -- entropy from microstates
          - enables:
            - **Statistical Thermodynamics** (application): Deriving macroscopic properties from microscopic behavior
    - **Third Law** (principle): Entropy approaches zero as temperature approaches absolute zero
  - enables:
    - **Chemical Engineering** (application): Reaction equilibria and phase diagrams
    - **Information Theory** (application): Shannon entropy as a measure of uncertainty
```

## Node Types

| Type | Meaning | Usage |
|------|---------|-------|
| **(core)** | The central concept or topic being mapped | Exactly one per map (or two for comparisons) |
| **(principle)** | Foundational truth or constraint | The 3-5 load-bearing ideas the concept rests on |
| **(innovation)** | Conceptual breakthrough or key contribution | Creative leaps that built on principles |
| **(application)** | Practical use or derived concept | Where the theory meets the real world |
| **(prerequisite)** | Required prior knowledge | What you need to understand before this concept |
| **(shared)** | Common to both concepts in a comparison | Only used in `/compare` maps |

## Relationship Labels

Use these labels as prefixes for nested groups:

| Label | Meaning | Direction |
|-------|---------|-----------|
| `rests on` | This concept is built on these principles | core -> principle |
| `requires` | This concept needs these prerequisites | core -> prerequisite |
| `led to` | This principle/innovation produced these innovations | principle -> innovation |
| `enables` | This innovation/principle enables these applications | innovation -> application |
| `generalizes` | This concept is a generalization of the child | parent -> child |
| `is a special case of` | This concept is a specialization of the child | child -> parent |
| `contrasts with` | These concepts are in tension or opposition | sibling <-> sibling |
| `equivalent to` | These are different formulations of the same idea | sibling <-> sibling |

## Structure Guidelines

1. **Start from the core concept** at the top level
2. **Group children by relationship type**: `requires` first, then `rests on`, then `enables`
3. **Every principle and innovation** from the explanation MUST appear in the map
4. **Nest innovations under their parent principle** using `led to`
5. **Add 2-4 applications** to show practical impact
6. **Add 1-3 prerequisites** for context
7. **Keep descriptions to one line** -- maps are structural, not narrative
8. **Limit depth to 4 levels** of nesting for readability

## Comparison Maps

For `/compare` outputs, use a three-section structure:

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

## Depth Scaling

| Depth | Total Nodes | Levels | Include |
|-------|------------|--------|---------|
| shallow | 5-8 | 2 | Core + immediate principles/innovations |
| standard | 10-15 | 3 | + applications + some prerequisites |
| deep | 15-25 | 4 | + cross-connections + secondary applications + all prerequisites |
