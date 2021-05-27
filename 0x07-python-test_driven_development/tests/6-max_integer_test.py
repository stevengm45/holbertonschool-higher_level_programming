#!/usr/bin/python3
"""Unittest in max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """testing class for max_integer"""

    def test_positive_num(self):
        """Test numbers positive in list"""
        i = [1, 2, 6, 8, 19, 44, 50, 97]
        self.assertEqual(max_integer(i), 97)

    def test_num_begging(self):
        """Test number max begging"""
        i = [54, 9, 7, 28, 10, 36]
        self.assertEqual(max_integer(i), 54)

    def test_empty(self):
        """Test with empty list []"""
        self.assertRaises(max_integer([]), None)

    def test_one_arg(self):
        """Test with a argument in list"""
        i = [1]
        self.assertEqual(max_integer(i), 1)

    def test_negative_num(self):
        """Test with a number negative in list"""
        i = [5, 32, -7, 41, 8]
        self.assertEqual(max_integer(i), 41)

    def test_all_negative(self):
        """Test with all numbers negative in list"""
        i = [-8, -99, -3, -1, -50]
        self.assertEqual(max_integer(i), -1)

    def test_string(self):
        """Test with a string in list"""
        max_integer("hello") == 'i'
        self.assertRaises(TypeError, max_integer, [1, 2, 3, "Hello"])
