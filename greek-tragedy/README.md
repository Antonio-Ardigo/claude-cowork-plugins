# Greek Tragedy Classifier

Classify Greek tragedies as **Apollonian**, **Dionysiac**, or a **mixture** using the aesthetic framework from Nietzsche's *The Birth of Tragedy* (1872).

## What this plugin does

This plugin provides a structured six-dimensional analysis for classifying Greek tragedies according to Nietzsche's two fundamental aesthetic drives:

- **Apollonian**: Individuation, form, beauty, dream, rational order, measured suffering
- **Dionysiac**: Dissolution, excess, intoxication, the chorus as ritual body, boundary-violation, the primal unity

The classification is based on *abstract aesthetic and structural qualities* -- never on whether specific gods appear as characters.

## Command

### `/classify-tragedy`

Runs a six-step workflow:
1. Identify and contextualize the tragedy
2. Analyze across six dimensions (chorus, individuation, suffering, resolution, language, body/boundaries)
3. Map the tension between Apollonian and Dionysiac impulses
4. Render a classification with scorecard
5. Compare multiple tragedies (if requested)
6. Export analysis as a `.md` file

## Skills

| Skill | Description |
|-------|-------------|
| `apollonian` | The Apollonian aesthetic principle -- individuation, form, beauty, dream, rational order |
| `dionysiac` | The Dionysiac aesthetic principle -- dissolution, excess, intoxication, boundary-violation, primal unity |

## Installation

This plugin is part of the `claude-cowork-plugins` marketplace.
