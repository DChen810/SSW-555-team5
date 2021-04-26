import unittest
from project10 import *
class test_Index(unittest.TestCase):
  
    def test_most_dead_year(self):
        textcase=function('Project01_Gengwu_Zhao.ged') 
        self.assertTrue(textcase.most_dead_year()==2014)

    def test_Adult_unmarried(self):
        textcase=function('Project01_Gengwu_Zhao.ged')
        li=textcase.Adult_unmarried()
        self.assertTrue(textcase.indi['I19'] in li)
        self.assertTrue(textcase.indi['I26'] in li)
        self.assertTrue(textcase.indi['I27'] not in li)
        self.assertTrue(textcase.indi['I28'] in li)

    def test_age_10_cp(self):
        textcase=function('Project01_Gengwu_Zhao.ged')
        li=textcase.age_10_cp()
        self.assertTrue(textcase.fami['F23'] in li)
        self.assertTrue(len(li)==1)
        
    def test_same_gender_cp(self):
        textcase=function('Project01_Gengwu_Zhao.ged')   
        li=textcase.same_gender_cp()
        self.assertTrue(textcase.fami['F23'] not in li)
        self.assertTrue(len(li)==0)

    def test_chil_older_p(self):
        textcase=function('Project01_Gengwu_Zhao.ged')  
        li=textcase.chil_older_p()
        self.assertTrue('F23' == li[0].id)
        self.assertTrue(len(li)==1)
        

    def test_chil_dead_bf_p(self):
        textcase=function('Project01_Gengwu_Zhao.ged')
        li=textcase.chil_dead_bf_p()
        self.assertTrue('F23' == li[0].id)
        self.assertTrue(len(li)==1)

if __name__ == '__main__':
    unittest.main(verbosity=2)