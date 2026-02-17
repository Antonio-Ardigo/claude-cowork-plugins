---
description: Quick conceptual map with one-line descriptions per node -- no full breakdown
argument-hint: "<concept or topic> [--depth shallow|standard|deep]"
---

# /map-only -- Quick Conceptual Map

Generate only the conceptual map for a topic -- quick reference, no deep explanation. Useful for review, as a starting point before a full `/explain`, or for surveying a broad topic before deciding where to drill in.

## Invocation

```
/map-only <concept or topic>
/map-only <concept or topic> --depth shallow
/map-only <concept or topic> --depth deep
```

Examples:
```
/map-only thermodynamics
/map-only machine learning --depth deep
/map-only organic chemistry --depth shallow
/map-only Renaissance art
/map-only microeconomics --depth standard
```

## Workflow

### Step 1: Accept the Topic

Accept the concept or topic name. This can be broader than `/explain` -- topics like "machine learning", "Greek philosophy", or "organic chemistry" are fine here since we are only generating a structural map, not a full breakdown.

Parse the optional `--depth` flag:

| Depth | Nodes | Scope |
|-------|-------|-------|
| `shallow` | 5-8 | Central concept + immediate principles and innovations only |
| `standard` (default) | 10-15 | Two levels deep -- principles, innovations, and their direct connections |
| `deep` | 15-25 | Three levels -- includes prerequisites, applications, and cross-connections |

Infer the domain from the topic name. Use kebab-case for the domain in the output filename.

### Step 2: Generate the Conceptual Map

Build the conceptual map as a markdown nested list using the standard concept-builder format.

**Node types** (marked in parentheses after each node name):
- **(core)**: The central concept or topic
- **(principle)**: Foundational principles
- **(innovation)**: Key innovations or breakthroughs
- **(application)**: Practical applications or derived concepts
- **(prerequisite)**: Required prior knowledge

**Relationship labels** as prefixes on nested groups: `rests on`, `led to`, `enables`, `requires`, `generalizes`, `is a special case of`, `contrasts with`, `equivalent to`.

Each node gets: **bold name**, type in parentheses, one-line description after colon.

**Ordering guidelines**:
- Start from the core concept at the top level
- Group children by relationship type
- Place `requires` (prerequisites) first, then `rests on` (principles), then `enables` (applications)
- Within principles, order from most fundamental to most derived
- Innovations nest under the principle they extend

**Output format**:

```
## Conceptual Map: [Topic Name]

- **[Topic Name]** (core): [one-line description]
  - requires:
    - **[Prerequisite 1]** (prerequisite): [description]
    - **[Prerequisite 2]** (prerequisite): [description]
  - rests on:
    - **[Principle 1]** (principle): [description]
      - led to:
        - **[Innovation A]** (innovation): [description]
    - **[Principle 2]** (principle): [description]
      - led to:
        - **[Innovation B]** (innovation): [description]
          - enables:
            - **[Application X]** (application): [description]
  - enables:
    - **[Application Y]** (application): [description]
    - **[Application Z]** (application): [description]
```

### Step 3: Exploration Prompts

Suggest 3 nodes from the map that would make good targets for deeper exploration:

```
## Where to Go Next

1. `/explain [Node A]` -- [why this is a good starting point for deeper study]
2. `/explain [Node B]` -- [why this node is interesting or important]
3. `/deep-dive [Node C] --from [this-file]` -- [why expanding this node would be valuable]
```

Prioritize nodes that are:
- Central to the topic (many connections in the map)
- Conceptually rich (would produce interesting `/explain` output)
- Prerequisites for advanced understanding

### Step 4: Export

Save as `concept-map-<domain>-<name>.md` in the current working directory.

**YAML frontmatter**:
```yaml
---
title: "Concept Map: [Topic Name]"
domain: [domain]
date: [YYYY-MM-DD]
type: map-only
depth: [shallow/standard/deep]
tags: [domain, topic-name]
---
```

## Notes

- Maps are intentionally concise -- resist the urge to explain nodes in detail. That is what `/explain` and `/deep-dive` are for.
- For broad topics (e.g., "physics"), the map represents a curated overview, not an exhaustive inventory. Acknowledge what is omitted.
- If the user asks for a map of a topic that already has a `concept-*.md` file in the directory, read that file and regenerate or update its map rather than creating a duplicate.
