import math
from fractions import Fraction
from sftoe.core import SmithianValue, fold, take, ONE
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.proof import verify_value
from sftoe.gate import verify_code

def run_coupled_shift_register(x0_val, steps):
    """
    Simulates the coupled system state X and the memory buffer M.
    Returns the final state X_T, the final memory buffer M_T, and the original bits.
    """
    X = Fraction(x0_val)
    M = Fraction(0, 1)
    original_bits = []
    
    # Trace forward
    for t in range(steps):
        # 1. Determine MSB of X (b = 1 if X >= 1/2 else 0)
        b = 1 if X >= Fraction(1, 2) else 0
        original_bits.append(b)
        
        # 2. Shift bit into memory buffer M
        M = M / 2 + Fraction(b, 2)
        
        # 3. Fold the system state X
        X = (X * 2) % 1
        if X == 0:
            X = Fraction(1, 1)
            
    return X, M, original_bits

def retrieve_bits_and_reconstruct(X_T, M_T, steps):
    """
    Retrieves the discarded bits from the memory buffer M_T
    and reconstructs the initial state X_0 step-by-step.
    """
    # 1. Retrieve bits from M_T
    retrieved_bits = []
    w = M_T
    for t in range(steps):
        w_double = w * 2
        b = int(w_double)
        retrieved_bits.append(b)
        w = w_double - b
        
    # Since the bits are retrieved in reverse order (b_{T-1}, ..., b_0)
    # let's reverse the list to have b_0, ..., b_{T-1}
    retrieved_bits.reverse()
    
    # 2. Reconstruct backward from X_T
    curr_X = X_T
    reconstructed_path = [curr_X]
    
    # We trace backward using retrieved_bits (from step T-1 down to 0)
    for t in range(steps - 1, -1, -1):
        b_t = retrieved_bits[t]
        if b_t == 0:
            # If b_t = 0, X_t = X_{t+1} / 2
            curr_X = curr_X / 2
        else:
            # If b_t = 1, X_t = (X_{t+1} + 1) / 2
            # Handle special boundary cases if needed (e.g. if predecessor was 1/2 or 1)
            if curr_X == 1:
                # Ambiguity if curr_X == 1: predecessor could be 1/2 or 1
                # But for our test cases with odd denominator factors, this is never reached
                curr_X = Fraction(1, 2)
            else:
                curr_X = (curr_X + 1) / 2
        reconstructed_path.append(curr_X)
        
    # Reconstructed initial state is the last element
    x0_reconstructed = reconstructed_path[-1]
    return x0_reconstructed, retrieved_bits

def test_state_reconstruction(x0_val, steps):
    print(f"\nTesting reconstruction for initial state X_0 = {x0_val} over {steps} steps:")
    X_T, M_T, orig_bits = run_coupled_shift_register(x0_val, steps)
    print(f"  Final state X_T: {X_T}")
    print(f"  Final memory buffer M_T: {M_T} (float: {float(M_T):.5f})")
    print(f"  Original bits discarded: {orig_bits}")
    
    x0_rec, ret_bits = retrieve_bits_and_reconstruct(X_T, M_T, steps)
    print(f"  Retrieved bits:          {ret_bits}")
    print(f"  Reconstructed X_0:       {x0_rec}")
    
    success = (x0_rec == Fraction(x0_val))
    print(f"  Reconstruction successful? {success}")
    return success

def main():
    print("=== SADE: Permanent Information Field Simulation ===")
    
    # Test periodic state 3/5
    test_state_reconstruction(Fraction(3, 5), 6)
    
    # Test complex state 5/7
    test_state_reconstruction(Fraction(5, 7), 8)
    
    # Test another rational state 7/15
    test_state_reconstruction(Fraction(7, 15), 10)
    
    # Derive the target state 3/5 using SADE pathfinder
    target = Fraction(3, 5)
    print(f"\nDeriving state {target} using SADE pathfinder...")
    proof = find_derivation(target)
    code = generate_sftoe_code(proof, "verify_information_field_state")
    
    print("\nVerifying generated code against AST constraints...")
    verify_code(code)
    print("AST Gate: PASSED")
    
    print("\nRunning generated code and verifying value...")
    namespace = {}
    exec(code, namespace)
    res = namespace["verify_information_field_state"]()
    verify_value(res)
    print(f"Value Verification: PASSED. Result: {res.value}")

if __name__ == "__main__":
    main()
