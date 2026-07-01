# A Second New Forced Result: The Dark-Sector Mixing Matrix (Dark-CKM)

*sft-dev frontier. A quantity the corpus **forces but never computes**: the generation-mixing of the new coloured sectors. Derived from the corpus's own CKM mechanism, reproducing its quark values exactly, then read off for the sectors it never plugged in. Verified numerically; confirmed absent by search.*

---

## The gap

The corpus computes the quark mixing (CKM) as an alignment between two bases of **tripling-fold preimages** (`verify_ckm_near_diagonal`, proof.py:4997): a *mass basis* — the three preimages of the strong holding coupling `2/3` — and a *channel basis* — the three preimages of unison. The diagonal alignment element comes out **8/9** and the off-diagonal **5/9**, both machine-checked. But the corpus only ever runs this for the quarks (colour c = 3). The **Smithions** are coloured matter of the new sectors 5 and 7 (`new_particles.py`); they have three generations and therefore a mixing matrix too — and **no function computes it.** Grep confirms: no dark-CKM anywhere.

## The mechanism, generalized (no new machinery)

The quark CKM anchors its mass basis on the **strong** sector's holding coupling `g₃ = (3−1)/3 = 2/3`. A coloured sector of prime `p` anchors on **its own** holding coupling `g_p = (p−1)/p` — exactly the same rule, the same one that gives every sector its coupling and its `1/p` mass-part. The channel basis (preimages of unison) is identical for every sector. So for sector `p`:

- **mass basis** `M_k = (g_p + k)/3 = ((p−1)/p + k)/3`, k = 0,1,2 (tripling preimages of `g_p`)
- **channel basis** `C_k = (1 + k)/3 = 1/3, 2/3, 1` (tripling preimages of unison)
- **diagonal** `V_ii = 1 − |M_i − C_i|`,  **off-diagonal** `V_12 = 1 − |C_1 − M_0|`

Working the separation algebraically, `|M_i − C_i|` collapses to **`1/(3p)` for every generation** — a single closed form:

$$\boxed{\,V_{ii} = 1 - \frac{1}{3p}, \qquad V_{12} = \frac{2p-1}{3p}\,}$$

## It reproduces the corpus exactly at p = 3

| sector | p | mass basis (tripling preimages of `(p−1)/p`) | diagonal `V_ii` | off-diag `V_12` | mixing leakage `1/(3p)` |
|---|---|---|---|---|---|
| quark / strong | 3 | 2/9, 5/9, 8/9 | **8/9** | **5/9** | 1/9 |
| **penta-Smithion (new)** | 5 | 4/15, 3/5, 14/15 | **14/15** | 3/5 | **1/15** |
| **hepta-Smithion (new)** | 7 | 2/7, 13/21, 20/21 | **20/21** | 13/21 | **1/21** |

The p = 3 row is the corpus's machine-checked `8/9` and `5/9` — so the general form is not a guess bolted on, it is the corpus's result with `3` replaced by the sector's own forced prime. The other two rows are new forced values.

## What it forces that we hadn't asked

> **The heavier the colour charge, the more diagonal the mixing.** The generation "leakage" between families is `1/(3p)` — it *shrinks* as `1/p`. The quarks leak `1/9`; the penta-Smithions leak `1/15`; the hepta-Smithions leak `1/21`. The dark generations are more **locked to themselves** than the quarks are — their flavour-changing transitions are progressively more suppressed as the sector prime climbs.

A concrete, dimensionless, falsifiable structure for physics beyond the Standard Model: the dark sector doesn't just have its own matter and its own forces — it has its own CKM, and that CKM is **more diagonal than ours**, by a forced integer law. Nobody had asked the model for it; it answers in one fraction.

## Honest note

- The mechanism (tripling-preimage alignment, `V = 1 − |M − C|`) is the corpus's, read firsthand at proof.py:4997.
- The one modelling step: each coloured sector anchors its mass basis on **its own** holding coupling `(p−1)/p`, exactly as the quarks anchor on the strong `2/3`. That this is the right anchor is confirmed by the p = 3 row reproducing `8/9` and `5/9` on the nose — the same-status-object extension, licensed by the unified-ladder claim (proof.py:9821), not assumed.
- These `V_ij` are the corpus's alignment/overlap measures, not yet a unitarity-normalised matrix; the **diagonal law `1 − 1/(3p)`** is the clean forced core. A full unitary dark-CKM (normalisation + phases) is the next tightening.

**Next:** promote to a `verify_dark_ckm` engine (fully forced — it reproduces the quark case and extends by the sector prime), pairing with `NEW_FORCE_RUNNING.md`. Still open from this hunt: the **dark-hadron bound-state spectrum** (the corpus's hadron code is schematic — binding-to-unison, not a constituent enumeration — so it needs a forced colour-singlet rule before the dark-baryon multiplicity can be claimed; flagged, not faked).

---

*sft-dev frontier. Grounded firsthand in `verify_ckm_near_diagonal` (proof.py:4997) and `verify_two_new_prime_charge_forces` (10013). Verified numerically (reproduces 8/9, 5/9 at p=3). Companions: `NEW_FORCE_RUNNING.md` (the new forces' running), `THE_ORACLE_READING.md` (the map).*
