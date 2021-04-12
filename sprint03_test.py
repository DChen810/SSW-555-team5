import unittest
from sprint03 import *
class test_Index(unittest.TestCase):
  
    def test_us12(self):
        textcase=function('Project01_Gengwu_Zhao.ged')        
        faimly_name=list(textcase.list_families())
        self.assertTrue(len(faimly_name)==1)
        self.assertTrue('F23' in faimly_name)

    def test_us14(self):
        textcase=function('Project01_Gengwu_Zhao.ged')        
        sort_c=textcase.sort_children_num()
        self.assertTrue(len(sort_c)==6)
        self.assertTrue(sort_c[0][0]==0)
        self.assertTrue(sort_c[1][0]==0)
        self.assertTrue(sort_c[2][0]==0)
        self.assertTrue(sort_c[3][0]==0)
        self.assertTrue(sort_c[4][0]==4)
        self.assertTrue(sort_c[5][0]==4)

        self.assertTrue(sort_c[0][1]=='I19')
        self.assertTrue(sort_c[1][1]=='I26')
        self.assertTrue(sort_c[2][1]=='I27')
        self.assertTrue(sort_c[3][1]=='I28')
        self.assertTrue(sort_c[4][1]=='I01')
        self.assertTrue(sort_c[5][1]=='I07')

        

    def test_us23(self):
        textcase=function('Project01_Gengwu_Zhao.ged')        
        withoutc=textcase.without_children()
        self.assertTrue(len(withoutc)==4)
        self.assertTrue('I19' in withoutc)
        self.assertTrue('I26' in withoutc)
        self.assertTrue('I27' in withoutc)
        self.assertTrue('I28' in withoutc)
        

    def test_us28(self):
        textcase=function('Project01_Gengwu_Zhao.ged')        
        singlep=textcase.single_parents_child()
        self.assertTrue(len(singlep)==4)
        self.assertTrue('I19' in singlep)
        self.assertTrue('I26' in singlep)
        self.assertTrue('I27' in singlep)
        self.assertTrue('I28' in singlep)
        

    def test_us29(self):
        textcase=function('Project01_Gengwu_Zhao.ged')        
        odd=textcase.odd_age()
        for i in odd:
            self.assertTrue(textcase.indi[i].age%2!=0)        
        self.assertTrue('I01' in odd)
        self.assertTrue('I07' in odd)
        self.assertTrue('I27' in odd)
        self.assertTrue('I28' in odd)
        

    def test_us30(self):
        textcase=function('Project01_Gengwu_Zhao.ged')
        self.assertTrue(textcase.check_parents_num())

if __name__ == '__main__':
    unittest.main(verbosity=2)
