# Concept Builder

*Learn like the pioneers -- core principles first, formalism second.*

A domain-agnostic concept explainer that produces structured Markdown files with LaTeX formulas, CTQ mastery criteria, and nested-list conceptual maps.

## Key Features

- **Any domain**: Physics, biology, mathematics, CS, economics, philosophy, engineering, or anything else
- **6-section structure**: Problem, Core Principles, Key Innovations, Intuitive Formalization, CTQ Mapping, Conceptual Map
- **LaTeX math**: All formulas in `$...$` and `$$...$$` notation
- **Conceptual maps**: Markdown nested lists with typed nodes and labeled relationships
- **File export**: Every explanation saved as a `.md` file with YAML frontmatter
- **Recursive learning**: Deep-dive into any node to expand it into its own full explanation
- **Comparison mode**: Side-by-side analysis with shared principles and unified maps
- **Learning paths**: Build connected paths through your concept library

## Quick Start

```
/explain entropy --domain physics
/explain gradient descent --domain machine-learning --level introductory
/map-only thermodynamics --depth deep
/deep-dive Boltzmann distribution --from concept-physics-entropy.md
/compare supervised learning vs unsupervised learning
/library list
/library path "calculus" "differential equations"
```

## Commands

| Command | Purpose | Output |
|---------|---------|--------|
| `/explain <concept>` | Full 6-section concept breakdown | `concept-<domain>-<name>.md` |
| `/deep-dive <node>` | Expand one map node recursively | `concept-<domain>-<name>.md` |
| `/compare <A> vs <B>` | Side-by-side two concepts | `concept-compare-<A>-vs-<B>.md` |
| `/map-only <topic>` | Quick conceptual map only | `concept-map-<domain>-<name>.md` |
| `/library [subcommand]` | Manage saved concept files | Index, search results, or learning path |

## Skills

| Skill | Auto-triggers when... |
|-------|----------------------|
| `concept-builder-methodology` | User asks to explain, teach, or break down any concept |
| `concept-maps` | User discusses concept maps, knowledge graphs, or topic structures |
| `ctq-methodology` | User asks about mastery criteria, prerequisites, or learning requirements |

## File Structure

```
concept-builder/
├── .claude-plugin/
│   └── plugin.json
├── README.md
├── CONNECTORS.md
├── commands/
│   ├── explain.md
│   ├── deep-dive.md
│   ├── compare.md
│   ├── map-only.md
│   └── library.md
└── skills/
    ├── concept-builder-methodology/
    │   └── SKILL.md
    ├── concept-maps/
    │   └── SKILL.md
    └── ctq-methodology/
        └── SKILL.md
```

## Philosophy

Traditional teaching presents conclusions: "here is the formula, here is how to use it." This plugin rebuilds the reasoning:

1. Start with the **problem** that forced the concept into existence
2. Establish the **principles** -- the foundational truths that constrain any solution
3. Trace the **innovations** -- the creative leaps that solved the problem
4. Only then **formalize** -- because now you know *why* every symbol is there
5. Map **CTQ factors** -- so you know what genuine mastery looks like
6. Visualize the **structure** -- so you see how everything connects
