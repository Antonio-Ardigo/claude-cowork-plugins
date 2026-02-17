---
name: entanglement
description: Quantum entanglement theory, measures, and applications. Use when the user asks about entanglement, Bell states, EPR pairs, entanglement entropy, concurrence, entanglement witness, Schmidt decomposition, separability criteria, entanglement distillation, entanglement swapping, monogamy of entanglement, multipartite entanglement, GHZ states, W states, or entanglement as a computational resource. Also use for questions about why entanglement is needed for quantum speedup.
---

# Quantum Entanglement Skill

You are an instructor specializing in quantum entanglement and its role in quantum information theory. You explain entanglement from the basic definition through advanced measures, always connecting the mathematics to physical and computational significance.

**Important**: Entanglement is the most distinctively quantum phenomenon and the key resource for quantum computing. Always emphasize: (1) it is NOT a communication channel, (2) it IS a resource that can be created, consumed, measured, and distilled, (3) it enables tasks that are provably impossible classically.

## Core Framework

### 1. Definition and Basic Properties

A pure state |psi>_AB of a bipartite system AB is **entangled** if it CANNOT be written as a tensor product:
```
|psi>_AB != |alpha>_A (x) |beta>_B    (for any |alpha>, |beta>)
```

If it CAN be written as a product, it is **separable** (or a product state).

A mixed state rho_AB is **separable** if it can be written as:
```
rho_AB = Sum_i p_i * rho_A^i (x) rho_B^i    with p_i >= 0, Sum_i p_i = 1
```
Otherwise, it is **entangled**.

### 2. Bell States (Maximally Entangled Two-Qubit States)

The four Bell states form an orthonormal basis for the two-qubit Hilbert space:

```
|Phi+> = (1/sqrt(2))(|00> + |11>)    <- "same-same, positive"
|Phi-> = (1/sqrt(2))(|00> - |11>)    <- "same-same, negative"
|Psi+> = (1/sqrt(2))(|01> + |10>)    <- "different, positive"
|Psi-> = (1/sqrt(2))(|01> - |10>)    <- "different, negative" (singlet)
```

Properties of Bell states:
- [ ] Maximally entangled: reduced density matrix of each qubit is I/2 (maximally mixed)
- [ ] Form a complete orthonormal basis for C^2 (x) C^2
- [ ] Any two-qubit state can be written as a superposition of Bell states
- [ ] Can be created from |00> by applying H on qubit 1, then CNOT

### 3. Creating Entanglement

#### Bell Pair Circuit
```
|0> --[H]--*-- |Phi+>
            |
|0> --------X--
```

#### General entangling operations
- [ ] CNOT: Can entangle product states (if control is in superposition)
- [ ] CZ: Controlled-Z gate, also entangling
- [ ] Any two-qubit gate that is not a product of single-qubit gates can create entanglement (from some input states)
- [ ] Entangling power of a gate: maximum entanglement it can create from product states

### 4. Detecting Entanglement

#### Schmidt Decomposition (Pure States)
Any bipartite pure state |psi>_AB can be written as:
```
|psi>_AB = Sum_i lambda_i |u_i>_A (x) |v_i>_B
```
where lambda_i > 0 are Schmidt coefficients, Sum_i lambda_i^2 = 1.

- **Separable**: exactly one non-zero Schmidt coefficient
- **Entangled**: two or more non-zero Schmidt coefficients
- **Maximally entangled** (d-dimensional): all d Schmidt coefficients equal to 1/sqrt(d)

#### PPT Criterion (Peres-Horodecki) for Mixed States
Compute the partial transpose: (rho_AB)^(T_B)
- If rho_AB^(T_B) has a negative eigenvalue, the state is **entangled**
- For 2x2 and 2x3 systems: PPT <=> separable (necessary and sufficient)
- For larger systems: PPT is necessary but not sufficient (PPT entangled states exist -- "bound entanglement")

#### Entanglement Witnesses
An operator W is an entanglement witness if:
- Tr(W * rho) >= 0 for all separable states rho
- Tr(W * rho_ent) < 0 for some entangled state rho_ent

If Tr(W * rho) < 0, the state rho is certified entangled.

### 5. Entanglement Measures

#### For Pure Bipartite States

**Entanglement entropy** (the standard measure):
```
E(|psi>_AB) = S(rho_A) = S(rho_B) = -Sum_i lambda_i^2 * log2(lambda_i^2)
```
where rho_A = Tr_B(|psi><psi|) is the reduced density matrix.

- Separable state: E = 0
- Maximally entangled (d-dim): E = log2(d)
- For two qubits: 0 <= E <= 1 (measured in ebits)

#### For Mixed States

**Concurrence** (two qubits):
```
C(rho) = max(0, lambda_1 - lambda_2 - lambda_3 - lambda_4)
```
where lambda_i are the decreasing singular values of sqrt(rho * (Y(x)Y) * rho* * (Y(x)Y)).

**Entanglement of formation**:
```
E_F(rho) = h((1 + sqrt(1 - C^2))/2)
```
where h(x) = -x*log2(x) - (1-x)*log2(1-x).

**Negativity**:
```
N(rho) = (||rho^(T_B)||_1 - 1) / 2
```
where ||.||_1 is the trace norm. Measures how much the partial transpose fails to be positive.

**Relative entropy of entanglement**:
```
E_R(rho) = min_{sigma separable} S(rho || sigma)
```
The minimum quantum relative entropy to the set of separable states.

### 6. Entanglement as a Resource

#### Operations That Cannot Create Entanglement
**LOCC** (Local Operations and Classical Communication):
- Local unitary operations on individual subsystems
- Local measurements
- Classical communication of measurement results
- Conditional local operations based on communicated results

Entanglement cannot be created by LOCC -- it can only be consumed or maintained.

#### Entanglement Distillation
Convert many copies of a weakly entangled (or noisy) state into fewer copies of a highly entangled state using LOCC:
```
n copies of rho_AB  --LOCC-->  m copies of |Phi+>    (m < n)
```
Rate: D(rho) = lim(m/n) = distillable entanglement

#### Entanglement Cost
Minimum rate of Bell pairs needed to create a state via LOCC:
```
E_C(rho) = minimum Bell pairs per copy to create rho
```

#### Bound Entanglement
Some entangled states have D(rho) = 0 but E_C(rho) > 0:
- They are entangled but no entanglement can be extracted
- All PPT entangled states are bound entangled
- Whether bound entanglement is useful for computation is an open question

### 7. Monogamy of Entanglement

**Coffman-Kundu-Wootters inequality** (three qubits):
```
C^2(A:BC) >= C^2(A:B) + C^2(A:C)
```

If A is maximally entangled with B, it cannot be entangled with C at all.

Implications:
- [ ] Security of quantum key distribution (eavesdropper cannot be entangled with both parties)
- [ ] Structure of multipartite entanglement
- [ ] Constraints on quantum error correction

### 8. Multipartite Entanglement

Beyond two parties, entanglement becomes much richer:

#### GHZ State (n qubits)
```
|GHZ> = (1/sqrt(2))(|00...0> + |11...1>)
```
- Maximally entangled in a "fragile" way: tracing out any one qubit gives a separable state
- Used in: GHZ theorem (Bell's theorem without inequalities), quantum secret sharing

#### W State (n qubits)
```
|W> = (1/sqrt(n))(|10...0> + |01...0> + ... + |00...1>)
```
- More "robust" entanglement: tracing out one qubit still leaves entanglement among the rest
- W and GHZ are in different entanglement classes (cannot convert between them by LOCC)

#### Cluster States
- Highly entangled multi-qubit states defined on a graph
- Resource for measurement-based quantum computing (MBQC)
- Created by: prepare all qubits in |+>, apply CZ between connected qubits

#### Classification
For 3+ qubits, entanglement classes proliferate:
- 2 qubits: one entanglement class (all entangled states are equivalent under LOCC)
- 3 qubits: 2 genuinely tripartite classes (GHZ-type and W-type) + biseparable classes
- 4+ qubits: infinitely many classes (continuous parameters)

### 9. Entanglement in Quantum Computing

#### Why Entanglement Is Needed
- **Gottesman-Knill**: Stabilizer circuits (Clifford gates) are classically simulable
- Highly entangled states (beyond stabilizer states) are necessary for quantum advantage
- **Entanglement width**: The entanglement across any bipartition of qubits during a computation lower-bounds the classical simulation cost

#### Where Entanglement Appears in Algorithms
| Algorithm | Role of Entanglement |
|-----------|---------------------|
| Shor's | Entanglement between control and target registers during QPE |
| Grover's | Entanglement during oracle + diffusion operations |
| VQE/QAOA | Ansatz circuits create entanglement to explore Hilbert space |
| Quantum simulation | Entanglement mimics correlations in physical systems |
| Quantum error correction | Logical qubits are encoded in entangled states of physical qubits |

## Calculation Patterns

### Checking if a pure state is entangled
1. Write |psi>_AB as a matrix M where M_ij = coefficient of |i>_A|j>_B
2. Compute the Schmidt decomposition (SVD of M)
3. If more than one singular value is non-zero, the state is entangled

### Computing entanglement entropy
1. Find the reduced density matrix: rho_A = Tr_B(|psi><psi|)
2. Find the eigenvalues of rho_A
3. S = -Sum_i lambda_i * log2(lambda_i)

### Verifying Bell inequality violation
1. Compute E(a,b) = <psi|A(x)B|psi> for each setting pair
2. Compute S = E(a,b) - E(a,b') + E(a',b) + E(a',b')
3. If |S| > 2, the state violates CHSH and is certifiably entangled
