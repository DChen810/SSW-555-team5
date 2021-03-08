"""
Project 03
Name:Gengwu Zhao
"""
from prettytable import PrettyTable
import datetime
from us2_3 import *
from us09_10 import *
from us17_18 import *
from us25_26 import *
import datetime

def get_file_str(file_path:str=None)->str:
    if file_path is None or file_path == '':
        file_path='Project01_Gengwu_Zhao.ged'
        print("No input path, default test document will be used: Project01_Gengwu_Zhao.ged")        
    file_str=open(file_path,'r').read()
    #if the txt is empty, raise a valueError
    if len(file_str)==0:
        raise ValueError
    return file_str

#get the averages of the confidences
def get_result(txt:str):
    moth={'JAN':1,'FEB':2,'MAR':3,'APR':4,'MAY':5,'JUN':6,'JUL':7,'AUG':8,'SEP':9,'OCT':10,'NOV':11,'DEC':12,}
    tag={
        "NAME":"Name",
        "SEX":"Gender",
        "BIRT":"Birthday",
        "DEAT":"Death",
        "FAMC":"Child",
        "FAMS":"Spoise",

        "MARR":"Married",
        "HUSB":"Husband ID",
        "WIFE":"WIFE ID",
        "CHIL":"Childern",
        "DIV":"Divorced",
    }
    indi=dict()
    fami=dict()
    is_fami=True
    txt_str=txt.split('\n')
    for line in txt_str:
        l=line.split()
        if l[0]=='0':
            Id=l[1]
            if l[2]=="INDI":
                is_fami=False
                indi.setdefault(Id,dict())
            elif l[2]=="FAM":
                is_fami=True
                fami.setdefault(Id,dict())
            else:
                continue
        elif l[0]=='1':
            last=tag[l[1]]
            if(is_fami):
                if last =='Childern':
                    fami[Id].setdefault(last,[])
                    fami[Id][last].append(l[2])
                else:
                    fami[Id].setdefault(last,'NA')
                    if len(l)>1:
                        fami[Id][last]=' '.join(l[2:])
            else:
                if last =='Child' or last == "Spoise":
                    indi[Id].setdefault(last,[])
                    indi[Id][last].append(l[2])
                else:
                    indi[Id].setdefault(last,'NA')
                    if len(l)>1:
                        indi[Id][last]=' '.join(l[2:])
        elif l[0]=='2':
            Time=datetime.date(int(l[4]),moth[l[3]],int(l[2]))
            if(is_fami):
                fami[Id][last]=Time
            else:
                indi[Id][last]=Time
    for Id in indi.keys():
        for last in tag.values():
            indi[Id].setdefault(last,'NA')
    for Id in fami.keys():
        for last in tag.values():
            fami[Id].setdefault(last,'NA')
    return indi,fami


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

def PPrint(indi:dict(),fami:dict()):
    row1:PrettyTable=PrettyTable()
    row1.field_names=['ID','Name','Gender','Birthday', 'Age','Alive','Death','Child','Spoise']
    for Id in indi.keys():
        if indi[Id]['Death']=='NA':
            Alive=True
            age=datetime.date.today().year-indi[Id]['Birthday'].year
        else:
            Alive=False
            age=indi[Id]['Death'].year-indi[Id]['Birthday'].year
        line=[Id,indi[Id]['Name'],indi[Id]['Gender'],indi[Id]['Birthday'],age,Alive,indi[Id]['Death'],indi[Id]['Child'],indi[Id]['Spoise']]
        #print(line)
        row1.add_row(line)
    print(row1)

    row2:PrettyTable=PrettyTable()
    row2.field_names=['ID','Married','Divorced','Husband name','Wifi ID','Wife Name','Children' ]
    for Id in fami.keys():
        line=[Id,fami[Id]['Married'],fami[Id]['Divorced'],indi[fami[Id]['Husband ID']]['Name'],fami[Id]['WIFE ID'],indi[fami[Id]['WIFE ID']]['Name'],fami[Id]['Childern'],]
        row2.add_row(line)
    print(row2)


def main():
    while True:
        #give three chance to enter the path of the file
        for i in range(3):
            try:
                file_path=input('Press enter only to use the default test file, \nor enter the file path:')
                find_str=get_file_str(file_path)
                result=get_result(find_str)
                PPrint(result[0],result[1])
                print()
                age=sort_age(result[0],True)
                print(f"the youngest:{get_youngest(age)}")
                print(f"the oldest:{get_oldest(age)}")
            except ValueError:
                print('The file is empty,try again.')
            except FileNotFoundError as e:
                print(f"{e}. try again.")
            else:
                #if there is no error, print the result and break the for loop to exit.
                break
            #if there is an error, not break, tell the left times to the user instead.
            print(f'You have left {2-i} times')
        user_choose=input("\nEnter 'q' to exit, any other key to continue:")
        #if user enter 'q', break
        if user_choose.lower()=='q':
            break

if __name__=='__main__':
    main()
