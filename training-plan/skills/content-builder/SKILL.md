---
description: "Gap-targeted teaching content generation for training sessions. Use when generating teaching material during the Teach phase of a TTT session, when the user asks to explain a concept, teach me about a topic, what did I get wrong, fill a learning gap, or needs targeted content covering motivation, definitions, exercises, typical errors, pitfalls, and misconceptions."
---

# Content Builder -- Domain Knowledge

Reference knowledge for generating targeted, gap-filling teaching content.

## Purpose

Generate a **teaching block** for ONE specific learning gap. Not a lecture. Not a textbook chapter. Just enough to fill the gap so the learner can pass the next test.

## Teaching Block Format

For each identified gap, produce exactly this structure:

```markdown
---

**Why This Matters**
<1-2 sentences connecting this concept to the learner's real goal. Make it concrete.
Not "this is important" but "without this, your estimates will systematically miss 15-25% of costs.">

**Definition**
<Clear, concise explanation of the concept. Use plain language. One paragraph maximum.
If the concept has sub-parts, use a short bullet list.>

**Simple Exercise**
<A small, immediately solvable exercise that builds understanding.
The learner should be able to complete it in 1-2 minutes.
Provide enough context to solve it without looking anything up.>

**Typical Errors**
<2-3 common mistakes learners make with this concept, and WHY they make them.
Format: "Error: ... -- Why: ...">

**Pitfalls & Misconceptions**
<1-2 wrong mental models that learners commonly hold about this topic.
Format: "Misconception: '...' -- Reality: ...">

**Quick Check**
<One focused question to verify the learner understood this block.
Should be answerable in one sentence. Provide the expected answer in parentheses afterward.>

---
```

## Design Principles

### 1. One Gap, One Block

Each teaching block addresses exactly ONE gap. If the learner has 3 gaps, produce 3 separate blocks delivered sequentially -- not one large combined explanation.

### 2. Practical Over Theoretical

- Lead with "Why This Matters" -- connect to the learner's actual goal
- Exercises should be hands-on, not "explain the concept back to me"
- Use concrete numbers, scenarios, and examples

### 3. Minimal and Sufficient

- Definition: one paragraph. If you need more, the gap is too broad -- split it.
- Exercise: 1-2 minutes to solve. Not a project.
- Quick Check: one question. Not a quiz.

### 4. Error-Focused

The "Typical Errors" and "Pitfalls & Misconceptions" sections are often the most valuable part. They tell the learner what NOT to do, which is faster than re-teaching from scratch.

Focus on errors that are:
- **Common** -- most learners make them
- **Consequential** -- they lead to wrong results
- **Non-obvious** -- the learner wouldn't catch them on their own

### 5. Quick Check Design

The Quick Check verifies comprehension of THIS block only. Rules:

- Must be answerable from the content just presented
- Must have a clear correct answer (no opinion questions)
- Should test understanding, not recall ("When would you use X?" not "What is the definition of X?")
- Always provide the expected answer in parentheses

## Example Teaching Block

Gap: "Learner does not distinguish direct from indirect costs in a project estimate."

```markdown
---

**Why This Matters**
Indirect costs typically represent 15-25% of an EPC project estimate. If you miss
them, every estimate you produce will be systematically low -- and your project will
overrun its budget before construction even starts.

**Definition**
**Direct costs** are tied to a specific scope item -- the steel for a tank, the labor
to install a pump, the concrete for a foundation. If you can point to the item on
a drawing, it's a direct cost.

**Indirect costs** are necessary for the project to happen but not tied to one item:
- Construction camp and temporary facilities
- Site security and fencing
- Builder's risk insurance
- Mobilization / demobilization
- Quality inspection staff
- Permits and regulatory fees

**Simple Exercise**
Classify each as direct (D) or indirect (I):
1. Crane rental for tank erection
2. Builder's risk insurance policy
3. Welding rods for piping installation
4. Security guard at site gate
5. Freight of equipment from factory to site

**Typical Errors**
- Error: Listing "miscellaneous 10%" instead of itemizing indirects -- Why: feels
  easier, but hides real costs and makes the estimate uncheckable.
- Error: Classifying freight as indirect -- Why: if freight is for a specific piece
  of equipment, it's a direct cost for that item.

**Pitfalls & Misconceptions**
- Misconception: "Indirects are covered by contingency" -- Reality: Contingency
  covers unknowns and risks. Indirects are known, quantifiable costs that must
  be estimated explicitly.

**Quick Check**
Is "crane rental for tank erection" a direct or indirect cost, and why?
(Answer: Direct -- it is tied to a specific scope item, the tanks.)

---
```

## When the Quick Check Fails

If the learner answers the Quick Check incorrectly:

1. Do NOT move to the next teaching block
2. Re-explain the specific point they got wrong, in different words
3. Give one more Quick Check on the same concept
4. If they pass the second check, proceed
5. If they fail again, note it as a persistent gap and proceed (don't loop on Quick Checks)

---

## Concept Map for TTT Sessions

When offered during Phase 3.5 of a TTT session, generate a concept map to help the learner visualize relationships between the concepts just taught. This uses the same node-type vocabulary as the concept-builder plugin but is self-contained -- no cross-plugin dependency.

### Format

Use a markdown nested list with the following node types and relationship labels.

**Node types** (in parentheses after node name):
- **(core)**: The sub-goal's central competency
- **(principle)**: Foundational ideas from the teaching blocks
- **(innovation)**: Key techniques or approaches
- **(application)**: Practical uses the learner should know
- **(prerequisite)**: Prior knowledge assumed by this sub-goal

**Relationship labels** as prefixes on nested groups:
`rests on`, `requires`, `led to`, `enables`

**Structure:**

```markdown
## Concept Map: <Sub-Goal Topic>

- **<Core Topic>** (core): <one-line description>
  - requires:
    - **<Prerequisite>** (prerequisite): <description>
  - rests on:
    - **<Principle from Gap 1>** (principle): <description>
      - led to:
        - **<Technique/Approach>** (innovation): <description>
    - **<Principle from Gap 2>** (principle): <description>
  - enables:
    - **<Application>** (application): <description>
```

### Design Rules

1. Use `shallow` depth: 5-8 nodes maximum
2. The (core) node is the sub-goal's topic, NOT the entire training plan topic
3. Principles should correspond to the gaps that were taught -- this makes the map a structural summary of what the learner just learned
4. Include 1-2 applications to connect the concepts to practical use
5. Keep descriptions to one line each
6. Do NOT include "Where to Go Next" suggestions -- the next step is the Final Test
