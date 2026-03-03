---
description: "Test-Teach-Test session design and execution. Use when the user asks to run a session, start a learning session, test me on a topic, practice a skill, assess my knowledge, design a TTT learning cycle, or execute an adaptive test-teach-test loop for a sub-goal."
---

# TTT Session -- Domain Knowledge

Reference knowledge for designing and executing Test-Teach-Test learning sessions.

## Two Modes

This skill operates in two modes:

1. **Design mode** -- called during `/create-training-plan` to produce session blueprints
2. **Execute mode** -- called during `/run-session` to run the interactive TTT loop

---

## MODE 1: Design (Session Blueprints)

For each sub-goal, produce a session blueprint with this structure:

```markdown
### SG-<N>: <title>

**Initial Test**
- Case: <practical scenario description -- what the learner must do>
- Assesses: <specific competencies being tested>
- Pass criteria: <concrete, measurable threshold>

**Teach Phase Plan** (activated only if Initial Test reveals gaps)
- Concepts to cover: <list of key ideas>
- Exercises: <2-3 graduated exercises>
- Known pitfalls: <common errors and misconceptions for this topic>

**Final Test**
- Case: <different scenario, same competencies>
- Pass criteria: <same threshold as Initial Test>

**Adaptation Rules**
- If fails on <specific gap>: re-teach <specific content>
- Max loops: 2
```

### Blueprint Design Principles

1. **Initial Test cases must be practical and immediate** -- the learner receives a scenario and must act. No multiple-choice. No "explain the theory." Instead: "Here is a situation. Solve it."

2. **The Initial Test must be solvable** by someone who has the knowledge -- it's a diagnostic, not a trick question. A competent person should pass it in a few minutes.

3. **The Final Test must be a DIFFERENT scenario** testing the SAME competencies. If the Initial Test used Project A, the Final Test uses Project B. Same skills, new context -- this verifies transfer, not memorization.

4. **Pass criteria must be concrete**:
   - Good: "Identifies at least 8 of 10 cost categories"
   - Good: "Calculation within 5% of reference answer"
   - Bad: "Shows understanding" (not measurable)

5. **Adaptation rules map specific gaps to specific content** -- not "if fails, re-teach everything" but "if fails on indirect costs, re-teach indirect costs specifically."

---

## MODE 2: Execute (Interactive TTT Loop)

When running a session, follow this exact protocol:

### Phase 1: INITIAL TEST

Present the practical case from the session blueprint to the learner.

Rules:
- No preamble, no warm-up, no theory introduction
- Present the scenario and the task directly
- Ask the learner to respond
- Wait for the learner's response before proceeding

Example opening:
> **Practical Case -- SG-3: Unit-Rate Estimation**
>
> You have the following quantities for a warehouse foundation:
> - Concrete: 450 m3
> - Rebar: 38,000 kg
> - Formwork: 1,200 m2
>
> Unit rates: Concrete $180/m3, Rebar $2.10/kg, Formwork $45/m2
>
> **Task:** Calculate the total foundation cost. Show your work.

### Phase 2: EVALUATE

After the learner responds, evaluate against the pass criteria:

- **PASS** (meets or exceeds criteria): Skip to Phase 6 (RECORD). Sub-goal complete.
- **PARTIAL** (some gaps identified): Proceed to Phase 3. List specific gaps.
- **FAIL** (major gaps): Proceed to Phase 3. List all gaps.

When evaluating, identify gaps as specific, named deficits:
- Good: "Gap: does not distinguish direct from indirect costs"
- Good: "Gap: unit conversion error (confused kg with lb)"
- Bad: "Gap: doesn't understand the topic" (too vague to teach)

### Phase 3: TEACH

For each identified gap, generate a teaching block using the `content-builder` skill format:

1. Why This Matters (1-2 sentences)
2. Definition (clear, concise)
3. Simple Exercise (immediately solvable)
4. Typical Errors (what others get wrong)
5. Pitfalls & Misconceptions (wrong mental models)
6. Quick Check (one verification question)

Rules:
- Deliver ONE teaching block at a time
- Wait for the learner to complete the Quick Check before moving to the next block
- If the Quick Check fails, re-explain that specific point before moving on
- After ALL gaps are taught, proceed to Phase 3.5

### Phase 3.5: OPTIONAL CONCEPT MAP

After all teaching blocks are delivered, optionally offer a concept map (see content-builder skill for format). This is a brief offer -- proceed to Phase 4 regardless.

### Phase 4: FINAL TEST

Present a NEW practical case testing the same competencies:

- Different scenario from the Initial Test (different project, different numbers, different context)
- Same competencies being assessed
- Same pass criteria
- Same format (practical, immediate, no preamble)

### Phase 5: EVALUATE FINAL

Evaluate the Final Test response:

- **PASS**: Proceed to Phase 6. Sub-goal complete.
- **FAIL (Loop 1)**: Identify remaining gaps. Loop back to Phase 3 with NARROWER focus -- only re-teach the specific gaps that persist. Then present ANOTHER new Final Test case.
- **FAIL (Loop 2)**: This is the maximum. Record the result and flag: "Sub-goal needs additional review. Recommend revisiting prerequisites or seeking instructor support."

### Phase 6: RECORD

Update the training plan file, write the session transcript, delete checkpoint, update learner profile, and suggest next step.

---

## Adaptation Loop Summary

```text
Loop 0 (normal):  Initial Test -> Teach -> Final Test -> PASS
Loop 1 (retry):   Initial Test -> Teach -> Final Test -> FAIL -> Re-teach (narrower) -> Final Test 2 -> PASS
Loop 2 (max):     Initial Test -> Teach -> Final Test -> FAIL -> Re-teach -> Final Test 2 -> FAIL -> FLAG
```

Maximum 2 adaptation loops per sub-goal. After 2 failures, do not loop again -- record the result and recommend review.

---

## Checkpoint File Format

When a session is interrupted, the checkpoint file preserves progress so the session can be resumed.

Filename: `<topic>_checkpoint_SG<N>.md`

```markdown
# Session Checkpoint: SG-<N> -- <title>
Started: <date>

## Current Phase: <INITIAL_TEST|EVALUATE|TEACH|CONCEPT_MAP_OFFER|FINAL_TEST|EVALUATE_FINAL|RECORD>
<!-- For TEACH phase, also note: Gap <X> of <Y> completed -->

## Initial Test
**Case:** <what was presented>
**Learner response:** <what they said>

## Evaluation
**Result:** <PASS/PARTIAL/FAIL>
**Gaps identified:** <list>

## Teach Phase
### Gap: <name>
**Content:** <summary of what was taught>
**Quick Check:** <question> -> Learner: <answer> -> <correct/incorrect>

(repeat for each gap completed so far)

## Concept Map
(if generated during Phase 3.5)

## Final Test
**Case:** <what was presented>
**Learner response:** <what they said>

## Final Evaluation
**Result:** <PASS/FAIL>
```

Sections are populated incrementally as phases complete. Sections below the current phase marker are absent or empty.

## Resume Protocol

When resuming from a checkpoint:

1. Read the checkpoint file
2. Show the learner a brief summary of completed phases
3. Ask if they want to resume or start fresh
4. If resuming, skip to the phase AFTER the `## Current Phase` marker
5. For TEACH phase resume: skip already-delivered gaps (listed in checkpoint) and continue from the next undelivered gap
6. When the session completes normally, delete the checkpoint and write the final transcript as usual
