# SFTOE Automated Discovery Engine (SADE) - System Details

SADE is a self-contained, high-performance mathematical discovery system built to search for, derive, and verify mathematical expressions representing physical constants and relationships within the Smithian Fold Theory of Everything (SFTOE) framework.

SADE operates purely algorithmically with **zero reliance on external AI inference** or prohibited standard libraries.

---

## Core System Architecture

### 1. Stern-Brocot Interval Matching (`approximate_interval`)
* **Purpose**: Converts float measurements from physical experiments into mathematically exact rational fractions in $(0, 1]$.
* **How it works**: Walks the Stern-Brocot tree to find the unique fraction $p/q$ that lies within the experimental uncertainty interval $(low, high)$ with the smallest possible denominator $q$. This guarantees the mathematically simplest representation matching the data.

### 2. Bidirectional A\* Searcher (`find_derivation`)
* **Purpose**: Finds the shortest chain of `fold` and `take` operations starting from the axiom `ONE` to derive any target fraction.
* **How it works**: Runs two search frontiers simultaneously—forward from `ONE` and backward from the target using inverse operators. A complexity heuristic $h(x) = \log_2(\text{denominator}(x))$ guides the search, enabling deep derivations to be solved in milliseconds.

### 3. Pure-Python LLL Basis Reduction (`find_integer_relation_lll`)
* **Purpose**: Discovers linear equations and relations ($\sum c_i v_i = c_0$) between multiple derived constants.
* **How it works**: Implements the Gram-Schmidt orthogonalization and Lenstra-Lenstra-Lovász (LLL) basis reduction algorithm in pure Python, bypassing the AST ban on libraries like `numpy` or `scipy`.

### 4. AST-Compliant Code Generator (`generate_sftoe_code`)
* **Purpose**: Serializes a derivation tree into runnable Python code.
* **How it works**: Replaces forbidden syntactic tokens (like literal `0` and bare subtraction `-`) with compliant SFTOE primitives (e.g. `one_val - one_val` and `take(a, b)`), ensuring the code passes the compiler gate in `gate.py` and the mathematical verification in `proof.py`.

---

## Basic API Usage

You can run queries programmatically from any python environment:

```python
from sftoe.discovery import query, find_integer_relation_lll
from fractions import Fraction

# 1. Query by uncertainty interval
result = query(interval=(0.15, 0.18))
print("simplest fraction:", result["fraction"])
print("AST-compliant code:\n", result["code"])

# 2. Find relations between constants
vals = [Fraction(1, 6), Fraction(1, 2), Fraction(5, 6)]
relation = find_integer_relation_lll(vals)
print("Relation found:", relation)
```
