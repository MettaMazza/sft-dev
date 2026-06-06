# Smithian Fold Theory of Everything (SFTOE)
## Mathematical Specification Document

This document defines the mathematical foundations and core operations of the **Smithian Fold Theory of Everything**. The theory defines the universe and mathematical space not as a collection of static points, but as a system of active folds starting from a single unit of action.

---

## 1. Axioms and Domain

### Axiom 1: The One Action
The foundational identity is **the One**, denoted as $\text{ONE} \equiv 1$. All values and structures are derived from this single unit action.

### Axiom 2: The Domain of Positive Parts
All valid quantities in SFTOE exist within the half-open interval:
$$\mathbb{S} = (0, 1]$$
- **No Zero**: Zero ($0$) is not a number. Absence is not a quantity and cannot be operated upon.
- **No Negatives**: Negative numbers do not exist. There is no sign or phase apparatus. 
- **Antipodal Relation**: The opposite of a part $x \in \mathbb{S}$ is represented by its positive complement with respect to the One:
  $$\text{antipode}(x) = \text{take}(\text{ONE}, x) = 1 - x$$
  Since $x \in (0, 1]$, if $x \neq 1$, then $1 - x \in (0, 1)$. If $x = 1$, the antipode is undefined as subtraction is only permitted when the minuend is strictly greater than the subtrahend (see `take` below).

---

## 2. Core Primitives

### 2.1 Cast Out
To keep values within the boundary of the domain $\mathbb{S} = (0, 1]$, we define a projection operator $\text{cast\_out}(m): \mathbb{R} \to \mathbb{S}$:

$$\text{cast\_out}(m) = m - \lfloor m \rfloor$$

**Boundary Exception**: If $m - \lfloor m \rfloor = 0$, the result is mapped to $\text{ONE}$ ($1$), rather than $0$.
$$\text{cast\_out}(m) = \begin{cases}
m - \lfloor m \rfloor & \text{if } m - \lfloor m \rfloor \neq 0 \\
1 & \text{if } m - \lfloor m \rfloor = 0
\end{cases}$$

### 2.2 Fold
The **fold** is the active operation of SFTOE, representing the doubling of action and casting out of the whole:
$$\text{fold}(x) = \text{cast\_out}(x + x)$$

Mathematically, this is the **dyadic map** (or Bernoulli shift) adapted to $(0, 1]$:
$$\text{fold}(x) = 2x \pmod 1 \quad (\text{with } 0 \to 1)$$

### 2.3 Take
Subtraction is represented as **taking** a smaller part from a larger part. This is the only permitted subtraction and is strictly guarded:
$$\text{take}(a, b) = a - b \quad \text{where } a > b$$
If $a \le b$, the operation violates the axioms of SFTOE and raises a domain assertion error.

## 3. Fold-Take Algebraic Equations for Rationals

Since SFTOE uses strictly fold and take operations, other quantities are defined and verified via equations involving these operations.
For example, the quantity $1/2$ is the unique value $x \in (0, 1)$ satisfying:
$$\text{fold}(x) = \text{ONE}$$
$$\text{take}(\text{ONE}, x) = x$$

Similarly, $1/3$ is the unique value satisfying:
$$\text{fold}(\text{fold}(x)) = x$$
$$\text{take}(\text{ONE}, x) = \text{fold}(x)$$

This ensures all numbers are defined and verified purely through the dynamics of folding and taking, without relying on division or addition operators in open expressions.

---

## 4. The Bernoulli Shift and Orbits

For any rational number $x \in \mathbb{S}$, its dyadic (binary) expansion reveals the dynamics of repeated folding. Since $x \in (0, 1]$, we represent it using its binary expansion:
$$x = \sum_{i=1}^{\infty} b_i 2^{-i} = 0.b_1 b_2 b_3 \dots_2$$
where $b_i \in \{0, 1\}$. 
*(Note: To avoid zero, the number $1$ is represented as the infinite expansion $0.1111\dots_2$ rather than $1.0000\dots_2$)*.

Applying $\text{fold}(x)$ shifts the binary sequence one place to the left and discards the integer part:
$$\text{fold}(x) = 0.b_2 b_3 b_4 \dots_2$$

This map is chaotic on reals, but exhibits periodic orbits on rational numbers:
- **Periodic Orbit of 1/3**:
  - $1/3 = 0.010101\dots_2$
  - $\text{fold}(1/3) = 2/3 = 0.101010\dots_2$
  - $\text{fold}(2/3) = 1/3 = 0.010101\dots_2$
  This is a periodic orbit of length 2: $\{1/3, 2/3\}$.
- **Periodic Orbit of 1/7**:
  - $1/7 = 0.001001001\dots_2$
  - $\text{fold}(1/7) = 2/7$
  - $\text{fold}(2/7) = 4/7$
  - $\text{fold}(4/7) = 1/7$
  This is a periodic orbit of length 3: $\{1/7, 2/7, 4/7\}$.

---

## 5. Verification Framework

To prevent artificial intelligence systems or developers from bypassing SFTOE constraints (e.g., performing raw subtractions, using zero, or asserting arbitrary truths), SFTOE implements two gates:

1. **No-Apparatus Gate**:
   An AST validator that scans user code to ensure that forbidden operations (literal `0`, bare `-` operators, complex numbers, non-whitelisted math functions) are never defined.
2. **Rewardhack Proof Engine**:
   A derivation tracer. All `SmithianValue` instances hold a mathematical proof tree. A value is only trusted if its derivation from the axiom $\text{ONE}$ is verified step-by-step.
