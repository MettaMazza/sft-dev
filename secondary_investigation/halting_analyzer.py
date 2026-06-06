import math
from fractions import Fraction
from sftoe.core import fold

def analyze_halting(p, q):
    """
    Decides the halting status of a program state p/q under the doubling fold.
    Returns a dictionary with status, steps to halt or cycle period, and details.
    """
    frac = Fraction(p, q)
    if not (0 < frac <= 1):
        raise ValueError("Program state must be in the SFTOE domain (0, 1]")
        
    num = frac.numerator
    den = frac.denominator
    
    # 1. Check if denominator is a power of 2
    # If den = 2^k, it halts. We find k.
    if (den & (den - 1)) == 0:
        k = int(math.log2(den))
        return {
            "status": "HALTS",
            "steps": k,
            "details": f"Denominator {den} is 2^{k}. The program halts (reaches ONE) in exactly {k} steps."
        }
        
    # 2. Denominator has odd factors. It never halts.
    # It enters a periodic cycle. We compute the pre-period steps and cycle length.
    # We factor den = 2^k * d where d is odd.
    temp_den = den
    k = 0
    while temp_den % 2 == 0:
        temp_den //= 2
        k += 1
    d = temp_den # odd part
    
    # The period L is the order of 2 modulo d: 2^L = 1 (mod d)
    # Since d is odd, 2 is coprime to d, so L always exists.
    L = 1
    val = 2 % d
    while val != 1:
        val = (val * 2) % d
        L += 1
        
    return {
        "status": "NEVER HALTS (RUNS FOREVER)",
        "pre_period_steps": k,
        "cycle_length": L,
        "details": f"Denominator {den} = 2^{k} * {d} (odd). The program enters a periodic cycle of length {L} after {k} pre-period steps."
    }

def print_orbit(frac, max_steps=12):
    print(f"Orbit of {frac}:")
    curr = frac
    for step in range(1, max_steps + 1):
        curr = fold(curr)
        print(f"  Step {step}: {curr}")
        if curr == Fraction(1, 1):
            print("  [Halted]")
            break

def main():
    print("=== SADE Halting Problem Analyzer ===")
    
    # Program A: p/q = 1/16 (denominator is power of 2)
    p1, q1 = 1, 16
    print(f"\nAnalyzing Program A: {p1}/{q1}")
    res1 = analyze_halting(p1, q1)
    print("Decision:", res1["status"])
    print("Details:", res1["details"])
    print_orbit(Fraction(p1, q1))
    
    # Program B: p/q = 1/24 (denominator has odd factors: 2^3 * 3)
    p2, q2 = 1, 24
    print(f"\nAnalyzing Program B: {p2}/{q2}")
    res2 = analyze_halting(p2, q2)
    print("Decision:", res2["status"])
    print("Details:", res2["details"])
    print_orbit(Fraction(p2, q2))

if __name__ == "__main__":
    main()
