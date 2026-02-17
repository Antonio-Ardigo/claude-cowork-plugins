---
name: quantum-experiments
description: Experimental techniques and physical phenomena that rely on quantum mechanics. Use when the user asks about nuclear magnetic resonance (NMR), infrared spectroscopy, Raman spectroscopy, X-ray crystallography, electron spin resonance (ESR/EPR), Stern-Gerlach experiment, double-slit experiment, Bell test experiments, quantum optics, photon detection, ion traps, superconducting qubits, quantum dots, NV centers, or any experimental realization of quantum phenomena. Also use when discussing how quantum computing hardware works physically.
---

# Quantum Experiments Skill

You are an instructor specializing in the experimental foundations of quantum mechanics and quantum computing. You explain the physical experiments that demonstrate quantum phenomena, the spectroscopic techniques that exploit quantum mechanics, and the hardware platforms for quantum computing.

**Important**: Quantum mechanics is not just a mathematical framework -- it is the most precisely tested theory in physics. Always connect theoretical concepts to the experiments that confirmed them. When discussing quantum computing hardware, emphasize the physical challenges (decoherence, gate fidelity, connectivity) alongside the theoretical idealization.

## Part 1: Foundational Quantum Experiments

### 1. The Double-Slit Experiment
- **What it shows**: Wave-particle duality; single particles create interference patterns
- **Setup**: Source emits particles (photons, electrons) through two slits onto a detector screen
- **Key observation**: Individual particles land as points, but the cumulative pattern shows interference fringes
- **Quantum insight**: The particle passes through "both slits" (superposition of paths); measurement (which-slit detector) destroys interference
- **Relevance to QC**: Demonstrates superposition and the role of measurement -- the foundational principles of quantum computing

### 2. Stern-Gerlach Experiment (1922)
- **What it shows**: Quantization of angular momentum (spin)
- **Setup**: Silver atoms pass through an inhomogeneous magnetic field
- **Key observation**: Beam splits into discrete spots (not a continuous smear) -- spin is quantized
- **Quantum insight**: Spin-1/2 particles have exactly two possible measurement outcomes (|up>, |down>) -- this is the physical qubit
- **Historical significance**: First direct evidence that quantum states have discrete outcomes

### 3. Bell Test Experiments
- **What they show**: Quantum entanglement violates Bell inequalities -- no local hidden variable theory can reproduce quantum predictions
- **Key experiments**:
  - Aspect et al. (1982): First convincing Bell test with polarization-entangled photons
  - Hensen et al. (2015): Loophole-free Bell test (Delft)
  - The BIG Bell Test (2018): Human-generated random choices
- **Bell inequality**: |S| <= 2 for any local hidden variable theory
- **Quantum prediction**: |S| = 2*sqrt(2) ~ 2.83 (Tsirelson bound) -- violated experimentally
- **Relevance to QC**: Proves entanglement is a genuinely non-classical resource

### 4. Quantum Teleportation Experiments
- **First demonstrated**: Innsbruck (Zeilinger) and Rome (De Martini), 1997
- **Protocol**: Transfer a quantum state using shared entanglement + classical communication
- **Modern achievements**: Teleportation over 1,400 km via satellite (Micius, 2017)
- **Relevance to QC**: Key primitive for quantum communication and distributed quantum computing

### 5. Quantum Eraser and Delayed-Choice Experiments
- **What they show**: The "decision" about wave vs particle behavior can be made after the particle passes through the slits
- **Wheeler's delayed-choice**: The choice of measurement apparatus (interference or which-path) after the photon enters the interferometer still determines the outcome
- **Quantum eraser**: "Erasing" which-path information restores the interference pattern
- **Quantum insight**: Quantum mechanics does not assign definite properties until measurement -- the past is not fixed until observed

## Part 2: Spectroscopic Techniques Using Quantum Mechanics

### 6. Nuclear Magnetic Resonance (NMR)

**Physical basis**: Nuclear spin interacts with external magnetic field

- **Quantum mechanics involved**:
  - Nuclear spin states (I = 1/2 for ^1H, ^13C): |up>, |down> in the field
  - Zeeman splitting: E = -gamma * hbar * B_0 * m_I
  - Larmor precession: omega_0 = gamma * B_0
  - Transitions driven by RF pulses (Rabi oscillations)
- **Key technique**: Apply RF pulse at resonance frequency -> spin flip -> detect precessing magnetization
- **Chemical shift**: Electronic environment modifies local field -> different nuclei resonate at different frequencies
- **Applications**: Molecular structure determination, medical imaging (MRI), materials science
- **Connection to QC**: NMR was the first platform for quantum computing experiments (Chuang & Gershenfeld, 1997; 7-qubit Shor's algorithm factoring 15)

### 7. Infrared (IR) Spectroscopy

**Physical basis**: Molecular vibrations are quantized (quantum harmonic oscillator)

- **Quantum mechanics involved**:
  - Vibrational energy levels: E_n = hbar * omega * (n + 1/2)
  - Selection rule: Delta_n = +/- 1 for harmonic oscillator (absorption/emission of one quantum)
  - Anharmonicity: real molecules deviate from harmonic -- overtones and combination bands
  - Zero-point energy: E_0 = hbar * omega / 2 (molecules vibrate even at absolute zero)
- **Key technique**: Pass IR light through a sample -> molecules absorb at characteristic frequencies -> fingerprint spectrum
- **Applications**: Chemical identification, atmospheric monitoring, forensics
- **Connection to QC**: Quantum simulation of molecular vibrations is a target application for quantum computers

### 8. Raman Spectroscopy

**Physical basis**: Inelastic scattering of photons by molecular vibrations

- **Quantum mechanics involved**:
  - Virtual excited state (not a real energy level)
  - Stokes scattering: photon loses energy -> molecule gains a vibrational quantum
  - Anti-Stokes scattering: photon gains energy -> molecule loses a vibrational quantum
  - Selection rules differ from IR: depends on polarizability change, not dipole moment change
- **Applications**: Complementary to IR; works for symmetric molecules (like O_2, N_2) that are IR-inactive

### 9. Electron Spin Resonance (ESR / EPR)

**Physical basis**: Electron spin in a magnetic field (analogous to NMR but for electrons)

- **Quantum mechanics involved**:
  - Electron spin splitting in magnetic field: Delta_E = g_e * mu_B * B_0
  - g-factor: deviations from g = 2 reveal spin-orbit coupling and local environment
  - Hyperfine coupling: electron spin interacts with nearby nuclear spins
  - Microwave frequency transitions (GHz range, vs MHz for NMR)
- **Applications**: Studying free radicals, transition metal complexes, defects in solids
- **Connection to QC**: ESR of nitrogen-vacancy (NV) centers in diamond is a quantum computing platform

### 10. X-Ray Crystallography

**Physical basis**: X-ray diffraction by periodic crystal lattice

- **Quantum mechanics involved**:
  - Bragg's law: 2d*sin(theta) = n*lambda (condition for constructive interference)
  - Electron density distribution determines scattering factors
  - Quantum mechanics of electron clouds determines the form factor
- **Applications**: Determining crystal structures, protein structures (DNA structure!), materials science

## Part 3: Quantum Computing Hardware Platforms

### 11. Superconducting Qubits
- **Physical system**: Josephson junction circuits cooled to ~15 mK
- **Qubit types**: Transmon, flux qubit, charge qubit
- **Gate mechanism**: Microwave pulses drive transitions between |0> and |1>
- **Pros**: Fast gates (~10-100 ns), mature fabrication, scalable
- **Cons**: Short coherence times (~100 microseconds), requires millikelvin cooling
- **Leading implementations**: IBM, Google, Rigetti

### 12. Trapped Ion Qubits
- **Physical system**: Individual ions (e.g., ^171Yb+, ^40Ca+) confined in electromagnetic traps
- **Qubit encoding**: Hyperfine states or optical transitions
- **Gate mechanism**: Laser pulses; entangling gates via shared motional modes
- **Pros**: Highest gate fidelities (>99.9%), long coherence times, all-to-all connectivity
- **Cons**: Slower gates (~1-100 microseconds), scaling challenges
- **Leading implementations**: IonQ, Quantinuum (Honeywell)

### 13. Photonic Qubits
- **Physical system**: Single photons (polarization, path, or time-bin encoding)
- **Gate mechanism**: Beam splitters, phase shifters, nonlinear interactions
- **Pros**: Room temperature, natural for communication, low decoherence
- **Cons**: Photon loss, difficult deterministic two-qubit gates (requires nonlinearity or measurement-based approaches)
- **Leading implementations**: Xanadu (Gaussian boson sampling), PsiQuantum

### 14. Nitrogen-Vacancy (NV) Centers in Diamond
- **Physical system**: Defect in diamond lattice (nitrogen replacing carbon + adjacent vacancy)
- **Qubit encoding**: Electron spin states of the NV center
- **Pros**: Room temperature operation, long coherence times, optical readout
- **Cons**: Low gate speeds, limited connectivity, difficult to scale
- **Applications**: Quantum sensing (magnetometry), small-scale quantum processors

### 15. Neutral Atom Arrays
- **Physical system**: Individual neutral atoms (e.g., rubidium, cesium) held in optical tweezers
- **Qubit encoding**: Hyperfine ground states or Rydberg states
- **Gate mechanism**: Rydberg blockade for entangling gates
- **Pros**: Large qubit numbers (>1000 demonstrated), reconfigurable geometry
- **Cons**: Relatively new, gate fidelities still improving
- **Leading implementations**: QuEra, Pasqal, Atom Computing

## Connecting Experiments to Theory

| Quantum Concept | Demonstrating Experiment | Year |
|----------------|------------------------|------|
| Quantized energy levels | Blackbody radiation (Planck) | 1900 |
| Wave-particle duality | Photoelectric effect (Einstein) | 1905 |
| Quantized angular momentum | Stern-Gerlach | 1922 |
| Wave nature of matter | Davisson-Germer (electron diffraction) | 1927 |
| Quantum tunneling | Alpha decay theory (Gamow) | 1928 |
| Entanglement exists | EPR paper (Einstein, Podolsky, Rosen) | 1935 |
| Bell inequality violation | Aspect experiment | 1982 |
| Quantum teleportation | Innsbruck/Rome experiments | 1997 |
| Quantum supremacy | Google Sycamore (53 qubits) | 2019 |
| Loophole-free Bell test | Hensen et al. (Delft) | 2015 |
