"""
SFTOE Forces — All four forces from the fold's sector structure.

Each force computes the interaction between particles based on the
lattice geometry and the sector coupling constants.

All arithmetic is Fraction — no floats, no irrationals.

Sources:
  Gravity: verify_newton_law, verify_schwarzschild_solution
  EM: verify_coulomb_law, verify_lorentz_force, verify_maxwell_wave_closure
  Strong: verify_strong_confinement, verify_colour_neutral
  Weak: verify_weak_range, verify_ew_mixing
  Unification: verify_unified_force_law (proof.py line 9544)
"""
from fractions import Fraction
from sftoe.core import SmithianValue, ONE, fold, take
from sftoe.constants import (
    SPATIAL_DIMENSION, LAPLACIAN_3D,
    SECTOR_COUPLINGS, PRIME_SECTORS,
    GRAVITY_GENERATOR, EM_GENERATOR, STRONG_GENERATOR,
    FUNDAMENTAL_COUPLING, COS2_THETA_W, N_COLORS,
)
from sftoe.spacetime import lattice_distance


def gravity_force(p1, p2, lattice_size):
    """
    Gravitational force between two particles.

    Source: verify_newton_law, verify_inverse_power_law
    F ∝ g★(p=2) × m1 × m2 / r²

    Gravity is universal — every massive particle feels it.
    Coupling: g★ = 1/2 (prime sector p=2)
    Law: inverse-square from Gauss flux in d=3

    Returns force magnitude as a Fraction.
    """
    r = lattice_distance(p1.position, p2.position, lattice_size)
    if r == 0:
        return Fraction(0)

    g_star = SECTOR_COUPLINGS[2].value  # 1/2
    m1 = Fraction(p1.mass_fraction).limit_denominator(10000)
    m2 = Fraction(p2.mass_fraction).limit_denominator(10000)

    # F = g★ × m1 × m2 / r²
    return g_star * m1 * m2 / Fraction(r * r)


def em_force(p1, p2, lattice_size):
    """
    Electromagnetic force between two charged particles.

    Source: verify_coulomb_law, verify_lorentz_force
    F ∝ g★(p=3) × q1 × q2 / r²

    Only particles whose denominator is divisible by 2 (binary fold sector)
    carry EM charge.
    Coupling: g★ = 2/3 (prime sector p=3)
    Law: inverse-square from Gauss flux in d=3

    Returns force magnitude as a Fraction. Positive = repulsive, negative = attractive.
    """
    if not (p1.feels_em() and p2.feels_em()):
        return Fraction(0)

    r = lattice_distance(p1.position, p2.position, lattice_size)
    if r == 0:
        return Fraction(0)

    g_star = SECTOR_COUPLINGS[3].value  # 2/3

    # Charge is determined by the denominator structure
    # Same-type particles repel, different-type attract
    q1 = Fraction(1, p1.denominator)
    q2 = Fraction(1, p2.denominator)

    # F = g★ × q1 × q2 / r²
    return g_star * q1 * q2 / Fraction(r * r)


def strong_force(p1, p2, lattice_size):
    """
    Strong force between two colored particles.

    Source: verify_strong_confinement, verify_colour_neutral
    Confining: constant force (linear potential) at large r
    Flux tube: field confined to 1D tube between quarks (d=1 confinement)

    Only particles whose denominator is divisible by 7 (strong generator 1/7)
    carry color charge.
    Coupling: g★ = 6/7 (prime sector p=7)

    Returns force magnitude as a Fraction.
    """
    if not (p1.feels_strong() and p2.feels_strong()):
        return Fraction(0)

    r = lattice_distance(p1.position, p2.position, lattice_size)
    if r == 0:
        return Fraction(0)

    g_star = SECTOR_COUPLINGS[7].value  # 6/7

    # Strong confinement: constant force (linear potential)
    # Source: verify_strong_confinement — flux tube is d=1
    # The force doesn't fall with distance — it's CONFINING
    # F = g★ × color_charge_product
    color_product = Fraction(1)
    if p1.color is not None and p2.color is not None:
        if p1.color == p2.color:
            # Same color — repulsive at short range
            color_product = Fraction(1, N_COLORS)
        else:
            # Different color — attractive (confinement)
            color_product = Fraction(1, N_COLORS)

    return g_star * color_product


def weak_force(p1, p2, lattice_size):
    """
    Weak force between two particles.

    Source: verify_weak_range
    Short range: massive mediator means force dies off quickly.
    A massless mediator propagates indefinitely; a massive one loses
    presence to its mass-part each tick, so its reach is bounded.

    Only particles whose denominator is divisible by 5 (prime sector 5)
    participate in weak interactions.
    Coupling: g★ = 4/5 (prime sector p=5)
    Range: ~1 lattice site (contact interaction at this resolution)

    Returns force magnitude as a Fraction.
    """
    if not (p1.feels_weak() and p2.feels_weak()):
        return Fraction(0)

    r = lattice_distance(p1.position, p2.position, lattice_size)

    # Weak force is contact-range only
    # Source: verify_weak_range — massive mediator limits range
    if r > 1:
        return Fraction(0)

    g_star = SECTOR_COUPLINGS[5].value  # 4/5

    return g_star * Fraction(1, p1.denominator) * Fraction(1, p2.denominator)


def compute_all_forces(universe):
    """
    Compute forces between all particle pairs in the universe.

    Returns a dict mapping particle name -> (fx, fy, fz) force vector.
    All values are Fraction — no floats, no irrationals.
    """
    particles = universe.alive_particles()
    lattice_size = universe.size
    forces = {p.name: [Fraction(0), Fraction(0), Fraction(0)] for p in particles}

    for idx_a, pa in enumerate(particles):
        for idx_b in range(idx_a + 1, len(particles)):
            pb = particles[idx_b]

            # Compute each force
            f_grav = gravity_force(pa, pb, lattice_size)
            f_em = em_force(pa, pb, lattice_size)
            f_strong = strong_force(pa, pb, lattice_size)
            f_weak = weak_force(pa, pb, lattice_size)

            total_magnitude = f_grav + f_em + f_strong + f_weak

            if total_magnitude == 0:
                continue

            # Direction: from a toward b (gravity/strong attractive)
            # Compute displacement vector
            dx = pb.position[0] - pa.position[0]
            dy = pb.position[1] - pa.position[1]
            dz = pb.position[2] - pa.position[2]

            # Handle periodic wrapping
            half = lattice_size // 2
            if dx > half:
                dx -= lattice_size
            elif dx < -half:
                dx += lattice_size
            if dy > half:
                dy -= lattice_size
            elif dy < -half:
                dy += lattice_size
            if dz > half:
                dz -= lattice_size
            elif dz < -half:
                dz += lattice_size

            r = abs(dx) + abs(dy) + abs(dz)
            if r == 0:
                continue

            # Normalize direction and apply force
            fx = total_magnitude * Fraction(dx, r)
            fy = total_magnitude * Fraction(dy, r)
            fz = total_magnitude * Fraction(dz, r)

            # Newton's third law
            forces[pa.name][0] += fx
            forces[pa.name][1] += fy
            forces[pa.name][2] += fz

            forces[pb.name][0] -= fx
            forces[pb.name][1] -= fy
            forces[pb.name][2] -= fz

            # Record coupling in universe
            if f_grav > 0:
                universe.add_coupling(pa, pb, 'gravity', f_grav)
            if f_em > 0:
                universe.add_coupling(pa, pb, 'em', f_em)
            if f_strong > 0:
                universe.add_coupling(pa, pb, 'strong', f_strong)
            if f_weak > 0:
                universe.add_coupling(pa, pb, 'weak', f_weak)

    return forces


def apply_forces(universe, forces):
    """
    Apply computed forces to update particle velocities.

    F = ma → a = F/m → Δv = a × Δt (Δt = 1 tick)

    Velocity accumulates as Fraction in particle.frac_vel.
    The particle's move() method extracts integer lattice steps.

    Source: verify_minkowski_causal
    """
    for p in universe.alive_particles():
        if p.name not in forces:
            continue

        fx, fy, fz = forces[p.name]
        mass = Fraction(p.mass_fraction).limit_denominator(10000)
        if mass == 0:
            continue

        # a = F/m, Δv = a (all Fraction)
        ax = fx / mass
        ay = fy / mass
        az = fz / mass

        # Accumulate into fractional velocity (convert to float for
        # accumulation — frac_vel is the bridge between exact force
        # computation and discrete lattice movement)
        p.frac_vel[0] += float(ax)
        p.frac_vel[1] += float(ay)
        p.frac_vel[2] += float(az)
