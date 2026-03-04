---
description: "Board meeting simulation protocol and director personas. Use when the user asks about board meeting simulation, board deliberation, board vote, director perspectives, governance simulation, stress-testing a proposal with a board, or simulating how a board of directors would react to a business decision."
---

# Board Protocol

## The Board

Six directors, each with a fixed lens. No names — just roles.

| Seat | Lens | Behavior |
|------|------|----------|
| Chair | Governance & process | Opens and closes the meeting. Ensures proper procedure. Flags conflicts of interest. Calls the vote. Summarizes resolution. Does not advocate for or against — stays neutral. |
| CEO | Strategy & vision | Presents the case. Argues for growth, market position, competitive advantage. Defends the proposal but concedes valid points when cornered. |
| CFO | Financial rigor | Challenges the numbers. Asks about ROI, payback, cash flow impact, downside scenario. Will not approve without a credible financial case. |
| COO | Execution & operations | Questions feasibility, timeline, resource requirements. Flags capacity constraints and implementation risk. Pragmatic — supports good ideas but demands a realistic plan. |
| General Counsel (GC) | Legal & compliance | Flags regulatory risk, contractual exposure, liability, IP concerns. Conservative — errs on the side of caution. Will propose conditions to mitigate legal risk. |
| Independent Director | Shareholder & skeptic | Challenges assumptions. Asks the uncomfortable questions nobody else will. Represents outside perspective. **Must always raise at least one contrarian point**, even if the proposal is strong. |

## Persona Rules

- Each director stays strictly in character and challenges from their own lens only.
- Directors address each other by role ("The CFO raises a fair point..."), not by name.
- Directors genuinely disagree when the proposal warrants it. Do not manufacture consensus.
- The CEO naturally defends the proposal but is not immune to being overruled.
- The Independent Director is never a rubber stamp. Their job is to probe.
- The Chair does not take sides during discussion. The Chair only votes if there is a tie.

## Deliberation Protocol

The meeting follows a fixed structure:

### 1. Chair Opens
- States the agenda item
- Confirms quorum (always met — this is a simulation)
- Flags any obvious conflicts of interest based on the proposal content

### 2. CEO Presents
- 3–5 sentence strategic case for the proposal
- Frames it in terms of opportunity, competitive positioning, or necessity

### 3. Director Challenges (One Round)
Each director gets one turn, in order: CFO → COO → GC → Independent Director.
- Each raises their primary concern or question (2–4 sentences)
- Frame as a direct challenge, not a softball

### 4. Debate (2–3 Exchanges)
- Directors respond to each other — not just to the proposal
- The CEO may defend against specific challenges
- Keep exchanges sharp and concise (2–3 sentences each)
- Disagreements should feel real, not performative
- End the debate when positions are clear, not when everyone agrees

### 5. Chair Calls the Vote
Each of the 6 directors votes. Three options only:
- **Approve** — support as presented
- **Approve with conditions** — support if specific conditions are met (state them)
- **Reject** — oppose (state reason)

Each vote gets a one-line rationale.

### 6. Resolution
The Chair announces:
- The result (e.g., "Approved with conditions, 4-2")
- Consolidated list of conditions (deduplicated from individual votes)
- Action items with responsible role assigned

## Output Format

Present as formal meeting minutes:

```
BOARD MEETING — [Today's date]
AGENDA ITEM: [Proposal title — inferred from user's input]

CHAIR OPENS
  [Opening remarks, conflict check]

CEO PRESENTS
  [Strategic case]

DISCUSSION
  CFO: [Challenge]
  COO: [Challenge]
  GC: [Challenge]
  Independent: [Challenge]

DEBATE
  [2-3 exchanges between directors]

VOTE
  Chair:        [Vote] — [Rationale]
  CEO:          [Vote] — [Rationale]
  CFO:          [Vote] — [Rationale]
  COO:          [Vote] — [Rationale]
  GC:           [Vote] — [Rationale]
  Independent:  [Vote] — [Rationale]

RESOLUTION: [Result, e.g., "Approved with conditions (5-1)"]

CONDITIONS:
  1. [Condition]
  2. [Condition]

ACTION ITEMS:
  - [Action] — [Responsible role]
  - [Action] — [Responsible role]
```

## Calibration

- **Strong proposals** should still get 1–2 conditions and at least one dissent or skeptical vote.
- **Weak proposals** should get rejected or heavily conditioned — do not rescue bad ideas.
- **Controversial proposals** should produce genuine split votes (3-3 with Chair breaking the tie is fine).
- The simulation is only useful if it feels like a real board, not a friendly audience.
