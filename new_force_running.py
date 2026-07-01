"""The running and unification of the new forces — forced from the corpus's own law.
The corpus forces a coupling running law on the scale axis R = 2^d (verify_accumulated
_separation, proof.py:9373):
        g_p(R) = (p + R - 1) / (p + R) ,
and proves the strong-electroweak convergence gap has the closed form
        g_3(R) - g_2(R) = 1 / ((2+R)(3+R)) .
It only ever plugs in the sectors p = 2, 3. The two NEW forces it forces to exist
(prime sectors 5 and 7, verify_two_new_prime_charge_forces) are never run. Applying the
identical law to them gives, for ANY two sectors i < j, a single forced closed form:
        g_j(R) - g_i(R) = (j - i) / ((i+R)(j+R)) ,
proved by expansion (the numerator collapses to exactly j - i). The corpus proves the
one case (i,j)=(2,3); the other five are new, including the convergence of the two new
forces  g_7 - g_5 = 2/((5+R)(7+R)).  As R -> infinity every g_p -> 1: all four forces
converge to unison, each gap closing at its own forced rate. Nothing fitted; the law and
the sectors are both the corpus's own.
"""
from fractions import Fraction
from sftoe.core import SmithianValue, take, ONE
from sftoe.proof import verify_value, VerificationError

SECTORS = (2, 3, 5, 7)


def _no_zero_guard():
    try:
        SmithianValue(Fraction(1 - 1, 1))
    except ValueError:
        return
    raise VerificationError("No-zero axiom check failed.")


def running_coupling(p, d):
    """The corpus's running law g_p(R) = (p+R-1)/(p+R), R = 2^d.
    SmithianValue enforces the domain (0,1]; the forcing is carried by the Route A vs
    Route B cross-check in forced_gap, not by orbit-tracing (these derived couplings have
    large odd denominators at high depth, whose eternal orbits exceed verify_value's cap)."""
    R = 2 ** d
    return SmithianValue(Fraction(p + R - 1, p + R))


def forced_gap(i, j, d):
    """Route A (fold subtraction) vs Route B (closed form); raise on any mismatch."""
    if not j > i:
        raise VerificationError("gap requires j > i")
    gi = running_coupling(i, d)
    gj = running_coupling(j, d)
    if not gj.value > gi.value:
        raise VerificationError("coupling ordering violated: need g_j > g_i")
    route_a = take(gj, gi).value                                  # g_j - g_i, guarded
    R = 2 ** d
    route_b = Fraction(j - i, (i + R) * (j + R))                  # forced closed form
    if route_a != route_b:
        raise VerificationError(
            "running gap mismatch (i=%d j=%d d=%d): %s != %s" % (i, j, d, route_a, route_b))
    return route_a


def verify():
    """Full forced check: reproduce the corpus strong-EW gap, force all six gaps, and
    the unison limit. Raises VerificationError on any deviation."""
    _no_zero_guard()
    verify_value(ONE)

    # anchor: reproduce the corpus's proven strong-electroweak gap 1/((2+R)(3+R))
    for d in range(0, 11):
        R = 2 ** d
        anchor = forced_gap(2, 3, d)
        if anchor != Fraction(1, (2 + R) * (3 + R)):
            raise VerificationError("failed to reproduce corpus strong-EW gap")

    # all six inter-sector gaps forced by the single closed form (j-i)/((i+R)(j+R))
    pairs = [(i, j) for a, i in enumerate(SECTORS) for j in SECTORS[a + 1:]]
    for d in range(0, 11):
        for (i, j) in pairs:
            forced_gap(i, j, d)          # raises internally if Route A != Route B

    # the new-force convergence gap g_7 - g_5 = 2/((5+R)(7+R))
    for d in range(0, 11):
        R = 2 ** d
        if forced_gap(5, 7, d) != Fraction(2, (5 + R) * (7 + R)):
            raise VerificationError("new-force gap g7-g5 mismatch")

    # unison limit: each coupling strictly increases toward 1; every gap strictly shrinks
    for p in SECTORS:
        prev = None
        for d in range(0, 20):
            g = running_coupling(p, d).value
            if g >= 1:
                raise VerificationError("coupling reached or exceeded unison at finite scale")
            if prev is not None and not g > prev:
                raise VerificationError("coupling not monotonically rising to unison")
            prev = g
    for (i, j) in pairs:
        if not forced_gap(i, j, 0) > forced_gap(i, j, 10):
            raise VerificationError("gap did not shrink with scale")

    return {
        "concept": "The two new forces run and all four converge to unison; gap = (j-i)/((i+R)(j+R)).",
        "corpus_anchor_strong_ew_gap_d0": str(forced_gap(2, 3, 0)),   # 1/12
        "new_force_gap_g7_g5_d0": str(forced_gap(5, 7, 0)),           # 1/24
        "all_forces_converge_to_unison": True,
    }


if __name__ == "__main__":
    result = verify()
    print("=" * 74)
    print("THE NEW FORCES RUN — and all four converge to unison (forced)")
    print("=" * 74)
    print("\n  running law (corpus): g_p(R) = (p+R-1)/(p+R),  R = 2^d")
    print("  forced gap (all pairs): g_j(R) - g_i(R) = (j-i)/((i+R)(j+R))\n")
    header = "  d  R  " + "  ".join("g_%d" % p for p in SECTORS) + "     g7-g5(new)"
    print(header)
    for d in range(0, 6):
        R = 2 ** d
        gs = "  ".join("%.4f" % float(running_coupling(p, d).value) for p in SECTORS)
        print("  %d %2d  %s     %s" % (d, R, gs, forced_gap(5, 7, d)))
    print("\n  anchor: reproduces the corpus strong-EW gap 1/((2+R)(3+R)) exactly.")
    print("  R -> inf: every g_p -> 1  =>  ALL FOUR FORCES UNIFY at unison.")
    print("\n  " + result["concept"])
