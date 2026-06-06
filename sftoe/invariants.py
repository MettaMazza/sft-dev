"""
SFTOE Invariants — Conservation laws checked every tick.

These are the structural guarantees the fold engine must maintain.
If any invariant fails, the theory is broken — not just the code.

Source: verify_coupled_lattice (conservation), verify_minkowski_causal (causality),
        verify_value (no-zero, positive, in (0,1])
"""
from fractions import Fraction
from sftoe.core import SmithianValue, ONE


class InvariantViolation(Exception):
    """Raised when a physical invariant is violated."""
    pass


def check_no_zero(particles):
    """
    No state can ever be zero. The fold has no zero.

    Source: SmithianValue rejects 0 in its constructor.
    """
    for p in particles:
        if p.state.value <= 0:
            raise InvariantViolation(
                f"NO-ZERO VIOLATION: {p.name} has state {p.state.value}"
            )


def check_positive_domain(particles):
    """
    All states must be in (0, 1]. No negatives, no values > ONE.

    Source: verify_value
    """
    for p in particles:
        if p.state.value <= 0 or p.state.value > 1:
            raise InvariantViolation(
                f"DOMAIN VIOLATION: {p.name} has state {p.state.value}, "
                f"must be in (0, 1]"
            )


def check_causality(particles, lattice_size):
    """
    No particle moves faster than c = ONE = 1 site/tick.

    Source: verify_minkowski_causal, verify_gravitational_wave_speed
    """
    for p in particles:
        speed = abs(p.velocity[0]) + abs(p.velocity[1]) + abs(p.velocity[2])
        if speed > 1:
            raise InvariantViolation(
                f"CAUSALITY VIOLATION: {p.name} has speed {speed} > c=1"
            )


def check_presence_conservation(lattice, expected_total=None):
    """
    Total lattice presence is conserved under coupled lattice evolution.

    Source: verify_coupled_lattice — total presence is conserved.
    """
    total = lattice.total_presence()

    if expected_total is not None:
        # Allow small rational arithmetic drift
        if total != expected_total:
            raise InvariantViolation(
                f"PRESENCE CONSERVATION VIOLATION: "
                f"total={total}, expected={expected_total}"
            )

    return total


def check_all(universe, expected_total=None):
    """
    Run all invariant checks on the universe.

    Returns a dict of results. Raises InvariantViolation on failure.
    """
    particles = universe.alive_particles()

    check_no_zero(particles)
    check_positive_domain(particles)
    check_causality(particles, universe.size)
    total = check_presence_conservation(universe.lattice, expected_total)

    return {
        'tick': universe.tick,
        'all_valid': True,
        'particle_count': len(particles),
        'total_presence': str(total),
        'no_zero': True,
        'positive_domain': True,
        'causality': True,
        'presence_conserved': True,
    }
