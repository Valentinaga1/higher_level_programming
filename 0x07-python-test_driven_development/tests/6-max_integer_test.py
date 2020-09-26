#!/usr/bin/python3
"""Test Module
"""
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
	"""Test for max_integer function
	"""
	 def test_max_integer(self):
        '''
        check valid cases:
        '''
        self.assertEqual(max_integer([6, 2, 3, 4]), 6)
        self.assertEqual(max_integer([-6, -2, -13, -4]), -2)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([3, 3, 3]), 3)
        self.assertEqual(max_integer([-2.2, -3.1, 4.1]), 4.1)

    def test_list_empty(self):
        '''
        check list empty
        '''
        self.assertEqual(max_integer([]), None)

    def test_typelist(self):
        '''
        check the diferent type of argument
        '''
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, ["str", 1, 3, 6])

if __name__ == '__main__':
    unittest.main()