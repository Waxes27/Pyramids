import unittest
from io import StringIO
import super_algos

class Test_super_algos(unittest.TestCase):
    def test_find_min(self):
        result = super_algos.find_min([-14,45,78,56,35])
        self.assertEqual(result,-14)

    def test_sum_all(self):
        result = super_algos.sum_all([1,2,3,4,5])
        self.assertEqual(result,15)
        result = super_algos.sum_all([-1,-2,-3,-4,-5])
        self.assertEqual(result,-15)
        result = super_algos.sum_all([-1,2,-3,4,-5])
        self.assertEqual(result,-3)

    def test_find_strings(self):
        result = super_algos.find_possible_strings(['a','b'],3)
        self.assertEqual(['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb'], result)
        result = super_algos.find_possible_strings(['a','b'],1)
        self.assertEqual(result,['a','b'])