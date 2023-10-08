from medi_score.helpers import get_air_or_oxygen_score, get_consciousness_score, get_respiration_range_score, get_spo2_score, get_temperature_score

def medi_score_calculation(observation_dict):
    total = 0
    
    # Get air or oxygen score or return an error message
    air_oxygen_score = get_air_or_oxygen_score(observation_dict["air_or_oxygen"])
    if air_oxygen_score == None:
        return "Please enter correct AIR or OXYGEN input!"
    
    # Get consciousness score or return an error message
    consciousness_score = get_consciousness_score(observation_dict["consciousness"])
    if consciousness_score == None:
        return "Please enter correct ALERT or CVPU input!"
    
    # Get respiration range score or return an error message
    respiration_score = get_respiration_range_score(observation_dict["respiration"])
    if respiration_score == None:
        return "Please enter integer value for Respiration rate"

    # Get SpO2 score or return an error message
    spo2_score = get_spo2_score(observation_dict["spo2"], observation_dict["air_or_oxygen"])
    if spo2_score == None:
        return "Please enter integer value for spO2"
    
    # Get temperature score or return an error message
    temperature_score = get_temperature_score(observation_dict["temperature"])
    if temperature_score == None:
        return "Please enter correct value for temperature"

    total += air_oxygen_score + consciousness_score + respiration_score + spo2_score + temperature_score

    return total
