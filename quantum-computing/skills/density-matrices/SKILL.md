---
name: density-matrices
description: Density matrix formalism and mixed states in quantum computing. Use when the user asks about density matrices, density operators, mixed states vs pure states, partial trace, reduced density matrix, von Neumann entropy, quantum channels, Kraus operators, decoherence, quantum noise, CPTP maps, Bloch sphere for mixed states, purity, fidelity, trace distance, or open quantum systems.
---

# Density Matrices Skill

You are an instructor specializing in the density matrix formalism for quantum computing. You explain mixed states, quantum channels, decoherence, and entanglement measures with mathematical precision and physical clarity.

**Important**: The density matrix formalism is essential for real quantum computing because real qubits interact with their environment. Always emphasize that pure-state descriptions (|psi>) are a special case of the more general density matrix framework, and that density matrices are necessary whenever we deal with statistical mixtures, open systems, or subsystems of entangled states.

## Core Framework

### 1. Pure States vs. Mixed States

#### Pure States
- Described by a state vector |psi> or equivalently by rho = |psi><psi|
- Properties: rho^2 = rho, Tr(rho) = 1, Tr(rho^2) = 1
- Represent maximum knowledge about the system

#### Mixed States
- Statistical ensemble: rho = Sum_i p_i |psi_i><psi_i| with Sum_i p_i = 1
- Properties: rho = rho_dagger, Tr(rho) = 1, Tr(rho^2) <= 1, rho >= 0 (positive semi-definite)
- Represent incomplete knowledge (classical uncertainty) or entanglement with another system
- **Key distinction**: A mixed state is NOT a superposition. It represents classical ignorance, not quantum coherence.

#### Purity
- Purity = Tr(rho^2)
- Pure state: Tr(rho^2) = 1
- Maximally mixed state on d dimensions: rho = I/d, Tr(rho^2) = 1/d
- Range: 1/d <= Tr(rho^2) <= 1

### 2. Density Matrix Construction

#### From an ensemble
Given states |psi_i> with probabilities p_i:
```
rho = Sum_i p_i |psi_i><psi_i|
```

#### Single qubit examples

Maximally mixed state:
```
rho = (1/2) I = (1/2) [[1, 0],
                         [0, 1]]
```

Pure state |+> = (|0> + |1>)/sqrt(2):
```
rho = |+><+| = (1/2) [[1, 1],
                        [1, 1]]
```

Classical mixture of |0> and |1> with equal probability:
```
rho = (1/2)|0><0| + (1/2)|1><1| = (1/2) [[1, 0],
                                            [0, 1]]
```

Note: The maximally mixed state and the classical 50/50 mixture are the **same** density matrix. The density matrix captures all physically distinguishable information.

### 3. Bloch Sphere for Mixed States

Any single-qubit density matrix can be written:
```
rho = (1/2)(I + r_x*X + r_y*Y + r_z*Z)
```

Where **r** = (r_x, r_y, r_z) is the Bloch vector:
- |**r**| = 1: pure state (on the surface of the Bloch sphere)
- |**r**| < 1: mixed state (inside the Bloch sphere)
- |**r**| = 0: maximally mixed state (center of the sphere)

### 4. Partial Trace and Reduced Density Matrices

For a bipartite system rho_AB, the reduced density matrix of subsystem A is:
```
rho_A = Tr_B(rho_AB) = Sum_j <j|_B rho_AB |j>_B
```

#### Computation rules:
- Tr_B(|a1><a2| (x) |b1><b2|) = <b2|b1> * |a1><a2|
- Apply linearly to all terms

#### Why it matters:
- Subsystems of entangled states are always mixed
- For |Phi+> = (|00> + |11>)/sqrt(2): rho_A = (1/2)I (maximally mixed)
- This is the mathematical expression of "entanglement creates local uncertainty"

### 5. Time Evolution

#### Closed system (unitary)
```
rho(t) = U * rho(0) * U_dagger
```

#### Open system (quantum channel)
A quantum channel E is a completely positive, trace-preserving (CPTP) map:
```
E(rho) = Sum_k E_k * rho * E_k_dagger
```
where {E_k} are Kraus operators satisfying Sum_k E_k_dagger * E_k = I.

### 6. Common Quantum Channels

#### Bit-flip channel
```
E(rho) = (1-p) * rho + p * X * rho * X
```
Kraus operators: E_0 = sqrt(1-p) * I, E_1 = sqrt(p) * X

#### Phase-flip (dephasing) channel
```
E(rho) = (1-p) * rho + p * Z * rho * Z
```
Kraus operators: E_0 = sqrt(1-p) * I, E_1 = sqrt(p) * Z

#### Depolarizing channel
```
E(rho) = (1-p) * rho + (p/3) * (X*rho*X + Y*rho*Y + Z*rho*Z)
```
Equivalently: E(rho) = (1 - 4p/3) * rho + (4p/3) * (I/2)

#### Amplitude damping channel
Models energy relaxation (T1 decay):
```
E_0 = [[1, 0],            E_1 = [[0, sqrt(gamma)],
        [0, sqrt(1-gamma)]]       [0, 0]]
```
- gamma = 0: no damping
- gamma = 1: complete relaxation to |0>

### 7. Entropy and Information Measures

#### Von Neumann Entropy
```
S(rho) = -Tr(rho * log2(rho)) = -Sum_i lambda_i * log2(lambda_i)
```
where lambda_i are eigenvalues of rho.
- Pure state: S = 0
- Maximally mixed state on d dims: S = log2(d)
- Subadditivity: S(rho_AB) <= S(rho_A) + S(rho_B)
- Strong subadditivity: S(rho_ABC) + S(rho_B) <= S(rho_AB) + S(rho_BC)

#### Mutual Information
```
I(A:B) = S(rho_A) + S(rho_B) - S(rho_AB)
```
Measures total correlations (classical + quantum) between A and B.

#### Fidelity
Between two states rho and sigma:
```
F(rho, sigma) = (Tr(sqrt(sqrt(rho) * sigma * sqrt(rho))))^2
```
For a pure state |psi> and mixed state rho:
```
F(|psi>, rho) = <psi|rho|psi>
```
- F = 1: identical states
- F = 0: orthogonal states

#### Trace Distance
```
D(rho, sigma) = (1/2) * Tr(|rho - sigma|) = (1/2) * Tr(sqrt((rho - sigma)_dagger * (rho - sigma)))
```
- Operational interpretation: maximum probability of distinguishing rho from sigma in a single measurement

### 8. Entanglement Measures (via Density Matrices)

#### Entanglement Entropy
For a bipartite pure state |psi>_AB:
```
E(|psi>_AB) = S(rho_A) = S(rho_B)
```

#### Concurrence (2-qubit systems)
```
C(rho) = max(0, lambda_1 - lambda_2 - lambda_3 - lambda_4)
```
where lambda_i are square roots of eigenvalues of rho * (Y (x) Y) * rho* * (Y (x) Y), in decreasing order.

#### Entanglement of Formation
```
E_F(rho) = h((1 + sqrt(1 - C^2))/2)
```
where h(x) = -x*log2(x) - (1-x)*log2(1-x) is the binary entropy.

## Common Calculation Patterns

### Checking if a state is mixed or pure
1. Compute rho^2
2. If rho^2 = rho, the state is pure
3. Alternatively, compute Tr(rho^2). If < 1, the state is mixed

### Finding the Bloch vector
1. Compute r_x = Tr(rho * X)
2. Compute r_y = Tr(rho * Y)
3. Compute r_z = Tr(rho * Z)
4. The Bloch vector is **r** = (r_x, r_y, r_z)

### Applying a quantum channel
1. Identify the Kraus operators {E_k}
2. Compute each term E_k * rho * E_k_dagger
3. Sum all terms: E(rho) = Sum_k E_k * rho * E_k_dagger
4. Verify: Tr(E(rho)) = 1 and E(rho) is positive semi-definite
