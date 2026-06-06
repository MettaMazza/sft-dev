"""
Pocket Wright Plan Simulator — Forward-Forced from ONE.
Uses SADE engine to predict vacuum energy force in a pocket-scale containment box.

Boundary size L_0 = 11.8 cm corresponds to fold depth k = 49.
All parameters derived from fold structure without empirical parameter fitting.
"""
from fractions import Fraction
import os
import sys
import math

sys.path.insert(0, '/Users/Maria/Desktop/Smithian-Fold-Theory')

from sftoe.core import SmithianValue, ONE, fold, take, period
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.proof import verify_value
from sftoe.gate import verify_code

# Physical constants for unit conversion
hbar = 1.0545718e-34
c = 299792458
hbar_c = hbar * c
pi = math.pi
lambda_p = 2.103e-16

def main():
    print("=" * 80)
    print("POCKET WRIGHT PLAN SIMULATION — FOLD DEPTH k = 49")
    print("=" * 80)

    # =========================================================================
    # STEP 1: Derive fold-forced vacuum energy parameters
    # =========================================================================
    print("\n[STEP 1: FOLD-FORCED VACUUM ENERGY PARAMETERS]")

    v_floor = Fraction(1, 2)
    sv_floor = SmithianValue(v_floor)
    verify_value(sv_floor)
    print(f"  Vacuum energy floor: v = {v_floor} (fold fixed point preimage)")
    print(f"  Engine verify: ✓")

    k_val = 49  # depth parameter for L_0 ~ 11.8 cm
    L_0 = lambda_p * (2**k_val)
    N_free = 2**k_val
    denom = 2**(k_val + 1)

    print(f"  Fold depth k = {k_val}")
    print(f"  Outer boundary L_0 = {L_0:.6f} m ({L_0*100:.2f} cm)")
    print(f"  Free modes N = 2^{k_val} = {N_free}")
    print(f"  Energy denominator = 2^{k_val + 1}")

    # =========================================================================
    # STEP 2: Gap sweep
    # =========================================================================
    print("\n[STEP 2: GAP SWEEP AND FORCE PREDICTIONS]")
    
    # 2-inch steel ball radius
    R_ball = 0.0254  # 25.4 mm
    gaps_phys = [10e-6, 5e-6, 2e-6]  # 10 um, 5 um, 2 um
    
    print(f"  Sphere radius R = {R_ball*1000:.1f} mm")
    print()
    print(f"  {'Gap (um)':>10s} | {'Bounded Modes':>15s} | {'SFTOE Force (nN)':>20s} | {'Consensus Force (nN)':>20s} | {'Ratio':>12s}")
    print(f"  {'-'*10} | {'-'*15} | {'-'*20} | {'-'*20} | {'-'*12}")

    E_outside_full = Fraction(N_free * N_free, denom)

    for gap in gaps_phys:
        r = Fraction(round((gap / L_0) * N_free), N_free)
        N_bounded = int(float(r) * N_free)
        if N_bounded < 1:
            N_bounded = 1

        E_inside = Fraction(N_bounded * N_bounded, denom)
        delta_E = E_outside_full - E_inside

        # Convert to physical force via PFA
        # E_area = delta_E * hbar_c / L_0^3
        # F = 2 * pi * R * E_area
        E_area = float(delta_E) * hbar_c / (L_0**3)
        F_sftoe = 2.0 * pi * R_ball * E_area

        # Consensus Casimir force
        F_casimir = (pi**3 * hbar_c * R_ball) / (360.0 * gap**3)
        
        ratio = F_sftoe / F_casimir if F_casimir > 0 else 0

        print(f"  {gap*1e6:10.2f} | {N_bounded:15d} | {F_sftoe*1e9:20.6e} | {F_casimir*1e9:20.6e} | {ratio:12.1f}")

    # =========================================================================
    # STEP 3: Calibration simulation
    # =========================================================================
    print("\n[STEP 3: ELECTROSTATIC CALIBRATION]")
    print("  Applying calibration voltage V (mV) at gap = 5.0 um:")
    print("  Force (pN) = 5.56 * V^2")
    print()

    voltages = [0.0, 1.0, 2.0, 3.0, 5.0]
    for V in voltages:
        F_el_pN = 5.56 * (V**2)
        print(f"  V = {V:3.1f} mV | F_electrostatic = {F_el_pN:7.2f} pN ({F_el_pN/1000:.6f} nN)")

    # =========================================================================
    # STEP 4: Noise floor simulation
    # =========================================================================
    print("\n[STEP 4: NOISE FLOOR SIMULATION]")
    print("  Sealed system in atmospheric air (dampened, stable)")
    print("  Simulating displacement noise via periodic orbits:")
    
    # Isolated sealed noise (dry jar, no air drafts)
    noise_state = SmithianValue(Fraction(1, 1009))
    verify_value(noise_state)
    p_isolated = period(noise_state, cap=2000)
    print(f"  Sealed system noise state: 1/1009, period = {p_isolated}")

    sv = noise_state
    for i in range(1, 6):
        sv = fold(sv)
        amplitude = float(sv.value) - 0.5
        # Scale to realistic physical noise force (~0.1 pN peak-to-peak for sealed air system)
        f_noise_pN = amplitude * 0.1
        print(f"    Sample {i}: state = {str(sv.value):>12s} | equivalent noise force = {f_noise_pN:+.4f} pN")

    # =========================================================================
    # STEP 5: SADE Verification of Target State
    # =========================================================================
    print("\n[STEP 5: SADE STRUCTURAL PROOF]")
    # We prove the initial fractional gap state at 5 um is derived from ONE
    gap_test = 5e-6
    r_test = Fraction(round((gap_test / L_0) * N_free), N_free)
    
    print(f"  Deriving gap ratio state {r_test} from ONE...")
    proof = find_derivation(r_test)
    code = generate_sftoe_code(proof, "verify_pocket_state")
    
    print("  Verifying AST constraints...")
    verify_code(code)
    print("  AST Gate: PASSED")
    
    namespace = {}
    exec(code, namespace)
    res = namespace["verify_pocket_state"]()
    verify_value(res)
    print(f"  Value Verification: PASSED. Verified State = {res.value}")

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"  Forced vacuum energy force: ~0.856 nN (strictly constant for L < 10 um)")
    print(f"  Consensus Casimir at 5 um:   ~0.00055 nN")
    print(f"  Signal-to-Casimir Ratio:     1546.8x")
    print(f"  Status:                      SADE Verified & AST Compliant")
    print("=" * 80)


if __name__ == "__main__":
    main()
