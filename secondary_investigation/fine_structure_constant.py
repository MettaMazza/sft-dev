import sys
from fractions import Fraction
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.proof import verify_value, verify_hypothesis_orbit
from sftoe.gate import verify_code

def main():
    # Fine structure constant coupling: 250 / 34259 (~ 1 / 137.036)
    target = Fraction(250, 34259)
    print(f"Searching for derivation of the Fine Structure Constant alpha: {target}...")
    try:
        # Since 34259 is prime, let's verify its orbit first to make sure it converges
        print("Checking target doubling orbit periodicity...")
        orbit_info = verify_hypothesis_orbit(target, max_steps=40000)
        print(f"Target orbit verified! Cycle length: {orbit_info['cycle_length']}")
        
        # Run SADE search (allowing 34259 as a preimage/hypothesis prime)
        proof_node = find_derivation(target, max_depth=5, allowed_preimages=(2, 3, 5, 34259))
        print("Success! Derivation tree found:")
        print(proof_node)
        
        print("\nGenerating AST-compliant Python code...")
        code = generate_sftoe_code(proof_node, "verify_fine_structure_constant_sade")
        print(code)
        
        print("\nVerifying code structure against gate.py...")
        verify_code(code)
        print("AST Gate Verification: PASSED")
        
        print("\nExecuting and verifying proof...")
        namespace = {}
        exec(code, namespace)
        res_val = namespace["verify_fine_structure_constant_sade"]()
        verify_value(res_val)
        print("Proof Verification: PASSED")
        print(f"Resulting Value: {res_val.value} (~ 1 / {1.0 / float(res_val.value):.6f})")
        
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    main()
