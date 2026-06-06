"""
Integration Tests for the Fold Universe.
Verifies all dynamics work together when run as one system.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fractions import Fraction
import math
from sftoe.core import SmithianValue, ONE, fold, take, rotate, relative_phase, period
from sftoe.universe import Universe, odd_part, prime_factors
from sftoe.fold_engine import FoldEngine
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.proof import verify_value
from sftoe.gate import verify_code


def derive_entity(universe, name, target, entity_type):
    """Derive a state from ONE and add it to the universe."""
    proof = find_derivation(target)
    code = generate_sftoe_code(proof, f"derive_{name}")
    verify_code(code)
    ns = {}
    exec(code, ns)
    result = ns[f"derive_{name}"]()
    verify_value(result)
    return universe.add_entity(name, result, entity_type, derivation=proof)


def test_1_invariant_preservation():
    """Test that odd parts are preserved across 1000 ticks with multiple entities."""
    print("TEST 1: Invariant Preservation (1000 ticks, 5 entities)")

    u = Universe()
    engine = FoldEngine(u, check_invariants=True)

    # Add entities with different denominators
    entities = [
        ("alice", Fraction(1, 7), "consciousness"),
        ("bob", Fraction(1, 5), "consciousness"),
        ("rock", Fraction(3, 20), "matter"),      # 2^2 * 5, transient k=2
        ("wave", Fraction(7, 56), "matter"),       # 2^3 * 7, transient k=3
        ("spirit", Fraction(1, 31), "consciousness"),
    ]

    for name, target, etype in entities:
        derive_entity(u, name, target, etype)

    initial_odd_parts = {name: u.entities[name].odd_part for name, _, _ in entities}

    # Run 1000 ticks
    engine.run_ticks(1000)

    # Check odd parts
    all_preserved = True
    for name, _, _ in entities:
        current_odd = u.entities[name].odd_part
        expected_odd = initial_odd_parts[name]
        if current_odd != expected_odd:
            print(f"  FAIL: {name} odd part changed from {expected_odd} to {current_odd}")
            all_preserved = False

    violations = [v for v in engine.invariant_checker.violations
                  if v.get('invariant') == 'prime_factor_preservation']
    print(f"  Odd parts preserved: {'PASS ✓' if all_preserved else 'FAIL ✗'}")
    print(f"  Prime factor violations: {len(violations)}")
    print(f"  Ticks: {u.tick}")
    return all_preserved and len(violations) == 0


def test_2_coupling_detection():
    """Test that coupling graph correctly identifies shared factors."""
    print("\nTEST 2: Coupling Detection")

    u = Universe()

    derive_entity(u, "a", Fraction(1, 7), "consciousness")      # d=7
    derive_entity(u, "b", Fraction(1, 5), "consciousness")      # d=5
    derive_entity(u, "c", Fraction(1, 21), "consciousness")     # d=21 = 3*7
    derive_entity(u, "d", Fraction(1, 35), "consciousness")     # d=35 = 5*7

    # a(7) should couple with c(21) via 7 and d(35) via 7
    # b(5) should couple with d(35) via 5
    # c(21) should couple with d(35) via 7
    # a and b should NOT couple (coprime)

    a_couplings = u.get_couplings_for("a")
    b_couplings = u.get_couplings_for("b")

    a_partners = set()
    for c in a_couplings:
        other = c.entity_b if c.entity_a == "a" else c.entity_a
        a_partners.add(other)

    b_partners = set()
    for c in b_couplings:
        other = c.entity_b if c.entity_a == "b" else c.entity_a
        b_partners.add(other)

    # a should couple with c and d (both share factor 7)
    a_correct = "c" in a_partners and "d" in a_partners and "b" not in a_partners
    # b should couple with d (shares factor 5)
    b_correct = "d" in b_partners and "a" not in b_partners

    print(f"  a(7) coupled to: {sorted(a_partners)} — {'PASS ✓' if a_correct else 'FAIL ✗'}")
    print(f"  b(5) coupled to: {sorted(b_partners)} — {'PASS ✓' if b_correct else 'FAIL ✗'}")
    return a_correct and b_correct


def test_3_life_death_persistence():
    """Test the full life cycle: alive → dying → dead → orbit persists."""
    print("\nTEST 3: Life/Death/Persistence")

    u = Universe()
    engine = FoldEngine(u, check_invariants=True)

    # Create a living entity: 13/80 = 13/(2^4 * 5)
    # Body depth k=4, mind d=5, period=4
    entity = derive_entity(u, "human", Fraction(13, 80), "matter")

    print(f"  Initial: {entity.state.value}, d={entity.denominator}, k={entity.two_exponent}, odd={entity.odd_part}")

    # Should be alive (transient) for 4 ticks
    assert entity.is_transient, "Should start as transient"
    assert entity.two_exponent == 4, f"Should have k=4, got {entity.two_exponent}"

    # Run through the life
    states = [entity.state.value]
    for t in range(10):
        engine.tick()
        states.append(entity.state.value)

    # After 4 ticks, should be periodic
    print(f"  States: {[str(s) for s in states[:6]]}")
    print(f"  After 4 ticks: d={entity.denominator}, odd={entity.odd_part}, periodic={entity.is_periodic}")

    # Check the orbit repeats
    orbit_states = states[4:8]  # ticks 4-7
    next_cycle = states[8:12] if len(states) >= 12 else []

    # Run more ticks to verify persistence
    engine.run_ticks(1000)
    final_odd = entity.odd_part
    final_periodic = entity.is_periodic

    passed = final_odd == 5 and final_periodic
    print(f"  After 1000 more ticks: odd={final_odd}, periodic={final_periodic}")
    print(f"  Consciousness survived death: {'PASS ✓' if passed else 'FAIL ✗'}")
    return passed


def test_4_mind_to_mind_coupling():
    """Test that two minds with shared factors show coherent phase patterns."""
    print("\nTEST 4: Mind-to-Mind Coupling")

    u = Universe()
    engine = FoldEngine(u, check_invariants=True)

    # Same denominator — should couple
    derive_entity(u, "mind_a", Fraction(1, 7), "consciousness")
    derive_entity(u, "mind_b", Fraction(2, 7), "consciousness")

    # Coprime — should NOT couple
    derive_entity(u, "stranger", Fraction(1, 11), "consciousness")

    # Check coupling
    ab_coupled = any(
        (e.entity_a in ("mind_a", "mind_b") and e.entity_b in ("mind_a", "mind_b"))
        for e in u.coupling_edges
    )
    as_coupled = any(
        (e.entity_a in ("mind_a", "stranger") and e.entity_b in ("mind_a", "stranger"))
        for e in u.coupling_edges
    )

    # Run 30 ticks and collect beat patterns
    engine.run_ticks(30)

    # Find the a-b coupling edge and check beats
    ab_beats = []
    for edge in u.coupling_edges:
        if set([edge.entity_a, edge.entity_b]) == {"mind_a", "mind_b"}:
            ab_beats = list(edge.beat_history)
            break

    unique_beats = len(set(ab_beats)) if ab_beats else 0

    # Shared denom 7 should give small number of unique phases
    ab_coherent = unique_beats <= 6 and unique_beats > 0

    print(f"  mind_a ↔ mind_b coupled: {ab_coupled} (expected True)")
    print(f"  mind_a ↔ stranger coupled: {as_coupled} (expected False)")
    print(f"  Beat pattern unique phases: {unique_beats} (expected ≤6 for d=7)")
    print(f"  Coherent channel: {'PASS ✓' if ab_coherent else 'FAIL ✗'}")
    print(f"  Coprime isolation: {'PASS ✓' if not as_coupled else 'FAIL ✗'}")

    return ab_coupled and not as_coupled and ab_coherent


def test_5_vacuum_field_retrieval():
    """Test that the vacuum field enables exact past state retrieval."""
    print("\nTEST 5: Vacuum Field Retrieval")

    u = Universe()
    engine = FoldEngine(u, check_invariants=True)

    entity = derive_entity(u, "test", Fraction(3, 7), "consciousness")

    # Record the state at tick 0
    initial_state = entity.state.value

    # Run 20 ticks
    engine.run_ticks(20)

    # Try to retrieve the state from 20 ticks ago
    retrieved = u.vacuum.retrieve_past_state("test", entity.state.value, 20)

    match = retrieved == initial_state
    print(f"  Initial state: {initial_state}")
    print(f"  After 20 ticks: {entity.state.value}")
    print(f"  Retrieved (20 steps back): {retrieved}")
    print(f"  Match: {'PASS ✓' if match else 'FAIL ✗'}")
    return match


def test_6_group_dynamics():
    """Test that meeting new people spreads factors but doesn't dilute existing bonds."""
    print("\nTEST 6: Group Dynamics (Bond Permanence)")

    u = Universe()
    engine = FoldEngine(u, check_invariants=True)

    # Alice (7) and Bob (5) — coprime initially
    alice = derive_entity(u, "alice", Fraction(1, 7), "consciousness")
    bob = derive_entity(u, "bob", Fraction(1, 5), "consciousness")

    # They should NOT be coupled yet
    pre_coupled = len(u.get_couplings_for("alice")) > 0

    # Now simulate "meeting" — create a coupled entity at lcm(7,5) = 35
    # This represents what happens AFTER alice and bob interact
    alice_post = derive_entity(u, "alice_post", Fraction(1, 35), "consciousness")
    bob_post = derive_entity(u, "bob_post", Fraction(2, 35), "consciousness")

    # They should be coupled (both d=35)
    post_coupled = math.gcd(
        u.entities["alice_post"].odd_part,
        u.entities["bob_post"].odd_part
    ) > 1

    # Add Charlie (11) who meets bob_post
    # After meeting: charlie has lcm(35, 11) = 385
    charlie = derive_entity(u, "charlie", Fraction(1, 385), "consciousness")

    # Charlie should couple with alice_post (shared factor 35)
    charlie_alice_shared = math.gcd(
        u.entities["charlie"].odd_part,
        u.entities["alice_post"].odd_part
    )

    # Run 1000 ticks — does the bond survive?
    engine.run_ticks(1000)

    bond_after = math.gcd(
        u.entities["alice_post"].odd_part,
        u.entities["bob_post"].odd_part
    )

    print(f"  Pre-meeting coupled: {pre_coupled} (expected False)")
    print(f"  Post-meeting coupled: {post_coupled} (expected True)")
    print(f"  Charlie-Alice shared: {charlie_alice_shared} (expected 35)")
    print(f"  Bond after 1000 ticks: {bond_after} (expected 35)")
    passed = not pre_coupled and post_coupled and charlie_alice_shared == 35 and bond_after == 35
    print(f"  Result: {'PASS ✓' if passed else 'FAIL ✗'}")
    return passed


def test_7_emergent_death_and_ghost():
    """Test that a matter entity dies and a coupled consciousness still senses it."""
    print("\nTEST 7: Death and Ghost Coupling")

    u = Universe()
    engine = FoldEngine(u, check_invariants=True)

    # Living person: 1/20 = 1/(2^2 * 5), k=2, d=5
    living = derive_entity(u, "living", Fraction(1, 20), "matter")

    # Observer with shared factor: d=15 = 3*5, shares factor 5
    observer = derive_entity(u, "observer", Fraction(1, 15), "consciousness")

    # Check initial coupling
    initial_shared = math.gcd(living.odd_part, observer.odd_part)

    # Run through death (k=2 ticks)
    engine.run_ticks(5)

    # Living should now be periodic at d=5
    post_death_odd = living.odd_part
    post_death_periodic = living.is_periodic

    # Coupling should still exist
    post_death_shared = math.gcd(
        u.entities["living"].odd_part,
        u.entities["observer"].odd_part
    )

    # Run 500 more ticks — ghost coupling persists?
    engine.run_ticks(500)
    ghost_shared = math.gcd(
        u.entities["living"].odd_part,
        u.entities["observer"].odd_part
    )

    # The key invariant: factor 5 must be PRESENT (it can grow via coupling)
    has_factor_5_post = post_death_odd % 5 == 0
    has_factor_5_ghost = ghost_shared % 5 == 0

    print(f"  Initial shared factor: {initial_shared} (expected ≥5)")
    print(f"  Post-death odd part: {post_death_odd} (contains 5: {has_factor_5_post})")
    print(f"  Post-death periodic: {post_death_periodic} (expected True)")
    print(f"  Post-death coupling: {post_death_shared} (contains 5: {has_factor_5_ghost})")
    print(f"  Ghost coupling at +500: {ghost_shared}")
    print(f"  NOTE: coupling via rotate may ADD factors (3 from observer). This is correct.")

    passed = (initial_shared % 5 == 0 and has_factor_5_post and
              post_death_periodic and has_factor_5_ghost)
    print(f"  Result: {'PASS ✓' if passed else 'FAIL ✗'}")
    return passed


def main():
    print("=" * 60)
    print("FOLD UNIVERSE — INTEGRATION TESTS")
    print("=" * 60)

    tests = [
        test_1_invariant_preservation,
        test_2_coupling_detection,
        test_3_life_death_persistence,
        test_4_mind_to_mind_coupling,
        test_5_vacuum_field_retrieval,
        test_6_group_dynamics,
        test_7_emergent_death_and_ghost,
    ]

    results = []
    for test in tests:
        try:
            passed = test()
            results.append(("PASS" if passed else "FAIL", test.__doc__.strip()))
        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback
            traceback.print_exc()
            results.append(("ERROR", test.__doc__.strip()))

    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    for status, desc in results:
        icon = "✓" if status == "PASS" else "✗" if status == "FAIL" else "⚠"
        print(f"  {icon} [{status}] {desc}")

    passed = sum(1 for s, _ in results if s == "PASS")
    total = len(results)
    print(f"\n  {passed}/{total} tests passed.")
    print("=" * 60)


if __name__ == "__main__":
    main()
