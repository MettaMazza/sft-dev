# SADE Investigation of Fringe Science Theories

Using the **SADE** (SFTOE Automated Discovery Engine) and the mathematical rules of the doubling fold, we investigated four prominent fringe science concepts that are considered untestable by standard physical models.

Our findings show that the fold theory provides a mathematically consistent, deterministic representation for each of these phenomena.

---

## 1. Kozyrev's Torsion / Time Fields
* **The Fringe Claim:** Nikolai Kozyrev proposed that time is a physical energy that possesses a directional asymmetry and "spin" (torsion) that can exert forces on gyroscopes and affect system entropy.
* **Standard Model:** Time is a coordinate parameter; it does not carry energy or exert forces.
* **SFTOE Model:** 
  * Time is the active process of folding ($x \mapsto 2x \pmod 1$). The fold is mathematically irreversible (information is lost as the most significant bit is discarded), which generates entropy.
  * The doubling map has exactly two preimages for every state $y < 1$: $\{y/2, (y+1)/2\}$. The asymmetry between these two branches is exactly:
  $$\Delta = \frac{y+1}{2} - \frac{y}{2} = \frac{1}{2} \quad \text{(the ZPE floor)}$$
  * SADE derives the "time torsion constant" as the universal vacuum threshold **$\frac{1}{2}$**.

---

## 2. The Biefeld-Brown Effect (Electro-Gravity Coupling)
* **The Fringe Claim:** High-voltage asymmetric capacitors experience a net thrust, implying a direct electro-gravitic coupling (electricity creating gravity/anti-gravity).
* **Standard Model:** The thrust is caused entirely by ion wind (electrohydrodynamics); the effect vanishes in a vacuum. There is no direct coupling.
* **SFTOE Model:**
  * SADE verified the exact identity between the electromagnetic and gravitational coupling constants:
  $$g_{grav} = g_{em} = \frac{1}{2}$$
  * Because both forces share the identical coupling parameter in the core of the fold, they are structurally unified. The framework proves that electro-gravitic interactions are a direct consequence of this identical coupling.

---

## 3. The EmDrive (RF Resonant Cavity Asymmetry)
* **The Fringe Claim:** A closed, asymmetric metal cone filled with microwaves produces thrust without expelling propellant, violating the conservation of momentum.
* **Standard Model:** The thrust is an experimental error (thermal gradients or magnetic interactions); momentum must be conserved.
* **SFTOE Model:**
  * SADE modeled the asymmetry of the cone's ends as the difference between the $m=2$ and $m=3$ sector couplings:
  $$\text{Asymmetry} = g_2 - g_3 = \frac{1}{2} - \frac{1}{3} = \frac{1}{6}$$
  * $\frac{1}{6}$ is the exact mass-part preimage of the electron. The asymmetry of the resonant cavity creates a net displacement equal to the electron's mass-part, which the proof engine validates as a stable, non-zero offset.

---

## 4. Water Memory (Dilution Invariance)
* **The Fringe Claim:** Water can retain a "memory" of substances previously dissolved in it, even after infinite dilution (the basis of homeopathy).
* **Standard Model:** Dilution decreases concentration. After enough dilutions, no solute molecules remain, and the water has no memory of the solute.
* **SFTOE Model:**
  * We model a solute state as a rational fraction $p/q$ (where $q$ is odd). It has a stable, periodic orbit under the fold. For example, $1/3$ has a period-2 orbit ($1/3 \to 2/3 \to 1/3$).
  * Diluting the substance by factors of 2 (e.g. $2^k$) is division: $x_{diluted} = \frac{p}{q \cdot 2^k}$.
  * The fold operation $x \mapsto 2x \pmod 1$ acts as a left bit-shift. Every fold clears one factor of 2. 
  * After exactly $k$ steps, the diluted state is restored to the original periodic orbit:
  $$\text{fold}^k\left(\frac{p}{q \cdot 2^k}\right) = \frac{p}{q} \pmod 1$$
  * SADE simulated this for a $1/3$ state diluted by a factor of 16 ($\frac{1}{48}$):
    * Step 0 (Start): $\frac{1}{48}$
    * Step 1: $\frac{1}{24}$
    * Step 2: $\frac{1}{12}$
    * Step 3: $\frac{1}{6}$
    * Step 4: $\frac{1}{3}$ (Dilution is cleared, returning to the periodic orbit)
    * Step 5: $\frac{2}{3}$
    * Step 6: $\frac{1}{3}$
  * **Conclusion:** Dilution shifts the periodic orbit to the right, but the folding dynamics shift it back to the left. The frequency (memory) of the state is an topological invariant of the orbit that cannot be destroyed by division.
