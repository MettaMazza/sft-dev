import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fractions import Fraction
from sftoe.core import SmithianValue, fold, take, ONE
from sftoe.proof import verify_value
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.gate import verify_code

class Derivation:
    def __init__(self, val, op, args, depth):
        self.val = val
        self.op = op
        self.args = args
        self.depth = depth

def fold_frac(x):
    res = (x * 2) % 1
    if res == 0:
        return Fraction(1, 1)
    return res

def to_str(D, c_frac, m_frac):
    if D.op == 'init':
        if D.val == c_frac:
            return "C"
        elif D.val == m_frac:
            return "M"
        elif D.val == Fraction(1, 1):
            return "ONE"
        else:
            return f"Fraction({D.val.numerator}, {D.val.denominator})"
    elif D.op == 'fold':
        return f"fold({to_str(D.args[0], c_frac, m_frac)})"
    elif D.op == 'take':
        return f"take({to_str(D.args[0], c_frac, m_frac)}, {to_str(D.args[1], c_frac, m_frac)})"

def run_forcing_bfs():
    print("================================================================")
    print("MENTAL MATTER MANIPULATION (STATE FORCING) BFS INVESTIGATION")
    print("================================================================")

    scenarios = [
        {"name": "Telekinesis", "C": Fraction(1, 3), "M": Fraction(1, 4), "T": Fraction(3, 4)},
        {"name": "Phase shift", "C": Fraction(1, 7), "M": Fraction(1, 6), "T": Fraction(5, 6)},
        {"name": "State creation", "C": Fraction(1, 5), "M": Fraction(1, 4), "T": Fraction(1, 10)},
        {"name": "Destruction prevention", "C": Fraction(1, 15), "M": Fraction(1, 8), "T": Fraction(1, 15)},
    ]

    for sc in scenarios:
        c_frac = sc["C"]
        m_frac = sc["M"]
        t_frac = sc["T"]
        name = sc["name"]

        print(f"\nScenario: {name}")
        print(f"  Inputs: C = {c_frac}, M_0 = {m_frac} | Target T = {t_frac}")

        reach = {
            c_frac: Derivation(c_frac, 'init', [], 0),
            m_frac: Derivation(m_frac, 'init', [], 0),
            Fraction(1, 1): Derivation(Fraction(1, 1), 'init', [], 0)
        }

        # Run BFS up to depth 8
        found = False
        for depth in range(1, 9):
            current_known = list(reach.values())
            # Folds
            for D_x in current_known:
                f = fold_frac(D_x.val)
                if f not in reach:
                    reach[f] = Derivation(f, 'fold', [D_x], depth)
            # Takes
            for D_x in current_known:
                for D_y in current_known:
                    if D_x.val > D_y.val:
                        t_val = D_x.val - D_y.val
                        if t_val not in reach:
                            reach[t_val] = Derivation(t_val, 'take', [D_x, D_y], depth)
            
            if t_frac in reach:
                found = True
                break

        if found:
            D_target = reach[t_frac]
            path_str = to_str(D_target, c_frac, m_frac)
            print(f"  Target Reachable! Depth: {D_target.depth}")
            print(f"  Algebraic Path: {path_str}")

            # SADE verify the target value
            target_val = SmithianValue(t_frac)
            proof = find_derivation(t_frac)
            code = generate_sftoe_code(proof, f"verify_{name.lower().replace(' ', '_')}")
            print(f"  SADE Generated Code:")
            print(code)
            print("  Code Complies with Gate:", verify_code(code))
        else:
            print("  Target NOT Reachable up to depth 8.")
            c_denom = c_frac.denominator
            m_denom = m_frac.denominator
            t_denom = t_frac.denominator
            lcm_denom = (c_denom * m_denom) // import_gcd(c_denom, m_denom)
            print(f"  Denominator Analysis: LCM of inputs is {lcm_denom}, Target denominator is {t_denom}.")

def import_gcd(a, b):
    import math
    return math.gcd(a, b)

if __name__ == "__main__":
    run_forcing_bfs()
