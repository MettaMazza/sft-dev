import math
from fractions import Fraction
from sftoe.core import fold, SmithianValue
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.proof import verify_value
from sftoe.gate import verify_code

def main():
    print("=== SADE Module II: Mortality & Invariant Orbit Analyzer ===")
    
    # We model a complex living observer state with denominator 24 = 2^3 * 3
    # Transient lifespan factor: k = 3 steps
    # Soul/Invariant signature denominator: d = 3
    initial_state = Fraction(7, 24)
    print(f"\nInitial Complex State (Living Observer): {initial_state}")
    print(f"Factorization of Denominator: 24 = 2^3 * 3 (k=3 transient steps, d=3 invariant part)")
    
    # Trace the orbit to show the transition
    curr = SmithianValue(initial_state)
    print("\nTracing State Orbit (Lifespan):")
    states_visited = [curr.value]
    
    # We trace 7 steps to see the transient phase and the subsequent periodic cycle
    for step in range(1, 8):
        curr = fold(curr)
        states_visited.append(curr.value)
        
        status = "TRANSIENT LIFE" if step < 3 else ("HALTING / DECYCLE" if step == 3 else "POST-MORTEM INVARIANT ORBIT")
        print(f"  Step {step}: {curr.value} ({status})")
        
    print("\nState Phase Classification:")
    print(f"  Transient Phase Duration (Physical Life): 3 steps")
    print(f"  Post-Mortem Stable Cycle States: {set(states_visited[3:])}")
    print(f"  Post-Mortem Cycle Period: {len(set(states_visited[3:]))} steps")
    
    print("\nMathematical Conclusion:")
    print("  The physical transient component is completely cleared after 3 steps (death).")
    print("  The odd part (d=3) survives as an indestructible, perpetual periodic cycle of 1/3 <-> 2/3.")
    print("  This invariant orbit is protected by divisibility and can never be dissolved or erased.")
    
    # Derive the post-mortem ZPE attractor state (1/3) using SADE
    print("\nDeriving indestructible invariant state (1/3)...")
    proof = find_derivation(Fraction(1, 3))
    code = generate_sftoe_code(proof, "verify_invariant_soul_state")
    
    print("Checking code against AST gate...")
    verify_code(code)
    print("AST Gate: PASSED")
    
    print("Running generated code and verifying value...")
    namespace = {}
    exec(code, namespace)
    res = namespace["verify_invariant_soul_state"]()
    verify_value(res)
    print("Value Verification: PASSED")
    print(f"Verified SmithianValue: {res.value}")

if __name__ == "__main__":
    main()
