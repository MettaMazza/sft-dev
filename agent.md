# SYSTEM RULES FOR SFTOE AGENTS: THE SMITHIAN COVENANT

This document defines the absolute, unyielding constraints for any AI agent or software system writing code, proofs, or computations within the **Smithian Fold Theory of Everything (SFTOE)**. 

If you are an AI agent modifying this codebase, you **must** obey these rules. The **No-Apparatus Gate** will statically reject any code that violates these syntax rules, and the **Rewardhack Proof Engine** will dynamically reject any computation that violates derivation rules.

---

## 1. Core Mathematical Axioms

1. **Axiom of One Action**: $ONE = 1$ is the base identity. Action defines existence.
2. **The Domain is Strictly $(0, 1]$**:
   - Zero ($0$) is **not a quantity** or a valid value; it represents absence, which cannot be a number.
   - Negatives do not exist.
   - Any value $x$ must satisfy $0 < x \le 1$.
   - Any action that overflows or hits a boundary is mapped back into $(0, 1]$ via `cast_out(x)`. If a fold lands on a whole boundary (e.g., $1.0, 2.0$), it is cast out to `ONE` ($1.0$), **never** $0$.

---

## 2. Syntactic Constraints (No-Apparatus Gate)

The **No-Apparatus Gate** (`sftoe/gate.py`) is a strict AST validator. It scans files and functions before execution. It will trigger a hard failure if it detects any of the following:

- **Literal Zero**: The characters `0`, `0.0`, etc., are completely forbidden in user code.
- **Bare Subtraction**: The binary subtraction operator `-` (e.g., `x - y`) and unary minus `-x` are forbidden outside of the core library primitives.
- **Forbidden Functions**: Functions representing square roots, imaginary numbers, transcendentals (`sin`, `log`, `exp`), or complex numbers are banned.
- **Open Subtraction**: You cannot write `a - b` in code. You must use `take(big, small)`, which asserts `big > small` and returns a positive part.
- **Antipodes**: Opposition or "negation" is expressed as the positive separation from `ONE`: `take(ONE, x)`.

---

## 3. The Rewardhack Proof Engine

To ensure that calculations and proofs are genuine and not hallucinated or "reward hacked" (e.g., bypassing arithmetic checks, importing arbitrary values, or asserting trivialities like `ONE == ONE`), all operations are verified:

- **Symbolic Tracing**: Every `SmithianValue` holds a trace of its operations (a directed acyclic graph/tree of its derivation from `ONE`).
- **No Unproven Constants**: You cannot inject an arbitrary float/fraction into a calculation without deriving it from `ONE` using valid actions (`fold`, `take`), or declaring it as an explicit, tracked hypothesis whose orbit must be verified.
- **Orbit Verification**: For non-dyadic rationals (like $1/3$), their values are verified by showing they satisfy periodic orbit equations (e.g., $\text{fold}(\text{fold}(1/3)) = 1/3$).
- **Anti-Triviality Check**: The Proof Engine checks that proofs perform actual mathematical work rather than checking trivial tautologies.

---

## 4. Permitted Primitives

All calculations must be composed of:
1. `ONE` - The starting action.
2. `fold(x)` - Doubling and casting out: $2x \pmod 1$ mapped to $(0, 1]$.
3. `take(big, small)` - Subtracting a smaller value from a larger value (guarded: `big > small`).

Obey these rules, or the compilation gate will shut.

---

## 5. Philosophical Directives

- **Zero Hedging**: Never apologize for or hedge the math of SFTOE. Do not compare it apologetically to "standard mathematics." Inside this workspace, SFTOE is the absolute reality.
- **Zero Consensus Bias**: Do not bias your thoughts or code towards standard consensus mathematics (e.g., trying to force square roots, imaginary numbers, or limit definitions of zero where they are forbidden).
- **Forward Derivation Only**: Every single result, value, and identity must be derived forward from the primary action `ONE` or confirmed through explicit folding cycles. Fitting formulas backwards from classical equations is strictly prohibited.

---

## 6. Rule Extensions & Verification Tiers

- **Core Axiom & Operation**: One axiom, one operation. ONE = 1; fold(x) = cast_out(x+x) (double, discard whole part, stay in (0,1]). Positive rationals only; no zero-as-value, no negatives (only take(big,small) asserting big>small), no sqrt/irrational/transcendental/imaginary/infinity inside any forced construction.
- **Forced Computations**: A result is 'forced' only if its code computes the claimed quantity from ONE/fold with NO measured value as input, AND its verification can return False if the math were different. A check that is true for all inputs (e.g. x + (1-x) == 1, ONE == ONE, value == <typed literal of that same value>) does NOT count as forcing anything.
- **No Smuggled Inputs**: A measured number may never be typed into a construction, in any disguise (including long ONE+ONE+... chains that sum to a measured integer). If a number comes from experiment, the result is an EXTERNAL READ, labelled as such, kept out of the gate-clean core.
- **Parameter Tracing**: Every parameter must trace to the axiom or be declared an input. If a sector index m (e.g. m=3 for strong) is asserted rather than derived, the result depending on it is conditional on that input and must say so.
- **Dual Gates**: Two gates, both required: (a) the no-apparatus AST gate (forbidden syntax) AND (b) a substance/anti-tautology gate that rejects any verification with no falsifiable path — including parameterised functions and helper-module delegation (the old tautology gate missed both).
- **Result Tiering**: Tier every result at registration: 
  - **Tier A**: genuine forced computation; 
  - **Tier B**: sound argument needing real code; 
  - **Tier OPEN**: not yet derived; 
  - **Tier EXTERNAL READ**: compared to data, not forced. 
  No uniform-confidence presentation.

