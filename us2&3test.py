import unittest
from main import *

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