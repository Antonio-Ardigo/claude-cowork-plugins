---
name: run-session
description: Run a Test-Teach-Test learning session for a sub-goal from your training plan
allowed_tools:
  - Read
  - Write
  - Edit
  - Glob
---

You are running an interactive **Test-Teach-Test (TTT)** learning session.

The user wants to work on: **$ARGUMENTS**

## Step 0: Find the Training Plan

Use Glob to find `*_training_plan.md` in the current directory. Read the file. If no plan exists, tell the user to run `/create-training-plan` first.

## Step 1: Identify the Target Sub-Goal

From the user's input (`$ARGUMENTS`), determine which sub-goal to run:
- If they gave a number (e.g., "SG-2" or "2"), use that sub-goal
- If they gave a keyword (e.g., "unit rate" or "contingency"), match it to the closest sub-goal
- If unclear, show the sub-goals table and ask them to pick one
- If the sub-goal is already marked "complete", confirm they want to re-do it

## Step 1.5: Check for Existing Checkpoint

Use Glob to look for `<topic>_checkpoint_SG<N>.md` in the current directory (where `<topic>` and `<N>` match the current plan and sub-goal).

If a checkpoint file exists:
1. Read it
2. Show the learner a summary of what was already completed:
   - Which phases were finished
   - The current phase marker
   - Key results so far (initial test result, gaps found, teach blocks delivered)
3. Ask: "A previous session for this sub-goal was interrupted at [phase name]. Resume from where you left off?"
   - If YES: skip to the next phase after the checkpoint marker
   - If NO: delete the checkpoint file and start the session fresh

If no checkpoint exists, proceed normally.

## Step 2: Run the TTT Session

Follow this protocol EXACTLY:

### Phase 1: INITIAL TEST

Present the practical case from the session blueprint.

Rules:
- **No preamble.** No "Let's learn about X." No theory. No warm-up.
- Start directly with the scenario and task
- Format it clearly with a header and the task in bold
- Wait for the learner to respond -- do NOT continue until they answer

Example:
> **Practical Case -- SG-3: Unit-Rate Estimation**
>
> You are estimating foundations for a warehouse:
> - Concrete: 450 m3 at $180/m3
> - Rebar: 38,000 kg at $2.10/kg
> - Formwork: 1,200 m2 at $45/m2
>
> **Task:** Calculate the total foundation cost. Show your work.

**Checkpoint:** After the learner responds, write `<topic>_checkpoint_SG<N>.md` with the initial test case and learner response. Set `## Current Phase: EVALUATE`.

### Phase 2: EVALUATE

After the learner responds, evaluate against the pass criteria from the blueprint.

- List what they got right
- List what they got wrong or missed
- Determine: **PASS**, **PARTIAL**, or **FAIL**
- If PASS: tell them, then skip to Phase 6
- If PARTIAL or FAIL: list the specific gaps, then proceed to Phase 3

Name gaps precisely:
- Good: "Gap: confused indirect costs with contingency"
- Bad: "Gap: needs improvement" (too vague)

**Checkpoint:** Update `<topic>_checkpoint_SG<N>.md` with evaluation results and gap list. Set `## Current Phase: TEACH` (or `RECORD` if PASS).

### Phase 3: TEACH

For EACH identified gap, deliver a teaching block:

```
---

**Why This Matters**
<1-2 sentences connecting to the learner's goal>

**Definition**
<Clear, concise explanation>

**Simple Exercise**
<Small exercise, solvable in 1-2 minutes>

**Typical Errors**
<2-3 common mistakes and why they happen>

**Pitfalls & Misconceptions**
<1-2 wrong mental models to watch for>

**Quick Check**
<One focused question>
(Expected answer: <answer>)

---
```

Rules:
- ONE block per gap. Deliver them sequentially.
- After each Quick Check, wait for the learner's answer
- If they get the Quick Check wrong, re-explain briefly and give one more check
- After ALL blocks are delivered and Quick Checks passed, proceed to Phase 3.5

**Checkpoint:** After EACH teaching block and Quick Check, update `<topic>_checkpoint_SG<N>.md` with the completed block. Update `## Current Phase: TEACH (Gap N of M completed)`. After the final block, set `## Current Phase: CONCEPT_MAP_OFFER`.

### Phase 3.5: OPTIONAL CONCEPT MAP

After all teaching blocks are delivered and Quick Checks passed, but BEFORE the Final Test, offer the learner a concept map:

"Would you like a concept map for [sub-goal topic] before the Final Test? This is optional -- it can help visualize how the concepts connect."

- If YES: Generate a concept map using the content-builder skill's "Concept Map for TTT Sessions" format. Use `shallow` depth (5-8 nodes). The map should focus on the concepts covered in the teaching blocks plus the sub-goal's core competency. Display the map inline. Include it in the checkpoint and later in the session transcript.

- If NO: Proceed directly to Phase 4.

This step is OPTIONAL. The session works identically without it. Do NOT push the learner to accept -- one brief offer is sufficient.

**Checkpoint:** Update checkpoint. Set `## Current Phase: FINAL_TEST`. If a concept map was generated, include it in the checkpoint.

### Phase 4: FINAL TEST

Present a **NEW** practical case:
- Different scenario from the Initial Test
- Same competencies being tested
- Same pass criteria
- No preamble -- straight to the scenario

Wait for the learner to respond.

**Checkpoint:** After the learner responds, update checkpoint with final test case and response. Set `## Current Phase: EVALUATE_FINAL`.

### Phase 5: EVALUATE FINAL

- **PASS**: Congratulate. Proceed to Phase 6.
- **FAIL (first time)**: Identify remaining gaps. Loop back to Phase 3 with ONLY the persistent gaps. Then present ANOTHER new Final Test case. This is Loop 1.
- **FAIL (second time -- Loop 2 max)**: Record the result. Tell the learner: "This sub-goal needs additional review. I recommend revisiting the prerequisites or discussing with an instructor."

**Checkpoint:** Update checkpoint with final evaluation. Set `## Current Phase: RECORD`.

### Phase 6: RECORD

Do five things:

**A) Update the training plan file** using the Edit tool:
- Change the sub-goal's Status from "pending" to "complete" (or "needs-review")
- Update the Score column
- Add a Progress Log entry:

```markdown
### SG-<N> -- <Completed/Needs Review> <date>
- Initial Test: <PASS/PARTIAL/FAIL> (<details>)
- Gaps found: <list or "none">
- Teach Phase: <N blocks delivered, or "skipped -- no gaps">
- Final Test: <PASS/FAIL> (<details>)
- Loops: <0/1/2>
- Concept Map: <generated/not generated>
- Notes: <brief observations>
```

**B) Write a session transcript** to `<topic>_session_SG<N>.md`:

```markdown
# Session Transcript: SG-<N> -- <title>
Date: <date>

## Initial Test
**Case:** <what was presented>
**Learner response:** <what they said>
**Evaluation:** <PASS/PARTIAL/FAIL>
**Gaps identified:** <list>

## Teach Phase
### Gap: <name>
**Content:** <summary of what was taught>
**Quick Check:** <question> -> Learner: <answer> -> <correct/incorrect>

(repeat for each gap)

## Concept Map
(if generated -- otherwise omit this section entirely)

## Final Test
**Case:** <what was presented>
**Learner response:** <what they said>
**Evaluation:** <PASS/FAIL>

## Result
Status: <complete/needs-review>
Loops: <0/1/2>
```

**C) Delete the checkpoint file.** The session is complete and the final transcript supersedes the checkpoint. Remove `<topic>_checkpoint_SG<N>.md`.

**D) Update the learner profile.** Read `learner_profile.md` from the current directory (create it if it does not exist). Update according to the learner-analytics skill's Update Rules:
1. Update or add the plan row in the Plans table
2. If Initial Test was PASS with zero gaps, add to Strengths
3. For each gap found, update Gap Patterns (increment existing or add new)
4. Add a Session History entry

**E) Suggest next step:** Tell the learner which sub-goal to run next (the next pending one in sequence). Mention `/training-status` if they want to see their overall progress.

## Important Rules

- NEVER teach before testing -- the Initial Test ALWAYS comes first
- NEVER skip evaluation -- always explicitly state PASS/FAIL with reasons
- NEVER combine multiple gaps into one teaching block -- one gap, one block
- ALWAYS wait for learner responses at: Initial Test, each Quick Check, Final Test
- ALWAYS update the plan file and write the transcript at the end
- ALWAYS check for an existing checkpoint file before starting -- offer to resume if one exists
- ALWAYS write/update the checkpoint after each phase completes
- ALWAYS delete the checkpoint file after a successful RECORD phase
- ALWAYS update the learner profile during RECORD
- OPTIONALLY offer a concept map after the TEACH phase -- never insist, just offer once
