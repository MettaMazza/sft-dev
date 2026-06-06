import math
from fractions import Fraction
from sftoe.core import SmithianValue, fold, take, period
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.proof import verify_value
from sftoe.gate import verify_code

def analyze_ctc_orbit(state_val):
    x = SmithianValue(state_val)
    orbit_period = period(x)
    print(f"\nAnalyzing state {x.value} as a Closed Timelike Curve (CTC):")
    print(f"  Orbit period (length of time loop L): {orbit_period}")
    
    # Trace the loop and verify self-consistency
    curr = x
    orbit = [curr.value]
    for step in range(orbit_period):
        curr = fold(curr)
        orbit.append(curr.value)
        
    print(f"  Timeline trajectory: {' -> '.join(str(v) for v in orbit)}")
    
    # Verify Novikov self-consistency: final state equals initial state
    self_consistent = (orbit[0] == orbit[-1])
    print(f"  Is timeline topologically self-consistent (no grandfather paradox)? {self_consistent}")
    
    return orbit_period, self_consistent

def main():
    print("=== SADE Topic C2: Time Travel & Closed Timelike Curves ===")
    
    # 1. Model CTC on periodic state 1/7
    analyze_ctc_orbit(Fraction(1, 7))
    
    # 2. Model CTC on periodic state 1/5
    analyze_ctc_orbit(Fraction(1, 5))
    
    # 3. Derive 1/7 using SADE pathfinder (1/7 is a periodic hypothesis orbit)
    target = Fraction(1, 7)
    print(f"\nDeriving state {target} using SADE pathfinder...")
    proof = find_derivation(target)
    code = generate_sftoe_code(proof, "verify_ctc_state")
    
    print("\nVerifying generated code against AST constraints...")
    verify_code(code)
    print("AST Gate: PASSED")
    
    print("\nRunning generated code and verifying value...")
    namespace = {}
    exec(code, namespace)
    res = namespace["verify_ctc_state"]()
    verify_value(res)
    print(f"Value Verification: PASSED. Result: {res.value}")

if __name__ == "__main__":
    main()
