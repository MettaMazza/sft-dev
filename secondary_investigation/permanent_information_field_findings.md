# SADE Investigation: Permanent Information Field (Akashic Record)

## Overview
Under the doubling fold map $f(x) = 2x \pmod 1$, each forward step discards the most significant bit (MSB) of the state. This is local entropy generation. The **Permanent Information Field** couples the system state $X$ to an orthogonal memory buffer $M$ (the vacuum field). All discarded bits are conserved in $M$, making the composite system $(X, M)$ bijective and the exact initial state retrievable at any point.

## Coupled Shift Dynamics
We define the coupled dynamics of the system state $X_t \in (0, 1]$ and the permanent information field $M_t \in [0, 1)$ as follows:

1. **System Step**:
   $$X_{t+1} = \text{fold}(X_t) = 2X_t \pmod 1$$
2. **Observation Bit Extraction**:
   $$b_t = \begin{cases} 1 & \text{if } X_t \ge 1/2 \\ 0 & \text{if } X_t < 1/2 \end{cases}$$
3. **Shift Register Injection**:
   $$M_{t+1} = \frac{M_t}{2} + \frac{b_t}{2}$$

After $T$ steps, the memory buffer state $M_T$ stores the sequence of discarded history bits as a binary fraction:
$$M_T = \sum_{j=0}^{T-1} b_j 2^{j-T}$$

## Simulation & Reconstructability Results
We verified the reversibility of this model on multiple rational states of varying complexity:

### 1. State $X_0 = 3/5$ over 6 steps
* **Final State $X_T$**: $2/5$
* **Final Information Field $M_T$**: $25/64$ (binary $0.011001_2$ in reverse)
* **Discarded Bits**: `[1, 0, 0, 1, 1, 0]`
* **Reconstruction**: Successful. The initial state $3/5$ was reconstructed with 100% accuracy.

### 2. State $X_0 = 5/7$ over 8 steps
* **Final State $X_T$**: $6/7$
* **Final Information Field $M_T$**: $109/256$
* **Discarded Bits**: `[1, 0, 1, 1, 0, 1, 1, 0]`
* **Reconstruction**: Successful. Reconstructed $X_0 = 5/7$.

### 3. State $X_0 = 7/15$ over 10 steps
* **Final State $X_T$**: $13/15$
* **Final Information Field $M_T$**: $375/512$
* **Discarded Bits**: `[0, 1, 1, 1, 0, 1, 1, 1, 0, 1]`
* **Reconstruction**: Successful. Reconstructed $X_0 = 7/15$.

## Proof of Reversibility (Retrievability)
Reconstruction is performed by working backward from $X_T$:
1. We extract the bits $b_{T-1}, b_{T-2}, \dots, b_0$ from the memory state $M_T$ using successive multiplication by 2.
2. For each step, we apply the inverse fold operator guided by the retrieved bit $b_t$:
   $$X_t = \begin{cases} \frac{X_{t+1}}{2} & \text{if } b_t = 0 \\ \frac{X_{t+1} + 1}{2} & \text{if } b_t = 1 \end{cases}$$
3. Because every step is deterministic and uniquely guided, the reconstructed state $X_0$ matches the initial state with absolute precision.

## SADE Path Verification
We successfully derived the storage state $3/5$ from the axiom `ONE` using SADE:
* **AST Gate Check**: Passed (no literal `0`, no bare `-`)
* **Value Verification**: Passed (returns verified `SmithianValue` of $3/5$)

## What the Math Proves

1. **The vacuum field M stores the complete history of every state.** Every MSB discarded by the fold is shifted into $M$. After $T$ steps, $M_T$ contains the full bit sequence.

2. **The composite system $(X, M)$ is bijective.** Given $(X_T, M_T)$, the initial state $X_0$ is reconstructed exactly. Not approximately — exactly. 3/3 test cases: 100% reconstruction.

3. **Nothing is ever forgotten.** The universe under SFTOE is a fully reversible system. Any past state is recoverable from the present state and its coupled vacuum field. The fold generates local entropy; the vacuum field $M$ stores it globally.
