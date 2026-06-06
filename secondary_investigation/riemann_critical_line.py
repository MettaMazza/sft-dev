from fractions import Fraction
from sftoe.discovery import find_derivation, find_integer_relation_lll, generate_sftoe_code
from sftoe.proof import verify_value
from sftoe.gate import verify_code

def main():
    print("=== SADE Riemann Critical Line & Force Relations ===")
    
    # 1. Critical line is 1/2
    critical_line = Fraction(1, 2)
    print(f"Critical Line State: {critical_line}")
    
    # Derive 1/2 using SADE
    proof_node = find_derivation(critical_line)
    print("Derivation Tree:", proof_node)
    
    code = generate_sftoe_code(proof_node, "verify_critical_line")
    print("\nGenerated AST-Compliant Code:\n", code)
    
    verify_code(code)
    print("AST Gate: PASSED")
    
    # 2. Find relations between Riemann critical line and prime force couplings
    g2 = Fraction(1, 2)   # Electroweak (2)
    g3 = Fraction(2, 3)   # Strong (3)
    g5 = Fraction(4, 5)   # Prime-5 Force
    g7 = Fraction(6, 7)   # Prime-7 Force
    
    values = [critical_line, g2, g3, g5, g7]
    names = ["Critical Line (1/2)", "g_2 (1/2)", "g_3 (2/3)", "g_5 (4/5)", "g_7 (6/7)"]
    
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
        
        val_sum = sum(c * v for c, v in zip(coeffs, values))
        print(f"Verification: sum = {val_sum} (expected {const})")
    else:
        print("\nNo relations found between Riemann line and forces.")

if __name__ == "__main__":
    main()
