import unittest
from index import *
class test_Index(unittest.TestCase):
    def test_the(self):
        textcase=function('Project01_Gengwu_Zhao.ged')
        textcase.PPrint()
        unmarried=textcase.unmarried_list()
        age=textcase.find_age(7)
        get_adults=textcase.get_adults()
        twins=textcase.get_twins()
        for i in unmarried:
            self.assertTrue(i.married==False)
        for i in age:
            self.assertTrue(i.age==7)
        for i in get_adults:
            self.assertTrue(i.age>=18)
        for i in twins:
            i=list(i)
            self.assertTrue(i[0].age==i[1].age)
if __name__ == '__main__':
    unittest.main()