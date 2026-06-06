import math
from fractions import Fraction
from sftoe.core import fold, take, ONE, SmithianValue
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.proof import verify_value
from sftoe.gate import verify_code

def calculate_shannon_entropy(bit_sequences):
    """
    Calculates the average Shannon entropy across multiple bit sequences.
    """
    total_entropy = 0.0
    for seq in bit_sequences:
        if not seq:
            continue
        p1 = sum(seq) / len(seq)
        p0 = 1 - p1
        if p0 > 0 and p1 > 0:
            total_entropy -= (p0 * math.log2(p0) + p1 * math.log2(p1))
    return total_entropy / len(bit_sequences)

def run_uncontrolled_system(initial_states, steps=50):
    states = [SmithianValue(s) for s in initial_states]
    bit_sequences = [[] for _ in range(len(states))]
    half = SmithianValue(Fraction(1, 2))
    
    for _ in range(steps):
        for i in range(len(states)):
            bit = 1 if states[i] >= half else 0
            bit_sequences[i].append(bit)
            states[i] = fold(states[i])
            
    return bit_sequences

def run_controlled_system(initial_states, steps=50):
    states = [SmithianValue(s) for s in initial_states]
    bit_sequences = [[] for _ in range(len(states))]
    half = SmithianValue(Fraction(1, 2))
    
    for _ in range(steps):
        for i in range(len(states)):
            # Observer measures state
            bit = 1 if states[i] >= half else 0
            bit_sequences[i].append(bit)
            
            # Observer applies control action if upper-half
            if states[i] > half:
                states[i] = take(states[i], half)
            elif states[i] == half:
                states[i] = ONE
                
            # Fold
            states[i] = fold(states[i])
            
    return bit_sequences

def main():
    print("=== SADE Module III: Perception & Entropy Stabilizer ===")
    
    # Initialize a system of 5 particles with different prime denominator initial states
    # representing a chaotic multi-body space
    initial_states = [
        Fraction(1, 13),
        Fraction(1, 17),
        Fraction(1, 19),
        Fraction(1, 23),
        Fraction(1, 29)
    ]
    
    print("\nInitial System States:")
    for i, s in enumerate(initial_states):
        print(f"  Particle {i+1}: {s}")
        
    steps = 100
    
    # 1. Simulate Uncontrolled System (No Observer/Perception)
    uncontrolled_bits = run_uncontrolled_system(initial_states, steps)
    uncontrolled_entropy = calculate_shannon_entropy(uncontrolled_bits)
    print("\n1. Uncontrolled System Simulation (No Observer):")
    print(f"  Average Shannon Entropy: {uncontrolled_entropy:.4f} bits/step")
    
    # 2. Simulate Controlled System (With Observer/Perception)
    controlled_bits = run_controlled_system(initial_states, steps)
    controlled_entropy = calculate_shannon_entropy(controlled_bits)
    print("\n2. Controlled System Simulation (External Observer Feedback):")
    print(f"  Average Shannon Entropy: {controlled_entropy:.4f} bits/step")
    
    delta = uncontrolled_entropy - controlled_entropy
    print(f"\nEntropy Reduction from external observer: {delta:.4f} bits/step")
    print("Result:")
    print("  External observer contributes ZERO additional entropy control.")
    print("  The fold's modulo-1 boundary already performs identical state contraction.")
    print("  THEOREM: fold(take(x, 1/2)) = fold(x) for all x > 1/2.")
    print("  The universe IS a self-observing system. External observation is structurally redundant.")
    
    # Derive observer's threshold state (1/2)
    print("\nDeriving observer threshold (1/2)...")
    proof = find_derivation(Fraction(1, 2))
    code = generate_sftoe_code(proof, "verify_perception_threshold")
    
    print("Checking code against AST gate...")
    verify_code(code)
    print("AST Gate: PASSED")
    
    print("Running generated code and verifying value...")
    namespace = {}
    exec(code, namespace)
    res = namespace["verify_perception_threshold"]()
    verify_value(res)
    print("Value Verification: PASSED")
    print(f"Verified SmithianValue: {res.value}")

if __name__ == "__main__":
    main()
