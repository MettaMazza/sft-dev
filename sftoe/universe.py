"""
SFTOE Universe — 3D Rational Lattice Substrate.

The universe is a cubic lattice of SmithianValues. Each cell holds a
field value in (0, 1]. Physics happens through neighbor interactions
using the fold's own operators.

Source: verify_cubic_lattice, verify_coupled_lattice, verify_continuum_limit
        MASTER.md eq.4 (3D curvature operator)
"""
from fractions import Fraction
from sftoe.core import SmithianValue, ONE, fold, take, cast_out
from sftoe.constants import (
    SPATIAL_DIMENSION, LAPLACIAN_3D, C,
    GRAVITY_GENERATOR, EM_GENERATOR, STRONG_GENERATOR,
)
from sftoe.particles import Particle


# ─────────────────────────────────────────────
# Backward-compatible utility functions
# (Used by v1 test suite in tests/test_universe.py)
# ─────────────────────────────────────────────

def odd_part(n):
    """Extract the odd part of an integer: remove all factors of 2."""
    if n == 0:
        return 0
    while n % 2 == 0:
        n //= 2
    return n


def prime_factors(n):
    """Return the set of prime factors of n."""
    factors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1:
        factors.add(n)
    return factors



class Lattice:
    """
    3D cubic lattice of rational field values.

    The lattice is periodic (toroidal) — positions wrap via cast_out.
    Each site stores a field value representing the local vacuum state.

    Attributes:
        depth: Binary tower depth k (lattice has 2^k sites per axis)
        size: Number of sites per axis = 2^depth
        total_sites: size³
        field: 3D dict mapping (i,j,k) -> SmithianValue
    """

    def __init__(self, depth=4):
        self.depth = depth
        self.size = 2 ** depth
        self.total_sites = self.size ** 3
        self.spacing = Fraction(1, self.size)

        # Initialize field: every site starts at ONE (uniform vacuum)
        # This IS the initial condition — ONE, nothing else.
        self.field = {}
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    self.field[(i, j, k)] = ONE

    def get(self, i, j, k):
        """Get field value at site (i, j, k) with periodic boundary."""
        pos = (i % self.size, j % self.size, k % self.size)
        return self.field[pos]

    def set(self, i, j, k, value):
        """Set field value at site (i, j, k)."""
        if not isinstance(value, SmithianValue):
            value = SmithianValue(value)
        pos = (i % self.size, j % self.size, k % self.size)
        self.field[pos] = value

    def neighbors(self, i, j, k):
        """
        Return the 6 nearest neighbors of site (i, j, k) on the cubic lattice.
        Periodic boundary conditions (toroidal topology).

        Source: verify_cubic_lattice — each site has exactly 6 neighbors.
        """
        s = self.size
        return [
            self.field[((i + 1) % s, j, k)],
            self.field[((i - 1) % s, j, k)],
            self.field[(i, (j + 1) % s, k)],
            self.field[(i, (j - 1) % s, k)],
            self.field[(i, j, (k + 1) % s)],
            self.field[(i, j, (k - 1) % s)],
        ]

    def neighbor_sum(self, i, j, k):
        """
        Sum of the 6 neighbor field values.

        For a uniform field at value v, this equals 6v.
        Source: verify_cubic_lattice — sum_neighbors = 6 × U_c
        """
        nbrs = self.neighbors(i, j, k)
        return sum(n.value for n in nbrs)

    def laplacian(self, i, j, k):
        """
        Discrete 3D Laplacian at site (i, j, k).

        Δf = (sum of neighbors - 6 × center) / spacing²

        This is the curvature operator from MASTER.md eq.4.
        Source: verify_cubic_lattice, verify_continuum_limit
        """
        center = self.field[(i % self.size, j % self.size, k % self.size)]
        nbr_sum = self.neighbor_sum(i, j, k)
        numerator = nbr_sum - LAPLACIAN_3D * center.value
        return numerator / (self.spacing * self.spacing)

    def evolve_site(self, i, j, k):
        """
        Evolve one lattice site by one tick using the coupled lattice rule.

        Source: verify_coupled_lattice (proof.py line 23028)
        next_U = U_center/2 + (sum of neighbors)/(2 × 6)

        This is the center-neighbor propagation that conserves total presence.
        """
        center = self.field[(i % self.size, j % self.size, k % self.size)]
        nbr_sum = self.neighbor_sum(i, j, k)

        # next = center/2 + neighbor_sum / (2 * num_neighbors)
        next_val = center.value / 2 + nbr_sum / (2 * LAPLACIAN_3D)

        # Cast out to keep in (0, 1]
        return SmithianValue(cast_out(next_val))

    def evolve_all(self):
        """
        Evolve the entire lattice by one tick.
        All sites update simultaneously (synchronous update).

        Optimization: if every site is identical (uniform field), the
        coupled lattice rule produces exactly the same value:
          next = v/2 + 6v/12 = v/2 + v/2 = v
        This is a mathematical identity — the uniform state is a fixed
        point of the propagation rule. We skip the computation in this
        case because it would produce identical output.
        """
        if self._is_uniform():
            return  # Fixed point — no change

        new_field = {}
        for pos in self.field:
            i, j, k = pos
            new_field[pos] = self.evolve_site(i, j, k)
        self.field = new_field

    def _is_uniform(self):
        """Check if all sites have the same value."""
        vals = iter(self.field.values())
        first = next(vals).value
        return all(v.value == first for v in vals)

    def total_presence(self):
        """
        Sum of all field values across the lattice.
        This should be conserved per verify_coupled_lattice.
        """
        return sum(v.value for v in self.field.values())

    def inject_perturbation(self, i, j, k, value):
        """
        Inject a perturbation (a particle/excitation) at a lattice site.

        The perturbation replaces the field at that site.
        Energy is redistributed from the surrounding vacuum.
        """
        if not isinstance(value, SmithianValue):
            value = SmithianValue(value)

        # Set the field at this site
        self.set(i, j, k, value)


class Universe:
    """
    The fold universe: a 3D lattice with particles evolving on it.

    This is the complete simulation state. The lattice holds the vacuum
    field, and particles live on top of it as excitations.

    Everything starts from ONE. Everything evolves through fold, take,
    and the lattice propagation rule.
    """

    def __init__(self, depth=4):
        self.lattice = Lattice(depth)
        self.particles = []
        self.couplings = []
        self.tick = 0
        self.history = []
        self.events = []

    @property
    def size(self):
        return self.lattice.size

    @property
    def depth(self):
        return self.lattice.depth

    def add_particle(self, name, state, position, particle_type,
                     generation=1, color=None, mass_fraction=None):
        """
        Add a particle to the universe.

        The particle is an excitation of the lattice — its state modifies
        the field at its position.
        """
        p = Particle(
            name=name,
            state=state,
            position=position,
            particle_type=particle_type,
            generation=generation,
            color=color,
            mass_fraction=mass_fraction,
        )
        self.particles.append(p)

        # Perturb the lattice at this position
        self.lattice.inject_perturbation(*position, state)

        self.events.append(f"tick {self.tick}: {name} created at {position}")
        return p

    def remove_particle(self, particle):
        """Remove a particle from the universe."""
        particle.alive = False
        self.events.append(f"tick {self.tick}: {particle.name} removed")

    def alive_particles(self):
        """Return list of living particles."""
        return [p for p in self.particles if p.alive]

    def add_coupling(self, p1, p2, force_type, strength):
        """
        Record a coupling between two particles.

        Force types: 'gravity', 'em', 'strong', 'weak'
        """
        coupling = {
            'from': p1.name,
            'to': p2.name,
            'force': force_type,
            'strength': float(strength),
        }
        self.couplings.append(coupling)
        return coupling

    def snapshot(self):
        """
        Return the current state as a serializable dict.
        Used by the WebSocket server to push to the visualizer.
        """
        particles_data = []
        for p in self.alive_particles():
            particles_data.append({
                'name': p.name,
                'state': str(p.state.value),
                'pos': list(p.position),
                'type': p.particle_type,
                'gen': p.generation,
                'mass': p.mass_fraction,
                'vel': list(p.frac_vel),
                'color': p.color,
            })

        return {
            'tick': self.tick,
            'lattice_size': self.size,
            'particles': particles_data,
            'couplings': self.couplings,
            'invariants': {
                'total_energy': str(self.lattice.total_presence()),
                'particle_count': len(self.alive_particles()),
            },
            'events': self.events[-10:],
        }

    def __repr__(self):
        return (f"Universe(depth={self.depth}, size={self.size}, "
                f"tick={self.tick}, particles={len(self.alive_particles())})")
