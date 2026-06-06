import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fractions import Fraction
from sftoe.core import SmithianValue, fold, take, rotate, period, ONE
from sftoe.proof import verify_value
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.gate import verify_code

def run_coupling_analysis():
    print("================================================================")
    print("CONSCIOUSNESS-MATTER ORBIT COUPLING ANALYSIS")
    print("================================================================")

    c_states = [Fraction(1, 3), Fraction(1, 5), Fraction(1, 7), Fraction(1, 15), Fraction(1, 31)]
    m_states = [Fraction(1, 4), Fraction(3, 8), Fraction(5, 16), Fraction(7, 64), Fraction(1, 6), Fraction(3, 10), Fraction(49, 67)]
    N = 50

    results = []

    for c_frac in c_states:
        for m_frac in m_states:
            print(f"\nAnalyzing Pair: C = {c_frac}, M = {m_frac}")
            
            # 1. Uncoupled evolution
            c_uncoupled = []
            m_uncoupled = []
            c_val = SmithianValue(c_frac)
            m_val = SmithianValue(m_frac)
            for _ in range(N):
                c_uncoupled.append(c_val.value)
                m_uncoupled.append(m_val.value)
                c_val = fold(c_val)
                m_val = fold(m_val)

            # 2. Coupled evolution via take
            m_take_trajectory = []
            c_val = SmithianValue(c_frac)
            m_val = SmithianValue(m_frac)
            take_success = True
            take_error_reason = None
            for step in range(N):
                m_take_trajectory.append(m_val.value)
                try:
                    if c_val.value == m_val.value:
                        raise AssertionError("Equality violation: cannot take equal values")
                    
                    if c_val.value > m_val.value:
                        coupled_m = take(c_val, m_val)
                    else:
                        coupled_m = take(m_val, c_val)
                    
                    c_val = fold(c_val)
                    m_val = fold(coupled_m)
                except AssertionError as e:
                    take_success = False
                    take_error_reason = str(e)
                    break
                except Exception as e:
                    take_success = False
                    take_error_reason = str(e)
                    break

            # 3. Coupled evolution via rotate
            m_rotate_trajectory = []
            c_val = SmithianValue(c_frac)
            m_val = SmithianValue(m_frac)
            for step in range(N):
                m_rotate_trajectory.append(m_val.value)
                coupled_m = rotate(m_val, c_val)
                c_val = fold(c_val)
                m_val = fold(coupled_m)

            # Analyze trajectory changes
            # Uncoupled attractor info
            unique_m_uncoupled = list(set(m_uncoupled[N//2:]))
            uncoupled_period = len(unique_m_uncoupled)

            # Coupled via rotate attractor info
            unique_m_rotate = list(set(m_rotate_trajectory[N//2:]))
            rotate_period = len(unique_m_rotate)

            rotate_altered = (m_rotate_trajectory != m_uncoupled)

            # Coupled via take attractor info
            if take_success:
                unique_m_take = list(set(m_take_trajectory[N//2:]))
                take_period = len(unique_m_take)
                take_altered = (m_take_trajectory != m_uncoupled)
            else:
                take_period = None
                take_altered = None

            results.append({
                "C": c_frac,
                "M": m_frac,
                "take_success": take_success,
                "take_error": take_error_reason,
                "uncoupled_period": uncoupled_period,
                "rotate_period": rotate_period,
                "rotate_altered": rotate_altered,
                "take_period": take_period,
                "take_altered": take_altered,
                "rotate_trajectory": [str(x) for x in m_rotate_trajectory[:10]],
                "take_trajectory": [str(x) for x in m_take_trajectory[:10]] if take_success else None
            })

            print(f"  Uncoupled Period: {uncoupled_period}")
            print(f"  Rotate Coupling Altered: {rotate_altered} | Rotate Period: {rotate_period}")
            if take_success:
                print(f"  Take Coupling Altered: {take_altered} | Take Period: {take_period}")
            else:
                print(f"  Take Coupling Failed: {take_error_reason}")

    # Output raw LaTeX-ready results table
    print("\n================================================================")
    print("RESULTS SUMMARY TABLE")
    print("================================================================")
    print("C | M | Take Success | Take Period | Rotate Period | Rotate Altered")
    for r in results:
        take_p_str = str(r["take_period"]) if r["take_success"] else "FAILED"
        print(f"{r['C']} | {r['M']} | {r['take_success']} | {take_p_str} | {r['rotate_period']} | {r['rotate_altered']}")

    # Let's perform SADE verification on one specific coupling result
    # We choose C=1/3, M=1/6. Let's verify the first coupled state of take:
    # C_0 = 1/3, M_0 = 1/6. C_0 > M_0. take(1/3, 1/6) = 1/6.
    # We find derivation and generate SADE code to show the gate verification pipeline works for coupling states.
    sample_val = SmithianValue(Fraction(1, 6))
    proof = find_derivation(sample_val.value)
    code = generate_sftoe_code(proof, "verify_coupling_sample")
    print("\nSADE Generated Code for Coupling Sample state 1/6:")
    print(code)
    print("Code Complies with Gate:", verify_code(code))

if __name__ == "__main__":
    run_coupling_analysis()
