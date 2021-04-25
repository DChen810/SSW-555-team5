import datetime

def age_limit(indi):
    """
    user story 07
    All human should be less then 150 years old
    """
    err_num =0
    for Id in indi.keys():
        if indi[Id]['Death']!='NA':
            age =indi[Id]['Death'].year-indi[Id]['Birthday'].year
            if (age > 150):
                err_num = err_num + 1
                return f"ERROR: US07: {indi['Birthday'].line}: {indi['Id'].value}: age beyond 150"
        else:
            age=datetime.date.today().year-indi[Id]['Birthday'].year
            if (age>150):
                err_num = err_num + 1
                return f"ERROR: US07: {indi['Birthday'].line}: {indi['Id'].value}: age beyond 150"
    if err_num ==0:
        print('US07:checked, everyone is less then 150 years old')

def marriage_limit(indi):
    """
    user story 08
    Marriage after 18
    """
    err_num =0
    for Id in indi.keys():
        if indi[Id]['Married']=='NA':
            continue
        else:
            marriage_age = indi[Id]['Married'].year-indi[Id]['Birthday'].year
            if (marriage_age<18):
                err_num = err_num + 1
                return f"ERROR: US08: {indi['Married'].line}: {indi['Id'].value}: death before divorced"
            else:
                continue
    if err_num ==0:
        print('US08:checked, all marriage after 18 years old')