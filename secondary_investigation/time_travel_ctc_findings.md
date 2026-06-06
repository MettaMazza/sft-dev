# SADE Investigation: Time Travel & Closed Timelike Curves (Topic C2)

## Overview
Closed Timelike Curves (CTCs) are trajectories in spacetime that loop back on themselves, allowing an object to return to its own past. This concept is allowed under certain solutions to Einstein's General Relativity (such as Goedel's rotating universe or Morris-Thorne wormholes) but introduces logical paradoxes (like the grandfather paradox). Under Smithian Fold Theory, we model a CTC as a periodic orbit under the doubling fold map $f(x) = 2x \pmod 1$. This investigation analyzes the self-consistency of these loops.

## Mathematical Results
We simulated trajectories for rational states with odd denominators, which are topologically guaranteed to form periodic cycles:

### The $1/7$ Time Loop (Period $L=3$)
* **Timeline**: $1/7 \to 2/7 \to 4/7 \to 1/7$
* **Self-Consistency**: The state after $3$ steps is exactly $1/7$. 
* **Grandfather Paradox**: Forbidden. There is no point in the loop where the history can branch or mutate; the trajectory is deterministic and closed.

### The $1/5$ Time Loop (Period $L=4$)
* **Timeline**: $1/5 \to 2/5 \to 4/5 \to 3/5 \to 1/5$
* **Self-Consistency**: The state after $4$ steps is exactly $1/5$.

## The Novikov Self-Consistency Principle
The Novikov self-consistency principle asserts that if time travel is possible, the laws of physics must allow only self-consistent histories. 
In SFTOE, this principle is a direct mathematical consequence of the fold's determinism:
* The fold map $f(x)$ is a deterministic function.
* For any rational state with an odd denominator $q$, the sequence $x_k = f^k(x_0)$ is periodic with period $L$ dividing $\text{ord}_2(q)$.
* By definition, the boundary conditions match exactly at $k=0$ and $k=L$.
* Because there is no external randomness or branching in the forward direction, the timeline is globally self-consistent and closed by construction.

## SADE Path Verification
We verified the mathematical validity of the periodic state $1/7$ using SADE:
* **AST Gate Check**: Passed (no literal `0`, no bare `-`)
* **Value Verification**: Passed (returns verified `SmithianValue` of $1/7$)

## What the Math Proves: Natural vs. Synthetic Time Loops

Under Smithian Fold Theory, our understanding of Closed Timelike Curves expands into two distinct categories:

### 1. Natural CTCs (Passive Loops)
Periodic orbits of odd denominators (e.g. $1/7$) are naturally self-consistent. They require no energy or external information input to repeat because their boundary conditions close perfectly on themselves. These represent stable matter configurations.

### 2. Synthetic CTCs (Active/Memory-Driven Loops)
With the discovery of the **Permanent Information Field**, we can now construct time loops for *transient* states (even denominators) that would normally decay to the ground state. By feeding back the discarded bits stored in the memory buffer $M$ (acting as a temporal guide), we can force a transient state to reverse its decay and reconstruct its past, creating a synthetic time loop.

### 3. Reconstructive Time Travel
Because the information field $M$ is a perfect record of the system's trajectory, any observer with access to the field can execute "reconstructive time travel" — reconstructing the exact physical state at any past coordinate. The grandfather paradox is resolved because the past is retrieved analytically from a conserved record rather than physically re-entered, ensuring absolute causality and self-consistency.
