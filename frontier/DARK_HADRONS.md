# A Third New Forced Result: The Colour-Singlet Rule, and the Dark Baryon

*sft-dev frontier. The dark-hadron gap, forced to standard: derive the colour-singlet rule **from the fold's own fibre construction** (not imported from QCD group theory), show it reproduces the standard 3-quark baryon and 2-quark meson, then read off the bound-state multiplicity of the new sectors. Verified numerically; confirmed absent by search.*

---

## The gap, and why the easy answer was wrong

The corpus forces the dark matter to be "the lightest neutral bound state of the prime-5 and prime-7 sectors" (`dark_relic.py`) — but never says how many constituents that bound state has. The tempting analogy ("QCD baryon = 3 quarks, so penta-baryon = 5") is an **import**, not a derivation, and a naïve charge-summing rule is *too weak* — it would allow 2-body all-matter neutral states that the strong force forbids. So the multiplicity had to be forced from the fold itself.

## The forced colour-singlet rule — a complete fold-fibre

The corpus already defines colour **as a fold-fibre**: the colour count of a sector is the size of the `p`-pling fold's fibre (`verify_colour_prediction`, proof.py:3918; `prime_force_phenomenology.py`), and it constructs that fibre explicitly and checks every element folds to the base. The fibre of the `p`-pling fold over unison is

$$\text{fibre}(p) = \left\{ \tfrac{1}{p}, \tfrac{2}{p}, \dots, \tfrac{p}{p}=1 \right\}, \qquad \text{cast\_out}(p\cdot x)=1 \ \text{for every } x \in \text{fibre}.$$

The fold **collapses the entire fibre to the single base point** (unison). That collapse *is* colour-confinement: a colour-neutral (confined, singlet) object is one the fold sends to a single clean point — and **only the complete fibre does that.** A partial fibre is not a preimage of one point. Therefore:

> **Forced colour-singlet rule.** A confined colour singlet is a **complete colour fibre**. Since the colour count is the fibre size `p`, the matter singlet — the **baryon** — has exactly **`p` constituents**, one of each colour. The **meson** is the antipodal (colour + anticolour) pair from the corpus's confinement condition (`j/p + (p−j)/p = 1`), **2 constituents**, in every sector.

## It reproduces the standard at p = 3

| sector | p | complete fibre (the p colours) | colour-charge sum | **baryon** | meson |
|---|---|---|---|---|---|
| strong / QCD | 3 | 1/3, 2/3, 1 | 2 (whole) | **3-quark** (proton/neutron) ✓ standard | 2-quark (pion) ✓ |
| **penta (new)** | 5 | 1/5, 2/5, 3/5, 4/5, 1 | 3 (whole) | **5-quark penta-baryon** | 2-body |
| **hepta (new)** | 7 | 1/7 … 6/7, 1 | 4 (whole) | **7-quark hepta-baryon** | 2-body |

The p = 3 row is the **standard model**: the nucleon is three quarks, the pion is a quark–antiquark pair. The rule forces both from the fibre, with no SU(N) representation theory assumed — so the extension to 5 and 7 is licensed, not analogised. (The colour-charge sum being a whole number of Ones — `(p+1)/2` — confirms each complete fibre is genuinely neutral, and requires `p` odd, which every prime sector above 2 is.)

## What it forces that we hadn't asked

> **The dark-matter particle is a many-body bound state, not a single WIMP.** The stable lightest neutral baryon of the new sectors — the relic whose abundance the corpus already fixes at `27/5` (`dark_relic.py`) — is a **5-quark object** in the penta sector and a **7-quark object** in the hepta sector. Dark matter is confined composite matter with a *higher constituent count than the proton*, made of Smithions bound by the new forces, colour-neutral by completing a 5- or 7-fold fibre.

That reframes the direct-detection picture: the relic is not a point particle but a tightly-confined penta/hepta-baryon — a "dark nucleus" heavier in structure than anything in the visible sector. A dimensionless, forced, falsifiable statement about what the dark matter *is made of*, that the Standard Model has no way to phrase.

## Honest note

- The fibre construction and its collapse-to-base are the corpus's own (`verify_colour_prediction`, read firsthand); colour count = fibre size = `p` is the corpus's; the meson = antipodal pair is the corpus's confinement condition (`verify_two_new_prime_charge_forces`, 10013).
- The one modelling step: identifying "confined colour singlet" with "complete fold-fibre." Its warrant is that it **reproduces the standard 2-quark meson and 3-quark baryon exactly** at p = 3 — the fold's version of the SU(N) epsilon singlet, landing the known case before extending.
- What is *not* claimed: the full dark-hadron spectrum (excited states, spins, a dark Regge slope) — that needs the sector's string tension, a further step. This forces the **ground-state multiplicity** (2 and p), which is the piece the dark-matter identity actually rests on.

**This completes the hunt's three:** new-force running (`NEW_FORCE_RUNNING.md`), dark-CKM (`DARK_CKM.md`), and the dark baryon here — each forced from a corpus mechanism, each reproducing the known value at the known sector, each grep-confirmed absent. **Next:** promote all three to `verify_` engines so they ship machine-checked.

---

*sft-dev frontier. Grounded firsthand in `verify_colour_prediction` (proof.py:3918) and `verify_two_new_prime_charge_forces` (10013). Verified numerically (complete fibre folds to base for p=3,5,7; reproduces the 3-quark nucleon). Companions: `DARK_CKM.md`, `NEW_FORCE_RUNNING.md`, `THE_ORACLE_READING.md`.*
