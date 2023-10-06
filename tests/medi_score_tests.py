import unittest
from medi_score.medi_score import medi_score_calculation
from medi_score.helpers import get_air_or_oxygen_score
from medi_score.Enums import AirOrOxygen

#                                    -- medi_score_calculation tests --
class MediScoreCalculationTest(unittest.TestCase):
    """ Test module for medi_score_calculation function """

    def test_returns_medi_score(self):
         result = medi_score_calculation()
         self.assertEqual(result, 'medi score')


#                                    -- helper function - get_air_or_oxygen_score tests --
class AirOrOxygenTest(unittest.TestCase):
    """ Test module for get_air_or_oxygen_score function """
    
    def test_get_air_or_oxygen_score_returns_false_if_passed_string_value(self):
        """ Confirm get_air_or_oxygen_score returns False if a string is passed """
        result = get_air_or_oxygen_score('nonsense')
        self.assertFalse(False)
    
    def test_get_air_or_oxygen_score_returns_false_if_incorrect_passed_value(self):
        """ Confirm get_air_or_oxygen_score returns False if a incorrect value is passed """
        result = get_air_or_oxygen_score(7)
        self.assertFalse(False)

    def test_get_air_or_oxygen_score_returns_correct_score(self):
        """ Confirm get_air_or_oxygen_score returns correct score when passed 'AIR' or 'OXYGEN' """
        air_result = get_air_or_oxygen_score(AirOrOxygen.AIR.value)
        self.assertEqual(air_result, 0)
        oxygen_result = get_air_or_oxygen_score(AirOrOxygen.OXYGEN.value)
        self.assertEqual(oxygen_result, 2)


if __name__ == '__main__':
    unittest.main()