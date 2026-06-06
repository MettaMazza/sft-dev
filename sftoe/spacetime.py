"""
SFTOE Spacetime — Minkowski metric, causal structure, distance.

All from the fold's own take-difference metric.
Source: verify_minkowski_causal, MASTER.md Section 3 (Paper 1).
"""
from fractions import Fraction
from sftoe.core import SmithianValue, ONE, fold, take, cast_out
from sftoe.constants import C, SPATIAL_DIMENSION


def lattice_distance(pos_a, pos_b, lattice_size):
    """
    Compute the shortest-path (toroidal) Manhattan distance between two
    lattice positions in d=3.

    Each position is a tuple of 3 integer indices (i, j, k).
    lattice_size is the number of sites along each axis (2^depth).

    The lattice is periodic (cast_out wraps), so distance along each
    axis is the minimum of the direct gap and the wrap-around gap.
    """
    total = 0
    for a, b in zip(pos_a, pos_b):
        direct = abs(a - b)
        wrapped = lattice_size - direct
        total += min(direct, wrapped)
    return total


def causal_check(pos_a, pos_b, delta_t, lattice_size):
    """
    Verify that two events respect the causal cone.

    Source: verify_minkowski_causal, MASTER.md eq.7
    c × Δt ≥ d(x₁, x₂)

    c = ONE = 1 site/tick, so this reduces to:
    Δt ≥ Manhattan_distance(pos_a, pos_b)

    Returns True if the separation is causal (signal CAN reach).
    Returns False if it would require faster-than-light propagation.
    """
    d = lattice_distance(pos_a, pos_b, lattice_size)
    return delta_t >= d


def fold_separation(state_a, state_b):
    """
    Compute the separation metric between two fold states.

    Source: MASTER.md eq.6
    d(a, b) = min(take(a,b), take(ONE, take(a,b)))

    This is the short-way path around the unit circle.
    """
    if state_a.value == state_b.value:
        return SmithianValue(Fraction(1, 1))  # unison — zero separation maps to ONE

    if state_a.value > state_b.value:
        diff = take(state_a, state_b)
    else:
        diff = take(state_b, state_a)

    # Short-way: min of diff and take(ONE, diff)
    complement = take(ONE, diff)

    if diff.value <= complement.value:
        return diff
    else:
        return complement


def gravitational_time_dilation(rs, r):
    """
    Compute the Schwarzschild time dilation factor A(r) = take(ONE, rs/r).

    Source: verify_gravitational_time_dilation (proof.py line ~900)
    verify_schwarzschild_solution (proof.py line 865)

    rs = Schwarzschild radius (as SmithianValue)
    r = radial coordinate (as SmithianValue, must be > rs)

    Returns A(r) such that proper_time/coordinate_time = sqrt(A(r))
    """
    if not isinstance(rs, SmithianValue):
        rs = SmithianValue(rs)
    if not isinstance(r, SmithianValue):
        r = SmithianValue(r)

    ratio = Fraction(rs.value, r.value)
    if ratio >= 1:
        raise ValueError(f"Position r={r.value} is at or inside horizon rs={rs.value}")

    return take(ONE, SmithianValue(ratio))


def velocity_composition(u, v):
    """
    Relativistic velocity composition: w = (u + v) / (1 + u*v)

    Source: verify_velocity_composition
    c = ONE is the fixed point: compose(c, anything) = c

    All velocities are SmithianValues in (0, 1].
    """
    if not isinstance(u, SmithianValue):
        u = SmithianValue(u)
    if not isinstance(v, SmithianValue):
        v = SmithianValue(v)

    numerator = u.value + v.value
    denominator = 1 + u.value * v.value
    result = Fraction(numerator, denominator)

    return SmithianValue(cast_out(result))


def equivalence_redshift(g, h):
    """
    Gravitational redshift z = g*h/c² in a uniform field.

    Source: verify_equivalence_redshift

    g = acceleration (as Fraction)
    h = height (as Fraction)
    c = ONE, so c² = 1

    Returns z as a SmithianValue.
    """
    z_val = Fraction(g) * Fraction(h)
    return SmithianValue(cast_out(z_val))
