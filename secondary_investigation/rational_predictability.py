import math
from fractions import Fraction
from sftoe.core import SmithianValue, fold, take, ONE
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.proof import verify_value
from sftoe.gate import verify_code

def analyze_rational_orbit(x0_val):
    x = Fraction(x0_val)
    print(f"\nAnalyzing rational state X_0 = {x}:")
    
    # 1. Simulate step-by-step to find transient length k and period L
    visited = []
    curr = x
    for step in range(100):
        visited.append(curr)
        next_val = (curr * 2) % 1
        if next_val == 0:
            next_val = Fraction(1, 1)
        if next_val in visited:
            k = visited.index(next_val)
            L = len(visited) - k
            orbit = visited[k:]
            break
        curr = next_val
        
    print(f"  Transient length (k): {k}")
    print(f"  Orbit period length (L): {L}")
    print(f"  Stable orbit cycle: {orbit}")
    return k, L, orbit

def predict_future_state(k, L, orbit, N):
    """
    Predicts the exact state at step N (for arbitrary large N)
    without simulating step-by-step.
    """
    if N < k:
        # If N is in the transient, we can just run it
        # (This is rare for large N)
        return "Inside transient"
        
    # Find the position in the periodic cycle
    cycle_index = (N - k) % L
    return orbit[cycle_index]

def main():
    print("=== SADE: Rational Predictability Engine ===")
    
    # Chaotic state X_0 = 13/80
    # denominator 80 = 2^4 * 5 -> k=4 steps of transient, period of 5 is L=4 (2^4 = 16 = 1 mod 5)
    x0 = Fraction(13, 80)
    
    k, L, orbit = analyze_rational_orbit(x0)
    
    # Predict state at N = 10^100
    N = 10**100
    print(f"\nPredicting state at step N = 10^100 (Google-scale time):")
    predicted_val = predict_future_state(k, L, orbit, N)
    print(f"  Predicted state: {predicted_val}")
    
    # Verify by showing that 10^100 % 4 is indeed the same index
    # 10^100 = 2^100 * 5^100, which is a multiple of 4 since 2^100 is a multiple of 4.
    # Therefore, (10^100 - 4) % 4 = 0.
    # The index should be 0, which corresponds to orbit[0]
    print(f"  Orbit index 0 state: {orbit[0]}")
    print(f"  Is prediction mathematically 100% exact? {predicted_val == orbit[0]}")
    
    # Derive the chaotic state 13/80 using SADE pathfinder
    target = Fraction(13, 80)
    print(f"\nDeriving state {target} using SADE pathfinder...")
    proof = find_derivation(target)
    code = generate_sftoe_code(proof, "verify_predictable_state")
    
    print("\nVerifying generated code against AST constraints...")
    verify_code(code)
    print("AST Gate: PASSED")
    
    print("\nRunning generated code and verifying value...")
    namespace = {}
    exec(code, namespace)
    res = namespace["verify_predictable_state"]()
    verify_value(res)
    print(f"Value Verification: PASSED. Result: {res.value}")

if __name__ == "__main__":
    main()
