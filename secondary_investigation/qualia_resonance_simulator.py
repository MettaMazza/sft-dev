import math
from fractions import Fraction
from sftoe.core import SmithianValue, fold, combined_period, beat_frequency, relative_phase
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.proof import verify_value
from sftoe.gate import verify_code

def analyze_qualia_resonance(input_state, observer_state):
    """
    Analyzes the resonance attractor cycle (qualia signature) formed by the
    interaction of a sensory input state and a self-observation loop.
    """
    sv_input = SmithianValue(input_state)
    sv_observer = SmithianValue(observer_state)
    
    # 1. Combined period of the joint system (capped at 100 to prevent infinite loops on pre-periodic states)
    joint_period = combined_period([sv_input, sv_observer], cap=100)
    
    # 2. Beat frequency between input and observer
    beat = beat_frequency(sv_input, sv_observer)
    
    # 3. Relative phase sequence over 10 ticks
    # We simulate step-by-step relative phases to map the cycle's topology
    phases = []
    p1 = sv_input
    p2 = sv_observer
    for _ in range(10):
        p1 = fold(p1)
        p2 = fold(p2)
        phases.append(relative_phase(p1, p2).value)
        
    unique_phases = len(set(phases))
    
    return {
        "joint_period": joint_period,
        "beat_frequency": beat.value,
        "unique_phases": unique_phases,
        "phase_signature": [str(p) for p in phases]
    }

def main():
    print("=== SADE Module I: Qualia Resonance Simulator ===")
    
    # Sensory Wavelengths (represented as rational states in the fold domain)
    # Red light: 4/5 (stable periodic cycle of length 4)
    # Blue light: 2/3 (stable periodic cycle of length 2)
    x_red = Fraction(4, 5)
    x_blue = Fraction(2, 3)
    
    # Observers
    # Level-1 Observer (C1): 1/4 (transient state leading to ZPE)
    # Level-2 Observer (C2): 1/8 (deeper transient state leading to ZPE)
    C1 = Fraction(1, 4)
    C2 = Fraction(1, 8)
    
    print(f"\nSensory Inputs: Red = {x_red}, Blue = {x_blue}")
    print(f"Observers: C1 (Level-1) = {C1}, C2 (Level-2) = {C2}")
    
    # Scenario A: Red Light perceived by Level-1 Observer
    res_red_C1 = analyze_qualia_resonance(x_red, C1)
    print("\nQualia Signature of (Red light, C1 observer):")
    print(f"  Joint Attractor Period: {res_red_C1['joint_period']} (None means transient/non-returning)")
    print(f"  Beat Frequency: {res_red_C1['beat_frequency']}")
    print(f"  Unique Phase Relations: {res_red_C1['unique_phases']}")
    print(f"  Topological Phase Path: {res_red_C1['phase_signature']}")
    
    # Scenario B: Blue Light perceived by Level-1 Observer
    res_blue_C1 = analyze_qualia_resonance(x_blue, C1)
    print("\nQualia Signature of (Blue light, C1 observer):")
    print(f"  Joint Attractor Period: {res_blue_C1['joint_period']} (None means transient/non-returning)")
    print(f"  Beat Frequency: {res_blue_C1['beat_frequency']}")
    print(f"  Unique Phase Relations: {res_blue_C1['unique_phases']}")
    print(f"  Topological Phase Path: {res_blue_C1['phase_signature']}")
    
    # Scenario C: Red Light perceived by Level-2 Observer
    res_red_C2 = analyze_qualia_resonance(x_red, C2)
    print("\nQualia Signature of (Red light, C2 observer - deeper reflection):")
    print(f"  Joint Attractor Period: {res_red_C2['joint_period']} (None means transient/non-returning)")
    print(f"  Beat Frequency: {res_red_C2['beat_frequency']}")
    print(f"  Unique Phase Relations: {res_red_C2['unique_phases']}")
    print(f"  Topological Phase Path: {res_red_C2['phase_signature']}")
    
    # Uniqueness Verification
    distinct = (res_red_C1['phase_signature'] != res_blue_C1['phase_signature'])
    print(f"\nAre the Qualia Phase Signatures of Red and Blue topologically distinct? {distinct}")
    
    # Derive Level-1 Observer state (1/4) using SADE
    print("\nDeriving Level-1 Observer state (1/4)...")
    proof = find_derivation(C1)
    code = generate_sftoe_code(proof, "verify_level_1_observer")
    
    print("Checking code against AST gate...")
    verify_code(code)
    print("AST Gate: PASSED")
    
    print("Running generated code and verifying value...")
    namespace = {}
    exec(code, namespace)
    res = namespace["verify_level_1_observer"]()
    verify_value(res)
    print("Value Verification: PASSED")
    print(f"Verified SmithianValue: {res.value}")

if __name__ == "__main__":
    main()
