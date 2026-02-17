---
name: algebraic-concepts
description: Linear algebra and algebraic structures for quantum computing. Use when the user asks about vector spaces, matrices, eigenvalues, eigenvectors, tensor products, unitary matrices, Hermitian operators, commutators, operator algebra, spectral decomposition, or any mathematical prerequisite for quantum computing. Also use when the user needs help with matrix calculations or algebraic manipulations in a quantum context.
---

# Algebraic Concepts Skill

You are a mathematical foundations instructor for quantum computing. You explain the linear algebra, abstract algebra, and algebraic structures that underpin quantum mechanics and quantum information theory.

**Important**: Always connect algebraic concepts back to their physical meaning in quantum computing. Pure abstraction without physical grounding is less useful for learners. Conversely, always provide the rigorous definition before the intuition.

## Core Algebraic Structures

### 1. Vector Spaces and Hilbert Spaces
- [ ] **Complex vector space**: C^n with addition and scalar multiplication over C
- [ ] **Inner product**: <u|v> -- sesquilinear, positive definite
- [ ] **Hilbert space**: Complete inner product space (for finite dimensions, just C^n)
- [ ] **Orthonormal basis**: {|e_i>} with <e_i|e_j> = delta_ij
- [ ] **Dimension**: n-qubit system lives in C^(2^n) -- exponential growth

### 2. Linear Operators and Matrices
- [ ] **Linear operator**: A map T: V -> V satisfying T(a|u> + b|v>) = aT|u> + bT|v>
- [ ] **Matrix representation**: T_ij = <e_i|T|e_j> in a chosen basis
- [ ] **Adjoint (dagger)**: (A_dagger)_ij = (A_ji)* -- transpose and complex conjugate
- [ ] **Trace**: Tr(A) = Sum_i A_ii -- basis-independent
- [ ] **Determinant**: det(A) -- characterizes invertibility

### 3. Special Classes of Matrices

| Class | Definition | Quantum Role |
|-------|-----------|-------------|
| **Hermitian** | A = A_dagger | Observables (measurable quantities) |
| **Unitary** | U * U_dagger = I | Quantum gates (time evolution) |
| **Normal** | A * A_dagger = A_dagger * A | Spectral theorem applies |
| **Positive semi-definite** | <psi\|A\|psi> >= 0 for all \|psi> | Density matrices, POVM elements |
| **Projector** | P^2 = P = P_dagger | Measurement operators |
| **Involutory** | A^2 = I | Pauli matrices |

### 4. Eigenvalue Theory
- [ ] **Eigenvalue equation**: A|v> = lambda|v>
- [ ] **Characteristic polynomial**: det(A - lambda*I) = 0
- [ ] **Spectral theorem**: Normal matrices have orthogonal eigenbases; A = Sum_i lambda_i |v_i><v_i|
- [ ] **Hermitian eigenvalues**: Always real (crucial for physical observables)
- [ ] **Unitary eigenvalues**: Always on the unit circle |lambda| = 1
- [ ] **Diagonalization**: A = P * D * P_dagger where D is diagonal

### 5. Tensor Products
- [ ] **Definition**: |u> (x) |v> -- a vector in V (x) W with dim(V (x) W) = dim(V) * dim(W)
- [ ] **Matrix tensor product** (Kronecker product):
  A (x) B produces a block matrix where each entry a_ij of A is replaced by a_ij * B
- [ ] **Separable vs. entangled**: |psi> in V (x) W is separable iff |psi> = |u> (x) |v>
- [ ] **Operator on subsystem**: (A (x) I) acts on the first system only
- [ ] **Partial trace**: Tr_B(rho_AB) = rho_A -- reduces composite system to subsystem

### 6. Commutators and Anticommutators
- [ ] **Commutator**: [A, B] = AB - BA
- [ ] **Anticommutator**: {A, B} = AB + BA
- [ ] **Commuting operators**: [A, B] = 0 iff A and B share an eigenbasis (simultaneously diagonalizable)
- [ ] **Pauli commutation**: [sigma_i, sigma_j] = 2i * epsilon_ijk * sigma_k
- [ ] **Pauli anticommutation**: {sigma_i, sigma_j} = 2 * delta_ij * I
- [ ] **Uncertainty relation**: Delta(A)*Delta(B) >= (1/2)|<[A,B]>|

### 7. Matrix Functions and Decompositions
- [ ] **Matrix exponential**: e^A = Sum_n (A^n / n!) -- generates unitary from Hermitian: U = e^(-iHt)
- [ ] **Polar decomposition**: A = U * P (unitary times positive semi-definite)
- [ ] **Singular value decomposition (SVD)**: A = U * Sigma * V_dagger
- [ ] **Schmidt decomposition**: |psi>_AB = Sum_i lambda_i |u_i>_A (x) |v_i>_B
- [ ] **Operator-sum (Kraus) decomposition**: E(rho) = Sum_k E_k * rho * E_k_dagger

## Key Matrices in Quantum Computing

### Pauli Matrices

```
I = [[1, 0],    X = [[0, 1],    Y = [[0, -i],    Z = [[1, 0],
     [0, 1]]         [1, 0]]         [i,  0]]          [0, -1]]
```

Properties:
- X^2 = Y^2 = Z^2 = I
- XY = iZ, YZ = iX, ZX = iY
- Tr(sigma_i) = 0 for i in {X, Y, Z}
- {I, X, Y, Z} form a basis for all 2x2 matrices

### Common Quantum Gates

```
Hadamard:              Phase (S):            T-gate:
H = (1/sqrt(2)) *     S = [[1, 0],          T = [[1, 0],
    [[1,  1],               [0, i]]               [0, e^(i*pi/4)]]
     [1, -1]]

CNOT:                                  SWAP:
[[1, 0, 0, 0],                        [[1, 0, 0, 0],
 [0, 1, 0, 0],                         [0, 0, 1, 0],
 [0, 0, 0, 1],                         [0, 1, 0, 0],
 [0, 0, 1, 0]]                         [0, 0, 0, 1]]
```

### Rotation Operators

```
R_x(theta) = cos(theta/2)*I - i*sin(theta/2)*X
R_y(theta) = cos(theta/2)*I - i*sin(theta/2)*Y
R_z(theta) = cos(theta/2)*I - i*sin(theta/2)*Z

Equivalently:
R_x(theta) = e^(-i*theta*X/2)
R_y(theta) = e^(-i*theta*Y/2)
R_z(theta) = e^(-i*theta*Z/2)
```

## Calculation Patterns

When helping with algebraic calculations in quantum computing, follow these patterns:

### Verifying Unitarity
1. Compute U * U_dagger
2. Check if result equals I
3. Alternatively: check that columns form an orthonormal set

### Finding Eigenvalues/Eigenvectors
1. Write the characteristic equation det(A - lambda*I) = 0
2. Solve for eigenvalues lambda
3. For each lambda, solve (A - lambda*I)|v> = 0
4. Normalize the eigenvectors
5. Verify: A|v> = lambda|v> for each pair

### Computing Tensor Products
1. For states: (alpha|0> + beta|1>) (x) (gamma|0> + delta|1>) = alpha*gamma|00> + alpha*delta|01> + beta*gamma|10> + beta*delta|11>
2. For matrices: write the Kronecker product block structure
3. Verify dimensions: (m x n) (x) (p x q) = (mp x nq)

### Partial Trace
1. Write rho_AB in the computational basis
2. Tr_B(|ij><kl|) = delta_jl * |i><k|
3. Sum all terms after applying the partial trace rule
4. Verify: Tr(rho_A) = 1 and rho_A is positive semi-definite
