"""
Homework 04
Name:Gengwu Zhao

"""

import unittest
from HW04_Gengwu_Zhao import *
#the user stroy is print the information of every people by the sort of age.
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

class test_sort_ages(unittest.TestCase):
    def test_sort_age(self):
        find_str=get_file_str()
        result=get_result(find_str)#get the infomation of gedcom file
        age=sort_age(result[0],True)#Get information about age [age,Name,id]
        
        last_age=age[0][0]      
        self.assertTrue(len(age)==len(result[0]))#Test the age output is equal to the total numeber of people
        for i in age:
            #get the real age of every people.
            if result[0][i[2]]['Death']=='NA':
                i_age=datetime.date.today().year-result[0][i[2]]['Birthday'].year
            else:
                i_age=result[0][i[2]]['Death'].year-result[0][i[2]]['Birthday'].year
            self.assertTrue(i[1]==result[0][i[2]]['Name'])#test the sort name is equal of the output
            self.assertTrue(i[0]==i_age)#test the sort age is equal of the output
            self.assertTrue(i[0]>0)#test the age is greater than 0
            self.assertTrue(i[0]>=last_age)# test the age is better than last one
            last_age=i[0]
class UserStory02Tests(unittest.TestCase):
    def test1(self):
        #no birth is not fine
        self.assertTrue(birth_before_marriage({},{}))

    def test2(self):
        b = {"year":2001, "month":1, "day":1}
        self.assertTrue(birth_before_marriage(b,{}))

    def test3(self):
        #marrigage without birth is NOT fine
        m = {"year":2000, "month":1, "day":1}
        self.assertFalse(birth_before_marriage({},m))

    def test4(self):
        #both events is fine
        b = {"year":2000, "month":1, "day":1}
        m = {"year":2019, "month":1, "day":1}
        self.assertTrue(birth_before_marriage(b,m))

    def test5(self):
        #both events, with marriage first is NOT fine
        m = {"year":2000, "month":1, "day":1}
        b = {"year":2025, "month":1, "day":1}
        self.assertFalse(birth_before_marriage(b,m))

class UserStory03Tests(unittest.TestCase):
    def test1(self):
        #no birth is not fine
        self.assertFalse(birth_before_death({},{}))

    def test2(self):
        #birth without death is fine
        b = {"year":2000, "month":1, "day":1}
        self.assertTrue(birth_before_death(b,{}))

    def test3(self):
        #death without birth is not fine
        d = {"year":2000, "month":1, "day":1}
        self.assertFalse(birth_before_death({},d))

    def test4(self):
        #both events, with birth first is fine
        b = {"year":2000, "month":1, "day":1}
        d = {"year":2010, "month":1, "day":1}
        self.assertTrue(birth_before_death(b,d))

    def test5(self):
        #both events, with death first is NOT fine
        d = {"year":2000, "month":1, "day":1}
        b = {"year":2010, "month":1, "day":1}
        self.assertFalse(birth_before_death(b,d))
        

if __name__ == '__main__':
    unittest.main()
