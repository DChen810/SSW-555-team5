def marriage_before_divorce(d1, d2):
    """
    user story 04
    marriage should occur before divorce
    """
    if d2 == {}:
        return True 
    if d1 == {}:
        if d2 == {}:
            return True
        if d2 != {}:
            return False
    return int(str(d1["year"]) + str(d1["month"]) + str(d1["day"])) < int(str(d2["year"]) + str(d2["month"]) + str(d2["day"]))

def marriage_before_death(d1, d2):
    """
    user story 05
    marriage should occur before death
    """
    if d2 == {}:
        return True 
    if d1 == {}:
        return True 
    return int(str(d1["year"]) + str(d1["month"]) + str(d1["day"])) < int(str(d2["year"]) + str(d2["month"]) + str(d2["day"]))