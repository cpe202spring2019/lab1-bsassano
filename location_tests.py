import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(loc2),"Location('Paris', 48.9, 2.4)")
        self.assertNotEqual(repr(loc2),"Location('SLO', 35.3, -120.7)")

    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = Location("SLO", 35.3, -120.7)
        loc4 = loc1
        self.assertTrue(loc1==loc3,True)
        self.assertTrue(loc1==loc4,True)
        self.assertFalse(loc1==loc2,False)
        self.assertFalse(loc2==loc4,False)
        self.assertFalse(loc1!=loc4,True)

        self.assertTrue(loc1.name=="SLO")
        self.assertTrue(loc1.lat==35.3)
        self.assertTrue(loc1.lon==-120.7)
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
