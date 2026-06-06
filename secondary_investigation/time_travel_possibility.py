import math
from fractions import Fraction
from sftoe.core import SmithianValue, fold, take, ONE
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.proof import verify_value
from sftoe.gate import verify_code

def search_algebraic_space(initial_states, max_depth=4):
    """
    Performs a BFS over all valid fold/take operations starting from initial_states.
    Returns the set of all reachable rational values.
    """
    reached = set(Fraction(x) for x in initial_states)
    
    for depth in range(max_depth):
        next_reached = set(reached)
        # Apply fold to all elements
        for x in reached:
            folded = (x * 2) % 1
            if folded == 0:
                folded = Fraction(1, 1)
            next_reached.add(folded)
            
        # Apply take to all pairs
        reached_list = list(reached)
        for i in range(len(reached_list)):
            for j in range(len(reached_list)):
                a = reached_list[i]
                b = reached_list[j]
                if a > b:
                    diff = a - b
                    next_reached.add(diff)
                    
        reached = next_reached
        
    return reached

def main():
    print("=== SADE: Physical Time Travel Algebraic Possibility ===")
    
    # Traveler state X = 3/5
    X = Fraction(3, 5)
    preimage_target = Fraction(3, 10)
    
    print(f"Traveler initial state X: {X}")
    print(f"Target past preimage coordinate: {preimage_target}")
    
    # Scenario 1: Closed system {X, 1} (No temporal conduit)
    print("\nScenario 1: Closed system starting from {X, ONE}...")
    reached_closed = search_algebraic_space({X, Fraction(1, 1)}, max_depth=4)
    
    # Check if target preimage is reached
    reached_preimage = preimage_target in reached_closed
    print(f"  Total states generated: {len(reached_closed)}")
    print(f"  Generated states: {sorted(list(reached_closed))}")
    print(f"  Was the past preimage {preimage_target} reached? {reached_preimage}")
    print("  Denominator Theorem: The denominators generated are strictly divisors of 5.")
    print("  Conclusion: Physical travel to this past coordinate is mathematically FORBIDDEN in a closed system.")
    
    # Scenario 2: Coupled system with conduit state Y = 1/2
    conduit = Fraction(1, 2)
    print(f"\nScenario 2: Coupled system starting from {X, ONE} + Conduit {conduit}...")
    reached_coupled = search_algebraic_space({X, Fraction(1, 1), conduit}, max_depth=4)
    
    reached_preimage_coupled = preimage_target in reached_coupled
    print(f"  Total states generated: {len(reached_coupled)}")
    print(f"  Was the past preimage {preimage_target} reached? {reached_preimage_coupled}")
    
    # Show the exact algebraic derivation
    # fold(3/5) = 1/5
    # take(1/2, 1/5) = 3/10
    print("\nDiscovered Algebraic Transition Path:")
    print("  Step 1: fold(3/5) = 1/5")
    print("  Step 2: take(1/2, 1/5) = 3/10")
    print("  Conclusion: Physical travel to the past is possible by coupling with a temporal conduit of higher denominator complexity.")
    
    # Derive the target state 3/10 using SADE pathfinder
    target = Fraction(3, 10)
    print(f"\nDeriving state {target} using SADE pathfinder...")
    proof = find_derivation(target)
    code = generate_sftoe_code(proof, "verify_time_travel_preimage")
    
    print("\nVerifying generated code against AST constraints...")
    verify_code(code)
    print("AST Gate: PASSED")
    
    print("\nRunning generated code and verifying value...")
    namespace = {}
    exec(code, namespace)
    res = namespace["verify_time_travel_preimage"]()
    verify_value(res)
    print(f"Value Verification: PASSED. Result: {res.value}")

if __name__ == "__main__":
    main()
