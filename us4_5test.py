import unittest
from us4_5 import *

class UserStory04Tests(unittest.TestCase):
    def test1(self):
        #no marriage is fine
        self.assertTrue(marriage_before_divorce({},{}))

    def test2(self):
        m = {"year":2001, "month":1, "day":1}
        self.assertTrue(marriage_before_divorce(m,{}))

    def test3(self):
        #divorce without marriage is NOT fine
        d = {"year":2000, "month":1, "day":1}
        self.assertFalse(marriage_before_divorce({},d))

    def test4(self):
        #both events is fine
        m = {"year":2000, "month":1, "day":1}
        d = {"year":2019, "month":1, "day":1}
        self.assertTrue(marriage_before_divorce(m,d))

    def test5(self):
        #both events, with divorce first is NOT fine
        d = {"year":2000, "month":1, "day":1}
        m = {"year":2025, "month":1, "day":1}
        self.assertFalse(marriage_before_divorce(m,d))

class UserStory05Tests(unittest.TestCase):
    def test1(self):
        #no marriage is fine
        self.assertTrue(marriage_before_death({},{}))

    def test2(self):
        #marriage without death is fine
        m = {"year":2000, "month":1, "day":1}
        self.assertTrue(marriage_before_death(m,{}))

    def test3(self):
        #death without marriage is fine
        d = {"year":2000, "month":1, "day":1}
        self.assertTrue(marriage_before_death({},d))

    def test4(self):
        #both events, with marriage3 first is fine
        m = {"year":2000, "month":1, "day":1}
        d = {"year":2010, "month":1, "day":1}
        self.assertTrue(marriage_before_death(m,d))

    def test5(self):
        #both events, with death first is NOT fine
        d = {"year":2000, "month":1, "day":1}
        m = {"year":2010, "month":1, "day":1}
        self.assertFalse(marriage_before_death(m,d))
        

if __name__ == '__main__':
    unittest.main()