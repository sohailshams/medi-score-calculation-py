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


def get_spo2_score(spo, air_or_oxygen=None):
   # Check if spO2 is a number
    if type(spo) != int:
        return False

    if (spo <= 83 )or (spo >= 97 and air_or_oxygen == AirOrOxygen.OXYGEN):
      return 3  
    elif (spo >= 84 and spo <= 85) or (spo >= 95 and spo <= 96 and air_or_oxygen == AirOrOxygen.OXYGEN):
        return 2
    elif (spo >= 86 and spo <= 87) or (spo >= 93 and spo <= 94 and air_or_oxygen == AirOrOxygen.OXYGEN):
        return 1
    elif (spo >= 88 and spo <= 92) or (spo >= 93 and air_or_oxygen == AirOrOxygen.AIR):
      return 0
    else:
      return False

