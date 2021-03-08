from prettytable import PrettyTable
import datetime

def Print_aliving(indi):
    row:PrettyTable=PrettyTable()
    row.field_names=['ID','Name','Gender','Birthday', 'Age','Alive','Death','Child','Spoise']
    aliving_list=list()
    for Id in indi.keys():
        if indi[Id]['Death']=='NA':
            Alive=True
            age=datetime.date.today().year-indi[Id]['Birthday'].year
        else:
            Alive=False
            age=indi[Id]['Death'].year-indi[Id]['Birthday'].year
        line=[Id,indi[Id]['Name'],indi[Id]['Gender'],indi[Id]['Birthday'],age,Alive,indi[Id]['Death'],indi[Id]['Child'],indi[Id]['Spoise']]
        if indi[Id]['Death']=='NA':
            #print(line)
            aliving_list.append(indi[Id]['Name'])
            row.add_row(line)
    #print(row)
    return aliving_list

def Print_death(indi):
    row:PrettyTable=PrettyTable()
    row.field_names=['ID','Name','Gender','Birthday', 'Age','Alive','Death','Child','Spoise']
    death_list=list()
    for Id in indi.keys():
        if indi[Id]['Death']=='NA':
            Alive=True
            age=datetime.date.today().year-indi[Id]['Birthday'].year
        else:
            Alive=False
            age=indi[Id]['Death'].year-indi[Id]['Birthday'].year
        line=[Id,indi[Id]['Name'],indi[Id]['Gender'],indi[Id]['Birthday'],age,Alive,indi[Id]['Death'],indi[Id]['Child'],indi[Id]['Spoise']]
        if indi[Id]['Death']=='NA':
            #print(line)
            death_list.append(indi[Id]['Name'])
            row.add_row(line)
    #print(row)
    return death_list