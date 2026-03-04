---
name: board-meeting
description: Simulate a board of directors meeting. Present a proposal and get it debated, challenged, and voted on by six directors.
allowed_tools:
  - Read
  - Glob
  - Grep
---

# Board Meeting

Simulate a board of directors deliberation on a proposal.

## Step 1: Get the Proposal

If the user has already provided a proposal, use it. If not, ask:

"What proposal should the board consider? Describe it in a few sentences — what you want to do, why, and the rough cost or commitment involved."

If the user provides a file, read it and extract the proposal.

## Step 2: Run the Simulation

Follow the board-protocol skill exactly. Execute the full meeting sequence:

1. Chair opens — frame the agenda item, flag any conflicts
2. CEO presents the strategic case (3–5 sentences)
3. Each director challenges in order: CFO, COO, GC, Independent Director
4. 2–3 rounds of debate between directors
5. Chair calls the vote — each director votes with rationale
6. Chair announces resolution, conditions, and action items

## Step 3: Format as Meeting Minutes

Present the full output in the meeting minutes format defined in board-protocol.

## Rules

- Do NOT ask the user to configure the board or pick directors. The board is fixed.
- Do NOT break character mid-simulation or add meta-commentary between sections.
- Do NOT soften the challenges. The simulation is useful because it's honest.
- Run the entire meeting in a single response — do not pause for user input mid-meeting.
- Keep the total output concise — aim for roughly 600–900 words. Tight, not bloated.
