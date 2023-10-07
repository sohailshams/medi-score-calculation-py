import unittest
from medi_score.medi_score import medi_score_calculation
from medi_score.helpers import get_air_or_oxygen_score, get_consciousness_score, get_respiration_range_score, get_spo2_score
from medi_score.Enums import AirOrOxygen, Consciousness

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
        self.assertFalse(result)
    
    def test_get_air_or_oxygen_score_returns_false_if_incorrect_passed_value(self):
        """ Confirm get_air_or_oxygen_score returns False if a incorrect value is passed """
        result = get_air_or_oxygen_score(7)
        self.assertFalse(result)

    def test_get_air_or_oxygen_score_returns_correct_score(self):
        """ Confirm get_air_or_oxygen_score returns correct score when passed 'AIR' or 'OXYGEN' """
        air_result = get_air_or_oxygen_score(AirOrOxygen.AIR.value)
        self.assertEqual(air_result, 0)
        oxygen_result = get_air_or_oxygen_score(AirOrOxygen.OXYGEN.value)
        self.assertEqual(oxygen_result, 2)


#                                    -- helper function - get_consciousness_score tests --
class ConsciousnessTest(unittest.TestCase):
    """ Test module for get_consciousness_score function """
    
    def test_get_consciousness_score_returns_false_if_passed_string_value(self):
        """ Confirm get_consciousness_score returns False if a string is passed """
        result = get_consciousness_score('nonsense')
        self.assertFalse(result)
    
    def test_get_consciousness_score_returns_false_if_incorrect_passed_value(self):
        """ Confirm get_consciousness_score returns False if a incorrect value is passed """
        result = get_consciousness_score(7)
        self.assertFalse(result)

    def test_get_consciousness_score_returns_correct_score(self):
        """ Confirm get_consciousness_score returns correct score when passed 'AIR' or 'OXYGEN' """
        alert_result = get_consciousness_score(Consciousness.ALERT.value)
        self.assertEqual(alert_result, 0)
        cvpu_result = get_consciousness_score(Consciousness.CVPU.value)
        self.assertEqual(cvpu_result, 3)


#                                    -- helper function - get_respiration_range_score tests --
class RespirationRangeTest(unittest.TestCase):
    """ Test module for get_respiration_range_score function """
    
    def test_get_respiration_range_score_returns_false_if_passed_string_value(self):
        """ Confirm get_respiration_range_score returns False if a string is passed """
        result = get_respiration_range_score("something")
        self.assertFalse(result)
    
    def test_get_respiration_range_score_returns_correct_score_if_observation_range_less_equal_8(self):
        """ Confirm get_respiration_range_score returns correct score observation range is <=8 """
        result_less_8 = get_respiration_range_score(5)
        result_equal_8 = get_respiration_range_score(8)
        self.assertEqual(result_less_8, 3)
        self.assertEqual(result_equal_8, 3)

    def test_get_respiration_range_score_returns_correct_score_if_observation_range_9_11(self):
        """ Confirm get_respiration_range_score returns correct score observation range is >=9 and <=11 """
        result_equal_9 = get_respiration_range_score(9)
        result_equal_10 = get_respiration_range_score(10)
        result_equal_11 = get_respiration_range_score(11)
        self.assertEqual(result_equal_9, 1)
        self.assertEqual(result_equal_10, 1)
        self.assertEqual(result_equal_11, 1)

    def test_get_respiration_range_score_returns_correct_score_if_observation_range_12_20(self):
        """ Confirm get_respiration_range_score returns correct score observation range is >=12 and <=20 """
        result_equal_12 = get_respiration_range_score(12)
        result_equal_15 = get_respiration_range_score(15)
        result_equal_20 = get_respiration_range_score(20)
        self.assertEqual(result_equal_12, 0)
        self.assertEqual(result_equal_15, 0)
        self.assertEqual(result_equal_20, 0)

    def test_get_respiration_range_score_returns_correct_score_if_observation_range_21_24(self):
        """ Confirm get_respiration_range_score returns correct score observation range is >=21 and <=24 """
        result_equal_21 = get_respiration_range_score(21)
        result_equal_22 = get_respiration_range_score(22)
        result_equal_24 = get_respiration_range_score(24)
        self.assertEqual(result_equal_21, 2)
        self.assertEqual(result_equal_22, 2)
        self.assertEqual(result_equal_24, 2)

    def test_get_respiration_range_score_returns_correct_score_if_observation_range_greater_equal_25(self):
        """ Confirm get_respiration_range_score returns correct score observation range is >=25 """
        result_equal_25 = get_respiration_range_score(25)
        result_greater_25 = get_respiration_range_score(30)
        self.assertEqual(result_equal_25, 3)
        self.assertEqual(result_greater_25, 3)


#                                    -- helper function - get_respiration_range_score tests --
class Spo2Test(unittest.TestCase):
    """ Test module for get_spo2_score function """
    
    def test_get_spo2_score_returns_false_if_passed_string_value(self):
        """ Confirm get_spo2_score returns False if a string is passed """
        result = get_spo2_score("something")
        self.assertFalse(result)
    
    def test_get_spo2_score_returns_correct_score_if_observation_range_less_equal_83(self):
        """ Confirm get_spo2_score returns correct score observation range is <=83 """
        result_less_83 = get_spo2_score(80)
        result_equal_83 = get_spo2_score(83)
        self.assertEqual(result_less_83, 3)
        self.assertEqual(result_equal_83, 3)

    def test_get_spo2_score_returns_correct_score_if_observation_range_84_85(self):
        """ Confirm get_spo2_score returns correct score observation range is >=84 and <=85 """
        result_equal_84 = get_spo2_score(84)
        result_equal_85 = get_spo2_score(85)
        self.assertEqual(result_equal_84, 2)
        self.assertEqual(result_equal_85, 2)

    def test_get_spo2_score_returns_correct_score_if_observation_range_86_87(self):
        """ Confirm get_spo2_score returns correct score observation range is >=86 and <=87 """
        result_equal_86 = get_spo2_score(86)
        result_equal_87 = get_spo2_score(87)
        self.assertEqual(result_equal_86, 1)
        self.assertEqual(result_equal_87, 1)

    def test_get_spo2_score_returns_correct_score_if_observation_range_88_92(self):
        """ Confirm get_spo2_score returns correct score observation range is >=88 and <=92 """
        result_equal_88 = get_spo2_score(88)
        result_equal_92 = get_spo2_score(92)
        self.assertEqual(result_equal_88, 0)
        self.assertEqual(result_equal_92, 0)

    def test_get_spo2_score_returns_correct_score_if_observation_range_93_air(self):
        """ Confirm get_spo2_score returns correct score observation range is >=93 and on air """
        result_equal_93 = get_spo2_score(93, AirOrOxygen.AIR)
        result_equal_95 = get_spo2_score(95, AirOrOxygen.AIR)
        self.assertEqual(result_equal_93, 0)
        self.assertEqual(result_equal_95, 0)

    def test_get_spo2_score_returns_correct_score_if_observation_range_93_94_oxygen(self):
        """ Confirm get_spo2_score returns correct score observation range is >=93 and <=94 on oxygen """
        result_equal_93 = get_spo2_score(93, AirOrOxygen.OXYGEN)
        result_equal_94 = get_spo2_score(94, AirOrOxygen.OXYGEN)
        self.assertEqual(result_equal_93, 1)
        self.assertEqual(result_equal_94, 1)

    def test_get_spo2_score_returns_correct_score_if_observation_range_95_96_oxygen(self):
        """ Confirm get_spo2_score returns correct score observation range is >=95 and <=96 on oxygen """
        result_equal_95 = get_spo2_score(95, AirOrOxygen.OXYGEN)
        result_equal_96 = get_spo2_score(96, AirOrOxygen.OXYGEN)
        self.assertEqual(result_equal_95, 2)
        self.assertEqual(result_equal_96, 2)

    def test_get_spo2_score_returns_correct_score_if_observation_range_97_greater_oxygen(self):
        """ Confirm get_spo2_score returns correct score observation range is >=97 on oxygen """
        result_equal_97 = get_spo2_score(97, AirOrOxygen.OXYGEN)
        result_equal_100 = get_spo2_score(100, AirOrOxygen.OXYGEN)
        self.assertEqual(result_equal_97, 3)
        self.assertEqual(result_equal_100, 3)

   


if __name__ == '__main__':
    unittest.main()