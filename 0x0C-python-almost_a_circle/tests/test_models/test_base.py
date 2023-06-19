#!/usr/bin/python3
"""a test file"""


import unittest

from models.base import Base


class Test(unittest.TestCase):
    """TestCase for class"""

    def test_type(self):
        """test the type of Base"""
        b = Base()
        self.assertIsInstance(b, Base)

    def test_attribute_id(self):
        """test the instance attribute id"""
        b = Base()
        self.assertEqual(b.id, 1)
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)

    def test_private_attribute_is_hidden(self):
        b = Base()
        self.assertEqual(hasattr(b, "__nb_objects"), False)
