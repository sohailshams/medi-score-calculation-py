from medi_score.Enums import AirOrOxygen

def get_air_or_oxygen_score(air_or_oxygen):
    match air_or_oxygen:
        case AirOrOxygen.AIR:
            return air_or_oxygen
        case AirOrOxygen.OXYGEN:
            return air_or_oxygen
        case _:
            return False
        