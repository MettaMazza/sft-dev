import math
from fractions import Fraction
from sftoe.core import SmithianValue, fold, take
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.proof import verify_value
from sftoe.gate import verify_code

def collatz_fractional_map(x):
    """
    Implements the Collatz map on the interval (0, 1] using x = 1/n.
    If 1/x is even: f(x) = 2x
    If 1/x is odd:  f(x) = x / (3 + x)
    """
    n = Fraction(1, x)
    # Ensure it's an integer
    if n.denominator != 1:
        # If not an integer, we generalize: if numerator is odd/even
        # For this model, we restrict to integer n (unit fractions)
        raise ValueError("Collatz fractional map is defined on unit fractions 1/n")
        
    n_val = int(n)
    if n_val % 2 == 0:
        return Fraction(2, n_val)
    else:
        return Fraction(1, 3 * n_val + 1)

def run_collatz_trace(start_n):
    x = Fraction(1, start_n)
    trace = [x]
    print(f"Collatz trace for n={start_n} (x={x}):")
    
    # Run up to 20 steps or until we see the 4-2-1 loop
    visited = {x}
    for step in range(20):
        try:
            x = collatz_fractional_map(x)
            trace.append(x)
            print(f"  Step {step + 1}: x = {x} (n = {1/x})")
            if x in visited and len(visited) > 3:
                # We hit a loop
                print(f"Detected loop at step {step + 1}!")
                break
            visited.add(x)
        except Exception as e:
            print(f"Error: {e}")
            break
            
    return trace

def main():
    print("=== SADE Topic B6: Collatz Conjecture Fold Analysis ===")
    
    # 1. Run trace for n=3 (x=1/3)
    run_collatz_trace(3)
    
    # 2. Run trace for n=7 (x=1/7)
    print("")
    run_collatz_trace(7)
    
    # 3. Derive 3/16 using SADE pathfinder
    target = Fraction(3, 16)
    print(f"\nDeriving state {target} using SADE pathfinder...")
    proof = find_derivation(target)
    code = generate_sftoe_code(proof, "verify_collatz_state")
    
    print("\nVerifying generated code against AST constraints...")
    verify_code(code)
    print("AST Gate: PASSED")
    
    print("\nRunning generated code and verifying value...")
    namespace = {}
    exec(code, namespace)
    res = namespace["verify_collatz_state"]()
    verify_value(res)
    print(f"Value Verification: PASSED. Result: {res.value}")

if __name__ == "__main__":
    main()
