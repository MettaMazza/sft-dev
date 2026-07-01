"""The dark-sector mixing matrix (dark-CKM) — forced from the corpus's own CKM mechanism.
The corpus computes quark mixing (verify_ckm_near_diagonal, proof.py:4997) as an alignment
of two bases of tripling-fold preimages: a MASS basis (the three preimages of the strong
holding coupling 2/3) and a CHANNEL basis (the three preimages of unison), with
        diagonal  V_ii = 1 - |M_i - C_i| = 8/9 ,   off-diagonal V_12 = 5/9 .
It runs this only for the quarks (colour c = 3). A coloured sector of prime p anchors its
mass basis on ITS OWN holding coupling g_p = (p-1)/p (exactly as the quarks anchor on the
strong 2/3). The generation-mixing then follows the identical rule, and the separation
collapses to the single closed form
        |M_i - C_i| = 1/(3p)   =>   V_ii = 1 - 1/(3p) ,   V_12 = (2p-1)/(3p) .
At p = 3 this reproduces the corpus's 8/9 and 5/9 exactly; at p = 5, 7 it gives the
NEW dark mixings 14/15 and 20/21. The generation "leakage" 1/(3p) shrinks as 1/p:
the heavier the colour charge, the more diagonal the mixing.
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


def _tripling_preimages(base):
    """The three generation positions: preimages of `base` under the tripling fold.
    Each x_k = (base + k)/3 satisfies cast_out(3 * x_k) == base (verified)."""
    pre = []
    for k in range(3):
        x = SmithianValue(Fraction(base + k, 3))
        verify_value(x)
        if cast_out(x.value * 3) != base:
            raise VerificationError("tripling preimage does not fold to base")
        pre.append(x)
    return pre


def forced_ckm(p):
    """Route A: build the mass/channel bases and align them. Route B: the closed form.
    Raise on any mismatch. Returns (diagonal V_ii, off-diagonal V_12)."""
    g_p = Fraction(p - 1, p)                       # sector holding coupling
    mass = _tripling_preimages(g_p)                # preimages of (p-1)/p
    channel = _tripling_preimages(Fraction(1, 1))  # preimages of unison: 1/3, 2/3, 1

    # diagonal: V_ii = 1 - |C_i - M_i|  (channel_i > mass_i, so take is guarded)
    diag = None
    for i in range(3):
        if not channel[i].value > mass[i].value:
            raise VerificationError("expected channel_i > mass_i for the diagonal")
        sep = take(channel[i], mass[i])            # |C_i - M_i|, forced subtraction
        v_ii = take(ONE, sep).value                # 1 - separation
        if diag is None:
            diag = v_ii
        elif v_ii != diag:
            raise VerificationError("diagonal alignment is not symmetric across generations")

    # off-diagonal: V_12 = 1 - |C_1 - M_0|
    sep12 = take(channel[1], mass[0])
    v12 = take(ONE, sep12).value

    # Route B closed forms (reproduce corpus 8/9, 5/9 at p=3)
    if diag != Fraction(3 * p - 1, 3 * p):
        raise VerificationError("diagonal != 1 - 1/(3p) at p=%d: %s" % (p, diag))
    if v12 != Fraction(2 * p - 1, 3 * p):
        raise VerificationError("off-diagonal != (2p-1)/(3p) at p=%d: %s" % (p, v12))
    if not diag > v12:
        raise VerificationError("near-diagonal check failed: need V_ii > V_12")
    return diag, v12


def verify():
    """Force the dark-CKM for all coloured sectors; anchor on the corpus quark values."""
    _no_zero_guard()
    verify_value(ONE)

    results = {}
    for p in COLOURED_SECTORS:
        diag, v12 = forced_ckm(p)
        results[p] = (diag, v12)

    # anchor: p = 3 must reproduce the corpus's machine-checked 8/9 and 5/9
    if results[3] != (Fraction(8, 9), Fraction(5, 9)):
        raise VerificationError("failed to reproduce corpus CKM 8/9, 5/9")
    # the new forced dark values
    if results[5][0] != Fraction(14, 15) or results[7][0] != Fraction(20, 21):
        raise VerificationError("dark-CKM diagonal mismatch")

    return {
        "concept": "Dark-CKM diagonal V_ii = 1 - 1/(3p): quark 8/9, penta 14/15, hepta 20/21.",
        "quark_p3": [str(results[3][0]), str(results[3][1])],
        "penta_p5": [str(results[5][0]), str(results[5][1])],
        "hepta_p7": [str(results[7][0]), str(results[7][1])],
        "leakage_shrinks_as": "1/(3p)",
    }


if __name__ == "__main__":
    result = verify()
    print("=" * 74)
    print("THE DARK-CKM — the new sectors' generation mixing (forced)")
    print("=" * 74)
    print("\n  mechanism (corpus): align tripling-preimages of the holding coupling (p-1)/p")
    print("  forced diagonal:  V_ii = 1 - 1/(3p)   ;   leakage = 1/(3p)\n")
    print("  sector        p   diagonal V_ii   off-diag V_12   leakage")
    names = {3: "quark/strong", 5: "PENTA (new) ", 7: "HEPTA (new) "}
    for p in COLOURED_SECTORS:
        diag = Fraction(3 * p - 1, 3 * p)
        v12 = Fraction(2 * p - 1, 3 * p)
        print("  %s  %d     %-7s       %-7s       %s" % (names[p], p, diag, v12, Fraction(1, 3 * p)))
    print("\n  anchor: p=3 reproduces the corpus's 8/9 and 5/9 exactly.")
    print("  heavier colour => smaller leakage => MORE diagonal => less generation mixing.")
    print("\n  " + result["concept"])
