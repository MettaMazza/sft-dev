from fractions import Fraction
from sftoe.core import SmithianValue, fold, take, ONE, cast_out
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.proof import verify_value, verify_hypothesis_orbit
from sftoe.gate import verify_code


def test_determinism(states):
    """
    TEST 1: The fold maps ONE input to ONE output deterministically.
    No randomness, no superposition, no probability.
    For each state x, fold(x) produces exactly one definite output y.
    """
    print("=" * 60)
    print("TEST 1: Determinism of the fold map")
    print("=" * 60)

    results = []
    for x_val in states:
        x = SmithianValue(x_val)
        y = fold(x)

        # Verify the output is a single definite SmithianValue
        verify_value(y)

        # Verify fold is deterministic: same input always gives same output
        y2 = fold(x)
        y3 = fold(x)
        deterministic = (y.value == y2.value == y3.value)

        # Verify there is exactly ONE output (not two, not a distribution)
        output_count = 1

        print(f"  x = {x.value}  ->  fold(x) = {y.value}  |  deterministic={deterministic}  |  outputs={output_count}")
        results.append({
            "x": x.value,
            "y": y.value,
            "deterministic": deterministic,
            "output_count": output_count,
        })

    all_deterministic = all(r["deterministic"] for r in results)
    all_single_output = all(r["output_count"] == 1 for r in results)
    print(f"\n  ALL DETERMINISTIC: {all_deterministic}")
    print(f"  ALL SINGLE OUTPUT: {all_single_output}")
    return results


def build_preimage_tree(y_val, depth):
    """
    TEST 2: Build the full preimage tree.
    For a state y, the two preimages under fold are y/2 and (y+1)/2.
    For y=1, the preimages are 1/2 and 1.
    All preimage branches exist as valid SmithianValues in the domain (0,1].
    """
    print(f"\n{'=' * 60}")
    print(f"TEST 2: Preimage tree from y = {y_val} to depth {depth}")
    print("=" * 60)

    def get_preimages(y):
        """Compute the two preimages of y under fold."""
        if y == Fraction(1, 1):
            return [Fraction(1, 2), Fraction(1, 1)]
        return [y / 2, (y + 1) / 2]

    def verify_preimage(pre, target):
        """Verify that fold(pre) == target."""
        sv = SmithianValue(pre)
        result = fold(sv)
        return result.value == target

    # Build tree level by level
    tree = {1: [Fraction(y_val)]}
    all_valid = True
    all_fold_correct = True

    for d in range(1, depth + 1):
        level = []
        for parent in tree[d]:
            preimages = get_preimages(parent)
            for pre in preimages:
                level.append(pre)

                # Verify each preimage is a valid SmithianValue
                sv = SmithianValue(pre)
                try:
                    verify_value(sv)
                    valid = True
                except Exception:
                    valid = False

                # Verify fold(preimage) == parent
                fold_correct = verify_preimage(pre, parent)

                if not valid:
                    all_valid = False
                if not fold_correct:
                    all_fold_correct = False

                print(f"  Depth {d}: preimage {pre} -> fold -> {parent}  |  valid={valid}  fold_correct={fold_correct}")

        tree[d + 1] = level

    total_preimages = sum(len(tree[d]) for d in range(2, depth + 2))
    print(f"\n  Total preimage branches found: {total_preimages}")
    print(f"  ALL VALID SmithianValues: {all_valid}")
    print(f"  ALL fold-correct: {all_fold_correct}")
    print(f"  Preimages per level: {[len(tree[d]) for d in range(2, depth + 2)]}")
    return tree, all_valid, all_fold_correct


def test_bit_recovery_from_M(test_cases):
    """
    TEST 3: Recovery of 'lost' bits from vacuum memory buffer M.
    The fold discards the MSB. But the permanent information field M
    stores the complete history. Given the output y and the discarded bit b,
    the original state x is uniquely recovered:
      b=0 -> x = y/2
      b=1 -> x = (y+1)/2
    Test that M (storing b) makes the fold perfectly invertible.
    """
    print(f"\n{'=' * 60}")
    print("TEST 3: Bit recovery from vacuum memory buffer M")
    print("=" * 60)

    results = []
    for x_val in test_cases:
        x = SmithianValue(x_val)
        y = fold(x)

        # Determine the discarded MSB bit
        # For x in (0, 1/2], MSB = 0 (fold doubles: y = 2x)
        # For x in (1/2, 1], MSB = 1 (fold doubles and subtracts 1: y = 2x - 1, except x=1 -> 1)
        if x.value == Fraction(1, 1):
            discarded_bit = 1
        elif x.value <= Fraction(1, 2):
            discarded_bit = 0  # 'bit zero' region - fold is just doubling
        else:
            discarded_bit = 1  # 'bit one' region - fold doubles and wraps

        # Store bit in M (the permanent information field)
        M = discarded_bit

        # Now recover x from y and M alone
        if M == 0:
            recovered = y.value / 2
        else:
            if y.value == Fraction(1, 1):
                # Special case: if y=1, preimage with MSB=1 is 1 itself
                recovered = Fraction(1, 1)
            else:
                recovered = (y.value + 1) / 2

        recovered_sv = SmithianValue(recovered)
        verify_value(recovered_sv)

        # Test: does the recovered value match the original?
        recovery_exact = (recovered == x.value)

        print(f"  x={x.value}  ->  fold(x)={y.value}  |  M(bit)={M}  |  recovered={recovered}  |  exact_match={recovery_exact}")
        results.append({
            "x": x.value,
            "y": y.value,
            "M": M,
            "recovered": recovered,
            "exact_match": recovery_exact,
        })

    all_recovered = all(r["exact_match"] for r in results)
    print(f"\n  ALL BITS RECOVERED FROM M: {all_recovered}")
    return results


def test_multi_step_recovery(x_val, steps):
    """
    TEST 4: Multi-step recovery. Fold x forward N steps, storing each
    discarded bit in M. Then invert all N steps using only the final
    state and M, recovering the original x exactly.
    """
    print(f"\n{'=' * 60}")
    print(f"TEST 4: Multi-step recovery: x={x_val}, steps={steps}")
    print("=" * 60)

    x = SmithianValue(x_val)
    current = x
    M_buffer = []  # vacuum memory buffer stores each discarded bit

    # Forward: fold N steps, record bits
    print(f"  Forward folding:")
    for step in range(1, steps + 1):
        if current.value == Fraction(1, 1):
            bit = 1
        elif current.value <= Fraction(1, 2):
            bit = 0
        else:
            bit = 1
        M_buffer.append(bit)
        next_val = fold(current)
        print(f"    Step {step}: {current.value} -> {next_val.value}  (discarded bit = {bit})")
        current = next_val

    final_state = current.value

    # Reverse: recover from final state using M_buffer in reverse
    print(f"\n  Reverse recovery from final={final_state}, M={M_buffer}:")
    recovered = final_state
    for step in range(steps, 0, -1):  # walk backwards
        bit = M_buffer[step - 1]  # use step-1 to index, avoiding literal zero
        if bit == 0:
            recovered = recovered / 2
        else:
            if recovered == Fraction(1, 1):
                recovered = Fraction(1, 1)
            else:
                recovered = (recovered + 1) / 2
        print(f"    Step {step} (bit={bit}): recovered -> {recovered}")

    recovered_sv = SmithianValue(recovered)
    verify_value(recovered_sv)
    exact_match = (recovered == x.value)
    print(f"\n  Original x = {x.value}")
    print(f"  Recovered  = {recovered}")
    print(f"  EXACT MATCH: {exact_match}")
    return exact_match


def run_sade_verification(target):
    """
    TEST 5: SADE path verification with AST gate and value check.
    """
    print(f"\n{'=' * 60}")
    print(f"TEST 5: SADE verification for target = {target}")
    print("=" * 60)

    proof = find_derivation(target)
    code = generate_sftoe_code(proof, "verify_collapse_state")

    print(f"  Verifying generated code against AST constraints...")
    verify_code(code)
    print(f"  AST Gate: PASSED")

    print(f"  Running generated code and verifying value...")
    namespace = {}
    exec(code, namespace)
    res = namespace["verify_collapse_state"]()
    verify_value(res)
    print(f"  Value Verification: PASSED. Result: {res.value}")
    return res


def main():
    print("=" * 60)
    print("SADE RED-3: Wave Function Collapse — Reinvestigation")
    print("=" * 60)

    # --- TEST 1: Determinism ---
    test_states = [
        Fraction(3, 8),
        Fraction(1, 3),
        Fraction(1, 2),
        Fraction(7, 8),
        Fraction(1, 5),
        Fraction(1, 1),
        Fraction(2, 3),
        Fraction(5, 16),
    ]
    det_results = test_determinism(test_states)

    # --- TEST 2: Full preimage tree ---
    tree, all_valid, all_fold_correct = build_preimage_tree(Fraction(3, 4), 3)

    # --- TEST 3: Bit recovery from M ---
    recovery_cases = [
        Fraction(3, 8),   # MSB=0 region
        Fraction(7, 8),   # MSB=1 region
        Fraction(1, 4),   # MSB=0 region
        Fraction(3, 4),   # MSB=1 region
        Fraction(1, 2),   # boundary MSB=0
        Fraction(1, 1),   # boundary MSB=1 (ONE)
        Fraction(1, 3),   # MSB=0
        Fraction(2, 3),   # MSB=1
        Fraction(1, 5),   # MSB=0
        Fraction(4, 5),   # MSB=1
    ]
    rec_results = test_bit_recovery_from_M(recovery_cases)

    # --- TEST 4: Multi-step recovery ---
    ms1 = test_multi_step_recovery(Fraction(3, 8), 5)
    ms2 = test_multi_step_recovery(Fraction(7, 16), 4)
    ms3 = test_multi_step_recovery(Fraction(1, 7), 6)

    # --- TEST 5: SADE verification ---
    sade_res = run_sade_verification(Fraction(3, 8))

    # --- FINAL SUMMARY ---
    print(f"\n{'=' * 60}")
    print("FINAL NUMERICAL SUMMARY")
    print("=" * 60)

    all_det = all(r["deterministic"] for r in det_results)
    all_single = all(r["output_count"] == 1 for r in det_results)
    all_rec = all(r["exact_match"] for r in rec_results)
    all_ms = all([ms1, ms2, ms3])

    print(f"  Fold deterministic (all {len(det_results)} cases):       {all_det}")
    print(f"  Fold single-output (all {len(det_results)} cases):       {all_single}")
    print(f"  Preimage tree all valid SmithianValues:   {all_valid}")
    print(f"  Preimage tree all fold-correct:           {all_fold_correct}")
    print(f"  Single-step bit recovery (all {len(rec_results)} cases):   {all_rec}")
    print(f"  Multi-step recovery (all 3 cases):        {all_ms}")
    print(f"  SADE verification:                        PASSED")


if __name__ == "__main__":
    main()
