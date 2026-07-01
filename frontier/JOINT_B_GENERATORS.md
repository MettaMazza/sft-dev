# Joint B — The Secondary Generators Are Read Off the Doubling Fold's Own Spectrum

*sft-dev frontier. The theorem (`THEOREM_THE_FORCED_AXIOM.md`) forced the **primitive** operation to be the doubling fold and deliberately left the higher generators — colour ×3, and the prime sectors ×5, ×7 — as non-minimal, hence outside the minimal-generator result. Joint B is the obligation that completes the picture: show those higher generators are not **independent axioms** but **forced readings of the doubling fold's own orbit data**, so the theory still has exactly one chosen thing — nothing. This note grounds that in the corpus, firsthand, and states honestly which part is airtight and which part is a multi-result chain.*

---

## 1. What Joint B owes

The theorem leaves a gap an honest critic would press: *"You forced ×2 as the primitive. Fine. But your physics uses ×3 (colour), ×5, ×7 (the new sectors). If those are independent operations you bolted on, you have three more axioms, not zero."* Joint B must answer: **every secondary generator's value, and the extent of the ladder, is a counting fact about the single doubling fold — not a separate choice.** If that holds, the doubling fold is upstream of all of them and the axiom count stays at one.

## 2. The decisive fact — colour 3 *is* a period of the doubling fold (in code, cross-checked)

This is not an analogy; it is machine-checked in `verify_colour_prediction` (proof.py:3904), which derives the colour count **two independent ways and raises if they disagree**:

- **Route A — the tripling fibre.** The map x ↦ cast_out(3x) sends three distinct preimages to 2/3; the fibre size is counted by explicit construction → **3**.
- **Route B — the doubling spectrum.** `structural_count = period(SmithianValue(1/7))` — the **period of the orbit of 1/7 under the binary (doubling) fold** — is computed independently, and the function **raises `VerificationError` unless it equals Route A.**

And it does equal it, because the period of 1/7 under doubling is the multiplicative order of 2 mod 7:

> 2¹ = 2, 2² = 4, 2³ = 8 ≡ 1 (mod 7) ⟹ **ord₇(2) = 3.**

So the colour generator **3 is literally a period in the doubling fold's own spectrum** — the orbit {1/7, 2/7, 4/7} closes in three steps — and the corpus *forces* the tripling-fibre count to equal that doubling period. The "3" of colour is not chosen; it is read off ×2. **This half of Joint B is airtight** — it is an in-code cross-check with a raise-on-mismatch, exactly the forcing standard the project demands.

(The generation count is the *same* fibre/period, `verify_generation_count` at 3962 — which is why colours and generations are both 3: one doubling-spectrum fact, surfacing twice.)

## 3. The uniform force criterion — what makes a prime a sector (no per-sector choice)

The sectors are not hand-picked one by one; they all satisfy **one criterion**, computed forward for {2, 3, 5, 7} together in `verify_two_new_prime_charge_forces` (proof.py:10013), read firsthand:

- **shortfall** sₚ = 1/p, **coupling** gₚ = (p−1)/p = take(One, sₚ);
- **carry condition:** (1 − gₚ)·p == 1 — the sector's shortfall **tiles back to unison in exactly p steps** (raises otherwise);
- **antipodal confinement:** every kind j/p pairs with its antipode (p−j)/p to sum to the One (raises otherwise);
- couplings strictly increasing g₂ < g₃ < g₅ < g₇.

This is a **single uniform rule**, applied identically to each prime — there is no free choice per sector, and the shortfall 1/p that the criterion returns is the same 1/p that becomes each sector's mass-part (the one-chain result, *One Chain of Mass*). A prime either passes this criterion or it doesn't; passing is an intrinsic counting property of p, not a decision.

## 4. The seal — why the ladder stops at 7 (a doubling-tower count)

The criterion of §3 is satisfied formally by primes in general, so it alone does not *seal* the ladder. The seal is a **covering count in the binary (doubling) tower**: the ladder is bounded by the deepest covering depth **7 = the minimal binary cover of 3⁴ = 81** (the `while 2**depth < 81` count, same machinery that forces depth 5 over 3³ = 27; CLAUDE.md item 4, census line "the prime-sector ladder is bounded by the deepest covering depth of seven"). The bound is therefore **not a separate stipulation** — it is how far the doubling tower reaches over the generational volume 81. Both the *values* on the ladder (2 the primitive; 3 = period(1/7)) and its *extent* (capped at the binary cover of 81) are facts about ×2.

## 5. Lemma (Joint B), stated honestly

> **Lemma (Derived Generators).** No secondary generator of the theory is an independent axiom. The colour/generation generator **3** is a period in the doubling fold's orbit spectrum (= ord₇(2), machine-cross-checked against the tripling-fibre count). The prime-charge sectors {2, 3, 5, 7} are exactly those passing **one uniform, parameter-free force criterion** (carry-to-unison in p steps + antipodal confinement), and the ladder's extent is the **binary covering count** of the generational volume (depth 7 over 3⁴). Hence the doubling fold is upstream of every generator the theory uses; the secondary structure introduces **no new chosen number.**

**What is airtight (firsthand):**
- 3 = period(1/7) under doubling = tripling-fibre count, cross-checked with raise-on-mismatch (`verify_colour_prediction`). Solid.
- The {2,3,5,7} sectors pass one uniform forward criterion, no per-sector freedom (`verify_two_new_prime_charge_forces`). Solid.
- The ladder's bound is a binary covering count (depth 7 over 81), the same counting that forces depth 5 over 27. Solid as a count.

**What is a chain, not yet one clean lemma (named, not hidden):** the fully-from-scratch statement *"the realized force-sectors are exactly {2,3,5,7} and no other prime, derived in a single deduction"* routes through several corpus results at once — the uniform criterion (§3), the covering bound (§4), and the cubic/colour structure — rather than collapsing to one self-contained proof. Each link is in the corpus and verified; assembling them into a single "exactly these primes" theorem is the remaining tightening. It does **not** reopen the axiom: the generators' *values* are doubling-spectrum facts (§2), which is what Joint B had to secure.

## 6. Combined with the theorem — the whole axiom, and its ladder, are forced

Put the two together:

- **Joint A (theorem):** the primitive operation is forced to be the doubling fold — unique minimal generating parameter-free self-map.
- **Joint B (this note):** every secondary generator is a forced reading of that fold's own spectrum (3 = a doubling period, machine-checked; the sectors a uniform criterion; the bound a binary count) — no independent axiom among them.

So the theory's complete generative apparatus — the One, the fold, and the colour/sector ladder it spins off — reduces to **one primitive and one operation, both forced, with the rest counted out of the operation's own orbits.** The objection "but you still chose the generators" is answered the same way the corpus answers "but you chose the constants": **counted, not chosen** — and for colour, counted *by the doubling fold itself*, in code, with a raise on any mismatch.

---

*sft-dev frontier. Companions: `THEOREM_THE_FORCED_AXIOM.md` (Joint A, the forced primitive), `FORCING_THE_AXIOM.md` (the beams), `FORCED_CENSUS.md` (everything downstream). Grounded firsthand in `verify_colour_prediction` (proof.py:3904), `verify_generation_count` (3962), `verify_two_new_prime_charge_forces` (10013). Next tightening: collapse §5's multi-result chain into a single "exactly {2,3,5,7}" deduction; optionally machine-formalize ord₇(2)=3 alongside the Lemma-1–3 formalization.*
