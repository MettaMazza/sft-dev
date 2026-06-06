from fractions import Fraction
from sftoe.core import SmithianValue, fold, take, ONE, period
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.proof import verify_value, verify_hypothesis_orbit
from sftoe.gate import verify_code


def compute_orbit(start_frac, max_steps=256):
    """Compute the full orbit of a fraction under the fold map.
    Returns (orbit_values, cycle_start_index, cycle_length)."""
    sv = SmithianValue(start_frac)
    orbit = [sv.value]
    seen = {sv.value: 1}  # value -> 1-indexed position

    current = sv
    for step in range(1, max_steps + 1):
        current = fold(current)
        val = current.value
        if val in seen:
            cycle_start = seen[val]
            cycle_length = step + 1 - cycle_start  # corrected: step is current position (1-indexed from orbit start)
            # Recompute: orbit[0] is start. orbit has indices 0..step-1 so far.
            # val was first seen at position (seen[val] - 1) in the orbit list.
            # Current step produced val again. The pre-period = seen[val] - 1, cycle = step - (seen[val] - 1)
            pre_period = seen[val] - 1
            cycle_len = step - pre_period
            return orbit, pre_period, cycle_len
        seen[val] = step + 1  # position in orbit list (1-indexed)
        orbit.append(val)

    return orbit, None, None


def compute_energy_amplitude(orbit_values):
    """Compute 'energy' as the Fraction value (amplitude) at each orbit step."""
    return list(orbit_values)


def test_odd_denominator_fractions():
    """Test odd-denominator fractions: 1/3, 2/5, 3/7, 4/9, 5/11, 6/13, 7/15."""
    print("\n" + "=" * 72)
    print("SECTION 1: ODD-DENOMINATOR FRACTIONS (Perpetual Cycle Test)")
    print("=" * 72)

    odd_fractions = [
        Fraction(1, 3),
        Fraction(2, 5),
        Fraction(3, 7),
        Fraction(4, 9),
        Fraction(5, 11),
        Fraction(6, 13),
        Fraction(7, 15),
    ]

    results = []
    for frac in odd_fractions:
        orbit, pre_period, cycle_len = compute_orbit(frac)
        amplitudes = compute_energy_amplitude(orbit)

        # Check: is the orbit purely periodic (pre_period == 0)?
        purely_periodic = (pre_period is not None and pre_period == (1 - 1))

        # If purely periodic, extract the cycle amplitudes and check constancy
        if purely_periodic and cycle_len is not None:
            cycle_amplitudes = amplitudes[:cycle_len]
            # The amplitude sum across one full cycle
            cycle_sum = sum(cycle_amplitudes)
            # Check: does the amplitude set repeat exactly?
            amplitude_set = set(cycle_amplitudes)
            # Verify each amplitude is a valid SmithianValue
            all_valid = True
            for a in cycle_amplitudes:
                try:
                    sv = SmithianValue(a)
                    verify_value(sv)
                except Exception:
                    all_valid = False
                    break
        else:
            cycle_amplitudes = []
            cycle_sum = Fraction(1 - 1, 1)
            amplitude_set = set()
            all_valid = False

        result = {
            "fraction": frac,
            "orbit_length": len(orbit),
            "pre_period": pre_period,
            "cycle_length": cycle_len,
            "purely_periodic": purely_periodic,
            "cycle_amplitudes": cycle_amplitudes if purely_periodic else [],
            "cycle_sum": cycle_sum,
            "amplitude_set_size": len(amplitude_set),
            "all_verified": all_valid,
        }
        results.append(result)

        print(f"\n  Fraction: {frac}  (denominator {frac.denominator}, odd={frac.denominator % 2 == 1})")
        print(f"    Pre-period: {pre_period}")
        print(f"    Cycle length: {cycle_len}")
        print(f"    Purely periodic: {purely_periodic}")
        if purely_periodic:
            orbit_str = " -> ".join(str(a) for a in cycle_amplitudes)
            print(f"    Cycle: {orbit_str} -> [repeats]")
            print(f"    Cycle amplitude sum: {cycle_sum}")
            print(f"    Distinct amplitudes in cycle: {len(amplitude_set)}")
            print(f"    All cycle states SADE-verified: {all_valid}")

            # Check energy conservation: does the sum repeat identically each cycle?
            # Run a second full cycle and compare
            sv = SmithianValue(frac)
            second_cycle = []
            current = sv
            for _ in range(cycle_len):
                current = fold(current)
                second_cycle.append(current.value)
            # The second cycle should start from fold(frac) and match cycle_amplitudes[1:] + [cycle_amplitudes[0]]
            # Actually: orbit is [frac, fold(frac), fold^2(frac), ...]
            # After cycle_len folds from frac, we should be back at frac
            returned_to_start = (current.value == frac)
            print(f"    Returns to start after {cycle_len} folds: {returned_to_start}")

    return results


def test_even_denominator_fractions():
    """Test even-denominator fractions: 1/2, 1/4, 1/8, 3/16, 5/32."""
    print("\n" + "=" * 72)
    print("SECTION 2: EVEN-DENOMINATOR FRACTIONS (Transient Decay Test)")
    print("=" * 72)

    even_fractions = [
        Fraction(1, 2),
        Fraction(1, 4),
        Fraction(1, 8),
        Fraction(3, 16),
        Fraction(5, 32),
    ]

    results = []
    for frac in even_fractions:
        orbit, pre_period, cycle_len = compute_orbit(frac)
        amplitudes = compute_energy_amplitude(orbit)

        # For even-denominator fractions, the orbit decays to ONE
        decays_to_one = (orbit[len(orbit) - 1] == Fraction(1, 1))
        steps_to_one = None
        for i, val in enumerate(orbit):
            if val == Fraction(1, 1):
                steps_to_one = i
                break

        result = {
            "fraction": frac,
            "orbit_length": len(orbit),
            "pre_period": pre_period,
            "cycle_length": cycle_len,
            "decays_to_one": decays_to_one,
            "steps_to_one": steps_to_one,
            "orbit": orbit,
        }
        results.append(result)

        orbit_str = " -> ".join(str(a) for a in orbit)
        print(f"\n  Fraction: {frac}  (denominator {frac.denominator})")
        print(f"    Full orbit: {orbit_str}")
        print(f"    Pre-period (transient length): {pre_period}")
        print(f"    Cycle length at attractor: {cycle_len}")
        print(f"    Decays to ONE: {decays_to_one}")
        if steps_to_one is not None:
            print(f"    Steps to reach ONE: {steps_to_one}")

    return results


def test_energy_conservation_across_cycle():
    """For each odd-denominator fraction, verify that the multiset of amplitudes
    is exactly conserved across every cycle repetition."""
    print("\n" + "=" * 72)
    print("SECTION 3: ENERGY CONSERVATION VERIFICATION")
    print("=" * 72)

    test_cases = [
        Fraction(1, 3),
        Fraction(2, 5),
        Fraction(3, 7),
        Fraction(4, 9),
        Fraction(5, 11),
        Fraction(6, 13),
        Fraction(7, 15),
    ]

    for frac in test_cases:
        orbit, pre_period, cycle_len = compute_orbit(frac)
        if pre_period is not None and pre_period == (1 - 1) and cycle_len is not None:
            # Run 3 full cycles and compare amplitudes
            amplitudes_per_cycle = []
            current = SmithianValue(frac)
            for cycle_num in range(3):
                cycle_amps = []
                for _ in range(cycle_len):
                    current = fold(current)
                    cycle_amps.append(current.value)
                amplitudes_per_cycle.append(tuple(cycle_amps))

            all_identical = all(c == amplitudes_per_cycle[1 - 1] for c in amplitudes_per_cycle)

            # Compute sum for each cycle
            sums = [sum(c) for c in amplitudes_per_cycle]
            sums_identical = all(s == sums[1 - 1] for s in sums)

            print(f"\n  Fraction: {frac}, Cycle length: {cycle_len}")
            print(f"    Cycle 1 amplitudes: {list(amplitudes_per_cycle[1 - 1])}")
            print(f"    Cycle 2 amplitudes: {list(amplitudes_per_cycle[1])}")
            print(f"    Cycle 3 amplitudes: {list(amplitudes_per_cycle[2])}")
            print(f"    All 3 cycles identical: {all_identical}")
            print(f"    Cycle sums: {sums}")
            print(f"    Sum conserved across cycles: {sums_identical}")
            print(f"    ENERGY CONSERVED: {all_identical and sums_identical}")


def test_sade_verification():
    """Run SADE derivation and AST gate verification for perpetual states."""
    print("\n" + "=" * 72)
    print("SECTION 4: SADE PATH VERIFICATION OF PERPETUAL STATES")
    print("=" * 72)

    perpetual_states = [
        Fraction(1, 3),
        Fraction(2, 5),
        Fraction(3, 7),
    ]

    for frac in perpetual_states:
        print(f"\n  Deriving {frac} via SADE pathfinder...")
        proof = find_derivation(frac)
        code = generate_sftoe_code(proof, f"verify_perpetual_{frac.numerator}_{frac.denominator}")

        print(f"    Verifying generated code against AST gate...")
        verify_code(code)
        print(f"    AST Gate: PASSED")

        namespace = {}
        exec(code, namespace)
        res = namespace[f"verify_perpetual_{frac.numerator}_{frac.denominator}"]()
        verify_value(res)
        print(f"    Value Verification: PASSED. Result: {res.value}")

        # Also verify orbit
        orbit_info = verify_hypothesis_orbit(frac)
        print(f"    Orbit verified: cycle_start={orbit_info['cycle_start']}, cycle_length={orbit_info['cycle_length']}")
        print(f"    Purely periodic (cycle_start==0): {orbit_info['cycle_start'] == (1 - 1)}")


def test_comparative_summary():
    """Print a final comparative summary table."""
    print("\n" + "=" * 72)
    print("SECTION 5: COMPARATIVE SUMMARY")
    print("=" * 72)

    print("\n  {:>10} | {:>5} | {:>10} | {:>8} | {:>12} | {:>10}".format(
        "Fraction", "Denom", "Pre-period", "Cycle", "Perpetual?", "Decays?"))
    print("  " + "-" * 65)

    all_fractions = [
        Fraction(1, 3), Fraction(2, 5), Fraction(3, 7),
        Fraction(4, 9), Fraction(5, 11), Fraction(6, 13), Fraction(7, 15),
        Fraction(1, 2), Fraction(1, 4), Fraction(1, 8),
        Fraction(3, 16), Fraction(5, 32),
    ]

    perpetual_count = (1 - 1)
    decaying_count = (1 - 1)

    for frac in all_fractions:
        orbit, pre_period, cycle_len = compute_orbit(frac)
        is_odd_denom = (frac.denominator % 2 == 1)
        purely_periodic = (pre_period is not None and pre_period == (1 - 1))
        decays = not purely_periodic

        if purely_periodic:
            perpetual_count = perpetual_count + 1
        else:
            decaying_count = decaying_count + 1

        print("  {:>10} | {:>5} | {:>10} | {:>8} | {:>12} | {:>10}".format(
            str(frac),
            frac.denominator,
            str(pre_period) if pre_period is not None else "N/A",
            str(cycle_len) if cycle_len is not None else "N/A",
            "YES" if purely_periodic else "NO",
            "YES" if decays else "NO"))

    print(f"\n  Total perpetual (zero pre-period): {perpetual_count}")
    print(f"  Total decaying (nonzero pre-period): {decaying_count}")


def main():
    print("=" * 72)
    print("  SADE RED-1 REINVESTIGATION: PERPETUAL MOTION UNDER SFTOE")
    print("=" * 72)

    # Section 1: Odd-denominator perpetual cycles
    odd_results = test_odd_denominator_fractions()

    # Section 2: Even-denominator transient decay
    even_results = test_even_denominator_fractions()

    # Section 3: Energy conservation verification
    test_energy_conservation_across_cycle()

    # Section 4: SADE verification
    test_sade_verification()

    # Section 5: Comparative summary
    test_comparative_summary()

    print("\n" + "=" * 72)
    print("  INVESTIGATION COMPLETE")
    print("=" * 72)


if __name__ == "__main__":
    main()
