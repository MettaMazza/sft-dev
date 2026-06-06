import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fractions import Fraction
from sftoe.core import SmithianValue, fold, take, ONE
from sftoe.proof import verify_value

def get_preimages(x):
    # Returns the two preimages of a Fraction x under the SFTOE fold map
    # fold(y) = 2y mod 1 (with 0 -> 1)
    if x == Fraction(1, 1):
        return [Fraction(1, 2), Fraction(1, 1)]
    return [x / 2, (x + 1) / 2]

def get_past_states(m0, steps=5):
    # Computes the set of preimages at each past step -1, -2, ..., -steps
    # Returns a dict: step -> list of Fractions
    past = {}
    current_set = {m0}
    for s in range(1, steps + 1):
        next_set = set()
        for x in current_set:
            next_set.update(get_preimages(x))
        past[-s] = sorted(list(next_set))
        current_set = next_set
    return past

def fold_frac(x):
    # Exact fraction fold
    res = (x * 2) % 1
    if res == 0:
        return Fraction(1, 1)
    return res

def run_temporal_bfs():
    print("================================================================")
    print("MENTAL TEMPORAL MANIPULATION BFS INVESTIGATION")
    print("================================================================")

    c_states = [Fraction(1, 3), Fraction(1, 5), Fraction(1, 7), Fraction(1, 15)]
    m_states = [Fraction(3, 8), Fraction(5, 16), Fraction(1, 6), Fraction(3, 10)]

    for c_frac in c_states:
        for m_frac in m_states:
            print(f"\nAnalyzing C = {c_frac} | M = {m_frac}")
            
            # Compute future states M_t for t = 1 to 20
            future_states = {}
            curr = m_frac
            for t in range(1, 21):
                curr = fold_frac(curr)
                future_states[t] = curr

            # Compute past states (preimages) for steps = -1 to -5
            past_states = get_past_states(m_frac, steps=5)

            # BFS reachable set from {C, M_0, ONE} up to depth 6
            reach = {c_frac: 0, m_frac: 0, Fraction(1, 1): 0}
            for depth in range(1, 7):
                current_known = list(reach.keys())
                # Generate folds
                for x in current_known:
                    f = fold_frac(x)
                    if f not in reach:
                        reach[f] = depth
                # Generate takes
                for x in current_known:
                    for y in current_known:
                        if x > y:
                            t_val = x - y
                            if t_val not in reach:
                                reach[t_val] = depth

            # Determine which future states are reachable
            reachable_future = []
            for t in range(1, 21):
                ft = future_states[t]
                if ft in reach:
                    reachable_future.append((t, ft, reach[ft]))

            # Determine which past states are reachable
            reachable_past = []
            for s in range(1, 6):
                for p in past_states[-s]:
                    if p in reach:
                        reachable_past.append((-s, p, reach[p]))

            # Denominator barrier analysis
            c_denom = c_frac.denominator
            m_denom = m_frac.denominator
            lcm_denom = (c_denom * m_denom) // import_gcd(c_denom, m_denom)
            print(f"  Denominator of C: {c_denom} | Denominator of M: {m_denom} | LCM: {lcm_denom}")
            print(f"  Total Reachable States: {len(reach)}")
            print(f"  Reachable Future States (out of 20):")
            for t, ft, d in reachable_future:
                print(f"    M_{t} = {ft} (reached at depth {d})")
            print(f"  Reachable Past States (out of 5 steps back):")
            for s, pt, d in reachable_past:
                print(f"    M_{s} = {pt} (reached at depth {d})")

def import_gcd(a, b):
    import math
    return math.gcd(a, b)

if __name__ == "__main__":
    run_temporal_bfs()
