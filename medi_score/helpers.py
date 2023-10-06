from medi_score.Enums import AirOrOxygen, Consciousness

def get_air_or_oxygen_score(air_or_oxygen):
    match air_or_oxygen:
        case AirOrOxygen.AIR:
            return air_or_oxygen
        case AirOrOxygen.OXYGEN:
            return air_or_oxygen
        case _:
            return False
        
def get_consciousness_score(consciousness):
    match consciousness:
        case Consciousness.ALERT:
            return consciousness
        case Consciousness.CVPU:
            return consciousness
        case _:
            return False
        
def get_respiration_range_score(respiration_range):
    # Check if respiration is a number
    if type(respiration_range) != int:
        return False
  
    if respiration_range <= 8:
        return 3
    elif respiration_range >= 9 and respiration_range <= 11:
        return 1
    elif respiration_range >= 12 and respiration_range <= 20:
        return 0
    elif respiration_range >= 21 and respiration_range <= 24:
        return 2
    elif respiration_range >= 25:
        return 3
    else:
        return False

