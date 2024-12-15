#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Evan Cole
"""

import unittest

from ..count_up_to import count_up_to

class TestCountUpTo(unittest.TestCase):
    """ Test for count_up_to Function """

    def test_minimal_input(self):
        """Test for minimal input of 0"""
        self.assertEqual(count_up_to(0), [])

    def test_5_as_input(self):
        """Test for a typical input"""
        self.assertEqual(count_up_to(5), [0, 1, 2, 3, 4])

    def test_large_input(self):
        """Test for a larger input"""
        self.assertEqual(count_up_to(10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    def test_negative_input(self):
        """Test for a negative input, expecting an assertion error"""
        with self.assertRaises(AssertionError):
            count_up_to(-1)
            
    def test_non_integer_input(self):
        """Test for a non-integer input, expecting an assertion error"""
        with self.assertRaises(AssertionError):
            count_up_to(5.5)
        with self.assertRaises(AssertionError):
            count_up_to("5")
    