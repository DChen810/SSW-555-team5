from prettytable import PrettyTable
import datetime

def sort_age(indi:dict(),Prin=False)->list():
    row:PrettyTable=PrettyTable()
    row.field_names=['ID','name','age']
    age_name=list()
    for Id in indi.keys():
        if indi[Id]['Death']=='NA':
            age=datetime.date.today().year-indi[Id]['Birthday'].year
        else:
            age=indi[Id]['Death'].year-indi[Id]['Birthday'].year
        age_name.append([age,indi[Id]['Name'],Id])
    age=sorted(age_name)
    age_list=list()
    for i in age:
        row.add_row([i[2],i[1],i[0]])
        age_list.append(i[0])
    if(Prin):
        print(row)
    return age


def get_couple(indi:dict(),Prin=False)->list():
    row:PrettyTable=PrettyTable()
    row.field_names=['ID','name','age']
    age_name=list()
    for Id in indi.keys():
        if indi[Id]['Death']=='NA':
            age=datetime.date.today().year-indi[Id]['Birthday'].year
        else:
            age=indi[Id]['Death'].year-indi[Id]['Birthday'].year
        age_name.append([age,indi[Id]['Name'],Id])
    age=sorted(age_name)
    age_list=list()
    for i in age:
        row.add_row([i[2],i[1],i[0]])
        age_list.append(i[0])
    if(Prin):
        print(row)
    return age
