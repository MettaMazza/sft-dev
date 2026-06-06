from fractions import Fraction
from sftoe.discovery import find_derivation, find_integer_relation_lll, query
from sftoe.core import fold

def main():
    print("=== SADE Fringe Science Investigation ===")
    
    # 1. Biefeld-Brown (Electro-Gravitic Coupling)
    print("\n1. Biefeld-Brown Coupling:")
    g_em = Fraction(1, 2)
    g_grav = Fraction(1, 2)
    relation_bb = find_integer_relation_lll([g_em, g_grav])
    print(f"Discovered relation: {relation_bb['coefficients'][0]} * g_em + {relation_bb['coefficients'][1]} * g_grav = {relation_bb['constant']}")
    
    # 2. EMDrive Resonant Cavity Asymmetry
    print("\n2. EMDrive Resonant Cavity Asymmetry:")
    # We model the asymmetric cavity ends as the m=2 and m=3 sector couplings
    end1 = Fraction(1, 2)
    end2 = Fraction(1, 3)
    asymmetry = end1 - end2 # 1/6
    print(f"Cavity asymmetry (1/2 - 1/3): {asymmetry}")
    # Discover derivation for 1/6
    res_emdrive = query(target_float=float(asymmetry), tolerance=1e-6)
    print("Derivation for asymmetry fraction:", res_emdrive["fraction"])
    print("Derivation tree:", res_emdrive["proof_tree"])
    
    # 3. Water Memory (Dilution Invariance under Fold)
    print("\n3. Water Memory / Dilution Invariance:")
    # Start with a 3-sector state (1/3) which has period 2 (1/3 -> 2/3 -> 1/3)
    start_state = Fraction(1, 3)
    print(f"Original state: {start_state}, fold period = 2")
    
    # Dilute it 4 times by a factor of 2 (multiplied by 1/16)
    diluted = start_state / 16 # 1/48
    print(f"Diluted state (1/48): {diluted}")
    
    # Trace the fold orbit of the diluted state
    curr = diluted
    print("Folding diluted state:")
    for step in range(1, 8):
        # fold: (2 * curr) % 1 (with 0 -> 1)
        curr = (2 * curr) % 1
        if curr == 0:
            curr = Fraction(1, 1)
        print(f"  Step {step}: {curr}")
        
    print(f"After 4 dilution-clearing steps, did it return to the 1/3 periodic orbit? {curr in [Fraction(1,3), Fraction(2,3)]}")

if __name__ == "__main__":
    main()
