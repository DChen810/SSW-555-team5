def firstDateIsEarlier(d1, d2):
    """
    Given dates in the form {"year":1970, "month": 01, "day": 01},
    return True if the first date is the earlier of the two
    """
    yyyymmdd1 = str(d1["year"]) + str(d1["month"]) + str(d1["day"])
    yyyymmdd2 = str(d2["year"]) + str(d2["month"]) + str(d2["day"])
    return int(yyyymmdd1) < int(yyyymmdd2)

def birth_before_marriage(bir, mar):
    """
    user story 02
    Birth should occur before marriage
    """
    if mar == {}:
        return True 
    if bir == {}:
        return False 
    return firstDateIsEarlier(bir, mar)

def birth_before_death(bir, death):
    """
    user story 03
    Birth should occur before death of either spouse
    """
    if bir == {}:
        return False 
    if death == {}:
        return True 
    return firstDateIsEarlier(bir, death)