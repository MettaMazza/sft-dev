import math
from fractions import Fraction
from sftoe.core import SmithianValue, fold, take, period, combined_period, beat_frequency, run_wave
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.proof import verify_value
from sftoe.gate import verify_code

def simulate_ghost_interaction(ghost_val, observer_val):
    g = SmithianValue(ghost_val)
    o = SmithianValue(observer_val)
    
    print(f"\nSimulating Ghost ({g.value}) and Living Observer ({o.value}) interaction:")
    
    # 1. Periods
    g_per = period(g)
    o_per = period(o)
    joint_per = combined_period([g, o], cap=100)
    print(f"  Ghost periodic orbit length: {g_per}")
    print(f"  Observer periodic orbit length: {o_per}")
    print(f"  Joint system combined period: {joint_per}")
    
    # 2. Beat Frequency (the coupling field)
    beat = beat_frequency(g, o)
    print(f"  Interferometric Beat Frequency (coupling field): {beat.value}")
    
    # 3. Wave dynamics (10 ticks)
    rel_phases = run_wave(g, o, 10)
    print(f"  Relative Phase timeline:")
    for i, phase in enumerate(rel_phases):
        print(f"    Tick {i+1}: relative phase = {phase.value}")
        
    return beat.value

def main():
    print("=== SADE Topic E4: Ghosts & Residual Orbits ===")
    
    # Model a host S = 7/24 (transient k=3, periodic d=3)
    host = Fraction(7, 24)
    print(f"Host state S: {host}")
    
    # Decay of transient (Death)
    curr = host
    print("Simulating life-to-death transient clearing:")
    for step in range(4):
        curr = (curr * 2) % 1
        if curr == 0: curr = Fraction(1, 1)
        print(f"  Step {step + 1}: {curr}")
        
    # The persistent core is 1/3 <-> 2/3 (Ghost)
    print("\nThe transient cleared. The invariant periodic core (Ghost) persists.")
    
    # Simulate interaction between ghost 1/3 and observer 1/5
    beat_val = simulate_ghost_interaction(Fraction(1, 3), Fraction(1, 5))
    
    # Derive the interaction beat channel 1/15 (as beat is 2/15, 1/15 is its basis)
    target = Fraction(1, 15)
    print(f"\nDeriving interaction resonance base {target} using SADE pathfinder...")
    proof = find_derivation(target)
    code = generate_sftoe_code(proof, "verify_ghost_channel")
    
    print("\nVerifying generated code against AST constraints...")
    verify_code(code)
    print("AST Gate: PASSED")
    
    print("\nRunning generated code and verifying value...")
    namespace = {}
    exec(code, namespace)
    res = namespace["verify_ghost_channel"]()
    verify_value(res)
    print(f"Value Verification: PASSED. Result: {res.value}")

if __name__ == "__main__":
    main()
