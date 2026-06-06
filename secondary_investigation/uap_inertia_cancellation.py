import sys
from fractions import Fraction
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.proof import verify_value
from sftoe.gate import verify_code

def main():
    # Low-inertia target coupling: 1/20
    target = Fraction(1, 20)
    print(f"Searching for derivation of UAP low-inertia state: {target}...")
    try:
        proof_node = find_derivation(target, max_depth=5, allowed_preimages=(2, 3, 5))
        print("Success! Derivation tree found:")
        print(proof_node)
        
        print("\nGenerating AST-compliant Python code...")
        code = generate_sftoe_code(proof_node, "verify_low_inertia_coupling")
        print(code)
        
        # Verify the code
        print("\nVerifying code structure against gate.py...")
        verify_code(code)
        print("AST Gate Verification: PASSED")
        
        # Execute and verify
        print("\nExecuting and verifying proof...")
        namespace = {}
        exec(code, namespace)
        res_val = namespace["verify_low_inertia_coupling"]()
        verify_value(res_val)
        print("Proof Verification: PASSED")
        print(f"Resulting Value: {res_val.value}")
        
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    main()
