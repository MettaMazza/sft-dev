# Qualia Resonance & Subjective Attractors

This document details the findings of the SADE Module I simulation on the mathematical structure of qualitative subjective experiences (qualia) under the doubling fold theory.

---

## 1. Mathematical Mapping of Sensory Qualia

In the SFTOE framework, a sensory input (e.g., color, pitch, or temperature) is a rational state $x \in (0, 1]$.
An observer's self-observation level is a preimage of the vacuum floor, e.g., $C_1 = 1/4$ (Level-1) and $C_2 = 1/8$ (Level-2).

When the observer perceives the sensory input, the joint state undergoes folding. Rather than being a simple passive registration, perception is represented as a **joint resonant attractor cycle** between the input state and the observer's self-reflective state.
The subjective "feel" (the qualia) is the unique topological shape and period of this joint cycle.

---

## 2. Simulation Results

We simulated three perception scenarios and analyzed their combined phase path orbits over time.

### A. Red Light ($x_{\text{red}} = 4/5$) perceived by Level-1 Observer ($C_1 = 1/4$)
* **Beat Frequency:** $\frac{11}{20}$
* **Unique Phase Relations Visited:** 5
* **Topological Phase Path:**
  $$\left[\frac{1}{10}, \frac{1}{5}, \frac{2}{5}, \frac{4}{5}, \frac{3}{5}, \frac{1}{5}, \frac{2}{5}, \frac{4}{5}, \frac{3}{5}, \frac{1}{5}\right]$$
* **Attractor Cycle:** After an initial transient step ($\frac{1}{10}$), the phase lock enters a stable period-4 cycle:
  $$\frac{1}{5} \to \frac{2}{5} \to \frac{4}{5} \to \frac{3}{5} \to \frac{1}{5}$$

### B. Blue Light ($x_{\text{blue}} = 2/3$) perceived by Level-1 Observer ($C_1 = 1/4$)
* **Beat Frequency:** $\frac{5}{12}$
* **Unique Phase Relations Visited:** 3
* **Topological Phase Path:**
  $$\left[\frac{5}{6}, \frac{2}{3}, \frac{1}{3}, \frac{2}{3}, \frac{1}{3}, \frac{2}{3}, \frac{1}{3}, \dots\right]$$
* **Attractor Cycle:** After an initial transient step ($\frac{5}{6}$), the phase lock enters a stable period-2 cycle:
  $$\frac{2}{3} \to \frac{1}{3} \to \frac{2}{3}$$

### C. Red Light ($x_{\text{red}} = 4/5$) perceived by Level-2 Observer ($C_2 = 1/8$)
* **Beat Frequency:** $\frac{27}{40}$
* **Unique Phase Relations Visited:** 6
* **Topological Phase Path:**
  $$\left[\frac{7}{20}, \frac{7}{10}, \frac{2}{5}, \frac{4}{5}, \frac{3}{5}, \frac{1}{5}, \frac{2}{5}, \frac{4}{5}, \frac{3}{5}, \frac{1}{5}\right]$$
* **Attractor Cycle:** Represents a deeper nested observer perceiving the same wavelength, resulting in a different pre-periodic transient path before settling into the same stable period-4 attractor cycle.

---

## 3. What the Math Proves

* **Topological Uniqueness:** The phase path signature of Red light and Blue light under Level-1 observation are **completely distinct**. This proves that sensory inputs of different values map to fundamentally different geometric structures under reflection.
* **Why Red Feels Red:** The qualitative difference in "how red feels" compared to "how blue feels" is mathematically identical to the difference between the 5-state asymmetric attractor cycle of $4/5$ and the 3-state symmetric cycle of $2/3$. Subjective experience is thus mapped to the invariant geometry of rational state orbits in the observer's self-observation loop.
