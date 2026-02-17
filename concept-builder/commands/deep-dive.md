---
description: Expand one node from a previous conceptual map into its own full concept breakdown
argument-hint: "<node name> [--from <concept-file.md>]"
---

# /deep-dive -- Recursive Concept Expansion

Take one node from a previous conceptual map (a principle, innovation, application, or prerequisite) and expand it into its own full concept-builder explanation. Enables recursive learning -- zoom into any piece without losing the big picture.

## Invocation

```
/deep-dive <node name>
/deep-dive <node name> --from <concept-file.md>
```

Examples:
```
/deep-dive Boltzmann distribution --from concept-physics-entropy.md
/deep-dive backpropagation
/deep-dive Nash equilibrium --from concept-game-theory-mechanism-design.md
```

If no `--from` is provided, the command will search the current directory for the most recently modified `concept-*.md` file and use its map.

## Workflow

### Step 1: Identify the Source Concept

Locate the parent concept file:

1. **If `--from` is provided**: Read the specified file directly.
2. **If not provided**: Use `Glob` to find `concept-*.md` files in the current directory. Select the most recently modified one. Present its conceptual map nodes to the user and ask which node to expand.

Parse the source file's conceptual map (the markdown nested list in Section 6) to extract:
- The list of nodes (with their types: principle, innovation, application, prerequisite)
- The relationships connecting them (rests on, led to, enables, requires, etc.)
- The one-line descriptions for each node

If the requested node name does not match any node in the map, suggest the closest matches and ask the user to clarify.

### Step 2: Extract Context from Parent

From the source file, gather all context about the selected node:
- The one-line description from the legend table
- All edges connected to this node (what it depends on, what depends on it)
- Any mention of this concept in the parent file's sections (principles, innovations, etc.)

This context seeds the deep-dive so it connects back to the parent. The deep-dive should:
- Start where the parent left off (don't re-explain what the parent already covered)
- Acknowledge the parent concept explicitly in the Problem section ("In the context of [parent concept], we need to understand [this node] because...")
- Use the parent's framing as a bridge

### Step 3: Run the Full /explain Workflow

Execute the complete 7-step `/explain` workflow for the selected node as a standalone concept:

1. The Problem -- framed in the context of the parent concept
2. Core Principles -- the node's own foundational truths
3. Key Innovations -- breakthroughs specific to this sub-concept
4. Intuitive Formalization -- the math for this node specifically
5. CTQ Mapping -- what you must understand about this sub-concept
6. Conceptual Map -- a new map for this node, showing its own internal structure

### Step 4: Link Back and Export

**File output**: Save as `concept-<domain>-<name>.md` (same naming pattern as `/explain`).

**YAML frontmatter** must include:
```yaml
---
title: "Concept Report: [Node Name]"
domain: [domain]
date: [YYYY-MM-DD]
type: deep-dive
parent: [filename of source concept file]
parent-node: [name of the node that was expanded]
tags: [domain, node-name, parent-concept-name]
---
```

The `parent` and `parent-node` fields enable the `/library` command to reconstruct learning paths and track the expansion tree.

### Step 5: Suggest Next Steps

After generating the deep-dive, suggest 2-3 other nodes from the **original parent map** that would be natural next deep-dives:
- Prioritize nodes that are directly connected to the just-expanded node
- Prioritize nodes that are prerequisites for understanding more advanced parts of the parent concept
- Format as actionable `/deep-dive` commands the user can copy-paste

```
## Next Steps

Based on the conceptual map from [parent file], consider exploring:

1. `/deep-dive [Node A] --from [parent-file]` -- [why this is a good next step]
2. `/deep-dive [Node B] --from [parent-file]` -- [why this is a good next step]
3. `/deep-dive [Node C] --from [parent-file]` -- [why this is a good next step]
```

## Notes

- Deep-dives can be chained: a deep-dive can itself become the parent for another deep-dive, creating an arbitrarily deep learning tree
- The domain is inherited from the parent concept unless the node clearly belongs to a different domain
- The depth level (introductory/intermediate/advanced) is inherited from the parent unless the user specifies otherwise
- If the node is a prerequisite (slate/grey in the map), the deep-dive may need to cover material outside the parent's domain -- this is expected and correct
