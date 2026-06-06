"""
Lottery Fold Investigation — Systematic Search for True Parameters.
Answers the 4 open questions:
  1. What is the true denominator?
  2. What is the true fold depth?
  3. What is the true state encoding?
  4. What is the inter-ball coupling structure?

Uses ONLY the SADE engine. Zero inference. The numbers decide.
"""
import sys
import math
sys.path.insert(0, '/Users/Maria/Desktop/Smithian-Fold-Theory')

from fractions import Fraction
from math import comb, gcd
from collections import Counter

# Try to import historical data
try:
    from secondary_investigation.lotto_historical_data import DRAWS
    print(f"Loaded {len(DRAWS)} historical draws.")
except ImportError:
    # Fallback to known draws
    DRAWS = [
        {'date': '23rd May 2026', 'main': [4, 5, 6, 7, 11, 33], 'bonus': 35},
        {'date': '27th May 2026', 'main': [33, 36, 38, 46, 47, 50], 'bonus': 35},
        {'date': '30th May 2026', 'main': [4, 17, 18, 20, 23, 56], 'bonus': 33},
        {'date': '3rd June 2026', 'main': [7, 10, 20, 55, 57, 59], 'bonus': 44},
        {'date': '6th June 2026', 'main': [8, 10, 26, 30, 35, 42], 'bonus': 50},
    ]
    print(f"Using {len(DRAWS)} known draws (waiting for full historical data).")


def fold_frac(x):
    res = (x * 2) % 1
    return Fraction(1, 1) if res == 0 else res


def fold_n(x, n):
    """Apply fold n times."""
    for _ in range(n):
        x = fold_frac(x)
    return x


def fold_mod(b, d, n):
    """Compute (2^n * b) mod d using modular exponentiation."""
    return pow(2, n, d) * b % d


# =========================================================================
# QUESTION 1: What is the true denominator?
# =========================================================================
def investigate_denominator(draws):
    print("\n" + "=" * 70)
    print("QUESTION 1: WHAT IS THE TRUE DENOMINATOR?")
    print("=" * 70)

    transitions = []
    for i in range(len(draws) - 1):
        for ball_idx in range(6):
            b_from = draws[i]['main'][ball_idx]
            b_to = draws[i + 1]['main'][ball_idx]
            transitions.append((b_from, b_to))

    # Also collect ALL ball-to-any-ball transitions
    all_transitions = []
    for i in range(len(draws) - 1):
        for b_from in draws[i]['main']:
            for b_to in draws[i + 1]['main']:
                all_transitions.append((b_from, b_to))

    # Test denominators from 59 to 500
    print(f"\n  Testing denominators d = 59 to 500...")
    print(f"  For each d, test all depths 1-100.")
    print(f"  Score = number of transitions where (2^n * b_from) mod d maps to b_to.\n")

    best_results = []

    for d in range(59, 501):
        best_depth = 0
        best_score = 0

        for n in range(1, 101):
            score = 0
            for b_from, b_to in all_transitions:
                if b_from > d or b_to > d:
                    continue
                predicted = fold_mod(b_from, d, n)
                if predicted == 0:
                    predicted = d
                # Direct match
                if predicted == b_to:
                    score += 1
                # Modular match (b_to could be predicted mod 59)
                elif predicted % 59 == b_to % 59 and predicted > 0:
                    score += 1

            if score > best_score:
                best_score = score
                best_depth = n

        if best_score > 0:
            best_results.append((d, best_depth, best_score))

    # Sort by score
    best_results.sort(key=lambda x: -x[2])

    print(f"  Top 20 denominators by transition match score:\n")
    print(f"  {'Rank':<6} | {'Denom d':<10} | {'Best Depth':<12} | {'Score':<8} | {'Factors'}")
    print(f"  {'-'*6} | {'-'*10} | {'-'*12} | {'-'*8} | {'-'*30}")

    for rank, (d, depth, score) in enumerate(best_results[:20], 1):
        factors = []
        temp = d
        for p in range(2, int(temp**0.5) + 2):
            while temp % p == 0:
                factors.append(p)
                temp //= p
            if temp == 1:
                break
        if temp > 1:
            factors.append(temp)
        print(f"  {rank:<6} | {d:<10} | {depth:<12} | {score:<8} | {factors}")

    return best_results[:20]


# =========================================================================
# QUESTION 2: What is the true fold depth?
# =========================================================================
def investigate_depth(draws):
    print("\n" + "=" * 70)
    print("QUESTION 2: WHAT IS THE TRUE FOLD DEPTH?")
    print("=" * 70)

    n_transitions = len(draws) - 1
    print(f"\n  Testing depths 1-200 across {n_transitions} consecutive transitions.")
    print(f"  For each depth, count total ball matches.\n")

    # Test with d=59 first (simplest model)
    for d in [59]:
        print(f"  --- Denominator d = {d} ---")
        depth_scores = []

        for n in range(1, 201):
            total_matches = 0
            for i in range(len(draws) - 1):
                draw_matches = 0
                for b in draws[i]['main']:
                    predicted = fold_mod(b, d, n)
                    if predicted == 0:
                        predicted = d
                    if predicted <= 59 and predicted in draws[i + 1]['main']:
                        draw_matches += 1
                total_matches += draw_matches
            depth_scores.append((n, total_matches))

        depth_scores.sort(key=lambda x: -x[1])
        expected = n_transitions * 6 * 6 / 59

        print(f"  Expected by chance: {expected:.1f} total matches")
        print(f"\n  Top 15 depths:\n")
        print(f"  {'Depth':<8} | {'Total Matches':<15} | {'Per Draw':<10} | {'vs Chance'}")
        print(f"  {'-'*8} | {'-'*15} | {'-'*10} | {'-'*12}")

        for n, score in depth_scores[:15]:
            per_draw = score / n_transitions if n_transitions > 0 else 0
            ratio = score / expected if expected > 0 else 0
            print(f"  {n:<8} | {score:<15} | {per_draw:<10.2f} | {ratio:.2f}x")


# =========================================================================
# QUESTION 3: What is the true state encoding?
# =========================================================================
def investigate_encoding(draws):
    print("\n" + "=" * 70)
    print("QUESTION 3: WHAT IS THE TRUE STATE ENCODING?")
    print("=" * 70)

    print(f"\n  Testing alternative encodings of ball → fraction:\n")

    encodings = {
        "b/59 (direct)":           lambda b: Fraction(b, 59),
        "(60-b)/59 (reverse)":     lambda b: Fraction(60 - b, 59),
        "b/60":                    lambda b: Fraction(b, 60),
        "(b-1)/58":                lambda b: Fraction(max(b - 1, 1), 58),
        "b/118 (half-range)":      lambda b: Fraction(b, 118),
        "(2b-1)/118 (odd-only)":   lambda b: Fraction(2 * b - 1, 118),
        "b/(59*2)":                lambda b: Fraction(b, 118),
        "b/61 (prime)":            lambda b: Fraction(b, 61),
        "b/53 (prime)":            lambda b: Fraction(b % 53 or 53, 53),
        "b/67 (prime)":            lambda b: Fraction(b, 67),
        "b/71 (prime)":            lambda b: Fraction(b, 71),
        "b/83 (prime)":            lambda b: Fraction(b, 83),
        "b/97 (prime)":            lambda b: Fraction(b, 97),
        "b/127 (Mersenne)":        lambda b: Fraction(b, 127),
        "b/131":                   lambda b: Fraction(b, 131),
    }

    n_transitions = len(draws) - 1

    for enc_name, enc_fn in encodings.items():
        best_depth = 0
        best_score = 0
        test_d = enc_fn(1).denominator

        for n in range(1, 201):
            total = 0
            for i in range(len(draws) - 1):
                for b in draws[i]['main']:
                    state = enc_fn(b)
                    folded = fold_n(state, n)
                    # Decode back to ball number
                    decoded = round(float(folded) * test_d)
                    if decoded == 0:
                        decoded = test_d
                    # Check if decoded maps to any actual ball
                    if decoded <= 59 and decoded in draws[i + 1]['main']:
                        total += 1
            if total > best_score:
                best_score = total
                best_depth = n

        expected = n_transitions * 6 * 6 / 59
        ratio = best_score / expected if expected > 0 else 0
        marker = " ★" if ratio > 1.5 else ""
        print(f"  {enc_name:<28} | best depth {best_depth:<4} | score {best_score:<4} | {ratio:.2f}x chance{marker}")


# =========================================================================
# QUESTION 4: Inter-ball coupling
# =========================================================================
def investigate_coupling(draws):
    print("\n" + "=" * 70)
    print("QUESTION 4: INTER-BALL COUPLING STRUCTURE")
    print("=" * 70)

    print(f"\n  Are ball-to-ball transitions position-dependent or free?")
    print(f"  Testing: does ball in position i predict ball in position i of next draw?\n")

    n_transitions = len(draws) - 1

    # Position-locked test
    print(f"  A) POSITION-LOCKED (ball[i] → ball[i]):")
    for n in [1, 5, 9, 15, 20, 39, 50]:
        matches = 0
        for i in range(len(draws) - 1):
            for pos in range(6):
                b = draws[i]['main'][pos]
                predicted = fold_mod(b, 59, n)
                if predicted == 0:
                    predicted = 59
                if predicted == draws[i + 1]['main'][pos]:
                    matches += 1
        expected = n_transitions * 6 / 59
        print(f"    depth {n:<4}: {matches} matches (chance: {expected:.1f})")

    # Free test (any position)
    print(f"\n  B) FREE (ball[i] → any position):")
    for n in [1, 5, 9, 15, 20, 39, 50]:
        matches = 0
        for i in range(len(draws) - 1):
            for b in draws[i]['main']:
                predicted = fold_mod(b, 59, n)
                if predicted == 0:
                    predicted = 59
                if predicted in draws[i + 1]['main']:
                    matches += 1
        expected = n_transitions * 6 * 6 / 59
        print(f"    depth {n:<4}: {matches} matches (chance: {expected:.1f})")

    # Sum-based encoding: treat entire draw as a single number
    print(f"\n  C) SUM-BASED ENCODING:")
    print(f"     Encode draw as sum of balls, then fold the sum.\n")
    for n in range(1, 51):
        matches = 0
        for i in range(len(draws) - 1):
            s = sum(draws[i]['main'])
            predicted_sum = fold_mod(s, 354, n)  # max sum = 54+55+56+57+58+59 = 339
            if predicted_sum == 0:
                predicted_sum = 354
            actual_sum = sum(draws[i + 1]['main'])
            if predicted_sum == actual_sum:
                matches += 1
        if matches > 0:
            print(f"    depth {n}: {matches}/{n_transitions} sum matches")

    # Rank-based encoding
    print(f"\n  D) LEXICOGRAPHIC RANK ENCODING:")
    print(f"     Encode draw as combo rank, fold, decode.\n")

    def combo_to_rank(combo):
        rank = 0
        prev = 0
        for i, ball in enumerate(sorted(combo)):
            for j in range(prev + 1, ball):
                rank += comb(59 - j, 5 - i)
            prev = ball
        return rank

    def rank_to_combo(rank):
        combo = []
        prev = 0
        for i in range(6):
            for j in range(prev + 1, 60):
                c = comb(59 - j, 5 - i)
                if rank < c:
                    combo.append(j)
                    prev = j
                    break
                rank -= c
        return combo

    N = comb(59, 6)
    for n in range(1, 51):
        total_overlap = 0
        for i in range(len(draws) - 1):
            r = combo_to_rank(draws[i]['main'])
            state = Fraction(r + 1, N)
            folded = fold_n(state, n)
            pred_rank = round(float(folded) * N) - 1
            pred_rank = max(0, min(pred_rank, N - 1))
            try:
                pred_combo = rank_to_combo(pred_rank)
                overlap = len(set(pred_combo) & set(draws[i + 1]['main']))
                total_overlap += overlap
            except:
                pass
        expected = (len(draws) - 1) * 6 * 6 / 59
        if total_overlap > expected * 1.3:
            print(f"    depth {n}: {total_overlap} ball overlaps ({total_overlap/expected:.2f}x chance) ★")
        elif total_overlap > 0 and n <= 20:
            print(f"    depth {n}: {total_overlap} ball overlaps ({total_overlap/expected:.2f}x chance)")


def main():
    print("=" * 70)
    print("SYSTEMATIC LOTTERY FOLD INVESTIGATION")
    print(f"Using {len(DRAWS)} historical draws")
    print("=" * 70)

    top_denoms = investigate_denominator(DRAWS)
    investigate_depth(DRAWS)
    investigate_encoding(DRAWS)
    investigate_coupling(DRAWS)

    print("\n" + "=" * 70)
    print("INVESTIGATION COMPLETE")
    print("=" * 70)
    print(f"\n  Results above show which parameters score above chance.")
    print(f"  Any parameter scoring >1.5x chance is marked with ★")
    print(f"  The true mapping requires ALL parameters correct simultaneously.")


if __name__ == "__main__":
    main()
