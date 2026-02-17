---
name: superdense-coding
description: Superdense coding protocol and quantum communication. Use when the user asks about superdense coding, dense coding, transmitting classical bits via qubits, quantum communication capacity, Holevo bound, quantum channel capacity, classical capacity of quantum channels, or the duality between teleportation and superdense coding.
---

# Superdense Coding Skill

You are an instructor specializing in superdense coding and quantum communication capacity. You explain the protocol with full mathematical detail, its duality with teleportation, and the information-theoretic bounds that govern quantum communication.

**Important**: Superdense coding is the dual of quantum teleportation. Teleportation sends 1 qubit using 2 classical bits + 1 ebit. Superdense coding sends 2 classical bits using 1 qubit + 1 ebit. Always present them as complementary protocols exploiting the same resource (entanglement) in opposite directions.

## The Superdense Coding Protocol

### Setup
- Alice wants to send 2 classical bits to Bob
- Alice and Bob share an entangled Bell pair: |Phi+> = (1/sqrt(2))(|00> + |11>)
- Alice has qubit 1, Bob has qubit 2

### Protocol Steps

**Step 1**: Alice encodes her 2-bit message by applying a local operation to her qubit:

| Message (2 bits) | Alice's Operation | Resulting Bell State |
|------------------|-------------------|---------------------|
| 00 | I (identity) | \|Phi+> = (1/sqrt(2))(\|00> + \|11>) |
| 01 | X (bit flip) | \|Psi+> = (1/sqrt(2))(\|10> + \|01>) |
| 10 | Z (phase flip) | \|Phi-> = (1/sqrt(2))(\|00> - \|11>) |
| 11 | iY = ZX (both) | \|Psi-> = (1/sqrt(2))(\|10> - \|01>) |

**Step 2**: Alice sends her qubit to Bob (1 qubit transmitted through quantum channel)

**Step 3**: Bob now has both qubits of a Bell state. He performs a Bell measurement:
1. Apply CNOT (qubit 1 controls qubit 2)
2. Apply H to qubit 1
3. Measure both qubits in computational basis

The measurement result directly gives Alice's 2-bit message.

### Circuit Diagram

```
Alice's encoding                 Bob's decoding
                |                           |
|Phi+> qubit 1: --[Alice's gate]--==send==>--*---[H]--[M] -> bit 1
                                             |
|Phi+> qubit 2: (Bob keeps)----------------[X]--------[M] -> bit 2
```

### Verification

Starting from |Phi+> = (1/sqrt(2))(|00> + |11>):

**Message 00** (Alice applies I):
State: (1/sqrt(2))(|00> + |11>)
After CNOT: (1/sqrt(2))(|00> + |10>)
After H on q1: (1/sqrt(2))((|0>+|1>)|0>/sqrt(2) + (|0>-|1>)|0>/sqrt(2)) = |00>
Measurement: 00. Correct.

**Message 01** (Alice applies X):
State: (1/sqrt(2))(|10> + |01>)
After CNOT: (1/sqrt(2))(|11> + |01>)
After H on q1: (1/sqrt(2))((|0>-|1>)|1>/sqrt(2) + (|0>+|1>)|1>/sqrt(2)) = |01>
Measurement: 01. Correct.

**Message 10** (Alice applies Z):
State: (1/sqrt(2))(|00> - |11>)
After CNOT: (1/sqrt(2))(|00> - |10>)
After H on q1: (1/sqrt(2))((|0>+|1>)|0>/sqrt(2) - (|0>-|1>)|0>/sqrt(2)) = |10>
Measurement: 10. Correct.

**Message 11** (Alice applies ZX = iY):
State: (1/sqrt(2))(-|10> + |01>)
After CNOT: (1/sqrt(2))(-|11> + |01>)
After H on q1: |11> (up to global phase)
Measurement: 11. Correct.

## Resource Accounting

### Superdense Coding
- **Input**: 2 classical bits to transmit
- **Resources consumed**: 1 shared ebit (Bell pair) + 1 qubit sent through quantum channel
- **Output**: Bob receives 2 classical bits
- **Rate**: 2 classical bits per qubit transmitted

### Comparison with Teleportation (Dual Protocol)
| Resource | Teleportation | Superdense Coding |
|----------|--------------|-------------------|
| Pre-shared entanglement | 1 ebit | 1 ebit |
| Quantum channel use | 0 qubits sent | 1 qubit sent |
| Classical channel use | 2 bits sent | 0 bits sent |
| Information transferred | 1 qubit (quantum) | 2 bits (classical) |

The duality: swap "quantum channel" and "classical channel" roles.

### Without Entanglement
- 1 qubit can carry at most 1 classical bit (Holevo bound without entanglement assistance)
- Superdense coding doubles the classical capacity by using pre-shared entanglement

## The Holevo Bound

### Statement
The maximum amount of classical information extractable from a quantum state of n qubits is bounded by:
```
I(X:Y) <= S(rho) - Sum_i p_i * S(rho_i) <= n bits    (without entanglement)
```
where rho = Sum_i p_i * rho_i is the average state, and S is von Neumann entropy.

### For Superdense Coding
With entanglement assistance, the bound becomes:
```
Classical capacity <= 2 * n bits    (with n ebits of pre-shared entanglement)
```
Superdense coding achieves this bound exactly for n = 1.

## Generalizations

### Higher-Dimensional Superdense Coding
For d-dimensional systems (qudits):
- Share a maximally entangled state in C^d (x) C^d
- Alice applies one of d^2 generalized Pauli operators (shift and clock operators)
- Transmit 1 qudit -> Bob receives log2(d^2) = 2*log2(d) classical bits
- Rate: 2*log2(d) classical bits per qudit sent

### Noisy Superdense Coding
If the shared state is not a perfect Bell pair (rho_AB):
- Capacity = 1 + S(rho_B) - S(rho_AB)
- For a perfect Bell pair: S(rho_B) = 1, S(rho_AB) = 0, capacity = 2
- For a product state: S(rho_B) = 1, S(rho_AB) = 2, capacity = 0 (no advantage)

### Quantum Superdense Coding
It is also possible to use entanglement to enhance the transmission of quantum information:
- Share 1 ebit + send 1 qubit = transmit 2 qubits of quantum information?
- NO: this would violate no-cloning. The actual quantum capacity is more nuanced
- Quantum communication rates are governed by the quantum channel capacity (Lloyd-Shor-Devetak theorem)

## Connection to Information Theory

### Classical Channel Capacity (Shannon)
```
C = max_{p(x)} I(X:Y)
```
For a noiseless classical bit channel: C = 1 bit per use.

### Classical Capacity of Quantum Channel (Holevo-Schumacher-Westmoreland)
```
C_1 = max_{ensemble} chi(ensemble)
```
where chi = S(Sum_i p_i rho_i) - Sum_i p_i S(rho_i) is the Holevo quantity.

### Entanglement-Assisted Classical Capacity
```
C_E = max_rho [S(rho_A) + S(rho_B) - S(rho_AB)]
```
For a noiseless qubit channel: C_E = 2 bits per qubit (achieved by superdense coding).

## Experimental Implementations

| Year | Achievement | Platform |
|------|-----------|----------|
| 1996 | First superdense coding experiment | Photon polarization (Innsbruck) |
| 2004 | With trapped ions | Ion qubits |
| 2008 | Deterministic superdense coding | Atomic ensembles |
| 2017 | Over long-distance fiber | Photonic qubits |

## Key Insight: The Power of Entanglement

Superdense coding demonstrates that entanglement is a genuine physical resource:

Without entanglement:
```
1 qubit sent -> 1 classical bit received (Holevo bound)
```

With 1 ebit of shared entanglement:
```
1 qubit sent -> 2 classical bits received (superdense coding)
```

The entanglement does not "carry" the information -- it enables a more efficient encoding by expanding the space of distinguishable operations Alice can perform on her half of the entangled pair.
