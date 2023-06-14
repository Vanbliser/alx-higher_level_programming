#!/usr/bin/python3
"""test module for max_integer(list=[]), a function to find and return the max
integer in a list of integers. If the list is empty, the function returns None
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestFor_max_integer(unittest.TestCase):
    """a subclass of the unittest.TestCase class"""

    def test_parameter_type(self):
        """test incorrect being passed"""

        self.assertRaises(TypeError, max_integer, 5)
        self.assertRaises(TypeError, max_integer, 's')
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1, 5, 3]), 5)
    
    def test_list_of_integers(self):
        """test if the list has elements of type integer"""

        self.assertRaises(TypeError, max_integer, [1, '7', 5])
        self.assertRaises(TypeError, max_integer, [1, None, 5])
        self.assertRaises(TypeError, max_integer, [1, True, 5])

    def test_correct_parameters(self):
        """test the the function behaves as intended for rigth parameters"""

        self.assertEqual(max_integer([1,2,2]), 2)
        self.assertEqual(max_integer([1,1,1]), 1)
        self.assertEqual(max_integer([0,0,0]), 0)
        self.assertEqual(max_integer([1,2,3]), 3)
