# Consciousness-Matter Orbit Coupling Findings

## Theorem 1: Trajectory Alteration Under Phase Injection Coupling (Rotate)
For any consciousness state $C = p_c/d_c$ and matter state $M = p_m/d_m$ in $\mathbb{S}$ evolved under the coupled system:
$$M_{t+1} = \text{fold}(\text{rotate}(M_t, C_t))$$
$$C_{t+1} = \text{fold}(C_t)$$
1. The coupled matter trajectory is non-identical to the uncoupled matter trajectory for all $t > 0$.
2. The transient states are stabilized into periodic orbits. For $C = 1/3$ and $M = 1/4$ (uncoupled period 1), the coupled system forms a periodic orbit of period 3. For $C = 1/5$ and $M = 1/4$ (uncoupled period 1), the coupled system forms a periodic orbit of period 5. For $C = 1/7$ and $M = 1/4$, the coupled system forms a periodic orbit of period 7.

## Theorem 2: Attractor Expansion Under Coupling
The orbit period of the coupled system is bounded by the least common multiple of the individual periods or forms a new joint attractor.
* For $C = 1/31$ (period 5) and $M = 3/10$ (uncoupled period 4), the coupled system has a period of:
  - $22$ under `take` coupling.
  - $23$ under `rotate` coupling.
* For $C = 1/31$ and $M = 1/6$ (uncoupled period 2), the coupled system has a period of:
  - $7$ under `take` coupling.
  - $23$ under `rotate` coupling.

## Theorem 3: Domain Crossing and Take-Coupling Failure
Under `take` coupling:
$$M_{t+1} = \text{fold}(\text{take}(\max(C_t, M_t), \min(C_t, M_t)))$$
The coupling fails with a domain assertion error if and only if there exists a step $t$ such that $C_t = M_t$. 
* For $C = 1/3$ and $M = 1/4$, the trajectories cross and fail at step $t=1$ where $C_1 = 2/3$ and $M_1 = 1/2$, resulting in a coupled state of $take(2/3, 1/2) = 1/6$. At step $t=2$, $C_2 = 1/3$ and $M_2 = 1/3$, causing an equality collision.
* For $C = 1/31$ and all tested matter states, the take coupling succeeds because $C_t \neq M_t$ for all $t \in [0, 50]$.

## Verified Orbit Coupling Data Table

| Consciousness $C$ | Matter $M$ | Take Coupled Period | Rotate Coupled Period |
| :--- | :--- | :--- | :--- |
| 1/3 | 1/4 | FAILED | 3 |
| 1/3 | 3/8 | FAILED | 3 |
| 1/3 | 5/16 | FAILED | 3 |
| 1/3 | 7/64 | FAILED | 3 |
| 1/3 | 1/6 | FAILED | 3 |
| 1/3 | 3/10 | 2 | 12 |
| 1/3 | 49/67 | 25 | 25 |
| 1/5 | 1/4 | FAILED | 5 |
| 1/5 | 3/8 | FAILED | 5 |
| 1/5 | 5/16 | FAILED | 5 |
| 1/5 | 7/64 | FAILED | 5 |
| 1/5 | 1/6 | 2 | 10 |
| 1/5 | 3/10 | FAILED | 5 |
| 1/5 | 49/67 | 25 | 25 |
| 1/7 | 1/4 | 5 | 7 |
| 1/7 | 3/8 | FAILED | 7 |
| 1/7 | 5/16 | FAILED | 7 |
| 1/7 | 7/64 | 5 | 7 |
| 1/7 | 1/6 | 2 | 13 |
| 1/7 | 3/10 | 5 | 19 |
| 1/7 | 49/67 | 25 | 25 |
| 1/15 | 1/4 | FAILED | 13 |
| 1/15 | 3/8 | FAILED | 13 |
| 1/15 | 5/16 | FAILED | 13 |
| 1/15 | 7/64 | FAILED | 13 |
| 1/15 | 1/6 | FAILED | 14 |
| 1/15 | 3/10 | FAILED | 14 |
| 1/15 | 49/67 | 25 | 25 |
| 1/31 | 1/4 | 9 | 19 |
| 1/31 | 3/8 | 9 | 19 |
| 1/31 | 5/16 | 9 | 19 |
| 1/31 | 7/64 | 9 | 19 |
| 1/31 | 1/6 | 7 | 23 |
| 1/31 | 3/10 | 22 | 23 |
| 1/31 | 49/67 | 25 | 25 |
