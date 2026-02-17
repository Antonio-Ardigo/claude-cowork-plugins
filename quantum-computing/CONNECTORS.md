# Connectors

## How tool references work

This plugin is primarily self-contained and does not require external tool connections. It uses Claude's built-in knowledge of quantum computing, physics, and mathematics.

However, if connected tools are available, they can enhance the workflow:

## Optional Connectors

| Category | Placeholder | Use Case |
|----------|-------------|----------|
| Web search | `~~web` | Look up recent research papers, experimental results, or hardware specifications |
| File system | `~~files` | Save generated reports, read user-provided problem sets or lecture notes |
| Notebook | `~~notebook` | Generate Jupyter notebooks with Qiskit or Cirq code for the worked examples |

## Notes

- This plugin works fully without any external connectors
- All quantum computing knowledge is drawn from Claude's training data
- For the latest research results or hardware specifications, web search may be helpful
- For interactive computation and visualization, Jupyter notebook integration is recommended
