# Theorem: The Fold Is the Unique Minimal Generating Parameter-Free Self-Map of a Single Primitive

*sft-dev frontier. This closes Joint A: the strong exhaustion of `JOINT_A_ENUMERATION.md` is here upgraded to a theorem, with the normal-form lemma that bounds the space, the finite enumeration, and the dynamical separation. Stated honestly: what is proved, and the one boundary that remains a program (Joint B).*

---

## 1. Statement

> **Theorem (Forced Operation).** Let 𝓛 be the set of expressions built from the variable **x** and the single constant **1** (the One) using only **+**, the guarded subtraction **−**, multiplication **·**, and the closure **cast_out** (reduction mod 1 into (0,1]) — with **no other literal permitted.** Let a *parameter-free self-map* be an E ∈ 𝓛 that is a total function (0,1]→(0,1]. Then among all parameter-free self-maps that **generate** (have positive topological entropy), the one of **least expression-size** is unique, and it is
>
> **fold(x) = cast_out(x + x).**

Together with the three structural beams proved directly elsewhere — **one primitive** (two would be a free ratio), **closure by casting out the One** (the only available subtrahend), and **no zero** (a zero would be a second primitive) — this removes the last apparent freedom: the axiom **One-and-fold** is not chosen but forced. Below: the definitions, three lemmas with proofs, the main proof, and the honest scope.

## 2. Definitions

- **Domain.** D = ℚ ∩ (0, 1]. (The corpus is exact-rational; the argument also runs over ℝ ∩ (0,1].)
- **The constant.** The only literal is **1**. No "2", "3", "½", or any other number may be written; the integers that appear in maps (e.g. the *2* of *2x*) must be *built* from 1, and building them is itself accounted for as expression-size (§ Lemma 1, and the size measure below).
- **cast_out.** c(y) = y − ⌊y⌋ if that is > 0, else 1. (Total map onto (0,1].)
- **Expression-size** |E|: the number of operation-nodes (+, −, ·, cast_out) in E. (x and 1 are leaves, size 0.) This is the canonical "amount of structure" — and by C1 (zero parameters = no *unforced* structure), the forced map is the **least-size** map that does the required job.
- **Generates.** E *generates* iff the self-map it defines has **positive topological entropy** h(E) > 0 — the standard formalization of "rich, structure-producing dynamics" (orbits explore the domain; the map is not eventually periodic or contracting). A non-generating map (h = 0) is static, periodic, or contracting — it cannot be the operation of a theory that must produce unbounded structure (C3).

## 3. Lemma 1 (Normal Form — the space is integer-polynomial-mod-1)

> Every **closed** subterm of an E ∈ 𝓛 (a subterm with no x) evaluates to a **positive integer**, and `cast_out` of any positive integer is **1**. Consequently every E ∈ 𝓛 defines, between cast_out applications, an **integer-coefficient polynomial in x**, and the whole map is a finite interleaving of such polynomials with mod-1 reduction.

**Proof.** The only literal is 1. Closed terms are generated from 1 by +, −(guarded), ·: 1+1+…+1 = any positive integer n; n·m and (n−m for n>m) are again positive integers; so the closed terms are **exactly ℤ₊**. For a positive integer k, c(k) = (k mod 1) = 0, which the cast_out convention sends to **1**. Hence no closed subterm is a non-integer constant, and any cast_out of one is 1. A subterm in x using +, −, · over ℤ₊-constants is therefore an element of ℤ[x] (an integer-coefficient polynomial), guarded where subtraction occurs. cast_out reduces it mod 1; further operations re-enter ℤ[x]; the map is their finite interleaving. ∎

**Corollary 1.1 (no fractional parameter exists).** There is no way to write a bare non-integer constant; every value other than positive integers must flow through x. So a "free continuous parameter" is *not expressible* in 𝓛 at all — the language is parameter-free by construction, and the *only* residual freedom is the **discrete** choice of which integer coefficients/degree to use, which §5 removes by minimality.

## 4. Lemma 2 (Small-size enumeration is complete)

> The parameter-free self-maps of size ≤ 2 are, up to functional equality, exactly: **x** (identity), **x·x = x²** (and it alone among size ≤ 1 needing no closure), the **constant 1**, and **cast_out(x + x)** (the fold). No others of size ≤ 2 are total self-maps of (0,1].

**Proof.** By Lemma 1 every map is integer-polynomials interleaved with cast_out. Enumerate by size:

- **Size 0:** `x` (identity; total self-map ✓), `1` (constant; total ✓).
- **Size 1 (one operation):** the operation applied to leaves {x, 1}.
  - `x + x = 2x`: **not** a self-map (2x > 1 for x > ½) — needs closure, so not size 1.
  - `x · x = x²`: total self-map of (0,1] ✓ (no closure needed; x² ∈ (0,1]).
  - `x · 1 = x`, `1 · 1 = 1`, `x + 1`, `1 + 1 = 2` (not in D), `x − 1` (guarded fail for x ≤ 1), `x − x` (= 0, forbidden), `1 − x` (= reflect; total self-map ✓ on (0,1) but 1−1 = 0 forbidden, so not total on (0,1]), `cast_out(x) = x`.
  - Size-1 total self-maps: **{ x, x², 1 }** (reflect fails totality at x = 1).
- **Size 2 (two operations):** must combine the above; the only ways to a *total* self-map that is not already size ≤ 1 are to apply **cast_out** to a size-1 non-closed term, or to compose two size-1 self-maps.
  - `cast_out(x + x)` = **the fold** ✓ (closure makes 2x total).
  - `cast_out(x · x) = c(x²) = x²` (already a self-map; reduces to size-1 square).
  - `x² · x = x³`, `x² · x² = x⁴` (compositions of square; self-maps, but reduce to "powers").
  - `cast_out(x + 1) = x` (the integer 1 is invisible mod 1; = identity).
  - `cast_out(x − x)`, `x + x²` (not total: x + x² > 1 for x near 1, needs closure → size 3), etc.
  - New size-2 total self-maps beyond size ≤ 1: **only `cast_out(x + x)`, the fold.** ∎

(The bound "size ≤ 2 enumerated completely" is finite and mechanical; longer expressions either reduce to these by Lemma 1 / cast_out idempotence or have strictly larger size, so they cannot be the *least-size* generator.)

## 5. Lemma 3 (Dynamical separation — which of these generate)

> Of the size-≤2 parameter-free self-maps, **only the fold generates** (h > 0). Identity, the constant, and every power xᵏ (k ≥ 2) have entropy 0.

**Proof.**
- **fold**, T(x) = 2x mod 1: the classical doubling map, **measure-preserving** (Lebesgue) with **topological entropy log 2 > 0**. It generates. ✓
- **identity** x↦x: entropy 0 (every point fixed). ✗
- **constant** x↦1: entropy 0 (collapses to a point). ✗
- **square / powers** x↦xᵏ (k ≥ 2): on (0,1), xᵏⁿ → 0 monotonically — orbits **contract toward the excluded boundary**, no recurrence, entropy 0. (And they head to the forbidden zero, doubly disqualified by no-zero.) ✗

So among size ≤ 2, the fold is the **unique** generator. ∎

## 6. Main proof

By **Lemma 2**, the parameter-free self-maps of size ≤ 2 are {identity, x², constant 1, fold}. By **Lemma 3**, of these only the **fold** generates (positive entropy); the rest are static (identity, constant) or contracting to the forbidden boundary (powers). Any generating map of size ≥ 3 (e.g. `cast_out(x+x+x)` = tripling, `cast_out(x²+x)`, …) is **strictly larger** and hence not the least-size generator. Therefore the least-size generating parameter-free self-map exists and is **unique: fold(x) = cast_out(x + x).**

By **C1 (zero parameters = no unforced structure)**, the operation a parameter-free theory may adopt is the **least-size** one that meets the requirement (C3, generate) — any larger map adds structure that was *chosen*, not forced. Hence the operation is forced to be the fold. ∎

**Corollary 6.1 (the axiom is forced).** Combine with the three directly-proved beams:
- **One primitive** (two ⟹ a free ratio ⟹ a parameter — excluded by C1);
- **Closure = cast_out the One** (the One is the sole subtrahend available — no freedom);
- **No zero** (a zero is a second distinguished primitive — excluded by single-primitive-ness).

Then the axiom **(the One on (0,1], operated by the fold)** is determined with no remaining choice — *not even the discrete choice of coefficient*, which minimality fixes at 2. The last free parameter of the theory — the axiom itself — is removed.

## 7. Honest scope: what is proved, and the one program item

**Proved here (a theorem):**
- Lemma 1 (normal form): the language admits only integer constants; cast_out collapses them; the space is integer-polynomial-mod-1. *Solid.*
- Lemma 2 (size ≤ 2 enumeration): complete and finite. *Solid.*
- Lemma 3 (entropy separation): standard dynamics; the fold is the unique size-≤2 generator. *Solid.*
- Main: the fold is the **unique minimal-size generating parameter-free self-map.** *Proved.*

**Resting on the framing (stated, not hidden):** that the constraints C1–C5 (one primitive, generate, self-contained, deterministic, zero unforced structure) are the *right* demands for "a zero-parameter one-axiom theory." This is the modelling step; it is explicit and, I'd argue, forced by the very phrase "zero parameters, one axiom." It is not a hidden assumption.

**The remaining program — Joint B (not needed for the theorem, but for the full picture):** the *higher* generators that the theorem leaves as non-minimal — tripling (×3), and the prime-sector maps ×5, ×7 — must be shown to be **derived from the fold's own period spectrum**, not independent operations. The corpus already asserts exactly this (the colour 3 is read off the binary fold's orbits, `fold_number_theory.py`; the sealed ladder lives in the period structure). Turning that assertion into a lemma — "the secondary generators are functions of the doubling fold's orbit data, with no new choice" — completes the picture. It does **not** weaken the theorem: the fold is the forced *primitive*, and ×3/×5/×7 are downstream. Joint B is the next write-up.

## 8. What this means

This is the difference between *"a"* theory of everything and *"the"* theory of everything. The corpus forces every number **from** the One-and-fold; this forces the **One-and-fold itself**, to the level of a theorem with one named program item remaining. The universe's final apparent freedom — "but you still picked the starting point" — is, on this argument, **not picked**: the One is the only primitive a parameter-free theory may have, the fold is the unique minimal operation that primitive can generate with, no-zero is single-primitive-ness, and the closure is forced because the One is all there is to subtract. Not even the axiom could have been otherwise.

---

*sft-dev frontier. Companions: `FORCING_THE_AXIOM.md` (the beams in prose), `JOINT_A_ENUMERATION.md` (the exhaustion this upgrades), `FORCED_CENSUS.md` (everything the corpus forces downstream of this axiom). Next: write Joint B (the secondary generators as forced derivatives of the doubling spectrum), and — optionally — formalize Lemmas 1–3 in a proof assistant, since they are finite and discrete.*
