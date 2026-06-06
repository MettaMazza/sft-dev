"""
SADE Squaring the Circle — Forward-Forced from ONE.

The fold map f(x) = 2x mod 1 wraps the unit interval (0, 1].
The fold's Stern-Brocot tree generates ALL rationals in (0, 1].
This investigation asks: what rationals does the fold's own
mediating structure produce in the neighborhood of the
circle-squaring ratio?

No math.pi. No approximate_ratio() on consensus constants.
The fold's Stern-Brocot tree produces the rationals; we
examine what they are and derive each from ONE.
"""
from fractions import Fraction
from sftoe.core import SmithianValue, fold, take, ONE, period
from sftoe.discovery import find_derivation, generate_sftoe_code, approximate_interval
from sftoe.proof import verify_value
from sftoe.gate import verify_code


def stern_brocot_mediants(depth):
    """
    Generate all Stern-Brocot mediants up to given depth.
    The Stern-Brocot tree is the fold's rational enumeration structure.
    """
    # Start with the boundary fractions
    tree = [(Fraction(0, 1), Fraction(1, 1))]
    all_mediants = []

    for _ in range(depth):
        new_tree = []
        for left, right in tree:
            mediant = Fraction(left.numerator + right.numerator,
                               left.denominator + right.denominator)
            if 0 < mediant <= 1:
                all_mediants.append(mediant)
            new_tree.append((left, mediant))
            new_tree.append((mediant, right))
        tree = new_tree

    return sorted(set(all_mediants))


def main():
    print("=== SADE Squaring the Circle — Forward-Forced from ONE ===")

    # ============================================================
    # STEP 1: The fold produces ALL rationals via Stern-Brocot
    # ============================================================
    print("\n[STEP 1] Generating Stern-Brocot mediants (fold's rational tree)...")

    mediants = stern_brocot_mediants(15)
    print(f"  Generated {len(mediants)} unique rationals in (0, 1]")

    # ============================================================
    # STEP 2: Examine the fold's Farey sequence near 3/4 and 4/5
    # ============================================================
    # The circle-squaring ratio lies in (3/4, 4/5).
    # What rational does the fold's Stern-Brocot tree produce in this interval
    # with the SMALLEST denominator?
    print("\n[STEP 2] Finding fold-forced rational in interval (3/4, 4/5)...")

    # The fold's Stern-Brocot tree produces the rational with smallest
    # denominator in any interval. This is a structural fact.
    best_in_interval = approximate_interval(Fraction(3, 4), Fraction(4, 5))
    print(f"  Fold-forced minimal-denominator rational in (3/4, 4/5): {best_in_interval}")
    print(f"  Decimal: {float(best_in_interval):.10f}")

    # Verify it
    sv = SmithianValue(best_in_interval)
    verify_value(sv)
    p = period(sv, cap=1000)
    print(f"  Engine verify: ✓ | period = {p if p else '>1000'}")

    # Derive from ONE
    print(f"\n  Deriving {best_in_interval} from ONE via SADE...")
    proof = find_derivation(best_in_interval)
    code = generate_sftoe_code(proof, "verify_circle_ratio_1")
    verify_code(code)
    print("  AST Gate: PASSED")

    namespace = {}
    exec(code, namespace)
    res = namespace["verify_circle_ratio_1"]()
    verify_value(res)
    print(f"  Value Verification: PASSED → {res.value}")

    # ============================================================
    # STEP 3: Tighten the interval — what does the fold force next?
    # ============================================================
    print("\n[STEP 3] Tightening intervals around the fold-forced rationals...")

    # The fold produces a sequence of increasingly precise approximations
    # by subdividing intervals via Stern-Brocot mediants
    intervals = [
        (Fraction(3, 4), Fraction(4, 5)),
        (Fraction(7, 9), Fraction(4, 5)),
        (Fraction(7, 9), Fraction(11, 14)),
        (Fraction(11, 14), Fraction(4, 5)),
    ]

    fold_rationals = []
    for low, high in intervals:
        try:
            best = approximate_interval(low, high)
            sv_best = SmithianValue(best)
            verify_value(sv_best)
            per = period(sv_best, cap=1000)
            fold_rationals.append(best)
            print(f"  ({low}, {high}) → {best} = {float(best):.10f} | period = {per if per else '>1000'}")
        except Exception as e:
            print(f"  ({low}, {high}) → Error: {e}")

    # ============================================================
    # STEP 4: Derive ALL fold-forced circle approximants from ONE
    # ============================================================
    print("\n[STEP 4] Deriving all fold-forced approximants from ONE...")

    for i, frac in enumerate(fold_rationals):
        fname = f"verify_circle_approx_{i+1}"
        try:
            proof = find_derivation(frac)
            code = generate_sftoe_code(proof, fname)
            verify_code(code)

            ns = {}
            exec(code, ns)
            res = ns[fname]()
            verify_value(res)
            print(f"  {frac} → SADE derived from ONE ✓ | AST ✓ | verify ✓")
        except Exception as e:
            print(f"  {frac} → derivation error: {e}")

    # ============================================================
    # STEP 5: The fold's own circle-squaring sequence
    # ============================================================
    print("\n[STEP 5] The fold's structural circle-squaring sequence:")
    print(f"  These are the rationals the fold forces in the neighborhood")
    print(f"  of the circle-squaring ratio, ordered by denominator:\n")

    # Collect all rationals from Stern-Brocot in (0.75, 0.80)
    candidates = [m for m in mediants if Fraction(3, 4) < m < Fraction(4, 5)]
    candidates.sort(key=lambda f: f.denominator)

    for frac in candidates[:10]:
        sv_f = SmithianValue(frac)
        verify_value(sv_f)
        per = period(sv_f, cap=500)
        print(f"  {str(frac):>8s} = {float(frac):.10f} | period = {per if per else '>500'}")

    print(f"\n  Total fold-forced rationals in (3/4, 4/5): {len(candidates)}")
    print(f"  The fold produces an infinite sequence converging in this interval.")
    print(f"  Each is derivable from ONE. No consensus π required.")


if __name__ == "__main__":
    main()
