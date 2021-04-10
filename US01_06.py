import datetime

def dates_before_current(indi):
    """
    user story 01
    All dates should before current date
    """
    err_num =0
    for Id in indi.keys():
        curr = datetime.date.today()
        if indi[Id]['Death']!='NA':
            dea = indi[Id]['Death']
            if (curr < dea):
                err_num = err_num + 1
                return f"ERROR: US01: {indi['Death'].line}: {indi['Id'].value}: death before current"
        if indi[Id]['Married']!='NA':
            marr = indi[Id]['Married']
            if (curr < marr):
                err_num = err_num + 1
                return f"ERROR: US01: {indi['Married'].line}: {indi['Id'].value}: marry before current"
        if indi[Id]['Divorced']!='NA':
            div = indi[Id]['Divorced']
            if (curr < div):
                err_num = err_num + 1
                return f"ERROR: US01: {indi['Divorced'].line}: {indi['Id'].value}: divorce before current"
        if indi[Id]['Birthday']!='NA':
            bir = indi[Id]['Birthday']
            if (curr < bir):
                err_num = err_num + 1
                return f"ERROR: US01: {indi['Birthday'].line}: {indi['Id'].value}: Birthday before current"
        else:
            continue
    if err_num ==0:
        print('US01:checked,all dates before current')

def divorce_before_death(indi):
    """
    user story 06
    Divorce before death
    """
    err_num =0
    for Id in indi.keys():
        if indi[Id]['Death']=='NA':
            continue
        if indi[Id]['Divorced']=='NA':
            continue
        else:
            divo = indi[Id]['Divorced']
            dea = indi[Id]['Death']
            if indi[Id]['Divorced']=='NA':
                continue
            if indi[Id]['Death']=='NA':
                continue
            elif dea < divo:
                err_num = err_num + 1
                return f"ERROR: US06: {indi['Divorced'].line}: {indi['Id'].value}: death before divorced"
            else:
                continue
    if err_num ==0:
        print('US06:checked, all death before divorced')

