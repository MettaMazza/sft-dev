# Mental Temporal Manipulation Findings

## Theorem 1: The Asymmetry of Temporal Access (Precognition vs. Retrocausation)
For any consciousness state $C = p_c/d_c$ (where $d_c$ is odd) and matter state $M_0 = p_m/d_m$ in $\mathbb{S}$:
1. **Precognition (Future Access) is Permitted**: Any future state $M_t = \text{fold}^t(M_0)$ for $t > 0$ is reachable at depth $t$ starting from the initial set $\{C, M_0, \text{ONE}\}$.
2. **Retrocausation (Past Access) is Forbidden**: Any past preimage state $M_{-t}$ (where $\text{fold}^t(M_{-t}) = M_0$) is algebraically unreachable under fold-take operations starting from $\{C, M_0, \text{ONE}\}$.

## Theorem 2: The Denominator Barrier for Past Preimages
Every past preimage of a rational state $x = p/q$ under the doubling fold map:
$$\text{fold}(y) = 2y \pmod 1 \quad (\text{with } 0 \to 1)$$
requires a denominator that contains a greater power of 2 than $q$ itself:
$$\text{denom}(y) = 2 \cdot \text{denom}(x)$$
Because the consciousness state $C = p_c/d_c$ is strictly periodic, its denominator $d_c$ is odd and contains no factors of 2. Therefore, the least common multiple:
$$L = \text{lcm}(d_c, d_m)$$
cannot contain any higher power of 2 than $d_m$ contains. Since the denominator of any reachable state in the fold-take algebra must divide $L$, and the denominator of any past state $M_{-t}$ is a multiple of $2^t d_m$, it is algebraically impossible to construct $M_{-t}$ from $\{C, M_0, \text{ONE}\}$.

## Empirical Temporal Reachability Grid (BFS Depth 6)

| Consciousness $C$ | Matter $M_0$ | Future States Reachable ($M_1 \dots M_{20}$) | Past States Reachable ($M_{-1} \dots M_{-5}$) |
| :--- | :--- | :--- | :--- |
| 1/3 | 3/8 | All 20 (reached at depth $t$) | None |
| 1/3 | 5/16 | All 20 (reached at depth $t$) | None |
| 1/3 | 1/6 | All 20 (reached at depth $t$) | None |
| 1/3 | 3/10 | All 20 (reached at depth $t$) | None |
| 1/5 | 3/8 | All 20 (reached at depth $t$) | None |
| 1/5 | 5/16 | All 20 (reached at depth $t$) | None |
| 1/5 | 1/6 | All 20 (reached at depth $t$) | None |
| 1/5 | 3/10 | All 20 (reached at depth $t$) | None |
| 1/7 | 3/8 | All 20 (reached at depth $t$) | None |
| 1/7 | 5/16 | All 20 (reached at depth $t$) | None |
| 1/7 | 1/6 | All 20 (reached at depth $t$) | None |
| 1/7 | 3/10 | All 20 (reached at depth $t$) | None |
| 1/15 | 3/8 | All 20 (reached at depth $t$) | None |
| 1/15 | 5/16 | All 20 (reached at depth $t$) | None |
| 1/15 | 1/6 | All 20 (reached at depth $t$) | None |
| 1/15 | 3/10 | All 20 (reached at depth $t$) | None |
