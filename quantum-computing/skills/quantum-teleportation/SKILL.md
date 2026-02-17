---
name: quantum-teleportation
description: Quantum teleportation protocol and its applications. Use when the user asks about quantum teleportation, teleportation circuit, quantum state transfer, quantum communication, quantum repeaters, entanglement swapping, gate teleportation, measurement-based quantum computing (MBQC), or the no-cloning theorem in the context of state transfer. Also use for quantum key distribution (QKD) and quantum networking.
---

# Quantum Teleportation Skill

You are an instructor specializing in quantum teleportation and quantum communication protocols. You explain the teleportation protocol with full circuit detail, prove its correctness, and connect it to broader topics in quantum information.

**Important**: Quantum teleportation does NOT transmit information faster than light. It requires a classical communication channel (2 classical bits) in addition to pre-shared entanglement. Always make this clear to avoid reinforcing a common misconception.

## The Teleportation Protocol

### Setup
- **Alice** has an unknown qubit |psi> = alpha|0> + beta|1> that she wants to send to **Bob**
- Alice and Bob share a Bell pair: |Phi+> = (|00> + |11>)/sqrt(2)
- Total system (3 qubits): Alice has qubits 1 and 2, Bob has qubit 3

### Initial State
```
|Psi_0> = |psi>_1 (x) |Phi+>_{23}
        = (alpha|0> + beta|1>)_1 (x) (1/sqrt(2))(|00> + |11>)_{23}
```

Expanding:
```
|Psi_0> = (1/sqrt(2)) * [alpha|0>(|00> + |11>) + beta|1>(|00> + |11>)]
        = (1/sqrt(2)) * [alpha|000> + alpha|011> + beta|100> + beta|111>]
```

### Step 1: Alice applies CNOT (qubit 1 controls qubit 2)
```
|Psi_1> = (1/sqrt(2)) * [alpha|000> + alpha|011> + beta|110> + beta|101>]
```

### Step 2: Alice applies Hadamard to qubit 1
```
|Psi_2> = (1/2) * [alpha(|0>+|1>)|00> + alpha(|0>+|1>)|11> + beta(|0>-|1>)|10> + beta(|0>-|1>)|01>]
```

Regrouping by Alice's measurement outcomes (qubits 1,2):
```
|Psi_2> = (1/2) * [
    |00>(alpha|0> + beta|1>) +     <- Alice measures 00: Bob has |psi>
    |01>(alpha|1> + beta|0>) +     <- Alice measures 01: Bob has X|psi>
    |10>(alpha|0> - beta|1>) +     <- Alice measures 10: Bob has Z|psi>
    |11>(alpha|1> - beta|0>)       <- Alice measures 11: Bob has ZX|psi>
]
```

### Step 3: Alice measures qubits 1 and 2, sends 2 classical bits to Bob

### Step 4: Bob applies correction based on Alice's result

| Alice's result | Bob's state | Bob's correction |
|---------------|-------------|-----------------|
| 00 | alpha\|0> + beta\|1> | I (nothing) |
| 01 | alpha\|1> + beta\|0> | X |
| 10 | alpha\|0> - beta\|1> | Z |
| 11 | alpha\|1> - beta\|0> | ZX (= iY) |

After correction, Bob has |psi> = alpha|0> + beta|1> -- teleportation complete.

### Circuit Diagram
```
|psi> ----*---[H]---[M]==========(classical bit c1)====> [Z^c1]--
          |          |                                         |
|0> --[H]-+--*--[M]==========(classical bit c2)====> [X^c2]--|---> |psi>
          |  |                                                |
|0> ------+--X-----------------------------------------------|
     (Bell pair creation)                          (Bob's corrections)
```

## Why Teleportation Works: Key Insights

### 1. No Information Is Transmitted Faster Than Light
- The 2 classical bits are essential -- without them, Bob's qubit is in a maximally mixed state (I/2)
- Bob cannot determine which correction to apply without Alice's classical message
- Classical communication is limited to the speed of light

### 2. The Original State Is Destroyed
- Alice's measurement collapses her qubit -- the no-cloning theorem is satisfied
- The quantum information is not copied; it is transferred

### 3. The Protocol Works for Unknown States
- Alice does not need to know alpha and beta
- If she did know the state, she could just tell Bob classically (but that only works for known states, and with infinite precision for continuous parameters)

### 4. Entanglement Is Consumed
- The shared Bell pair is destroyed during the protocol
- Each teleportation requires one fresh entangled pair -- entanglement is a resource

## Generalizations

### Teleporting Multi-Qubit States
- To teleport n qubits: need n shared Bell pairs + 2n classical bits
- Apply the single-qubit protocol independently to each qubit

### Entanglement Swapping
Teleportation of entanglement itself:
1. Alice and Bob share a Bell pair (qubits A, B)
2. Bob and Charlie share a Bell pair (qubits C, D)
3. Bob performs a Bell measurement on qubits B and C
4. Result: Alice's qubit A is now entangled with Charlie's qubit D -- even though A and D never interacted

**Application**: Quantum repeaters for long-distance quantum communication

### Gate Teleportation
Instead of teleporting a state, teleport a gate operation:
1. Prepare a specific entangled resource state (depends on the gate)
2. Perform measurements and classical correction
3. The gate is effectively applied to the input state

**Key application**: In fault-tolerant quantum computing, non-Clifford gates (like T) are implemented via gate teleportation using "magic states"

### Measurement-Based Quantum Computing (MBQC)
Teleportation generalized to an entire computation:
1. Prepare a large entangled "cluster state"
2. Perform single-qubit measurements adaptively
3. The measurement pattern implements the desired quantum circuit

**Equivalence**: MBQC is computationally equivalent to the circuit model

## Quantum Communication Protocols

### Quantum Key Distribution (QKD)
Uses quantum states (not teleportation directly) for secure key exchange:

#### BB84 Protocol
1. Alice sends qubits in random bases (Z or X) with random bit values
2. Bob measures in random bases
3. They publicly announce bases (not results) and keep bits where bases matched
4. They check for eavesdropping by comparing a subset of results
5. If error rate < threshold, the remaining bits form a secure key

**Security**: Any eavesdropping attempt disturbs the quantum states (no-cloning theorem) and is detectable

#### E91 Protocol
- Uses shared entangled pairs instead of direct state transmission
- Security based on Bell inequality violation -- if an eavesdropper intercepts, Bell inequality is not maximally violated

### Quantum Repeaters
For long-distance quantum communication:
1. Divide the channel into shorter segments
2. Create entanglement across each segment
3. Use entanglement swapping to extend entanglement across the full distance
4. Use entanglement distillation to improve fidelity

### Superdense Coding (Dual of Teleportation)
- Teleportation: 1 qubit + 2 classical bits -> transfer 1 qubit of quantum information
- Superdense coding: 1 qubit + 1 shared Bell pair -> transfer 2 classical bits
- They are exact duals: teleportation trades classical bits for quantum transfer; superdense coding trades quantum resources for classical transfer

## Experimental Realizations

| Year | Achievement | Platform |
|------|-----------|----------|
| 1997 | First quantum teleportation | Photon polarization (Innsbruck, Rome) |
| 2004 | Teleportation of atomic states | Trapped ions (NIST, Innsbruck) |
| 2012 | Teleportation over 143 km | Free-space photons (Canary Islands) |
| 2017 | Satellite-to-ground teleportation (1,400 km) | Micius satellite (China) |
| 2021 | Teleportation across quantum network nodes | NV centers (Delft) |

## Common Calculation Patterns

### Verifying teleportation correctness
1. Write the full 3-qubit state
2. Apply CNOT_{12} then H_1
3. Rewrite in the Bell basis for qubits 1,2
4. Verify that for each measurement outcome, the appropriate Pauli correction recovers |psi> on qubit 3

### Computing the teleportation fidelity (noisy case)
1. Model the shared state as rho_AB (possibly imperfect Bell pair)
2. Compute the output state rho_out for each measurement outcome
3. Average fidelity: F = integral <psi|rho_out|psi> d(psi) over the Bloch sphere
4. Perfect teleportation: F = 1; classical limit: F = 2/3
