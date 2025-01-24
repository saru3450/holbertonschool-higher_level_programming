#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):

        self.assertEqual(max_integer([10, 25, 7]), 25)
        self.assertEqual(max_integer([12, 15, 9, 3]), 15)
        self.assertEqual(max_integer([-5, -2, -10, -1]), -1)
        self.assertEqual(max_integer([-12, 0, 3, 11, 6]), 11)
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([]), None)


        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
