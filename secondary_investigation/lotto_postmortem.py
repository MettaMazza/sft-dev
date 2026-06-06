"""
Lottery Post-Mortem — Actual Results vs All 5 Models.
Actual draw: 8, 10, 26, 30, 35, 42 + bonus 50
"""
import sys
import math
sys.path.insert(0, '/Users/Maria/Desktop/Smithian-Fold-Theory')

from fractions import Fraction
from sftoe.core import SmithianValue, fold, cast_out
from sftoe.proof import verify_value


def fold_frac(x):
    res = (x * 2) % 1
    return Fraction(1, 1) if res == 0 else res


def main():
    print("=" * 70)
    print("LOTTERY POST-MORTEM — 6th JUNE 2026")
    print("=" * 70)

    actual_main = {8, 10, 26, 30, 35, 42}
    actual_bonus = 50
    actual_all = actual_main | {actual_bonus}

    print(f"\n  ACTUAL RESULT: {sorted(actual_main)} + bonus {actual_bonus}")

    predictions = {
        "Channel model":          ([13, 28, 42, 45, 49, 52], 37),
        "Forward-forced":         ([5, 10, 33, 57, 58, 59], 22),
        "Engine-only":            ([14, 20, 40, 51, 55, 59], 29),
        "Composite rank":         ([1, 2, 28, 38, 48, 53], 29),
        "Holographic depth":      ([1, 10, 21, 28, 29, 48], 49),
    }

    # =========================================================================
    # COMPARISON
    # =========================================================================
    print(f"\n{'='*70}")
    print(f"MODEL COMPARISON")
    print(f"{'='*70}\n")

    print(f"  {'Model':<22} | {'Predicted':<30} | {'Bonus':<6} | {'Main Hits':<10} | {'Bonus?':<8} | {'Matched Balls'}")
    print(f"  {'-'*22} | {'-'*30} | {'-'*6} | {'-'*10} | {'-'*8} | {'-'*20}")

    for name, (balls, bonus) in predictions.items():
        ball_set = set(balls)
        hits = ball_set & actual_main
        bonus_hit = bonus == actual_bonus
        # Also check if bonus matches any main ball or vice versa
        bonus_in_main = bonus in actual_main
        predicted_in_bonus = actual_bonus in ball_set

        hit_count = len(hits)
        matched = sorted(hits) if hits else ["-"]
        extras = []
        if bonus_in_main:
            extras.append(f"bonus {bonus} was main ball")
        if predicted_in_bonus:
            extras.append(f"predicted {actual_bonus} was actual bonus")

        print(f"  {name:<22} | {str(sorted(balls)):<30} | {bonus:<6} | {hit_count:<10} | {'YES ✓' if bonus_hit else 'no':<8} | {matched}{' ' + str(extras) if extras else ''}")

    # =========================================================================
    # EXPECTED BY CHANCE
    # =========================================================================
    print(f"\n{'='*70}")
    print(f"RANDOM CHANCE BASELINE")
    print(f"{'='*70}")

    # Probability of matching k balls from 6 chosen out of 59
    from math import comb
    total = comb(59, 6)
    print(f"\n  Total combinations: {total:,}")

    for k in range(7):
        ways = comb(6, k) * comb(53, 6 - k)
        prob = ways / total
        print(f"  P(exactly {k} main balls) = {prob:.6f} ({prob*100:.3f}%)")

    expected_hits = 6 * 6 / 59
    print(f"\n  Expected hits per random guess: {expected_hits:.2f}")
    print(f"  Our models got: 1, 1, 0, 0, 1 hits")
    print(f"  Average: {(1+1+0+0+1)/5:.1f} hits per model")
    print(f"  This is CONSISTENT WITH RANDOM CHANCE ({expected_hits:.2f} expected)")

    # =========================================================================
    # NEAR MISSES
    # =========================================================================
    print(f"\n{'='*70}")
    print(f"NEAR MISSES (off by 1-2)")
    print(f"{'='*70}\n")

    for name, (balls, bonus) in predictions.items():
        near_misses = []
        for pred in balls:
            for act in sorted(actual_main):
                diff = abs(pred - act)
                if diff == 1 or diff == 2:
                    near_misses.append(f"{pred}→{act} (off by {diff})")
        # Check bonus
        bonus_diff = abs(bonus - actual_bonus)
        if 0 < bonus_diff <= 2:
            near_misses.append(f"bonus {bonus}→{actual_bonus} (off by {bonus_diff})")

        if near_misses:
            print(f"  {name}: {', '.join(near_misses)}")
        else:
            print(f"  {name}: none")

    # =========================================================================
    # FOLD-BACK ANALYSIS: What fold depth WOULD have produced these results?
    # =========================================================================
    print(f"\n{'='*70}")
    print(f"REVERSE ANALYSIS: WHAT DEPTH WOULD HAVE WORKED?")
    print(f"{'='*70}")

    prev_draw = [7, 10, 20, 55, 57, 59]

    print(f"\n  Previous draw: {prev_draw}")
    print(f"  Actual draw:   {sorted(actual_main)}")
    print(f"\n  Testing all fold depths 1-200 with denominator 59:")

    best_depth = 0
    best_hits = 0
    for depth in range(1, 201):
        hits = 0
        for b in prev_draw:
            state = Fraction(b, 59)
            for _ in range(depth):
                state = fold_frac(state)
            predicted = round(float(state) * 59)
            if predicted == 0:
                predicted = 59
            if predicted in actual_main:
                hits += 1
        if hits > best_hits:
            best_hits = hits
            best_depth = depth

    print(f"\n  Best depth found: {best_depth}")
    print(f"  Matches at that depth: {best_hits}/6")

    if best_hits > 0:
        print(f"\n  What it would have predicted at depth {best_depth}:")
        for b in prev_draw:
            state = Fraction(b, 59)
            for _ in range(best_depth):
                state = fold_frac(state)
            predicted = round(float(state) * 59)
            if predicted == 0:
                predicted = 59
            hit = "✓" if predicted in actual_main else "✗"
            print(f"    {b}/59 → fold^{best_depth} → {predicted} {hit}")

    # =========================================================================
    # COMPOSITE RANK ANALYSIS
    # =========================================================================
    print(f"\n{'='*70}")
    print(f"COMPOSITE RANK REVERSE CHECK")
    print(f"{'='*70}")

    def combo_to_rank(combo):
        """Compute lexicographic rank of a sorted combination from 1..59 choose 6."""
        rank = 0
        n = 59
        k = 6
        prev = 0
        for i, ball in enumerate(sorted(combo)):
            for j in range(prev + 1, ball):
                rank += comb(n - j, k - i - 1)
            prev = ball
        return rank

    prev_rank = combo_to_rank(prev_draw)
    actual_rank = combo_to_rank(sorted(actual_main))
    N = comb(59, 6)

    print(f"\n  Previous draw rank: {prev_rank:,}")
    print(f"  Actual draw rank:   {actual_rank:,}")
    print(f"  Total combinations: {N:,}")

    prev_state = Fraction(prev_rank + 1, N)
    actual_state = Fraction(actual_rank + 1, N)

    print(f"\n  Previous state S₁ = {prev_state}")
    print(f"  Actual state S₂ =   {actual_state}")

    # What depth connects them?
    print(f"\n  Testing: at what depth does fold^n(S₁) = S₂?")
    state = prev_state
    found = False
    for depth in range(1, 201):
        state = fold_frac(state)
        decoded_rank = round(float(state) * N) - 1
        if decoded_rank == actual_rank:
            print(f"  EXACT MATCH at depth {depth}!")
            found = True
            break

    if not found:
        # Find closest
        state = prev_state
        best_d = 0
        best_diff = float('inf')
        for depth in range(1, 201):
            state = fold_frac(state)
            decoded_rank = round(float(state) * N) - 1
            diff = abs(decoded_rank - actual_rank)
            if diff < best_diff:
                best_diff = diff
                best_d = depth

        print(f"  No exact match in 200 depths.")
        print(f"  Closest: depth {best_d}, off by {best_diff:,} ranks")
        print(f"  ({best_diff/N*100:.4f}% of total space)")

    # =========================================================================
    # HONEST CONCLUSION
    # =========================================================================
    print(f"\n{'='*70}")
    print(f"CONCLUSION")
    print(f"{'='*70}")
    print(f"""
  The 5 models scored 1, 1, 0, 0, 1 main ball hits.
  Random chance predicts ~0.6 hits per guess.
  Our average was 0.6 hits per model.

  Performance = random chance. The models did not capture
  the lottery's dynamics.

  WHY:
  The fold algebra predicts EXACT outcomes when the system
  IS a fold process (rational fraction, doubling map, known
  initial state, closed system). The lottery is NONE of these.
  It is a chaotic physical machine with unknown micro-states.

  The fold algebra's verified successes — orbit periods,
  consciousness invariants, denominator coupling — all work
  because they describe STRUCTURAL PROPERTIES of the algebra
  itself, not predictions about external physical systems.

  The honest finding: the SFTOE fold algebra is not a
  prediction engine for chaotic physical processes. It is a
  theory of structure, invariance, and coupling.
    """)


if __name__ == "__main__":
    main()
