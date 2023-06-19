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

    def test_private_attribute_is_hidden(self):
        r = Rectangle(5, 3)
        self.assertEqual(hasattr(r, "__nb_objects"), False)

    def test_attribute_id(self):
        """test the instance attribute id"""
        r = Rectangle(5, 3)
        self.assertEqual(r.id, 1)
        r1 = Rectangle(5, 3, id=12)
        self.assertEqual(r1.id, 12)
        r2 = Rectangle(5, 3)
        self.assertEqual(r2.id, 2)

    def test_public_attributes(self):
        """test correct attribute is passed"""
        r = Rectangle(5, 3, 2, 1, 12)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)
