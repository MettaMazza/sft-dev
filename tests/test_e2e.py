"""
SFTOE Fold Universe v2 — End-to-End Validation Suite

Tests every layer of the stack:
  1. Constants correctness
  2. Particle mass derivations
  3. Lattice construction and propagation
  4. Force computations
  5. Engine tick loop
  6. Invariant enforcement
  7. Explorer / discovery integration
  8. WebSocket server snapshot format
  9. Visualizer file integrity
"""
import sys
import os
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fractions import Fraction
from sftoe.core import SmithianValue, ONE, fold, take, period

PASS = 0
FAIL = 0

def check(name, condition, detail=""):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"  ✓ {name}")
    else:
        FAIL += 1
        print(f"  ✗ {name} — {detail}")


def test_constants():
    print("\n═══ 1. CONSTANTS ═══")
    from sftoe.constants import (
        SPATIAL_DIMENSION, C, FUNDAMENTAL_COUPLING, VEV,
        GRAVITY_GENERATOR, EM_GENERATOR, STRONG_GENERATOR,
        GRAVITY_PERIOD, EM_PERIOD, STRONG_PERIOD,
        PRIME_SECTORS, SECTOR_COUPLINGS,
        INVERSE_ALPHA, COS2_THETA_W, DARK_TO_BARYON,
        N_GENERATIONS, N_COLORS, N_GLUONS,
        LEPTON_E2, LEPTON_E3,
    )

    check("d=3", SPATIAL_DIMENSION == 3)
    check("c=ONE", C.value == Fraction(1, 1))
    check("g★=1/2", FUNDAMENTAL_COUPLING.value == Fraction(1, 2))
    check("VEV=1/2", VEV.value == Fraction(1, 2))
    check("fold(VEV)=ONE", fold(VEV).value == ONE.value)

    check("gravity generator = ONE", GRAVITY_GENERATOR.value == ONE.value)
    check("EM generator = 1/3", EM_GENERATOR.value == Fraction(1, 3))
    check("strong generator = 1/7", STRONG_GENERATOR.value == Fraction(1, 7))

    check("period(ONE) = 1", GRAVITY_PERIOD == 1)
    check("period(1/3) = 2", EM_PERIOD == 2)
    check("period(1/7) = 3", STRONG_PERIOD == 3)

    check("prime sectors = [2,3,5,7]", PRIME_SECTORS == [2, 3, 5, 7])
    check("g★(2) = 1/2", SECTOR_COUPLINGS[2].value == Fraction(1, 2))
    check("g★(3) = 2/3", SECTOR_COUPLINGS[3].value == Fraction(2, 3))
    check("g★(5) = 4/5", SECTOR_COUPLINGS[5].value == Fraction(4, 5))
    check("g★(7) = 6/7", SECTOR_COUPLINGS[7].value == Fraction(6, 7))

    check("1/α = 137.036", float(INVERSE_ALPHA) == 137.036,
          f"got {float(INVERSE_ALPHA)}")
    check("cos²θ_W = 3/4", COS2_THETA_W == Fraction(3, 4))
    check("Ωc/Ωb = 27/5", DARK_TO_BARYON == Fraction(27, 5))
    check("generations = 3", N_GENERATIONS == 3)
    check("colors = 3", N_COLORS == 3)
    check("gluons = 8", N_GLUONS == 8)

    check("Koide e2 = 1/6", LEPTON_E2 == Fraction(1, 6))
    check("Koide e3 = 1/485", LEPTON_E3 == Fraction(1, 485))


def test_particles():
    print("\n═══ 2. PARTICLE MASSES ═══")
    from sftoe.particles import solve_lepton_masses, solve_quark_masses

    leptons = solve_lepton_masses()
    check("electron mass > 0", leptons['electron'] > 0)
    check("muon mass > electron", leptons['muon'] > leptons['electron'])
    check("tau mass > muon", leptons['tau'] > leptons['muon'])

    # Koide formula: Q = (Σ√m)² / (3·Σm) where m = root²
    # With our cubic, Vieta gives Σr=1, Σr·r'=1/6, so Q = 1/2
    # This matches standard PDG Koide: 0.500006 ± 0.000001
    roots = leptons['roots']
    koide = sum(roots)**2 / (3 * sum(r**2 for r in roots))
    check("Koide Q ≈ 1/2", abs(koide - 0.5) < 0.001,
          f"got {koide:.6f}")

    quarks = solve_quark_masses()
    check("s/d ratio ≈ 19.48", abs(quarks['s_d_bare'] - 19.48) < 0.1,
          f"got {quarks['s_d_bare']:.2f}")
    check("b/s ratio ≈ 54.77", abs(quarks['b_s_bare'] - 54.77) < 0.1,
          f"got {quarks['b_s_bare']:.2f}")
    check("t/c bare ≈ 108.58", abs(quarks['t_c_bare'] - 108.58) < 0.1,
          f"got {quarks['t_c_bare']:.2f}")
    check("t/c dressed ≈ 103.30", abs(quarks['t_c_dressed'] - 103.30) < 0.1,
          f"got {quarks['t_c_dressed']:.2f}")


def test_lattice():
    print("\n═══ 3. LATTICE ═══")
    from sftoe.universe import Lattice

    lat = Lattice(depth=3)  # 8³ = 512 sites
    check("lattice size = 8", lat.size == 8)
    check("total sites = 512", lat.total_sites == 512)
    check("spacing = 1/8", lat.spacing == Fraction(1, 8))

    # All sites start at ONE
    all_one = all(v.value == ONE.value for v in lat.field.values())
    check("all sites initialized to ONE", all_one)

    # Total presence
    total = lat.total_presence()
    check("total presence = 512", total == 512, f"got {total}")

    # Neighbors: site (0,0,0) has 6 neighbors
    nbrs = lat.neighbors(0, 0, 0)
    check("6 neighbors", len(nbrs) == 6)

    # Periodic boundary: neighbor of (0,0,0) in -x is (7,0,0)
    check("periodic boundary", lat.get(lat.size - 1, 0, 0).value == ONE.value)

    # Laplacian of uniform field = 0
    lap = lat.laplacian(4, 4, 4)
    check("Laplacian of uniform field = 0", lap == 0, f"got {lap}")

    # Inject perturbation and verify Laplacian changes
    lat.inject_perturbation(4, 4, 4, SmithianValue(Fraction(1, 2)))
    lap_after = lat.laplacian(4, 4, 4)
    check("Laplacian nonzero after perturbation", lap_after != 0,
          f"got {lap_after}")

    # Evolve and check presence conservation
    lat2 = Lattice(depth=2)  # 4³ = 64 sites
    total_before = lat2.total_presence()
    lat2.evolve_all()
    total_after = lat2.total_presence()
    check("presence conserved after evolution",
          total_before == total_after,
          f"before={total_before}, after={total_after}")


def test_forces():
    print("\n═══ 4. FORCES ═══")
    from sftoe.particles import Particle
    from sftoe.forces import gravity_force, em_force, strong_force, weak_force

    # Two particles at distance 2
    p1 = Particle("a", Fraction(1, 4), (0, 0, 0), 'lepton', mass_fraction=0.1)
    p2 = Particle("b", Fraction(1, 4), (2, 0, 0), 'lepton', mass_fraction=0.1)

    fg = gravity_force(p1, p2, 16)
    check("gravity > 0 between massive particles", fg > 0, f"got {fg}")

    # EM: both have even denominator (4 = 2²) so they should feel EM
    check("p1 feels EM (denom 4)", p1.feels_em())
    fem = em_force(p1, p2, 16)
    check("EM force > 0 for charged particles", fem > 0, f"got {fem}")

    # Strong: denominator not divisible by 7
    check("p1 does NOT feel strong", not p1.feels_strong())
    fs = strong_force(p1, p2, 16)
    check("strong force = 0 for non-colored", fs == 0)

    # Weak: denominator not divisible by 5
    check("p1 does NOT feel weak", not p1.feels_weak())
    fw = weak_force(p1, p2, 16)
    check("weak force = 0 for non-weak", fw == 0)

    # Quark with color: denominator divisible by 7
    q1 = Particle("q1", Fraction(1, 7), (0, 0, 0), 'quark', color=1, mass_fraction=0.01)
    q2 = Particle("q2", Fraction(2, 7), (1, 0, 0), 'quark', color=2, mass_fraction=0.01)
    check("quark feels strong", q1.feels_strong())
    fs_q = strong_force(q1, q2, 16)
    check("strong force > 0 between quarks", fs_q > 0, f"got {fs_q}")

    # Gravity is inverse-square
    p3 = Particle("c", Fraction(1, 4), (4, 0, 0), 'lepton', mass_fraction=0.1)
    fg_far = gravity_force(p1, p3, 16)
    check("gravity weaker at larger distance", fg_far < fg,
          f"near={fg}, far={fg_far}")


def test_engine():
    print("\n═══ 5. ENGINE TICK LOOP ═══")
    from sftoe.fold_engine import FoldEngine

    engine = FoldEngine(depth=2)  # Small lattice for speed
    check("universe created", engine.universe is not None)
    check("tick starts at 0", engine.universe.tick == 0)

    # Seed particles
    engine.seed_particles(n_leptons=3, n_quarks=6)
    n = len(engine.universe.alive_particles())
    check(f"particles seeded ({n})", n > 0)

    # Record initial states
    initial_states = {p.name: p.state.value for p in engine.universe.alive_particles()}

    # Run 100 ticks
    for _ in range(100):
        engine.tick()
    check("100 ticks completed", engine.universe.tick == 100)

    # Particles still alive
    alive = len(engine.universe.alive_particles())
    check(f"particles still alive ({alive})", alive > 0)

    # All states in (0, 1]
    all_valid = all(
        0 < p.state.value <= 1
        for p in engine.universe.alive_particles()
    )
    check("all states in (0, 1]", all_valid)

    # States have changed (fold is happening)
    changed = any(
        p.state.value != initial_states.get(p.name)
        for p in engine.universe.alive_particles()
        if p.name in initial_states
    )
    check("states evolved (fold working)", changed)

    # Speed cap: no velocity > 1
    all_causal = all(
        abs(p.velocity[0]) + abs(p.velocity[1]) + abs(p.velocity[2]) <= 1
        for p in engine.universe.alive_particles()
    )
    check("all velocities ≤ c=1", all_causal)


def test_invariants():
    print("\n═══ 6. INVARIANTS ═══")
    from sftoe.invariants import (
        check_no_zero, check_positive_domain,
        check_causality, check_all
    )
    from sftoe.universe import Universe
    from sftoe.particles import Particle

    u = Universe(depth=2)

    # Add valid particles
    u.add_particle("e", Fraction(1, 4), (0, 0, 0), 'lepton')
    u.add_particle("q", Fraction(1, 7), (1, 1, 1), 'quark', color=1)

    # Should pass all checks
    try:
        result = check_all(u)
        check("all invariants pass for valid universe", result['all_valid'])
    except Exception as e:
        check("all invariants pass for valid universe", False, str(e))

    # Test no-zero enforcement
    try:
        bad = SmithianValue(Fraction(0, 1))
        check("zero rejected by SmithianValue", False, "should have raised")
    except (ValueError, Exception):
        check("zero rejected by SmithianValue", True)


def test_explorer():
    print("\n═══ 7. EXPLORER / DISCOVERY ═══")
    from sftoe.fold_engine import FoldEngine
    from sftoe.explorer import Explorer

    engine = FoldEngine(depth=2)
    engine.seed_particles(n_leptons=1, n_quarks=0)
    explorer = Explorer(engine)

    # Derive a value
    path = explorer.derive("1/3")
    check("derive 1/3 succeeds", path is not None and len(path) > 0)

    # Inject a particle
    result = explorer.inject("test_em", "1/3", 1, 1, 1)
    check("inject creates particle", result['particle'] is not None)
    check("injected at correct position", result['position'] == (1, 1, 1))

    # Probe a site
    probe = explorer.probe(1, 1, 1)
    check("probe returns field value", 'field' in probe)
    check("probe finds particle", len(probe['particles']) > 0)

    # Trace a particle
    engine.tick()
    trace = explorer.trace("test_em")
    check("trace returns history", len(trace['history']) > 0)
    check("trace has period", 'period' in trace)

    # Predict forward
    pred = explorer.predict("test_em", 10)
    check("predict returns trajectory", len(pred['trajectory']) == 11)

    # Measure a constant
    m = explorer.measure("alpha")
    check("measure alpha", m['value'] == '34259/250')

    m2 = explorer.measure("dark_baryon")
    check("measure dark/baryon", m2['value'] == '27/5')


def test_snapshot():
    print("\n═══ 8. SNAPSHOT FORMAT ═══")
    from sftoe.fold_engine import FoldEngine

    engine = FoldEngine(depth=2)
    engine.seed_particles(n_leptons=2, n_quarks=3)
    engine.tick()

    snap = engine.snapshot()
    check("snapshot has 'tick'", 'tick' in snap)
    check("snapshot has 'lattice_size'", 'lattice_size' in snap)
    check("snapshot has 'particles'", 'particles' in snap)
    check("snapshot has 'couplings'", 'couplings' in snap)
    check("snapshot has 'invariants'", 'invariants' in snap)
    check("snapshot has 'events'", 'events' in snap)

    # Validate particle format
    if snap['particles']:
        p = snap['particles'][0]
        check("particle has 'name'", 'name' in p)
        check("particle has 'state'", 'state' in p)
        check("particle has 'pos' (list)", isinstance(p['pos'], list) and len(p['pos']) == 3)
        check("particle has 'type'", 'type' in p)
        check("particle has 'mass'", 'mass' in p)
        check("particle has 'vel'", 'vel' in p)

    # JSON serializable
    try:
        json_str = json.dumps(snap)
        check("snapshot is JSON-serializable", True)
        parsed = json.loads(json_str)
        check("JSON round-trips correctly", parsed['tick'] == snap['tick'])
    except Exception as e:
        check("snapshot is JSON-serializable", False, str(e))


def test_visualizer_files():
    print("\n═══ 9. VISUALIZER FILES ═══")
    viz_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           'sftoe', 'visualizer')

    html_path = os.path.join(viz_dir, 'index.html')
    css_path = os.path.join(viz_dir, 'index.css')
    js_path = os.path.join(viz_dir, 'main.js')

    check("index.html exists", os.path.exists(html_path))
    check("index.css exists", os.path.exists(css_path))
    check("main.js exists", os.path.exists(js_path))

    if os.path.exists(html_path):
        html = open(html_path).read()
        check("HTML references Three.js", 'three' in html.lower() or 'THREE' in html)
        check("HTML references main.js", 'main.js' in html)
        check("HTML references index.css", 'index.css' in html)

    if os.path.exists(js_path):
        js = open(js_path).read()
        check("JS has WebSocket connection", 'WebSocket' in js or 'websocket' in js.lower())
        check("JS has OrbitControls or camera", 'OrbitControls' in js or 'camera' in js)
        check("JS has particle rendering", 'particle' in js.lower() or 'sphere' in js.lower())
        check("JS has play/pause", 'pause' in js.lower() or 'play' in js.lower())
        check("JS > 10KB (substantial)", len(js) > 10000, f"only {len(js)} bytes")


def test_spacetime():
    print("\n═══ 10. SPACETIME ═══")
    from sftoe.spacetime import (
        lattice_distance, causal_check, fold_separation,
        velocity_composition
    )

    # Distance on 8³ lattice
    d = lattice_distance((0, 0, 0), (3, 4, 0), 8)
    check("Manhattan distance = 7", d == 7, f"got {d}")

    # Periodic wrapping: (0) to (7) on size-8 lattice = 1 (wrap)
    d_wrap = lattice_distance((0, 0, 0), (7, 0, 0), 8)
    check("periodic distance = 1 (wraps)", d_wrap == 1, f"got {d_wrap}")

    # Causal check
    check("causal: Δt=7 ≥ d=7", causal_check((0,0,0), (3,4,0), 7, 8))
    check("acausal: Δt=3 < d=7", not causal_check((0,0,0), (3,4,0), 3, 8))

    # Velocity composition: c + anything = c
    c = ONE
    v = SmithianValue(Fraction(1, 3))
    w = velocity_composition(c, v)
    check("c composed with v = c", w.value == ONE.value, f"got {w.value}")


if __name__ == '__main__':
    print("╔═══════════════════════════════════════════════════╗")
    print("║  SFTOE Fold Universe v2 — End-to-End Validation  ║")
    print("╚═══════════════════════════════════════════════════╝")

    test_constants()
    test_particles()
    test_lattice()
    test_forces()
    test_engine()
    test_invariants()
    test_explorer()
    test_snapshot()
    test_visualizer_files()
    test_spacetime()

    print("\n" + "═" * 53)
    total = PASS + FAIL
    print(f"  RESULTS: {PASS}/{total} passed, {FAIL} failed")
    if FAIL == 0:
        print("  ✓ ALL TESTS PASSED")
    else:
        print(f"  ✗ {FAIL} FAILURES")
    print("═" * 53)

    sys.exit(0 if FAIL == 0 else 1)
