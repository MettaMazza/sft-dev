"""
SFTOE Particles — Every mass derived from the fold's cubic equations.

No mass is typed from measurement. Each comes from the Koide cubic (leptons)
or the quark cubics, with dressing factors forced by covering depths.

Sources:
  - verify_lepton_cubic_entire, verify_charged_leptons
  - verify_quark_mass_confinement_lift, verify_quark_dressing_factor
  - verify_proton_electron_ratio
  - verify_generation_count, verify_colour_prediction
  - verify_mediator_count
  - particle_validation.py
  - MASTER.md Sections 4-5 (Paper 2)
"""
from fractions import Fraction
from sftoe.core import SmithianValue, ONE, fold, take, period
from sftoe.constants import (
    LEPTON_E2, LEPTON_E3,
    DOWN_QUARK_I1, DOWN_QUARK_I2,
    UP_QUARK_I1, UP_QUARK_I2,
    INVERSE_ALPHA,
    UP_TYPE_COVERING_DEPTH, DOWN_TYPE_COVERING_DEPTH,
    N_COLORS, N_GENERATIONS, N_GLUONS,
    COLOR_COUNT,
)


def _bisect_cubic(i1, i2, lo, hi):
    """
    Find root of x³ - x² + i1·x - i2 = 0 in [lo, hi] by bisection.
    64 iterations give machine precision.
    """
    def f(x):
        return x**3 - x**2 + float(i1) * x - float(i2)

    a, b = float(lo), float(hi)
    sign_a = f(a) > 0.0
    for _ in range(64):
        c = (a + b) / 2
        if (f(c) > 0.0) == sign_a:
            a = c
        else:
            b = c
    return (a + b) / 2


def solve_lepton_masses():
    """
    Solve the Koide cubic: x³ - x² + (1/6)x - 1/485 = 0

    Returns dict with keys 'electron', 'muon', 'tau', each mapping to
    the mass-squared root (x_i²).

    Source: MASTER.md eq.9, verify_lepton_cubic_entire
    """
    x1 = _bisect_cubic(LEPTON_E2, LEPTON_E3, 0.0, 0.05)
    x2 = _bisect_cubic(LEPTON_E2, LEPTON_E3, 0.05, 0.35)
    x3 = _bisect_cubic(LEPTON_E2, LEPTON_E3, 0.7, 0.99)

    return {
        'electron': x1**2,
        'muon': x2**2,
        'tau': x3**2,
        'roots': sorted([x1, x2, x3]),
    }


def solve_quark_masses():
    """
    Solve the quark cubics.

    Down-type: x³ - x² + (1/8)x - 1/383 = 0  → d, s, b
    Up-type:   x³ - x² + (1/12)x - 1/3071 = 0 → u, c, t

    Returns bare and dressed mass ratios.

    Source: particle_validation.py, verify_quark_mass_confinement_lift
    """
    # Down-type cubic
    d_roots = [
        _bisect_cubic(DOWN_QUARK_I1, DOWN_QUARK_I2, 0.0, 0.05),
        _bisect_cubic(DOWN_QUARK_I1, DOWN_QUARK_I2, 0.05, 0.35),
        _bisect_cubic(DOWN_QUARK_I1, DOWN_QUARK_I2, 0.7, 0.99),
    ]
    d_masses = [x**2 for x in d_roots]

    # Up-type cubic
    u_roots = [
        _bisect_cubic(UP_QUARK_I1, UP_QUARK_I2, 0.0, 0.05),
        _bisect_cubic(UP_QUARK_I1, UP_QUARK_I2, 0.05, 0.35),
        _bisect_cubic(UP_QUARK_I1, UP_QUARK_I2, 0.7, 0.99),
    ]
    u_masses = [x**2 for x in u_roots]

    # Bare ratios
    s_d_bare = d_masses[1] / d_masses[0]
    b_s_bare = d_masses[2] / d_masses[1]
    t_c_bare = u_masses[2] / u_masses[1]

    # Dressing: R_dressed = R_bare × (1/α) / (1/α + d_sector)
    # Source: verify_quark_dressing_factor
    inv_alpha = float(INVERSE_ALPHA)
    up_dressed_factor = inv_alpha / (inv_alpha + UP_TYPE_COVERING_DEPTH)
    down_dressed_factor = inv_alpha / (inv_alpha + DOWN_TYPE_COVERING_DEPTH)

    return {
        'down_masses': d_masses,    # [d, s, b] as mass fractions
        'up_masses': u_masses,      # [u, c, t] as mass fractions
        's_d_bare': s_d_bare,
        'b_s_bare': b_s_bare,
        't_c_bare': t_c_bare,
        's_d_dressed': s_d_bare * down_dressed_factor,
        'b_s_dressed': b_s_bare * down_dressed_factor,
        't_c_dressed': t_c_bare * up_dressed_factor,
    }


def proton_electron_ratio():
    """
    Compute mp/me from the lepton cubic.

    Source: verify_proton_electron_ratio, particle_validation.py
    mp/me = (1/3) × (1 - me/mμ) / me
    """
    leptons = solve_lepton_masses()
    me = leptons['electron']
    mmu = leptons['muon']
    em_correction = (mmu - me) / mmu
    proton = (1.0 / 3.0) * em_correction
    return proton / me


# ─────────────────────────────────────────────
# Particle type classification
# ─────────────────────────────────────────────

class ParticleType:
    """Classifies a fold state by its denominator prime structure."""

    LEPTON = 'lepton'
    QUARK = 'quark'
    BOSON = 'boson'
    BARYON = 'baryon'

    # Force sensitivity based on denominator factors
    @staticmethod
    def feels_gravity():
        """All massive particles feel gravity. Always True."""
        return True

    @staticmethod
    def feels_em(denominator):
        """Charged particles: denominator divisible by 2 (binary fold sector)."""
        return denominator % 2 == 0

    @staticmethod
    def feels_strong(denominator):
        """Colored particles: denominator divisible by 7 (strong generator 1/7)."""
        return denominator % 7 == 0

    @staticmethod
    def feels_weak(denominator):
        """Weak interaction: denominator divisible by 5 (prime sector 5)."""
        return denominator % 5 == 0


# ─────────────────────────────────────────────
# Particle registry — the full catalogue
# ─────────────────────────────────────────────

class Particle:
    """
    A particle on the fold lattice.

    Attributes:
        name: Human-readable name
        state: SmithianValue — the fold state (mass-energy fraction)
        position: (i, j, k) — lattice coordinates
        particle_type: lepton/quark/boson/baryon
        generation: 1, 2, or 3
        color: None for leptons/bosons, 1-3 for quarks
        mass_fraction: Dimensionless mass from the cubics
        velocity: (vi, vj, vk) — lattice velocity in sites/tick
    """

    def __init__(self, name, state, position, particle_type,
                 generation=1, color=None, mass_fraction=None):
        if not isinstance(state, SmithianValue):
            state = SmithianValue(state)
        self.name = name
        self.state = state
        self.position = position
        self.particle_type = particle_type
        self.generation = generation
        self.color = color
        self.mass_fraction = mass_fraction or float(state.value)
        self.velocity = (0, 0, 0)       # integer lattice steps this tick
        self.frac_vel = [0.0, 0.0, 0.0]  # accumulated fractional velocity
        self.alive = True
        self.history = [state.value]

    @property
    def denominator(self):
        return self.state.value.denominator

    @property
    def period_val(self):
        return period(self.state)

    def feels_gravity(self):
        return ParticleType.feels_gravity()

    def feels_em(self):
        return ParticleType.feels_em(self.denominator)

    def feels_strong(self):
        return ParticleType.feels_strong(self.denominator)

    def feels_weak(self):
        return ParticleType.feels_weak(self.denominator)

    def fold_step(self):
        """Advance this particle's state by one fold."""
        self.state = fold(self.state)
        self.history.append(self.state.value)

    def move(self, lattice_size):
        """Move particle using accumulated fractional velocity.

        Each tick:
        1. Extract integer steps from frac_vel (floor for positive, ceil for negative)
        2. Cap total displacement to c=1 per tick (Manhattan norm)
        3. Apply the displacement to position (with wrapping)
        4. Remainder stays in frac_vel for next tick

        Source: verify_minkowski_causal — nothing moves faster than c.
        """
        import math
        steps = [0, 0, 0]
        for axis in range(3):
            if self.frac_vel[axis] >= 0:
                steps[axis] = int(math.floor(self.frac_vel[axis]))
            else:
                steps[axis] = int(math.ceil(self.frac_vel[axis]))
            self.frac_vel[axis] -= steps[axis]

        # Speed cap: total Manhattan displacement ≤ 1 per tick
        total_step = abs(steps[0]) + abs(steps[1]) + abs(steps[2])
        if total_step > 1:
            # Find dominant axis and cap to 1 step in that direction
            abs_steps = [abs(s) for s in steps]
            dominant = abs_steps.index(max(abs_steps))
            # Return excess to frac_vel and move only 1 step
            for axis in range(3):
                if axis == dominant:
                    self.frac_vel[axis] += steps[axis] - (1 if steps[axis] > 0 else -1)
                    steps[axis] = 1 if steps[axis] > 0 else -1
                else:
                    self.frac_vel[axis] += steps[axis]
                    steps[axis] = 0

        self.velocity = tuple(steps)
        i, j, k = self.position
        self.position = (
            (i + steps[0]) % lattice_size,
            (j + steps[1]) % lattice_size,
            (k + steps[2]) % lattice_size,
        )

    def __repr__(self):
        return (f"Particle({self.name}, state={self.state}, "
                f"pos={self.position}, type={self.particle_type})")


# ─────────────────────────────────────────────
# Pre-computed mass catalogue
# ─────────────────────────────────────────────

_lepton_masses = None
_quark_masses = None

def get_lepton_masses():
    global _lepton_masses
    if _lepton_masses is None:
        _lepton_masses = solve_lepton_masses()
    return _lepton_masses

def get_quark_masses():
    global _quark_masses
    if _quark_masses is None:
        _quark_masses = solve_quark_masses()
    return _quark_masses
