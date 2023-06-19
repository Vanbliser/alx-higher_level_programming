#!/usr/bin/python3
"""test module"""


import unittest

from models.rectangle import Rectangle


class Test(unittest.TestCase):
    """TestCase"""

    def test_instantiation(self):
        """test for object instantiation"""
        r = Rectangle(5, 3)
        self.assertIsInstance(r, Rectangle)

    def test_attributes(self):
        """test correct attribute is passed"""
        r = Rectangle(5, 3, 2, 1, 12)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)

