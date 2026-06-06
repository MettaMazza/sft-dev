import math
from fractions import Fraction
from sftoe.core import SmithianValue, fold, take, ONE
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.proof import verify_value
from sftoe.gate import verify_code

def simulate_synthetic_ctc(x0_val, loop_steps):
    """
    Simulates a synthetic Closed Timelike Curve for transient states.
    For x0_val = 1/4, it folds forward for 1 step (to 1/2), storing the bit in M.
    At step 2, it reads the bit from M to perform a guided reverse step, returning to 1/4.
    It runs this cycle for the specified number of loop steps.
    """
    X = Fraction(x0_val)
    print(f"\nStabilizing transient state X_0 = {X} into a synthetic CTC:")
    
    trajectory = [X]
    M = Fraction(0, 1)
    
    # We run 3 full cycles of the loop (forward-backward-forward-backward...)
    for cycle in range(loop_steps):
        # 1. Forward step (fold and record bit)
        b = 1 if X >= Fraction(1, 2) else 0
        # record bit in memory buffer
        M = Fraction(b, 2)
        X = (X * 2) % 1
        if X == 0:
            X = Fraction(1, 1)
        trajectory.append(X)
        print(f"  Cycle {cycle + 1} - Forward:  State = {X}, Buffer M = {M}")
        
        # 2. Backward step (retrieve bit from M and rewind)
        # retrieve bit
        b_ret = int(M * 2)
        if b_ret == 0:
            X = X / 2
        else:
            if X == 1:
                X = Fraction(1, 2)
            else:
                X = (X + 1) / 2
        trajectory.append(X)
        print(f"  Cycle {cycle + 1} - Backward: State = {X} (Rewound to past!)")
        
    print(f"Full trajectory: {' -> '.join(str(v) for v in trajectory)}")
    success = (trajectory[0] == trajectory[-1])
    print(f"Is the transient state successfully stabilized in a closed causal loop? {success}")
    return success

def main():
    print("=== SADE: Transient Closed Timelike Curves ===")
    
    # Simulate synthetic time loop for 1/4
    simulate_synthetic_ctc(Fraction(1, 4), 3)
    
    # Derive starting state 1/4 using SADE pathfinder
    target = Fraction(1, 4)
    print(f"\nDeriving state {target} using SADE pathfinder...")
    proof = find_derivation(target)
    code = generate_sftoe_code(proof, "verify_transient_loop_state")
    
    print("\nVerifying generated code against AST constraints...")
    verify_code(code)
    print("AST Gate: PASSED")
    
    print("\nRunning generated code and verifying value...")
    namespace = {}
    exec(code, namespace)
    res = namespace["verify_transient_loop_state"]()
    verify_value(res)
    print(f"Value Verification: PASSED. Result: {res.value}")

if __name__ == "__main__":
    main()
