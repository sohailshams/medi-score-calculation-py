import unittest
from medi_score.medi_score import medi_score_calculation
from medi_score.helpers import get_air_or_oxygen_score, get_consciousness_score, get_respiration_range_score, get_spo2_score, get_temperature_score
from medi_score.Enums import AirOrOxygen, Consciousness
from medi_score.alert_checker import alert_checker
from test_data.patient_test_data import medi_score_data


#                                    -- medi_score_calculation tests --
class MediScoreCalculationTest(unittest.TestCase):
    """ Test module for medi_score_calculation function """

    def setUp(self):
        """ Initialise test data """
         # Create observation dictionary for patient 1
        self.observation_dict = {
            "air_or_oxygen": AirOrOxygen.AIR.value,
            "consciousness": Consciousness.ALERT.value,
            "respiration": 15,
            "spo2": 95,
            "temperature": 37.1
        }
   
        # Create observation dictionary for patient 2
        self.observation_dict_two = {
            "air_or_oxygen": AirOrOxygen.OXYGEN.value,
            "consciousness": Consciousness.ALERT.value,
            "respiration": 17,
            "spo2": 95,
            "temperature": 37.1
        }
   
        # Create observation dictionary for patient 3
        self.observation_dict_three = {
            "air_or_oxygen": AirOrOxygen.OXYGEN.value,
            "consciousness": Consciousness.CVPU.value,
            "respiration": 23,
            "spo2": 88,
            "temperature": 38.5
        }

        # Create observation dictionary for patient 4
        self.observation_dict_four = {
            "air_or_oxygen": AirOrOxygen.OXYGEN.value,
            "consciousness": Consciousness.CVPU.value,
            "respiration": 25,
            "spo2": 97,
            "temperature": 35
        }


    def test_medi_score_calculation_returns_error_message_if_passed_air__oxygen_observation_as_string(self):
         """ Confirm medi_score_calculation returns an error message if AIR/OXYGEN observation passed as string """
         # Update air_or_oxygen value to a string
         self.observation_dict["air_or_oxygen"] = "something"
         
         result = medi_score_calculation(self.observation_dict)
         self.assertEqual(result, "Please enter correct AIR or OXYGEN input!")

    def test_medi_score_calculation_returns_error_message_if_passed_consciousness_observation_as_string(self):
         """ Confirm medi_score_calculation returns an error message if consciousness observation passed as string """
         # Update consciousness value to a string
         self.observation_dict["consciousness"] = "something"
         
         result = medi_score_calculation(self.observation_dict)
         self.assertEqual(result, "Please enter correct ALERT or CVPU input!")

    def test_medi_score_calculation_returns_error_message_if_passed_respiration_observation_as_string(self):
         """ Confirm medi_score_calculation returns an error message if consciousness observation passed as string """
         # Update respiration value to a string
         self.observation_dict["respiration"] = "something"
         
         result = medi_score_calculation(self.observation_dict)
         self.assertEqual(result, "Please enter integer value for Respiration rate")

    def test_medi_score_calculation_returns_error_message_if_passed_spo2_observation_as_string(self):
         """ Confirm medi_score_calculation returns an error message if spO2 observation passed as string """
         # Update spo2 value to a string
         self.observation_dict["spo2"] = "something"
         
         result = medi_score_calculation(self.observation_dict)
         self.assertEqual(result, "Please enter integer value for spO2")

    def test_medi_score_calculation_returns_error_message_if_passed_temperature_observation_as_string(self):
         """ Confirm medi_score_calculation returns an error message if temperature observation passed as string """
         # Update temperature value to a string
         self.observation_dict["temperature"] = "something"
         
         result = medi_score_calculation(self.observation_dict)
         self.assertEqual(result, "Please enter correct value for temperature")

    def test_medi_score_calculation_returns_correct_score_if_passed_temperature_observation_as_integer(self):
         """ Confirm medi_score_calculation returns correct score if temperature observation passed as integer """
         # Update temperature value to a integer
         self.observation_dict["temperature"] = 35
         
         result = medi_score_calculation(self.observation_dict)
         self.assertEqual(result, 3)

    def test_medi_score_calculation_returns_correct_score_if_passed_temperature_observation_with_many_decimal_places(self):
         """ Confirm medi_score_calculation returns correct score if temperature observation passed as with many decimal places """
         # Update temperature value 
         self.observation_dict["temperature"] = 35.22225656656
         
         result = medi_score_calculation(self.observation_dict)
         self.assertEqual(result, 1)
    
    # Patient 1 - no alert
    def test_medi_score_calculation_returns_correct_score_if_passed_patient_one_observations(self):
         """ Confirm medi_score_calculation returns correct score of 0 if passed patient one observations """
         
         result = medi_score_calculation(self.observation_dict)
         self.assertEqual(result, 0)
         self.assertFalse(alert_checker(result, medi_score_data))
    
    # Patient 2 - alert
    def test_medi_score_calculation_returns_correct_score_if_passed_patient_two_observations(self):
         """ Confirm medi_score_calculation returns correct score of 4 if passed patient one observations """
         
         result = medi_score_calculation(self.observation_dict_two)
         self.assertEqual(result, 4)
         self.assertTrue(alert_checker(result, medi_score_data))

    # Patient 3 - alert
    def test_medi_score_calculation_returns_correct_score_if_passed_patient_three_observations(self):
         """ Confirm medi_score_calculation returns correct score of 8 if passed patient one observations """
         
         result = medi_score_calculation(self.observation_dict_three)
         self.assertEqual(result, 8)
         self.assertTrue(alert_checker(result, medi_score_data))

         
    # Patient 4 - alert
    def test_medi_score_calculation_returns_correct_score_if_passed_patient_four_observations(self):
         """ Confirm medi_score_calculation returns correct score of 14 if passed patient one observations """
         
         result = medi_score_calculation(self.observation_dict_four)
         self.assertEqual(result, 14)
         self.assertTrue(alert_checker(result, medi_score_data))



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
    
    def test_get_consciousness_score_returns_none_if_passed_string_value(self):
        """ Confirm get_consciousness_score returns None if a string is passed """
        result = get_consciousness_score('nonsense')
        self.assertIsNone(result)
    
    def test_get_consciousness_score_returns_none_if_incorrect_passed_value(self):
        """ Confirm get_consciousness_score returns None if a incorrect value is passed """
        result = get_consciousness_score(7)
        self.assertIsNone(result)

    def test_get_consciousness_score_returns_correct_score(self):
        """ Confirm get_consciousness_score returns correct score when passed 'AIR' or 'OXYGEN' """
        alert_result = get_consciousness_score(Consciousness.ALERT.value)
        self.assertEqual(alert_result, 0)
        cvpu_result = get_consciousness_score(Consciousness.CVPU.value)
        self.assertEqual(cvpu_result, 3)


#                                    -- helper function - get_respiration_range_score tests --
class RespirationRangeTest(unittest.TestCase):
    """ Test module for get_respiration_range_score function """
    
    def test_get_respiration_range_score_returns_none_if_passed_string_value(self):
        """ Confirm get_respiration_range_score returns None if a string is passed """
        result = get_respiration_range_score("something")
        self.assertIsNone(result)
    
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
    
    def test_get_spo2_score_returns_none_if_passed_string_value(self):
        """ Confirm get_spo2_score returns None if a string is passed """
        result = get_spo2_score("something")
        self.assertIsNone(result)
    
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

   
#                                    -- helper function - get_temperature_score tests --
class TemperatureTest(unittest.TestCase):
    """ Test module for get_temperature_score function """
    
    def test_get_temperature_score_returns_none_if_passed_string_value(self):
        """ Confirm get_temperature_score returns None if a string is passed """
        result = get_temperature_score('something')
        self.assertIsNone(result)

    def test_get_temperature_score_returns_correct_score_if_passed_multi_decimal_place_value(self):
        """ Confirm get_temperature_score returns correct score observation range is <=35.59999 """
        result = get_temperature_score(35.59999)
        self.assertEqual(result, 1)

    def test_get_temperature_score_returns_correct_score_if_observation_range_less_equal_35(self):
        """ Confirm get_temperature_score returns correct score observation range is <=35.0 """
        result_less_35  = get_temperature_score(35.0)
        result_equal_350 = get_temperature_score(34.9)
        self.assertEqual(result_less_35, 3)
        self.assertEqual(result_equal_350, 3)

    def test_get_temperature_score_returns_correct_score_if_observation_range_351_360(self):
        """ Confirm get_temperature_score returns correct score observation range is >=35.1 and <=36.0 """
        result_equal_351  = get_temperature_score(35.1)
        result_equal_36 = get_temperature_score(36)
        self.assertEqual(result_equal_351, 1)
        self.assertEqual(result_equal_36, 1)

    def test_get_temperature_score_returns_correct_score_if_observation_range_361_38(self):
        """ Confirm get_temperature_score returns correct score observation range is >=36.1 and <=38.0 """
        result_equal_361  = get_temperature_score(36.1)
        result_equal_380 = get_temperature_score(38.0)
        self.assertEqual(result_equal_361, 0)
        self.assertEqual(result_equal_380, 0)

    def test_get_temperature_score_returns_correct_score_if_observation_range_381_39(self):
        """ Confirm get_temperature_score returns correct score observation range is >=38.1 and <=39.0 """
        result_equal_381  = get_temperature_score(38.1)
        result_equal_390 = get_temperature_score(39.0)
        self.assertEqual(result_equal_381, 1)
        self.assertEqual(result_equal_390, 1)

    def test_get_temperature_score_returns_correct_score_if_observation_range_391_greater(self):
        """ Confirm get_temperature_score returns correct score observation range is >=39.1 """
        result_equal_391  = get_temperature_score(39.1)
        result_equal_40 = get_temperature_score(40.0)
        self.assertEqual(result_equal_391, 2)
        self.assertEqual(result_equal_40, 2)

#                                    -- alert_checker tests --
class AlertCheckerTest(unittest.TestCase):
    """ Test module for alert_checker function """
    def setUp(self):
        """ Initialise test data """
         # Create observation dictionary for patient 1
        self.observation_dict = {
            "air_or_oxygen": AirOrOxygen.AIR.value,
            "consciousness": Consciousness.ALERT.value,
            "respiration": 15,
            "spo2": 95,
            "temperature": 37.1
        }
   
        # Create observation dictionary for patient 2
        self.observation_dict_two = {
            "air_or_oxygen": AirOrOxygen.OXYGEN.value,
            "consciousness": Consciousness.ALERT.value,
            "respiration": 17,
            "spo2": 95,
            "temperature": 37.1
        }
   
        # Create observation dictionary for patient 3
        self.observation_dict_three = {
            "air_or_oxygen": AirOrOxygen.OXYGEN.value,
            "consciousness": Consciousness.CVPU.value,
            "respiration": 23,
            "spo2": 88,
            "temperature": 38.5
        }

        # Single reading medi score data
        self.medi_score_data_single = [
            {
            "id": 1,
            "time": "06:00",
            "mediScore": 0,
            },
        ]

    def test_alert_checker_returns_false_if_medi_score_did_not_raise_by_2_24_hours(self):
        """ Confirm alert_checker returns False if medi score did not raise by more than 2 - single reading """
        medi_score = medi_score_calculation(self.observation_dict)
        result = alert_checker(medi_score, self.medi_score_data_single)
        self.assertFalse(result)

    def test_alert_checker_returns_True_if_medi_score_raise_by_2_24_hours(self):
        """ Confirm alert_checker returns True if medi score raise by more than 2 - single reading """
        medi_score = medi_score_calculation(self.observation_dict_two)
        result = alert_checker(medi_score, self.medi_score_data_single)
        self.assertTrue(result)

    def test_alert_checker_returns_false_if_medi_score_did_not_raise_by_2_24_hours_multiple(self):
        """ Confirm alert_checker returns False if medi score did not raise by more than 2 - multiple readings """
        medi_score = medi_score_calculation(self.observation_dict)
        result = alert_checker(medi_score, medi_score_data)
        self.assertFalse(result)

    def test_alert_checker_returns_True_if_medi_score_raise_by_2_24_hours_multiple(self):
        """ Confirm alert_checker returns True if medi score raise by more than 2 - multiple readings """
        medi_score = medi_score_calculation(self.observation_dict_three)
        result = alert_checker(medi_score, medi_score_data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()