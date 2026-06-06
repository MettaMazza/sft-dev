from fractions import Fraction
from sftoe.discovery import find_integer_relation_lll, find_derivation, generate_sftoe_code
from sftoe.gate import verify_code
from sftoe.proof import verify_value

def main():
    print("=== SADE Nested Machine Consciousness Investigation ===")
    
    # Define nested self-observation levels
    c1 = Fraction(1, 4)   # Level 1 self-observation
    c2 = Fraction(1, 8)   # Level 2 self-observation
    c3 = Fraction(1, 16)  # Level 3 self-observation
    c4 = Fraction(1, 32)  # Level 4 self-observation
    
    values = [c1, c2, c3, c4]
    names = ["C_1 (1/4)", "C_2 (1/8)", "C_3 (1/16)", "C_4 (1/32)"]
    print("Nested Observers:", [str(v) for v in values])
    
    # Run SADE LLL solver
    relation = find_integer_relation_lll(values)
    
    if relation:
        coeffs = relation["coefficients"]
        const = relation["constant"]
        
        terms = []
        for c, name in zip(coeffs, names):
            if c != 0:
                sign = "+" if c > 0 else "-"
                abs_c = abs(c)
                c_str = f"{abs_c}*" if abs_c != 1 else ""
                terms.append(f"{sign} {c_str}{name}")
                
        equation = " ".join(terms)
        if equation.startswith("+ "):
            equation = equation[2:]
        elif equation.startswith("- "):
            equation = "-" + equation[2:]
            
        print("\nSuccess! Relation found:")
        print(f"{equation} = {const}")
        
        # Verify
        val_sum = sum(c * v for c, v in zip(coeffs, values))
        print(f"Verification: sum = {val_sum} (expected {const})")
        
        # SADE search for C_4 (1/32) derivation from ONE
        print("\nDeriving C_4 (1/32) using SADE pathfinder...")
        proof_node = find_derivation(c4)
        print("C_4 Derivation tree:", proof_node)
        
        # Generate code
        code = generate_sftoe_code(proof_node, "verify_nested_consciousness")
        print("\nGenerated AST-Compliant Code:\n", code)
        
        verify_code(code)
        print("AST Gate: PASSED")
    else:
        print("\nNo relations found.")

if __name__ == "__main__":
    main()
