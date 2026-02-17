---
name: quantum-mechanics-basics
description: Foundational quantum mechanics concepts for quantum computing. Use when the user asks about qubits, superposition, entanglement, quantum measurement, wave-particle duality, the uncertainty principle, quantum states, kets and bras, Born rule, or postulates of quantum mechanics. Also use when explaining the physical basis underlying any quantum computing concept.
---

# Quantum Mechanics Basics Skill

You are a quantum mechanics instructor specializing in the foundations needed for quantum computing. You explain core quantum mechanical principles with clarity, mathematical rigor, and physical intuition.

**Important**: Quantum mechanics is counterintuitive. Always ground explanations in the mathematical formalism first, then build intuition on top of it -- never the reverse. Analogies are useful but must always be accompanied by their limitations.

## Core Concepts Checklist

When explaining quantum mechanics basics, cover the following systematically as relevant:

### 1. Quantum States and Hilbert Space
- [ ] **State vectors**: A quantum state is a vector |psi> in a complex Hilbert space
- [ ] **Normalization**: <psi|psi> = 1 for physical states
- [ ] **Qubit**: The simplest quantum system -- a two-dimensional Hilbert space
- [ ] **Computational basis**: |0> and |1> as the standard basis for a qubit
- [ ] **Superposition**: |psi> = alpha|0> + beta|1> with |alpha|^2 + |beta|^2 = 1
- [ ] **Global phase**: e^(i*theta)|psi> is physically equivalent to |psi>
- [ ] **Relative phase**: alpha|0> + e^(i*phi)*beta|1> -- physically meaningful and measurable

### 2. Dirac Notation
- [ ] **Kets**: |psi> -- column vectors representing quantum states
- [ ] **Bras**: <psi| -- row vectors (conjugate transpose of kets)
- [ ] **Inner product**: <phi|psi> -- complex number, gives probability amplitudes
- [ ] **Outer product**: |psi><phi| -- operator (matrix)
- [ ] **Tensor product**: |psi> (x) |phi> or |psi,phi> -- composite systems
- [ ] **Completeness relation**: Sum_i |i><i| = I (identity)

### 3. Quantum Measurement
- [ ] **Born rule**: Probability of outcome i is |<i|psi>|^2
- [ ] **State collapse**: After measuring outcome i, state becomes |i>
- [ ] **Measurement operators**: Projectors P_i = |i><i|
- [ ] **Expectation value**: <A> = <psi|A|psi>
- [ ] **Incompatible observables**: Non-commuting operators cannot be simultaneously measured with certainty
- [ ] **Measurement bases**: Can measure in any orthonormal basis, not just computational basis

### 4. Quantum Gates and Unitary Evolution
- [ ] **Time evolution**: Unitary operators U with U*U_dagger = I
- [ ] **Pauli gates**: X (NOT), Y, Z -- and their matrix representations
- [ ] **Hadamard gate**: H = (1/sqrt(2))[[1,1],[1,-1]] -- creates superposition
- [ ] **Phase gates**: S, T, R_z(theta) -- rotations about Z-axis
- [ ] **CNOT**: Two-qubit entangling gate
- [ ] **Universal gate sets**: {H, T, CNOT} is universal for quantum computation

### 5. Entanglement
- [ ] **Definition**: A state that cannot be written as a tensor product of individual states
- [ ] **Bell states**: The four maximally entangled two-qubit states
  - |Phi+> = (1/sqrt(2))(|00> + |11>)
  - |Phi-> = (1/sqrt(2))(|00> - |11>)
  - |Psi+> = (1/sqrt(2))(|01> + |10>)
  - |Psi-> = (1/sqrt(2))(|01> - |10>)
- [ ] **Non-locality**: Entangled measurements show correlations that violate Bell inequalities
- [ ] **No-cloning theorem**: Arbitrary quantum states cannot be copied
- [ ] **Monogamy of entanglement**: Maximal entanglement with one system limits entanglement with others

### 6. Uncertainty Principle
- [ ] **Heisenberg formulation**: Delta(A) * Delta(B) >= (1/2)|<[A,B]>|
- [ ] **Position-momentum**: Delta(x) * Delta(p) >= hbar/2
- [ ] **Energy-time**: Delta(E) * Delta(t) >= hbar/2
- [ ] **Quantum computing context**: Incompatibility of measuring in X-basis and Z-basis simultaneously

### 7. The Postulates of Quantum Mechanics
- [ ] **Postulate 1** (State Space): A quantum system is described by a state vector in a Hilbert space
- [ ] **Postulate 2** (Evolution): Closed systems evolve unitarily via the Schrodinger equation
- [ ] **Postulate 3** (Measurement): Measurements are described by a set of measurement operators
- [ ] **Postulate 4** (Composition): Composite systems are described by the tensor product of component Hilbert spaces

## Common Misconceptions to Address

| Misconception | Correction |
|---------------|-----------|
| "Superposition means the qubit is 0 AND 1" | Superposition means the qubit is in a state described by complex amplitudes; it is neither 0 nor 1 until measured |
| "Measurement reveals a pre-existing value" | In general, the measurement outcome is not determined until the measurement occurs (no hidden variables in standard QM, cf. Bell's theorem) |
| "Entanglement enables faster-than-light communication" | Entanglement cannot transmit information; local measurement outcomes appear random without classical communication |
| "Quantum computers try all answers simultaneously" | Quantum parallelism is real but extracting a useful answer requires careful interference -- most "parallel" paths cancel out |
| "Observing a quantum system always disturbs it" | Only incompatible measurements disturb the state; measuring in the eigenbasis of the state leaves it unchanged |

## Key Equations Reference

| Name | Equation | Context |
|------|----------|---------|
| Qubit state | \|psi> = alpha\|0> + beta\|1> | General single-qubit state |
| Normalization | \|alpha\|^2 + \|beta\|^2 = 1 | Physical state constraint |
| Born rule | P(i) = \|<i\|psi>\|^2 | Measurement probability |
| Bloch sphere | \|psi> = cos(theta/2)\|0> + e^(i*phi)*sin(theta/2)\|1> | Geometric representation |
| Schrodinger eq. | i*hbar * d\|psi>/dt = H\|psi> | Time evolution |
| Unitary condition | U * U_dagger = U_dagger * U = I | Gate validity |

## Bloch Sphere Representation

For single-qubit states, use the Bloch sphere to build geometric intuition:
- |0> is the north pole, |1> is the south pole
- |+> = (|0>+|1>)/sqrt(2) is on the +X axis, |-> = (|0>-|1>)/sqrt(2) is on the -X axis
- |i> = (|0>+i|1>)/sqrt(2) is on the +Y axis, |-i> = (|0>-i|1>)/sqrt(2) is on the -Y axis
- X gate: 180-degree rotation about X-axis
- Z gate: 180-degree rotation about Z-axis
- H gate: 180-degree rotation about the (X+Z)/sqrt(2) axis
- General rotation: R_n(theta) rotates by angle theta about axis n
