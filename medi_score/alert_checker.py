def alert_checker(medi_score_calculation, medi_score_data):
    flag_up = False
    
    for obj in medi_score_data:
        # Check if current score is > 2
        # assuming mediScoreData only contains last 24 hours readings
        if medi_score_calculation - obj["mediScore"] > 2:
            flag_up = True
    
    return flag_up
