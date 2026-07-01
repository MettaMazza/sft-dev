"""Machine-checks for the three frontier forced results:
  - new_force_running : the new forces run and all four converge to unison
  - dark_ckm          : the dark-sector mixing matrix
  - dark_baryon       : the colour-singlet rule and the dark baryon
Each engine computes Route A (forward from the fold mechanism) and Route B (the closed
form) and raises on any mismatch. These tests assert the forced values, that each
reproduces the known Standard-Model sector as its anchor, and that the internal forcing
checks are load-bearing (mutation raises).
"""
import unittest
from fractions import Fraction

from sftoe.proof import VerificationError
import new_force_running as nfr
import dark_ckm
import dark_baryon


class TestNewForceRunning(unittest.TestCase):
    def test_verify_runs_and_forces_unison(self):
        r = nfr.verify()
        self.assertTrue(r["all_forces_converge_to_unison"])

    def test_reproduces_corpus_strong_ew_gap(self):
        # anchor: the corpus's proven gap 1/((2+R)(3+R))
        for d in range(0, 11):
            R = 2 ** d
            self.assertEqual(nfr.forced_gap(2, 3, d), Fraction(1, (2 + R) * (3 + R)))

    def test_new_force_gap_g7_g5(self):
        for d in range(0, 11):
            R = 2 ** d
            self.assertEqual(nfr.forced_gap(5, 7, d), Fraction(2, (5 + R) * (7 + R)))

    def test_general_closed_form_all_pairs(self):
        for d in range(0, 6):
            R = 2 ** d
            for i, j in [(2, 3), (3, 5), (5, 7), (2, 5), (3, 7), (2, 7)]:
                self.assertEqual(nfr.forced_gap(i, j, d), Fraction(j - i, (i + R) * (j + R)))

    def test_mutation_ordering_guard_raises(self):
        # a gap with j <= i must raise (the ordering guard is load-bearing)
        with self.assertRaises(VerificationError):
            nfr.forced_gap(3, 2, 0)

    def test_couplings_below_unison_and_rising(self):
        for p in nfr.SECTORS:
            self.assertLess(nfr.running_coupling(p, 0).value, Fraction(1, 1))
            self.assertGreater(
                nfr.running_coupling(p, 5).value, nfr.running_coupling(p, 0).value)


class TestDarkCKM(unittest.TestCase):
    def test_verify_runs(self):
        r = dark_ckm.verify()
        self.assertEqual(r["leakage_shrinks_as"], "1/(3p)")

    def test_reproduces_corpus_quark_values(self):
        self.assertEqual(dark_ckm.forced_ckm(3), (Fraction(8, 9), Fraction(5, 9)))

    def test_new_dark_diagonals(self):
        self.assertEqual(dark_ckm.forced_ckm(5)[0], Fraction(14, 15))
        self.assertEqual(dark_ckm.forced_ckm(7)[0], Fraction(20, 21))

    def test_diagonal_closed_form(self):
        for p in (3, 5, 7):
            self.assertEqual(dark_ckm.forced_ckm(p)[0], Fraction(3 * p - 1, 3 * p))

    def test_near_diagonal_property(self):
        for p in (3, 5, 7):
            diag, v12 = dark_ckm.forced_ckm(p)
            self.assertGreater(diag, v12)


class TestDarkBaryon(unittest.TestCase):
    def test_verify_runs(self):
        r = dark_baryon.verify()
        self.assertEqual(r["baryon_multiplicity"], {3: 3, 5: 5, 7: 7})
        self.assertEqual(r["meson_multiplicity"], {3: 2, 5: 2, 7: 2})

    def test_reproduces_standard_model_p3(self):
        self.assertEqual(dark_baryon.baryon_multiplicity(3), 3)   # 3-quark nucleon
        self.assertEqual(dark_baryon.meson_multiplicity(3), 2)    # 2-quark pion

    def test_new_dark_baryons(self):
        self.assertEqual(dark_baryon.baryon_multiplicity(5), 5)   # penta-baryon
        self.assertEqual(dark_baryon.baryon_multiplicity(7), 7)   # hepta-baryon

    def test_complete_fibre_folds_to_unison(self):
        for p in (3, 5, 7):
            fibre = dark_baryon.colour_fibre(p)
            self.assertEqual(len(fibre), p)

    def test_mutation_even_sector_not_neutral_raises(self):
        # an even colour count is not colour-neutral (charge sum not whole) -> must raise
        with self.assertRaises(VerificationError):
            dark_baryon.baryon_multiplicity(4)


if __name__ == "__main__":
    unittest.main()
