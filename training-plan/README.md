# Training Plan Plugin

Generate customized learning paths using **Test-Teach-Test (TTT)** methodology.

## How It Works

1. You provide a learning goal
2. The plugin decomposes it into testable sub-goals
3. For each sub-goal, you run a TTT session:
   - **Test** — face a practical case immediately
   - **Teach** — get targeted content for your gaps (if any)
   - **Test** — prove mastery with a new case
4. Repeat until all sub-goals are complete

## Commands

### `/create-training-plan <learning goal>`

Creates a full training plan with sub-goals and session blueprints.

Example:
```
/create-training-plan I want to learn cost estimation for EPC construction projects
```

### `/run-session <sub-goal>`

Runs an interactive TTT session for one sub-goal.

Example:
```
/run-session SG-2
/run-session unit-rate estimation
```

## Architecture

- **1 agent**: `training-planner` (orchestrator)
- **3 skills**: `goal-decomposer`, `ttt-session`, `content-builder`
- **2 commands**: `/create-training-plan`, `/run-session`

## Output Files

| File | Content |
|------|---------|
| `<topic>_training_plan.md` | Plan + progress tracking |
| `<topic>_session_SG<N>.md` | Session transcript per sub-goal |
