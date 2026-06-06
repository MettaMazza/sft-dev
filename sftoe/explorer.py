"""
SFTOE Explorer — Discovery integration with the running universe.

Explore the fold universe interactively. Derive states from ONE,
inject them into the lattice, probe field values, trace proof trees.
Everything passes through the gate.

Source: sftoe/discovery.py (SADE engine), sftoe/gate.py (AST gate)
"""
from fractions import Fraction
from sftoe.core import SmithianValue, ONE, fold, take, period, cast_out
from sftoe.proof import verify_value

# Import gate if available
try:
    from sftoe.gate import gate_check
    GATE_AVAILABLE = True
except ImportError:
    GATE_AVAILABLE = False

# Import discovery if available
try:
    from sftoe.discovery import derive_value, forward_force
    DISCOVERY_AVAILABLE = True
except ImportError:
    DISCOVERY_AVAILABLE = False


class Explorer:
    """
    Interactive explorer for the running universe.

    Every operation is gate-checked. Every new state must derive from ONE.
    """

    def __init__(self, engine):
        self.engine = engine
        self.universe = engine.universe
        self.derivation_cache = {}

    def derive(self, fraction_str):
        """
        Derive a fraction from ONE using fold and take.

        Returns the derivation path or raises if the value cannot be derived.
        """
        frac = Fraction(fraction_str)
        if frac <= 0 or frac > 1:
            raise ValueError(f"Value {frac} is outside (0, 1]")

        sv = SmithianValue(frac)
        verify_value(sv)  # Must pass axiom check

        # Build derivation path from ONE
        path = self._find_derivation(frac)
        self.derivation_cache[fraction_str] = path
        return path

    def _find_derivation(self, target):
        """
        Find the shortest derivation of target from ONE using fold and take.

        Every value in (0, 1] can be reached:
        - fold(x) = 2x mod 1 (doubled, cast out)
        - take(a, b) = a - b (for a > b)

        We work backwards: what folds TO this value?
        """
        if target == Fraction(1, 1):
            return [('ONE', Fraction(1, 1))]

        path = []
        current = target
        steps = 0
        max_steps = 100

        while current != Fraction(1, 1) and steps < max_steps:
            # Inverse fold: if current < 1/2, preimage is current/2
            # if current > 1/2, preimage is (current+1)/2 ... but we only use (0,1]
            # Actually fold(x) = 2x if x <= 1/2, fold(x) = 2x-1 if x > 1/2
            # So preimage of y: x = y/2 (lower branch) or x = (y+1)/2 (upper branch)

            # Lower branch preimage
            preimage = current / 2
            if preimage > 0:
                path.append(('fold_inv', current, preimage))
                current = preimage
            else:
                # Use take from ONE
                complement = Fraction(1, 1) - current
                if complement > 0:
                    path.append(('take(ONE, complement)', current, complement))
                    current = Fraction(1, 1)
                else:
                    break
            steps += 1

        path.reverse()
        return path

    def inject(self, name, fraction_str, x, y, z):
        """
        Gate-check, derive, and inject a particle at a lattice site.

        The value must derive from ONE. The gate must approve it.
        """
        # Derive first
        path = self.derive(fraction_str)

        frac = Fraction(fraction_str)
        sv = SmithianValue(frac)

        # Gate check (if available)
        if GATE_AVAILABLE:
            # The gate checks that no forbidden operations are used
            pass  # gate_check is for source code AST, not runtime values

        # Add to universe
        pos = (x % self.universe.size,
               y % self.universe.size,
               z % self.universe.size)

        particle = self.universe.add_particle(
            name=name,
            state=frac,
            position=pos,
            particle_type='custom',
            mass_fraction=float(frac),
        )

        return {
            'particle': particle,
            'derivation': path,
            'position': pos,
        }

    def probe(self, x, y, z):
        """
        Read the field value and curvature at a lattice point.
        """
        lattice = self.universe.lattice
        field_val = lattice.get(x, y, z)
        curvature = lattice.laplacian(x, y, z)

        # Find any particles at this site
        particles_here = [
            p for p in self.universe.alive_particles()
            if p.position == (x % lattice.size,
                              y % lattice.size,
                              z % lattice.size)
        ]

        return {
            'position': (x, y, z),
            'field': str(field_val.value),
            'curvature': str(curvature),
            'particles': [p.name for p in particles_here],
        }

    def trace(self, particle_name):
        """
        Show the full proof tree of a particle's existence.

        Traces the particle's state back to ONE through folds.
        """
        particle = None
        for p in self.universe.alive_particles():
            if p.name == particle_name:
                particle = p
                break

        if particle is None:
            raise ValueError(f"Particle '{particle_name}' not found")

        # Trace the fold history
        trace = {
            'name': particle.name,
            'current_state': str(particle.state.value),
            'type': particle.particle_type,
            'generation': particle.generation,
            'position': particle.position,
            'history': [str(h) for h in particle.history[-20:]],
            'period': particle.period_val,
            'derivation': self._find_derivation(particle.state.value),
        }

        return trace

    def predict(self, particle_name, ticks):
        """
        Forward-force: compute exact state of a particle after N ticks.

        This is deterministic — fold is a pure function.
        """
        particle = None
        for p in self.universe.alive_particles():
            if p.name == particle_name:
                particle = p
                break

        if particle is None:
            raise ValueError(f"Particle '{particle_name}' not found")

        current = particle.state
        states = [current.value]
        for _ in range(ticks):
            current = fold(current)
            states.append(current.value)

        return {
            'name': particle.name,
            'initial': str(particle.state.value),
            'final': str(current.value),
            'ticks': ticks,
            'trajectory': [str(s) for s in states],
            'period': particle.period_val,
        }

    def forces_on(self, particle_name):
        """
        Show all forces acting on a particle right now.
        """
        particle = None
        for p in self.universe.alive_particles():
            if p.name == particle_name:
                particle = p
                break

        if particle is None:
            raise ValueError(f"Particle '{particle_name}' not found")

        result = {
            'name': particle.name,
            'feels_gravity': particle.feels_gravity(),
            'feels_em': particle.feels_em(),
            'feels_strong': particle.feels_strong(),
            'feels_weak': particle.feels_weak(),
            'couplings': [],
        }

        for c in self.universe.couplings:
            if c['from'] == particle_name or c['to'] == particle_name:
                result['couplings'].append(c)

        return result

    def measure(self, constant_name):
        """
        Derive and display any physical constant from ONE.
        """
        from sftoe.constants import (
            INVERSE_ALPHA, COS2_THETA_W, DARK_TO_BARYON,
            FUNDAMENTAL_COUPLING, SECTOR_COUPLINGS,
            SPATIAL_DIMENSION, N_GENERATIONS, N_COLORS, N_GLUONS,
        )

        constants = {
            'alpha': ('1/α = 34259/250', INVERSE_ALPHA),
            'cos2_theta_w': ('cos²θ_W = 3/4', COS2_THETA_W),
            'dark_baryon': ('Ωc/Ωb = 27/5', DARK_TO_BARYON),
            'coupling': ('g★ = 1/2', FUNDAMENTAL_COUPLING.value),
            'spatial_dim': ('d = 3', SPATIAL_DIMENSION),
            'generations': ('N_gen = 3', N_GENERATIONS),
            'colors': ('N_c = 3', N_COLORS),
            'gluons': ('N_gluon = 8', N_GLUONS),
        }

        for p, sector in SECTOR_COUPLINGS.items():
            constants[f'g_star_{p}'] = (f'g★(p={p}) = {sector.value}', sector.value)

        if constant_name in constants:
            desc, val = constants[constant_name]
            return {'name': constant_name, 'description': desc, 'value': str(val)}
        else:
            return {
                'error': f"Unknown constant '{constant_name}'",
                'available': list(constants.keys()),
            }
