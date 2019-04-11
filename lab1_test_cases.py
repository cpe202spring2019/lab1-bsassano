import unittest
from lab1 import *
from math import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([1,3,5]),5)
        self.assertEqual(max_list_iter([5,3,1]),5)
        self.assertEqual(max_list_iter([1,5,3]),5)

        self.assertEqual(max_list_iter([1,1,1,1,1]),1)
        self.assertEqual(max_list_iter([1,4,2,8,6,9]),9)
        self.assertEqual(max_list_iter([0,0,0,1,0]),1)

        self.assertEqual(max_list_iter([2.5,2.51,2.52]),2.52)
        self.assertEqual(max_list_iter([2.5,pi,0]),pi)
        self.assertEqual(max_list_iter([]),None)

    def test_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1,1,1]),[1,1,1])
        self.assertEqual(reverse_rec([2.5,3.5,4.5]),[4.5,3.5,2.5])

        self.assertEqual(reverse_rec([]),[])
        self.assertEqual(reverse_rec([1]),[1])
        self.assertEqual(reverse_rec([1,0,1,1]), [1,1,0,1])

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        tlist = None
        with self.assertRaises(ValueError):
            bin_search(5,0,9,tlist)
        self.assertEqual(bin_search(4,0,len(list_val)-1,list_val),4 )
        self.assertEqual(bin_search(10,0,5,[5,10,15,20,25,30]),1)
        self.assertEqual(bin_search(3,0,3,[1,2,3,4]),2)

        self.assertEqual(bin_search(3,0,3,[1,2,4,5]),None)
        self.assertEqual(bin_search(5,0,9,[1,2,3,4,5,6,7,8,9,10]),4)
        self.assertEqual(bin_search(2,0,4,[0,0,0,0,0]),None)

        self.assertEqual(bin_search(2,0,4,[0,0,0,0,2]),4)
        self.assertEqual(bin_search(1, 0, 2, [1,2,3]), 0)
        self.assertEqual(bin_search(100,0,14,[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]),9)

if __name__ == "__main__":
        unittest.main()

    
