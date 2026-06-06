import math
from fractions import Fraction
from sftoe.core import SmithianValue, fold, take, ONE
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.proof import verify_value
from sftoe.gate import verify_code

def run_forward(x0_val, T):
    X = Fraction(x0_val)
    M = Fraction(0, 1)
    trajectory = [X]
    
    for t in range(T):
        b = 1 if X >= Fraction(1, 2) else 0
        M = M / 2 + Fraction(b, 2)
        X = (X * 2) % 1
        if X == 0:
            X = Fraction(1, 1)
        trajectory.append(X)
        
    return X, M, trajectory

def retrieve_past_state(X_T, M_T, T, t_target):
    """
    Reconstructs the system state at t_target (0 <= t_target <= T)
    using only X_T, M_T, T.
    """
    # 1. Extract bits from memory buffer
    w = M_T
    bits = []
    for _ in range(T):
        w_double = w * 2
        b = int(w_double)
        bits.append(b)
        w = w_double - b
    bits.reverse() # In order: b_0, b_1, ..., b_{T-1}
    
    # 2. Reconstruct backward from T down to t_target
    curr_X = X_T
    for step in range(T - 1, t_target - 1, -1):
        b_step = bits[step]
        if b_step == 0:
            curr_X = curr_X / 2
        else:
            if curr_X == 1:
                curr_X = Fraction(1, 2)
            else:
                curr_X = (curr_X + 1) / 2
                
    return curr_X

def main():
    print("=== SADE: Temporal Retrieval Engine ===")
    
    # Starting state X_0 = 17/30 (complex rational state)
    x0 = Fraction(17, 30)
    T = 12
    t_target = 5
    
    print(f"Initial State X_0: {x0}")
    print(f"Running system forward for T = {T} steps...")
    
    X_T, M_T, trajectory = run_forward(x0, T)
    print(f"Final State X_{T}: {X_T}")
    print(f"Final Memory State M_{T}: {M_T}")
    
    print(f"\nQuerying the past state at step t = {t_target}...")
    x_retrieved = retrieve_past_state(X_T, M_T, T, t_target)
    x_actual = trajectory[t_target]
    
    print(f"  Retrieved state: {x_retrieved}")
    print(f"  Actual state:    {x_actual}")
    
    success = (x_retrieved == x_actual)
    print(f"  Temporal retrieval successful? {success}")
    
    # Derive the starting state 17/30 using SADE pathfinder
    target = Fraction(17, 30)
    print(f"\nDeriving state {target} using SADE pathfinder...")
    proof = find_derivation(target)
    code = generate_sftoe_code(proof, "verify_temporal_engine_state")
    
    print("\nVerifying generated code against AST constraints...")
    verify_code(code)
    print("AST Gate: PASSED")
    
    print("\nRunning generated code and verifying value...")
    namespace = {}
    exec(code, namespace)
    res = namespace["verify_temporal_engine_state"]()
    verify_value(res)
    print(f"Value Verification: PASSED. Result: {res.value}")

if __name__ == "__main__":
    main()
