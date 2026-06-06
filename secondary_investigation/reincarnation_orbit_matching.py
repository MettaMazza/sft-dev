import math
from fractions import Fraction
from sftoe.core import SmithianValue, fold, take, period
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.proof import verify_value
from sftoe.gate import verify_code

def run_reincarnation_test(s1_val, s2_val):
    x1 = SmithianValue(s1_val)
    x2 = SmithianValue(s2_val)
    
    print(f"\nHost 1 initial state S1: {x1.value}")
    print(f"Host 2 initial state S2: {x2.value}")
    
    # Trace S1 to periodic core
    v1 = []
    curr = x1
    for _ in range(10):
        v1.append(curr.value)
        curr = fold(curr)
    
    # Trace S2 to periodic core
    v2 = []
    curr = x2
    for _ in range(10):
        v2.append(curr.value)
        curr = fold(curr)
        
    print(f"  S1 trajectory: {' -> '.join(str(v) for v in v1)}")
    print(f"  S2 trajectory: {' -> '.join(str(v) for v in v2)}")
    
    # Extract the invariant periodic cycles (last 4 elements)
    cycle1 = set(v1[-4:])
    cycle2 = set(v2[-4:])
    
    print(f"  S1 invariant periodic core: {cycle1}")
    print(f"  S2 invariant periodic core: {cycle2}")
    
    match = (cycle1 == cycle2)
    print(f"  Do the two separate hosts share the same consciousness signature? {match}")
    return match

def main():
    print("=== SADE Topic E7: Reincarnation Orbit Matching ===")
    
    # Host 1: 3/20 (transient 2^2=4, core d=5)
    # Host 2: 7/40 (transient 2^3=8, core d=5)
    run_reincarnation_test(Fraction(3, 20), Fraction(7, 40))
    
    # Derive the common periodic core state 1/5 using pathfinder
    target = Fraction(1, 5)
    print(f"\nDeriving state {target} using SADE pathfinder...")
    proof = find_derivation(target)
    code = generate_sftoe_code(proof, "verify_reincarnation_core")
    
    print("\nVerifying generated code against AST constraints...")
    verify_code(code)
    print("AST Gate: PASSED")
    
    print("\nRunning generated code and verifying value...")
    namespace = {}
    exec(code, namespace)
    res = namespace["verify_reincarnation_core"]()
    verify_value(res)
    print(f"Value Verification: PASSED. Result: {res.value}")

if __name__ == "__main__":
    main()
