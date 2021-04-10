import datetime

def marriage_before_divorce(indi):
    """
    user story 04
    marriage should occur before divorce
    """
    err_num =0
    for Id in indi.keys():
        if indi[Id]['Married']=='NA':
            if indi[Id]['Divorced'] =='NA':
                continue
            else:
                err_num = err_num + 1
                return f"ERROR: FAMILY: US04: {indi['Married'].line}: {indi['Id'].value}: divorce without married"
        else:
            marr = indi[Id]['Married']
            div = indi[Id]['Divorced']
            if div < marr:
                err_num = err_num + 1
                return f"ERROR: US04: {indi['Married'].line}: {indi['Id'].value}: divorce before married"
            else:
                continue
    if err_num ==0:
        print('US04:checked,all marriage before divorce')

def marriage_before_death(indi):
    """
    user story 05
    marriage should occur before death
    """
    err_num =0
    for Id in indi.keys():
        if indi[Id]['Married']=='NA':
            continue
        if indi[Id]['Death']=='NA':
            continue
        else:
            marr = indi[Id]['Married']
            dea = indi[Id]['Death']
            if indi[Id]['Married']=='NA':
                continue
            if indi[Id]['Death']=='NA':
                continue
            elif dea < marr:
                err_num = err_num + 1
                return f"ERROR: US05: {indi['Married'].line}: {indi['Id'].value}: death before married"
            else:
                continue
    if err_num ==0:
        print('US05:checked, all death before married')