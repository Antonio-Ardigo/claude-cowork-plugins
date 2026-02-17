# Quantum Computing Concept Explainer Plugin

An AI-powered educational plugin that explains quantum computing concepts through structured research, mathematical formulation, worked examples, and intuitive insights.

## Key Features

- **LaTeX Formula Rendering**: All mathematical expressions use proper LaTeX notation (`$...$` for inline, `$$...$$` for display equations) — Dirac notation, matrices, operators, and more
- **Markdown File Export**: Every `/explain-concept` invocation automatically saves a complete `.md` report file with YAML frontmatter, LaTeX formulas, and references

> **Disclaimer:** This plugin is an educational tool. It provides structured explanations of quantum computing concepts but should not substitute for formal coursework, textbooks, or peer-reviewed research. Always verify mathematical derivations independently.

## Target Personas

- **Students** -- Learning quantum computing fundamentals, preparing for exams or research
- **Software Engineers** -- Transitioning into quantum computing, need practical understanding
- **Researchers** -- Quick reference for concepts outside their primary specialization
- **Educators** -- Structured material for teaching quantum computing topics

## Installation

```
claude plugins add knowledge-work-plugins/quantum-computing
```

## Quick Start

### 1. Explain any quantum computing concept

```
/explain-concept superposition
/explain-concept Grover's algorithm
/explain-concept density matrices
```

### 2. Configure depth level (optional)

Add a depth level to your request:
- `introductory` -- minimal math, focus on intuition
- `intermediate` -- full Dirac notation and matrices (default)
- `advanced` -- proofs, generalizations, research-level problems

Example:
```
/explain-concept quantum error correction --level advanced
```

## Command

### `/explain-concept` -- Quantum Concept Explainer

Explain a quantum computing concept through a six-phase structured workflow:

1. **Motivation** -- Why does this concept matter?
2. **Historical Context** -- How was it discovered? What problem did it solve?
3. **Mathematical Formulation** -- Algebraic and matrix representations
4. **Worked Examples** -- 5 progressively complex, fully developed examples
5. **"Aha" Insights** -- Intuition, misconceptions, analogies
6. **Summary Report** -- Comprehensive compiled report

```
/explain-concept <concept>
```

## Skills (15)

### Foundations
| Skill | Description |
|-------|-------------|
| `quantum-mechanics-basics` | Qubits, superposition, measurement, Born rule, postulates of QM |
| `entanglement` | Bell states, EPR pairs, entanglement measures, Schmidt decomposition, monogamy, GHZ/W states |
| `bell-inequalities` | Bell's theorem, CHSH inequality, local realism, Tsirelson bound, experimental tests, loopholes |

### Mathematics
| Skill | Description |
|-------|-------------|
| `algebraic-concepts` | Vector spaces, matrices, eigenvalues, tensor products, Hermitian/unitary operators, commutators |
| `clifford-algebra` | Clifford algebra, Pauli group, Clifford group, stabilizer formalism, Gottesman-Knill theorem |
| `group-theory` | Symmetry groups, SU(2), representations, Lie algebras, hidden subgroup problem |

### Algorithms and Protocols
| Skill | Description |
|-------|-------------|
| `quantum-algorithms` | Shor's, Grover's, QPE, VQE, QAOA, Deutsch-Jozsa, complexity classes |
| `quantum-fourier-transform` | QFT definition, circuit decomposition, phase estimation, period finding |
| `quantum-teleportation` | Teleportation protocol, gate teleportation, quantum repeaters, QKD, MBQC |
| `superdense-coding` | Dense coding protocol, Holevo bound, quantum channel capacity |
| `density-matrices` | Mixed states, partial trace, quantum channels, Kraus operators, decoherence |

### Experiments and Hardware
| Skill | Description |
|-------|-------------|
| `quantum-experiments` | NMR, IR spectroscopy, Raman, ESR/EPR, Stern-Gerlach, quantum hardware platforms |

### History and Resources
| Skill | Description |
|-------|-------------|
| `history-quantum-mechanics` | Planck to modern interpretations -- ultraviolet catastrophe, Bohr, Heisenberg, Schrodinger, EPR |
| `history-quantum-computing` | Feynman to NISQ era -- Deutsch, Shor, Grover, quantum supremacy, hardware generations |
| `quantum-textbooks` | Textbook reviews, learning paths, online courses, study roadmaps by background |

## Example Workflows

### Learn a New Concept

1. Run `/explain-concept quantum entanglement`
2. Read the motivation and historical context for background
3. Work through the mathematical formulation
4. Follow all 5 examples step by step
5. Review the "aha" insights to solidify understanding
6. Use the self-assessment questions to test yourself

### Quick Reference

Ask about a specific aspect:
- "What are the Pauli matrices and their commutation relations?"
- "Show me the circuit for 3-qubit QFT"
- "What is the partial trace of a Bell state?"

The skills will activate automatically and provide structured answers.

### Exam Preparation

1. Run `/explain-concept` on each topic in your syllabus
2. Focus on the worked examples and self-assessment questions
3. Use the misconceptions tables to identify common errors

### Export Reports

Every concept explanation is automatically saved as a Markdown file:
- Filename: `quantum-concept-<concept-name>.md`
- Includes YAML frontmatter with title, date, level, and tags
- All LaTeX formulas preserved for rendering in any Markdown viewer that supports math (VS Code, Obsidian, Typora, GitHub, Jupyter, etc.)

## File Structure

```
quantum-computing/
+-- .claude-plugin/plugin.json
+-- README.md
+-- CONNECTORS.md
+-- commands/
|   +-- explain-concept.md
+-- skills/
    +-- quantum-mechanics-basics/SKILL.md
    +-- algebraic-concepts/SKILL.md
    +-- clifford-algebra/SKILL.md
    +-- group-theory/SKILL.md
    +-- quantum-algorithms/SKILL.md
    +-- quantum-fourier-transform/SKILL.md
    +-- density-matrices/SKILL.md
    +-- entanglement/SKILL.md
    +-- bell-inequalities/SKILL.md
    +-- quantum-teleportation/SKILL.md
    +-- superdense-coding/SKILL.md
    +-- quantum-experiments/SKILL.md
    +-- history-quantum-mechanics/SKILL.md
    +-- history-quantum-computing/SKILL.md
    +-- quantum-textbooks/SKILL.md
```

## References

Key textbooks and resources used as reference standards:

- **Nielsen & Chuang** -- *Quantum Computation and Quantum Information* (the standard textbook)
- **Preskill** -- *Quantum Information and Computation* (Caltech lecture notes)
- **Mermin** -- *Quantum Computer Science: An Introduction*
- **Wilde** -- *From Classical to Quantum Shannon Theory*
- **Kaye, Laflamme, Mosca** -- *An Introduction to Quantum Computing*
