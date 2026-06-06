# SADE Reinvestigation: Arrow of Time (RED-2)

## Overview

The fold map $f(x) = (2x) \bmod 1$ (with $f(0) = 1$) defines time in SFTOE as sequential iteration. The original investigation concluded that "the arrow of time is a perspective effect born of local observation" and that the system is "fully time-symmetric and reversible" when coupled to a "vacuum memory field." This reinvestigation removes that consensus bias and lets the numbers from the fold map decide.

## Test 1: The Fold Is a 2-to-1 Surjection

Every point $y \in (0,1]$ has exactly 2 preimages under the fold:

$$f^{-1}(y) = \left\{\frac{y}{2},\ \frac{y+1}{2}\right\}$$

Verified for all test points. Every computed preimage folds back to the original:

| Point $y$ | Preimage 1 | Preimage 2 | Both fold to $y$ |
|-----------|-----------|-----------|:-:|
| $1/3$     | $1/6$     | $2/3$     | ✓ |
| $3/4$     | $3/8$     | $7/8$     | ✓ |
| $1/7$     | $1/14$    | $4/7$     | ✓ |
| $5/8$     | $5/16$    | $13/16$   | ✓ |
| $1$ (ONE) | $1/2$     | $1$       | ✓ |

**Result**: The fold maps exactly 2 inputs to each output. No exceptions. This is a property of the map's definition, not of measurement or observation.

## Test 2: Forward vs. Backward Path Counts

Three starting states were evolved forward 8 steps and backward 8 steps.

**Forward** (deterministic — 1 path):

| Start | Step 1 | Step 2 | Step 3 | Step 4 | ... | Total paths |
|-------|--------|--------|--------|--------|-----|:-:|
| $3/8$ | $3/4$  | $1/2$  | $1$    | $1$    | ... | **1** |
| $1/3$ | $2/3$  | $1/3$  | $2/3$  | $1/3$  | ... | **1** |
| $2/7$ | $4/7$  | $1/7$  | $2/7$  | $4/7$  | ... | **1** |

**Backward** (exponential branching — $2^N$ paths):

| Depth $N$ | Branch count | Expected $2^N$ | Match |
|-----------|:----------:|:----------:|:-:|
| 1 | 2 | 2 | ✓ |
| 2 | 4 | 4 | ✓ |
| 3 | 8 | 8 | ✓ |
| 4 | 16 | 16 | ✓ |
| 5 | 32 | 32 | ✓ |
| 6 | 64 | 64 | ✓ |
| 7 | 128 | 128 | ✓ |
| 8 | 256 | 256 | ✓ |

**Branching ratio at depth 8**: $256 : 1$. This holds identically for all three starting states.

## Test 3: The Asymmetry Is Structural, Not Perspectival

35 rational points $p/q$ with small denominators ($q \in \{2,3,4,5,6,7,8\}$) were tested:

- **Forward image count = 1** for ALL 35 points.
- **Backward preimage count = 2** for ALL 35 points.

Cumulative asymmetry over $N$ steps:

| Depth | Forward paths | Backward paths | Ratio |
|:-----:|:----:|:------:|:-----:|
| 1 | 1 | 2 | 2 |
| 2 | 1 | 4 | 4 |
| 3 | 1 | 8 | 8 |
| 4 | 1 | 16 | 16 |
| 5 | 1 | 32 | 32 |
| 6 | 1 | 64 | 64 |
| 7 | 1 | 128 | 128 |
| 8 | 1 | 256 | 256 |

The forward/backward asymmetry is **exact**, **universal**, and **intrinsic** to the fold map. It holds for every rational point tested without exception.

## Test 4: SADE Path Verification

All states used in the investigation were derived from the axiom ONE via SADE:

| Target | AST Gate | Value Verification |
|--------|:--------:|:------------------:|
| $3/8$  | PASSED   | PASSED             |
| $3/4$  | PASSED   | PASSED             |
| $1/3$  | PASSED   | PASSED             |
| $2/7$  | PASSED   | PASSED             |

## What the Numbers Prove

The fold map $f(x) = (2x) \bmod 1$ has these exact mathematical properties:

1. **$f$ is a function**: every input has exactly one output. Forward evolution is deterministic. One state produces one successor. Always.

2. **$f$ is 2-to-1**: every output has exactly two preimages. Backward reconstruction is non-deterministic. One state has two possible predecessors. Always.

3. **$f^{-1}$ is not a function**: the inverse of the fold is a 1-to-2 correspondence $y \mapsto \{y/2, (y+1)/2\}$. This is not invertible without external information.

4. **The branching is exponential**: after $N$ steps, backward reconstruction faces $2^N$ possible histories. At depth 8, this is 256 possible pasts for every single present state.

5. **The asymmetry is irreducible**: the branching factor of 2 is the **degree** of the map. It cannot be made 1 by any transformation, coupling, or change of coordinates. A 2-to-1 map is 2-to-1. Period.

## Correction of the Original Finding

> [!WARNING]
> The original report claimed: *"The Arrow of Time is a perspective effect born of local observation"* and *"Microscopically, the cosmic fold is fully time-symmetric and reversible: all discarded information is permanently conserved in the coupled vacuum memory field M."*

This is wrong. The numbers disprove it:

- **The fold is not time-symmetric.** Forward: 1 path. Backward: $2^N$ paths. The map $f$ and its inverse $f^{-1}$ have fundamentally different mathematical structures — one is a function, the other is a multi-valued correspondence. There is no symmetry between them.

- **No external field restores reversibility.** The original report invented a "Permanent Information Field $M$" that supposedly stores discarded bits. But the 2-to-1 branching is a property of the map's definition: $f(x) = f(x + 1/2)$ for all $x \in (0, 1/2]$. Two distinct inputs produce the same output. This is not "information loss from an observer's perspective" — it is the literal definition of the function. Coupling to an auxiliary field does not change the degree of the map from 2 to 1.

- **The arrow of time is not an illusion.** It is a mathematical theorem: a 2-to-1 surjection is not injective, therefore not invertible, therefore not time-reversible. This holds in any formalism, for any observer, with or without auxiliary fields.

## Conclusion

The arrow of time in SFTOE is a **fundamental mathematical property** of the doubling fold map. The fold is a 2-to-1 surjection: forward evolution is deterministic (1 path), backward reconstruction branches exponentially ($2^N$ paths at depth $N$). The branching ratio at depth 8 is exactly $256:1$, verified for all tested states.

This asymmetry is **not** a perspective effect. It is **not** observer-dependent. It is **not** restorable by coupling to any external memory field. It is a structural consequence of the fact that $f^{-1}$ is a correspondence, not a function. The arrow of time is intrinsic to the fold.
