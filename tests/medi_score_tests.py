import unittest
from medi_score.medi_score import medi_score_calculation

class TestClass(unittest.TestCase):
    def test_returns_medi_score(self):
         result = medi_score_calculation()
         self.assertEqual(result, 'medi score')

if __name__ == '__main__':
    unittest.main()