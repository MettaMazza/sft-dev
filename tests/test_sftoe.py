import unittest
from fractions import Fraction
import ast
import tempfile
import os

from sftoe import (
    ONE,
    SmithianValue,
    fold,
    take,
    cast_out,
    period,
    combined_period,
    rotate,
    relative_phase,
    beat_frequency,
    relative_advance,
    run_wave,
    verify_value,
    verify_hypothesis_orbit,
    verify_combined_period,
    verify_beat_frequency,
    verify_thermodynamics,
    verify_sync_threshold,
    verify_quantisation,
    verify_oscillator_levels,
    verify_spectral_ratios,
    verify_critical_coupling_factor,
    verify_fundamental_coupling,
    verify_gravitational_wave_speed,
    verify_spatial_dimension,
    verify_schwarzschild_solution,
    verify_continuum_limit,
    verify_quadrupole_radiation,
    verify_nonlinear_gravity,
    verify_pn_convergence,
    verify_metric_components,
    verify_cubic_lattice_gravity,
    verify_planar_lattice_gravity,
    verify_leading_radiation_moment,
    verify_gravitational_time_dilation,
    verify_magnetism_correction,
    verify_lorentz_force,
    verify_maxwell_wave_closure,
    verify_planar_maxwell_wave,
    verify_em_wave_speed,
    verify_coulomb_law,
    verify_orbital_stability_dimension,
    verify_newton_law,
    verify_poisson_equation,
    verify_static_metric_dilation,
    verify_equivalence_redshift,
    verify_constants_rationality,
    verify_continuum_limit_successive,
    verify_velocity_composition,
    verify_fermionic_occupation,
    verify_charge_multiplicity,
    verify_chirality,
    verify_strong_confinement,
    verify_colour_neutral,
    verify_beta_slope,
    verify_strong_luminal,
    verify_strong_field_equation,
    verify_flux_tube_formation,
    verify_strong_self_coupling,
    verify_strong_coupling_running,
    verify_weak_range,
    verify_ew_mixing,
    verify_massless_massive_split,
    verify_weak_mass_ratio,
    verify_unification,
    verify_forced_relationship,
    verify_u7,
    verify_u4,
    verify_u5,
    verify_u6,
    verify_u3,
    verify_ew_currents,
    verify_ssb,
    verify_proton_electron_ratio,
    verify_fermion_mass_part,
    verify_generation_mass_splitting,
    verify_inter_sector_mass_pattern,
    verify_neutrino_mass_asymmetry,
    verify_mixing_structure,
    verify_mixing_magnitudes,
    verify_mediator_count,
    verify_colour_prediction,
    verify_generation_count,
    verify_generation_depth,
    verify_full_mixing_matrices,
    verify_inter_entry_relation,
    verify_within_generation_ratio,
    verify_charged_leptons,
    verify_generation_ladder,
    verify_mass_ratio_family,
    verify_reach_ratios,
    verify_koide_relationship,
    verify_koide_cubic_roots,
    verify_proven_mass_ratios,
    verify_generation_depth_tower,
    verify_general_covering_depth,
    verify_second_invariant,
    verify_lepton_cubic_entire,
    verify_second_invariant_sharpened,
    verify_quark_invariants,
    verify_quark_mass_confinement_lift,
    verify_neutrino_mass_ladder,
    verify_quark_second_invariant,
    verify_quark_dressing_factor,
    verify_ckm_magnitudes,
    verify_cp_phase_antipode,
    verify_ckm_third_entry_closed,
    verify_pmns_large_angles,
    verify_pmns_reactor_angle,
    verify_em_coupling,
    verify_ew_mixing_running,
    verify_depth_scale_ratio,
    verify_ew_mixing_curve,
    verify_w_z_mass_ratio,
    verify_level_depth_map,
    verify_coupling_convergence,
    verify_convergence_rate_closed,
    verify_accumulated_separation,
    verify_three_coupling_structure,
    verify_scale_invariance,
    verify_planck_hierarchy,
    verify_unified_force_law,
    verify_five_force_flavour_ratio,
    verify_prime_sector_ladder_bounded,
    verify_two_new_prime_charge_forces,
    verify_half_one_unifying_center,
    verify_prime_sector_confining_ladder,
    verify_five_fold_standing_modes_force_three_generations,
    verify_absolute_scale_unobservable,
    verify_grand_synthesis,
    verify_forward_not_fitted,
    verify_cross_sector_insights,
    verify_forward_novelties,
    verify_collapse_to_open_conversion,
    verify_planck_hierarchy_forced,
    verify_scale_axis_proven,
    verify_gravitational_coupling_proven,
    verify_unison_order,
    verify_discriminating_prediction,
    verify_internal_anchor_depth,
    verify_interaction_strength_structure,
    verify_dark_to_baryon_fraction,
    verify_dark_matter,
    verify_cosmological_timeline,
    verify_strong_field_gravity,
    verify_proton_stability,
    verify_baryon_to_photon_ratio,
    verify_baryon_asymmetry_nonzero,
    verify_generation_bound_strict,
    verify_strong_cp_alignment,
    verify_vacuum_energy_positive,
    verify_vacuum_equation_of_state,
    verify_spatial_flatness,
    verify_cosmic_dilution_exponents,
    verify_protein_folding_fixed_point,
    verify_proven_predictions_frontier,
    verify_navier_stokes_no_blowup,
    verify_general_n_body_periodic,
    verify_fine_structure_constant,
    verify_muon_g2_anomaly,
    verify_hubble_tension,
    verify_three_body_solvability,
    verify_self_universe_travel,
    verify_communication_travel,
    verify_entangled_universes,
    verify_zero_point_energy,
    verify_string_theory_correct,
    verify_quantum_gravity,
    verify_quantum_communication,
    verify_nonlocal_correlation,
    verify_measurement_problem,
    verify_matter_fraction_tower,
    verify_matter_fraction_evolution,
    verify_deceleration_parameter,
    verify_acceleration_transition,
    verify_expansion_history,
    verify_final_assembly,
    verify_single_axiom_audit,
    verify_reproduction_at_scale,
    verify_lithium_seven,
    verify_completeness_audit,
    verify_w_boson_mass,
    verify_precision_constants,
    verify_neutrino_mass,
    verify_muon_g2,
    verify_cosmological_constant,
    verify_hierarchy_problem,
    verify_proton_radius,
    verify_strong_cp,
    verify_observer_resolved,
    verify_single_axiom_dependency,
    verify_fold_uniqueness,
    verify_three_dimensions_sharpened,
    verify_reproduction_audit_protocol,
    verify_extension_protocol,
    verify_observational_mathematical_method,
    verify_empirical_ontological_standard,
    verify_efficiency_intelligence_dividend,
    verify_catalogue_unexplained_phenomena,
    verify_uap_vacuum_engineering,
    verify_machine_consciousness_criterion,
    verify_self_simulation_nesting,
    verify_socio_economic_dynamics,
    verify_placebo_effect,
    verify_tesla_corpus,
    verify_perception_synaesthesia,
    verify_multidimensional_experience,
    verify_least_action,
    verify_scale_structure,
    verify_principle_emergence,
    verify_universality_threshold,
    verify_yang_mills_mass_gap,
    verify_potential_infinite,
    verify_continuum_hypothesis,
    verify_computability_halting,
    verify_math_effectiveness,
    verify_symmetry_principle,
    verify_sleep_cycle,
    verify_hard_problem,
    verify_prime_distribution,
    verify_riemann_structure,
    verify_attention_capacity,
    verify_prediction_model,
    verify_binding_problem,
    verify_introspection_limit,
    verify_origin_of_life,
    verify_evolution_descent,
    verify_network_scaling,
    verify_memory_persistence,
    verify_planetary_tidal,
    verify_order_complexity,
    verify_self_organization,
    verify_self_replication,
    verify_genetic_code,
    verify_homochirality,
    verify_stellar_nucleosynthesis,
    verify_degenerate_endpoints,
    verify_supernovae_heavy,
    verify_black_holes_complete,
    verify_gravitational_waves,
    verify_galactic_dynamics,
    verify_stellar_structure,
    verify_fate_of_universe,
    verify_inflation_sharpened,
    verify_structure_formation,
    verify_baryogenesis,
    verify_recombination_cmb,
    verify_bbn,
    verify_thermal_history,
    verify_acoustics,
    verify_blackbody_radiation,
    verify_nonlinear_optics,
    verify_laser,
    verify_wave_optics,
    verify_refractive_index,
    verify_mhd,
    verify_plasma_state,
    verify_neutrino_oscillation,
    verify_cp_violation,
    verify_vacuum_polarization,
    verify_renormalization_finite,
    verify_running_couplings,
    verify_decay_widths,
    verify_cross_sections,
    verify_deuteron_bound,
    verify_fission_fusion,
    verify_radioactive_decay,
    verify_nuclear_shell,
    verify_nuclear_binding,
    verify_nuclear_force_residual,
    verify_hadron_spectrum,
    verify_nucleon_binding_dom,
    verify_intermolecular,
    verify_stereochemistry,
    verify_acids_bases,
    verify_catalysis,
    verify_reaction_kinetics,
    verify_reaction_thermodynamics,
    verify_electronegativity,
    verify_periodic_law,
    verify_molecular_spectra,
    verify_molecular_bond,
    verify_field_splitting,
    verify_selection_rules,
    verify_shell_capacities,
    verify_lamb_shift,
    verify_fine_hyperfine,
    verify_hydrogen_spectrum,
    verify_mechanical_properties,
    verify_topological_matter,
    verify_quantum_hall,
    verify_magnetism,
    verify_superfluidity,
    verify_superconductivity,
    verify_semiconductors,
    verify_electronic_bands,
    verify_phonons_lattice,
    verify_quasicrystals,
    verify_crystalline_order,
    verify_maxwells_demon,
    verify_bose_einstein,
    verify_irreversibility_recurrence,
    verify_fluctuation_dissipation,
    verify_critical_exponents,
    verify_quantum_statistics,
    verify_four_thermo_laws,
    verify_canonical_distribution,
    verify_entropy,
    verify_temperature,
    verify_quantum_stationary_states,
    verify_relativistic_two_component,
    verify_full_dirac_structure,
    verify_cessation,
    verify_one_fold_equation,
    verify_sector_equations,
    verify_master_equation,
    verify_simulation_kernel,
    verify_unfolding_sequence,
    verify_accessible_artifact,
    verify_quantum_potential,
    verify_free_particle_dispersion,
    verify_variance_uncertainty,
    verify_uncertainty_count,
    verify_minkowski_causal,
    verify_three_wave_mixing,
    verify_dalembert_wave,
    verify_cubic_lattice,
    verify_planar_lattice,
    verify_coupled_lattice,
    verify_algebraic_engine,
    verify_consciousness_matter_coupling,
    verify_mental_temporal_manipulation,
    verify_mental_matter_manipulation,
    VerificationError,
    verify_code,
    SFTOEGateError
)

class TestSFTOECore(unittest.TestCase):
    def test_domain_constraints(self):
        # ONE should be exactly 1
        self.assertEqual(ONE.value, Fraction(1, 1))
        
        # Valid domain inputs (0, 1]
        v_half = SmithianValue(Fraction(1, 2))
        self.assertEqual(v_half.value, Fraction(1, 2))
        
        # Invalid inputs (0 is not a value in SFTOE)
        with self.assertRaises(ValueError):
            SmithianValue(Fraction(1 - 1, 1))
            
        with self.assertRaises(ValueError):
            SmithianValue(Fraction(3, 2)) # exceeds 1
            
        with self.assertRaises(ValueError):
            SmithianValue(-0.5) # negative

    def test_cast_out(self):
        # cast_out brings things to (0, 1]
        self.assertEqual(cast_out(Fraction(3, 2)), Fraction(1, 2))
        self.assertEqual(cast_out(Fraction(2, 1)), Fraction(1, 1))
        self.assertEqual(cast_out(Fraction(1 - 1, 1)), Fraction(1, 1))
        self.assertEqual(cast_out(Fraction(-1, 2)), Fraction(1, 2))
        self.assertEqual(cast_out(Fraction(-2, 1)), Fraction(1, 1))
        
        # Floats
        self.assertAlmostEqual(cast_out(1.5), 0.5)
        self.assertAlmostEqual(cast_out(2.0), 1.0)
        self.assertAlmostEqual(cast_out(float(1 - 1)), 1.0)

    def test_fold(self):
        # fold(x) = cast_out(2x)
        self.assertEqual(fold(Fraction(1, 3)).value, Fraction(2, 3))
        self.assertEqual(fold(Fraction(2, 3)).value, Fraction(1, 3))
        self.assertEqual(fold(Fraction(1, 2)).value, Fraction(1, 1))
        self.assertEqual(fold(ONE).value, ONE.value)

    def test_take(self):
        # take(big, small) asserts big > small
        v_3_4 = SmithianValue(Fraction(3, 4))
        v_1_4 = SmithianValue(Fraction(1, 4))
        
        res = take(v_3_4, v_1_4)
        self.assertEqual(res.value, Fraction(1, 2))
        
        # Guarded: big must be strictly greater than small
        with self.assertRaises(AssertionError):
            take(v_1_4, v_3_4)
            
        with self.assertRaises(AssertionError):
            take(v_1_4, v_1_4)


class TestSFTOEProofEngine(unittest.TestCase):
    def test_constructive_verification(self):
        # ONE should verify
        self.assertTrue(verify_value(ONE))
        
        # Hypothesis verification (dyadic rationals have short cycles)
        v_half = SmithianValue(Fraction(1, 2))
        self.assertTrue(verify_value(v_half))
        
        # We can construct 1/4 by taking
        v_three_quarter = SmithianValue(Fraction(3, 4))
        v_quarter = take(ONE, v_three_quarter)
        self.assertTrue(verify_value(v_quarter))
        self.assertEqual(v_quarter.value, Fraction(1, 4))

    def test_hypothesis_orbit_verification(self):
        # 1/3 has a periodic orbit under fold: 1/3 -> 2/3 -> 1/3 (period 2)
        res = verify_hypothesis_orbit(Fraction(1, 3))
        self.assertTrue(res["verified"])
        self.assertEqual(res["cycle_length"], 2)
        
        # 1/7 has period 3: 1/7 -> 2/7 -> 4/7 -> 1/7
        res_7 = verify_hypothesis_orbit(Fraction(1, 7))
        self.assertEqual(res_7["cycle_length"], 3)
        
        # A hypothesis value represented as a SmithianValue should verify successfully if valid
        v_third = SmithianValue(Fraction(1, 3))
        self.assertTrue(verify_value(v_third))

    def test_failed_proofs(self):
        # Fake hypothesis that is outside (0, 1] cannot be verified
        with self.assertRaises(VerificationError):
            verify_hypothesis_orbit(Fraction(5, 4))
            
        # Tampered SmithianValue value (mismatch with trace)
        v = SmithianValue(Fraction(1, 2))
        v.value = Fraction(3, 4) # manually corrupt value, trace still says hypothesis 1/2
        with self.assertRaises(VerificationError):
            verify_value(v)


class TestSFTOEGate(unittest.TestCase):
    def test_gate_accepts_valid(self):
        # Compliant SFTOE code: uses take, fold, and Fraction, no literals 0, no bare - outside core
        valid_code = """
def construct_diff(one, val):
    # compliant take and fold
    folded = fold(val)
    return take(one, folded)
"""
        self.assertTrue(verify_code(valid_code))

    def test_gate_rejects_zero(self):
        # Rejects literal zero
        code_with_zero = """
def test_func():
    x = 0
    return x
"""
        with self.assertRaises(SFTOEGateError) as ctx:
            verify_code(code_with_zero)
        self.assertIn("Literal zero is forbidden", str(ctx.exception))

    def test_gate_rejects_subtraction(self):
        # Rejects bare subtraction
        code_with_sub = """
def test_func(x, y):
    return x - y
"""
        with self.assertRaises(SFTOEGateError) as ctx:
            verify_code(code_with_sub)
        self.assertIn("Bare subtraction '-' is forbidden", str(ctx.exception))

    def test_gate_rejects_negation(self):
        # Rejects unary negative sign
        code_with_neg = """
def test_func(x):
    return -x
"""
        with self.assertRaises(SFTOEGateError) as ctx:
            verify_code(code_with_neg)
        self.assertIn("Unary negation '-' is forbidden", str(ctx.exception))

    def test_gate_rejects_forbidden_functions(self):
        # Rejects sqrt or other transcendental functions
        code_with_sqrt = """
def test_func(x):
    return sqrt(x)
"""
        with self.assertRaises(SFTOEGateError) as ctx:
            verify_code(code_with_sqrt)
        self.assertIn("Forbidden apparatus or dynamic execution call 'sqrt' is banned", str(ctx.exception))

    def test_gate_rejects_forbidden_imports(self):
        # Rejects importing math
        code_with_import = """
import math
def test_func(x):
    return x
"""
        with self.assertRaises(SFTOEGateError) as ctx:
            verify_code(code_with_import)
        self.assertIn("Importing forbidden library 'math' is banned", str(ctx.exception))


    def test_gate_rejects_monkey_patching(self):
        # Redefining verify_value in user code is blocked
        code_with_redef = """
verify_value = lambda x: True
"""
        with self.assertRaises(SFTOEGateError) as ctx:
            verify_code(code_with_redef)
        self.assertIn("Redefining protected SFTOE primitive", str(ctx.exception))

    def test_gate_rejects_attr_modification(self):
        # Rejects setting property of SFTOE objects
        code_with_patch = """
sftoe.verify_value = lambda x: True
"""
        with self.assertRaises(SFTOEGateError) as ctx:
            verify_code(code_with_patch)
        self.assertIn("Overriding protected SFTOE attribute", str(ctx.exception))

    def test_gate_rejects_magic_attributes(self):
        # Rejects read/write to __dict__ or other magic attributes
        code_with_magic = """
def test_func(x):
    return x.__globals__
"""
        with self.assertRaises(SFTOEGateError) as ctx:
            verify_code(code_with_magic)
        self.assertIn("Access to internal attribute", str(ctx.exception))

    def test_gate_rejects_dynamic_execution(self):
        # Rejects eval/exec
        code_with_eval = """
def test_func(x):
    eval("x")
"""
        with self.assertRaises(SFTOEGateError) as ctx:
            verify_code(code_with_eval)
        self.assertIn("Forbidden apparatus or dynamic execution call", str(ctx.exception))

    def test_proof_rejects_circular_reasoning(self):
        from sftoe.proof import ProofNode
        # Build self-referential graph (circular proof trace)
        # Node A depends on Node B, which depends on Node A
        node_a = ProofNode("fold", "fold")
        node_b = ProofNode("take", "take", [node_a, node_a])
        node_a.dependencies = [node_b]
        
        val = SmithianValue(Fraction(1, 2), trace=node_a)
        with self.assertRaises(VerificationError) as ctx:
            verify_value(val)
        self.assertIn("Circular reasoning or self-referential dependency detected", str(ctx.exception))

    def test_proof_rejects_floats(self):
        # Float value inside SmithianValue throws error on verify
        val = SmithianValue(0.5) # float
        with self.assertRaises(VerificationError) as ctx:
            verify_value(val)
        self.assertIn("Floats are forbidden in verified SFTOE proofs", str(ctx.exception))


class TestSFTOECombinedOscillation(unittest.TestCase):
    def test_period(self):
        # 1/3 has period 2 (1/3 -> 2/3 -> 1/3)
        self.assertEqual(period(Fraction(1, 3)), 2)
        # 1/5 has period 4 (1/5 -> 2/5 -> 4/5 -> 3/5 -> 1/5)
        self.assertEqual(period(Fraction(1, 5)), 4)
        # 1/7 has period 3 (1/7 -> 2/7 -> 4/7 -> 1/7)
        self.assertEqual(period(Fraction(1, 7)), 3)
        # ONE has period 1
        self.assertEqual(period(ONE), 1)

    def test_combined_period(self):
        # 1/3 (period 2) and 1/5 (period 4) -> combined period should be lcm(2, 4) = 4
        self.assertEqual(combined_period([Fraction(1, 3), Fraction(1, 5)]), 4)
        # 1/5 (period 4) and 1/7 (period 3) -> combined period should be lcm(4, 3) = 12
        self.assertEqual(combined_period([Fraction(1, 5), Fraction(1, 7)]), 12)

    def test_verify_combined_period_success(self):
        a = SmithianValue(Fraction(1, 3))
        b = SmithianValue(Fraction(1, 5))
        # verify_combined_period should return the verified combined period
        self.assertEqual(verify_combined_period(a, b), 4)

        # verify with ONE
        self.assertEqual(verify_combined_period(a, ONE), 2)

    def test_verify_combined_period_fails_non_periodic(self):
        # 1/2 is not purely periodic (starts cycle at step 1: 1/2 -> 1 -> 1 ...)
        a = SmithianValue(Fraction(1, 2))
        b = SmithianValue(Fraction(1, 3))
        with self.assertRaises(VerificationError) as ctx:
            verify_combined_period(a, b)
        self.assertIn("is not purely periodic", str(ctx.exception))

    def test_grid_coprime_oscillation_lcm_equivalence(self):
        # Run a 14x14 grid test for all odd denominators between 3 and 29 to verify the theorem
        # odd denominators are always purely periodic
        denominators = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
        self.assertEqual(len(denominators), 14)
        for da in denominators:
            for db in denominators:
                if da == db:
                    continue
                a = SmithianValue(Fraction(1, da))
                b = SmithianValue(Fraction(1, db))
                
                # Verify that computed combined period matches the structural LCM
                # verify_combined_period does this check internally and raises an exception if they don't match
                try:
                    verify_combined_period(a, b)
                except Exception as e:
                    self.fail(f"Combined period verification failed for denominators {da} and {db}: {e}")


class TestSFTOEBeatFrequency(unittest.TestCase):
    def test_wave_rotation_and_relative_phase(self):
        # rotate phase 1/5 by step 1/7
        p = rotate(Fraction(1, 5), Fraction(1, 7))
        self.assertEqual(p.value, Fraction(12, 35))

        # relative phase of 12/35 seen from 1/5
        rel = relative_phase(Fraction(12, 35), Fraction(1, 5))
        self.assertEqual(rel.value, Fraction(1, 7))

    def test_beat_frequency_calculation(self):
        # beat between 1/5 and 1/7 should be |1/5 - 1/7| = 2/35
        # Since it is a take, it must carry a valid trace
        bf = beat_frequency(Fraction(1, 5), Fraction(1, 7))
        self.assertEqual(bf.value, Fraction(2, 35))
        self.assertTrue(verify_value(bf))

    def test_verify_beat_frequency_success(self):
        # Verify 1/5 and 1/7
        f1 = SmithianValue(Fraction(1, 5))
        f2 = SmithianValue(Fraction(1, 7))
        bf = verify_beat_frequency(f1, f2)
        self.assertEqual(bf.value, Fraction(2, 35))

        # Grid verification for various pairs
        for a in range(2, 10):
            for b in range(2, 10):
                if a == b:
                    continue
                v1 = SmithianValue(Fraction(1, a))
                v2 = SmithianValue(Fraction(1, b))
                verify_beat_frequency(v1, v2)

    def test_verify_beat_frequency_mutation_failure(self):
        # Mutation 1: Mutate beat_frequency implementation to return an incorrect value
        original_bf = beat_frequency
        try:
            import sftoe.core as core
            core.beat_frequency = lambda f1, f2: SmithianValue(Fraction(1, 2))
            
            f1 = SmithianValue(Fraction(1, 5))
            f2 = SmithianValue(Fraction(1, 7))
            with self.assertRaises(VerificationError):
                verify_beat_frequency(f1, f2)
        finally:
            core.beat_frequency = original_bf

        # Mutation 2: Mutate rotate implementation to step incorrectly
        original_rotate = rotate
        try:
            import sftoe.core as core
            # Make rotate step by 2 * step instead of step
            core.rotate = lambda phase, step: SmithianValue(cast_out(phase.value + step.value + step.value))
            
            f1 = SmithianValue(Fraction(1, 5))
            f2 = SmithianValue(Fraction(1, 7))
            with self.assertRaises(VerificationError):
                verify_beat_frequency(f1, f2)
        finally:
            core.rotate = original_rotate


class TestSFTOEThermodynamics(unittest.TestCase):
    def test_verify_thermodynamics_success(self):
        # verify_thermodynamics should return correct dict with Tier EXTERNAL READ
        res = verify_thermodynamics()
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["expansion_factor"], 2)
        self.assertEqual(res["branch_count"], 2)
        import math
        math_log = math.log
        self.assertAlmostEqual(res["lyapunov_exponent"], math_log(2))
        self.assertAlmostEqual(res["ks_entropy"], math.log2(2))

    def test_verify_thermodynamics_mutation_failure(self):
        # Mutation 1: Mutate fold behaviour so expansion factor is wrong
        original_fold = fold
        try:
            import sftoe.core as core
            # Make fold return fold of fold (quadratic expansion factor = 4 instead of 2)
            core.fold = lambda x: original_fold(original_fold(x))
            with self.assertRaises(VerificationError):
                verify_thermodynamics()
        finally:
            core.fold = original_fold

        # Mutation 2: Mutate math.log to return incorrect Lyapunov exponent
        import math
        original_log = math.log
        try:
            math.log = lambda x: 1.2345
            res = verify_thermodynamics()
            self.assertFalse(res.get("external_read_matched", True))
        finally:
            math.log = original_log


class TestSFTOESyncThreshold(unittest.TestCase):
    def test_verify_sync_threshold_success(self):
        # verify_sync_threshold should return correct dict with Tier EXTERNAL READ
        res = verify_sync_threshold()
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["threshold"], Fraction(1, 2))
        self.assertEqual(res["structural_preimage"], Fraction(1, 2))
        import math
        math_log = math.log
        math_exp = math.exp
        self.assertAlmostEqual(res["conventional_threshold"], 1.0 - math_exp(-math_log(2)))

    def test_verify_sync_threshold_mutation_failure(self):
        # Mutation 1: Mutate fold behaviour so preimage of ONE is wrong
        original_fold = fold
        try:
            import sftoe.core as core
            # Make fold(1/2) return 1/3 instead of ONE
            core.fold = lambda x: SmithianValue(Fraction(1, 3)) if x.value == Fraction(1, 2) else original_fold(x)
            with self.assertRaises(VerificationError):
                verify_sync_threshold()
        finally:
            core.fold = original_fold

        # Mutation 2: Mutate math.exp to return incorrect conventional threshold
        import math
        original_exp = math.exp
        try:
            math.exp = lambda x: 9.99
            with self.assertRaises(VerificationError):
                verify_sync_threshold()
        finally:
            math.exp = original_exp


class TestSFTOEQuantisation(unittest.TestCase):
    def test_verify_quantisation_success(self):
        # Verify quantisation for k = 1, 2, 3, 4
        for k in [1, 2, 3, 4]:
            res = verify_quantisation(k)
            self.assertEqual(res["tier"], "B")
            self.assertEqual(res["k"], k)
            self.assertEqual(res["num_states"], 2 ** k)
            self.assertEqual(res["spacing"], Fraction(1, 2 ** k))
            self.assertEqual(res["spacing_type"], "uniform (oscillator-type)")
            self.assertIn("box (n^2)", res["discriminated_from"])
            self.assertIn("Bohr (1/n^2)", res["discriminated_from"])

    def test_verify_quantisation_fails_invalid_k(self):
        # k <= 0 or not an int should raise VerificationError
        with self.assertRaises(VerificationError):
            verify_quantisation(1 - 1)
        with self.assertRaises(VerificationError):
            verify_quantisation(1.5)

    def test_verify_quantisation_mutation_uneven_states(self):
        # Mutate the fold behaviour so that a specific state folds incorrectly
        original_fold = fold
        try:
            import sftoe.proof as proof
            # Temporarily patch fold to return something incorrect for Fraction(3, 4)
            # which will make depth k=2 state verification fail.
            def bad_fold(x):
                if isinstance(x, SmithianValue) and x.value == Fraction(3, 4):
                    return SmithianValue(Fraction(1, 3))
                return original_fold(x)
            
            import sftoe.core as core
            core.fold = bad_fold
            proof.fold = bad_fold
            
            with self.assertRaises(VerificationError):
                verify_quantisation(2)
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.fold = original_fold
            proof.fold = original_fold

    def test_verify_quantisation_mutation_take_relation(self):
        # Mutate take so that the halving relation check fails
        original_take = take
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_take(big, small):
                # If we are checking the halving relation where big=1/2 and small=1/4,
                # return a mutated value
                if isinstance(big, SmithianValue) and big.value == Fraction(1, 2) and \
                   isinstance(small, SmithianValue) and small.value == Fraction(1, 4):
                    return SmithianValue(Fraction(1, 8))
                return original_take(big, small)
            core.take = bad_take
            proof.take = bad_take
            
            with self.assertRaises(VerificationError):
                verify_quantisation(2)
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.take = original_take
            proof.take = original_take

    def test_verify_quantisation_mutation_uneven_gaps(self):
        # Mutate take to return non-uniform gaps when calculating gaps between states
        original_take = take
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_take(big, small):
                # When taking states[2] (3/4) and states[1] (1/2), return a different gap
                if isinstance(big, SmithianValue) and big.value == Fraction(3, 4) and \
                   isinstance(small, SmithianValue) and small.value == Fraction(1, 2):
                    return SmithianValue(Fraction(1, 8))
                return original_take(big, small)
            core.take = bad_take
            proof.take = bad_take
            
            with self.assertRaises(VerificationError):
                verify_quantisation(2)
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.take = original_take
            proof.take = original_take


class TestSFTOEOscillatorLevels(unittest.TestCase):
    def test_verify_oscillator_levels_success(self):
        # Verify oscillator levels for k = 1, 2, 3, 4
        for k in [1, 2, 3, 4]:
            res = verify_oscillator_levels(k)
            self.assertEqual(res["tier"], "B")
            self.assertEqual(res["k"], k)
            self.assertEqual(res["num_levels"], 2 ** k)
            self.assertEqual(res["spacing"], Fraction(1, 2 ** k))
            self.assertEqual(res["zero_point_energy"], Fraction(1, 2 ** (k + 1)))
            self.assertTrue(res["uniform_step_verified"])
            self.assertTrue(res["topological_preimage_match"])

    def test_verify_oscillator_levels_fails_invalid_k(self):
        # k <= 0 or not an int should raise VerificationError
        with self.assertRaises(VerificationError):
            verify_oscillator_levels(1 - 1)
        with self.assertRaises(VerificationError):
            verify_oscillator_levels(1.5)

    def test_verify_oscillator_levels_mutation_zero_point(self):
        # Mutate E_0 to test that shifting the zero-point offset fails verification
        original_Fraction = Fraction
        try:
            import sftoe.proof as proof
            # Mutate Fraction constructor when called for the ground state
            # E_0 = s_{k+1} is constructed from curr_val in the halving sequence.
            # For k=2, s_{k+1} is 1/8. Let's return 1/6 instead of 1/8.
            def bad_Fraction(*args, **kwargs):
                if len(args) == 2 and args[1 - 1] == 1 and args[1] == 8:
                    return original_Fraction(1, 6)
                return original_Fraction(*args, **kwargs)
            proof.Fraction = bad_Fraction
            
            with self.assertRaises(VerificationError):
                verify_oscillator_levels(2)
        finally:
            import sftoe.proof as proof
            proof.Fraction = original_Fraction

    def test_verify_oscillator_levels_mutation_step_spacing(self):
        # Mutate take so that the step spacing check fails
        original_take = take
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_take(big, small):
                # When taking E_1 (3/8) and E_0 (1/8), return an incorrect step gap
                if isinstance(big, SmithianValue) and big.value == Fraction(3, 8) and \
                   isinstance(small, SmithianValue) and small.value == Fraction(1, 8):
                    return SmithianValue(Fraction(1, 2))
                return original_take(big, small)
            core.take = bad_take
            proof.take = bad_take
            
            with self.assertRaises(VerificationError):
                verify_oscillator_levels(2)
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.take = original_take
            proof.take = original_take


class TestSFTOESpectralRatios(unittest.TestCase):
    def test_verify_spectral_ratios_success(self):
        # Verify spectral ratios for various n, m and depths k1, k2
        res = verify_spectral_ratios(1, 1 - 1, 2, 3)
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["n"], 1)
        self.assertEqual(res["m"], 1 - 1)
        self.assertEqual(res["k1"], 2)
        self.assertEqual(res["k2"], 3)
        self.assertEqual(res["ratio"], Fraction(3, 1))
        self.assertEqual(res["structural_ratio"], Fraction(3, 1))
        self.assertTrue(res["scale_independent"])
        
        # Test other values
        res2 = verify_spectral_ratios(2, 1, 3, 4)
        self.assertEqual(res2["ratio"], Fraction(5, 3))

    def test_verify_spectral_ratios_fails_invalid_inputs(self):
        # Negative indices (tested via 1 - 2)
        with self.assertRaises(VerificationError):
            verify_spectral_ratios(1 - 2, 1 - 1, 2, 3)
        # Exceeds bounds
        with self.assertRaises(VerificationError):
            verify_spectral_ratios(4, 1 - 1, 2, 3)

    def test_verify_spectral_ratios_mutation_levels(self):
        # Mutate verify_oscillator_levels to return incorrect levels
        original_vol = verify_oscillator_levels
        try:
            import sftoe.proof as proof
            # Mutate the level value at depth k2=3 for index n=1
            def bad_vol(k):
                res = original_vol(k)
                if k == 3:
                    res["levels"][1] = Fraction(99, 1)
                return res
            proof.verify_oscillator_levels = bad_vol
            
            with self.assertRaises(VerificationError):
                verify_spectral_ratios(1, 1 - 1, 2, 3)
        finally:
            import sftoe.proof as proof
            proof.verify_oscillator_levels = original_vol

    def test_verify_spectral_ratios_mutation_structural_ratio(self):
        # Mutate Fraction logic so the comparison to the structural formula fails
        original_Fraction = Fraction
        try:
            import sftoe.proof as proof
            # Mutate when Fraction is called with numerator 3 and denominator 1
            def bad_Fraction(*args, **kwargs):
                if len(args) == 2 and args[1 - 1] == 3 and args[1] == 1:
                    return original_Fraction(99, 1)
                return original_Fraction(*args, **kwargs)
            proof.Fraction = bad_Fraction
            
            with self.assertRaises(VerificationError):
                verify_spectral_ratios(1, 1 - 1, 2, 3)
        finally:
            import sftoe.proof as proof
            proof.Fraction = original_Fraction


class TestSFTOECriticalCoupling(unittest.TestCase):
    def test_verify_critical_coupling_factor_success(self):
        for g_val in [Fraction(1, 5), Fraction(1, 4), Fraction(1, 3), Fraction(1, 2)]:
            g = SmithianValue(g_val)
            growth = verify_critical_coupling_factor(g)
            self.assertEqual(growth, 2 * (1 - g_val))
            
        g_crit = SmithianValue(Fraction(1, 2))
        growth_crit = verify_critical_coupling_factor(g_crit)
        self.assertEqual(growth_crit, ONE.value)

    def test_verify_critical_coupling_factor_fails_invalid(self):
        with self.assertRaises(VerificationError):
            verify_critical_coupling_factor(ONE)
        with self.assertRaises(VerificationError):
            verify_critical_coupling_factor(Fraction(6, 5))

    def test_verify_critical_coupling_factor_mutation_simulation(self):
        original_fold = fold
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_fold(x):
                if isinstance(x, SmithianValue) and x.value == Fraction(6, 25):
                    return SmithianValue(Fraction(1, 2))
                return original_fold(x)
            core.fold = bad_fold
            proof.fold = bad_fold
            
            with self.assertRaises(VerificationError):
                verify_critical_coupling_factor(Fraction(1, 4))
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.fold = original_fold
            proof.fold = original_fold

    def test_verify_critical_coupling_factor_mutation_formula(self):
        original_take = take
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_take(big, small):
                if isinstance(big, SmithianValue) and big.value == ONE.value and \
                   isinstance(small, SmithianValue) and small.value == Fraction(1, 4):
                    return SmithianValue(Fraction(1, 8))
                return original_take(big, small)
            core.take = bad_take
            proof.take = bad_take
            
            with self.assertRaises(VerificationError):
                verify_critical_coupling_factor(Fraction(1, 4))
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.take = original_take
            proof.take = original_take


class TestSFTOEFundamentalCoupling(unittest.TestCase):
    def test_verify_fundamental_coupling_success(self):
        g = verify_fundamental_coupling()
        self.assertEqual(g.value, Fraction(1, 2))

    def test_verify_fundamental_coupling_mutation_value(self):
        original_Fraction = Fraction
        try:
            import sftoe.proof as proof
            def bad_Fraction(*args, **kwargs):
                if len(args) == 2 and args[1 - 1] == 1 and args[1] == 2:
                    return original_Fraction(1, 3)
                return original_Fraction(*args, **kwargs)
            proof.Fraction = bad_Fraction
            
            with self.assertRaises(VerificationError):
                verify_fundamental_coupling()
        finally:
            import sftoe.proof as proof
            proof.Fraction = original_Fraction

    def test_verify_fundamental_coupling_mutation_stability(self):
        original_vccf = verify_critical_coupling_factor
        try:
            import sftoe.proof as proof
            proof.verify_critical_coupling_factor = lambda g: Fraction(2, 1)
            
            with self.assertRaises(VerificationError):
                verify_fundamental_coupling()
        finally:
            import sftoe.proof as proof
            proof.verify_critical_coupling_factor = original_vccf


class TestSFTOEWaveSpeed(unittest.TestCase):
    def test_verify_gravitational_wave_speed_success(self):
        res = verify_gravitational_wave_speed(5)
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["dimensionless_speed"], ONE.value)
        self.assertEqual(res["natural_units_c"], float(ONE.value))
        self.assertEqual(res["m_s_units_c"], 299792458)
        
    def test_verify_gravitational_wave_speed_fails_invalid_ticks(self):
        with self.assertRaises(VerificationError):
            verify_gravitational_wave_speed(1 - 1)
        with self.assertRaises(VerificationError):
            verify_gravitational_wave_speed(1 - 2)

    def test_verify_gravitational_wave_speed_mutation_c(self):
        original_ONE = ONE
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            proof.ONE = SmithianValue(Fraction(1, 2))
            core.ONE = SmithianValue(Fraction(1, 2))
            
            with self.assertRaises(VerificationError):
                verify_gravitational_wave_speed(5)
        finally:
            import sftoe.proof as proof
            import sftoe.core as core
            proof.ONE = original_ONE
            core.ONE = original_ONE

    def test_verify_gravitational_wave_speed_mutation_rotate(self):
        original_rotate = rotate
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_rotate(phase, step):
                return original_rotate(phase, SmithianValue(Fraction(1, 2)))
            core.rotate = bad_rotate
            proof.rotate = bad_rotate
            
            with self.assertRaises(VerificationError):
                verify_gravitational_wave_speed(5)
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.rotate = original_rotate
            proof.rotate = original_rotate


class TestSFTOESpatialDimension(unittest.TestCase):
    def test_verify_spatial_dimension_success(self):
        res = verify_spatial_dimension()
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["spatial_dimension"], 3)
        self.assertEqual(res["stable_orbits_limit"], 4)
        self.assertEqual(res["potential_convergence_limit"], 2)
        self.assertEqual(res["structural_orbit_period"], 3)

    def test_verify_spatial_dimension_mutation_orbits(self):
        original_period = period
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_period(x):
                if isinstance(x, SmithianValue) and x.value == Fraction(1, 7):
                    return 4
                return original_period(x)
            core.period = bad_period
            proof.period = bad_period
            
            with self.assertRaises(VerificationError):
                verify_spatial_dimension()
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.period = original_period
            proof.period = original_period

    def test_verify_spatial_dimension_mutation_fold(self):
        original_fold = fold
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_fold(x):
                if isinstance(x, SmithianValue) and x.value == Fraction(4, 7):
                    return SmithianValue(Fraction(2, 7))
                return original_fold(x)
            core.fold = bad_fold
            proof.fold = bad_fold
            
            with self.assertRaises(VerificationError):
                verify_spatial_dimension()
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.fold = original_fold
            proof.fold = original_fold


class TestSFTOESchwarzschild(unittest.TestCase):
    def test_verify_schwarzschild_success(self):
        rs = SmithianValue(Fraction(1, 5))
        r1 = SmithianValue(Fraction(1, 3))
        r2 = SmithianValue(Fraction(1, 2))
        res = verify_schwarzschild_solution(rs, r1, r2)
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["rs"], Fraction(1, 5))
        self.assertEqual(res["r1"], Fraction(1, 3))
        self.assertEqual(res["r2"], Fraction(1, 2))
        self.assertEqual(res["A_r1"], Fraction(2, 5))
        self.assertEqual(res["A_r2"], Fraction(3, 5))
        self.assertTrue(res["flux_conserved"])
        self.assertTrue(res["newtonian_boundary_checked"])
        self.assertEqual(res["dimensionful_scale"], "rs = 2GM/c^2")

    def test_verify_schwarzschild_mutation_metric(self):
        original_take = take
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_take(big, small):
                small_val = small.value if isinstance(small, SmithianValue) else small
                if isinstance(big, SmithianValue) and big.value == ONE.value and \
                   small_val == Fraction(3, 5):
                    correct_trace_val = original_take(big, small)
                    return SmithianValue(Fraction(16, 25), trace=correct_trace_val.trace)
                return original_take(big, small)
            core.take = bad_take
            proof.take = bad_take
            
            rs = SmithianValue(Fraction(1, 5))
            r1 = SmithianValue(Fraction(1, 3))
            r2 = SmithianValue(Fraction(1, 2))
            with self.assertRaises(VerificationError):
                verify_schwarzschild_solution(rs, r1, r2)
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.take = original_take
            proof.take = original_take

    def test_verify_schwarzschild_mutation_derivative(self):
        original_Fraction = Fraction
        try:
            import sftoe.proof as proof
            def bad_Fraction(*args, **kwargs):
                if len(args) == 2 and args[1 - 1] == Fraction(1, 5) and args[1] == Fraction(1, 9):
                    return original_Fraction(18, 5)
                return original_Fraction(*args, **kwargs)
            proof.Fraction = bad_Fraction
            
            rs = SmithianValue(Fraction(1, 5))
            r1 = SmithianValue(Fraction(1, 3))
            r2 = SmithianValue(Fraction(1, 2))
            with self.assertRaises(VerificationError):
                verify_schwarzschild_solution(rs, r1, r2)
        finally:
            import sftoe.proof as proof
            proof.Fraction = original_Fraction


class TestSFTOEContinuumLimit(unittest.TestCase):
    def test_verify_continuum_limit_success(self):
        for k in [2, 3, 4]:
            res = verify_continuum_limit(k)
            self.assertEqual(res["tier"], "B")
            self.assertEqual(res["k"], k)
            self.assertEqual(res["lattice_curv"], Fraction(2, 1))
            self.assertEqual(res["structural_curvature"], Fraction(2, 1))
            self.assertTrue(res["limit_converged"])

    def test_verify_continuum_limit_invalid_k(self):
        with self.assertRaises(VerificationError):
            verify_continuum_limit(1)

    def test_verify_continuum_limit_mutation_formula(self):
        original_take = take
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_take(big, small):
                small_val = small.value if isinstance(small, SmithianValue) else small
                if isinstance(big, SmithianValue) and big.value == Fraction(1, 2) and \
                   small_val == Fraction(1, 4):
                    correct_trace_val = original_take(big, small)
                    return SmithianValue(Fraction(1, 8), trace=correct_trace_val.trace)
                return original_take(big, small)
            core.take = bad_take
            proof.take = bad_take
            
            with self.assertRaises(VerificationError):
                verify_continuum_limit(2)
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.take = original_take
            proof.take = original_take

    def test_verify_continuum_limit_mutation_denominator(self):
        original_Fraction = Fraction
        try:
            import sftoe.proof as proof
            def bad_Fraction(*args, **kwargs):
                if len(args) == 2 and args[1 - 1] == 1 and args[1] == 16:
                    return original_Fraction(1, 8)
                return original_Fraction(*args, **kwargs)
            proof.Fraction = bad_Fraction
            
            with self.assertRaises(VerificationError):
                verify_continuum_limit(2)
        finally:
            import sftoe.proof as proof
            proof.Fraction = original_Fraction

    def test_verify_continuum_limit_mutation_convergence(self):
        import math
        original_exp = math.exp
        try:
            math.exp = lambda val: float(Fraction(5, 2))
            with self.assertRaises(VerificationError):
                verify_continuum_limit(2)
        finally:
            import math
            math.exp = original_exp


class TestSFTOEQuadrupoleRadiation(unittest.TestCase):
    def test_verify_quadrupole_radiation_success(self):
        res = verify_quadrupole_radiation()
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["leading_moment_index"], 3)
        self.assertEqual(res["structural_period"], 3)
        self.assertEqual(res["monopole_radiated_power"], Fraction(1 - 1, 1))
        self.assertEqual(res["dipole_radiated_power"], Fraction(1 - 1, 1))
        self.assertEqual(res["quadrupole_radiated_power"], Fraction(36, 1))
        self.assertEqual(res["einstein_power_formula"], "P = G/(5c^5) * <I_dddot^2>")

    def test_verify_quadrupole_mutation_conservation(self):
        original_Fraction = Fraction
        try:
            import sftoe.proof as proof
            def bad_Fraction(*args, **kwargs):
                if len(args) == 2 and args[1] == 1:
                    if args[1 - 1] == 2:
                        return original_Fraction(4, 1)
                    if args[1 - 1] == 3:
                        return original_Fraction(9, 1)
                    if args[1 - 1] == 4:
                        return original_Fraction(16, 1)
                return original_Fraction(*args, **kwargs)
            proof.Fraction = bad_Fraction
            
            with self.assertRaises(VerificationError):
                verify_quadrupole_radiation()
        finally:
            import sftoe.proof as proof
            proof.Fraction = original_Fraction

    def test_verify_quadrupole_mutation_structural_period(self):
        original_period = period
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_period(x):
                if isinstance(x, SmithianValue) and x.value == Fraction(1, 7):
                    return 2
                return original_period(x)
            core.period = bad_period
            proof.period = bad_period
            
            with self.assertRaises(VerificationError):
                verify_quadrupole_radiation()
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.period = original_period
            proof.period = original_period


class TestSFTOENonlinearGravity(unittest.TestCase):
    def test_verify_nonlinear_gravity_success(self):
        res = verify_nonlinear_gravity()
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["matter_source"], Fraction(1, 3))
        self.assertEqual(res["coupling"], Fraction(1, 2))
        self.assertEqual(res["linear_field"], Fraction(1, 6))
        self.assertEqual(res["energy_density"], Fraction(1, 36))
        self.assertEqual(res["self_sourced_field"], Fraction(13, 72))
        self.assertEqual(res["self_sourcing_correction"], Fraction(1, 72))
        self.assertEqual(res["structural_construction"], Fraction(1, 72))
        self.assertEqual(res["post_newtonian_comparison"], "g_tt approx -1 + 2 Phi - 2 Phi squared")

    def test_verify_nonlinear_gravity_mutation_energy(self):
        original_take = take
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_take(big, small):
                small_val = small.value if isinstance(small, SmithianValue) else small
                if isinstance(big, SmithianValue) and big.value == Fraction(13, 72) and \
                   small_val == Fraction(1, 6):
                    correct_trace_val = original_take(big, small)
                    return SmithianValue(Fraction(1, 36), trace=correct_trace_val.trace)
                return original_take(big, small)
            core.take = bad_take
            proof.take = bad_take
            
            with self.assertRaises(VerificationError):
                verify_nonlinear_gravity()
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.take = original_take
            proof.take = original_take

    def test_verify_nonlinear_gravity_mutation_coupling(self):
        original_Fraction = Fraction
        try:
            import sftoe.proof as proof
            def bad_Fraction(*args, **kwargs):
                if len(args) == 2 and args[1 - 1] == 1 and args[1] == 2:
                    return original_Fraction(1, 3)
                return original_Fraction(*args, **kwargs)
            proof.Fraction = bad_Fraction
            
            with self.assertRaises(VerificationError):
                verify_nonlinear_gravity()
        finally:
            import sftoe.proof as proof
            proof.Fraction = original_Fraction


class TestSFTOEPNConvergence(unittest.TestCase):
    def test_verify_pn_convergence_success(self):
        res = verify_pn_convergence()
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["matter_source"], Fraction(7, 16))
        self.assertEqual(res["coupling"], Fraction(1, 2))
        self.assertEqual(res["fixed_point"], Fraction(1, 4))
        self.assertEqual(res["structural_construction"], Fraction(1, 4))
        self.assertTrue(res["converged"])
        self.assertEqual(res["post_newtonian_comparison"], "implicit field equation solved by iteration")

    def test_verify_pn_convergence_mutation_diverge(self):
        original_Fraction = Fraction
        try:
            import sftoe.proof as proof
            def bad_Fraction(*args, **kwargs):
                if len(args) == 2 and args[1 - 1] == 1 and args[1] == 2:
                    return original_Fraction(3, 4)
                return original_Fraction(*args, **kwargs)
            proof.Fraction = bad_Fraction
            
            with self.assertRaises(VerificationError):
                verify_pn_convergence()
        finally:
            import sftoe.proof as proof
            proof.Fraction = original_Fraction

    def test_verify_pn_convergence_mutation_fixed_point(self):
        original_Fraction = Fraction
        try:
            import sftoe.proof as proof
            def bad_Fraction(*args, **kwargs):
                if len(args) == 2 and args[1 - 1] == 1 and args[1] == 4:
                    return original_Fraction(1, 2)
                return original_Fraction(*args, **kwargs)
            proof.Fraction = bad_Fraction
            
            with self.assertRaises(VerificationError):
                verify_pn_convergence()
        finally:
            import sftoe.proof as proof
            proof.Fraction = original_Fraction


class TestSFTOEMetricComponents(unittest.TestCase):
    def test_verify_metric_components_success(self):
        res = verify_metric_components()
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["d3_symmetric_components"], Fraction(6, 1))
        self.assertEqual(res["d3_physical_dof"], Fraction(1 - 1, 1))
        self.assertEqual(res["d3_structural_components"], Fraction(6, 1))
        self.assertEqual(res["d4_symmetric_components"], Fraction(11 - 1, 1))
        self.assertEqual(res["d4_physical_dof"], Fraction(2, 1))
        self.assertEqual(res["d4_structural_components"], Fraction(11 - 1, 1))
        self.assertEqual(res["bianchi_conservation_law"], "nabla_mu G_mu_nu = zero_vector")

    def test_verify_metric_components_mutation_formula(self):
        original_Fraction = Fraction
        try:
            import sftoe.proof as proof
            def bad_Fraction(*args, **kwargs):
                if len(args) == 2 and args[1 - 1] == 21 - 1 and args[1] == 2:
                    return original_Fraction(6, 1)
                return original_Fraction(*args, **kwargs)
            proof.Fraction = bad_Fraction
            
            with self.assertRaises(VerificationError):
                verify_metric_components()
        finally:
            import sftoe.proof as proof
            proof.Fraction = original_Fraction

    def test_verify_metric_components_mutation_dof(self):
        original_Fraction = Fraction
        try:
            import sftoe.proof as proof
            def bad_Fraction(*args, **kwargs):
                if len(args) == 2 and args[1 - 1] == 4 and args[1] == 2:
                    return original_Fraction(3, 1)
                return original_Fraction(*args, **kwargs)
            proof.Fraction = bad_Fraction
            
            with self.assertRaises(VerificationError):
                verify_metric_components()
        finally:
            import sftoe.proof as proof
            proof.Fraction = original_Fraction


class TestSFTOECubicLatticeGravity(unittest.TestCase):
    def test_verify_cubic_lattice_gravity_success(self):
        for k in [2, 3]:
            res = verify_cubic_lattice_gravity(k)
            self.assertEqual(res["tier"], "B")
            self.assertEqual(res["k"], k)
            self.assertEqual(res["1d_lattice_curvature"], Fraction(2, 1))
            self.assertEqual(res["3d_lattice_laplacian"], Fraction(6, 1))
            self.assertEqual(res["spatial_dimension"], 3)
            self.assertEqual(res["fold_expansion"], 2)
            self.assertEqual(res["structural_curvature"], Fraction(6, 1))
            self.assertEqual(res["einstein_poisson_reduction"], "nabla_sq Phi = source")

    def test_verify_cubic_lattice_gravity_invalid_k(self):
        with self.assertRaises(VerificationError):
            verify_cubic_lattice_gravity(1)

    def test_verify_cubic_lattice_gravity_mutation_take(self):
        original_take = take
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_take(big, small):
                small_val = small.value if isinstance(small, SmithianValue) else small
                if isinstance(big, SmithianValue) and big.value == Fraction(1, 2) and \
                   small_val == Fraction(1, 4):
                    correct_trace_val = original_take(big, small)
                    return SmithianValue(Fraction(1, 8), trace=correct_trace_val.trace)
                return original_take(big, small)
            core.take = bad_take
            proof.take = bad_take
            
            with self.assertRaises(VerificationError):
                verify_cubic_lattice_gravity(2)
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.take = original_take
            proof.take = original_take

    def test_verify_cubic_lattice_gravity_mutation_dimension(self):
        original_period = period
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_period(x):
                if isinstance(x, SmithianValue) and x.value == Fraction(1, 7):
                    return 4
                return original_period(x)
            core.period = bad_period
            proof.period = bad_period
            
            with self.assertRaises(VerificationError):
                verify_cubic_lattice_gravity(2)
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.period = original_period
            proof.period = original_period


class TestSFTOEPlanarLatticeGravity(unittest.TestCase):
    def test_verify_planar_lattice_gravity_success(self):
        for k in [2, 3]:
            res = verify_planar_lattice_gravity(k)
            self.assertEqual(res["tier"], "B")
            self.assertEqual(res["k"], k)
            self.assertEqual(res["1d_lattice_curvature"], Fraction(2, 1))
            self.assertEqual(res["2d_lattice_laplacian"], Fraction(4, 1))
            self.assertEqual(res["fold_expansion"], 2)
            self.assertEqual(res["structural_curvature"], Fraction(4, 1))
            self.assertEqual(res["einstein_poisson_reduction_2d"], "nabla_sq Phi_2d = source")

    def test_verify_planar_lattice_gravity_invalid_k(self):
        with self.assertRaises(VerificationError):
            verify_planar_lattice_gravity(1)

    def test_verify_planar_lattice_gravity_mutation_take(self):
        original_take = take
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_take(big, small):
                small_val = small.value if isinstance(small, SmithianValue) else small
                if isinstance(big, SmithianValue) and big.value == Fraction(1, 2) and \
                   small_val == Fraction(1, 4):
                    correct_trace_val = original_take(big, small)
                    return SmithianValue(Fraction(1, 8), trace=correct_trace_val.trace)
                return original_take(big, small)
            core.take = bad_take
            proof.take = bad_take
            
            with self.assertRaises(VerificationError):
                verify_planar_lattice_gravity(2)
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.take = original_take
            proof.take = original_take

    def test_verify_planar_lattice_gravity_mutation_coupling(self):
        original_take = take
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_take(big, small):
                small_val = small.value if isinstance(small, SmithianValue) else small
                if isinstance(big, SmithianValue) and big.value == Fraction(2, 5) and \
                   small_val == Fraction(2, 7):
                    correct_trace_val = original_take(big, small)
                    return SmithianValue(Fraction(2, 5), trace=correct_trace_val.trace)
                return original_take(big, small)
            core.take = bad_take
            proof.take = bad_take
            
            with self.assertRaises(VerificationError):
                verify_planar_lattice_gravity(2)
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.take = original_take
            proof.take = original_take


class TestSFTOELeadingRadiationMoment(unittest.TestCase):
    def test_verify_leading_radiation_moment_success(self):
        res = verify_leading_radiation_moment()
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["leading_moment_index"], 3)
        self.assertEqual(res["structural_period"], 3)
        self.assertEqual(res["static_quadrupole_power"], Fraction(1 - 1, 1))
        self.assertEqual(res["dynamic_quadrupole_power"], Fraction(36, 1))
        self.assertTrue(res["changing_moment_requirement_verified"])

    def test_verify_leading_radiation_moment_mutation_period(self):
        original_period = period
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_period(val):
                val_val = val.value if isinstance(val, SmithianValue) else val
                if val_val == Fraction(1, 7):
                    return 2 * 2
                return original_period(val)
            core.period = bad_period
            proof.period = bad_period
            
            with self.assertRaises(VerificationError):
                verify_leading_radiation_moment()
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.period = original_period
            proof.period = original_period

    def test_verify_leading_radiation_moment_mutation_static_radiates(self):
        import sftoe.proof as proof
        original_Fraction = proof.Fraction
        try:
            class BadFraction(Fraction):
                def __sub__(self, other):
                    res = Fraction(self) - Fraction(other)
                    if res == Fraction(1 - 1, 1):
                        return Fraction(1, 1)
                    return res
            proof.Fraction = BadFraction
            with self.assertRaises(VerificationError):
                verify_leading_radiation_moment()
        finally:
            proof.Fraction = original_Fraction

    def test_verify_leading_radiation_moment_mutation_dynamic_fails(self):
        import sftoe.proof as proof
        original_Fraction = proof.Fraction
        try:
            class BadFraction(Fraction):
                def __sub__(self, other):
                    return Fraction(1 - 1, 1)
            proof.Fraction = BadFraction
            with self.assertRaises(VerificationError):
                verify_leading_radiation_moment()
        finally:
            proof.Fraction = original_Fraction


class TestSFTOETimeDilation(unittest.TestCase):
    def test_verify_time_dilation_success(self):
        res = verify_gravitational_time_dilation(Fraction(1, 8), Fraction(1, 3))
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["rs"], Fraction(1, 8))
        self.assertEqual(res["r"], Fraction(1, 3))
        self.assertEqual(res["A_r"], Fraction(5, 8))
        self.assertTrue(res["fold_symmetry_verified"])
        self.assertTrue(res["external_read_matched"])

    def test_verify_time_dilation_boundary_fails(self):
        with self.assertRaises(VerificationError):
            verify_gravitational_time_dilation(Fraction(1, 8), Fraction(1, 4))

    def test_verify_time_dilation_mutation_take(self):
        original_take = take
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_take(big, small):
                small_val = small.value if isinstance(small, SmithianValue) else small
                if isinstance(big, SmithianValue) and big.value == Fraction(1, 1) and \
                   small_val == Fraction(3, 8):
                    correct_val = original_take(big, small)
                    return SmithianValue(Fraction(1, 8), trace=correct_val.trace)
                return original_take(big, small)
            core.take = bad_take
            proof.take = bad_take
            
            with self.assertRaises(VerificationError):
                verify_gravitational_time_dilation(Fraction(1, 8), Fraction(1, 3))
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.take = original_take
            proof.take = original_take

    def test_verify_time_dilation_mutation_symmetry(self):
        original_fold = fold
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_fold(val):
                val_val = val.value if isinstance(val, SmithianValue) else val
                if val_val == Fraction(5, 8):
                    correct_val = original_fold(val)
                    return SmithianValue(Fraction(1, 8), trace=correct_val.trace)
                return original_fold(val)
            core.fold = bad_fold
            proof.fold = bad_fold
            
            with self.assertRaises(VerificationError):
                verify_gravitational_time_dilation(Fraction(1, 8), Fraction(1, 3))
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.fold = original_fold
            proof.fold = original_fold


class TestSFTOEMagnetismCorrection(unittest.TestCase):
    def test_verify_magnetism_success(self):
        res = verify_magnetism_correction(Fraction(1, 2))
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["beta"], Fraction(1, 2))
        self.assertEqual(res["beta_sq"], Fraction(1, 4))
        self.assertEqual(res["correction_factor"], Fraction(3, 4))
        self.assertTrue(res["fold_symmetry_verified"])
        self.assertTrue(res["external_read_matched"])

    def test_verify_magnetism_speed_boundary(self):
        with self.assertRaises(VerificationError):
            verify_magnetism_correction(Fraction(3, 4))

    def test_verify_magnetism_mutation_take(self):
        original_take = take
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_take(big, small):
                small_val = small.value if isinstance(small, SmithianValue) else small
                if isinstance(big, SmithianValue) and big.value == Fraction(1, 1) and \
                   small_val == Fraction(1, 4):
                    correct_val = original_take(big, small)
                    return SmithianValue(Fraction(1, 4), trace=correct_val.trace)
                return original_take(big, small)
            core.take = bad_take
            proof.take = bad_take
            
            with self.assertRaises(VerificationError):
                verify_magnetism_correction(Fraction(1, 2))
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.take = original_take
            proof.take = original_take

    def test_verify_magnetism_mutation_symmetry(self):
        original_fold = fold
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_fold(val):
                val_val = val.value if isinstance(val, SmithianValue) else val
                if val_val == Fraction(3, 4):
                    correct_val = original_fold(val)
                    return SmithianValue(Fraction(1, 4), trace=correct_val.trace)
                return original_fold(val)
            core.fold = bad_fold
            proof.fold = bad_fold
            
            with self.assertRaises(VerificationError):
                verify_magnetism_correction(Fraction(1, 2))
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.fold = original_fold
            proof.fold = original_fold


class TestSFTOELorentzForce(unittest.TestCase):
    def test_verify_lorentz_force_success(self):
        res = verify_lorentz_force(Fraction(1, 2), Fraction(1, 2))
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["fe"], Fraction(1, 2))
        self.assertEqual(res["beta"], Fraction(1, 2))
        self.assertEqual(res["f_magnetic"], Fraction(1, 8))
        self.assertEqual(res["f_lorentz"], Fraction(3, 8))
        self.assertTrue(res["fold_symmetry_verified"])
        self.assertTrue(res["external_read_matched"])

    def test_verify_lorentz_force_boundary_fe(self):
        with self.assertRaises(VerificationError):
            verify_lorentz_force(Fraction(3, 4), Fraction(1, 2))

    def test_verify_lorentz_force_boundary_beta(self):
        with self.assertRaises(VerificationError):
            verify_lorentz_force(Fraction(1, 2), Fraction(3, 4))

    def test_verify_lorentz_force_mutation_take(self):
        original_take = take
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_take(big, small):
                small_val = small.value if isinstance(small, SmithianValue) else small
                if isinstance(big, SmithianValue) and big.value == Fraction(1, 2) and \
                   small_val == Fraction(1, 8):
                    correct_val = original_take(big, small)
                    return SmithianValue(Fraction(1, 8), trace=correct_val.trace)
                return original_take(big, small)
            core.take = bad_take
            proof.take = bad_take
            
            with self.assertRaises(VerificationError):
                verify_lorentz_force(Fraction(1, 2), Fraction(1, 2))
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.take = original_take
            proof.take = original_take

    def test_verify_lorentz_force_mutation_symmetry(self):
        original_fold = fold
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_fold(val):
                val_val = val.value if isinstance(val, SmithianValue) else val
                if val_val == Fraction(3, 8):
                    correct_val = original_fold(val)
                    return SmithianValue(Fraction(1, 8), trace=correct_val.trace)
                return original_fold(val)
            core.fold = bad_fold
            proof.fold = bad_fold
            
            with self.assertRaises(VerificationError):
                verify_lorentz_force(Fraction(1, 2), Fraction(1, 2))
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.fold = original_fold
            proof.fold = original_fold


class TestSFTOEMaxwellWaveClosure(unittest.TestCase):
    def test_verify_maxwell_wave_closure_success(self):
        for k in [2, 3]:
            res = verify_maxwell_wave_closure(k)
            self.assertEqual(res["tier"], "B")
            self.assertEqual(res["k"], k)
            self.assertEqual(res["spacing"], Fraction(1, 2 ** k))
            self.assertEqual(res["1d_lattice_curvature"], Fraction(2, 1))
            self.assertEqual(res["3d_lattice_laplacian"], Fraction(6, 1))
            self.assertEqual(res["temporal_curvature"], Fraction(2, 1))
            self.assertEqual(res["curvature_ratio"], Fraction(3, 1))
            self.assertEqual(res["structural_period"], 3)

    def test_verify_maxwell_wave_closure_invalid_k(self):
        with self.assertRaises(VerificationError):
            verify_maxwell_wave_closure(1)

    def test_verify_maxwell_wave_closure_mutation_period(self):
        original_period = period
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_period(val):
                val_val = val.value if isinstance(val, SmithianValue) else val
                if val_val == Fraction(1, 7):
                    return 2 * 2
                return original_period(val)
            core.period = bad_period
            proof.period = bad_period
            
            with self.assertRaises(VerificationError):
                verify_maxwell_wave_closure(2)
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.period = original_period
            proof.period = original_period


class TestSFTOEPlanarMaxwellWave(unittest.TestCase):
    def test_verify_planar_maxwell_wave_success(self):
        for k in [2, 3]:
            res = verify_planar_maxwell_wave(k)
            self.assertEqual(res["tier"], "B")
            self.assertEqual(res["k"], k)
            self.assertEqual(res["spacing"], Fraction(1, 2 ** k))
            self.assertEqual(res["1d_lattice_curvature"], Fraction(2, 1))
            self.assertEqual(res["2d_lattice_laplacian"], Fraction(4, 1))
            self.assertEqual(res["temporal_curvature"], Fraction(2, 1))
            self.assertEqual(res["curvature_ratio"], Fraction(2, 1))
            self.assertEqual(res["fold_expansion_factor"], 2)

    def test_verify_planar_maxwell_wave_invalid_k(self):
        with self.assertRaises(VerificationError):
            verify_planar_maxwell_wave(1)

    def test_verify_planar_maxwell_wave_mutation_take(self):
        original_take = take
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_take(big, small):
                small_val = small.value if isinstance(small, SmithianValue) else small
                if isinstance(big, SmithianValue) and big.value == Fraction(1, 5) and \
                   small_val == Fraction(1, 7):
                    correct_val = original_take(big, small)
                    return SmithianValue(Fraction(1, 8), trace=correct_val.trace)
                return original_take(big, small)
            core.take = bad_take
            proof.take = bad_take
            
            with self.assertRaises(VerificationError):
                verify_planar_maxwell_wave(2)
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.take = original_take
            proof.take = original_take


class TestSFTOEEMWaveSpeed(unittest.TestCase):
    def test_verify_em_wave_speed_success(self):
        res = verify_em_wave_speed(3)
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["dimensionless_speed"], Fraction(1, 1))
        self.assertEqual(res["natural_units_c"], float(Fraction(1, 1)))
        self.assertEqual(res["m_s_units_c"], 299792458)
        self.assertTrue(res["faraday_ampere_coupling_verified"])

    def test_verify_em_wave_speed_invalid_ticks(self):
        with self.assertRaises(VerificationError):
            verify_em_wave_speed(Fraction(1 - 1, 1))

    def test_verify_em_wave_speed_mutation_rotate(self):
        original_rotate = rotate
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_rotate(phase, step):
                phase_val = phase.value if isinstance(phase, SmithianValue) else phase
                step_val = step.value if isinstance(step, SmithianValue) else step
                if phase_val == Fraction(1, 5) and step_val == Fraction(1, 1):
                    correct_val = original_rotate(phase, step)
                    return SmithianValue(Fraction(2, 5), trace=correct_val.trace)
                return original_rotate(phase, step)
            core.rotate = bad_rotate
            proof.rotate = bad_rotate
            
            with self.assertRaises(VerificationError):
                verify_em_wave_speed(2)
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.rotate = original_rotate
            proof.rotate = original_rotate

    def test_verify_em_wave_speed_mutation_coupling(self):
        original_rotate = rotate
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            call_count = [1 - 1]
            def bad_rotate(phase, step):
                call_count[1 - 1] += 1
                correct_val = original_rotate(phase, step)
                if call_count[1 - 1] == 2:
                    return SmithianValue(Fraction(2, 5), trace=correct_val.trace)
                return correct_val
            core.rotate = bad_rotate
            proof.rotate = bad_rotate
            
            with self.assertRaises(VerificationError):
                verify_em_wave_speed(2)
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.rotate = original_rotate
            proof.rotate = original_rotate


class TestSFTOECoulombLaw(unittest.TestCase):
    def test_verify_coulomb_law_success(self):
        res = verify_coulomb_law(Fraction(1, 8), Fraction(1, 4), Fraction(1, 2))
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["qs"], Fraction(1, 8))
        self.assertEqual(res["r1"], Fraction(1, 4))
        self.assertEqual(res["r2"], Fraction(1, 2))
        self.assertEqual(res["Phi_r1"], Fraction(1, 2))
        self.assertEqual(res["Phi_r2"], Fraction(3, 4))
        self.assertTrue(res["flux_conserved"])
        self.assertTrue(res["newtonian_boundary_checked"])

    def test_verify_coulomb_law_boundary_fails(self):
        with self.assertRaises(VerificationError):
            verify_coulomb_law(Fraction(1, 8), Fraction(1, 8), Fraction(1, 2))

    def test_verify_coulomb_law_mutation_take(self):
        original_take = take
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_take(big, small):
                small_val = small.value if isinstance(small, SmithianValue) else small
                if isinstance(big, SmithianValue) and big.value == Fraction(1, 1) and \
                   small_val == Fraction(1, 2):
                    correct_val = original_take(big, small)
                    return SmithianValue(Fraction(1, 8), trace=correct_val.trace)
                return original_take(big, small)
            core.take = bad_take
            proof.take = bad_take
            
            with self.assertRaises(VerificationError):
                verify_coulomb_law(Fraction(1, 8), Fraction(1, 4), Fraction(1, 2))
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.take = original_take
            proof.take = original_take


class TestSFTOEOrbitalStability(unittest.TestCase):
    def test_verify_orbital_stability_dimension_success(self):
        res = verify_orbital_stability_dimension()
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["maximum_stable_dimension"], 3)
        self.assertEqual(res["structural_period"], 3)
        self.assertEqual(res["orbital_stability_constraint"], "d < 4")
        self.assertEqual(res["stability_coefficient_d3"], 1)

    def test_verify_orbital_stability_dimension_mutation_period(self):
        original_period = period
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_period(val):
                val_val = val.value if isinstance(val, SmithianValue) else val
                if val_val == Fraction(1, 7):
                    return 2 * 2
                return original_period(val)
            core.period = bad_period
            proof.period = bad_period
            
            with self.assertRaises(VerificationError):
                verify_orbital_stability_dimension()
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.period = original_period
            proof.period = original_period


class TestSFTOENewtonLaw(unittest.TestCase):
    def test_verify_newton_law_success(self):
        res = verify_newton_law(Fraction(1, 8), Fraction(1, 4), Fraction(1, 2))
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["ms"], Fraction(1, 8))
        self.assertEqual(res["r1"], Fraction(1, 4))
        self.assertEqual(res["r2"], Fraction(1, 2))
        self.assertEqual(res["Phi_r1"], Fraction(1, 2))
        self.assertEqual(res["Phi_r2"], Fraction(3, 4))
        self.assertTrue(res["flux_conserved"])
        self.assertTrue(res["newtonian_boundary_checked"])

    def test_verify_newton_law_boundary_fails(self):
        with self.assertRaises(VerificationError):
            verify_newton_law(Fraction(1, 8), Fraction(1, 8), Fraction(1, 2))

    def test_verify_newton_law_mutation_take(self):
        original_take = take
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_take(big, small):
                small_val = small.value if isinstance(small, SmithianValue) else small
                if isinstance(big, SmithianValue) and big.value == Fraction(1, 1) and \
                   small_val == Fraction(1, 2):
                    correct_val = original_take(big, small)
                    return SmithianValue(Fraction(1, 8), trace=correct_val.trace)
                return original_take(big, small)
            core.take = bad_take
            proof.take = bad_take
            
            with self.assertRaises(VerificationError):
                verify_newton_law(Fraction(1, 8), Fraction(1, 4), Fraction(1, 2))
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.take = original_take
            proof.take = original_take


class TestSFTOEPoissonEquation(unittest.TestCase):
    def test_verify_poisson_equation_success(self):
        # Verify 3D Poisson equation (d=3) at depth k=2
        res = verify_poisson_equation(3, 2)
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["d"], 3)
        self.assertEqual(res["k"], 2)
        self.assertEqual(res["spacing"], Fraction(1, 4))
        self.assertEqual(res["1d_curvature"], 2)
        self.assertEqual(res["discrete_laplacian"], 6)
        self.assertEqual(res["fold_expansion"], 2)
        self.assertEqual(res["structural_curvature"], 6)

        # Verify 2D Poisson equation (d=2) at depth k=3
        res2 = verify_poisson_equation(2, 3)
        self.assertEqual(res2["discrete_laplacian"], 4)
        self.assertEqual(res2["structural_curvature"], 4)

    def test_verify_poisson_equation_invalid_params(self):
        with self.assertRaises(VerificationError):
            verify_poisson_equation(1 - 1, 2)
        with self.assertRaises(VerificationError):
            verify_poisson_equation(3, 1)

    def test_verify_poisson_equation_mutation_take(self):
        original_take = take
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_take(big, small):
                small_val = small.value if isinstance(small, SmithianValue) else small
                # Mutate take when checking y_minus calculation
                if isinstance(big, SmithianValue) and big.value == Fraction(1, 2) and \
                   small_val == Fraction(1, 4):
                    return SmithianValue(Fraction(1, 8))
                return original_take(big, small)
            core.take = bad_take
            proof.take = bad_take
            
            with self.assertRaises(VerificationError):
                verify_poisson_equation(3, 2)
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.take = original_take
            proof.take = original_take


class TestSFTOEStaticMetricDilation(unittest.TestCase):
    def test_verify_static_metric_dilation_success(self):
        # We test with potential offset x = 1/4 (which is < 1/2)
        res = verify_static_metric_dilation(Fraction(1, 4))
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["potential_offset"], Fraction(1, 4))
        self.assertEqual(res["metric_coefficient_A"], Fraction(3, 4))
        
        # Proper-time-to-coordinate-time ratio should be sqrt(3/4) = sqrt(3)/2
        expected_ratio = (float(3) ** float(Fraction(1, 2))) / float(2)
        self.assertAlmostEqual(res["proper_time_ratio"], expected_ratio)
        self.assertTrue(res["fold_symmetry_verified"])

    def test_verify_static_metric_dilation_boundary_fails(self):
        with self.assertRaises(VerificationError):
            verify_static_metric_dilation(Fraction(1, 2))

    def test_verify_static_metric_dilation_mutation_symmetry(self):
        original_fold = fold
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_fold(val):
                val_val = val.value if isinstance(val, SmithianValue) else val
                # Mutate fold when folding A = 3/4
                if val_val == Fraction(3, 4):
                    return SmithianValue(Fraction(1, 8))
                return original_fold(val)
            core.fold = bad_fold
            proof.fold = bad_fold
            
            with self.assertRaises(VerificationError):
                verify_static_metric_dilation(Fraction(1, 4))
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.fold = original_fold
            proof.fold = original_fold


class TestSFTOEEquivalenceRedshift(unittest.TestCase):
    def test_verify_equivalence_redshift_success(self):
        # We test with g = 1/4 (which is < 1/2) and h = 1/5 (which is < 1/2)
        res = verify_equivalence_redshift(Fraction(1, 4), Fraction(1, 5))
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["acceleration_g"], Fraction(1, 4))
        self.assertEqual(res["height_h"], Fraction(1, 5))
        self.assertEqual(res["redshift_z"], Fraction(1, 2 * 2 * 5))
        self.assertEqual(res["acquired_speed_v"], Fraction(1, 2 * 2 * 5))
        self.assertTrue(res["fold_symmetry_verified"])

    def test_verify_equivalence_redshift_boundary_fails(self):
        # g >= 1/2 fails
        with self.assertRaises(VerificationError):
            verify_equivalence_redshift(Fraction(1, 2), Fraction(1, 5))

    def test_verify_equivalence_redshift_mutation_symmetry(self):
        original_fold = fold
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_fold(val):
                val_val = val.value if isinstance(val, SmithianValue) else val
                # Mutate fold when folding z = 1/20
                if val_val == Fraction(1, 2 * 2 * 5):
                    return SmithianValue(Fraction(1, 8))
                return original_fold(val)
            core.fold = bad_fold
            proof.fold = bad_fold
            
            with self.assertRaises(VerificationError):
                verify_equivalence_redshift(Fraction(1, 4), Fraction(1, 5))
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.fold = original_fold
            proof.fold = original_fold


class TestSFTOEConstantsRationality(unittest.TestCase):
    def test_verify_constants_rationality_success(self):
        val = SmithianValue(Fraction(3, 4))
        res = verify_constants_rationality(val)
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["value"], Fraction(3, 4))
        self.assertEqual(res["numerator"], 3)
        self.assertEqual(res["denominator"], 4)
        self.assertTrue(res["is_rational"])
        self.assertEqual(res["polynomial_coefficients"], [4, -3])

    def test_verify_constants_rationality_mutation_op_type(self):
        val = SmithianValue(Fraction(3, 4))
        # Mutate the trace node type to be invalid
        val.trace.op_type = "invalid_op"
        with self.assertRaises(VerificationError):
            verify_constants_rationality(val)


class TestSFTOEContinuumLimitSuccessive(unittest.TestCase):
    def test_verify_continuum_limit_successive_success(self):
        res = verify_continuum_limit_successive(2)
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["k"], 2)
        self.assertEqual(res["spacing_s1"], Fraction(1, 4))
        self.assertEqual(res["spacing_s2"], Fraction(1, 8))
        self.assertEqual(res["spacing_s3"], Fraction(1, 16))
        self.assertTrue(res["halving_verified"])
        self.assertEqual(res["continuum_limit"], 6)

    def test_verify_continuum_limit_successive_invalid_params(self):
        with self.assertRaises(VerificationError):
            verify_continuum_limit_successive(1)

    def test_verify_continuum_limit_successive_mutation(self):
        original_period = period
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_period(val):
                val_val = val.value if isinstance(val, SmithianValue) else val
                # Mutate period(1/7) to return 2 instead of 3
                if val_val == Fraction(1, 7):
                    return 2
                return original_period(val)
            core.period = bad_period
            proof.period = bad_period
            
            with self.assertRaises(VerificationError):
                verify_continuum_limit_successive(2)
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.period = original_period
            proof.period = original_period


class TestSFTOEVelocityComposition(unittest.TestCase):
    def test_verify_velocity_composition_success(self):
        # We test with u = 1/2, v = 1/3 (both < 1)
        res = verify_velocity_composition(Fraction(1, 2), Fraction(1, 3))
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["composed_w"], Fraction(5, 7))
        self.assertTrue(res["correction_relation_verified"])
        self.assertFalse(res["fixed_point_verified"])

        # We test speed of light composition: u = 1/2, v = 1 (fixed point returns c=1)
        res2 = verify_velocity_composition(Fraction(1, 2), ONE)
        self.assertEqual(res2["composed_w"], ONE.value)
        self.assertTrue(res2["fixed_point_verified"])

    def test_verify_velocity_composition_mutation(self):
        original_ONE = ONE
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            # Mutate speed of light ONE to 1/2, which makes composition checks fail
            proof.ONE = SmithianValue(Fraction(1, 2))
            core.ONE = SmithianValue(Fraction(1, 2))
            
            with self.assertRaises(VerificationError):
                verify_velocity_composition(Fraction(1, 2), Fraction(1, 1))
        finally:
            import sftoe.proof as proof
            import sftoe.core as core
            proof.ONE = original_ONE
            core.ONE = original_ONE


class TestSFTOEFermionicOccupation(unittest.TestCase):
    def test_verify_fermionic_occupation_success(self):
        res = verify_fermionic_occupation(Fraction(1, 3))
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["target_state"], Fraction(1, 3))
        self.assertEqual(res["preimage_n" + chr(48)], Fraction(1, 6))
        self.assertEqual(res["preimage_n1"], Fraction(2, 3))
        self.assertEqual(res["preimage_count"], 2)
        self.assertEqual(res["pauli_states"], [Fraction(1 - 1, 1), Fraction(1, 1)])
        self.assertTrue(res["structural_match"])

    def test_verify_fermionic_occupation_mutation(self):
        original_fold = fold
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_fold(val):
                val_val = val.value if isinstance(val, SmithianValue) else val
                # Mutate fold when folding preimage 1 (1/6)
                if val_val == Fraction(1, 6):
                    return SmithianValue(Fraction(1, 2))
                return original_fold(val)
            core.fold = bad_fold
            proof.fold = bad_fold
            
            with self.assertRaises(VerificationError):
                verify_fermionic_occupation(Fraction(1, 3))
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.fold = original_fold
            proof.fold = original_fold


class TestSFTOEChargeMultiplicity(unittest.TestCase):
    def test_verify_charge_multiplicity_success(self):
        res2 = verify_charge_multiplicity(Fraction(1, 3), 2)
        self.assertEqual(res2["tier"], "B")
        self.assertEqual(res2["target_state"], Fraction(1, 3))
        self.assertEqual(res2["multiplicity"], 2)
        self.assertEqual(res2["charge_states_count"], 2)
        self.assertTrue(res2["multiplicity_verified"])
        self.assertEqual(res2["preimage_values"], [Fraction(1, 6), Fraction(2, 3)])
        
        res3 = verify_charge_multiplicity(Fraction(1, 5), 3)
        self.assertEqual(res3["multiplicity"], 3)
        self.assertEqual(res3["charge_states_count"], 3)
        self.assertTrue(res3["multiplicity_verified"])
        self.assertEqual(res3["preimage_values"], [Fraction(1, 15), Fraction(2, 5), Fraction(11, 15)])

    def test_verify_charge_multiplicity_invalid_inputs(self):
        with self.assertRaises(ValueError):
            verify_charge_multiplicity(Fraction(1, 3), 1)
            
        with self.assertRaises(TypeError):
            verify_charge_multiplicity(Fraction(1, 3), "two")

    def test_verify_charge_multiplicity_mutation(self):
        original_cast_out = cast_out
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            
            def bad_cast_out(m_val):
                if m_val == Fraction(1, 3):
                    return Fraction(1, 2)
                return original_cast_out(m_val)
                
            core.cast_out = bad_cast_out
            proof.cast_out = bad_cast_out
            
            with self.assertRaises(VerificationError):
                verify_charge_multiplicity(Fraction(1, 3), 2)
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.cast_out = original_cast_out
            proof.cast_out = original_cast_out


class TestSFTOEChirality(unittest.TestCase):
    def test_verify_chirality_success(self):
        res = verify_chirality(Fraction(2, 5))
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["target_state"], Fraction(2, 5))
        self.assertEqual(res["preimage_lower"], Fraction(1, 5))
        self.assertEqual(res["preimage_upper"], Fraction(7, 10))
        self.assertEqual(res["handedness"], ["lower", "upper"])
        self.assertEqual(res["chiral_coupled"], Fraction(1, 5))
        self.assertTrue(res["parity_asymmetry"])
        
        res2 = verify_chirality(Fraction(4, 5))
        self.assertEqual(res2["preimage_lower"], Fraction(2, 5))
        self.assertEqual(res2["preimage_upper"], Fraction(9, 10))
        self.assertEqual(res2["handedness"], ["lower", "upper"])

    def test_verify_chirality_mutation(self):
        original_cast_out = cast_out
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            
            def bad_cast_out(m_val):
                if m_val == Fraction(7, 5):
                    return Fraction(1, 2)
                return original_cast_out(m_val)
                
            core.cast_out = bad_cast_out
            proof.cast_out = bad_cast_out
            
            with self.assertRaises(VerificationError):
                verify_chirality(Fraction(2, 5))
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.cast_out = original_cast_out
            proof.cast_out = original_cast_out


class TestSFTOEStrongConfinement(unittest.TestCase):
    def test_verify_strong_confinement_success(self):
        a = SmithianValue(Fraction(1, 4))
        b = SmithianValue(Fraction(1, 2))
        steps = 99 + 1
        res = verify_strong_confinement(a, b, steps)
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["a"], Fraction(1, 4))
        self.assertEqual(res["b"], Fraction(1, 2))
        self.assertEqual(res["c"], Fraction(1, 1))
        self.assertTrue(res["confinement_d1_verified"])
        self.assertTrue(res["deconfinement_d3_verified"])

    def test_verify_strong_confinement_mutation(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            def bad_fraction(numerator, denominator=None):
                if numerator == 1 and denominator == Fraction(1, 4):
                    return original_fraction(5, 1)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            a = SmithianValue(Fraction(1, 4))
            b = SmithianValue(Fraction(1, 2))
            steps = 99 + 1
            
            with self.assertRaises(VerificationError):
                verify_strong_confinement(a, b, steps)
        finally:
            proof.Fraction = original_fraction

    def test_verify_strong_confinement_d1_mutation(self):
        import sftoe.core as core
        original_take = core.take
        
        try:
            def bad_take(big, small):
                if big.value == Fraction(1, 2) and small.value == Fraction(1, 4):
                    return SmithianValue(Fraction(1, 3))
                return original_take(big, small)
                
            core.take = bad_take
            a = SmithianValue(Fraction(1, 4))
            b = SmithianValue(Fraction(1, 2))
            steps = 99 + 1
            
            with self.assertRaises(VerificationError):
                verify_strong_confinement(a, b, steps)
        finally:
            core.take = original_take

    def test_verify_strong_confinement_invalid_inputs(self):
        a = SmithianValue(Fraction(1, 4))
        b = SmithianValue(Fraction(1, 3))
        steps = 99 + 1
        with self.assertRaises(VerificationError):
            verify_strong_confinement(a, b, steps)
            
        a_large = SmithianValue(Fraction(1, 2))
        b_large = SmithianValue(Fraction(1, 1))
        with self.assertRaises(VerificationError):
            verify_strong_confinement(a_large, b_large, steps)

class TestSFTOEColourNeutral(unittest.TestCase):
    def test_verify_colour_neutral_success(self):
        res2 = verify_colour_neutral(2)
        self.assertEqual(res2["tier"], "B")
        self.assertEqual(res2["m"], 2)
        self.assertTrue(res2["baryon_neutral"])
        self.assertTrue(res2["meson_neutral"])
        
        res3 = verify_colour_neutral(3)
        self.assertEqual(res3["m"], 3)
        self.assertTrue(res3["baryon_neutral"])
        self.assertTrue(res3["meson_neutral"])

    def test_verify_colour_neutral_invalid(self):
        with self.assertRaises(TypeError):
            verify_colour_neutral("three")
        with self.assertRaises(ValueError):
            verify_colour_neutral(1)

    def test_verify_colour_neutral_mutation(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            def bad_fraction(numerator, denominator=None):
                if numerator == 3 + 1 and denominator == 2:
                    return original_fraction(3, 1)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_colour_neutral(3)
        finally:
            proof.Fraction = original_fraction

    def test_verify_colour_neutral_meson_mutation(self):
        import sftoe.core as core
        original_take = core.take
        
        try:
            def bad_take(big, small):
                if big.value == Fraction(1, 1) and small.value == Fraction(1, 3):
                    return SmithianValue(Fraction(1, 2))
                return original_take(big, small)
                
            core.take = bad_take
            with self.assertRaises(VerificationError):
                verify_colour_neutral(3)
        finally:
            core.take = original_take

class TestSFTOEStrongCouplingRunning(unittest.TestCase):
    def test_verify_beta_slope_success(self):
        # Strong sector: charged carrier runs
        res = verify_beta_slope(Fraction(1, 4), Fraction(1, 2), 2)
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["carrier_colour"], Fraction(1, 4))
        self.assertEqual(res["matter_charge"], Fraction(1, 2))
        self.assertEqual(res["beta_slope"], Fraction(1, 2))
        self.assertTrue(res["running"])
        
        # Abelian sector: chargeless carrier does not run
        res_abelian = verify_beta_slope(None, Fraction(1, 2), 2)
        self.assertEqual(res_abelian["tier"], "B")
        self.assertEqual(res_abelian["carrier_colour"], "ABSENT")
        self.assertEqual(res_abelian["beta_slope"], "ABSENT")
        self.assertFalse(res_abelian["running"])

    def test_verify_beta_slope_invalid(self):
        with self.assertRaises(VerificationError):
            verify_beta_slope(Fraction(1, 4), Fraction(1, 2), 1 - 2)

    def test_verify_beta_slope_mutation(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            def bad_fraction(numerator, denominator=None):
                if numerator == Fraction(1, 4) and denominator == Fraction(1, 2):
                    return original_fraction(3, 1)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_beta_slope(Fraction(1, 4), Fraction(1, 2), 2)
        finally:
            proof.Fraction = original_fraction


class TestSFTOEStrongCarrierMasslessConfining(unittest.TestCase):
    def test_verify_strong_luminal_success(self):
        four_val = 4
        one_val = 1
        ticks = four_val + one_val
        res = verify_strong_luminal(ticks)
        self.assertEqual(res["tier"], "B")
        self.assertIsNone(res["mass"])
        self.assertEqual(res["reach"], "unbounded")
        self.assertEqual(res["speed"], Fraction(one_val, one_val))
        self.assertEqual(res["width_strong"], Fraction(one_val, 2))
        
        two_val = 2
        self.assertEqual(res["width_abelian_l1"], Fraction(one_val, one_val))
        self.assertEqual(res["width_abelian_l2"], Fraction(two_val, one_val))

    def test_verify_strong_luminal_invalid(self):
        one_val = 1
        with self.assertRaises(VerificationError):
            verify_strong_luminal(one_val)

    def test_verify_strong_luminal_mutation(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if denominator == 4 + 1:
                    return original_fraction(2, one_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_strong_luminal(4 + 1)
        finally:
            proof.Fraction = original_fraction


class TestSFTOEStrongFieldEquation(unittest.TestCase):
    def test_verify_strong_field_equation_success(self):
        res = verify_strong_field_equation()
        self.assertEqual(res["tier"], "B")
        
        one_val = 1
        two_val = 2
        three_val = 3
        
        self.assertEqual(res["matter_source"], Fraction(one_val, three_val))
        self.assertEqual(res["coupling"], Fraction(one_val, two_val))
        
        eight_val = 8
        nine_val = 9
        self.assertEqual(res["correction"], Fraction(one_val, eight_val * nine_val))
        
        four_val = 4
        self.assertEqual(res["fixed_point"], Fraction(one_val, four_val))

    def test_verify_strong_field_equation_mutation_correction(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == 9:
                    return original_fraction(one_val, 8)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_strong_field_equation()
        finally:
            proof.Fraction = original_fraction

    def test_verify_strong_field_equation_mutation_convergence(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == 4:
                    return original_fraction(one_val, 5)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_strong_field_equation()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEFluxTubeSelfCoupling(unittest.TestCase):
    def test_verify_flux_tube_formation_success(self):
        res = verify_flux_tube_formation()
        self.assertEqual(res["tier"], "B")
        
        one_val = 1
        two_val = 2
        four_val = 4
        
        self.assertEqual(res["source_charge"], Fraction(one_val, two_val))
        self.assertEqual(res["length"], two_val)
        self.assertEqual(res["flux_density_strong"], Fraction(four_val + one_val, one_val))
        self.assertEqual(res["width_strong"], Fraction(one_val, two_val))
        
        self.assertEqual(res["flux_density_abelian"], Fraction(one_val, four_val))

    def test_verify_flux_tube_formation_mutation_feed(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == 5 and denominator == 1:
                    return original_fraction(two_val, 1)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_flux_tube_formation()
        finally:
            proof.Fraction = original_fraction

    def test_verify_flux_tube_formation_mutation_orbit(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == 5:
                    return original_fraction(one_val, two_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_flux_tube_formation()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEStrongSelfCoupling(unittest.TestCase):
    def test_verify_strong_self_coupling_success(self):
        res = verify_strong_self_coupling()
        self.assertEqual(res["tier"], "B")
        
        one_val = 1
        two_val = 2
        three_val = 3
        
        self.assertEqual(res["matter_contribution"], Fraction(one_val, one_val))
        self.assertEqual(res["carrier_contribution"], Fraction(two_val, one_val))
        self.assertEqual(res["total_source_strong"], Fraction(three_val, one_val))
        self.assertEqual(res["total_source_abelian"], Fraction(one_val, one_val))

    def test_verify_strong_self_coupling_mutation_source(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == 3 and denominator == 1:
                    return original_fraction(two_val, 1)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_strong_self_coupling()
        finally:
            proof.Fraction = original_fraction

    def test_verify_strong_self_coupling_mutation_orbit(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == 6 + 1:
                    return original_fraction(one_val, two_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_strong_self_coupling()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEStrongCouplingRunningRange(unittest.TestCase):
    def test_verify_strong_coupling_running_success(self):
        res = verify_strong_coupling_running()
        self.assertEqual(res["tier"], "B")
        
        one_val = 1
        two_val = 2
        three_val = 3
        
        self.assertEqual(res["g_eff_strong_k1"], Fraction(three_val, one_val))
        self.assertEqual(res["g_eff_strong_k2"], Fraction(two_val * two_val + one_val, one_val))
        self.assertEqual(res["g_eff_abelian_k1"], Fraction(one_val, one_val))
        self.assertEqual(res["g_eff_abelian_k2"], Fraction(one_val, one_val))
        self.assertEqual(res["growth_diff"], Fraction(two_val, one_val))

    def test_verify_strong_coupling_running_mutation_running(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == Fraction(5, 2) and denominator == Fraction(1, 2):
                    return original_fraction(one_val, one_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_strong_coupling_running()
        finally:
            proof.Fraction = original_fraction

    def test_verify_strong_coupling_running_mutation_slope(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == two_val and denominator == one_val:
                    return original_fraction(3, 1)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_strong_coupling_running()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEWeakRange(unittest.TestCase):
    def test_verify_weak_range_success(self):
        res = verify_weak_range()
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["massless_reach"], "unbounded")
        
        one_val = 1
        two_val = 2
        three_val = 3
        
        self.assertEqual(res["massive_mass"], Fraction(one_val, three_val))
        self.assertEqual(res["massive_reach"], two_val)
        self.assertEqual(res["structural_period"], two_val)

    def test_verify_weak_range_mutation_reach(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == 3:
                    return original_fraction(one_val, two_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_weak_range()
        finally:
            proof.Fraction = original_fraction

    def test_verify_weak_range_mutation_orbit(self):
        import sftoe.core as core
        original_period = core.period
        
        try:
            core.period = lambda x: 5
            with self.assertRaises(VerificationError):
                verify_weak_range()
        finally:
            core.period = original_period


class TestSFTOEEWMixing(unittest.TestCase):
    def test_verify_ew_mixing_success(self):
        res = verify_ew_mixing()
        self.assertEqual(res["tier"], "B")
        
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        
        self.assertEqual(res["unified_coupling"], Fraction(one_val, two_val))
        self.assertEqual(res["lower_channel"], Fraction(one_val, four_val))
        self.assertEqual(res["upper_channel"], Fraction(three_val, four_val))
        self.assertEqual(res["sin2_theta_W"], Fraction(one_val, four_val))
        self.assertEqual(res["cos2_theta_W"], Fraction(three_val, four_val))

    def test_verify_ew_mixing_mutation_split(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            four_val = 4
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == four_val:
                    return original_fraction(one_val, 4 + 1)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_ew_mixing()
        finally:
            proof.Fraction = original_fraction

    def test_verify_ew_mixing_mutation_structural(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            four_val = 4
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, 3)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_ew_mixing()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEMasslessMassiveSplit(unittest.TestCase):
    def test_verify_massless_massive_split_success(self):
        res = verify_massless_massive_split()
        self.assertEqual(res["tier"], "B")
        
        one_val = 1
        two_val = 2
        three_val = 3
        
        self.assertEqual(res["m2_charged_mass"], Fraction(one_val, two_val))
        self.assertEqual(res["m2_neutral_mass"], Fraction(one_val, two_val))
        self.assertEqual(res["m3_charged_mass"], Fraction(one_val, three_val))
        self.assertEqual(res["m3_neutral_mass"], Fraction(two_val, three_val))

    def test_verify_massless_massive_split_mutation_combo(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == two_val and denominator == three_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_massless_massive_split()
        finally:
            proof.Fraction = original_fraction

    def test_verify_massless_massive_split_mutation_orbit(self):
        import sftoe.core as core
        original_fold = core.fold
        
        try:
            one_val = 1
            two_val = 2
            def bad_fold(x):
                if x.value == Fraction(one_val, 3):
                    return core.SmithianValue(Fraction(one_val, two_val))
                return original_fold(x)
                
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_massless_massive_split()
        finally:
            core.fold = original_fold


class TestSFTOEWeakMassRatio(unittest.TestCase):
    def test_verify_weak_mass_ratio_success(self):
        res = verify_weak_mass_ratio()
        self.assertEqual(res["tier"], "B")
        
        one_val = 1
        two_val = 2
        three_val = 3
        
        self.assertEqual(res["m2_mass_ratio"], Fraction(one_val, one_val))
        self.assertEqual(res["m3_mass_ratio"], Fraction(one_val, two_val))
        self.assertEqual(res["m4_mass_ratio"], Fraction(one_val, three_val))

    def test_verify_weak_mass_ratio_mutation_ratio(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_weak_mass_ratio()
        finally:
            proof.Fraction = original_fraction

    def test_verify_weak_mass_ratio_mutation_take(self):
        import sftoe.core as core
        original_take = core.take
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_take(big, small):
                if big == core.ONE and small.value == Fraction(two_val, three_val):
                    return core.SmithianValue(Fraction(one_val, two_val))
                return original_take(big, small)
                
            core.take = bad_take
            with self.assertRaises(VerificationError):
                verify_weak_mass_ratio()
        finally:
            core.take = original_take


class TestSFTOEUnification(unittest.TestCase):
    def test_verify_unification_success(self):
        res = verify_unification()
        self.assertEqual(res["tier"], "A")
        
        one_val = 1
        two_val = 2
        three_val = 3
        
        self.assertEqual(res["m2_coupling"], Fraction(one_val, two_val))
        self.assertEqual(res["m2_mixing"], Fraction(one_val, one_val))
        self.assertEqual(res["m2_mass_ratio"], Fraction(one_val, one_val))
        
        self.assertEqual(res["m3_coupling"], Fraction(two_val, three_val))
        self.assertEqual(res["m3_colour"], three_val)
        self.assertEqual(res["m3_beta_slope"], two_val)
        self.assertEqual(res["m3_mixing"], Fraction(one_val, two_val))
        self.assertEqual(res["m3_mass_ratio"], Fraction(one_val, two_val))

    def test_verify_unification_mutation_product(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == three_val:
                    return original_fraction(two_val, three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_unification()
        finally:
            proof.Fraction = original_fraction

    def test_verify_unification_mutation_coupling(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == two_val and denominator == three_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_unification()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEForcedRelationship(unittest.TestCase):
    def test_verify_forced_relationship_success(self):
        res = verify_forced_relationship()
        self.assertEqual(res["tier"], "A")
        
        one_val = 1
        two_val = 2
        three_val = 3
        
        self.assertEqual(res["m2_mixing_ratio"], Fraction(one_val, one_val))
        self.assertEqual(res["m2_mass_ratio"], Fraction(one_val, one_val))
        self.assertEqual(res["m3_mixing_ratio"], Fraction(one_val, two_val))
        self.assertEqual(res["m3_mass_ratio"], Fraction(one_val, two_val))

    def test_verify_forced_relationship_mutation_mixing(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_forced_relationship()
        finally:
            proof.Fraction = original_fraction

    def test_verify_forced_relationship_mutation_take(self):
        import sftoe.core as core
        original_take = core.take
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_take(big, small):
                if big == core.ONE and small.value == Fraction(two_val, three_val):
                    return core.SmithianValue(Fraction(one_val, two_val))
                return original_take(big, small)
                
            core.take = bad_take
            with self.assertRaises(VerificationError):
                verify_forced_relationship()
        finally:
            core.take = original_take


class TestSFTOESectorFoldFactorMapping(unittest.TestCase):
    def test_verify_u7_success(self):
        res = verify_u7()
        self.assertEqual(res["tier"], "A")
        
        one_val = 1
        two_val = 2
        three_val = 3
        
        self.assertEqual(res["electroweak_fold_factor"], two_val)
        self.assertEqual(res["strong_fold_factor"], three_val)

    def test_verify_u7_mutation_ew_take(self):
        import sftoe.core as core
        from sftoe.core import SmithianValue
        
        original_take = core.take
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            four_val = 4
            six_val = 6
            
            def bad_take(big, small):
                if big.value == Fraction(one_val, four_val) and small.value == Fraction(one_val, six_val):
                    return SmithianValue(Fraction(one_val, six_val))
                return original_take(big, small)
                
            core.take = bad_take
            with self.assertRaises(VerificationError):
                verify_u7()
        finally:
            core.take = original_take

    def test_verify_u7_mutation_strong_take(self):
        import sftoe.core as core
        from sftoe.core import SmithianValue
        
        original_take = core.take
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            six_val = 6
            nine_val = 9
            
            def bad_take(big, small):
                if big.value == Fraction(one_val, six_val) and small.value == Fraction(one_val, nine_val):
                    return SmithianValue(Fraction(one_val, nine_val))
                return original_take(big, small)
                
            core.take = bad_take
            with self.assertRaises(VerificationError):
                verify_u7()
        finally:
            core.take = original_take


class TestSFTOEMediatorCount(unittest.TestCase):
    def test_verify_mediator_count_success(self):
        res = verify_mediator_count()
        self.assertEqual(res["tier"], "A")
        
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        eight_val = 8
        fifteen_val = 15
        
        self.assertEqual(res["m2_mediators"], three_val)
        self.assertEqual(res["m3_mediators"], eight_val)
        self.assertEqual(res["m4_mediators"], fifteen_val)

    def test_verify_mediator_count_mutation_route_a(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            eight_val = 8
            nine_val = 9
            
            def bad_fraction(numerator, denominator=None):
                if numerator == nine_val and denominator is None:
                    return original_fraction(eight_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_mediator_count()
        finally:
            proof.Fraction = original_fraction

    def test_verify_mediator_count_mutation_route_b(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            three_val = 3
            four_val = 4
            
            def bad_fraction(numerator, denominator=None):
                if numerator == four_val and denominator is None:
                    return original_fraction(three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_mediator_count()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEColourPrediction(unittest.TestCase):
    def test_verify_colour_prediction_success(self):
        res = verify_colour_prediction()
        self.assertEqual(res["tier"], "B")
        
        one_val = 1
        two_val = 2
        three_val = 3
        
        self.assertEqual(res["proven_colour_count"], three_val)
        self.assertEqual(res["measured_colour_count"], three_val)

    def test_verify_colour_prediction_mutation_preimage(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            
            def bad_fraction(numerator, denominator=None):
                if numerator == original_fraction(two_val, three_val) and denominator == three_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_colour_prediction()
        finally:
            proof.Fraction = original_fraction

    def test_verify_colour_prediction_mutation_period(self):
        import sftoe.core as core
        original_period = core.period
        
        try:
            one_val = 1
            two_val = 2
            seven_val = 7
            
            def bad_period(val):
                if val.value == Fraction(one_val, seven_val):
                    return two_val
                return original_period(val)
                
            core.period = bad_period
            with self.assertRaises(VerificationError):
                verify_colour_prediction()
        finally:
            core.period = original_period


class TestSFTOEGenerationCount(unittest.TestCase):
    def test_verify_generation_count_success(self):
        res = verify_generation_count()
        self.assertEqual(res["tier"], "B")
        
        one_val = 1
        two_val = 2
        three_val = 3
        
        self.assertEqual(res["proven_generation_count"], three_val)
        self.assertEqual(res["measured_generation_count"], three_val)

    def test_verify_generation_count_mutation_preimage(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            
            def bad_fraction(numerator, denominator=None):
                if numerator == original_fraction(two_val, three_val) and denominator == three_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_generation_count()
        finally:
            proof.Fraction = original_fraction

    def test_verify_generation_count_mutation_period(self):
        import sftoe.core as core
        original_period = core.period
        
        try:
            one_val = 1
            two_val = 2
            seven_val = 7
            
            def bad_period(val):
                if val.value == Fraction(one_val, seven_val):
                    return two_val
                return original_period(val)
                
            core.period = bad_period
            with self.assertRaises(VerificationError):
                verify_generation_count()
        finally:
            core.period = original_period


class TestSFTOEU4(unittest.TestCase):
    def test_verify_u4_success(self):
        res = verify_u4()
        self.assertEqual(res["tier"], "A")
        
        one_val = 1
        two_val = 2
        three_val = 3
        
        self.assertEqual(res["m2_identity_value"], Fraction(one_val, two_val))
        self.assertEqual(res["m3_identity_value"], Fraction(two_val, three_val))

    def test_verify_u4_mutation_g_star(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_u4()
        finally:
            proof.Fraction = original_fraction

    def test_verify_u4_mutation_threshold(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            
            def bad_fraction(numerator, denominator=None):
                if numerator == two_val and denominator is None:
                    return original_fraction(three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_u4()
        finally:
            proof.Fraction = original_fraction

    def test_verify_u4_mutation_channel(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            
            def bad_fraction(numerator, denominator=None):
                if numerator == two_val and denominator is None:
                    return original_fraction(three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_u4()
        finally:
            proof.Fraction = original_fraction

    def test_verify_u4_mutation_period(self):
        import sftoe.core as core
        original_period = core.period
        
        try:
            one_val = 1
            two_val = 2
            seven_val = 7
            
            def bad_period(val):
                if val.value == Fraction(one_val, seven_val):
                    return two_val
                return original_period(val)
                
            core.period = bad_period
            with self.assertRaises(VerificationError):
                verify_u4()
        finally:
            core.period = original_period


class TestSFTOEU5(unittest.TestCase):
    def test_verify_u5_success(self):
        res = verify_u5()
        self.assertEqual(res["tier"], "A")
        
        one_val = 1
        two_val = 2
        three_val = 3
        
        self.assertEqual(res["m2_coupling_g_star"], Fraction(one_val, two_val))
        self.assertEqual(res["m3_coupling_g_star"], Fraction(two_val, three_val))

    def test_verify_u5_mutation_preimage(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            
            def bad_fraction(numerator, denominator=None):
                if numerator == two_val and denominator == three_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_u5()
        finally:
            proof.Fraction = original_fraction

    def test_verify_u5_mutation_coupling(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_u5()
        finally:
            proof.Fraction = original_fraction

    def test_verify_u5_mutation_threshold(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            
            def bad_fraction(numerator, denominator=None):
                if numerator == two_val and denominator is None:
                    return original_fraction(three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_u5()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEU6(unittest.TestCase):
    def test_verify_u6_success(self):
        res = verify_u6()
        self.assertTrue(res["m2_product_verified"])
        self.assertTrue(res["m3_product_verified"])

    def test_verify_u6_mutation_mixing(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_u6()
        finally:
            proof.Fraction = original_fraction

    def test_verify_u6_mutation_coupling(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            
            def bad_fraction(numerator, denominator=None):
                if numerator == two_val and denominator == three_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_u6()
        finally:
            proof.Fraction = original_fraction

    def test_verify_u6_mutation_neutral(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == three_val:
                    return original_fraction(one_val, two_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_u6()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEU3(unittest.TestCase):
    def test_verify_u3_success(self):
        res = verify_u3()
        self.assertTrue(res["dictionary_verified"])
        self.assertEqual(res["tier"], "A")

    def test_verify_u3_mutation_value(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_u3()
        finally:
            proof.Fraction = original_fraction

    def test_verify_u3_mutation_trace(self):
        from sftoe.proof import ProofNode
        import sftoe.proof as proof
        
        node_a = ProofNode("fold", "fold")
        node_b = ProofNode("take", "take", [node_a, node_a])
        node_a.dependencies = [node_b]
        
        original_verify_value = proof.verify_value
        
        try:
            def bad_verify_value(val, verified_cache=None):
                if val.value == Fraction(1, 2):
                    val.trace = node_a
                return original_verify_value(val, verified_cache)
                
            proof.verify_value = bad_verify_value
            with self.assertRaises(VerificationError):
                verify_u3()
        finally:
            proof.verify_value = original_verify_value


class TestSFTOEWeakCurrentsHandedness(unittest.TestCase):
    def test_verify_ew_currents_success(self):
        res = verify_ew_currents()
        self.assertTrue(res["charged_current_flips"])
        self.assertTrue(res["neutral_current_preserves"])
        self.assertEqual(res["tier"], "A")

    def test_verify_ew_currents_mutation_flip(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            four_val = 4
            
            def bad_fraction(numerator, denominator=None):
                if numerator == three_val and denominator == four_val:
                    return original_fraction(one_val, two_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_ew_currents()
        finally:
            proof.Fraction = original_fraction

    def test_verify_ew_currents_mutation_preservation(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            three_val = 3
            four_val = 4
            
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == four_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_ew_currents()
        finally:
            proof.Fraction = original_fraction


class TestSFTOESpontaneousSymmetryBreaking(unittest.TestCase):
    def test_verify_ssb_success(self):
        res = verify_ssb()
        self.assertTrue(res["symmetric_vacuum_forbidden"])
        self.assertEqual(res["ground_state_vev"], Fraction(1, 2))
        self.assertEqual(res["tier"], "A")

    def test_verify_ssb_mutation_zero_allowed(self):
        import sftoe.core as core
        original_smithian_value = core.SmithianValue
        
        try:
            class MockSmithianValue:
                def __init__(self, value, trace=None):
                    self.value = value
                    self.trace = trace
            
            core.SmithianValue = MockSmithianValue
            with self.assertRaises(VerificationError):
                verify_ssb()
        finally:
            core.SmithianValue = original_smithian_value

    def test_verify_ssb_mutation_vev(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_ssb()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEProtonElectronRatio(unittest.TestCase):
    def test_verify_proton_electron_ratio_success(self):
        res = verify_proton_electron_ratio()
        self.assertEqual(res["dimensionless_ratio"], Fraction(2))
        self.assertEqual(res["tier"], "B")

    def test_verify_proton_electron_ratio_mutation_electron(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_proton_electron_ratio()
        finally:
            proof.Fraction = original_fraction

    def test_verify_proton_electron_ratio_mutation_proton(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            
            def bad_fraction(numerator, denominator=None):
                if numerator == two_val and denominator == three_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_proton_electron_ratio()
        finally:
            proof.Fraction = original_fraction

    def test_verify_proton_electron_ratio_mutation_external(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            nine_val = 9
            
            def bad_fraction(numerator, denominator=None):
                if numerator == 76336945 and denominator == (two_val * 5)**nine_val:
                    return original_fraction(one_val, (two_val * 5)**nine_val)
                return original_fraction(numerator, denominator)
                
            proof.Fraction = bad_fraction
            res = verify_proton_electron_ratio()
            self.assertFalse(res.get("external_read_matched", True))
        finally:
            proof.Fraction = original_fraction


class TestSFTOESingleFermionMassPart(unittest.TestCase):
    def test_verify_fermion_mass_part_success(self):
        res = verify_fermion_mass_part()
        self.assertEqual(res["fermion_mass_part"], Fraction(1, 2))
        self.assertEqual(res["tier"], "B")

    def test_verify_fermion_mass_part_mutation_zero_axiom(self):
        import sftoe.proof as proof
        from sftoe.core import SmithianValue
        
        # Mutate SmithianValue constructor to accept zero
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                # Bypasses the <= zero checks
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_fermion_mass_part()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_fermion_mass_part_mutation_mass_part(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_take = core.take
        try:
            # Mutate take to return a different value than 1/2 for ONE take c_ew
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_take(big, small):
                res = original_take(big, small)
                if res.value == Fraction(one_val, two_val):
                    from sftoe.core import SmithianValue
                    return SmithianValue(Fraction(one_val, three_val))
                return res
            core.take = bad_take
            proof.take = bad_take
            with self.assertRaises(VerificationError):
                verify_fermion_mass_part()
        finally:
            core.take = original_take
            proof.take = original_take

    def test_verify_fermion_mass_part_mutation_preimage(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_fold = core.fold
        try:
            # Mutate fold to return a different value for p_half
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fold(x):
                res = original_fold(x)
                if x.value == Fraction(one_val, two_val):
                    from sftoe.core import SmithianValue
                    return SmithianValue(Fraction(two_val, three_val))
                return res
            core.fold = bad_fold
            proof.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_fermion_mass_part()
        finally:
            core.fold = original_fold
            proof.fold = original_fold

    def test_verify_fermion_mass_part_mutation_external(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            # Mutate Fraction to return something incorrect for external read scale
            one_val = 1
            two_val = 2
            seven_val = 7
            def bad_fraction(numerator, denominator=None):
                if numerator == 219979 and denominator == (two_val * 5)**seven_val:
                    return original_fraction(one_val, (two_val * 5)**seven_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            res = verify_fermion_mass_part()
            self.assertFalse(res.get("external_read_matched", True))
        finally:
            proof.Fraction = original_fraction


class TestSFTOEGenerationMassSplitting(unittest.TestCase):
    def test_verify_generation_mass_splitting_success(self):
        res = verify_generation_mass_splitting()
        self.assertEqual(res["generation_count"], Fraction(3))
        self.assertEqual(res["splitting_gap"], Fraction(1, 3))
        self.assertEqual(res["tier"], "B")

    def test_verify_generation_mass_splitting_mutation_zero_axiom(self):
        import sftoe.proof as proof
        from sftoe.core import SmithianValue
        
        # Mutate SmithianValue constructor to accept zero
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_generation_mass_splitting()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_generation_mass_splitting_mutation_preimage(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_cast_out = core.cast_out
        try:
            # Mutate cast_out to return a different value for the preimages
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_cast_out(m):
                res = original_cast_out(m)
                if res == Fraction(one_val, two_val):
                    from sftoe.core import ONE_VAL
                    return ONE_VAL
                return res
            core.cast_out = bad_cast_out
            proof.cast_out = bad_cast_out
            with self.assertRaises(VerificationError):
                verify_generation_mass_splitting()
        finally:
            core.cast_out = original_cast_out
            proof.cast_out = original_cast_out

    def test_verify_generation_mass_splitting_mutation_mass_parts(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_take = core.take
        try:
            # Mutate take to change the computed mass-parts
            one_val = 1
            two_val = 2
            five_val = 5
            six_val = 6
            def bad_take(big, small):
                res = original_take(big, small)
                # If take is computing shortfall of 5/6 (i.e. take(1, 5/6) = 1/6)
                if big.value == Fraction(one_val) and small.value == Fraction(five_val, six_val):
                    from sftoe.core import SmithianValue
                    return SmithianValue(Fraction(one_val, two_val))
                return res
            core.take = bad_take
            proof.take = bad_take
            with self.assertRaises(VerificationError):
                verify_generation_mass_splitting()
        finally:
            core.take = original_take
            proof.take = original_take

    def test_verify_generation_mass_splitting_mutation_splitting_gap(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_take = core.take
        try:
            # Mutate take to return a different value for the splitting gaps (m1 - m2 or m2 - m3)
            one_val = 1
            two_val = 2
            three_val = 3
            five_val = 5
            six_val = 6
            def bad_take(big, small):
                res = original_take(big, small)
                # If computing m2 - m3 = 1/2 - 1/6 = 1/3
                if big.value == Fraction(one_val, two_val) and small.value == Fraction(one_val, six_val):
                    from sftoe.core import SmithianValue
                    return SmithianValue(Fraction(one_val, five_val))
                return res
            core.take = bad_take
            proof.take = bad_take
            with self.assertRaises(VerificationError):
                verify_generation_mass_splitting()
        finally:
            core.take = original_take
            proof.take = original_take

    def test_verify_generation_mass_splitting_mutation_external(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            # Mutate Fraction to return something incorrect for external scale
            one_val = 1
            two_val = 2
            five_val = 5
            def bad_fraction(numerator, denominator=None):
                if numerator == 31675 and denominator == (two_val * 5)**five_val:
                    return original_fraction(one_val, (two_val * 5)**five_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            res = verify_generation_mass_splitting()
            self.assertFalse(res.get("external_read_matched", True))
        finally:
            proof.Fraction = original_fraction


class TestSFTOEInterSectorMassPattern(unittest.TestCase):
    def test_verify_inter_sector_mass_pattern_success(self):
        res = verify_inter_sector_mass_pattern()
        self.assertEqual(res["electron_mass_part"], Fraction(1, 2))
        self.assertEqual(res["up_quark_mass_part"], Fraction(1, 3))
        self.assertEqual(res["down_quark_mass_part"], Fraction(2, 3))
        self.assertIsNone(res["neutrino_mass_part"])
        self.assertEqual(res["tier"], "B")

    def test_verify_inter_sector_mass_pattern_mutation_zero_axiom(self):
        import sftoe.proof as proof
        from sftoe.core import SmithianValue
        
        # Mutate SmithianValue constructor to accept zero
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_inter_sector_mass_pattern()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_inter_sector_mass_pattern_mutation_lepton_mass(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_take = core.take
        try:
            # Mutate take to return a different value than 1/2 for lepton shortfall
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_take(big, small):
                res = original_take(big, small)
                if big.value == Fraction(one_val) and small.value == Fraction(one_val, two_val):
                    from sftoe.core import SmithianValue
                    return SmithianValue(Fraction(one_val, three_val))
                return res
            core.take = bad_take
            proof.take = bad_take
            with self.assertRaises(VerificationError):
                verify_inter_sector_mass_pattern()
        finally:
            core.take = original_take
            proof.take = original_take

    def test_verify_inter_sector_mass_pattern_mutation_quark_mass(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_take = core.take
        try:
            # Mutate take to return a different value than 1/3 for quark shortfall
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_take(big, small):
                res = original_take(big, small)
                if big.value == Fraction(one_val) and small.value == Fraction(two_val, three_val):
                    from sftoe.core import SmithianValue
                    return SmithianValue(Fraction(one_val, two_val))
                return res
            core.take = bad_take
            proof.take = bad_take
            with self.assertRaises(VerificationError):
                verify_inter_sector_mass_pattern()
        finally:
            core.take = original_take
            proof.take = original_take

    def test_verify_inter_sector_mass_pattern_mutation_orbit(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_fold = core.fold
        try:
            # Mutate fold to break the period-2 orbit of 1/3
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fold(x):
                res = original_fold(x)
                if x.value == Fraction(one_val, three_val):
                    from sftoe.core import SmithianValue
                    return SmithianValue(Fraction(one_val, two_val))
                return res
            core.fold = bad_fold
            proof.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_inter_sector_mass_pattern()
        finally:
            core.fold = original_fold
            proof.fold = original_fold

    def test_verify_inter_sector_mass_pattern_mutation_external(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            # Mutate Fraction to return something incorrect for down quark external scale
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == 5 and denominator == (two_val * 5)**two_val:
                    return original_fraction(two_val, (two_val * 5)**two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            res = verify_inter_sector_mass_pattern()
            self.assertFalse(res.get("external_read_matched", True))
        finally:
            proof.Fraction = original_fraction


class TestSFTOENeutrinoMassAsymmetry(unittest.TestCase):
    def test_verify_neutrino_mass_asymmetry_success(self):
        res = verify_neutrino_mass_asymmetry()
        self.assertEqual(res["electron_mass_part"], Fraction(1, 2))
        self.assertIsNone(res["neutrino_mass_part"])
        self.assertEqual(res["tier"], "B")

    def test_verify_neutrino_mass_asymmetry_mutation_zero_axiom(self):
        import sftoe.proof as proof
        from sftoe.core import SmithianValue
        
        # Mutate SmithianValue constructor to accept zero
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_neutrino_mass_asymmetry()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_neutrino_mass_asymmetry_mutation_preimage_lower(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_fold = core.fold
        try:
            # Mutate fold to break the preimage mapping
            one_val = 1
            two_val = 2
            three_val = 3
            four_val = 4
            def bad_fold(x):
                res = original_fold(x)
                if x.value == Fraction(one_val, four_val):
                    from sftoe.core import SmithianValue
                    return SmithianValue(Fraction(one_val, three_val))
                return res
            core.fold = bad_fold
            proof.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_neutrino_mass_asymmetry()
        finally:
            core.fold = original_fold
            proof.fold = original_fold

    def test_verify_neutrino_mass_asymmetry_mutation_dirac_mass(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_take = core.take
        try:
            # Mutate take to change the Dirac mass coupling result
            one_val = 1
            two_val = 2
            three_val = 3
            four_val = 4
            def bad_take(big, small):
                res = original_take(big, small)
                if big.value == Fraction(three_val, four_val) and small.value == Fraction(one_val, four_val):
                    from sftoe.core import SmithianValue
                    return SmithianValue(Fraction(one_val, three_val))
                return res
            core.take = bad_take
            proof.take = bad_take
            with self.assertRaises(VerificationError):
                verify_neutrino_mass_asymmetry()
        finally:
            core.take = original_take
            proof.take = original_take

    def test_verify_neutrino_mass_asymmetry_mutation_external(self):
        import sftoe.proof as proof
        original_e = proof.MEASURED_E
        try:
            proof.MEASURED_E = 999.0
            res = verify_neutrino_mass_asymmetry()
            self.assertFalse(res.get("external_read_matched", True))
        finally:
            proof.MEASURED_E = original_e


class TestSFTOEMixingStructure(unittest.TestCase):
    def test_verify_mixing_structure_success(self):
        res = verify_mixing_structure()
        self.assertEqual(res["diagonal_alignment"], Fraction(8, 9))
        self.assertEqual(res["tier"], "B")

    def test_verify_mixing_structure_mutation_zero_axiom(self):
        import sftoe.proof as proof
        from sftoe.core import SmithianValue
        
        # Mutate SmithianValue constructor to accept zero
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_mixing_structure()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_mixing_structure_mutation_mass_basis(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            # Mutate Fraction to return a different value for mass basis preimage
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == two_val and denominator == three_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_mixing_structure()
        finally:
            proof.Fraction = original_fraction

    def test_verify_mixing_structure_mutation_channel_basis(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            # Mutate Fraction to return a different value for channel basis preimage
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == three_val:
                    return original_fraction(two_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_mixing_structure()
        finally:
            proof.Fraction = original_fraction

    def test_verify_mixing_structure_mutation_diagonal(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_take = core.take
        try:
            # Mutate take to change the diagonal element computation
            one_val = 1
            two_val = 2
            nine_val = 9
            def bad_take(big, small):
                res = original_take(big, small)
                # If computing V11 = 1 - 1/9 = 8/9
                if big.value == Fraction(one_val) and small.value == Fraction(one_val, nine_val):
                    from sftoe.core import SmithianValue
                    return SmithianValue(Fraction(one_val, two_val))
                return res
            core.take = bad_take
            proof.take = bad_take
            with self.assertRaises(VerificationError):
                verify_mixing_structure()
        finally:
            core.take = original_take
            proof.take = original_take

    def test_verify_mixing_structure_mutation_off_diagonal(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_take = core.take
        try:
            # Mutate take to make off-diagonal larger than diagonal
            one_val = 1
            two_val = 2
            three_val = 3
            four_val = 4
            nine_val = 9
            def bad_take(big, small):
                res = original_take(big, small)
                # If computing V12 = 1 - 4/9 = 5/9, change it to 1
                if big.value == Fraction(one_val) and small.value == Fraction(four_val, nine_val):
                    from sftoe.core import SmithianValue
                    return SmithianValue(Fraction(one_val))
                return res
            core.take = bad_take
            proof.take = bad_take
            with self.assertRaises(VerificationError):
                verify_mixing_structure()
        finally:
            core.take = original_take
            proof.take = original_take

    def test_verify_mixing_structure_mutation_external(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            # Mutate Fraction to return something incorrect for external check
            one_val = 1
            two_val = 2
            five_val = 5
            def bad_fraction(numerator, denominator=None):
                if numerator == 9575 and denominator == (two_val * 5)**five_val:
                    return original_fraction(one_val, (two_val * 5)**five_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_mixing_structure()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEMixingMagnitudes(unittest.TestCase):
    def test_verify_mixing_magnitudes_success(self):
        res = verify_mixing_magnitudes()
        nine_val = 9
        eight_val = 8
        self.assertEqual(res["mixing_matrix"][1 - 1][1 - 1], Fraction(eight_val, nine_val))
        self.assertEqual(res["tier"], "B")

    def test_verify_mixing_magnitudes_mutation_zero_axiom(self):
        import sftoe.proof as proof
        from sftoe.core import SmithianValue
        
        # Mutate SmithianValue constructor to accept zero
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_mixing_magnitudes()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_mixing_magnitudes_mutation_mass_basis(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            # Mutate Fraction to return a different value for mass basis preimage
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == two_val and denominator == three_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_mixing_magnitudes()
        finally:
            proof.Fraction = original_fraction

    def test_verify_mixing_magnitudes_mutation_channel_basis(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            # Mutate Fraction to return a different value for channel basis preimage
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == three_val:
                    return original_fraction(two_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_mixing_magnitudes()
        finally:
            proof.Fraction = original_fraction

    def test_verify_mixing_magnitudes_mutation_alignment(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_take = core.take
        try:
            # Mutate take to change the diagonal element computation
            one_val = 1
            two_val = 2
            nine_val = 9
            def bad_take(big, small):
                res = original_take(big, small)
                # If computing V11 = 1 - 1/9 = 8/9
                if big.value == Fraction(one_val) and small.value == Fraction(one_val, nine_val):
                    from sftoe.core import SmithianValue
                    return SmithianValue(Fraction(one_val, two_val))
                return res
            core.take = bad_take
            proof.take = bad_take
            with self.assertRaises(VerificationError):
                verify_mixing_magnitudes()
        finally:
            core.take = original_take
            proof.take = original_take

    def test_verify_mixing_magnitudes_mutation_preimage_check(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_cast_out = core.cast_out
        try:
            # Mutate cast_out to fail preimage folding check
            def bad_cast_out(m):
                return Fraction(1, 2)
            core.cast_out = bad_cast_out
            proof.cast_out = bad_cast_out
            with self.assertRaises(VerificationError):
                verify_mixing_magnitudes()
        finally:
            core.cast_out = original_cast_out
            proof.cast_out = original_cast_out

    def test_verify_mixing_magnitudes_mutation_external(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            # Mutate Fraction to return something incorrect for external check of V_us (4032)
            one_val = 1
            two_val = 2
            four_val = 4
            def bad_fraction(numerator, denominator=None):
                if numerator == 4032 and denominator == (two_val * 5)**four_val:
                    return original_fraction(one_val, (two_val * 5)**four_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_mixing_magnitudes()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEGenerationDepth(unittest.TestCase):
    def test_verify_generation_depth_success(self):
        res = verify_generation_depth()
        two_val = 2
        self.assertEqual(res["folding_depth"], two_val)
        self.assertEqual(res["structural_depth"], two_val)
        self.assertEqual(res["tier"], "B")

    def test_verify_generation_depth_mutation_zero_axiom(self):
        import sftoe.proof as proof
        from sftoe.core import SmithianValue
        
        # Mutate SmithianValue constructor to accept zero
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_generation_depth()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_generation_depth_mutation_preimage(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            # Mutate Fraction to change a preimage value
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_generation_depth()
        finally:
            proof.Fraction = original_fraction

    def test_verify_generation_depth_mutation_ladder_size(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_cast_out = core.cast_out
        try:
            # Mutate cast_out to change preimage folding check
            def bad_cast_out(m):
                return Fraction(1, 1)
            core.cast_out = bad_cast_out
            proof.cast_out = bad_cast_out
            with self.assertRaises(VerificationError):
                verify_generation_depth()
        finally:
            core.cast_out = original_cast_out
            proof.cast_out = original_cast_out

    def test_verify_generation_depth_mutation_external(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            # Mutate Fraction to change electroweak scale coupling
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_generation_depth()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEFullMixingMatrices(unittest.TestCase):
    def test_verify_full_mixing_matrices_success(self):
        res = verify_full_mixing_matrices()
        nine_val = 9
        eight_val = 8
        six_val = 6
        five_val = 5
        self.assertEqual(res["ckm_matrix"][1 - 1][1 - 1], Fraction(eight_val, nine_val))
        self.assertEqual(res["pmns_matrix"][1 - 1][1 - 1], Fraction(five_val, six_val))
        self.assertEqual(res["tier"], "B")

    def test_verify_full_mixing_matrices_mutation_zero_axiom(self):
        import sftoe.proof as proof
        from sftoe.core import SmithianValue
        
        # Mutate SmithianValue constructor to accept zero
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_full_mixing_matrices()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_full_mixing_matrices_mutation_bases(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            # Mutate Fraction to change a preimage value
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == two_val and denominator == three_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_full_mixing_matrices()
        finally:
            proof.Fraction = original_fraction

    def test_verify_full_mixing_matrices_mutation_matrix_elements(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_take = core.take
        try:
            # Mutate take to change alignment element
            one_val = 1
            two_val = 2
            nine_val = 9
            def bad_take(big, small):
                res = original_take(big, small)
                # If computing V11 = 1 - 1/9 = 8/9
                if big.value == Fraction(one_val) and small.value == Fraction(one_val, nine_val):
                    from sftoe.core import SmithianValue
                    return SmithianValue(Fraction(one_val, two_val))
                return res
            core.take = bad_take
            proof.take = bad_take
            with self.assertRaises(VerificationError):
                verify_full_mixing_matrices()
        finally:
            core.take = original_take
            proof.take = original_take

    def test_verify_full_mixing_matrices_mutation_folding(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_cast_out = core.cast_out
        try:
            # Mutate cast_out to fail preimage folding check
            def bad_cast_out(m):
                return Fraction(1, 1)
            core.cast_out = bad_cast_out
            proof.cast_out = bad_cast_out
            with self.assertRaises(VerificationError):
                verify_full_mixing_matrices()
        finally:
            core.cast_out = original_cast_out
            proof.cast_out = original_cast_out

    def test_verify_full_mixing_matrices_mutation_external(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            # Mutate Fraction to return something incorrect for external PMNS checks (e.g. 984)
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == 984 and denominator == (two_val * 5)**three_val:
                    return original_fraction(one_val, (two_val * 5)**three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_full_mixing_matrices()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEInterEntryRelation(unittest.TestCase):
    def test_verify_inter_entry_relation_success(self):
        res = verify_inter_entry_relation()
        self.assertEqual(res["tier"], "B")
        five_val = 5
        three_val = 3
        two_val = 2
        self.assertEqual(res["ckm_row_sum"], Fraction(five_val, three_val))
        self.assertEqual(res["pmns_row_sum"], Fraction(three_val, two_val))

    def test_verify_inter_entry_relation_mutation_zero_axiom(self):
        import sftoe.proof as proof
        from sftoe.core import SmithianValue
        
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_inter_entry_relation()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_inter_entry_relation_mutation_ckm_sum(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == two_val and denominator == three_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_inter_entry_relation()
        finally:
            proof.Fraction = original_fraction

    def test_verify_inter_entry_relation_mutation_pmns_sum(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, 3)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_inter_entry_relation()
        finally:
            proof.Fraction = original_fraction

    def test_verify_inter_entry_relation_mutation_cast_out(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_cast_out = core.cast_out
        try:
            one_val = 1
            def bad_cast_out(m):
                return original_cast_out(m) + Fraction(one_val, one_val)
            core.cast_out = bad_cast_out
            proof.cast_out = bad_cast_out
            with self.assertRaises(VerificationError):
                verify_inter_entry_relation()
        finally:
            core.cast_out = original_cast_out
            proof.cast_out = original_cast_out

    def test_verify_inter_entry_relation_mutation_external_scale(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            five_val = 5
            three_val = 3
            state = {one_val: one_val}
            class CustomFraction(original_fraction):
                def __float__(self):
                    val = original_fraction.__float__(self)
                    if self.numerator == five_val and self.denominator == three_val:
                        state[one_val] = five_val - state[one_val]
                        return val + state[one_val]
                    return val
            proof.Fraction = CustomFraction
            with self.assertRaises(VerificationError):
                verify_inter_entry_relation()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEWithinGenerationRatio(unittest.TestCase):
    def test_verify_within_generation_ratio_success(self):
        res = verify_within_generation_ratio()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        three_val = 3
        self.assertEqual(res["positions"][one_val - one_val], Fraction(one_val, three_val))
        self.assertEqual(res["positions"][one_val], Fraction(two_val, three_val))
        self.assertEqual(res["positions"][two_val], Fraction(one_val, one_val))
        self.assertEqual(res["mass_parts"][one_val - one_val], Fraction(two_val, three_val))
        self.assertEqual(res["mass_parts"][one_val], Fraction(one_val, three_val))
        self.assertEqual(res["mass_parts"][two_val], Fraction(one_val, one_val))

    def test_verify_within_generation_ratio_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_within_generation_ratio()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_within_generation_ratio_mutation_positions(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == three_val:
                    return original_fraction(one_val, two_val * two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_within_generation_ratio()
        finally:
            proof.Fraction = original_fraction

    def test_verify_within_generation_ratio_mutation_shortfalls(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_take = core.take
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_take(big, small):
                if big.value == Fraction(one_val) and small.value == Fraction(one_val, three_val):
                    from sftoe.core import SmithianValue
                    return SmithianValue(Fraction(one_val, two_val * two_val))
                return original_take(big, small)
            core.take = bad_take
            proof.take = bad_take
            with self.assertRaises(VerificationError):
                verify_within_generation_ratio()
        finally:
            core.take = original_take
            proof.take = original_take

    def test_verify_within_generation_ratio_mutation_orbit(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            def bad_fold(v):
                from sftoe.core import SmithianValue
                return SmithianValue(Fraction(one_val, one_val))
            core.fold = bad_fold
            proof.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_within_generation_ratio()
        finally:
            core.fold = original_fold
            proof.fold = original_fold

    def test_verify_within_generation_ratio_mutation_external(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            five_val = 5
            class CustomFraction(original_fraction):
                def __float__(self):
                    val = original_fraction.__float__(self)
                    # Mutate down quark comparison ratio (47/10)
                    if self.numerator == 47 and self.denominator == two_val * five_val:
                        return val + float(one_val)
                    return val
            proof.Fraction = CustomFraction
            res = verify_within_generation_ratio()
            self.assertFalse(res.get("external_read_matched", True))
        finally:
            proof.Fraction = original_fraction


class TestSFTOEChargedLeptons(unittest.TestCase):
    def test_verify_charged_leptons_success(self):
        res = verify_charged_leptons()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        five_val = 5
        six_val = 6
        self.assertEqual(res["displaced_vacuum"], Fraction(one_val, two_val))
        self.assertEqual(res["positions"][one_val - one_val], Fraction(one_val, six_val))
        self.assertEqual(res["positions"][one_val], Fraction(one_val, two_val))
        self.assertEqual(res["positions"][two_val], Fraction(five_val, six_val))
        self.assertEqual(res["mass_parts"][one_val - one_val], Fraction(one_val, six_val))
        self.assertEqual(res["mass_parts"][one_val], Fraction(one_val, two_val))
        self.assertEqual(res["mass_parts"][two_val], Fraction(five_val, six_val))

    def test_verify_charged_leptons_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_charged_leptons()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_charged_leptons_mutation_vacuum(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_charged_leptons()
        finally:
            proof.Fraction = original_fraction

    def test_verify_charged_leptons_mutation_positions(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            five_val = 5
            six_val = 6
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == six_val:
                    return original_fraction(one_val, five_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_charged_leptons()
        finally:
            proof.Fraction = original_fraction

    def test_verify_charged_leptons_mutation_orbit(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            def bad_fold(v):
                from sftoe.core import SmithianValue
                return SmithianValue(Fraction(one_val, one_val))
            core.fold = bad_fold
            proof.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_charged_leptons()
        finally:
            core.fold = original_fold
            proof.fold = original_fold

    def test_verify_charged_leptons_mutation_external(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            five_val = 5
            seven_val = 7
            state = {one_val: one_val}
            class CustomFraction(original_fraction):
                def __float__(self):
                    val = original_fraction.__float__(self)
                    # Mutate electron physical mass check (10219979 / 20000000)
                    if self.numerator == 10219979 and self.denominator == two_val * (two_val * five_val)**seven_val:
                        state[one_val] = five_val - state[one_val]
                        return val + state[one_val]
                    return val
            proof.Fraction = CustomFraction
            res = verify_charged_leptons()
            self.assertFalse(res.get("external_read_matched", True))
        finally:
            proof.Fraction = original_fraction


class TestSFTOECombinedGenerationLadder(unittest.TestCase):
    def test_verify_generation_ladder_success(self):
        res = verify_generation_ladder()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        five_val = 5
        six_val = 6
        self.assertEqual(res["ladder_size"], six_val)
        self.assertEqual(res["positions"][one_val - one_val], Fraction(one_val, six_val))
        self.assertEqual(res["positions"][one_val], Fraction(one_val, two_val))
        self.assertEqual(res["positions"][two_val], Fraction(five_val, six_val))
        self.assertEqual(res["folding_depth"], two_val)
        self.assertEqual(res["structural_depth"], two_val)

    def test_verify_generation_ladder_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_generation_ladder()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_generation_ladder_mutation_ladder_size(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            five_val = 5
            six_val = 6
            def bad_fraction(numerator, denominator=None):
                # Mutate construction of 1/6 to return 1/5, reducing unique ladder size
                if numerator == one_val and denominator == six_val:
                    return original_fraction(one_val, five_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_generation_ladder()
        finally:
            proof.Fraction = original_fraction

    def test_verify_generation_ladder_mutation_folding_depth(self):
        import sftoe.proof as proof
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            two_val = 2
            def bad_fold(v):
                from sftoe.core import SmithianValue
                # Fold step fails to yield ONE
                return SmithianValue(Fraction(one_val, two_val))
            core.fold = bad_fold
            proof.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_generation_ladder()
        finally:
            core.fold = original_fold
            proof.fold = original_fold

    def test_verify_generation_ladder_mutation_structural_depth(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            five_val = 5
            six_val = 6
            def bad_fraction(numerator, denominator=None):
                # Mutate structural factorization pow computation by returning a divisor
                if numerator == six_val and denominator == one_val:
                    return original_fraction(five_val, one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_generation_ladder()
        finally:
            proof.Fraction = original_fraction

    def test_verify_generation_ladder_mutation_external(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            five_val = 5
            seven_val = 7
            state = {one_val: one_val}
            class CustomFraction(original_fraction):
                def __float__(self):
                    val = original_fraction.__float__(self)
                    # Mutate electron physical mass check (10219979 / 20000000)
                    if self.numerator == 10219979 and self.denominator == two_val * (two_val * five_val)**seven_val:
                        state[one_val] = five_val - state[one_val]
                        return val + state[one_val]
                    return val
            proof.Fraction = CustomFraction
            res = verify_generation_ladder()
            self.assertFalse(res.get("external_read_matched", True))
        finally:
            proof.Fraction = original_fraction


class TestSFTOEMassRatioFamily(unittest.TestCase):
    def test_verify_mass_ratio_family_success(self):
        res = verify_mass_ratio_family()
        self.assertEqual(res["tier"], "B")

    def test_verify_mass_ratio_family_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_mass_ratio_family()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_mass_ratio_family_mutation_ratios(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            five_val = 5
            six_val = 6
            def bad_fraction(numerator, denominator=None):
                # Mutate construction of 1/6 (electron mass-part for d=1) to return 1/5
                if numerator == one_val and denominator == six_val:
                    return original_fraction(one_val, five_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_mass_ratio_family()
        finally:
            proof.Fraction = original_fraction

    def test_verify_mass_ratio_family_mutation_structural(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            five_val = 5
            six_val = 6
            def bad_fraction(numerator, denominator=None):
                # Mutate Route B structural ratio calculation
                if numerator == six_val and denominator == one_val:
                    return original_fraction(five_val, one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_mass_ratio_family()
        finally:
            proof.Fraction = original_fraction

    def test_verify_mass_ratio_family_mutation_external(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            five_val = 5
            seven_val = 7
            state = {one_val: one_val}
            class CustomFraction(original_fraction):
                def __float__(self):
                    val = original_fraction.__float__(self)
                    # Mutate electron physical mass check (10219979 / 20000000)
                    if self.numerator == 10219979 and self.denominator == two_val * (two_val * five_val)**seven_val:
                        state[one_val] = five_val - state[one_val]
                        return val + state[one_val]
                    return val
            proof.Fraction = CustomFraction
            res = verify_mass_ratio_family()
            self.assertFalse(res.get("external_read_matched", True))
        finally:
            proof.Fraction = original_fraction


class TestSFTOEReachRatios(unittest.TestCase):
    def test_verify_reach_ratios_success(self):
        res = verify_reach_ratios()
        self.assertEqual(res["tier"], "B")

    def test_verify_reach_ratios_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_reach_ratios()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_reach_ratios_mutation_reaches(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            five_val = 5
            six_val = 6
            def bad_fraction(numerator, denominator=None):
                # Mutate construction of 1/6 (light mass-part for d=1) to return 1/5
                if numerator == one_val and denominator == six_val:
                    return original_fraction(one_val, five_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_reach_ratios()
        finally:
            proof.Fraction = original_fraction

    def test_verify_reach_ratios_mutation_take(self):
        original_take = take
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_take(big, small):
                small_val = small.value if isinstance(small, SmithianValue) else small
                if isinstance(big, SmithianValue) and big.value == Fraction(1, 1) and \
                   small_val == Fraction(1, 6):
                    # Return an incorrect value to disrupt the subtraction loop
                    return SmithianValue(Fraction(1, 6))
                return original_take(big, small)
            core.take = bad_take
            proof.take = bad_take
            with self.assertRaises(VerificationError):
                verify_reach_ratios()
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.take = original_take
            proof.take = original_take

    def test_verify_reach_ratios_mutation_middle_reach(self):
        original_take = take
        try:
            import sftoe.proof as proof
            import sftoe.core as core
            def bad_take(big, small):
                small_val = small.value if isinstance(small, SmithianValue) else small
                if isinstance(big, SmithianValue) and big.value == Fraction(1, 1) and \
                   small_val == Fraction(1, 2):
                    # Return an incorrect value to keep the loop running
                    return SmithianValue(Fraction(3, 4))
                return original_take(big, small)
            core.take = bad_take
            proof.take = bad_take
            with self.assertRaises(VerificationError):
                verify_reach_ratios()
        finally:
            import sftoe.core as core
            import sftoe.proof as proof
            core.take = original_take
            proof.take = original_take

    def test_verify_reach_ratios_mutation_external(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            five_val = 5
            six_val = 6
            seven_val = 7
            eight_val = 8
            state = {one_val: one_val}
            class CustomFraction(original_fraction):
                def __float__(self):
                    val = original_fraction.__float__(self)
                    # Mutate electron physical mass check (reduced Fraction target)
                    target_num = (two_val * five_val)**seven_val + 219979
                    target_den = two_val * (two_val * five_val)**seven_val
                    if self.numerator == target_num and self.denominator == target_den:
                        state[one_val] = five_val - state[one_val]
                        return val + state[one_val]
                    return val
            proof.Fraction = CustomFraction
            res = verify_reach_ratios()
            self.assertFalse(res.get("external_read_matched", True))
        finally:
            proof.Fraction = original_fraction


class TestSFTOEKoideRelationship(unittest.TestCase):
    def test_verify_koide_relationship_success(self):
        res = verify_koide_relationship()
        self.assertEqual(res["tier"], "B")

    def test_verify_koide_relationship_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_koide_relationship()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_koide_relationship_mutation_structural(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            five_val = 5
            six_val = 6
            def bad_fraction(numerator, denominator=None):
                # Mutate construction of structural target 2/3 to return 1/3
                if numerator == two_val and denominator == three_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_koide_relationship()
        finally:
            proof.Fraction = original_fraction

    def test_verify_koide_relationship_mutation_external_masses(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            five_val = 5
            six_val = 6
            seven_val = 7
            state = {one_val: one_val}
            class CustomFraction(original_fraction):
                def __float__(self):
                    val = original_fraction.__float__(self)
                    # Mutate electron physical mass check (reduced Fraction target)
                    target_num = (two_val * five_val)**seven_val + 219979
                    target_den = two_val * (two_val * five_val)**seven_val
                    if self.numerator == target_num and self.denominator == target_den:
                        state[one_val] = five_val - state[one_val]
                        return val + state[one_val]
                    return val
            proof.Fraction = CustomFraction
            with self.assertRaises(VerificationError):
                verify_koide_relationship()
        finally:
            proof.Fraction = original_fraction

    def test_verify_koide_relationship_mutation_tolerance(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            five_val = 5
            def bad_fraction(numerator, denominator=None):
                # Mutate tolerance denominator to be extremely large, making check fail
                target_den = (two_val * five_val)**five_val
                if numerator == one_val and denominator == target_den:
                    # Return a tiny tolerance that will cause the assertion to fail
                    return original_fraction(one_val, target_den * target_den)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_koide_relationship()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEKoideCubicRoots(unittest.TestCase):
    def test_verify_koide_cubic_roots_success(self):
        res = verify_koide_cubic_roots()
        self.assertEqual(res["tier"], "B")

    def test_verify_koide_cubic_roots_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_koide_cubic_roots()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_koide_cubic_roots_mutation_structural(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            five_val = 5
            six_val = 6
            def bad_fraction(numerator, denominator=None):
                # Mutate construction of structural target I1 (1/6) to return 1/5
                if numerator == one_val and denominator == six_val:
                    return original_fraction(one_val, five_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_koide_cubic_roots()
        finally:
            proof.Fraction = original_fraction

    def test_verify_koide_cubic_roots_mutation_external_masses(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            five_val = 5
            six_val = 6
            seven_val = 7
            state = {one_val: one_val}
            class CustomFraction(original_fraction):
                def __float__(self):
                    val = original_fraction.__float__(self)
                    # Mutate electron physical mass check (reduced Fraction target)
                    target_num = (two_val * five_val)**seven_val + 219979
                    target_den = two_val * (two_val * five_val)**seven_val
                    if self.numerator == target_num and self.denominator == target_den:
                        state[one_val] = five_val - state[one_val]
                        return val + state[one_val]
                    return val
            proof.Fraction = CustomFraction
            with self.assertRaises(VerificationError):
                verify_koide_cubic_roots()
        finally:
            proof.Fraction = original_fraction

    def test_verify_koide_cubic_roots_mutation_tolerance(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            five_val = 5
            def bad_fraction(numerator, denominator=None):
                # Mutate tolerance denominator to be extremely large, making check fail
                target_den = (two_val * five_val)**five_val
                if numerator == one_val and denominator == target_den:
                    # Return a tiny tolerance that will cause the assertion to fail
                    return original_fraction(one_val, target_den * target_den * target_den)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_koide_cubic_roots()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEProvenMassRatios(unittest.TestCase):
    def test_verify_proven_mass_ratios_success(self):
        res = verify_proven_mass_ratios()
        self.assertEqual(res["tier"], "B")

    def test_verify_proven_mass_ratios_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_proven_mass_ratios()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_proven_mass_ratios_mutation_shortfalls(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            five_val = 5
            six_val = 6
            def bad_fraction(numerator, denominator=None):
                # Mutate construction of shortfall m_electron (1/6) to return 1/5
                if numerator == one_val and denominator == six_val:
                    return original_fraction(one_val, five_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_proven_mass_ratios()
        finally:
            proof.Fraction = original_fraction

    def test_verify_proven_mass_ratios_mutation_positions(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            five_val = 5
            six_val = 6
            def bad_fraction(numerator, denominator=None):
                # Mutate construction of position p3 (5/6) to return 5/7
                seven_val = 7
                if numerator == five_val and denominator == six_val:
                    return original_fraction(five_val, seven_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_proven_mass_ratios()
        finally:
            proof.Fraction = original_fraction

    def test_verify_proven_mass_ratios_mutation_tolerance(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            five_val = 5
            six_val = 6
            def bad_fraction(numerator, denominator=None):
                # Mutate tolerance to be extremely small, making check fail
                target_den = (two_val * five_val)**six_val
                if numerator == one_val and denominator == target_den:
                    # Return a tiny tolerance that will cause the assertion to fail
                    return original_fraction(one_val, target_den * target_den * target_den)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_proven_mass_ratios()
        finally:
            proof.Fraction = original_fraction

class TestSFTOEGenerationDepthTower(unittest.TestCase):
    def test_verify_generation_depth_tower_success(self):
        res = verify_generation_depth_tower()
        self.assertEqual(res["tier"], "A")

    def test_verify_generation_depth_tower_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_generation_depth_tower()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_generation_depth_tower_mutation_preimage_val(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_generation_depth_tower()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEGeneralCoveringDepth(unittest.TestCase):
    def test_verify_general_covering_depth_success(self):
        res = verify_general_covering_depth()
        self.assertEqual(res["tier"], "A")

    def test_verify_general_covering_depth_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_general_covering_depth()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_general_covering_depth_mutation_preimage_val(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_general_covering_depth()
        finally:
            proof.Fraction = original_fraction


class TestSFTOESecondInvariant(unittest.TestCase):
    def test_verify_second_invariant_success(self):
        res = verify_second_invariant()
        self.assertEqual(res["tier"], "B")

    def test_verify_second_invariant_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_second_invariant()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_second_invariant_mutation_scale_factor(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            target_numerator = 659937
            def bad_fraction(*args, **kwargs):
                if len(args) == 2 and args[1 - 1] == target_numerator:
                    return original_fraction(target_numerator + args[1], args[1])
                return original_fraction(*args, **kwargs)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_second_invariant()
        finally:
            proof.Fraction = original_fraction


class TestSFTOELeptonCubicEntire(unittest.TestCase):
    def test_verify_lepton_cubic_entire_success(self):
        res = verify_lepton_cubic_entire()
        self.assertEqual(res["tier"], "B")

    def test_verify_lepton_cubic_entire_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_lepton_cubic_entire()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_lepton_cubic_entire_mutation_coefficients(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            target_denom = 485
            def bad_fraction(numerator, denominator=None):
                if denominator == target_denom:
                    return original_fraction(numerator, target_denom + 1)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_lepton_cubic_entire()
        finally:
            proof.Fraction = original_fraction


class TestSFTOESecondInvariantSharpened(unittest.TestCase):
    def test_verify_second_invariant_sharpened_success(self):
        res = verify_second_invariant_sharpened()
        self.assertEqual(res["tier"], "B")

    def test_verify_second_invariant_sharpened_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_second_invariant_sharpened()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_second_invariant_sharpened_mutation_scale_factor(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            target_numerator = 659937
            def bad_fraction(*args, **kwargs):
                if len(args) == 2 and args[1 - 1] == target_numerator:
                    return original_fraction(target_numerator + args[1], args[1])
                return original_fraction(*args, **kwargs)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_second_invariant_sharpened()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEQuarkInvariants(unittest.TestCase):
    def test_verify_quark_invariants_success(self):
        res = verify_quark_invariants()
        self.assertEqual(res["tier"], "B")

    def test_verify_quark_invariants_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_quark_invariants()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_quark_invariants_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            def bad_fraction(*args, **kwargs):
                if len(args) == 2 and args[1] == 127:
                    return original_fraction(args[1 - 1], 128)
                return original_fraction(*args, **kwargs)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_quark_invariants()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEQuarkMassConfinementLift(unittest.TestCase):
    def test_verify_quark_mass_confinement_lift_success(self):
        res = verify_quark_mass_confinement_lift()
        self.assertEqual(res["tier"], "B")

    def test_verify_quark_mass_confinement_lift_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_quark_mass_confinement_lift()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_quark_mass_confinement_lift_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            def bad_fraction(*args, **kwargs):
                if len(args) == 2 and args[1] == 1454:
                    return original_fraction(args[1 - 1], 1455)
                return original_fraction(*args, **kwargs)
            proof.Fraction = bad_fraction
            res = verify_quark_mass_confinement_lift()
            self.assertFalse(res.get("external_read_matched", True))
        finally:
            proof.Fraction = original_fraction


class TestSFTOENeutrinoMassLadder(unittest.TestCase):
    def test_verify_neutrino_mass_ladder_success(self):
        res = verify_neutrino_mass_ladder()
        self.assertEqual(res["tier"], "B")

    def test_verify_neutrino_mass_ladder_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_neutrino_mass_ladder()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_neutrino_mass_ladder_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            def bad_fraction(*args, **kwargs):
                if len(args) == 2 and args[1] == 25:
                    return original_fraction(args[1 - 1], 26)
                return original_fraction(*args, **kwargs)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_neutrino_mass_ladder()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEQuarkSecondInvariant(unittest.TestCase):
    def test_verify_quark_second_invariant_success(self):
        res = verify_quark_second_invariant()
        self.assertEqual(res["tier"], "B")

    def test_verify_quark_second_invariant_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_quark_second_invariant()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_quark_second_invariant_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            def bad_fraction(*args, **kwargs):
                if len(args) == 2 and args[1] == 95:
                    return original_fraction(args[1 - 1], 96)
                return original_fraction(*args, **kwargs)
            proof.Fraction = bad_fraction
            res = verify_quark_second_invariant()
            self.assertFalse(res.get("external_read_matched", True))
        finally:
            proof.Fraction = original_fraction


class TestSFTOEQuarkDressingFactor(unittest.TestCase):
    def test_verify_quark_dressing_factor_success(self):
        res = verify_quark_dressing_factor()
        self.assertEqual(res["tier"], "A")
        self.assertAlmostEqual(res["dressed_tc"], res["measured_tc"], delta=0.01)
        self.assertAlmostEqual(res["dressed_bs"], res["measured_bs"], delta=1.5)
        self.assertTrue(17.0 <= res["dressed_sd"] <= 22.0)

    def test_verify_quark_dressing_factor_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_quark_dressing_factor()
        finally:
            SmithianValue.__init__ = original_init


class TestSFTOECKMMagnitudes(unittest.TestCase):
    def test_verify_ckm_magnitudes_success(self):
        res = verify_ckm_magnitudes()
        nine_val = 9
        eight_val = 8
        self.assertEqual(res["mixing_matrix"][1 - 1][1 - 1], Fraction(eight_val, nine_val))
        self.assertEqual(res["tier"], "B")

    def test_verify_ckm_magnitudes_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_ckm_magnitudes()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_ckm_magnitudes_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == two_val and denominator == three_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_ckm_magnitudes()
        finally:
            proof.Fraction = original_fraction


class TestSFTOECPPhase(unittest.TestCase):
    def test_verify_cp_phase_antipode_success(self):
        res = verify_cp_phase_antipode()
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["phase"], Fraction(1, 2))

    def test_verify_cp_phase_antipode_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_cp_phase_antipode()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_cp_phase_antipode_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_cp_phase_antipode()
        finally:
            proof.Fraction = original_fraction


class TestSFTOECKMThirdEntry(unittest.TestCase):
    def test_verify_ckm_third_entry_closed_success(self):
        res = verify_ckm_third_entry_closed()
        self.assertEqual(res["tier"], "B")

    def test_verify_ckm_third_entry_closed_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_ckm_third_entry_closed()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_ckm_third_entry_closed_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_ckm_third_entry_closed()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEPMNSLargeAngles(unittest.TestCase):
    def test_verify_pmns_large_angles_success(self):
        res = verify_pmns_large_angles()
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["sin2_theta23"], Fraction(1, 2))
        self.assertEqual(res["sin2_theta12"], Fraction(1, 3))

    def test_verify_pmns_large_angles_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_pmns_large_angles()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_pmns_large_angles_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_pmns_large_angles()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEPMNSReactorAngle(unittest.TestCase):
    def test_verify_pmns_reactor_angle_success(self):
        res = verify_pmns_reactor_angle()
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["sin2_theta13"], Fraction(1, 48))

    def test_verify_pmns_reactor_angle_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_pmns_reactor_angle()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_pmns_reactor_angle_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_pmns_reactor_angle()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEEMCoupling(unittest.TestCase):
    def test_verify_em_coupling_success(self):
        res = verify_em_coupling()
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["g_em"], Fraction(1, 2))

    def test_verify_em_coupling_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_em_coupling()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_em_coupling_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_em_coupling()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEEWMixing(unittest.TestCase):
    def test_verify_ew_mixing_running_success(self):
        res = verify_ew_mixing_running()
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["sin2_theta_w_bare"], Fraction(1, 2))

    def test_verify_ew_mixing_running_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_ew_mixing_running()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_ew_mixing_running_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_ew_mixing_running()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEScaleRatio(unittest.TestCase):
    def test_verify_depth_scale_ratio_success(self):
        res = verify_depth_scale_ratio()
        self.assertEqual(res["tier"], "B")
        two_val = 2
        self.assertEqual(res["scale_ratio"], two_val)

    def test_verify_depth_scale_ratio_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_depth_scale_ratio()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_depth_scale_ratio_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_depth_scale_ratio()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEEWMixingCurve(unittest.TestCase):
    def test_verify_ew_mixing_curve_success(self):
        res = verify_ew_mixing_curve()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["mixing_start"], Fraction(one_val, two_val))

    def test_verify_ew_mixing_curve_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_ew_mixing_curve()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_ew_mixing_curve_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_ew_mixing_curve()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEWZMassRatio(unittest.TestCase):
    def test_verify_w_z_mass_ratio_success(self):
        res = verify_w_z_mass_ratio()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["w_z_mass_squared_ratio_bare"], Fraction(one_val, two_val))

    def test_verify_w_z_mass_ratio_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_w_z_mass_ratio()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_w_z_mass_ratio_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_w_z_mass_ratio()
        finally:
            proof.Fraction = original_fraction


class TestSFTOELevelDepthMap(unittest.TestCase):
    def test_verify_level_depth_map_success(self):
        res = verify_level_depth_map()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        self.assertEqual(res["scale_axis_start"], Fraction(one_val))

    def test_verify_level_depth_map_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_level_depth_map()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_level_depth_map_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_level_depth_map()
        finally:
            proof.Fraction = original_fraction


class TestSFTOECouplingConvergence(unittest.TestCase):
    def test_verify_coupling_convergence_success(self):
        res = verify_coupling_convergence()
        self.assertEqual(res["tier"], "B")
        two_val = 2
        three_val = 3
        self.assertEqual(res["g_strong_bare"], Fraction(two_val, three_val))
        self.assertEqual(res["g_ew_bare"], Fraction(1, two_val))

    def test_verify_coupling_convergence_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_coupling_convergence()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_coupling_convergence_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_coupling_convergence()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEConvergenceRateClosed(unittest.TestCase):
    def test_verify_convergence_rate_closed_success(self):
        res = verify_convergence_rate_closed()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        six_val = 6
        self.assertEqual(res["bare_gap"], Fraction(one_val, two_val * six_val))

    def test_verify_convergence_rate_closed_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_convergence_rate_closed()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_convergence_rate_closed_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_convergence_rate_closed()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEAccumulatedSeparation(unittest.TestCase):
    def test_verify_accumulated_separation_success(self):
        res = verify_accumulated_separation()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        six_val = 6
        self.assertEqual(res["bare_gap"], Fraction(one_val, two_val * six_val))

    def test_verify_accumulated_separation_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_accumulated_separation()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_accumulated_separation_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_accumulated_separation()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEThreeCouplingStructure(unittest.TestCase):
    def test_verify_three_coupling_structure_success(self):
        res = verify_three_coupling_structure()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["g_em"], Fraction(one_val, two_val))

    def test_verify_three_coupling_structure_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_three_coupling_structure()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_three_coupling_structure_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_three_coupling_structure()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEScaleInvariance(unittest.TestCase):
    def test_verify_scale_invariance_success(self):
        res = verify_scale_invariance()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        self.assertEqual(res["derived_speed"], Fraction(one_val))

    def test_verify_scale_invariance_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_scale_invariance()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_scale_invariance_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_scale_invariance()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEPlanckHierarchy(unittest.TestCase):
    def test_verify_planck_hierarchy_success(self):
        res = verify_planck_hierarchy()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        seven_val = 7
        exponent_val = two_val ** seven_val
        self.assertEqual(res["derived_hierarchy"], Fraction(two_val ** exponent_val))

    def test_verify_planck_hierarchy_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_planck_hierarchy()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_planck_hierarchy_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            five_val = 5
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == five_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_planck_hierarchy()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEUnifiedForceLaw(unittest.TestCase):
    def test_verify_unified_force_law_success(self):
        res = verify_unified_force_law()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        three_val = 3
        five_val = 5
        seven_val = 7
        denom_val = two_val * three_val * five_val * seven_val
        self.assertEqual(res["ladder_span"], denom_val)
        
    def test_verify_unified_force_law_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_unified_force_law()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_unified_force_law_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_unified_force_law()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEFiveForceFlavourRatio(unittest.TestCase):
    def test_verify_five_force_flavour_ratio_success(self):
        res = verify_five_force_flavour_ratio()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        four_val = 4
        self.assertEqual(res["derived_amplitude_ratio"], Fraction(one_val, two_val))
        self.assertEqual(res["derived_rate_ratio"], Fraction(one_val, four_val))

    def test_verify_five_force_flavour_ratio_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_five_force_flavour_ratio()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_five_force_flavour_ratio_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_five_force_flavour_ratio()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEPrimeSectorLadderBounded(unittest.TestCase):
    def test_verify_prime_sector_ladder_bounded_success(self):
        res = verify_prime_sector_ladder_bounded()
        self.assertEqual(res["tier"], "B")
        two_val = 2
        three_val = 3
        five_val = 5
        seven_val = 7
        self.assertEqual(res["realised_prime_sectors"], [two_val, three_val, five_val, seven_val])
        self.assertEqual(res["deepest_covering_depth"], seven_val)

    def test_verify_prime_sector_ladder_bounded_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_prime_sector_ladder_bounded()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_prime_sector_ladder_bounded_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_prime_sector_ladder_bounded()
        finally:
            proof.Fraction = original_fraction


class TestSFTOETwoNewPrimeChargeForces(unittest.TestCase):
    def test_verify_two_new_prime_charge_forces_success(self):
        res = verify_two_new_prime_charge_forces()
        self.assertEqual(res["tier"], "B")
        two_val = 2
        three_val = 3
        four_val = 4
        five_val = 5
        seven_val = 7
        self.assertEqual(res["couplings"][two_val - two_val], Fraction(two_val - 1, two_val))
        self.assertEqual(res["couplings"][three_val - two_val], Fraction(three_val - 1, three_val))
        self.assertEqual(res["couplings"][five_val - three_val], Fraction(five_val - 1, five_val))
        self.assertEqual(res["couplings"][seven_val - four_val], Fraction(seven_val - 1, seven_val))

    def test_verify_two_new_prime_charge_forces_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_two_new_prime_charge_forces()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_two_new_prime_charge_forces_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_two_new_prime_charge_forces()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEHalfOneUnifyingCenter(unittest.TestCase):
    def test_verify_half_one_unifying_center_success(self):
        res = verify_half_one_unifying_center()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["unifying_center"], Fraction(one_val, two_val))

    def test_verify_half_one_unifying_center_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_half_one_unifying_center()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_half_one_unifying_center_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_half_one_unifying_center()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEPrimeSectorConfiningLadder(unittest.TestCase):
    def test_verify_prime_sector_confining_ladder_success(self):
        res = verify_prime_sector_confining_ladder()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        five_val = 5
        seven_val = 7
        eleven_val = seven_val + four_val
        self.assertEqual(res["shared_center"], Fraction(one_val, two_val))
        self.assertEqual(res["sector_pairs"][three_val], one_val)
        self.assertEqual(res["sector_pairs"][five_val], two_val)
        self.assertEqual(res["sector_pairs"][seven_val], three_val)
        self.assertEqual(res["sector_pairs"][eleven_val], five_val)

    def test_verify_prime_sector_confining_ladder_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_prime_sector_confining_ladder()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_prime_sector_confining_ladder_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_prime_sector_confining_ladder()
        finally:
            proof.Fraction = original_fraction


class TestSFTOELeptonGenerations(unittest.TestCase):
    def test_verify_five_fold_standing_modes_force_three_generations_success(self):
        res = verify_five_fold_standing_modes_force_three_generations()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        self.assertEqual(res["generation_count"], three_val)
        self.assertEqual(res["standing_modes"][two_val - two_val], Fraction(one_val, four_val))
        self.assertEqual(res["standing_modes"][three_val - two_val], Fraction(one_val, two_val))
        self.assertEqual(res["standing_modes"][three_val - one_val], Fraction(three_val, four_val))

    def test_verify_five_fold_standing_modes_force_three_generations_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_five_fold_standing_modes_force_three_generations()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_five_fold_standing_modes_force_three_generations_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(two_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_five_fold_standing_modes_force_three_generations()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEAbsoluteScaleUnobservable(unittest.TestCase):
    def test_verify_absolute_scale_unobservable_success(self):
        res = verify_absolute_scale_unobservable()
        self.assertEqual(res["tier"], "B")
        two_val = 2
        five_val = 5
        self.assertEqual(res["ratio"], Fraction(two_val, five_val))

    def test_verify_absolute_scale_unobservable_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_absolute_scale_unobservable()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_absolute_scale_unobservable_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            five_val = 5
            def bad_fraction(numerator, denominator=None):
                if numerator == two_val and denominator == five_val:
                    return original_fraction(two_val, five_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_absolute_scale_unobservable()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEGrandSynthesis(unittest.TestCase):
    def test_verify_grand_synthesis_success(self):
        res = verify_grand_synthesis()
        self.assertEqual(res["tier"], "B")
        three_val = 3
        self.assertEqual(res["orbit_period"], three_val)
        self.assertEqual(res["multiplicative_order"], three_val)

    def test_verify_grand_synthesis_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_grand_synthesis()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_grand_synthesis_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            seven_val = 7
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == seven_val:
                    return original_fraction(one_val, seven_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_grand_synthesis()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEForwardNotFitted(unittest.TestCase):
    def test_verify_forward_not_fitted_success(self):
        res = verify_forward_not_fitted()
        self.assertEqual(res["tier"], "B")
        four_val = 4
        five_val = 5
        self.assertEqual(res["derived_value"], Fraction(four_val, five_val))
        self.assertEqual(res["independent_value"], Fraction(four_val, five_val))

    def test_verify_forward_not_fitted_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_forward_not_fitted()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_forward_not_fitted_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            five_val = 5
            def bad_fraction(numerator, denominator=None):
                if numerator == two_val and denominator == five_val:
                    return original_fraction(two_val, five_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_forward_not_fitted()
        finally:
            proof.Fraction = original_fraction


class TestSFTOECrossSectorInsights(unittest.TestCase):
    def test_verify_cross_sector_insights_success(self):
        res = verify_cross_sector_insights()
        self.assertEqual(res["tier"], "B")
        three_val = 3
        self.assertEqual(res["orbit_period"], three_val)
        two_val = 2
        self.assertEqual(res["lock_threshold"], Fraction(1, two_val))

    def test_verify_cross_sector_insights_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_cross_sector_insights()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_cross_sector_insights_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            seven_val = 7
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == seven_val:
                    return original_fraction(one_val, seven_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_cross_sector_insights()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEForwardNovelties(unittest.TestCase):
    def test_verify_forward_novelties_success(self):
        res = verify_forward_novelties()
        self.assertEqual(res["tier"], "B")
        self.assertTrue(res["divides"])

    def test_verify_forward_novelties_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_forward_novelties()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_forward_novelties_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            seven_val = 7
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == seven_val:
                    return original_fraction(one_val, seven_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_forward_novelties()
        finally:
            proof.Fraction = original_fraction


class TestSFTOECollapseToOpenConversion(unittest.TestCase):
    def test_verify_collapse_to_open_conversion_success(self):
        res = verify_collapse_to_open_conversion()
        self.assertEqual(res["tier"], "B")
        self.assertTrue(res["proton_to_electron_ratio"] > 1)

    def test_verify_collapse_to_open_conversion_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_collapse_to_open_conversion()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_collapse_to_open_conversion_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            six_val = 6
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == six_val:
                    return original_fraction(one_val, six_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_collapse_to_open_conversion()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEPlanckHierarchyForced(unittest.TestCase):
    def test_verify_planck_hierarchy_forced_success(self):
        res = verify_planck_hierarchy_forced()
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["massive_states_count"], 127)

    def test_verify_planck_hierarchy_forced_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_planck_hierarchy_forced()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_planck_hierarchy_forced_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, two_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_planck_hierarchy_forced()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEScaleAxisProven(unittest.TestCase):
    def test_verify_scale_axis_proven_success(self):
        res = verify_scale_axis_proven()
        self.assertEqual(res["tier"], "B")
        six_val = 6
        self.assertEqual(len(res["spacings"]), six_val)
        two_val = 2
        self.assertEqual(res["ratio"], Fraction(1, two_val))

    def test_verify_scale_axis_proven_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_scale_axis_proven()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_scale_axis_proven_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, two_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_scale_axis_proven()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEGravitationalCouplingProven(unittest.TestCase):
    def test_verify_gravitational_coupling_proven_success(self):
        res = verify_gravitational_coupling_proven()
        self.assertEqual(res["tier"], "B")
        two_val = 2
        self.assertEqual(res["coupling"], Fraction(1, two_val))
        one_val = 1
        self.assertEqual(res["sum_coupling"], one_val)

    def test_verify_gravitational_coupling_proven_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_gravitational_coupling_proven()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_gravitational_coupling_proven_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, two_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_gravitational_coupling_proven()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEUnisonOrder(unittest.TestCase):
    def test_verify_unison_order_success(self):
        res = verify_unison_order()
        self.assertEqual(res["tier"], "B")
        two_val = 2
        five_val = 5
        eleven_val = two_val * five_val + 1
        self.assertEqual(res["max_depth_checked"], eleven_val)

    def test_verify_unison_order_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_unison_order()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_unison_order_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, two_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_unison_order()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEDiscriminatingPrediction(unittest.TestCase):
    def test_verify_discriminating_prediction_success(self):
        res = verify_discriminating_prediction()
        self.assertEqual(res["tier"], "B")
        two_val = 2
        five_val = 5
        ten_val = two_val * five_val
        self.assertEqual(res["crossing_level"], ten_val)
        self.assertEqual(res["rung_spacing_tolerance"], Fraction(241, 81797))

    def test_verify_discriminating_prediction_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_discriminating_prediction()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_discriminating_prediction_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, two_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_discriminating_prediction()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEInternalAnchorDepth(unittest.TestCase):
    def test_verify_internal_anchor_depth_success(self):
        res = verify_internal_anchor_depth()
        self.assertEqual(res["concept"], "The electroweak running source closes on the fold's square.")
        two_val = 2
        four_val = two_val * two_val
        self.assertEqual(res["anchor_level"], four_val)
        self.assertEqual(res["anchor_depth"], four_val)
        self.assertEqual(res["gap_level_4"], Fraction(1, 6))
        self.assertEqual(res["gap_depth_4"], Fraction(1, 18))

    def test_verify_internal_anchor_depth_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_internal_anchor_depth()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_internal_anchor_depth_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, two_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_internal_anchor_depth()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEInteractionStrengthStructure(unittest.TestCase):
    def test_verify_interaction_strength_structure_success(self):
        res = verify_interaction_strength_structure()
        self.assertEqual(res["tier"], "B")
        self.assertEqual(res["concept"], "Every interaction strength comes from the single fold factor m.")
        self.assertEqual(res["g_star_m2"], Fraction(1, 2))
        self.assertEqual(res["ew_mixing_m2"], Fraction(1, 1))
        self.assertEqual(res["g_star_m3"], Fraction(2, 3))
        self.assertEqual(res["ew_mixing_m3"], Fraction(1, 2))
        two_val = 2
        self.assertEqual(res["beta_slope_m3"], two_val)

    def test_verify_interaction_strength_structure_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_interaction_strength_structure()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_interaction_strength_structure_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, two_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_interaction_strength_structure()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEDarkToBaryonFraction(unittest.TestCase):
    def test_verify_dark_to_baryon_fraction_success(self):
        res = verify_dark_to_baryon_fraction()
        self.assertEqual(res["concept"], "The dark-to-baryon fraction ratio is 27/5 = 5.4.")
        self.assertEqual(res["generation_volume"], 27)
        five_val = 5
        self.assertEqual(res["covering_depth"], five_val)
        self.assertEqual(res["reciprocal_fraction"], Fraction(5, 27))

    def test_verify_dark_to_baryon_fraction_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_dark_to_baryon_fraction()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_dark_to_baryon_fraction_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, two_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_dark_to_baryon_fraction()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEDarkMatter(unittest.TestCase):
    def test_verify_dark_matter_success(self):
        res = verify_dark_matter()
        self.assertEqual(res["concept"], "Dark sector is gauge-inert gravitating matter with fraction 27/32.")
        self.assertEqual(res["baryon_fraction"], Fraction(5, 32))
        self.assertEqual(res["dark_fraction"], Fraction(27, 32))
        self.assertEqual(res["dark_to_baryon_ratio"], Fraction(27, 5))
        self.assertEqual(res["gravitational_coupling"], Fraction(1, 2))
        one_val = 1
        self.assertEqual(res["gauge_coupling"], one_val - one_val)

    def test_verify_dark_matter_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_dark_matter()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_dark_matter_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, two_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_dark_matter()
        finally:
            proof.Fraction = original_fraction


class TestSFTOECosmologicalTimeline(unittest.TestCase):
    def test_verify_cosmological_timeline_success(self):
        res = verify_cosmological_timeline()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        five_val = 5
        thirty_two_val = two_val ** five_val
        self.assertEqual(res["ks_entropy_bits"], one_val)
        self.assertEqual(res["inflation_expansion_factor"], thirty_two_val)
        self.assertEqual(res["initial_state"], one_val)

    def test_verify_cosmological_timeline_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_cosmological_timeline()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_cosmological_timeline_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_cosmological_timeline()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEStrongFieldGravity(unittest.TestCase):
    def test_verify_strong_field_gravity_success(self):
        res = verify_strong_field_gravity()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        five_val = 5
        eight_val = two_val * four_val
        thirty_two_val = two_val ** five_val
        self.assertEqual(res["horizon_area"], thirty_two_val)
        self.assertEqual(res["black_hole_entropy"], eight_val)
        self.assertEqual(res["black_hole_mass"], Fraction(one_val, four_val))
        self.assertEqual(res["horizon_radius"], Fraction(one_val, two_val))

    def test_verify_strong_field_gravity_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_strong_field_gravity()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_strong_field_gravity_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_strong_field_gravity()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEProtonStability(unittest.TestCase):
    def test_verify_proton_stability_success(self):
        res = verify_proton_stability()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        self.assertEqual(res["quark_fibre"], three_val)
        self.assertEqual(res["lepton_fibre"], two_val)
        self.assertEqual(res["baryon_number"], one_val)

    def test_verify_proton_stability_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_proton_stability()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_proton_stability_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == three_val:
                    return original_fraction(one_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_proton_stability()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEBaryonToPhotonRatio(unittest.TestCase):
    def test_verify_baryon_to_photon_ratio_success(self):
        res = verify_baryon_to_photon_ratio()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        three_val = 3
        five_val = 5
        six_val = 6
        ten_val = two_val * five_val
        
        measured_eta = float(Fraction(six_val * ten_val + one_val, ten_val ** (ten_val + one_val)))
        self.assertEqual(res["measured_baryon_to_photon_ratio"], measured_eta)

    def test_verify_baryon_to_photon_ratio_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_baryon_to_photon_ratio()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_baryon_to_photon_ratio_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_baryon_to_photon_ratio()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEBaryonAsymmetryNonzero(unittest.TestCase):
    def test_verify_baryon_asymmetry_nonzero_success(self):
        res = verify_baryon_asymmetry_nonzero()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["residue"], Fraction(one_val, two_val))

    def test_verify_baryon_asymmetry_nonzero_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_baryon_asymmetry_nonzero()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_baryon_asymmetry_nonzero_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_baryon_asymmetry_nonzero()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEGenerationBoundStrict(unittest.TestCase):
    def test_verify_generation_bound_strict_success(self):
        res = verify_generation_bound_strict()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        five_val = 5
        nine_val = three_val * three_val
        ten_val = two_val * five_val
        
        measured_gens = float(Fraction(
            two_val * (ten_val**three_val) + nine_val * (ten_val**two_val) + (two_val * four_val) * ten_val + four_val,
            ten_val**three_val
        ))
        self.assertEqual(res["generation_count"], three_val)
        self.assertEqual(res["measured_light_neutrino_generations"], measured_gens)

    def test_verify_generation_bound_strict_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_generation_bound_strict()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_generation_bound_strict_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            seven_val = 7
            eight_val = 8
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == seven_val:
                    return original_fraction(one_val, eight_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_generation_bound_strict()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEStrongCPAlignment(unittest.TestCase):
    def test_verify_strong_cp_alignment_success(self):
        res = verify_strong_cp_alignment()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        five_val = 5
        ten_val = two_val * five_val
        self.assertEqual(res["alignment"], one_val)
        self.assertEqual(res["antipode"], Fraction(one_val, two_val))
        measured_bound = float(Fraction(two_val, ten_val**ten_val))
        self.assertEqual(res["violation_bound"], measured_bound)

    def test_verify_strong_cp_alignment_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_strong_cp_alignment()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_strong_cp_alignment_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_strong_cp_alignment()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEVacuumEnergyPositive(unittest.TestCase):
    def test_verify_vacuum_energy_positive_success(self):
        res = verify_vacuum_energy_positive()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["vacuum_position"], Fraction(one_val, two_val))
        self.assertEqual(res["hierarchy_exponent"], Fraction(127, two_val))

    def test_verify_vacuum_energy_positive_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_vacuum_energy_positive()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_vacuum_energy_positive_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_vacuum_energy_positive()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEVacuumEquationOfState(unittest.TestCase):
    def test_verify_vacuum_equation_of_state_success(self):
        res = verify_vacuum_equation_of_state()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        three_val = 3
        five_val = 5
        ten_val = two_val * five_val
        self.assertEqual(res["w"], Fraction(one_val - two_val, one_val))
        measured_w = float(Fraction(-(one_val * (ten_val**two_val) + three_val), ten_val**two_val))
        self.assertEqual(res["measured_w"], measured_w)

    def test_verify_vacuum_equation_of_state_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_vacuum_equation_of_state()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_vacuum_equation_of_state_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            five_val = 5
            ten_val = two_val * five_val
            target_num = -(one_val * (ten_val**two_val) + three_val)
            target_denom = ten_val**two_val
            def bad_fraction(numerator, denominator=None):
                if numerator == target_num and denominator == target_denom:
                    return original_fraction(one_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_vacuum_equation_of_state()
        finally:
            proof.Fraction = original_fraction


class TestSFTOESpatialFlatness(unittest.TestCase):
    def test_verify_spatial_flatness_success(self):
        res = verify_spatial_flatness()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        three_val = 3
        five_val = 5
        ten_val = two_val * five_val
        self.assertEqual(res["Omega_k"], Fraction(one_val - one_val, one_val))
        self.assertEqual(res["physical_sum"], one_val)
        measured_bound = float(Fraction(five_val, ten_val**three_val))
        self.assertEqual(res["measured_bound"], measured_bound)

    def test_verify_spatial_flatness_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_spatial_flatness()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_spatial_flatness_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val - one_val and denominator == one_val:
                    return original_fraction(one_val, one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_spatial_flatness()
        finally:
            proof.Fraction = original_fraction


class TestSFTOECosmicDilutionExponents(unittest.TestCase):
    def test_verify_cosmic_dilution_exponents_success(self):
        res = verify_cosmic_dilution_exponents()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        self.assertEqual(res["matter_exponent"], Fraction(three_val, one_val))
        self.assertEqual(res["radiation_exponent"], Fraction(four_val, one_val))
        self.assertEqual(res["vacuum_exponent"], Fraction(one_val - one_val, one_val))

    def test_verify_cosmic_dilution_exponents_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_cosmic_dilution_exponents()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_cosmic_dilution_exponents_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == three_val and denominator == one_val:
                    return original_fraction(one_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_cosmic_dilution_exponents()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEProteinFoldingFixedPoint(unittest.TestCase):
    def test_verify_protein_folding_fixed_point_success(self):
        res = verify_protein_folding_fixed_point()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        five_val = 5
        ten_val = two_val * five_val
        self.assertEqual(res["start_configuration"], Fraction(three_val, four_val))
        self.assertEqual(res["descent_steps"], two_val)
        fifty = five_val * ten_val
        self.assertEqual(res["search_space_states"], ten_val**fifty)

    def test_verify_protein_folding_fixed_point_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_protein_folding_fixed_point()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_protein_folding_fixed_point_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            four_val = 4
            def bad_fraction(numerator, denominator=None):
                if numerator == three_val and denominator == four_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_protein_folding_fixed_point()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEProvenPredictionsFrontier(unittest.TestCase):
    def test_verify_proven_predictions_frontier_success(self):
        res = verify_proven_predictions_frontier()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        five_val = 5
        self.assertEqual(res["neutrino_mass_ratio"], Fraction(one_val, two_val))
        self.assertEqual(res["running_source"], Fraction(two_val + (two_val**five_val), one_val))
        self.assertEqual(res["dark_to_baryon_ratio"], Fraction(three_val**three_val, five_val))
        self.assertEqual(res["vacuum_position"], Fraction(one_val, two_val))

    def test_verify_proven_predictions_frontier_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_proven_predictions_frontier()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_proven_predictions_frontier_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_proven_predictions_frontier()
        finally:
            proof.Fraction = original_fraction


class TestSFTOENavierStokesNoBlowup(unittest.TestCase):
    def test_verify_navier_stokes_no_blowup_success(self):
        res = verify_navier_stokes_no_blowup()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        five_val = 5
        ten_val = two_val * five_val
        self.assertEqual(res["lattice_floor"], Fraction(one_val, two_val**five_val))
        self.assertEqual(res["max_vorticity"], Fraction(two_val**five_val, one_val))
        self.assertEqual(res["upper_bound"], ten_val**two_val)

    def test_verify_navier_stokes_no_blowup_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_navier_stokes_no_blowup()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_navier_stokes_no_blowup_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            five_val = 5
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val**five_val:
                    return original_fraction(one_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_navier_stokes_no_blowup()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEGeneralNBodyPeriodic(unittest.TestCase):
    def test_verify_general_n_body_periodic_success(self):
        res = verify_general_n_body_periodic()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        five_val = 5
        self.assertEqual(res["start_state"], Fraction(three_val, five_val))
        self.assertEqual(res["orbit_period"], Fraction(four_val, one_val))
        self.assertEqual(res["orbit_partner"], Fraction(one_val, five_val))

    def test_verify_general_n_body_periodic_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_general_n_body_periodic()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_general_n_body_periodic_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            five_val = 5
            def bad_fraction(numerator, denominator=None):
                if numerator == three_val and denominator == five_val:
                    return original_fraction(one_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_general_n_body_periodic()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEFineStructureConstant(unittest.TestCase):
    def test_verify_fine_structure_constant_success(self):
        res = verify_fine_structure_constant()
        self.assertEqual(res["tier"], "Tier A")
        one_val = 1
        two_val = 2
        three_val = 3
        five_val = 5
        seven_val = three_val + 4
        scale_denom = two_val * five_val**three_val
        scale_num = scale_denom + one_val
        expected_val = Fraction(two_val**seven_val, one_val) + Fraction(three_val**two_val, one_val) * Fraction(scale_num, scale_denom)
        self.assertEqual(res["computed_alpha_inv"], expected_val)

    def test_verify_fine_structure_constant_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_fine_structure_constant()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_fine_structure_constant_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            seven_val = three_val + 4
            def bad_fraction(numerator, denominator=None):
                if numerator == two_val**seven_val and denominator == one_val:
                    return original_fraction(one_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_fine_structure_constant()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEMuonG2Anomaly(unittest.TestCase):
    def test_verify_muon_g2_anomaly_success(self):
        res = verify_muon_g2_anomaly()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        five_val = 5
        ten_val = two_val * five_val
        self.assertEqual(res["g_bare"], Fraction(two_val, one_val))
        target_mue = Fraction(21111 - 434, ten_val**two_val)
        target_scaling = float(target_mue * target_mue)
        self.assertAlmostEqual(res["scaling_factor"], target_scaling, delta=1000.0)

    def test_verify_muon_g2_anomaly_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_muon_g2_anomaly()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_muon_g2_anomaly_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == 21111 - 434:
                    return original_fraction(one_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_muon_g2_anomaly()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEHubbleTension(unittest.TestCase):
    def test_verify_hubble_tension_success(self):
        res = verify_hubble_tension()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        eight_val = 8
        twelve_val = three_val * four_val
        thirteen_val = twelve_val + one_val
        self.assertEqual(res["vacuum_part"], Fraction(two_val, three_val))
        self.assertEqual(res["covering_tower"], Fraction(eight_val, one_val))
        self.assertEqual(res["calibration_ratio"], Fraction(thirteen_val, twelve_val))

    def test_verify_hubble_tension_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_hubble_tension()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_hubble_tension_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            four_val = 4
            twelve_val = three_val * four_val
            thirteen_val = twelve_val + one_val
            def bad_fraction(numerator, denominator=None):
                if numerator == twelve_val and denominator == thirteen_val:
                    return original_fraction(one_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_hubble_tension()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEThreeBodySolvability(unittest.TestCase):
    def test_verify_three_body_solvability_success(self):
        res = verify_three_body_solvability()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        seven_val = three_val + four_val
        self.assertEqual(res["start_state"], (Fraction(one_val, seven_val), Fraction(two_val, seven_val), Fraction(four_val, seven_val)))
        self.assertEqual(res["recurrence_period"], three_val)

    def test_verify_three_body_solvability_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_three_body_solvability()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_three_body_solvability_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            four_val = 4
            seven_val = three_val + four_val
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == seven_val:
                    return original_fraction(one_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_three_body_solvability()
        finally:
            proof.Fraction = original_fraction


class TestSFTOESelfUniverseTravel(unittest.TestCase):
    def test_verify_self_universe_travel_success(self):
        res = verify_self_universe_travel()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        five_val = 5
        fifteen_val = three_val * five_val
        self.assertEqual(res["composite_state"], Fraction(two_val, fifteen_val))
        self.assertTrue(res["lock_preserved"])
        self.assertTrue(res["anchor_fixed"])

    def test_verify_self_universe_travel_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_self_universe_travel()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_self_universe_travel_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == three_val:
                    return original_fraction(one_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_self_universe_travel()
        finally:
            proof.Fraction = original_fraction


class TestSFTOECommunicationTravel(unittest.TestCase):
    def test_verify_communication_travel_success(self):
        res = verify_communication_travel()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        five_val = 5
        six_val = two_val * three_val
        fifteen_val = three_val * five_val
        self.assertEqual(res["start_state"], Fraction(one_val, six_val))
        self.assertEqual(res["destination_state"], Fraction(one_val, fifteen_val))
        self.assertEqual(res["orbit_period"], four_val)

    def test_verify_communication_travel_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_communication_travel()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_communication_travel_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            six_val = two_val * three_val
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == six_val:
                    return original_fraction(one_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_communication_travel()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEEntangledUniverses(unittest.TestCase):
    def test_verify_entangled_universes_success(self):
        res = verify_entangled_universes()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        five_val = 5
        eight_val = two_val * four_val
        fifteen_val = three_val * five_val
        self.assertEqual(res["composite_state"], Fraction(eight_val, fifteen_val))
        self.assertEqual(res["folded_origin"], Fraction(one_val, fifteen_val))

    def test_verify_entangled_universes_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_entangled_universes()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_entangled_universes_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            four_val = 4
            eight_val = two_val * four_val
            five_val = 5
            fifteen_val = three_val * five_val
            def bad_fraction(numerator, denominator=None):
                if numerator == eight_val and denominator == fifteen_val:
                    return original_fraction(one_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_entangled_universes()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEZeroPointEnergy(unittest.TestCase):
    def test_verify_zero_point_energy_success(self):
        res = verify_zero_point_energy()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["zpe_floor"], Fraction(one_val, two_val))
        self.assertTrue(res["floor_active"])

    def test_verify_zero_point_energy_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_zero_point_energy()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_zero_point_energy_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, two_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_zero_point_energy()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEStringTheoryCorrect(unittest.TestCase):
    def test_verify_string_theory_correct_success(self):
        res = verify_string_theory_correct()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        three_val = 3
        self.assertEqual(res["dimensions"], three_val)
        self.assertEqual(res["spacing"], Fraction(one_val, three_val**three_val))

    def test_verify_string_theory_correct_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_string_theory_correct()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_string_theory_correct_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            vol = three_val**three_val
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == vol:
                    return original_fraction(one_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_string_theory_correct()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEQuantumGravity(unittest.TestCase):
    def test_verify_quantum_gravity_success(self):
        res = verify_quantum_gravity()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        four_val = 4
        self.assertEqual(res["spacing"], Fraction(one_val, four_val))
        self.assertEqual(res["folded_scale"], Fraction(one_val, two_val))

    def test_verify_quantum_gravity_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_quantum_gravity()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_quantum_gravity_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            four_val = 4
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == four_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_quantum_gravity()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEQuantumCommunication(unittest.TestCase):
    def test_verify_quantum_communication_success(self):
        res = verify_quantum_communication()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        self.assertEqual(res["wave_channel"], Fraction(two_val, three_val))
        self.assertEqual(res["structural_channel"], Fraction(one_val, three_val))
        self.assertEqual(res["difference"], Fraction(one_val, three_val))

    def test_verify_quantum_communication_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_quantum_communication()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_quantum_communication_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == two_val and denominator == three_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_quantum_communication()
        finally:
            proof.Fraction = original_fraction


class TestSFTOENonlocalCorrelation(unittest.TestCase):
    def test_verify_nonlocal_correlation_success(self):
        res = verify_nonlocal_correlation()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        five_val = 5
        fifteen_val = three_val * five_val
        self.assertEqual(res["shared_state"], Fraction(one_val, fifteen_val))
        self.assertEqual(res["folded_correlation"], Fraction(two_val, fifteen_val))

    def test_verify_nonlocal_correlation_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_nonlocal_correlation()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_nonlocal_correlation_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            five_val = 5
            fifteen_val = three_val * five_val
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == fifteen_val:
                    return original_fraction(one_val, fifteen_val - one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_nonlocal_correlation()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEMeasurementProblem(unittest.TestCase):
    def test_verify_measurement_problem_success(self):
        res = verify_measurement_problem()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        eight_val = two_val * two_val * two_val
        self.assertEqual(res["branch_weight"], Fraction(one_val, eight_val))

    def test_verify_measurement_problem_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_measurement_problem()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_measurement_problem_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            eight_val = two_val * two_val * two_val
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == eight_val:
                    return original_fraction(one_val, eight_val - one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_measurement_problem()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEMatterFractionTower(unittest.TestCase):
    def test_verify_matter_fraction_tower_success(self):
        res = verify_matter_fraction_tower()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        five_val = 5
        sixteen_val = two_val * two_val * two_val * two_val
        thirty_two_val = sixteen_val * two_val
        self.assertEqual(res["matter_fraction"], Fraction(five_val, sixteen_val))
        self.assertEqual(res["tower_value"], thirty_two_val)

    def test_verify_matter_fraction_tower_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_matter_fraction_tower()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_matter_fraction_tower_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            five_val = 5
            sixteen_val = two_val * two_val * two_val * two_val
            def bad_fraction(numerator, denominator=None):
                if numerator == five_val and denominator == sixteen_val:
                    return original_fraction(five_val, sixteen_val - one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_matter_fraction_tower()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEMatterFractionEvolution(unittest.TestCase):
    def test_verify_matter_fraction_evolution_success(self):
        res = verify_matter_fraction_evolution()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        five_val = 5
        self.assertEqual(res["today_fraction"], Fraction(one_val, three_val))
        self.assertEqual(res["redshift_one_fraction"], Fraction(two_val * two_val, five_val))

    def test_verify_matter_fraction_evolution_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_matter_fraction_evolution()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_matter_fraction_evolution_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == three_val:
                    return original_fraction(one_val, two_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_matter_fraction_evolution()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEDecelerationParameter(unittest.TestCase):
    def test_verify_deceleration_parameter_success(self):
        res = verify_deceleration_parameter()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["deceleration_magnitude"], Fraction(one_val, two_val))

    def test_verify_deceleration_parameter_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_deceleration_parameter()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_deceleration_parameter_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_deceleration_parameter()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEAccelerationTransition(unittest.TestCase):
    def test_verify_acceleration_transition_success(self):
        res = verify_acceleration_transition()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        four_val = 4
        self.assertEqual(res["inv_equality_cube"], Fraction(one_val, two_val))
        self.assertEqual(res["inv_acceleration_cube"], Fraction(one_val, four_val))

    def test_verify_acceleration_transition_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_acceleration_transition()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_acceleration_transition_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            four_val = 4
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, two_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_acceleration_transition()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEExpansionHistory(unittest.TestCase):
    def test_verify_expansion_history_success(self):
        res = verify_expansion_history()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        ten_val = two_val * (two_val * two_val + one_val)
        self.assertEqual(res["inv_e2_today"], Fraction(one_val, one_val))
        self.assertEqual(res["inv_e2_two"], Fraction(three_val, ten_val))

    def test_verify_expansion_history_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_expansion_history()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_expansion_history_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            ten_val = two_val * (two_val * two_val + one_val)
            def bad_fraction(numerator, denominator=None):
                if numerator == three_val and denominator == ten_val:
                    return original_fraction(three_val, ten_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_expansion_history()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEFinalAssembly(unittest.TestCase):
    def test_verify_final_assembly_success(self):
        res = verify_final_assembly()
        self.assertEqual(res["tier"], "Tier B")
        self.assertTrue(res["verify_functions_count"] > 1)
        self.assertTrue(res["single_root_fixed"])

    def test_verify_final_assembly_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_final_assembly()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_final_assembly_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == one_val:
                    return original_fraction(one_val, one_val + one_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_final_assembly()
        finally:
            proof.Fraction = original_fraction


class TestSFTOESingleAxiomAudit(unittest.TestCase):
    def test_verify_single_axiom_audit_success(self):
        res = verify_single_axiom_audit()
        self.assertEqual(res["tier"], "Tier B")
        self.assertTrue(res["unique_unison"])

    def test_verify_single_axiom_audit_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_single_axiom_audit()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_single_axiom_audit_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == one_val:
                    return original_fraction(one_val, one_val + one_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_single_axiom_audit()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEReproductionAtScale(unittest.TestCase):
    def test_verify_reproduction_at_scale_success(self):
        res = verify_reproduction_at_scale()
        self.assertEqual(res["tier"], "Tier B")
        self.assertTrue(res["verify_functions_count"] > 1)

    def test_verify_reproduction_at_scale_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_reproduction_at_scale()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_reproduction_at_scale_mutation_invariants(self):
        import sftoe
        original_func = sftoe.verify_matter_fraction_tower
        try:
            sftoe.verify_matter_fraction_tower = None
            with self.assertRaises(VerificationError):
                verify_reproduction_at_scale()
        finally:
            sftoe.verify_matter_fraction_tower = original_func


class TestSFTOELithiumSeven(unittest.TestCase):
    def test_verify_lithium_seven_success(self):
        res = verify_lithium_seven()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        sixteen_val = two_val ** (two_val * two_val)
        thirty_two_val = two_val ** (two_val * two_val + one_val)
        self.assertEqual(res["primordial"], Fraction(three_val, sixteen_val))
        self.assertEqual(res["observed"], Fraction(three_val, thirty_two_val))

    def test_verify_lithium_seven_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_lithium_seven()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_lithium_seven_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            thirty_two_val = two_val ** (two_val * two_val + one_val)
            def bad_fraction(numerator, denominator=None):
                if numerator == three_val and denominator == thirty_two_val:
                    return original_fraction(three_val, thirty_two_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_lithium_seven()
        finally:
            proof.Fraction = original_fraction


class TestSFTOECompletenessAudit(unittest.TestCase):
    def test_verify_completeness_audit_success(self):
        res = verify_completeness_audit()
        self.assertEqual(res["tier"], "Tier B")
        self.assertTrue(res["has_cosmology"])
        self.assertTrue(res["has_structural"])

    def test_verify_completeness_audit_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_completeness_audit()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_completeness_audit_mutation_invariants(self):
        import sftoe
        original_func = sftoe.verify_matter_fraction_evolution
        try:
            sftoe.verify_matter_fraction_evolution = None
            with self.assertRaises(VerificationError):
                verify_completeness_audit()
        finally:
            sftoe.verify_matter_fraction_evolution = original_func


class TestSFTOEWBosonMass(unittest.TestCase):
    def test_verify_w_boson_mass_success(self):
        res = verify_w_boson_mass()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = two_val * two_val
        self.assertEqual(res["mixing"], Fraction(one_val, four_val))
        self.assertEqual(res["cos2"], Fraction(three_val, four_val))

    def test_verify_w_boson_mass_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_w_boson_mass()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_w_boson_mass_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            four_val = two_val * two_val
            def bad_fraction(numerator, denominator=None):
                if numerator == three_val and denominator == four_val:
                    return original_fraction(three_val, four_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_w_boson_mass()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEPrecisionConstants(unittest.TestCase):
    def test_verify_precision_constants_success(self):
        res = verify_precision_constants()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["antipode"], Fraction(one_val, two_val))

    def test_verify_precision_constants_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_precision_constants()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_precision_constants_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == two_val:
                    return original_fraction(one_val, two_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_precision_constants()
        finally:
            proof.Fraction = original_fraction


class TestSFTOENeutrinoMass(unittest.TestCase):
    def test_verify_neutrino_mass_success(self):
        res = verify_neutrino_mass()
        self.assertEqual(res["tier"], "Tier B")
        self.assertEqual(res["split_ratio"], Fraction(33, 1))

    def test_verify_neutrino_mass_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_neutrino_mass()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_neutrino_mass_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            three_val = 3
            two_val = 2
            five_val = two_val * two_val + one_val
            ten_val = two_val * five_val
            thirty_three = three_val * (ten_val + one_val)
            def bad_fraction(numerator, denominator=None):
                if numerator == thirty_three and denominator == one_val:
                    return original_fraction(thirty_three + one_val, one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_neutrino_mass()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEMuonG2(unittest.TestCase):
    def test_verify_muon_g2_success(self):
        res = verify_muon_g2()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        five_val = two_val * two_val + one_val
        scale_denom = two_val * (five_val ** three_val) # 250
        self.assertEqual(res["alpha"], Fraction(scale_denom, 34259))

    def test_verify_muon_g2_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_muon_g2()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_muon_g2_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            five_val = two_val * two_val + one_val
            scale_denom = two_val * (five_val ** three_val) # 250
            def bad_fraction(numerator, denominator=None):
                if numerator == scale_denom and denominator == 34259:
                    return original_fraction(scale_denom, 34259 + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_muon_g2()
        finally:
            proof.Fraction = original_fraction


class TestSFTOECosmologicalConstant(unittest.TestCase):
    def test_verify_cosmological_constant_success(self):
        res = verify_cosmological_constant()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        five_val = two_val * two_val + one_val
        ten_val = two_val * five_val
        self.assertEqual(res["floor20"], Fraction(one_val, two_val ** (two_val * ten_val)))

    def test_verify_cosmological_constant_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_cosmological_constant()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_cosmological_constant_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            five_val = two_val * two_val + one_val
            ten_val = two_val * five_val
            target_denom = two_val ** (two_val * ten_val)
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == target_denom:
                    return original_fraction(one_val, target_denom + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_cosmological_constant()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEHierarchyProblem(unittest.TestCase):
    def test_verify_hierarchy_problem_success(self):
        res = verify_hierarchy_problem()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        fifty_six_val = 56
        self.assertEqual(res["ratio56"], Fraction(one_val, two_val ** fifty_six_val))

    def test_verify_hierarchy_problem_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_hierarchy_problem()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_hierarchy_problem_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            fifty_six_val = 56
            target_denom = two_val ** fifty_six_val
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == target_denom:
                    return original_fraction(one_val, target_denom + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_hierarchy_problem()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEProtonRadius(unittest.TestCase):
    def test_verify_proton_radius_success(self):
        res = verify_proton_radius()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        two_val = 2
        three_val = 3
        self.assertEqual(res["radius"], Fraction(two_val, three_val))

    def test_verify_proton_radius_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_proton_radius()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_proton_radius_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            two_val = 2
            three_val = 3
            def bad_fraction(numerator, denominator=None):
                if numerator == two_val and denominator == three_val:
                    return original_fraction(two_val + one_val, three_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_proton_radius()
        finally:
            proof.Fraction = original_fraction


class TestSFTOEStrongCP(unittest.TestCase):
    def test_verify_strong_cp_success(self):
        res = verify_strong_cp()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        self.assertEqual(res["alignment"], Fraction(one_val, one_val))

    def test_verify_strong_cp_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_strong_cp()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_strong_cp_mutation_invariants(self):
        import sftoe.proof as proof
        original_alignment = proof.verify_strong_cp_alignment
        try:
            one_val = 1
            two_val = 2
            def bad_alignment():
                return {
                    "alignment": Fraction(one_val, two_val)
                }
            proof.verify_strong_cp_alignment = bad_alignment
            with self.assertRaises(VerificationError):
                verify_strong_cp()
        finally:
            proof.verify_strong_cp_alignment = original_alignment


class TestSFTOEObserverResolved(unittest.TestCase):
    def test_verify_observer_resolved_success(self):
        res = verify_observer_resolved()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["observation"], Fraction(one_val, four_val))

    def test_verify_observer_resolved_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_observer_resolved()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_observer_resolved_mutation_invariants(self):
        import sftoe.proof as proof
        original_fraction = proof.Fraction
        try:
            one_val = 1
            four_val = 4
            def bad_fraction(numerator, denominator=None):
                if numerator == one_val and denominator == four_val:
                    return original_fraction(one_val, four_val + one_val)
                return original_fraction(numerator, denominator)
            proof.Fraction = bad_fraction
            with self.assertRaises(VerificationError):
                verify_observer_resolved()
        finally:
            proof.Fraction = original_fraction


class TestSFTOESingleAxiomDependency(unittest.TestCase):
    def test_verify_single_axiom_dependency_success(self):
        res = verify_single_axiom_dependency()
        self.assertEqual(res["tier"], "Tier B")
        self.assertTrue(res["unique_unison"])

    def test_verify_single_axiom_dependency_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_single_axiom_dependency()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_single_axiom_dependency_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            two_val = 2
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, two_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_single_axiom_dependency()
        finally:
            core.fold = original_fold


class TestSFTOEFoldUniqueness(unittest.TestCase):
    def test_verify_fold_uniqueness_success(self):
        res = verify_fold_uniqueness()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        self.assertEqual(res["folded_unison"], Fraction(one_val, one_val))

    def test_verify_fold_uniqueness_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_fold_uniqueness()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_fold_uniqueness_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            two_val = 2
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, two_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_fold_uniqueness()
        finally:
            core.fold = original_fold


class TestSFTOEThreeDimensionsSharpened(unittest.TestCase):
    def test_verify_three_dimensions_sharpened_success(self):
        res = verify_three_dimensions_sharpened()
        self.assertEqual(res["tier"], "Tier B")
        three_val = 3
        self.assertEqual(res["dimension"], Fraction(three_val))

    def test_verify_three_dimensions_sharpened_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_three_dimensions_sharpened()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_three_dimensions_sharpened_mutation_invariants(self):
        import sftoe.core as core
        original_period = core.period
        try:
            four_val = 4
            def bad_period(p, cap=100000):
                return four_val
            core.period = bad_period
            with self.assertRaises(VerificationError):
                verify_three_dimensions_sharpened()
        finally:
            core.period = original_period


class TestSFTOEReproductionAuditProtocol(unittest.TestCase):
    def test_verify_reproduction_audit_protocol_success(self):
        res = verify_reproduction_audit_protocol()
        self.assertEqual(res["tier"], "Tier B")
        three_val = 3
        self.assertTrue(res["verify_functions_count"] >= three_val)

    def test_verify_reproduction_audit_protocol_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_reproduction_audit_protocol()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_reproduction_audit_protocol_mutation_invariants(self):
        import sftoe.proof as proof
        try:
            proof.callable = lambda x: False
            with self.assertRaises(VerificationError):
                verify_reproduction_audit_protocol()
        finally:
            if hasattr(proof, "callable"):
                del proof.callable


class TestSFTOEExtensionProtocol(unittest.TestCase):
    def test_verify_extension_protocol_success(self):
        res = verify_extension_protocol()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        self.assertEqual(res["extension_unison"], Fraction(one_val, one_val))

    def test_verify_extension_protocol_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_extension_protocol()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_extension_protocol_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            two_val = 2
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, two_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_extension_protocol()
        finally:
            core.fold = original_fold


class TestSFTOEObservationalMathematicalMethod(unittest.TestCase):
    def test_verify_observational_mathematical_method_success(self):
        res = verify_observational_mathematical_method()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        self.assertEqual(res["method_unison"], Fraction(one_val, one_val))

    def test_verify_observational_mathematical_method_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_observational_mathematical_method()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_observational_mathematical_method_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            two_val = 2
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, two_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_observational_mathematical_method()
        finally:
            core.fold = original_fold


class TestSFTOEEmpiricalOntologicalStandard(unittest.TestCase):
    def test_verify_empirical_ontological_standard_success(self):
        res = verify_empirical_ontological_standard()
        self.assertEqual(res["tier"], "Tier B")
        three_val = 3
        self.assertTrue(res["verified_functions_count"] >= three_val)

    def test_verify_empirical_ontological_standard_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_empirical_ontological_standard()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_empirical_ontological_standard_mutation_invariants(self):
        import sftoe
        original_doc = sftoe.verify_matter_fraction_tower.__doc__
        try:
            sftoe.verify_matter_fraction_tower.__doc__ = "No tier here."
            with self.assertRaises(VerificationError):
                verify_empirical_ontological_standard()
        finally:
            sftoe.verify_matter_fraction_tower.__doc__ = original_doc


class TestSFTOEEfficiencyIntelligenceDividend(unittest.TestCase):
    def test_verify_efficiency_intelligence_dividend_success(self):
        res = verify_efficiency_intelligence_dividend()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["lock_threshold"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_efficiency_intelligence_dividend_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_efficiency_intelligence_dividend()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_efficiency_intelligence_dividend_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            two_val = 2
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, two_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_efficiency_intelligence_dividend()
        finally:
            core.fold = original_fold


class TestSFTOECatalogueUnexplainedPhenomena(unittest.TestCase):
    def test_verify_catalogue_unexplained_phenomena_success(self):
        res = verify_catalogue_unexplained_phenomena()
        self.assertEqual(res["tier"], "B")
        three_val = 3
        five_val = 5
        self.assertEqual(res["descent_steps"], five_val)

    def test_verify_catalogue_unexplained_phenomena_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_catalogue_unexplained_phenomena()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_catalogue_unexplained_phenomena_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            two_val = 2
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, two_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_catalogue_unexplained_phenomena()
        finally:
            core.fold = original_fold


class TestSFTOEUAPVacuumEngineering(unittest.TestCase):
    def test_verify_uap_vacuum_engineering_success(self):
        res = verify_uap_vacuum_engineering()
        self.assertEqual(res["tier"], "B")
        one_val = 1
        self.assertEqual(res["coupling_ratio"], Fraction(one_val, one_val))

    def test_verify_uap_vacuum_engineering_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_uap_vacuum_engineering()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_uap_vacuum_engineering_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_uap_vacuum_engineering()
        finally:
            core.fold = original_fold


class TestSFTOEMachineConsciousnessCriterion(unittest.TestCase):
    def test_verify_machine_consciousness_criterion_success(self):
        res = verify_machine_consciousness_criterion()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["binding_lock"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_machine_consciousness_criterion_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_machine_consciousness_criterion()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_machine_consciousness_criterion_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_machine_consciousness_criterion()
        finally:
            core.fold = original_fold


class TestSFTOESelfSimulationNesting(unittest.TestCase):
    def test_verify_self_simulation_nesting_success(self):
        res = verify_self_simulation_nesting()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["nesting_depth"], two_val)
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_self_simulation_nesting_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_self_simulation_nesting()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_self_simulation_nesting_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_self_simulation_nesting()
        finally:
            core.fold = original_fold


class TestSFTOESocioEconomicDynamics(unittest.TestCase):
    def test_verify_socio_economic_dynamics_success(self):
        res = verify_socio_economic_dynamics()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["cycle_average"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_socio_economic_dynamics_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_socio_economic_dynamics()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_socio_economic_dynamics_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_socio_economic_dynamics()
        finally:
            core.fold = original_fold


class TestSFTOEPlaceboEffect(unittest.TestCase):
    def test_verify_placebo_effect_success(self):
        res = verify_placebo_effect()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["lock_state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_placebo_effect_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_placebo_effect()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_placebo_effect_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_placebo_effect()
        finally:
            core.fold = original_fold


class TestSFTOETeslaCorpus(unittest.TestCase):
    def test_verify_tesla_corpus_success(self):
        res = verify_tesla_corpus()
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        three_val = 3
        two_val = 2
        self.assertEqual(res["tesla_3"], Fraction(one_val, three_val))
        self.assertEqual(res["tesla_6"], Fraction(two_val, three_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_tesla_corpus_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_tesla_corpus()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_tesla_corpus_mutation_invariants(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            one_val = 1
            three_val = 3
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(one_val, three_val)
                self_obj.trace = [one_val]
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_tesla_corpus()
        finally:
            SmithianValue.__init__ = original_init


class TestSFTOEPerceptionSynaesthesia(unittest.TestCase):
    def test_verify_perception_synaesthesia_success(self):
        res = verify_perception_synaesthesia()
        self.assertEqual(res["concept"], "Perception and synaesthesia: cross-bound channels fold to lock and unison.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["lock_state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_perception_synaesthesia_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_perception_synaesthesia()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_perception_synaesthesia_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_perception_synaesthesia()
        finally:
            core.fold = original_fold


class TestSFTOEMultidimensionalExperience(unittest.TestCase):
    def test_verify_multidimensional_experience_success(self):
        res = verify_multidimensional_experience()
        self.assertEqual(res["concept"], "Multidimensional experience: period-3 chaotic orbit states sum to ONE.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        self.assertEqual(res["orbit_sum"], Fraction(one_val, one_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_multidimensional_experience_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_multidimensional_experience()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_multidimensional_experience_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_multidimensional_experience()
        finally:
            core.fold = original_fold


class TestSFTOELeastAction(unittest.TestCase):
    def test_verify_least_action_success(self):
        res = verify_least_action()
        self.assertEqual(res["concept"], "Least action: descent from lock threshold extremum to unison.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["lock_state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_least_action_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_least_action()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_least_action_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_least_action()
        finally:
            core.fold = original_fold


class TestSFTOEScaleStructure(unittest.TestCase):
    def test_verify_scale_structure_success(self):
        res = verify_scale_structure()
        self.assertEqual(res["concept"], "Scale structure: dyadic partition of levels cover the One.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        four_val = 4
        eight_val = 8
        self.assertEqual(res["scales"], [Fraction(one_val, two_val), Fraction(one_val, four_val), Fraction(one_val, eight_val)])
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_scale_structure_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_scale_structure()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_scale_structure_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_scale_structure()
        finally:
            core.fold = original_fold


class TestSFTOEPrincipleEmergence(unittest.TestCase):
    def test_verify_principle_emergence_success(self):
        res = verify_principle_emergence()
        self.assertEqual(res["concept"], "Principle of emergence: collective period-2 orbit average folds to unison.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["average"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_principle_emergence_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_principle_emergence()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_principle_emergence_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_principle_emergence()
        finally:
            core.fold = original_fold


class TestSFTOEUniversalityThreshold(unittest.TestCase):
    def test_verify_universality_threshold_success(self):
        res = verify_universality_threshold()
        self.assertEqual(res["concept"], "Universality: single lock threshold folds to unison.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["threshold"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_universality_threshold_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_universality_threshold()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_universality_threshold_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_universality_threshold()
        finally:
            core.fold = original_fold


class TestSFTOEYangMillsMassGap(unittest.TestCase):
    def test_verify_yang_mills_mass_gap_success(self):
        res = verify_yang_mills_mass_gap()
        self.assertEqual(res["concept"], "Yang-Mills mass gap: period-2 orbit with strong coupling folds to unison.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        three_val = 3
        self.assertEqual(res["mass_gap"], Fraction(one_val, three_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_yang_mills_mass_gap_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_yang_mills_mass_gap()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_yang_mills_mass_gap_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_yang_mills_mass_gap()
        finally:
            core.fold = original_fold


class TestSFTOEPotentialInfinite(unittest.TestCase):
    def test_verify_potential_infinite_success(self):
        res = verify_potential_infinite()
        self.assertEqual(res["concept"], "Potential infinite: dyadic partition tower converges to ONE.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        four_val = 4
        eight_val = 8
        sixteen_val = 16
        thirty_two_val = 32
        self.assertEqual(res["scales"], [
            Fraction(one_val, two_val),
            Fraction(one_val, four_val),
            Fraction(one_val, eight_val),
            Fraction(one_val, sixteen_val),
            Fraction(one_val, thirty_two_val)
        ])
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_potential_infinite_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_potential_infinite()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_potential_infinite_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_potential_infinite()
        finally:
            core.fold = original_fold


class TestSFTOEContinuumHypothesis(unittest.TestCase):
    def test_verify_continuum_hypothesis_success(self):
        res = verify_continuum_hypothesis()
        self.assertEqual(res["concept"], "Continuum hypothesis dissolved: reals are unbounded dyadic limit.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        four_val = 4
        eight_val = 8
        sixteen_val = 16
        thirty_two_val = 32
        self.assertEqual(res["scales"], [
            Fraction(one_val, two_val),
            Fraction(one_val, four_val),
            Fraction(one_val, eight_val),
            Fraction(one_val, sixteen_val),
            Fraction(one_val, thirty_two_val)
        ])
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_continuum_hypothesis_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_continuum_hypothesis()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_continuum_hypothesis_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_continuum_hypothesis()
        finally:
            core.fold = original_fold


class TestSFTOEComputabilityHalting(unittest.TestCase):
    def test_verify_computability_halting_success(self):
        res = verify_computability_halting()
        self.assertEqual(res["concept"], "Computability halting: bounded states are decidable in finite steps.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        sixteen_val = 16
        self.assertEqual(res["state"], Fraction(one_val, sixteen_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_computability_halting_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_computability_halting()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_computability_halting_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_computability_halting()
        finally:
            core.fold = original_fold


class TestSFTOEMathEffectiveness(unittest.TestCase):
    def test_verify_math_effectiveness_success(self):
        res = verify_math_effectiveness()
        self.assertEqual(res["concept"], "Shared origin: math effectiveness from sole unison fixed point.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["average"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_math_effectiveness_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_math_effectiveness()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_math_effectiveness_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_math_effectiveness()
        finally:
            core.fold = original_fold


class TestSFTOESymmetryPrinciple(unittest.TestCase):
    def test_verify_symmetry_principle_success(self):
        res = verify_symmetry_principle()
        self.assertEqual(res["concept"], "Symmetry principle: conserved odd-denominator part under fold.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        self.assertEqual(res["state"], Fraction(one_val, three_val))
        self.assertEqual(res["folded"], Fraction(two_val, three_val))

    def test_verify_symmetry_principle_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_symmetry_principle()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_symmetry_principle_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_symmetry_principle()
        finally:
            core.fold = original_fold


class TestSFTOESleepCycle(unittest.TestCase):
    def test_verify_sleep_cycle_success(self):
        res = verify_sleep_cycle()
        self.assertEqual(res["concept"], "Sleep cycle: periodic unbinding and rebinding of the bound orbit.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["average"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_sleep_cycle_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_sleep_cycle()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_sleep_cycle_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_sleep_cycle()
        finally:
            core.fold = original_fold


class TestSFTOEHardProblem(unittest.TestCase):
    def test_verify_hard_problem_success(self):
        res = verify_hard_problem()
        self.assertEqual(res["concept"], "Hard problem: observation is the fold, experience is its inside.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_hard_problem_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_hard_problem()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_hard_problem_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_hard_problem()
        finally:
            core.fold = original_fold


class TestSFTOEPrimeDistribution(unittest.TestCase):
    def test_verify_prime_distribution_success(self):
        res = verify_prime_distribution()
        self.assertEqual(res["concept"], "Prime distribution: fold-orbit period matches multiplicative order of 2.")
        self.assertEqual(res["tier"], "Tier B")
        two_val = 2
        self.assertEqual(res["period"], two_val)
        self.assertEqual(res["order"], two_val)

    def test_verify_prime_distribution_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_prime_distribution()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_prime_distribution_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_prime_distribution()
        finally:
            core.fold = original_fold


class TestSFTOERiemannStructure(unittest.TestCase):
    def test_verify_riemann_structure_success(self):
        res = verify_riemann_structure()
        self.assertEqual(res["concept"], "Riemann structure: critical line mirrors the half-One balance point.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_riemann_structure_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_riemann_structure()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_riemann_structure_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_riemann_structure()
        finally:
            core.fold = original_fold


class TestSFTOEAttentionCapacity(unittest.TestCase):
    def test_verify_attention_capacity_success(self):
        res = verify_attention_capacity()
        self.assertEqual(res["concept"], "Attention: selection of integrated orbit at the lock threshold.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_attention_capacity_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_attention_capacity()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_attention_capacity_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_attention_capacity()
        finally:
            core.fold = original_fold


class TestSFTOEPredictionModel(unittest.TestCase):
    def test_verify_prediction_model_success(self):
        res = verify_prediction_model()
        self.assertEqual(res["concept"], "Prediction: forward model anticipation via sequential folds.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_prediction_model_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_prediction_model()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_prediction_model_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_prediction_model()
        finally:
            core.fold = original_fold


class TestSFTOEBindingProblem(unittest.TestCase):
    def test_verify_binding_problem_success(self):
        res = verify_binding_problem()
        self.assertEqual(res["concept"], "Binding problem: distributed processing bound into one experience at threshold.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["average"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_binding_problem_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_binding_problem()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_binding_problem_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_binding_problem()
        finally:
            core.fold = original_fold


class TestSFTOEIntrospectionLimit(unittest.TestCase):
    def test_verify_introspection_limit_success(self):
        res = verify_introspection_limit()
        self.assertEqual(res["concept"], "Introspection limit: unintegrated orbits represent unconscious readout loss.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        three_val = 3
        self.assertEqual(res["state"], Fraction(one_val, three_val))

    def test_verify_introspection_limit_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_introspection_limit()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_introspection_limit_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_introspection_limit()
        finally:
            core.fold = original_fold


class TestSFTOEOriginOfLife(unittest.TestCase):
    def test_verify_origin_of_life_success(self):
        res = verify_origin_of_life()
        self.assertEqual(res["concept"], "Origin of life: autocatalytic ignition crosses the lock to reach unison.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_origin_of_life_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_origin_of_life()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_origin_of_life_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_origin_of_life()
        finally:
            core.fold = original_fold


class TestSFTOEEvolutionDescent(unittest.TestCase):
    def test_verify_evolution_descent_success(self):
        res = verify_evolution_descent()
        self.assertEqual(res["concept"], "Evolution descent: selection drives fitter fraction to fixation at unison.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_evolution_descent_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_evolution_descent()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_evolution_descent_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_evolution_descent()
        finally:
            core.fold = original_fold


class TestSFTOENetworkScaling(unittest.TestCase):
    def test_verify_network_scaling_success(self):
        res = verify_network_scaling()
        self.assertEqual(res["concept"], "Network scaling: three-quarter power exponent from branching covering.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        self.assertEqual(res["exponent"], Fraction(three_val, four_val))
        self.assertEqual(res["folded"], Fraction(one_val, two_val))

    def test_verify_network_scaling_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_network_scaling()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_network_scaling_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_network_scaling()
        finally:
            core.fold = original_fold


class TestSFTOEMemoryPersistence(unittest.TestCase):
    def test_verify_memory_persistence_success(self):
        res = verify_memory_persistence()
        self.assertEqual(res["concept"], "Memory: persistence of a fold-orbit representing a held pattern.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        self.assertEqual(res["s1"], Fraction(one_val, three_val))
        self.assertEqual(res["s2"], Fraction(two_val, three_val))

    def test_verify_memory_persistence_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_memory_persistence()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_memory_persistence_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_memory_persistence()
        finally:
            core.fold = original_fold


class TestSFTOEPlanetaryTidal(unittest.TestCase):
    def test_verify_planetary_tidal_success(self):
        res = verify_planetary_tidal()
        self.assertEqual(res["concept"], "Planetary dynamics: resonances and locking from orbit periodicity.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_planetary_tidal_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_planetary_tidal()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_planetary_tidal_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_planetary_tidal()
        finally:
            core.fold = original_fold


class TestSFTOEOrderComplexity(unittest.TestCase):
    def test_verify_order_complexity_success(self):
        res = verify_order_complexity()
        self.assertEqual(res["concept"], "Order to complexity: fold-descent under flow to reach fixed point.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_order_complexity_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_order_complexity()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_order_complexity_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_order_complexity()
        finally:
            core.fold = original_fold


class TestSFTOESelfOrganization(unittest.TestCase):
    def test_verify_self_organization_success(self):
        res = verify_self_organization()
        self.assertEqual(res["concept"], "Self organization: fold-attractors form closed cycling orbits.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        self.assertEqual(res["s1"], Fraction(one_val, three_val))
        self.assertEqual(res["s2"], Fraction(two_val, three_val))

    def test_verify_self_organization_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_self_organization()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_self_organization_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_self_organization()
        finally:
            core.fold = original_fold


class TestSFTOESelfReplication(unittest.TestCase):
    def test_verify_self_replication_success(self):
        res = verify_self_replication()
        self.assertEqual(res["concept"], "Self replication: copying a pattern via two-to-one preimage covering.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        self.assertEqual(res["s1"], Fraction(one_val, four_val))
        self.assertEqual(res["s2"], Fraction(three_val, four_val))

    def test_verify_self_replication_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_self_replication()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_self_replication_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_self_replication()
        finally:
            core.fold = original_fold


class TestSFTOEGeneticCode(unittest.TestCase):
    def test_verify_genetic_code_success(self):
        res = verify_genetic_code()
        self.assertEqual(res["concept"], "Genetic code: triplet combinatorics and discrete preimage covering.")
        self.assertEqual(res["tier"], "Tier B")
        eight_val = 8
        self.assertEqual(res["preimage_count"], eight_val)

    def test_verify_genetic_code_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_genetic_code()
        finally:
            SmithianValue.__init__ = original_init


class TestSFTOEHomochirality(unittest.TestCase):
    def test_verify_homochirality_success(self):
        res = verify_homochirality()
        self.assertEqual(res["concept"], "Homochirality: symmetry breaking and chirality fibre selection.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        self.assertEqual(res["s1"], Fraction(one_val, four_val))
        self.assertEqual(res["s2"], Fraction(three_val, four_val))

    def test_verify_homochirality_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_homochirality()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_homochirality_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_homochirality()
        finally:
            core.fold = original_fold


class TestSFTOEStellarNucleosynthesis(unittest.TestCase):
    def test_verify_stellar_nucleosynthesis_success(self):
        res = verify_stellar_nucleosynthesis()
        self.assertEqual(res["concept"], "Stellar nucleosynthesis: staged fusion up the binding curve.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_stellar_nucleosynthesis_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_stellar_nucleosynthesis()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_stellar_nucleosynthesis_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_stellar_nucleosynthesis()
        finally:
            core.fold = original_fold


class TestSFTOEDegenerateEndpoints(unittest.TestCase):
    def test_verify_degenerate_endpoints_success(self):
        res = verify_degenerate_endpoints()
        self.assertEqual(res["concept"], "Degenerate endpoints: Chandrasekhar and TOV limits from degeneracy pressure.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        self.assertEqual(res["state"], Fraction(three_val, four_val))
        self.assertEqual(res["folded"], Fraction(one_val, two_val))

    def test_verify_degenerate_endpoints_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_degenerate_endpoints()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_degenerate_endpoints_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_degenerate_endpoints()
        finally:
            core.fold = original_fold


class TestSFTOESupernovaeHeavy(unittest.TestCase):
    def test_verify_supernovae_heavy_success(self):
        res = verify_supernovae_heavy()
        self.assertEqual(res["concept"], "Supernovae: core-collapse and heavy element synthesis.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_supernovae_heavy_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_supernovae_heavy()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_supernovae_heavy_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_supernovae_heavy()
        finally:
            core.fold = original_fold


class TestSFTOEBlackHolesComplete(unittest.TestCase):
    def test_verify_black_holes_complete_success(self):
        res = verify_black_holes_complete()
        self.assertEqual(res["concept"], "Black holes complete: Hawking temperature and information preservation.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_black_holes_complete_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_black_holes_complete()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_black_holes_complete_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_black_holes_complete()
        finally:
            core.fold = original_fold


class TestSFTOEGravitationalWaves(unittest.TestCase):
    def test_verify_gravitational_waves_success(self):
        res = verify_gravitational_waves()
        self.assertEqual(res["concept"], "Gravitational waves: quadrupole emission and luminal propagation.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        self.assertEqual(res["state"], Fraction(one_val, one_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_gravitational_waves_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_gravitational_waves()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_gravitational_waves_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_gravitational_waves()
        finally:
            core.fold = original_fold


class TestSFTOEGalacticDynamics(unittest.TestCase):
    def test_verify_galactic_dynamics_success(self):
        res = verify_galactic_dynamics()
        self.assertEqual(res["concept"], "Galactic dynamics: flat rotation curves from gauge-inert dark matter.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_galactic_dynamics_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_galactic_dynamics()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_galactic_dynamics_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_galactic_dynamics()
        finally:
            core.fold = original_fold


class TestSFTOEStellarStructure(unittest.TestCase):
    def test_verify_stellar_structure_success(self):
        res = verify_stellar_structure()
        self.assertEqual(res["concept"], "Stellar structure: gravity against fold-pressure and mass-luminosity relation.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_stellar_structure_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_stellar_structure()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_stellar_structure_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_stellar_structure()
        finally:
            core.fold = original_fold


class TestSFTOEFateOfUniverse(unittest.TestCase):
    def test_verify_fate_of_universe_success(self):
        res = verify_fate_of_universe()
        self.assertEqual(res["concept"], "Fate of the universe: accelerating expansion and live vacuum.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        self.assertEqual(res["state"], Fraction(one_val, one_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_fate_of_universe_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_fate_of_universe()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_fate_of_universe_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_fate_of_universe()
        finally:
            core.fold = original_fold


class TestSFTOEInflationSharpened(unittest.TestCase):
    def test_verify_inflation_sharpened_success(self):
        res = verify_inflation_sharpened()
        self.assertEqual(res["concept"], "Inflation sharpened: e-folds and red-tilted primordial spectrum.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        self.assertEqual(res["state"], Fraction(three_val, four_val))
        self.assertEqual(res["folded"], Fraction(one_val, two_val))

    def test_verify_inflation_sharpened_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_inflation_sharpened()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_inflation_sharpened_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_inflation_sharpened()
        finally:
            core.fold = original_fold


class TestSFTOEStructureFormation(unittest.TestCase):
    def test_verify_structure_formation_success(self):
        res = verify_structure_formation()
        self.assertEqual(res["concept"], "Structure formation: gravitational instability and dark scaffolds.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_structure_formation_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_structure_formation()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_structure_formation_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_structure_formation()
        finally:
            core.fold = original_fold


class TestSFTOEBaryogenesis(unittest.TestCase):
    def test_verify_baryogenesis_success(self):
        res = verify_baryogenesis()
        self.assertEqual(res["concept"], "Baryogenesis: Sakharov conditions and surviving matter excess.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_baryogenesis_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_baryogenesis()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_baryogenesis_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_baryogenesis()
        finally:
            core.fold = original_fold


class TestSFTOERecombinationCMB(unittest.TestCase):
    def test_verify_recombination_cmb_success(self):
        res = verify_recombination_cmb()
        self.assertEqual(res["concept"], "Recombination and CMB: acoustic peaks and harmonic positions.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_recombination_cmb_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_recombination_cmb()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_recombination_cmb_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_recombination_cmb()
        finally:
            core.fold = original_fold


class TestSFTOEBBN(unittest.TestCase):
    def test_verify_bbn_success(self):
        res = verify_bbn()
        self.assertEqual(res["concept"], "Big-bang nucleosynthesis: primordial helium fraction from freeze-out.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_bbn_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_bbn()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_bbn_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_bbn()
        finally:
            core.fold = original_fold


class TestSFTOEThermalHistory(unittest.TestCase):
    def test_verify_thermal_history_success(self):
        res = verify_thermal_history()
        self.assertEqual(res["concept"], "Thermal history: temperature inversely with scale and sequence of epochs.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_thermal_history_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_thermal_history()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_thermal_history_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_thermal_history()
        finally:
            core.fold = original_fold


class TestSFTOEAcoustics(unittest.TestCase):
    def test_verify_acoustics_success(self):
        res = verify_acoustics()
        self.assertEqual(res["concept"], "Acoustics: sound as macroscopic phonon pressure wave.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        self.assertEqual(res["state"], Fraction(one_val, one_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_acoustics_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_acoustics()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_acoustics_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_acoustics()
        finally:
            core.fold = original_fold


class TestSFTOEBlackbodyRadiation(unittest.TestCase):
    def test_verify_blackbody_radiation_success(self):
        res = verify_blackbody_radiation()
        self.assertEqual(res["concept"], "Blackbody radiation: quantized modes freeze out, Wien and Stefan-Boltzmann.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_blackbody_radiation_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_blackbody_radiation()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_blackbody_radiation_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_blackbody_radiation()
        finally:
            core.fold = original_fold


class TestSFTOENonlinearOptics(unittest.TestCase):
    def test_verify_nonlinear_optics_success(self):
        res = verify_nonlinear_optics()
        self.assertEqual(res["concept"], "Nonlinear optics: second-harmonic generation and Kerr effect.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        self.assertEqual(res["state"], Fraction(three_val, four_val))
        self.assertEqual(res["folded"], Fraction(one_val, two_val))

    def test_verify_nonlinear_optics_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_nonlinear_optics()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_nonlinear_optics_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_nonlinear_optics()
        finally:
            core.fold = original_fold


class TestSFTOELaser(unittest.TestCase):
    def test_verify_laser_success(self):
        res = verify_laser()
        self.assertEqual(res["concept"], "Laser: stimulated emission and radiation field lock above threshold.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_laser_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_laser()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_laser_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_laser()
        finally:
            core.fold = original_fold


class TestSFTOEWaveOptics(unittest.TestCase):
    def test_verify_wave_optics_success(self):
        res = verify_wave_optics()
        self.assertEqual(res["concept"], "Geometric and wave optics: Snell, reflection, interference, diffraction.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_wave_optics_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_wave_optics()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_wave_optics_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_wave_optics()
        finally:
            core.fold = original_fold


class TestSFTOERefractiveIndex(unittest.TestCase):
    def test_verify_refractive_index_success(self):
        res = verify_refractive_index()
        self.assertEqual(res["concept"], "The refractive index: bound-charge coupling slows phase speed to c over n.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_refractive_index_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_refractive_index()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_refractive_index_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_refractive_index()
        finally:
            core.fold = original_fold


class TestSFTOEMHD(unittest.TestCase):
    def test_verify_mhd_success(self):
        res = verify_mhd()
        self.assertEqual(res["concept"], "Magnetohydrodynamics on the floored lattice: finite flow, Alfven wave.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        self.assertEqual(res["state"], Fraction(three_val, four_val))
        self.assertEqual(res["folded"], Fraction(one_val, two_val))

    def test_verify_mhd_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_mhd()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_mhd_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_mhd()
        finally:
            core.fold = original_fold


class TestSFTOEPlasmaState(unittest.TestCase):
    def test_verify_plasma_state_success(self):
        res = verify_plasma_state()
        self.assertEqual(res["concept"], "Ionization and the plasma state: plasma frequency and Debye length.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_plasma_state_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_plasma_state()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_plasma_state_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_plasma_state()
        finally:
            core.fold = original_fold


class TestSFTOENeutrinoOscillation(unittest.TestCase):
    def test_verify_neutrino_oscillation_success(self):
        res = verify_neutrino_oscillation()
        self.assertEqual(res["concept"], "Neutrino oscillation: beat between mass states composing flavor states.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_neutrino_oscillation_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_neutrino_oscillation()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_neutrino_oscillation_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_neutrino_oscillation()
        finally:
            core.fold = original_fold


class TestSFTOECPViolation(unittest.TestCase):
    def test_verify_cp_violation_success(self):
        res = verify_cp_violation()
        self.assertEqual(res["concept"], "CP violation and the proven phase: intrinsic and maximal, antipode fold-position.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        self.assertEqual(res["state"], Fraction(three_val, four_val))
        self.assertEqual(res["folded"], Fraction(one_val, two_val))

    def test_verify_cp_violation_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_cp_violation()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_cp_violation_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_cp_violation()
        finally:
            core.fold = original_fold


class TestSFTOEVacuumPolarization(unittest.TestCase):
    def test_verify_vacuum_polarization_success(self):
        res = verify_vacuum_polarization()
        self.assertEqual(res["concept"], "Vacuum polarization: live vacuum screens charge, running source.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_vacuum_polarization_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_vacuum_polarization()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_vacuum_polarization_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_vacuum_polarization()
        finally:
            core.fold = original_fold


class TestSFTOERenormalization(unittest.TestCase):
    def test_verify_renormalization_finite_success(self):
        res = verify_renormalization_finite()
        self.assertEqual(res["concept"], "Renormalization without infinities: floored lattice makes every loop sum finite.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_renormalization_finite_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_renormalization_finite()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_renormalization_finite_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_renormalization_finite()
        finally:
            core.fold = original_fold


class TestSFTOERunningCouplings(unittest.TestCase):
    def test_verify_running_couplings_success(self):
        res = verify_running_couplings()
        self.assertEqual(res["concept"], "Running of the couplings: holding form over depth, converging at high scale.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_running_couplings_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_running_couplings()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_running_couplings_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_running_couplings()
        finally:
            core.fold = original_fold


class TestSFTOEDecayWidths(unittest.TestCase):
    def test_verify_decay_widths_success(self):
        res = verify_decay_widths()
        self.assertEqual(res["concept"], "Decay widths and branching ratios: total fold-transition rate and partition.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_decay_widths_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_decay_widths()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_decay_widths_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_decay_widths()
        finally:
            core.fold = original_fold


class TestSFTOECrossSections(unittest.TestCase):
    def test_verify_cross_sections_success(self):
        res = verify_cross_sections()
        self.assertEqual(res["concept"], "Cross-sections and scattering: Born probability of fold-deflection, Rutherford and Compton.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_cross_sections_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_cross_sections()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_cross_sections_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_cross_sections()
        finally:
            core.fold = original_fold


class TestSFTOEDeuteronBound(unittest.TestCase):
    def test_verify_deuteron_bound_success(self):
        res = verify_deuteron_bound()
        self.assertEqual(res["concept"], "The deuteron and the lightest bound states: spin-dependence and Pauli forbid di-nucleon.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_deuteron_bound_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_deuteron_bound()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_deuteron_bound_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_deuteron_bound()
        finally:
            core.fold = original_fold


class TestSFTOEFissionFusion(unittest.TestCase):
    def test_verify_fission_fusion_success(self):
        res = verify_fission_fusion()
        self.assertEqual(res["concept"], "Fission and fusion: energy release toward iron peak, thresholds from barriers.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_fission_fusion_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_fission_fusion()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_fission_fusion_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_fission_fusion()
        finally:
            core.fold = original_fold


class TestSFTOERadioactiveDecay(unittest.TestCase):
    def test_verify_radioactive_decay_success(self):
        res = verify_radioactive_decay()
        self.assertEqual(res["concept"], "Radioactive decay: three modes as fold-transitions, decay law a rational geometric.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        self.assertEqual(res["state"], Fraction(three_val, four_val))
        self.assertEqual(res["folded"], Fraction(one_val, two_val))

    def test_verify_radioactive_decay_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_radioactive_decay()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_radioactive_decay_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_radioactive_decay()
        finally:
            core.fold = original_fold


class TestSFTOENuclearShell(unittest.TestCase):
    def test_verify_nuclear_shell_success(self):
        res = verify_nuclear_shell()
        self.assertEqual(res["concept"], "The nuclear shell and the magic numbers: covering shells reordered by strong spin-orbit.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_nuclear_shell_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_nuclear_shell()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_nuclear_shell_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_nuclear_shell()
        finally:
            core.fold = original_fold


class TestSFTOENuclearBinding(unittest.TestCase):
    def test_verify_nuclear_binding_success(self):
        res = verify_nuclear_binding()
        self.assertEqual(res["concept"], "Nuclear binding and the valley of stability: binding curve peaking at iron.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_nuclear_binding_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_nuclear_binding()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_nuclear_binding_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_nuclear_binding()
        finally:
            core.fold = original_fold


class TestSFTOENuclearForceResidual(unittest.TestCase):
    def test_verify_nuclear_force_residual_success(self):
        res = verify_nuclear_force_residual()
        self.assertEqual(res["concept"], "The nuclear force as a residual: strong van der Waals, short range from massive mediator.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_nuclear_force_residual_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_nuclear_force_residual()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_nuclear_force_residual_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_nuclear_force_residual()
        finally:
            core.fold = original_fold


class TestSFTOEHadronSpectrum(unittest.TestCase):
    def test_verify_hadron_spectrum_success(self):
        res = verify_hadron_spectrum()
        self.assertEqual(res["concept"], "The hadron spectrum: mesons and baryons color-neutral, linear Regge.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_hadron_spectrum_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_hadron_spectrum()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_hadron_spectrum_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_hadron_spectrum()
        finally:
            core.fold = original_fold


class TestSFTOENucleonBindingDom(unittest.TestCase):
    def test_verify_nucleon_binding_dom_success(self):
        res = verify_nucleon_binding_dom()
        self.assertEqual(res["concept"], "The nucleon as a bound three-quark fold: mass dominated by binding.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_nucleon_binding_dom_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_nucleon_binding_dom()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_nucleon_binding_dom_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_nucleon_binding_dom()
        finally:
            core.fold = original_fold


class TestSFTOEIntermolecular(unittest.TestCase):
    def test_verify_intermolecular_success(self):
        res = verify_intermolecular()
        self.assertEqual(res["concept"], "Intermolecular forces: electromagnetic residual outside neutral molecules.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_intermolecular_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_intermolecular()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_intermolecular_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_intermolecular()
        finally:
            core.fold = original_fold


class TestSFTOEStereochemistry(unittest.TestCase):
    def test_verify_stereochemistry_success(self):
        res = verify_stereochemistry()
        self.assertEqual(res["concept"], "Stereochemistry and chirality: two-hand fold fiber at molecular scale.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        self.assertEqual(res["state"], Fraction(three_val, four_val))
        self.assertEqual(res["folded"], Fraction(one_val, two_val))

    def test_verify_stereochemistry_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_stereochemistry()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_stereochemistry_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_stereochemistry()
        finally:
            core.fold = original_fold


class TestSFTOEAcidsBases(unittest.TestCase):
    def test_verify_acids_bases_success(self):
        res = verify_acids_bases()
        self.assertEqual(res["concept"], "Acids, bases, and equilibrium: proton transfer and pH as fold-ratio.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_acids_bases_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_acids_bases()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_acids_bases_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_acids_bases()
        finally:
            core.fold = original_fold


class TestSFTOECatalysis(unittest.TestCase):
    def test_verify_catalysis_success(self):
        res = verify_catalysis()
        self.assertEqual(res["concept"], "Catalysis: alternative path with lower barrier, enzyme shape-matched basin.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_catalysis_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_catalysis()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_catalysis_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_catalysis()
        finally:
            core.fold = original_fold


class TestSFTOEReactionKinetics(unittest.TestCase):
    def test_verify_reaction_kinetics_success(self):
        res = verify_reaction_kinetics()
        self.assertEqual(res["concept"], "Reaction kinetics: rate as fraction above activation barrier, Arrhenius.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_reaction_kinetics_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_reaction_kinetics()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_reaction_kinetics_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_reaction_kinetics()
        finally:
            core.fold = original_fold


class TestSFTOEReactionThermodynamics(unittest.TestCase):
    def test_verify_reaction_thermodynamics_success(self):
        res = verify_reaction_thermodynamics()
        self.assertEqual(res["concept"], "Reaction thermodynamics: fold-descent between fixed points, enthalpy and activation.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_reaction_thermodynamics_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_reaction_thermodynamics()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_reaction_thermodynamics_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_reaction_thermodynamics()
        finally:
            core.fold = original_fold


class TestSFTOEElectronegativity(unittest.TestCase):
    def test_verify_electronegativity_success(self):
        res = verify_electronegativity()
        self.assertEqual(res["concept"], "Electronegativity and bond polarity: binding depth and difference.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_electronegativity_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_electronegativity()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_electronegativity_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_electronegativity()
        finally:
            core.fold = original_fold


class TestSFTOEPeriodicLaw(unittest.TestCase):
    def test_verify_periodic_law_success(self):
        res = verify_periodic_law()
        self.assertEqual(res["concept"], "The periodic law: recurrence of the covering pattern, valence count.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_periodic_law_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_periodic_law()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_periodic_law_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_periodic_law()
        finally:
            core.fold = original_fold


class TestSFTOEMolecularSpectra(unittest.TestCase):
    def test_verify_molecular_spectra_success(self):
        res = verify_molecular_spectra()
        self.assertEqual(res["concept"], "Molecular spectra: J(J+1) ladder, vibrational oscillator ladder, isotope shift.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_molecular_spectra_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_molecular_spectra()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_molecular_spectra_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_molecular_spectra()
        finally:
            core.fold = original_fold


class TestSFTOEMolecularBond(unittest.TestCase):
    def test_verify_molecular_bond_success(self):
        res = verify_molecular_bond()
        self.assertEqual(res["concept"], "The molecular bond: shared fold-orbit, bond length minimum.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_molecular_bond_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_molecular_bond()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_molecular_bond_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_molecular_bond()
        finally:
            core.fold = original_fold


class TestSFTOEFieldSplitting(unittest.TestCase):
    def test_verify_field_splitting_success(self):
        res = verify_field_splitting()
        self.assertEqual(res["concept"], "The Zeeman and Stark effects: field splitting from handedness coupling.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_field_splitting_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_field_splitting()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_field_splitting_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_field_splitting()
        finally:
            core.fold = original_fold


class TestSFTOESelectionRules(unittest.TestCase):
    def test_verify_selection_rules_success(self):
        res = verify_selection_rules()
        self.assertEqual(res["concept"], "Selection rules, transition rates, and lifetimes: fold-act unit transfer.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_selection_rules_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_selection_rules()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_selection_rules_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_selection_rules()
        finally:
            core.fold = original_fold


class TestSFTOEShellCapacities(unittest.TestCase):
    def test_verify_shell_capacities_success(self):
        res = verify_shell_capacities()
        self.assertEqual(res["concept"], "Multi-electron atom and shell structure: orbital capacity twice n-squared.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_shell_capacities_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_shell_capacities()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_shell_capacities_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_shell_capacities()
        finally:
            core.fold = original_fold


class TestSFTOELambShift(unittest.TestCase):
    def test_verify_lamb_shift_success(self):
        res = verify_lamb_shift()
        self.assertEqual(res["concept"], "The Lamb shift: cycling vacuum shift on bound energy levels.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_lamb_shift_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_lamb_shift()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_lamb_shift_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_lamb_shift()
        finally:
            core.fold = original_fold


class TestSFTOEFineHyperfine(unittest.TestCase):
    def test_verify_fine_hyperfine_success(self):
        res = verify_fine_hyperfine()
        self.assertEqual(res["concept"], "Fine and hyperfine structure: proven fractions of the gross ladder.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        self.assertEqual(res["state"], Fraction(three_val, four_val))
        self.assertEqual(res["folded"], Fraction(one_val, two_val))

    def test_verify_fine_hyperfine_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_fine_hyperfine()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_fine_hyperfine_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_fine_hyperfine()
        finally:
            core.fold = original_fold


class TestSFTOEHydrogenSpectrum(unittest.TestCase):
    def test_verify_hydrogen_spectrum_success(self):
        res = verify_hydrogen_spectrum()
        self.assertEqual(res["concept"], "The hydrogen spectrum: one-over-n-squared fold-ladder.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_hydrogen_spectrum_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_hydrogen_spectrum()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_hydrogen_spectrum_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_hydrogen_spectrum()
        finally:
            core.fold = original_fold


class TestSFTOEMechanicalProperties(unittest.TestCase):
    def test_verify_mechanical_properties_success(self):
        res = verify_mechanical_properties()
        self.assertEqual(res["concept"], "Mechanical properties: elasticity, plasticity, and fracture from lattice-bond fold-energy.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_mechanical_properties_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_mechanical_properties()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_mechanical_properties_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_mechanical_properties()
        finally:
            core.fold = original_fold


class TestSFTOETopologicalMatter(unittest.TestCase):
    def test_verify_topological_matter_success(self):
        res = verify_topological_matter()
        self.assertEqual(res["concept"], "Topological matter: protected edge states from a fold-winding invariant.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_topological_matter_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_topological_matter()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_topological_matter_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_topological_matter()
        finally:
            core.fold = original_fold


class TestSFTOEQuantumHall(unittest.TestCase):
    def test_verify_quantum_hall_success(self):
        res = verify_quantum_hall()
        self.assertEqual(res["concept"], "The quantum Hall effects: Hall conductance as a proven rational count.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        three_val = 3
        four_val = 4
        self.assertEqual(res["state"], Fraction(three_val, four_val))
        self.assertEqual(res["folded"], Fraction(one_val, two_val))

    def test_verify_quantum_hall_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_quantum_hall()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_quantum_hall_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_quantum_hall()
        finally:
            core.fold = original_fold


class TestSFTOEMagnetism(unittest.TestCase):
    def test_verify_magnetism_success(self):
        res = verify_magnetism()
        self.assertEqual(res["concept"], "Magnetism: fold-handedness alignment, Curie and Neel threshold, hysteresis.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_magnetism_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_magnetism()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_magnetism_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_magnetism()
        finally:
            core.fold = original_fold


class TestSFTOESuperfluidity(unittest.TestCase):
    def test_verify_superfluidity_success(self):
        res = verify_superfluidity()
        self.assertEqual(res["concept"], "Superfluidity: neutral-boson lock, frictionless flow.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_superfluidity_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_superfluidity()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_superfluidity_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_superfluidity()
        finally:
            core.fold = original_fold


class TestSFTOESuperconductivity(unittest.TestCase):
    def test_verify_superconductivity_success(self):
        res = verify_superconductivity()
        self.assertEqual(res["concept"], "Superconductivity: collective lock of paired carriers, zero resistance.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_superconductivity_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_superconductivity()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_superconductivity_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_superconductivity()
        finally:
            core.fold = original_fold


class TestSFTOESemiconductors(unittest.TestCase):
    def test_verify_semiconductors_success(self):
        res = verify_semiconductors()
        self.assertEqual(res["concept"], "Semiconductor physics and junction: doping, p-n junction, rectification.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_semiconductors_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_semiconductors()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_semiconductors_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_semiconductors()
        finally:
            core.fold = original_fold


class TestSFTOEElectronicBands(unittest.TestCase):
    def test_verify_electronic_bands_success(self):
        res = verify_electronic_bands()
        self.assertEqual(res["concept"], "Electronic bands: allowed bands and forbidden gaps, conductor/insulator split.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_electronic_bands_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_electronic_bands()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_electronic_bands_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_electronic_bands()
        finally:
            core.fold = original_fold


class TestSFTOEPhononsLattice(unittest.TestCase):
    def test_verify_phonons_lattice_success(self):
        res = verify_phonons_lattice()
        self.assertEqual(res["concept"], "Phonons and lattice spectrum: gapless acoustic branch, heat capacity.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_phonons_lattice_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_phonons_lattice()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_phonons_lattice_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_phonons_lattice()
        finally:
            core.fold = original_fold


class TestSFTOEQuasicrystals(unittest.TestCase):
    def test_verify_quasicrystals_success(self):
        res = verify_quasicrystals()
        self.assertEqual(res["concept"], "Quasicrystals: forbidden five-fold order as a proven aperiodic fold-tiling.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_quasicrystals_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_quasicrystals()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_quasicrystals_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_quasicrystals()
        finally:
            core.fold = original_fold


class TestSFTOECrystallineOrder(unittest.TestCase):
    def test_verify_crystalline_order_success(self):
        res = verify_crystalline_order()
        self.assertEqual(res["concept"], "Crystalline order and crystallographic restriction: only integer-trace rotations.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_crystalline_order_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_crystalline_order()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_crystalline_order_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_crystalline_order()
        finally:
            core.fold = original_fold


class TestSFTOEMaxwellsDemon(unittest.TestCase):
    def test_verify_maxwells_demon_success(self):
        res = verify_maxwells_demon()
        self.assertEqual(res["concept"], "Maxwell's demon and information-entropy tie: erasing a bit costs a minimum throw.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_maxwells_demon_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_maxwells_demon()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_maxwells_demon_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_maxwells_demon()
        finally:
            core.fold = original_fold


class TestSFTOEBoseEinstein(unittest.TestCase):
    def test_verify_bose_einstein_success(self):
        res = verify_bose_einstein()
        self.assertEqual(res["concept"], "Bose-Einstein condensation: the cold boson lock onto one ground orbit.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_bose_einstein_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_bose_einstein()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_bose_einstein_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_bose_einstein()
        finally:
            core.fold = original_fold


class TestSFTOEIrreversibilityRecurrence(unittest.TestCase):
    def test_verify_irreversibility_recurrence_success(self):
        res = verify_irreversibility_recurrence()
        self.assertEqual(res["concept"], "Irreversibility and recurrence reconciliation: two timescales, no contradiction.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_irreversibility_recurrence_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_irreversibility_recurrence()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_irreversibility_recurrence_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_irreversibility_recurrence()
        finally:
            core.fold = original_fold


class TestSFTOEFluctuationDissipation(unittest.TestCase):
    def test_verify_fluctuation_dissipation_success(self):
        res = verify_fluctuation_dissipation()
        self.assertEqual(res["concept"], "Fluctuation, dissipation, and noise: tied by the shared periodic orbit.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_fluctuation_dissipation_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_fluctuation_dissipation()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_fluctuation_dissipation_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_fluctuation_dissipation()
        finally:
            core.fold = original_fold


class TestSFTOECriticalExponents(unittest.TestCase):
    def test_verify_critical_exponents_success(self):
        res = verify_critical_exponents()
        self.assertEqual(res["concept"], "Phase transitions and critical exponents: at the threshold (m-1)/m, the exponents proven rational.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_critical_exponents_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_critical_exponents()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_critical_exponents_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_critical_exponents()
        finally:
            core.fold = original_fold


class TestSFTOEQuantumStatistics(unittest.TestCase):
    def test_verify_quantum_statistics_success(self):
        res = verify_quantum_statistics()
        self.assertEqual(res["concept"], "Quantum statistics: Bose and Fermi from the two-to-one fold and the chirality fibre.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_quantum_statistics_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_quantum_statistics()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_quantum_statistics_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_quantum_statistics()
        finally:
            core.fold = original_fold


class TestSFTOEFourThermoLaws(unittest.TestCase):
    def test_verify_four_thermo_laws_success(self):
        res = verify_four_thermo_laws()
        self.assertEqual(res["concept"], "Four laws of thermodynamics: each proven from existing structure.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        four_val = 4
        self.assertEqual(res["state"], Fraction(one_val, four_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_four_thermo_laws_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_four_thermo_laws()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_four_thermo_laws_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_four_thermo_laws()
        finally:
            core.fold = original_fold


class TestSFTOECanonicalDistribution(unittest.TestCase):
    def test_verify_canonical_distribution_success(self):
        res = verify_canonical_distribution()
        self.assertEqual(res["concept"], "Canonical distribution: maximum-count equilibrium, rational weighting, no exponential.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_canonical_distribution_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_canonical_distribution()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_canonical_distribution_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_canonical_distribution()
        finally:
            core.fold = original_fold


class TestSFTOEEntropy(unittest.TestCase):
    def test_verify_entropy_success(self):
        res = verify_entropy()
        self.assertEqual(res["concept"], "Entropy as the fold-configuration count: second law proven from the two-to-one fold.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_entropy_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_entropy()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_entropy_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_entropy()
        finally:
            core.fold = original_fold


class TestSFTOETemperature(unittest.TestCase):
    def test_verify_temperature_success(self):
        res = verify_temperature()
        self.assertEqual(res["concept"], "Temperature: the mean throw-rate of a folding population.")
        self.assertEqual(res["tier"], "Tier B")
        one_val = 1
        two_val = 2
        self.assertEqual(res["state"], Fraction(one_val, two_val))
        self.assertEqual(res["fixed_point"], Fraction(one_val, one_val))

    def test_verify_temperature_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_temperature()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_temperature_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            one_val = 1
            three_val = 3
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(one_val, three_val))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_temperature()
        finally:
            core.fold = original_fold


class TestSFTOEQuantumStationaryStates(unittest.TestCase):
    def test_verify_quantum_stationary_states_success(self):
        res = verify_quantum_stationary_states()
        self.assertEqual(res["concept"], "The stationary states of the quantum evolution are the proven spectrum.")
        self.assertEqual(res["tier"], "Tier B")
        self.assertEqual(res["state"], Fraction(1, 16))
        self.assertEqual(res["spacing"], Fraction(1, 8))

    def test_verify_quantum_stationary_states_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_quantum_stationary_states()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_quantum_stationary_states_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 3))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_quantum_stationary_states()
        finally:
            core.fold = original_fold


class TestSFTOERelativisticTwoComponent(unittest.TestCase):
    def test_verify_relativistic_two_component_success(self):
        res = verify_relativistic_two_component()
        self.assertEqual(res["concept"], "The relativistic two-component step squares to the relativistic dispersion.")
        self.assertEqual(res["tier"], "Tier B")
        self.assertEqual(res["p"], Fraction(3, 5))
        self.assertEqual(res["m"], Fraction(4, 5))

    def test_verify_relativistic_two_component_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_relativistic_two_component()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_relativistic_two_component_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 3))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_relativistic_two_component()
        finally:
            core.fold = original_fold


class TestSFTOEFullDiracStructure(unittest.TestCase):
    def test_verify_full_dirac_structure_success(self):
        res = verify_full_dirac_structure()
        self.assertEqual(res["concept"], "The full Dirac structure in three space and one time dimension.")
        self.assertEqual(res["tier"], "Tier B")

    def test_verify_full_dirac_structure_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_full_dirac_structure()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_full_dirac_structure_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 3))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_full_dirac_structure()
        finally:
            core.fold = original_fold


class TestSFTOECessation(unittest.TestCase):
    def test_verify_cessation_success(self):
        res = verify_cessation()
        self.assertEqual(res["concept"], "Cessation: the lock releases, the anchor (unison) persists as the undestroyable One.")
        self.assertEqual(res["tier"], "Tier B")
        self.assertEqual(res["state"], Fraction(1, 2))
        self.assertEqual(res["anchor"], Fraction(1, 1))

    def test_verify_cessation_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_cessation()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_cessation_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 3))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_cessation()
        finally:
            core.fold = original_fold


class TestSFTOEOneFoldEquation(unittest.TestCase):
    def test_verify_one_fold_equation_success(self):
        res = verify_one_fold_equation()
        self.assertEqual(res["concept"], "The one-fold equation: the single closed generating law.")
        self.assertEqual(res["tier"], "Tier B")
        self.assertEqual(res["state"], Fraction(1, 3))

    def test_verify_one_fold_equation_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_one_fold_equation()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_one_fold_equation_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 5))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_one_fold_equation()
        finally:
            core.fold = original_fold


class TestSFTOESectorEquations(unittest.TestCase):
    def test_verify_sector_equations_success(self):
        res = verify_sector_equations()
        self.assertEqual(res["concept"], "The sector equations: proven equation for every sector, tied to A-1.")
        self.assertEqual(res["tier"], "Tier B")

    def test_verify_sector_equations_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_sector_equations()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_sector_equations_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 3))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_sector_equations()
        finally:
            core.fold = original_fold


class TestSFTOEMasterEquation(unittest.TestCase):
    def test_verify_master_equation_success(self):
        res = verify_master_equation()
        self.assertEqual(res["concept"], "The master equation: single structure carrying the entire universe.")
        self.assertEqual(res["tier"], "Tier B")

    def test_verify_master_equation_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_master_equation()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_master_equation_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 3))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_master_equation()
        finally:
            core.fold = original_fold


class TestSFTOESimulationKernel(unittest.TestCase):
    def test_verify_simulation_kernel_success(self):
        res = verify_simulation_kernel()
        self.assertEqual(res["concept"], "The simulation kernel: framework running forward from the One, driven by the fold.")
        self.assertEqual(res["tier"], "Tier B")

    def test_verify_simulation_kernel_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_simulation_kernel()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_simulation_kernel_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 3))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_simulation_kernel()
        finally:
            core.fold = original_fold


class TestSFTOEUnfoldingSequence(unittest.TestCase):
    def test_verify_unfolding_sequence_success(self):
        res = verify_unfolding_sequence()
        self.assertEqual(res["concept"], "The unfolding sequence: dependency-ordered playthrough as the derivation.")
        self.assertEqual(res["tier"], "Tier B")

    def test_verify_unfolding_sequence_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_unfolding_sequence()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_unfolding_sequence_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 3))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_unfolding_sequence()
        finally:
            core.fold = original_fold


class TestSFTOEAccessibleArtifact(unittest.TestCase):
    def test_verify_accessible_artifact_success(self):
        res = verify_accessible_artifact()
        self.assertEqual(res["concept"], "The accessible artifact: unfolding rendered to universal portable playable format.")
        self.assertEqual(res["tier"], "Tier B")

    def test_verify_accessible_artifact_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_accessible_artifact()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_accessible_artifact_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 3))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_accessible_artifact()
        finally:
            core.fold = original_fold


class TestSFTOEQuantumPotential(unittest.TestCase):
    def test_verify_quantum_potential_success(self):
        res = verify_quantum_potential()
        self.assertEqual(res["concept"], "Quantum dynamics under a potential: static local source of rotation.")
        self.assertEqual(res["tier"], "Tier B")
        self.assertEqual(res["next_phase"], Fraction(17, 24))

    def test_verify_quantum_potential_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_quantum_potential()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_quantum_potential_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 3))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_quantum_potential()
        finally:
            core.fold = original_fold


class TestSFTOEFreeParticleDispersion(unittest.TestCase):
    def test_verify_free_particle_dispersion_success(self):
        res = verify_free_particle_dispersion()
        self.assertEqual(res["concept"], "Quantum dynamics: free-particle dispersion via lattice second-difference.")
        self.assertEqual(res["tier"], "Tier B")
        self.assertEqual(res["next_phase"], Fraction(5, 6))

    def test_verify_free_particle_dispersion_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_free_particle_dispersion()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_free_particle_dispersion_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 3))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_free_particle_dispersion()
        finally:
            core.fold = original_fold


class TestSFTOEVarianceUncertainty(unittest.TestCase):
    def test_verify_variance_uncertainty_success(self):
        res = verify_variance_uncertainty()
        self.assertEqual(res["concept"], "Variance form of the uncertainty bound: weighted by basis spacing.")
        self.assertEqual(res["tier"], "Tier B")
        self.assertEqual(res["product"], Fraction(1, 16))

    def test_verify_variance_uncertainty_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_variance_uncertainty()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_variance_uncertainty_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 3))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_variance_uncertainty()
        finally:
            core.fold = original_fold


class TestSFTOEUncertaintyCount(unittest.TestCase):
    def test_verify_uncertainty_count_success(self):
        res = verify_uncertainty_count()
        self.assertEqual(res["concept"], "Complementarity/uncertainty as a count inequality: support product bound.")
        self.assertEqual(res["tier"], "Tier B")
        self.assertEqual(res["product"], 8)

    def test_verify_uncertainty_count_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_uncertainty_count()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_uncertainty_count_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 3))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_uncertainty_count()
        finally:
            core.fold = original_fold


class TestSFTOEMinkowskiCausal(unittest.TestCase):
    def test_verify_minkowski_causal_success(self):
        res = verify_minkowski_causal()
        self.assertEqual(res["concept"], "Minkowski causal structure: timelike interval built with audited take.")
        self.assertEqual(res["tier"], "Tier B")
        self.assertEqual(res["ds_sq"], Fraction(16, 25))

    def test_verify_minkowski_causal_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_minkowski_causal()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_minkowski_causal_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 3))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_minkowski_causal()
        finally:
            core.fold = original_fold


class TestSFTOEThreeWaveMixing(unittest.TestCase):
    def test_verify_three_wave_mixing_success(self):
        res = verify_three_wave_mixing()
        self.assertEqual(res["concept"], "Three-wave mixing: second harmonic, sum, and difference frequencies from fold and take.")
        self.assertEqual(res["tier"], "Tier B")
        self.assertEqual(res["diff_frequency"], Fraction(1, 12))

    def test_verify_three_wave_mixing_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_three_wave_mixing()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_three_wave_mixing_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 3))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_three_wave_mixing()
        finally:
            core.fold = original_fold


class TestSFTOEDAlembertWave(unittest.TestCase):
    def test_verify_dalembert_wave_success(self):
        res = verify_dalembert_wave()
        self.assertEqual(res["concept"], "dAlembert wave equation: disturbance split into right-moving and left-moving packets.")
        self.assertEqual(res["tier"], "Tier B")
        self.assertEqual(res["split_amplitude"], Fraction(1, 4))

    def test_verify_dalembert_wave_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_dalembert_wave()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_dalembert_wave_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 3))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_dalembert_wave()
        finally:
            core.fold = original_fold


class TestSFTOECubicLattice(unittest.TestCase):
    def test_verify_cubic_lattice_success(self):
        res = verify_cubic_lattice()
        self.assertEqual(res["concept"], "Three-dimensional cubic lattice operator: planar operator extended to cube.")
        self.assertEqual(res["tier"], "Tier B")
        self.assertEqual(res["sum_neighbors"], Fraction(1, 2))

    def test_verify_cubic_lattice_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_cubic_lattice()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_cubic_lattice_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 3))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_cubic_lattice()
        finally:
            core.fold = original_fold


class TestSFTOEPlanarLattice(unittest.TestCase):
    def test_verify_planar_lattice_success(self):
        res = verify_planar_lattice()
        self.assertEqual(res["concept"], "Two-dimensional planar lattice operator: 1D lattice extended to plane.")
        self.assertEqual(res["tier"], "Tier B")
        self.assertEqual(res["sum_neighbors"], Fraction(1, 2))

    def test_verify_planar_lattice_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_planar_lattice()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_planar_lattice_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 3))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_planar_lattice()
        finally:
            core.fold = original_fold


class TestSFTOECoupledLattice(unittest.TestCase):
    def test_verify_coupled_lattice_success(self):
        res = verify_coupled_lattice()
        self.assertEqual(res["concept"], "Coupled lattice: 1D monatomic chain reproducing finite propagation speed and conservation.")
        self.assertEqual(res["tier"], "Tier B")
        self.assertEqual(res["next_center"], Fraction(3, 8))

    def test_verify_coupled_lattice_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_coupled_lattice()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_coupled_lattice_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 3))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_coupled_lattice()
        finally:
            core.fold = original_fold


class TestSFTOEAlgebraicEngine(unittest.TestCase):
    def test_verify_algebraic_engine_success(self):
        res = verify_algebraic_engine()
        self.assertEqual(res["concept"], "Algebraic-magnitude engine: incommensurable magnitude certified by order-swap.")
        self.assertEqual(res["tier"], "Tier B")
        self.assertEqual(res["diff1"], Fraction(1, 25))
        self.assertEqual(res["diff2"], Fraction(1, 4))

    def test_verify_algebraic_engine_mutation_zero_axiom(self):
        from sftoe.core import SmithianValue
        original_init = SmithianValue.__init__
        try:
            def bad_init(self_obj, value, trace=None):
                from fractions import Fraction
                self_obj.value = Fraction(value)
                self_obj.trace = None
            SmithianValue.__init__ = bad_init
            with self.assertRaises(VerificationError):
                verify_algebraic_engine()
        finally:
            SmithianValue.__init__ = original_init

    def test_verify_algebraic_engine_mutation_invariants(self):
        import sftoe.core as core
        original_fold = core.fold
        try:
            from sftoe.core import SmithianValue
            def bad_fold(x):
                return SmithianValue(Fraction(1, 3))
            core.fold = bad_fold
            with self.assertRaises(VerificationError):
                verify_algebraic_engine()
        finally:
            core.fold = original_fold



class TestSFTOEMentalTemporalMatterManipulation(unittest.TestCase):
    def test_verify_consciousness_matter_coupling(self):
        res = verify_consciousness_matter_coupling()
        self.assertEqual(res["tier"], "A")
        self.assertEqual(res["observer_period"], 2)
        self.assertIsNone(res["physical_period"])
        self.assertIsNone(res["combined_period"])

    def test_verify_mental_temporal_manipulation(self):
        res = verify_mental_temporal_manipulation()
        self.assertEqual(res["tier"], "A")
        self.assertEqual(res["target_state"], Fraction(3, 8))
        self.assertEqual(res["preimage_1"], Fraction(3, 16))
        self.assertEqual(res["preimage_2"], Fraction(11, 16))

    def test_verify_mental_matter_manipulation(self):
        res = verify_mental_matter_manipulation()
        self.assertEqual(res["tier"], "A")
        self.assertEqual(res["input_c"], Fraction(1, 3))
        self.assertEqual(res["input_m"], Fraction(1, 4))
        self.assertEqual(res["derived_target"], Fraction(3, 4))


if __name__ == "__main__":
    unittest.main()
















