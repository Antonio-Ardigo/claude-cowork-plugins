---
description: Manage saved concept files -- list, search, link, create learning paths
argument-hint: "[list | search <query> | path <start> <end> | link <file1> <file2>]"
---

# /library -- Concept Library Manager

Manage a personal library of previously generated concept files. List, search, link concepts together, and create learning paths.

## Invocation

```
/library list
/library search <query>
/library path <start-concept> <end-concept>
/library link <file1.md> <file2.md>
```

Examples:
```
/library list
/library search entropy
/library path "calculus" "differential equations"
/library link concept-physics-entropy.md concept-physics-thermodynamics.md
```

If no subcommand is provided, default to `list`.

## Subcommands

### /library list

Scan the current directory for all `concept-*.md` files. Parse the YAML frontmatter from each file and display an organized index.

**Workflow**:
1. Use `Glob` to find all `concept-*.md` files in the current directory
2. Use `Read` to parse the YAML frontmatter from each file (title, domain, date, type, parent, tags)
3. Group files by domain
4. Display as a table sorted by domain, then date

**Output Format**:

```
## Concept Library

**[N] concept files found in [directory]**

### [Domain 1]
| File | Type | Title | Date | Parent |
|------|------|-------|------|--------|
| [filename](filename) | explain | [title] | [date] | -- |
| [filename](filename) | deep-dive | [title] | [date] | [parent file] |

### [Domain 2]
| File | Type | Title | Date | Parent |
|------|------|-------|------|--------|
| ... | ... | ... | ... | ... |

### Comparisons
| File | Concepts | Date |
|------|----------|------|
| [filename](filename) | [A] vs [B] | [date] |

### Maps
| File | Topic | Depth | Date |
|------|-------|-------|------|
| [filename](filename) | [topic] | [depth] | [date] |
```

If no concept files are found, suggest running `/explain` or `/map-only` to create some.

### /library search <query>

Search across all concept files for keyword matches in titles, tags, and content.

**Workflow**:
1. Use `Glob` to find all `concept-*.md` files
2. Use `Grep` to search for the query string across all matching files
3. Return files with matching context (surrounding lines)

**Output Format**:

```
## Search Results for "[query]"

**[N] matches in [M] files**

### [filename1]
- **Title**: [title]
- **Match**: ...[context around match]...

### [filename2]
- **Title**: [title]
- **Match**: ...[context around match]...
```

### /library path <start-concept> <end-concept>

Construct a recommended learning path between two concepts by analyzing the parent chains, conceptual map connections, and prerequisite relationships across all concept files.

**Workflow**:
1. Use `Glob` to find all `concept-*.md` files
2. Use `Read` to parse frontmatter (parent, tags) and conceptual maps from each file
3. Build a dependency graph from:
   - `parent` fields in frontmatter (deep-dive chains)
   - `requires` and `rests on` relationships in conceptual maps (nested lists)
   - `related` fields if any (from `/library link`)
4. Find the shortest learning path from start to end through the graph
5. For each step, check if a concept file already exists or needs to be created

**Output Format**:

```
## Learning Path: [Start] --> [End]

| Step | Concept | Status | Action |
|------|---------|--------|--------|
| 1 | [concept] | Exists | Read [filename](filename) |
| 2 | [concept] | Missing | Run `/explain [concept] --domain [d]` |
| 3 | [concept] | Exists | Read [filename](filename) |
| ... | ... | ... | ... |
| N | [end concept] | [status] | [action] |

### Gap Analysis
[N] of [M] concepts in this path already have files. Run the suggested `/explain` commands to fill the gaps.
```

If no connected path exists between the two concepts, suggest an approximate path based on domain similarity and prerequisite inference.

### /library link <file1> <file2>

Manually declare a dependency or relationship between two concept files. This adds a `related` entry to the YAML frontmatter of both files.

**Workflow**:
1. Verify both files exist
2. Read both files
3. Add or update the `related` field in the YAML frontmatter of each file:
   - In file1: add file2 to the `related` list
   - In file2: add file1 to the `related` list
4. Save both files

**Output**:
```
Linked [file1] <--> [file2]

[file1] now lists: [file2] as related
[file2] now lists: [file1] as related
```

## Notes

- The library operates on the current working directory only -- it does not search subdirectories or other locations
- All operations are non-destructive: `/library link` only adds metadata, never removes or overwrites content
- The learning path algorithm is best-effort: with more concept files in the directory, paths become more accurate and complete
- If the directory contains concept files from multiple unrelated projects, the library will show all of them grouped by domain
