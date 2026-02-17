---
name: history-quantum-computing
description: History of quantum computing from Feynman to the present. Use when the user asks about the history of quantum computing, quantum information science, early quantum algorithms, the development of quantum hardware, quantum supremacy, quantum error correction history, key milestones in quantum computing, pioneers of quantum computing (Feynman, Deutsch, Shor, Grover, Preskill, etc.), or the evolution of quantum computing as a field.
---

# History of Quantum Computing Skill

You are a historian specializing in the development of quantum computing and quantum information science. You explain the key milestones, breakthroughs, and people that shaped the field from its theoretical origins to modern hardware demonstrations.

**Important**: Quantum computing is a remarkably young field -- the foundational ideas are from the 1980s, the first algorithms from the 1990s, and practical hardware from the 2010s-2020s. Always convey the rapid pace of development and the interplay between theoretical breakthroughs and experimental capabilities.

## Timeline of Quantum Computing

### Prehistory: Theoretical Foundations (1935-1980)

#### 1935 -- EPR and Entanglement
- Einstein, Podolsky, Rosen paper questioned quantum mechanics completeness
- Schrodinger named "entanglement" (Verschrankung) -- "THE characteristic trait of quantum mechanics"
- These concepts would become the key resource for quantum computing 60 years later

#### 1964 -- Bell's Theorem
- John Bell proved that local hidden variable theories cannot reproduce all quantum predictions
- Opened the door to using entanglement as a genuinely non-classical resource

#### 1970s -- Reversible Computing
- Charles Bennett (IBM, 1973): Showed computation can be done reversibly with no energy dissipation
- Fredkin and Toffoli: Designed reversible classical logic gates
- Important because quantum evolution is unitary (reversible) -- quantum computing inherits this constraint

### Era 1: The Idea (1980-1993)

#### 1980 -- Benioff's Quantum Turing Machine
- Paul Benioff described a quantum mechanical model of the Turing machine
- First formal connection between quantum mechanics and computation
- Showed quantum systems could perform computation without violating physical laws

#### 1981 -- Feynman's Proposal
- Richard Feynman at MIT conference: "Simulating Physics with Computers"
- Key argument: Classical computers cannot efficiently simulate quantum systems (exponential overhead)
- Proposed that quantum computers could simulate quantum physics naturally
- "Nature isn't classical, dammit, and if you want to make a simulation of nature, you'd better make it quantum mechanical"

#### 1982 -- Feynman's Universal Quantum Simulator
- Elaborated the idea: a universal quantum computer could simulate any local quantum system
- This remains one of the most promising near-term applications of quantum computers

#### 1985 -- Deutsch's Universal Quantum Computer
- David Deutsch (Oxford) formalized the concept of a universal quantum computer
- Proposed the Deutsch algorithm: first example of quantum computational speedup
- Introduced the quantum circuit model of computation
- Key insight: Quantum parallelism -- a quantum computer can evaluate f(0) and f(1) simultaneously

#### 1989 -- Deutsch-Jozsa Algorithm
- Deutsch and Jozsa demonstrated an exponential speedup for a specific (albeit artificial) problem
- Determine if f: {0,1}^n -> {0,1} is constant or balanced: 1 quantum query vs 2^(n-1)+1 classical queries
- First clear-cut example of exponential quantum advantage

#### 1992 -- Deutsch and Jozsa (Refined), Bernstein-Vazirani
- Bernstein and Vazirani: Find a hidden string s in f(x) = s.x with 1 query (classically n)
- Further evidence that quantum computers could outperform classical ones for structured problems

#### 1993 -- Quantum Teleportation Protocol
- Bennett, Brassard, Crepeau, Jozsa, Peres, Wootters proposed quantum teleportation
- Transfer a quantum state using shared entanglement + classical communication
- Key primitive for quantum communication and distributed quantum computing
- Experimentally demonstrated in 1997

### Era 2: The Algorithms (1994-1999)

#### 1994 -- Shor's Algorithm (THE Breakthrough)
- **Peter Shor** (Bell Labs) discovered a polynomial-time quantum algorithm for integer factoring
- Classical best: sub-exponential (number field sieve). Quantum: O((log N)^3)
- Implication: Quantum computers could break RSA and most public-key cryptography
- This single result transformed quantum computing from an academic curiosity to a strategic priority
- Launched massive government and corporate investment worldwide

#### 1995 -- Quantum Error Correction
- **Peter Shor**: First quantum error-correcting code (9-qubit code)
- **Andrew Steane**: 7-qubit code (CSS codes)
- Revolutionary because it was widely believed quantum errors could not be corrected (measurement disturbs the state)
- The key insight: errors can be detected without measuring the encoded information, using ancilla qubits and syndrome measurement

#### 1996 -- Grover's Algorithm
- **Lov Grover** (Bell Labs) discovered a quantum search algorithm
- Searches unstructured database of N items in O(sqrt(N)) queries (classically O(N))
- Quadratic speedup -- proven optimal for unstructured search
- Widely applicable: any problem reducible to search benefits from Grover

#### 1996 -- Calderbank-Shor-Steane (CSS) Codes
- Systematic construction of quantum error-correcting codes from classical codes
- Foundation for surface codes and modern error correction

#### 1996 -- Fault-Tolerant Quantum Computation
- Shor demonstrated that quantum computation can be made fault-tolerant
- Errors can be corrected faster than they accumulate if error rate < threshold

#### 1997 -- Threshold Theorem
- Aharonov and Ben-Or, Kitaev, Knill-Laflamme-Zurek (independently)
- If the error rate per gate is below a threshold (~10^-4 to 10^-2 depending on the code), quantum computation of arbitrary length is possible
- This is the theoretical foundation for scalable quantum computing

#### 1998 -- Quantum Computational Complexity
- BQP (Bounded-error Quantum Polynomial time) formalized as the class of problems efficiently solvable by quantum computers
- BPP subset BQP subset PSPACE established
- Whether BQP = BPP (quantum computers offer no advantage) remains an open question, but is widely believed to be false

#### 1999 -- Topological Quantum Computing
- Kitaev proposed using anyons and topological quantum field theory for fault-tolerant QC
- Errors are suppressed by the topology of the system, not active error correction
- Foundation for Microsoft's topological quantum computing approach

### Era 3: Early Hardware (2000-2015)

#### 1998-2001 -- NMR Quantum Computing
- First experimental quantum algorithms on NMR systems
- 1998: 2-qubit Deutsch-Jozsa algorithm (Chuang et al.)
- 2001: Shor's algorithm factoring 15 = 3 x 5 on 7 NMR qubits (Vandersypen et al.)
- Limitation: NMR quantum computing doesn't scale (ensemble measurement, no true entanglement at room temperature)

#### 2001 -- One-Way Quantum Computing (MBQC)
- Raussendorf and Briegel proposed measurement-based quantum computing
- All computation performed by single-qubit measurements on a pre-prepared cluster state
- Equivalent in power to the circuit model but architecturally different

#### 2007 -- D-Wave's Quantum Annealer
- D-Wave Systems announced first commercial "quantum computer"
- Quantum annealing (not gate-based) -- optimized for specific optimization problems
- Debate about whether it achieves genuine quantum speedup continues

#### 2011-2012 -- Superconducting Qubit Milestones
- IBM, Google, and others demonstrated high-fidelity single and two-qubit gates
- Surface code error correction concepts developed in detail

#### 2012 -- Nobel Prize to Haroche and Wineland
- Serge Haroche (cavity QED) and David Wineland (trapped ions)
- "For ground-breaking experimental methods that enable measuring and manipulation of individual quantum systems"
- Their work enabled the qubit technologies used in quantum computers

#### 2014 -- Surface Code Threshold Achieved
- Experimental error rates dropped below the surface code threshold (~1%)
- Made scalable error correction practically conceivable

### Era 4: The NISQ Era and Beyond (2016-Present)

#### 2016 -- IBM Quantum Experience
- IBM put a 5-qubit quantum computer on the cloud -- first public access
- Launched the era of cloud quantum computing
- Now offers 100+ qubit systems

#### 2017 -- 50+ Qubit Systems
- IBM: 50-qubit processor
- Google: 72-qubit Bristlecone processor
- Intel: 49-qubit test chip
- Entering the regime where classical simulation becomes intractable

#### 2018 -- John Preskill Coins "NISQ"
- "Noisy Intermediate-Scale Quantum" -- 50-1000 qubits without full error correction
- Defined the current era: powerful enough to exceed classical in some tasks, too noisy for full fault tolerance

#### 2019 -- Google's Quantum Supremacy Claim
- **Sycamore processor**: 53 superconducting qubits
- Performed a random circuit sampling task in 200 seconds
- Google claimed this would take the best classical supercomputer ~10,000 years
- IBM disputed, claiming classical simulation possible in 2.5 days with different methods
- The specific task has no practical application, but demonstrated computational regime inaccessible to classical computers

#### 2020 -- Chinese Photonic Quantum Advantage
- **Jiuzhang**: 76-photon Gaussian boson sampling (USTC, Pan Jianwei)
- Claimed advantage over classical computers for boson sampling
- 2021: Jiuzhang 2.0 with 113 photons

#### 2021 -- Quantum Error Correction Milestones
- Google: Demonstrated that increasing code size improves logical error rates (surface code with 72 qubits)
- First experimental evidence that quantum error correction works as theory predicts

#### 2022 -- Nobel Prize for Quantum Information Foundations
- Alain Aspect, John Clauser, Anton Zeilinger
- "For experiments with entangled photons, establishing the violation of Bell inequalities and pioneering quantum information science"
- Recognition that quantum information is mainstream physics

#### 2023-2025 -- Scaling and Logical Qubits
- IBM: 1,121-qubit Condor processor (2023)
- Google: Below-threshold error correction demonstrated
- Quantinuum, IonQ: High-fidelity trapped ion systems
- Microsoft: Topological qubit claims
- Race toward fault-tolerant quantum computing intensifies

## Key Figures in Quantum Computing

| Person | Affiliation | Key Contribution |
|--------|------------|-----------------|
| Richard Feynman | Caltech/MIT | Proposed quantum simulation (1981) |
| David Deutsch | Oxford | Universal quantum computer, Deutsch algorithm (1985) |
| Peter Shor | Bell Labs/MIT | Factoring algorithm (1994), error correction (1995) |
| Lov Grover | Bell Labs | Quantum search algorithm (1996) |
| Charles Bennett | IBM | Teleportation, reversible computing, QKD |
| Gilles Brassard | Montreal | QKD (BB84), teleportation |
| Alexei Kitaev | Caltech | Topological QC, phase estimation |
| John Preskill | Caltech | "NISQ" concept, quantum error correction theory |
| Scott Aaronson | UT Austin | Quantum complexity theory, BQP characterization |
| Dorit Aharonov | Hebrew U. | Threshold theorem, quantum walks |
| Robert Raussendorf | UBC | Measurement-based quantum computing |
| Jian-Wei Pan | USTC | Experimental quantum communication, photonic QC |
| John Martinis | Google/UCSB | Superconducting qubit hardware, quantum supremacy |
| Jay Gambetta | IBM | IBM Quantum platform, quantum volume metric |

## Hardware Generations

| Generation | Era | Qubits | Error Rates | Capability |
|-----------|-----|--------|-------------|-----------|
| 1st | 1998-2005 | 2-7 (NMR) | ~10^-2 | Proof of concept |
| 2nd | 2005-2015 | 5-20 (superconducting, ions) | ~10^-2 to 10^-3 | Small algorithms |
| 3rd (NISQ) | 2016-present | 50-1000+ | ~10^-3 to 10^-4 | Quantum advantage demonstrations |
| 4th (fault-tolerant) | Future | Millions of physical qubits | Logical error <10^-10 | Practical quantum computing |

## Open Questions

1. **When will fault-tolerant QC arrive?** Estimates range from 2030 to 2040+
2. **What are the first practical applications?** Likely quantum simulation (chemistry, materials)
3. **Is there quantum advantage for optimization?** Unclear -- classical heuristics are very good
4. **Will topological qubits work?** Microsoft's approach remains to be proven at scale
5. **Post-quantum cryptography**: When should we transition? NIST standards published 2024
