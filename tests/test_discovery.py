import unittest
from fractions import Fraction
import sys

from sftoe.discovery import (
    approximate_ratio,
    approximate_interval,
    find_derivation,
    find_integer_relation_lll,
    generate_sftoe_code,
    query
)
from sftoe.gate import verify_code
from sftoe.proof import verify_value

class TestSFTOMathDiscovery(unittest.TestCase):
    def test_approximate_ratio(self):
        self.assertEqual(approximate_ratio(0.666667, 1e-5), Fraction(2, 3))
        self.assertEqual(approximate_ratio(0.5, 1e-6), Fraction(1, 2))
        self.assertEqual(approximate_ratio(0.1666667, 1e-5), Fraction(1, 6))

    def test_approximate_interval(self):
        # 1/6 is approximately 0.166666...
        # The simplest fraction in (0.15, 0.18) is 1/6
        self.assertEqual(approximate_interval(0.15, 0.18), Fraction(1, 6))
        # The simplest fraction in (0.3, 0.4) is 1/3
        self.assertEqual(approximate_interval(0.3, 0.4), Fraction(1, 3))

    def test_find_derivation_strong_coupling(self):
        # SADE should find the strong coupling constant (2/3)
        proof_node = find_derivation(Fraction(2, 3), max_depth=4)
        self.assertIsNotNone(proof_node)
        
        # Check generated code compliance
        code = generate_sftoe_code(proof_node, "verify_strong_coupling")
        self.assertTrue(verify_code(code))
        
        # Execute the generated code
        namespace = {}
        exec(code, namespace)
        res_val = namespace["verify_strong_coupling"]()
        
        self.assertEqual(res_val.value, Fraction(2, 3))
        self.assertTrue(verify_value(res_val))

    def test_find_derivation_lepton_preimage(self):
        # 1/6 is the electron mass shortfall preimage.
        proof_node = find_derivation(Fraction(1, 6), max_depth=4)
        self.assertIsNotNone(proof_node)
        
        # Check generated code compliance
        code = generate_sftoe_code(proof_node, "verify_electron_preimage")
        self.assertTrue(verify_code(code))
        
        # Execute the generated code
        namespace = {}
        exec(code, namespace)
        res_val = namespace["verify_electron_preimage"]()
        
        self.assertEqual(res_val.value, Fraction(1, 6))
        self.assertTrue(verify_value(res_val))

    def test_find_integer_relation_lll(self):
        # 1/6, 1/2, 5/6 sum to 3/2
        vals = [Fraction(1, 6), Fraction(1, 2), Fraction(5, 6)]
        relation = find_integer_relation_lll(vals)
        self.assertIsNotNone(relation)
        
        coeffs = relation["coefficients"]
        const = relation["constant"]
        
        computed_sum = sum(c * v for c, v in zip(coeffs, vals))
        self.assertEqual(computed_sum, const)

    def test_query_interface(self):
        # Test query by target float
        res1 = query(target_float=0.166667, tolerance=1e-5)
        self.assertEqual(res1["fraction"], Fraction(1, 6))
        self.assertTrue(verify_code(res1["code"]))
        
        # Test query by interval
        res2 = query(interval=(0.3, 0.4))
        self.assertEqual(res2["fraction"], Fraction(1, 3))
        self.assertTrue(verify_code(res2["code"]))
