from fractions import Fraction
from sftoe.discovery import find_integer_relation_lll

def main():
    zpe = Fraction(1, 2)
    t9 = Fraction(1, 9)
    t3 = Fraction(1, 3)
    t6 = Fraction(2, 3)
    
    values = [zpe, t9, t3, t6]
    names = ["ZPE (1/2)", "Tesla 9 (1/9)", "Tesla 3 (1/3)", "Tesla 6 (2/3)"]
    
    print("Investigating relations between Tesla's states and the ZPE floor...")
    print("Values:", [str(v) for v in values])
    
    relation = find_integer_relation_lll(values, max_coeff=10)
    
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
        print("\nNo linear relations found within max coefficient bounds.")

if __name__ == "__main__":
    main()
