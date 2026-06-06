import math
from fractions import Fraction
from sftoe.core import SmithianValue, fold, take
from sftoe.discovery import find_derivation, generate_sftoe_code, find_integer_relation_lll
from sftoe.proof import verify_value
from sftoe.gate import verify_code

def main():
    print("=== SADE Topic A1: Quantum Gravity Unification ===")
    
    # 1. Define couplings
    g_gravity = Fraction(1, 2)  # p=2 sector
    g_qm = Fraction(2, 3)       # p=3 sector
    
    print(f"Gravity coupling constant (g_gravity): {g_gravity}")
    print(f"QM coupling constant (g_qm): {g_qm}")
    
    # 2. Find integer relation using LLL
    print("\nFinding integer relation between couplings using LLL...")
    relation = find_integer_relation_lll([g_gravity, g_qm])
    if relation:
        coeffs = relation["coefficients"]
        const = relation["constant"]
        print(f"Discovered LLL relation: {coeffs[0]} * g_gravity + {coeffs[1]} * g_qm = {const}")
    else:
        print("No integer relation discovered.")
        
    # 3. Derive QM coupling constant (2/3) from ONE using SADE pathfinder
    print(f"\nDeriving g_qm ({g_qm}) from ONE...")
    proof = find_derivation(g_qm)
    code = generate_sftoe_code(proof, "verify_gravity_qm_relation")
    
    print("\nVerifying AST constraints...")
    verify_code(code)
    print("AST Gate: PASSED")
    
    print("\nRunning generated code and verifying value...")
    namespace = {}
    exec(code, namespace)
    res = namespace["verify_gravity_qm_relation"]()
    verify_value(res)
    print("Value Verification: PASSED")
    print(f"Verified SmithianValue: {res.value}")

if __name__ == "__main__":
    main()
