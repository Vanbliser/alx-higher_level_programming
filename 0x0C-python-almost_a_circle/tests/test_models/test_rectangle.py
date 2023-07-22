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
        """test that private attribute is hidden"""
        r = Rectangle(5, 3)
        self.assertEqual(hasattr(r, "__nb_objects"), False)

    def test_attribute_id(self):
        """test the instance attribute id"""
        r = Rectangle(5, 3, id=12)
        self.assertEqual(r.id, 12)

    def test_all_attribute_correctly_passed(self):
        """test all attribute is passed"""
        r = Rectangle(5, 3, 2, 1, id=12)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, 1)

    def test_attribute_width(self):
        """test correct attribute is passed"""
        self.assertRaises(ValueError, Rectangle, -1, 1)
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(TypeError, Rectangle, 3.4, 1)
        self.assertRaises(TypeError, Rectangle, "3.4", 1)
        self.assertRaises(TypeError, Rectangle, [1, 2], 1)
        self.assertRaises(TypeError, Rectangle, (1, 2), 1)
        self.assertRaises(TypeError, Rectangle, {"1": 1}, 1)
        r = Rectangle(5, 1)
        self.assertEqual(r.width, 5)

    def test_attribute_height(self):
        """test correct attribute is passed"""
        self.assertRaises(ValueError, Rectangle, 1, -1)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(TypeError, Rectangle, 1, 3.4)
        self.assertRaises(TypeError, Rectangle, 1, "3.4")
        self.assertRaises(TypeError, Rectangle, 1, [1, 2])
        self.assertRaises(TypeError, Rectangle, 1, (1, 2))
        self.assertRaises(TypeError, Rectangle, 1, {"1": 1})
        r = Rectangle(5, 1)
        self.assertEqual(r.height, 1)

    def test_attribute_x(self):
        """test correct attribute is passed"""
        self.assertRaises(ValueError, Rectangle, 1, 1, x=-1)
        self.assertRaises(TypeError, Rectangle, 1, 1, x=3.4)
        self.assertRaises(TypeError, Rectangle, 1, 1, x="3.4")
        self.assertRaises(TypeError, Rectangle, 1, 1, x=[1, 2])
        self.assertRaises(TypeError, Rectangle, 1, 1, x=(1, 2))
        self.assertRaises(TypeError, Rectangle, 1, 1, x={"1": 1})
        r = Rectangle(1, 1, x=5)
        self.assertEqual(r.x, 5)
        r1 = Rectangle(1, 1, x=0)
        self.assertEqual(r1.x, 0)
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.x, 0)

    def test_attribute_y(self):
        """test correct attribute is passed"""
        self.assertRaises(ValueError, Rectangle, 1, 1, y=-1)
        self.assertRaises(TypeError, Rectangle, 1, 1, y=3.4)
        self.assertRaises(TypeError, Rectangle, 1, 1, y="3.4")
        self.assertRaises(TypeError, Rectangle, 1, 1, y=[1, 2])
        self.assertRaises(TypeError, Rectangle, 1, 1, y=(1, 2))
        self.assertRaises(TypeError, Rectangle, 1, 1, y={"1": 1})
        r = Rectangle(1, 1, y=5)
        self.assertEqual(r.y, 5)
        r1 = Rectangle(1, 1, y=0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.y, 0)
