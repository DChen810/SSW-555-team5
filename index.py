from prettytable import PrettyTable
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

class individual:
    def __init__(self,Id:str=''):
        self.id=Id
        self.name="NA"
        self.gender="NA"
        self.birthday="NA"
        self.death="NA"
        self.child=list()
        self.spoise=list()
        self.age="NA"
        self.married=False
    def getage(self):
        if self.death=='NA':
            self.age=datetime.date.today().year-self.birthday.year
        else:
            self.age=self.death.year-self.birthday.year
    
class faimly:
    def __init__(self):
        self.id="NA"
        self.husbandId="NA"
        self.wifeId="NA"
        self.children=list()
        self.divorced="NA"
        self.married="NA"

class function:
    def __init__(self,str=''):
        self.dir=str
        self.indi=dict()
        self.fami=dict()
        self.txt=get_file_str(str)
        self.get_result()
    def get_result(self):
        moth={'JAN':1,'FEB':2,'MAR':3,'APR':4,'MAY':5,'JUN':6,'JUL':7,'AUG':8,'SEP':9,'OCT':10,'NOV':11,'DEC':12,}
        is_fami=True
        txt_str=self.txt.split('\n')
        for line in txt_str:
            l=line.split()
            if len(l)==0:
                continue
            if l[0]=='0':
                if len(l)<=2:
                    continue
                Id=l[1]
                if l[2]=="INDI":
                    is_fami=False
                    self.indi.setdefault(Id,individual())
                    self.indi[Id].id=Id
                elif l[2]=="FAM":
                    is_fami=True
                    self.fami.setdefault(Id,faimly())
                    self.fami[Id].id=Id
                else:                    
                    continue
            elif l[0]=='1':
                last=l[1]
                if(is_fami):
                    if last=="HUSB":
                        self.fami[Id].husbandId=' '.join(l[2:])
                    if last=="WIFE":
                        self.fami[Id].wifeId=' '.join(l[2:])
                    if last=="CHIL":
                        self.fami[Id].children.append(' '.join(l[2:]))
                else:
                    if last=="NAME":
                        self.indi[Id].name=' '.join(l[2:])
                    if last=="SEX":
                        self.indi[Id].gender=' '.join(l[2:])
                    if last=="FAMC":
                        self.indi[Id].child.append(' '.join(l[2:]))
                    if last=="FAMS":
                        self.indi[Id].spoise.append(' '.join(l[2:]))
            elif l[0]=='2':
                Time=datetime.date(int(l[4]),moth[l[3]],int(l[2]))
                if(is_fami):
                    if last=="MARR":
                        self.fami[Id].married=Time                        
                    if last=="DIV":
                        self.fami[Id].divorced=Time
                else:
                    if last=="BIRT":
                        self.indi[Id].birthday=Time
                    if last=="DEAT":
                        self.indi[Id].death=Time
        for Id in self.indi.keys():
            self.indi[Id].getage()
        for Id in self.fami.keys():
            self.indi[self.fami[Id].husbandId].married=True
            self.indi[self.fami[Id].wifeId].married=True
    def PPrint(self):
        row1:PrettyTable=PrettyTable()
        row1.field_names=['ID','Name','Gender','Birthday', 'Age','Alive','Death','Child','Spoise','Married']
        for Id in self.indi.keys():
            line=[Id,self.indi[Id].name,self.indi[Id].gender,self.indi[Id].birthday,self.indi[Id].age,self.indi[Id].death=="NA",self.indi[Id].death,self.indi[Id].child,self.indi[Id].spoise,self.indi[Id].married]
            #print(line)
            row1.add_row(line)
        print(row1)

        row2:PrettyTable=PrettyTable()
        row2.field_names=['ID','Married','Divorced','Husband name','Wifi ID','Wife Name','Children' ]
        for Id in self.fami.keys():
            line=[Id,self.fami[Id].married,self.fami[Id].divorced,self.indi[self.fami[Id].husbandId].name,self.fami[Id].wifeId,self.indi[self.fami[Id].wifeId].name,self.fami[Id].children,]
            row2.add_row(line)
        print(row2)

    def unmarried_list(self):
        unmarried=list()
        for Id in self.indi.keys():
            if self.indi[Id].married==False:
                unmarried.append(self.indi[Id])
        return unmarried
    
    def check_deadpeople_given(self):
        for person in self.indi.values():
            if person.death!="NA":#find the people is dead
                for fami in person.child:#find the people's family
                    for child in fami.children:#find the child in the family
                        if child.birthday>person.death:#id the date the child given is late than the people, print
                            print(f"The {person.name}'s(Id:{person.id}) child name {child.name}(Id:{child.id}) given later his death")
    
    def find_age(self,age):
        age_list=list()
        for person in self.indi.values():
            if person.age==age:
                age_list.append(person)
        return age_list
    
    def get_adults(self):
        age_list=list()
        for person in self.indi.values():
            if float(person.age)>=18:
                age_list.append(person)
        return age_list

    def different_sex_given(self):
        for famis in self.fami.values():
            if len(famis.children)>0 and (self.indi[famis.husbandId]==self.indi[famis.wifeId]):
                print(111)
    def get_twins(self):
        twins=list()
        for faimls in self.fami.values():
            for c1 in faimls.children:
                for c2 in faimls.children:
                    if(self.indi[c1].age==self.indi[c2].age and c1 != c2):
                        if(set([self.indi[c1],self.indi[c2]]) not in twins):
                            twins.append(set([self.indi[c1],self.indi[c2]]))    
        return twins

if __name__ == '__main__':
    while True:
        #give three chance to enter the path of the file
        for i in range(3):
            try:
                file_path=input('Press enter only to use the default test file, \nor enter the file path:')
                textcase=function(file_path)
                textcase.PPrint()
                unmarried=textcase.unmarried_list()
                print("the unmarried name list:")
                for i in unmarried:
                    print(i.name,end=' ')
                age=textcase.find_age(38)
                print("\nthe age 38:",end=' ')
                for i in age:
                    print(i.name,end=' ')
                get_adults=textcase.get_adults()
                print("\nthe adults:",end=' ')
                for i in age:
                    print(i.name)
                twins=textcase.get_twins()
                print(f"\nthe twins:{twins}",end=' ')
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
