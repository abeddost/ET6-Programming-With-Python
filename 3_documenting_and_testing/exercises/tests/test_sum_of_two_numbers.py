#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 12.09.2024

@author: Abdul Qader Dost
"""

import unittest

from ..sum_of_two_numbers import sum_of_two_numbers

class TestSumNumbers(unittest.TestCase):
    """ Test the summation of two numbers. """

    def test_0(self):
        """It should sum 50 and -20 and return 30 as result"""
        actual = sum_of_two_numbers(50,-20) # call function with test arguments
        expected = 30 # hand-write the expected return value
        self.assertEqual(actual, expected)
        
    def test_1(self):
        """It should sum -40 and 20 and return -20 as result"""
        actual = sum_of_two_numbers(-40,20) # call function with test arguments
        expected = -20 # hand-write the expected return value
        self.assertEqual(actual, expected)
        
    def test_2(self):
        """It should sum -40 and -20 and return -60 as result"""
        actual = sum_of_two_numbers(-40,-20) # call function with test arguments
        expected = -60 # hand-write the expected return value
        self.assertEqual(actual, expected)

    def test_not_a_number(self):
        """It should raise an assertion error if the argument is not a float or integer"""
        with self.assertRaises(AssertionError):
            sum_of_two_numbers("a", 5)
            
    def test_large_integers(self):
        a = 10**1000  # A very large integer
        b = 10**1000
        result = sum_of_two_numbers(a, b)
        self.assertEqual(result, a + b)  # Ensure it adds correctly, no overflow
        
    def test_floating_point_precision(self):
        a = 1e100  # A very large floating-point number
        b = 1
        result = sum_of_two_numbers(a, b)
        self.assertEqual(result, a + b)  # Ensure that the addition is handled correctly
        
    