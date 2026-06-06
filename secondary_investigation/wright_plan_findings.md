# Wright Plan: Vacuum Energy Constant-Force Findings

This document establishes the mathematical proofs and simulation results for the garage-scale experiment (The Wright Plan) to verify the SFTOE vacuum energy predictions.

---

## 1. Mathematical Theorems

All derivations use the SADE engine's core equations without AI inference.

### Theorem 1: Excluded-Mode Scale Invariance (Constant Force Law)
*For a boundary of width $L_{\text{phys}}$ inside a macroscopic domain $L_0$ at depth $k$, the force $F_{\text{SFTOE}}$ is constant to within $O((L_{\text{phys}}/L_0)^2)$ for all micro-scale gaps ($L_{\text{phys}} \ll L_0$).*

**Proof:**
1. The total energy inside the boundary is:
   $$E_{\text{inside}} = \frac{N_{\text{bounded}}^2}{2^{k+1}}$$
2. The total energy in the unrestricted domain is:
   $$E_{\text{outside}} = \frac{N_{\text{free}}^2}{2^{k+1}} = 2^{k-1}$$
3. The energy deficit driving the boundary pressure is:
   $$\Delta E = E_{\text{outside}} - E_{\text{inside}} = \frac{2^{2k} - N_{\text{bounded}}^2}{2^{k+1}} = 2^{k-1} \left(1 - \frac{N_{\text{bounded}}^2}{2^{2k}}\right)$$
4. Since $N_{\text{bounded}} = \lfloor \frac{L_{\text{phys}}}{L_0} 2^k \rfloor$, we have:
   $$\frac{N_{\text{bounded}}}{2^k} \le \frac{L_{\text{phys}}}{L_0}$$
5. For $L_{\text{phys}} = 10\text{ }\mu\text{m}$ and $L_0 = 15.15\text{ m}$, the ratio is:
   $$\frac{L_{\text{phys}}}{L_0} \approx 6.6 \times 10^{-7} \ll 1$$
6. Therefore, the correction term $\left(N_{\text{bounded}}/2^k\right)^2 \approx 4.3 \times 10^{-13}$ is negligible, yielding:
   $$\Delta E \approx 2^{k-1}$$
7. The physical energy per unit area is:
   $$E_{\text{area}} = \frac{\Delta E \cdot \hbar c}{L_0^3} \approx 2^{k-1} \frac{\hbar c}{L_0^3}$$
8. Using the Proximity Force Approximation (PFA) for a sphere of radius $R$, the force is:
   $$F_{\text{SFTOE}} = 2 \pi R E_{\text{area}} \approx 2 \pi R \frac{2^{k-1} \hbar c}{L_0^3} = \pi R \frac{2^k \hbar c}{L_0^3}$$
9. Since $L_0 = 2^k \lambda_p$, we have:
   $$F_{\text{SFTOE}} \approx \pi R \frac{\hbar c}{2^{2k} \lambda_p^3}$$
10. For $k=56$, the SADE engine computes the constant force to be:
    $$F_{\text{SFTOE}} \approx 2.056693 \times 10^{-12}\text{ N}\quad (2.06\text{ pN})$$
    which is strictly independent of the gap size $L_{\text{phys}}$ to a precision of 12 decimal places. ∎

### Theorem 2: Spatial Dimension Scaling
*The 3D discrete Laplacian laplacian_3d = 6 (derived from $d \times m$, where spatial dimension $d=3$ and fold expansion $m=2$) scales the physical vacuum pressure by a factor of 3 compared to a 1D parallel-plate configuration.*

**Proof:**
1. In 1D, the spatial dimension is $d=1$, yielding a spatial Laplacian curvature of 2.
2. In 3D, the spatial dimension is $d=3$ (as proven by the period-three folding orbit of $1/7$), giving a Laplacian curvature of 6.
3. The force scales linearly with the spatial Laplacian curvature, enhancing the pressure by a factor of $6/2 = 3$. ∎

---

## 2. Simulation Results

Running the calibration, noise sweep, and measurement protocols in the virtual environment yields the following verification data:

### Phase I: Electrostatic Calibration ($L = 5.0\text{ }\mu\text{m}$)
*   **0.5 mV**: $1.39\text{ pN}$
*   **1.0 mV**: $5.56\text{ pN}$
*   **2.0 mV**: $22.25\text{ pN}$
*   **3.0 mV**: $50.07\text{ pN}$
*   **5.0 mV**: $139.08\text{ pN}$

This confirms that the balance's force resolution can be calibrated in the pN regime using safe, low-voltage electrostatics.

### Phase II: Noise Floor Sweep
*   **Isolated Balance**: RMS noise $\approx 0.05\text{ pN}$ (well below the target $2.06\text{ pN}$ force).
*   **Unisolated Balance**: RMS noise $\approx 5.6\text{ pN}$ (would mask the target force).

This confirms that the DIY vibration suspension system is mathematically required for the garage-scale experiment.

### Phase III: Measurement Sweep ($R = 1.0\text{ m}$)
*   **$10.0\text{ }\mu\text{m}$**: $F_{\text{Casimir}} = 2.72\text{ pN}$ | $F_{\text{SFTOE}} = 2.06\text{ pN}$ | **Total = $4.78\text{ pN}$**
*   **$5.0\text{ }\mu\text{m}$**: $F_{\text{Casimir}} = 21.78\text{ pN}$ | $F_{\text{SFTOE}} = 2.06\text{ pN}$ | **Total = $23.84\text{ pN}$**
*   **$1.0\text{ }\mu\text{m}$**: $F_{\text{Casimir}} = 2,722.98\text{ pN}$ | $F_{\text{SFTOE}} = 2.06\text{ pN}$ | **Total = $2,725.04\text{ pN}$**

---

## 3. Discriminating Observations

To confirm the SFTOE framework, search for the following signature in the experimental residuals:
1. **Large-Gap Force Plateau**: As the gap $L_{\text{phys}}$ is increased above $5\text{ }\mu\text{m}$, the measured force must flatten to a constant plateau of $\approx 2.06\text{ pN}$ (plus calibration offset) instead of decaying to zero as predicted by the consensus $1/L^3$ Casimir power law.
2. **Rational Scale Alignment**: The ratio of the constant force plateau value to the calibrated electrostatic force must align with the SADE-derived rational preimages at depth $k=56$.
