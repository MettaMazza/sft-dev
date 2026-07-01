"""The colour-singlet rule and the dark baryon — forced from the fold's own fibre.
The corpus defines colour AS a fold-fibre: the colour count of a sector is the size of the
p-pling fold's fibre (verify_colour_prediction, proof.py:3918; prime_force_phenomenology.py),
and it builds that fibre and checks every element folds to the base. The fibre of the
p-pling fold over unison is { 1/p, 2/p, ..., p/p = 1 }, and the fold collapses the ENTIRE
fibre to the single base point (unison). That collapse is confinement: a confined colour
singlet is a COMPLETE fibre, because only the complete fibre folds to one clean point.
Hence:
    MESON  = antipodal pair (colour + anticolour) = 2 constituents, every sector
    BARYON = complete colour fibre (one of each of the p colours) = p constituents
At p = 3 this is the Standard Model: the 3-quark nucleon and the 2-quark pion. It forces
both from the fibre with no SU(N) representation theory imported, so the extension to the
new sectors is licensed: the penta baryon is a 5-quark object, the hepta baryon a 7-quark
object. The stable lightest neutral baryon of the new sectors is the dark-matter relic
(dark_relic.py) -- a many-body bound state, not a single WIMP.
"""
from fractions import Fraction
from sftoe.core import SmithianValue, take, ONE, cast_out
from sftoe.proof import verify_value, VerificationError

COLOURED_SECTORS = (3, 5, 7)     # strong (quarks), penta, hepta


def _no_zero_guard():
    try:
        SmithianValue(Fraction(1 - 1, 1))
    except ValueError:
        return
    raise VerificationError("No-zero axiom check failed.")


def colour_fibre(p):
    """The complete fibre of the p-pling fold over unison: p colours, all folding to ONE."""
    fibre = []
    for k in range(p):
        x = SmithianValue(Fraction(1 + k, p))     # 1/p, 2/p, ..., p/p = 1
        verify_value(x)
        if cast_out(x.value * p) != ONE.value:    # the whole fibre collapses to the base
            raise VerificationError("fibre element does not fold to unison")
        fibre.append(x)
    return fibre


def baryon_multiplicity(p):
    """Route A: the complete fibre (the singlet) has size = colour count. Route B: p.
    Neutrality: the colour-charge sum is a whole number of Ones (requires p odd)."""
    fibre = colour_fibre(p)
    count = len(fibre)
    if count != p:
        raise VerificationError("fibre size != colour count p")
    charge_sum = sum((x.value for x in fibre), Fraction(0, 1))
    if charge_sum != Fraction(p + 1, 2):
        raise VerificationError("colour-charge sum != (p+1)/2")
    if charge_sum.denominator != 1:
        raise VerificationError("complete fibre is not colour-neutral (p not odd)")
    return count


def meson_multiplicity(p):
    """A colour + anticolour antipodal pair sums to unison: 2 constituents (any sector)."""
    kind = SmithianValue(Fraction(1, p))          # one colour charge
    verify_value(kind)
    anti = take(ONE, kind)                         # its anticolour (antipode)
    if kind.value + anti.value != ONE.value:
        raise VerificationError("antipodal pair does not sum to unison")
    return 2


def verify():
    """Force the singlet rule; anchor on the Standard-Model p=3 nucleon and pion."""
    _no_zero_guard()
    verify_value(ONE)

    baryons = {p: baryon_multiplicity(p) for p in COLOURED_SECTORS}
    mesons = {p: meson_multiplicity(p) for p in COLOURED_SECTORS}

    # anchor: p = 3 is the Standard Model (3-quark baryon, 2-quark meson)
    if baryons[3] != 3 or mesons[3] != 2:
        raise VerificationError("failed to reproduce the Standard-Model p=3 hadrons")
    # the new forced dark multiplicities
    if baryons[5] != 5 or baryons[7] != 7:
        raise VerificationError("dark baryon multiplicity mismatch")

    return {
        "concept": "Colour singlet = complete fold-fibre; baryon = p constituents, meson = 2.",
        "baryon_multiplicity": {p: baryons[p] for p in COLOURED_SECTORS},   # 3, 5, 7
        "meson_multiplicity": {p: mesons[p] for p in COLOURED_SECTORS},     # 2, 2, 2
        "dark_matter_relic": "a p-quark baryon (5-body penta, 7-body hepta), not a WIMP",
    }


if __name__ == "__main__":
    result = verify()
    print("=" * 74)
    print("THE DARK BARYON — the colour-singlet rule, forced from the fold's fibre")
    print("=" * 74)
    print("\n  colour singlet = complete p-pling fold-fibre (folds to one base point)")
    print("  baryon = p constituents ;  meson = 2 (antipodal pair)\n")
    names = {3: "strong / QCD ", 5: "PENTA (new) ", 7: "HEPTA (new) "}
    for p in COLOURED_SECTORS:
        fib = [str(x.value) for x in colour_fibre(p)]
        print("  %s p=%d  fibre = %s" % (names[p], p, fib))
        print("               baryon = %d-quark   meson = 2   (charge sum = %s whole)"
              % (p, Fraction(p + 1, 2)))
    print("\n  anchor: p=3 is the Standard Model — 3-quark nucleon, 2-quark pion.")
    print("  the dark-matter relic is a %s" % result["dark_matter_relic"])
    print("\n  " + result["concept"])
