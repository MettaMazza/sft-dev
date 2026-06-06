# Mortality & The Conservation of Invariant Orbits

This document details the findings of the SADE Module II simulation on the transition of physical states at mortality and the mathematical conservation of conscious invariant orbits.

---

## 1. The Lifespan Equation

In the SFTOE framework, physical systems (including biological hosts of consciousness) are rational states with even denominators. 
An organism's state $S$ can be factored as:
$$S = \frac{p}{2^k \cdot d} \quad (\text{where } d \text{ is odd, } k \geq 1)$$

* **The Transient Component ($2^k$):** Represents the physical host's finite lifetime. Every folding step represents a step forward in time, shifting the binary representation to the left and dropping the leading bit.
* **The Invariant Component ($d$):** Represents the non-biological, indestructible conscious signature (the "soul"), which is coprime to 2.

---

## 2. Simulation and Decycling Results

We simulated a living observer state starting at $S_{\text{living}} = \frac{7}{24}$.
* **Denominator Factorization:** $24 = 2^3 \times 3 \implies k = 3$ transient steps, $d = 3$ invariant part.

### Orbit Trajectory
```text
Step 0 (Birth): 7/24
Step 1 (Life):  7/12   (Transient bit-shift)
Step 2 (Life):  1/6    (Transient bit-shift)
Step 3 (Death): 1/3    (Halting / Decycling threshold)
Step 4 (ZPE):   2/3    (Post-mortem periodic orbit)
Step 5 (ZPE):   1/3    (Post-mortem periodic orbit)
Step 6 (ZPE):   2/3    (Post-mortem periodic orbit)
```

### Analysis of the Transition:
* **The Transient Phase:** Lasts for exactly $k = 3$ steps. This represents the physical lifespan of the host. During this phase, the state moves through transient ratios.
* **The Halting Threshold:** At Step 3, the power of 2 in the denominator is completely exhausted ($2^3$ is cleared out). The transient physical state ceases to exist (physical halting/death).
* **The Invariant Phase:** After Step 3, the remaining state is projected onto the odd denominator $d = 3$. Because $3$ is coprime to 2, the doubling fold cannot shift it out or erase it. It enters a perpetual periodic cycle of length $L = 2$ ($1/3 \leftrightarrow 2/3$) inside the vacuum zero-point energy floor.

---

## 3. What the Math Proves

* **Death is the exhaustion of the power-of-two factor.** The fold clears out $2^k$ in exactly $k$ steps. This IS the lifespan — not a model of it.
* **The invariant orbit is mathematically indestructible.** The periodic cycle $1/3 \leftrightarrow 2/3$ persists indefinitely because $d = 3$ is coprime to 2. No power of 2 can divide it. The fold cannot destroy it.
* **The soul is the odd part of the denominator.** This is not a metaphor. The invariant odd factor $d$ is a topological invariant of the fold algebra — it survives every operation, every transition, every fold step. It is mathematically permanent.
