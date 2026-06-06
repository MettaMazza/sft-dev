"""
SFTOE Constants — All derived from ONE and fold.

Every constant here is computed forward from the axiom.
None are typed from measurement. Each traces to a verify_* function in proof.py.
"""
from fractions import Fraction
from sftoe.core import ONE, SmithianValue, fold, take, period, cast_out

# ─────────────────────────────────────────────
# Spatial structure
# ─────────────────────────────────────────────

# Spatial dimension d=3
# Forced by: orbital stability (d<4), potential convergence (d>2), period(1/7)=3
# Source: verify_spatial_dimension (proof.py line 824)
SPATIAL_DIMENSION = 3

# Lattice Laplacians (number of neighbors)
# Source: verify_cubic_lattice, verify_planar_lattice, verify_coupled_lattice
LAPLACIAN_1D = 2   # Two neighbors on a line
LAPLACIAN_2D = 4   # Four neighbors on a plane
LAPLACIAN_3D = 6   # Six neighbors on a cube

# ─────────────────────────────────────────────
# Speed of light
# ─────────────────────────────────────────────

# c = ONE = 1 site per tick (the maximum propagation speed)
# Source: verify_gravitational_wave_speed (proof.py line 772)
C = ONE  # SmithianValue(1)

# ─────────────────────────────────────────────
# Fundamental coupling
# ─────────────────────────────────────────────

# g★ = 1/2 — the fundamental dimensionless coupling
# At this coupling, transverse separation growth factor = ONE
# Source: verify_fundamental_coupling (proof.py line 736)
FUNDAMENTAL_COUPLING = SmithianValue(Fraction(1, 2))

# VEV (vacuum expectation value) = 1/2
# fold(1/2) = ONE — spontaneous symmetry breaking
# Source: verify_ssb
VEV = SmithianValue(Fraction(1, 2))

# ─────────────────────────────────────────────
# Sector generators
# ─────────────────────────────────────────────

# Source: verify_sector_equations (proof.py line 22170)
GRAVITY_GENERATOR = ONE                              # period 1
EM_GENERATOR = SmithianValue(Fraction(1, 3))         # period 2
STRONG_GENERATOR = SmithianValue(Fraction(1, 7))     # period 3

GRAVITY_PERIOD = period(GRAVITY_GENERATOR)   # 1
EM_PERIOD = period(EM_GENERATOR)             # 2
STRONG_PERIOD = period(STRONG_GENERATOR)     # 3

# ─────────────────────────────────────────────
# Four prime sectors
# ─────────────────────────────────────────────

# Source: verify_unified_force_law (proof.py line 9544)
# Couplings g★ = (p-1)/p for each prime sector
PRIME_SECTORS = [2, 3, 5, 7]

def sector_coupling(p):
    """Coupling g★ = (p-1)/p = take(ONE, 1/p) for prime sector p."""
    shortfall = SmithianValue(Fraction(1, p))
    return take(ONE, shortfall)

def sector_shortfall(p):
    """Shortfall = 1/p for prime sector p."""
    return SmithianValue(Fraction(1, p))

SECTOR_COUPLINGS = {p: sector_coupling(p) for p in PRIME_SECTORS}
# {2: 1/2, 3: 2/3, 5: 4/5, 7: 6/7}

# ─────────────────────────────────────────────
# Unification structure
# ─────────────────────────────────────────────

# Source: verify_unification (proof.py line 3608)
# For fold factor m: g★ = (m-1)/m, mixing = 1/(m-1)
# Product relation: mixing × g★ = 1/m

def fold_factor_coupling(m):
    """g★ = (m-1)/m for fold factor m."""
    return SmithianValue(Fraction(m - 1, m))

def fold_factor_mixing(m):
    """Electroweak mixing = 1/(m-1) for fold factor m."""
    return SmithianValue(Fraction(1, m - 1))

# m=2: electroweak sector
EW_FOLD_FACTOR = 2
EW_COUPLING = fold_factor_coupling(EW_FOLD_FACTOR)     # 1/2
EW_MIXING = fold_factor_mixing(EW_FOLD_FACTOR)         # 1/1 = ONE

# m=3: strong/color sector
STRONG_FOLD_FACTOR = 3
STRONG_COUPLING = fold_factor_coupling(STRONG_FOLD_FACTOR)  # 2/3
COLOR_COUNT = STRONG_FOLD_FACTOR                             # 3
STRONG_MIXING = fold_factor_mixing(STRONG_FOLD_FACTOR)       # 1/2

# ─────────────────────────────────────────────
# Fine structure constant
# ─────────────────────────────────────────────

# 1/α = 2^7 + 3^2 × (251/250) = 34259/250 = 137.036
# Source: MASTER.md eq.14, verify_fine_structure_constant
INVERSE_ALPHA = Fraction(34259, 250)

# ─────────────────────────────────────────────
# Electroweak mixing angle
# ─────────────────────────────────────────────

# cos²θ_W = 3/4 (bare)
# Source: verify_ew_mixing
COS2_THETA_W = Fraction(3, 4)

# ─────────────────────────────────────────────
# Generation and color counts
# ─────────────────────────────────────────────

# Source: verify_generation_count, verify_colour_prediction
N_GENERATIONS = 3   # tripling fold fibre carries exactly 3 kinds
N_COLORS = 3        # tripling fold m=3

# Mediator count = m²-1 = 8 (gluons)
# Source: verify_mediator_count
N_GLUONS = N_COLORS ** 2 - 1  # 8

# ─────────────────────────────────────────────
# Cosmological parameters
# ─────────────────────────────────────────────

# Source: verify_dark_to_baryon_fraction
DARK_TO_BARYON = Fraction(27, 5)  # Ωc/Ωb = 5.40

# Source: verify_matter_fraction_tower
MATTER_FRACTION = Fraction(5, 16)  # Ωm = 0.3125

# ─────────────────────────────────────────────
# Lattice structure (derived)
# ─────────────────────────────────────────────

# Covering depth: minimal k such that 2^k >= 3^3 = 27
# Source: verify_dark_matter (proof.py line 11508), verify_navier_stokes_no_blowup
COVERING_DEPTH = 5                      # 2^5 = 32 >= 27
LATTICE_SITES_PER_AXIS = 2 ** COVERING_DEPTH  # 32
LATTICE_FLOOR = Fraction(1, LATTICE_SITES_PER_AXIS)  # 1/32 = s_5

# ─────────────────────────────────────────────
# Quark dressing factors
# ─────────────────────────────────────────────

# Source: verify_quark_dressing_factor
# Covering depths: up-type d=7, down-type d=5
# Dressing: Δ = d_sector / (1/α) = d/137
UP_TYPE_COVERING_DEPTH = 7
DOWN_TYPE_COVERING_DEPTH = 5
UP_TYPE_DRESSING = Fraction(UP_TYPE_COVERING_DEPTH, int(INVERSE_ALPHA))     # 7/137
DOWN_TYPE_DRESSING = Fraction(DOWN_TYPE_COVERING_DEPTH, int(INVERSE_ALPHA)) # 5/137

# ─────────────────────────────────────────────
# Lepton cubic coefficients
# ─────────────────────────────────────────────

# Source: MASTER.md eq.9, verify_lepton_cubic_entire
# x³ - x² + (1/6)x - 1/485 = 0
LEPTON_E2 = Fraction(1, 6)
LEPTON_E3 = Fraction(1, 485)

# ─────────────────────────────────────────────
# Quark cubic coefficients
# ─────────────────────────────────────────────

# Source: particle_validation.py
# Down-type: x³ - x² + (1/8)x - 1/383 = 0
DOWN_QUARK_I1 = Fraction(1, 8)
DOWN_QUARK_I2 = Fraction(1, 383)

# Up-type: x³ - x² + (1/12)x - 1/3071 = 0
UP_QUARK_I1 = Fraction(1, 12)
UP_QUARK_I2 = Fraction(1, 3071)
