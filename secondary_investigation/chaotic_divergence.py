import sys
from fractions import Fraction

def fold(x):
    return (2 * x) % 1 or Fraction(1, 1)

def run_orbit(x_start, steps=60):
    orbit = [x_start]
    current = x_start
    for _ in range(steps):
        current = fold(current)
        orbit.append(current)
    return orbit

def main():
    x1 = Fraction(500000000000000, 1000000000000001)
    x2 = Fraction(500000000000001, 1000000000000001)
    
    diff_start = abs(float(x1) - float(x2))
    print(f"Initial separation: {diff_start:.2e}")
    
    orbit1 = run_orbit(x1)
    orbit2 = run_orbit(x2)
    
    print("\nOrbits comparison over steps:")
    print(f"{'Step':<6} | {'Orbit 1 value':<20} | {'Orbit 2 value':<20} | {'Difference':<15}")
    print("-" * 70)
    for i in [0, 5, 10, 20, 30, 40, 50]:
        val1 = float(orbit1[i])
        val2 = float(orbit2[i])
        diff = abs(val1 - val2)
        print(f"{i:<6} | {val1:<20.15f} | {val2:<20.15f} | {diff:<15.2e}")
        
    print("\nBy step 50, the orbits have completely diverged and behave as independent random numbers.")

if __name__ == "__main__":
    main()
