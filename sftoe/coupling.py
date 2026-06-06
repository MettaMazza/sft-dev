"""
SFTOE Coupling — Force coupling resolution from the fold's sector structure.

Determines which particles interact through which forces and at what strength.
Everything derives from the four prime sectors (2, 3, 5, 7).

Source: verify_unified_force_law (proof.py line 9544)
        verify_unification (proof.py line 3608)
"""
from fractions import Fraction
from sftoe.core import SmithianValue, ONE, take
from sftoe.constants import (
    SECTOR_COUPLINGS, PRIME_SECTORS,
    FUNDAMENTAL_COUPLING, EW_COUPLING, STRONG_COUPLING,
    COS2_THETA_W, N_COLORS,
)


def coupling_strength(prime_sector):
    """
    Get the coupling g★ = (p-1)/p for a prime sector.

    Source: verify_unified_force_law
    g★(2) = 1/2, g★(3) = 2/3, g★(5) = 4/5, g★(7) = 6/7
    """
    if prime_sector not in SECTOR_COUPLINGS:
        raise ValueError(f"Unknown prime sector: {prime_sector}. Valid: {PRIME_SECTORS}")
    return SECTOR_COUPLINGS[prime_sector]


def shortfall(prime_sector):
    """
    Shortfall = 1/p = take(ONE, g★) for a prime sector.

    Source: verify_unified_force_law
    """
    return SmithianValue(Fraction(1, prime_sector))


def total_shortfall():
    """
    Sum of shortfalls across all four prime sectors.
    1/2 + 1/3 + 1/5 + 1/7 = 247/210

    Source: verify_unified_force_law
    """
    return sum(Fraction(1, p) for p in PRIME_SECTORS)


def fold_factor_coupling(m):
    """
    g★ = (m-1)/m for fold factor m.

    Source: verify_unification
    m=2: electroweak, g★=1/2
    m=3: strong/color, g★=2/3
    """
    return SmithianValue(Fraction(m - 1, m))


def ew_mixing_ratio():
    """
    Electroweak mixing: cos²θ_W = 3/4 (bare value).

    Source: verify_ew_mixing
    """
    return COS2_THETA_W


def weak_mediator_mass_ratio(m):
    """
    Mass-part ratio of weak mediators.
    charged_mass / neutral_mass = 1/(m-1)

    Source: verify_forced_relationship
    """
    return Fraction(1, m - 1)


def running_coupling(m, depth):
    """
    Running coupling at fold depth d.

    Source: verify_coupling_convergence
    g(d) = (s-1)/s where s = m + 2^d
    """
    s = m + 2**depth
    return SmithianValue(Fraction(s - 1, s))


def coupling_gap(depth):
    """
    Gap between strong (m=3) and electroweak (m=2) couplings at depth d.

    Source: verify_coupling_convergence_rate
    gap = 1/((2 + 2^d)(3 + 2^d))
    """
    two_d = 2**depth
    return Fraction(1, (2 + two_d) * (3 + two_d))


def are_coupled(p1, p2, force_type):
    """
    Determine if two particles are coupled through a specific force.

    Based on the denominator prime structure of each particle's state.
    """
    if force_type == 'gravity':
        # Everything couples to gravity
        return True

    elif force_type == 'em':
        # EM: both must have even denominators (binary fold sector)
        return p1.feels_em() and p2.feels_em()

    elif force_type == 'strong':
        # Strong: both must have denominators divisible by 7
        return p1.feels_strong() and p2.feels_strong()

    elif force_type == 'weak':
        # Weak: both must have denominators divisible by 5
        return p1.feels_weak() and p2.feels_weak()

    return False
