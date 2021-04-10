def birth_before_marriage(indi):
    """
    user story 02
    birth before marriage
    """
    err_num =0
    for Id in indi.keys():
        if indi[Id]['Married']=='NA':
            continue
        else:
            bir = indi[Id]['Birthday']
            marr = indi[Id]['Married']
            if bir >= marr:
                err_num = err_num + 1
                return f"ERROR: US02: {indi['Married'].line}: {indi['Id'].value}: Married before birth"
            else:
                continue
    if err_num ==0:
        print('US02:checked, all birth before marry')


def birth_before_death(indi):
    """
    user story 03
    birth before death
    """
    err_num =0
    for Id in indi.keys():
        if indi[Id]['Death']=='NA':
            continue
        else:
            bir = indi[Id]['Birthday']
            dea = indi[Id]['Death']
            if bir >= dea:
                err_num = err_num + 1
                return f"ERROR: US03: {indi['Death'].line}: {indi['Id'].value}: Death before birth"
            else:
                continue
    if err_num ==0:
        print('US03:checked, all birth before death')