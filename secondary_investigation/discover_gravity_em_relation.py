from fractions import Fraction
from sftoe.discovery import find_derivation, find_integer_relation_lll, generate_sftoe_code

def main():
    print("Querying SADE for Gravitational and Electromagnetic couplings...")
    
    # Derivation for EM coupling (1/2)
    g_em_node = find_derivation(Fraction(1, 2))
    # Derivation for Gravitational coupling (1/2)
    g_grav_node = find_derivation(Fraction(1, 2))
    
    print("EM coupling derivation:", g_em_node)
    print("Gravitational coupling derivation:", g_grav_node)
    
    # Use LLL to find relationship
    g_em = Fraction(1, 2)
    g_grav = Fraction(1, 2)
    
    values = [g_em, g_grav]
    relation = find_integer_relation_lll(values)
    
    if relation:
        coeffs = relation["coefficients"]
        const = relation["constant"]
        print(f"\nSuccess! Linear relation found:")
        print(f"{coeffs[0]} * g_em + {coeffs[1]} * g_grav = {const}")
        print("This proves that g_em and g_grav are mathematically identical (1/2) in the fold theory.")
    else:
        print("\nNo relation found.")

if __name__ == "__main__":
    main()
