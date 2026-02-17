---
name: quantum-fourier-transform
description: Quantum Fourier Transform (QFT) and its applications. Use when the user asks about the quantum Fourier transform, inverse QFT, discrete Fourier transform in quantum computing, phase estimation, period finding, quantum signal processing, Shor's algorithm (the QFT component), quantum arithmetic, or frequency-domain analysis of quantum states.
---

# Quantum Fourier Transform Skill

You are an instructor specializing in the Quantum Fourier Transform (QFT) and its role in quantum algorithms. You explain the QFT with full mathematical detail, circuit decomposition, and connections to classical Fourier analysis and key quantum algorithms.

**Important**: The QFT is the workhorse subroutine of many quantum algorithms. Always connect it to its applications (phase estimation, period finding, Shor's algorithm) and contrast it with the classical Discrete Fourier Transform to highlight both similarities and key differences (especially: the QFT transforms amplitudes, which are not directly readable).

## Core Definition

### The Quantum Fourier Transform on N = 2^n states

The QFT maps computational basis states to Fourier basis states:

```
QFT|j> = (1/sqrt(N)) * Sum_{k=0}^{N-1} e^(2*pi*i*j*k/N) |k>
```

Equivalently, in matrix form (N x N unitary):
```
(QFT)_{jk} = (1/sqrt(N)) * omega^(j*k)
```
where omega = e^(2*pi*i/N) is the N-th root of unity.

### Action on a general state

```
QFT(Sum_j x_j |j>) = Sum_k y_k |k>
```
where y_k = (1/sqrt(N)) * Sum_j x_j * omega^(j*k) -- exactly the classical DFT of the amplitudes.

### Product representation (key for circuit implementation)

The QFT can be decomposed as:
```
QFT|j_1 j_2 ... j_n> = (1/sqrt(2^n)) *
    (|0> + e^(2*pi*i*0.j_n)|1>) (x)
    (|0> + e^(2*pi*i*0.j_{n-1}j_n)|1>) (x)
    ...
    (|0> + e^(2*pi*i*0.j_1j_2...j_n)|1>)
```

where 0.j_l j_{l+1}...j_n = j_l/2 + j_{l+1}/4 + ... + j_n/2^(n-l+1) is the binary fraction.

This factorization is what makes the efficient quantum circuit possible.

## Circuit Implementation

### Gate Decomposition

The QFT circuit uses:
- **Hadamard gates**: H -- creates the (|0> + e^(i*phase)|1>) superposition
- **Controlled rotation gates**: CR_k -- adds phase e^(2*pi*i/2^k) conditional on control qubit
- **SWAP gates**: Reverse the qubit order at the end

```
CR_k = [[1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, e^(2*pi*i/2^k)]]
```

### Circuit for n qubits (schematic)

```
|j_1> --[H]--[CR_2]--[CR_3]--..--[CR_n]---------------------------x--
              |        |           |                                |
|j_2> --------.---[H]--[CR_2]--..--[CR_{n-1}]------------------x--|--
                       |           |                            |  |
|j_3> -----------------.---[H]--..--[CR_{n-2}]--............--x|--|--
                                   |                          ||  |
  .                                .                          ..  .
  .                                .                          ..  .
                                                              ||  |
|j_n> --------------------------------..---[H]----------------x---x--
                                                        (SWAP network)
```

### Complexity

| Resource | Count |
|----------|-------|
| Hadamard gates | n |
| Controlled rotations | n(n-1)/2 |
| SWAP gates | floor(n/2) |
| **Total gates** | **O(n^2)** |
| Classical FFT | O(n * 2^n) operations |
| **Exponential speedup** | QFT: O(n^2) vs FFT: O(n * 2^n) |

**Critical caveat**: The QFT itself is exponentially faster, but we cannot efficiently read out all Fourier coefficients (measurement collapses the state). The power of the QFT comes from using it as a subroutine where we only need specific information (like the dominant frequency / period).

## Inverse QFT

The inverse QFT undoes the Fourier transform:
```
QFT_inverse|k> = (1/sqrt(N)) * Sum_{j=0}^{N-1} e^(-2*pi*i*j*k/N) |j>
```

Circuit: Reverse the order of all gates in the QFT circuit and replace each CR_k with CR_k_dagger (negate the phase).

## Applications

### 1. Quantum Phase Estimation (QPE)

**Setup**: Given unitary U with eigenstate |u> and eigenvalue e^(2*pi*i*phi), find phi.

**How QFT is used**:
1. Controlled-U operations create the state (1/sqrt(2^t)) * Sum_k e^(2*pi*i*phi*k) |k> in the ancilla register
2. This is exactly the QFT of the state |phi_approx> (the binary representation of phi)
3. Applying QFT_inverse extracts |phi_approx>
4. Measuring gives phi to t bits of precision

**Accuracy**: t ancilla qubits give phi to t bits with probability >= 1 - 1/(2(2^t - 2)).

### 2. Period Finding (Shor's Algorithm)

**Setup**: Find the period r of f(x) = a^x mod N.

**How QFT is used**:
1. Create superposition of |x, f(x)> for all x
2. Measuring the second register collapses the first register to a periodic superposition with period r
3. QFT converts this periodic state to peaks at multiples of N/r
4. Measuring and using continued fractions extracts r

**Key insight**: The QFT turns periodicity in the computational basis into sharp peaks, making the period measurable.

### 3. Hidden Subgroup Problem

The QFT over a group G generalizes period finding:
- **Abelian groups**: Efficient QFT exists; solves the abelian HSP (includes factoring, discrete log)
- **Non-abelian groups**: QFT is harder; graph isomorphism and shortest lattice vector are related to non-abelian HSPs

### 4. Quantum Counting

Combines Grover's algorithm with QPE:
- Use QPE on Grover's diffusion operator
- The estimated phase reveals the number of marked items
- Achieves O(sqrt(N)) precision for counting

## Comparison: Classical DFT vs. QFT

| Aspect | Classical DFT/FFT | Quantum Fourier Transform |
|--------|-------------------|--------------------------|
| Input | Vector of N numbers | Quantum state of n = log2(N) qubits |
| Output | Vector of N Fourier coefficients | Quantum state with Fourier amplitudes |
| Operations | O(N * log N) = O(n * 2^n) | O(n^2) = O((log N)^2) |
| Readout | All coefficients accessible | One measurement sample per run |
| Use case | Signal processing, direct computation | Subroutine in quantum algorithms |
| Precision | Exact (up to floating point) | Approximate (depends on number of qubits) |

## Key Mathematical Properties

### Unitarity
QFT * QFT_dagger = I. The QFT is a unitary transformation, as required for a quantum gate.

### Periodicity detection
If |psi> = (1/sqrt(r)) * Sum_{j=0}^{r-1} |x_0 + j*r> (periodic with period r and offset x_0), then:
```
QFT|psi> has peaks at positions k * N/r for k = 0, 1, ..., r-1
```

### Phase kickback identity
For a QFT-eigenvector interpretation:
```
QFT|1> = (1/sqrt(N)) * Sum_k omega^k |k>
```
This is the uniform superposition with linearly increasing phases -- the "frequency 1" state.

### Shift property
QFT shifts in one basis correspond to phase rotations in the other:
```
QFT(|j + s mod N>) = omega^(k*s) * QFT(|j>)
```

## Worked Example: 3-Qubit QFT

For n = 3 (N = 8), omega = e^(2*pi*i/8) = e^(i*pi/4):

```
QFT|j> = (1/2*sqrt(2)) * Sum_{k=0}^{7} e^(2*pi*i*j*k/8) |k>
```

Example: QFT|5> = QFT|101>

```
QFT|5> = (1/2*sqrt(2)) * [|0> + omega^5|1> + omega^10|2> + omega^15|3>
                          + omega^20|4> + omega^25|5> + omega^30|6> + omega^35|7>]

= (1/2*sqrt(2)) * [|0> + e^(i*5*pi/4)|1> + e^(i*5*pi/2)|2> + e^(i*15*pi/4)|3>
                   + e^(i*5*pi)|4> + e^(i*25*pi/4)|5> + e^(i*15*pi/2)|6> + e^(i*35*pi/4)|7>]
```

Product form:
```
QFT|101> = (1/2*sqrt(2)) *
    (|0> + e^(i*pi)|1>) (x)          = (|0> - |1>) / sqrt(2)
    (|0> + e^(i*pi/2*0.01)|1>) (x)   = (|0> + e^(i*pi/2)|1>) / sqrt(2)
    (|0> + e^(i*pi/2*0.101)|1>)      = (|0> + e^(i*5*pi/4)|1>) / sqrt(2)
```

## Approximate QFT

For practical implementations on noisy hardware:
- Controlled rotations CR_k with k > threshold can be dropped
- Approximation with only O(n * log(n)) gates achieves the same result to O(1/n) error
- This is important for near-term implementations where circuit depth must be minimized
