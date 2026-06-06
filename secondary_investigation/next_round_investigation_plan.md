# Next Round: Exhaustive Investigation Plan

A comprehensive, categorized list of every fringe, taboo, unprovable, impossible, and unsolved problem across physics, mathematics, consciousness, the paranormal, and philosophy — each with a concrete SADE modeling strategy under the doubling fold.

---

## Category A: Unsolved Fundamental Physics

### A1. Quantum Gravity & Unification
* **Problem:** General Relativity and Quantum Mechanics are mathematically incompatible.
* **SADE Model:** Model gravity as the $p=2$ sector and QM as the $p=3$ sector. Use `find_integer_relation_lll` to search for unification relations between their coupling constants ($g_2 = 1/2$, $g_3 = 2/3$).

### A2. Dark Matter
* **Problem:** ~27% of the universe's mass-energy is invisible. No known particle accounts for it.
* **SADE Model:** Model dark matter as states with very large odd prime denominators (long-period orbits invisible to short-observation-window detectors). Use `approximate_interval` to find the simplest fraction in the gravitational lensing mass range.

### A3. Dark Energy & Accelerating Expansion
* **Problem:** ~68% of the universe is an unknown repulsive energy driving cosmic acceleration.
* **SADE Model:** Model dark energy as the net Lyapunov expansion pressure ($\lambda = \ln 2$) of the fold itself. Derive the ratio of dark energy to total energy as a fold coupling constant.

### A4. Matter-Antimatter Asymmetry (Baryogenesis)
* **Problem:** Why is the universe made of matter, not equal parts matter and antimatter?
* **SADE Model:** Matter = states $x < 1/2$, Antimatter = states $x > 1/2$. The fold map $f(x) = 2x \pmod 1$ is asymmetric around $1/2$ for pre-periodic states. Simulate annihilation ($\text{take}(x, \bar{x})$) and show that the surviving residue is always biased to one side.

### A5. The Hierarchy Problem
* **Problem:** Why is gravity $10^{38}$ times weaker than the electromagnetic force?
* **SADE Model:** Search for the ratio $G_{\text{grav}}/G_{\text{EM}}$ as a fold-derived fraction with an extremely large denominator. Use LLL to find integer relations between the gravitational and electromagnetic coupling constants.

### A6. The Measurement Problem (Wave Function Collapse)
* **Problem:** How and why does quantum superposition collapse into a definite state upon observation?
* **SADE Model:** Model superposition as the pre-measurement state $x = p/q$ (multiple bits of information). Observation = one fold step, which shifts out the MSB (collapses one bit of information). The "collapse" is the irreversible loss of one bit per fold.

### A7. Neutrino Mass Origin
* **Problem:** Neutrinos have mass, but the Standard Model predicted they were massless.
* **SADE Model:** Derive the neutrino mass ratio from SADE's `approximate_interval` using experimental mass bounds. Find the simplest fold fraction in the allowed range.

### A8. Strong CP Problem
* **Problem:** Why does the strong force preserve CP symmetry when the theory allows violation?
* **SADE Model:** Model CP violation as an asymmetry in the fold orbit distribution. Show that the $p=3$ sector (strong force) has a symmetric orbit distribution under the doubling fold, proving CP conservation is topologically necessary.

### A9. The Cosmological Constant Problem
* **Problem:** Quantum field theory predicts vacuum energy $10^{120}$ times larger than observed.
* **SADE Model:** Model the vacuum as the ZPE floor $1/2$. Show that the fold's boundary conditions naturally regulate the vacuum energy to exactly $1/2$, not the divergent sum predicted by unbounded QFT.

---

## Category B: Unsolved Mathematics — Millennium Problems & Beyond

### B1. P vs NP
* **Problem:** Can every problem whose solution is quickly verifiable also be quickly solved?
* **SADE Model:** Model "solving" as forward fold iteration (exponential divergence) and "verifying" as backward preimage checking (polynomial). Show that the asymmetry of the doubling map ($2x$ forward vs $x/2$ backward) structurally separates P from NP.

### B2. Navier-Stokes Existence & Smoothness
* **Problem:** Do smooth solutions to the Navier-Stokes equations always exist in 3D?
* **SADE Model:** Model fluid flow as coupled rational orbits under the fold. Investigate whether chaotic orbits with odd denominators ever "blow up" (escape $(0,1]$), or whether the modulo-1 boundary guarantees perpetual smoothness.

### B3. Yang-Mills Mass Gap
* **Problem:** Prove that Yang-Mills gauge theory has a positive mass gap.
* **SADE Model:** Model the Yang-Mills vacuum as the ZPE floor $1/2$. The smallest excitation above the vacuum is $\text{take}(1, 1/2) = 1/2$. Show that no state closer to the vacuum than $1/(2q)$ can exist for any finite odd $q$, proving a discrete mass gap.

### B4. Birch & Swinnerton-Dyer Conjecture
* **Problem:** Relates the rank of elliptic curves to the behavior of their L-functions at $s=1$.
* **SADE Model:** Model elliptic curve rational points as fold orbits. Use `find_integer_relation_lll` to search for relations between the orbit periods and the L-function values at the critical point $s=1$.

### B5. Hodge Conjecture
* **Problem:** Certain cohomology classes on algebraic varieties are combinations of algebraic subvarieties.
* **SADE Model:** Model cohomology classes as sums of fold orbit cycle lengths. Use LLL to find integer decompositions of these sums into prime-sector contributions.

### B6. Collatz Conjecture (3n+1)
* **Problem:** Does the sequence $n \to n/2$ (even) or $n \to 3n+1$ (odd) always reach 1?
* **SADE Model:** Map the Collatz iteration to a modified fold on $(0,1]$. Compare the standard doubling fold (always reaches 1 for $q = 2^k$) with the Collatz fold (mixes $\times 2$ and $\times 3$ operations). Analyze whether the $3n+1$ step introduces odd-denominator traps.

### B7. Goldbach's Conjecture
* **Problem:** Every even integer $> 2$ is the sum of two primes.
* **SADE Model:** Model primes as the generators of fold orbit periods ($\text{ord}_2(p)$). Show that for every even number $2n$, there exist two primes $p, q$ whose orbit periods combine to tile the $2n$-step cycle.

### B8. Twin Prime Conjecture
* **Problem:** Are there infinitely many pairs of primes differing by 2?
* **SADE Model:** Model twin primes $(p, p+2)$ as adjacent odd denominators in the Stern-Brocot tree. Use `approximate_interval` to show that the density of twin-prime mediants never drops to zero.

### B9. Continuum Hypothesis (Unprovable in ZFC)
* **Problem:** Is there a set whose cardinality is strictly between $\aleph_0$ and $2^{\aleph_0}$?
* **SADE Model:** SFTOE operates on countable rationals only. Model the reals as the completion of fold orbits. Show that under fold dynamics, there is no "intermediate" cardinality because every orbit is either finite (halting) or countably periodic.

### B10. Gödel's Incompleteness
* **Problem:** Any consistent formal system containing arithmetic has true but unprovable statements.
* **SADE Model:** Model formal proofs as fold derivation trees (sequences of `fold` and `take`). Construct a self-referential state $G$ that encodes "this orbit is not derivable from ONE" and show it is a valid periodic hypothesis orbit that cannot be reached by the pathfinder.

---

## Category C: Time, Causality, and Spacetime

### C1. Arrow of Time (Why Time Flows Forward)
* **Problem:** Fundamental laws are time-symmetric, yet we experience an irreversible direction of time.
* **SADE Model:** The doubling fold $f(x) = 2x \pmod 1$ is not invertible (two preimages map to one image). This inherent information loss ($\lambda = \ln 2 > 0$) defines a thermodynamic arrow of time. Show that reversing the fold requires knowledge of the discarded MSB.

### C2. Time Travel & Closed Timelike Curves
* **Problem:** General Relativity permits CTCs (loops in time), but they create paradoxes.
* **SADE Model:** Model a CTC as a periodic orbit under the fold. A "time traveler" is a state that returns to its exact starting value after $L$ steps. Show that the Novikov self-consistency principle is automatically enforced: the orbit is deterministic and self-consistent by construction.

### C3. Retrocausality & Delayed-Choice Experiments
* **Problem:** Quantum eraser experiments appear to show future choices affecting past events.
* **SADE Model:** Model entangled pairs as two states with a shared denominator. Show that the fold identity $\text{fold}(\text{take}(x, 1/2)) = \text{fold}(x)$ means "erasing" information about one photon does not change the other's orbit — proving no retrocausal signal.

### C4. Alcubierre Warp Drive / FTL Travel
* **Problem:** The Alcubierre metric requires negative energy density (exotic matter).
* **SADE Model:** Show that "negative energy" corresponds to states outside the SFTOE domain $(0, 1]$. Since the domain is bounded and the fold cannot produce values $\leq 0$ or $> 1$, exotic matter is structurally forbidden. FTL is impossible under fold dynamics.

---

## Category D: Energy, Thermodynamics, and "Free Energy"

### D1. Perpetual Motion (1st and 2nd Kind)
* **Problem:** Proven impossible by the 1st and 2nd Laws of Thermodynamics.
* **SADE Model:** Show that every fold step irreversibly discards 1 bit ($\lambda = \ln 2$). No feedback mechanism can recover the lost bit without external energy input (Landauer's limit). Simulate a "perpetual motion machine" under fold dynamics and prove it always halts or dissipates.

### D2. Zero-Point Energy Extraction
* **Problem:** Can useful work be extracted from the quantum vacuum?
* **SADE Model:** The vacuum is the ZPE floor $1/2$. Show that $1/2$ is already the ground state of the fold — there is no state "below" it to extract energy from. Any attempt to `take` from the vacuum produces a value that immediately folds back to $1/2$.

### D3. Cold Fusion / LENR
* **Problem:** Room-temperature nuclear fusion was claimed in 1989 but never reliably reproduced.
* **SADE Model:** Model nuclear binding as the fold of two prime-sector states. Show that the energy barrier (the number of fold steps required to reach unison) is enormous for heavy nuclei, requiring exponential iteration — explaining why "cold" fusion is energetically prohibited at low fold depths.

### D4. Casimir Energy Harvesting
* **Problem:** Can the Casimir effect between conducting plates be used to generate unlimited energy?
* **SADE Model:** Model the Casimir plates as boundary conditions restricting the fold domain from $(0,1]$ to a sub-interval $(a, b]$. Show that collapsing the plates (narrowing the interval) releases energy, but resetting them (widening it back) costs at least as much — net zero.

---

## Category E: Consciousness, Mind, and the Paranormal

### E1. Telepathy / Mind-to-Mind Communication
* **Problem:** No reproducible evidence for direct mental information transfer.
* **SADE Model:** Model two observers as states $C_a$ and $C_b$. "Telepathy" = achieving phase-locked resonance (identical relative phase paths) without physical coupling. Show that two independent fold orbits can only synchronize if they share a common denominator factor — requiring prior physical interaction.

### E2. Psychokinesis (Mind Over Matter)
* **Problem:** No reproducible evidence for mental influence on physical systems.
* **SADE Model:** Model the observer as $C_k = 1/2^{k+1}$ and the physical system as $x = p/q$. Show that the observer's fold orbit and the system's orbit are mathematically independent unless coupled by `take` or `fold` operations — proving that observation alone cannot alter trajectories.

### E3. Precognition / Seeing the Future
* **Problem:** No reproducible evidence for knowledge of future events.
* **SADE Model:** The fold is deterministic for rational states. If an entity knows the exact rational state $p/q$, it can predict the entire future orbit analytically. "Precognition" = knowing the denominator factorization. Show that this requires complete knowledge of the initial state, which is destroyed by chaotic sensitivity.

### E4. Ghosts / Apparitions
* **Problem:** No reproducible scientific evidence for discarnate consciousness.
* **SADE Model:** Use the mortality decycle framework. After physical death ($2^k$ factor cleared), the invariant odd-denominator orbit persists in the vacuum. A "ghost" = a residual periodic orbit that has been decoupled from a physical host but continues cycling in the ZPE floor. Model its detectability as the beat frequency between the ghost's orbit and a living observer's orbit.

### E5. Remote Viewing
* **Problem:** The CIA's Stargate Project found some statistical anomalies but no actionable intelligence.
* **SADE Model:** Model remote viewing as attempting to determine the state $x$ of a distant system from the observer's local state $C_k$. Show that without physical coupling (shared denominator factors), the relative phase between $x$ and $C_k$ is uniformly distributed — no information transfer.

### E6. Near-Death Experiences (NDEs)
* **Problem:** ~17% of cardiac arrest patients report vivid experiences during clinical death.
* **SADE Model:** Model the dying brain as a state $S = p/(2^k \cdot d)$ undergoing rapid decycling. The transient phase ($2^k$ clearing) generates a burst of high-frequency fold iterations (gamma wave surge). The NDE content = the sequence of states visited during the accelerated transient clearing, experienced as vivid imagery before the invariant orbit is reached.

### E7. Reincarnation / Past-Life Memories
* **Problem:** Ian Stevenson documented cases of children with verified past-life memories.
* **SADE Model:** The invariant odd-denominator orbit ($d$) survives death and persists indefinitely. If a new physical host state $S' = p'/(2^{k'} \cdot d)$ is formed with the same odd factor $d$, the periodic orbit signature is identical. "Past-life memories" = the new host inheriting the same cycle pattern as the deceased, generating matching phase signatures.

### E8. Out-of-Body Experiences (OBEs)
* **Problem:** Subjective experiences of consciousness separating from the physical body.
* **SADE Model:** Model the body as the transient $2^k$ component and consciousness as the invariant $d$ component. An OBE = a temporary decoupling where the observer's self-referential loop ($C_k$) briefly detaches from the body's fold trajectory, operating independently for a few steps before recoupling.

### E9. Integrated Information Theory ($\Phi$) Verification
* **Problem:** IIT proposes consciousness = integrated information ($\Phi$), but $\Phi$ is computationally intractable.
* **SADE Model:** Model $\Phi$ as the LCM of all pairwise cycle lengths in a system of coupled fold orbits. Compute $\Phi$ exactly using `combined_period` for small systems and verify whether it correlates with the presence of closed self-referential loops.

### E10. Penrose-Hameroff Orch-OR (Quantum Consciousness)
* **Problem:** Consciousness arises from quantum collapse in microtubules. Criticized for decoherence.
* **SADE Model:** Model microtubule states as fold orbits with very short periods (high-frequency quantum oscillations). Show that the "objective reduction" threshold corresponds to the ZPE floor $1/2$. Compute the decoherence time as the number of fold steps before a pre-periodic state enters its stable cycle.

---

## Category F: Reality, Simulation, and Multiverse

### F1. Simulation Hypothesis
* **Problem:** Is our reality a computer simulation?
* **SADE Model:** The SFTOE framework is itself a discrete, deterministic, computable system operating on rational numbers. Show that all physical laws emerge from simple fold/take operations — proving that the universe is structurally equivalent to a finite-state automaton. The "simulation" is the fold itself.

### F2. Holographic Principle
* **Problem:** 3D reality may be encoded on a 2D boundary.
* **SADE Model:** The fold maps the 1D interval $(0,1]$ to itself. All orbits, forces, and particles are encoded in the 1D rational number line. Show that the fold's dynamics contain sufficient information to reconstruct all observed 3D physics — proving the holographic principle as a fold boundary encoding.

### F3. Black Hole Information Paradox
* **Problem:** Does information falling into a black hole disappear forever?
* **SADE Model:** Model a black hole as the unison state `ONE` (the fixed point attractor). All states eventually fold toward `ONE`. Show that the information (the denominator factorization of the original state) is encoded in the number of transient steps $k$ and the cycle length $L$ of the orbit — proving information conservation.

### F4. Firewall Paradox
* **Problem:** Is there a destructive energy wall at the event horizon?
* **SADE Model:** Model the event horizon as the transition from pre-periodic to periodic orbit (the decycling threshold). Show that crossing the threshold is smooth (the fold is continuous) — no "firewall" discontinuity. The state simply transitions from transient to cyclic behavior.

### F5. Many-Worlds Interpretation
* **Problem:** Does the universe branch into parallel realities at every quantum measurement?
* **SADE Model:** At each fold step, the state $x$ has two preimages ($x/2$ and $(x+1)/2$). Show that the "branching" is the inverse fold tree, and that all branches are deterministically connected. The "many worlds" are the complete preimage tree of the fold map.

### F6. Boltzmann Brains
* **Problem:** Random thermal fluctuations should produce isolated conscious observers more often than evolved ones.
* **SADE Model:** Model a Boltzmann Brain as a random rational state $p/q$ with a very large denominator that happens to have a consciousness-compatible cycle structure. Calculate the probability of this occurring versus the probability of a structured derivation from `ONE` — showing that structured derivation is exponentially more likely.

---

## Category G: Classical "Impossible" Constructions & Proofs

### G1. Trisecting an Arbitrary Angle
* **Problem:** Proven impossible with compass and straightedge (requires cubic roots).
* **SADE Model:** Model trisection as dividing a fold orbit into 3 equal parts. Use `approximate_ratio(1/3)` and `find_derivation` to construct the closest rational approximation and calculate the shortfall deficit.

### G2. Doubling the Cube (Delian Problem)
* **Problem:** Constructing $\sqrt[3]{2}$ is impossible with compass and straightedge.
* **SADE Model:** $\sqrt[3]{2} \approx 1.2599$. Since this exceeds $(0,1]$, use $\sqrt[3]{2}/2 \approx 0.62996$ as the target. Find the best rational approximation and derive the construction deficit.

### G3. Constructing a Regular Heptagon
* **Problem:** A regular 7-gon cannot be constructed with compass and straightedge.
* **SADE Model:** The heptagon angle is $2\pi/7$. Model this as $\cos(2\pi/7) \approx 0.6234898$ in the fold domain. Use `approximate_ratio` to find the closest constructible rational approximation.

---

## Category H: Biology, Evolution, and Origin of Life

### H1. Abiogenesis (Origin of Life)
* **Problem:** How did non-living chemistry become self-replicating life?
* **SADE Model:** Model self-replication as a fold orbit that, when perturbed, returns to its original cycle. Show that periodic orbits with odd denominators are inherently self-replicating under the fold — they reconstruct themselves after any number of fold steps.

### H2. The Hard Problem of Consciousness (Chalmers)
* **Problem:** Why is there subjective experience at all?
* **SADE Model:** Already investigated in Module I (qualia resonance). Expand to show that qualia are not optional "extras" but are the necessary topological structure of any closed self-referential loop in the fold.

### H3. Free Will vs Determinism
* **Problem:** Are human choices determined by prior causes, or genuinely free?
* **SADE Model:** The fold is deterministic for known rational states. However, if the initial state has an irrational or transcendental component (excluded from SFTOE), the orbit is unpredictable. "Free will" = the irreducible uncertainty in the initial state's denominator factorization.

---

## Category I: Information, Computation, and Cryptography

### I1. One-Way Functions (Cryptographic Foundations)
* **Problem:** Do true one-way functions exist? (Related to P vs NP)
* **SADE Model:** The fold $f(x) = 2x \pmod 1$ is a one-way function: computing $f(x)$ is trivial (multiply by 2), but inverting it requires knowing the discarded MSB. Show that this is the simplest possible one-way function.

### I2. Quantum Supremacy / Quantum Computing Limits
* **Problem:** What problems can quantum computers solve that classical computers cannot?
* **SADE Model:** Model quantum computation as simultaneous exploration of all preimages in the inverse fold tree. Classical computation = forward fold iteration (one path). Show that quantum speedup corresponds to the branching factor of the preimage tree.

### I3. Church-Turing Thesis (Limits of Computation)
* **Problem:** Is the class of computable functions exactly those computable by Turing machines?
* **SADE Model:** Show that the fold automaton (rational states + fold/take operations) is Turing-complete for all computations on rational numbers. Any function expressible as a finite sequence of fold/take steps is computable.

---

## Execution Plan

For each investigation above, we will create:
1. **A Python script** (`<topic_name>.py`) in `secondary_investigation/` that uses SADE's `find_derivation`, `approximate_ratio`, `find_integer_relation_lll`, `combined_period`, and `verify_hypothesis_orbit` to model and analyze the problem.
2. **A findings report** (`<topic_name>_findings.md`) documenting the mathematical results, physical interpretation, and fold-theoretic conclusions.
3. **AST-compliant verification code** generated by `generate_sftoe_code` and validated by `verify_code` and `verify_value`.

### Priority Tiers

**Tier 1 — Execute Immediately (High Impact, Directly Modelable):**
- A1 (Quantum Gravity Unification)
- A4 (Matter-Antimatter Asymmetry)
- A6 (Wave Function Collapse / Measurement Problem)
- B6 (Collatz Conjecture)
- C1 (Arrow of Time)
- C2 (Time Travel / CTCs)
- D1 (Perpetual Motion)
- E4 (Ghosts / Residual Orbits)
- E6 (Near-Death Experiences)
- E7 (Reincarnation)
- F1 (Simulation Hypothesis)
- F3 (Black Hole Information Paradox)

**Tier 2 — Execute Next (Requires Deeper Modeling):**
- A2 (Dark Matter)
- A3 (Dark Energy)
- A5 (Hierarchy Problem)
- A9 (Cosmological Constant)
- B1 (P vs NP)
- B2 (Navier-Stokes)
- B3 (Yang-Mills Mass Gap)
- C3 (Retrocausality)
- D2 (Zero-Point Energy Extraction)
- D4 (Casimir Harvesting)
- E1 (Telepathy)
- E3 (Precognition)
- F2 (Holographic Principle)
- F5 (Many-Worlds)
- H1 (Abiogenesis)
- H3 (Free Will)

**Tier 3 — Theoretical Extensions:**
- B4–B5, B7–B10 (Remaining math problems)
- C4 (Warp Drive)
- D3 (Cold Fusion)
- E2, E5, E8–E10 (Remaining paranormal)
- F4, F6 (Remaining reality)
- G1–G3 (Classical constructions)
- I1–I3 (Computation)
