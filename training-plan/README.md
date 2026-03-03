# Training Plan Plugin

Generate customized learning paths using **Test-Teach-Test (TTT)** methodology.

## How It Works

1. You provide a learning goal
2. The plugin decomposes it into testable sub-goals
3. For each sub-goal, you run a TTT session:
   - **Test** -- face a practical case immediately
   - **Teach** -- get targeted content for your gaps (if any)
   - **Test** -- prove mastery with a new case
4. Repeat until all sub-goals are complete
5. Sessions save checkpoints -- if interrupted, resume from where you left off
6. A learner profile tracks your progress, strengths, and gap patterns across all plans

## Commands

### `/create-training-plan <learning goal>`

Creates a full training plan with sub-goals and session blueprints. If a learner profile exists, it informs the plan design (harder tests for known strengths, proactive coverage for known weaknesses).

Example:
```
/create-training-plan I want to learn cost estimation for EPC construction projects
```

### `/run-session <sub-goal>`

Runs an interactive TTT session for one sub-goal. Saves checkpoints after each phase so interrupted sessions can be resumed. Optionally offers a concept map after the teaching phase.

Example:
```
/run-session SG-2
/run-session unit-rate estimation
```

### `/training-status`

Shows your cross-plan learning analytics: completion rates, strengths, recurring gap patterns, and recommendations for what to study next.

## Architecture

- **1 agent**: `training-planner` (orchestrator)
- **4 skills**: `goal-decomposer`, `ttt-session`, `content-builder`, `learner-analytics`
- **3 commands**: `/create-training-plan`, `/run-session`, `/training-status`

## Output Files

| File | Content |
|------|---------|
| `<topic>_training_plan.md` | Plan + progress tracking |
| `<topic>_session_SG<N>.md` | Session transcript per sub-goal |
| `<topic>_checkpoint_SG<N>.md` | In-progress session checkpoint (deleted on completion) |
| `learner_profile.md` | Persistent learner profile across all plans |

## Learning Science

See [PRINCIPLES.md](PRINCIPLES.md) for the cognitive science behind TTT and how this plugin addresses common learning risks (testing effect, desirable difficulty, fluency illusion, metacognitive blindness).
