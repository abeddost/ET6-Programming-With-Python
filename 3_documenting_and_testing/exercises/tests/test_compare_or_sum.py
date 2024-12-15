#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 14.12.2024

@author: Abdul Qader Dost
"""

import unittest

from ..compare_or_sum import compare_or_sum

class TestCompareOrGet(unittest.TestCase):
    """ Test the compare_or_sum Function """

    def test_minimal_input(self):
        """Test when both numbers are equal to 0."""
        self.assertEqual(compare_or_sum(0, 0), 0)

    def test_number1_smaller(self):
        """Test when number1 is smaller than number2."""
        self.assertEqual(compare_or_sum(5, 10), 5)

    def test_number2_smaller(self):
        """Test when number2 is smaller than number1."""
        self.assertEqual(compare_or_sum(50, 20), 20)

    def test_both_numbers_equal(self):
        """Test when both numbers are equal."""
        self.assertEqual(compare_or_sum(-10, -10), -20)

    def test_one_number_positive_one_negative(self):
        """Test when one number is positive and the other is negative."""
        self.assertEqual(compare_or_sum(-10, 10), -10)

    def test_large_positive_numbers(self):
        """Test when both numbers are large positive numbers."""
        self.assertEqual(compare_or_sum(1000000, 1000000), 2000000)

    def test_large_mixed_numbers(self):
        """Test when one number is large negative and the other is large positive."""
        self.assertEqual(compare_or_sum(-1000000, 500000), -1000000)

    def test_large_negative_numbers(self):
        """Test when both numbers are large negative numbers."""
        self.assertEqual(compare_or_sum(-1000000, -1000000), -2000000)

    def test_zero_and_positive(self):
        """Test when one number is zero and the other is positive."""
        self.assertEqual(compare_or_sum(0, 20), 0)

    def test_zero_and_negative(self):
        """Test when one number is zero and the other is negative."""
        self.assertEqual(compare_or_sum(0, -20), -20)

    def test_both_zero(self):
        """Test when both numbers are zero."""
        self.assertEqual(compare_or_sum(0, 0), 0)

    def test_different_signs(self):
        """Test when numbers have different signs."""
        self.assertEqual(compare_or_sum(-100, 50), -100)

    def test_equal_negative_numbers(self):
        """Test when both numbers are equal and negative."""
        self.assertEqual(compare_or_sum(-1, -1), -2)

    def test_extremely_large_numbers(self):
        """Test with extremely large numbers."""
        self.assertEqual(compare_or_sum(int(1e100), int(1e100)), int(2e100))
        
    def test_non_integer_input_number1(self):
        """Test when the first argument is not an integer (float)."""
        with self.assertRaises(AssertionError):
            compare_or_sum(10.5, 20)

    def test_non_integer_input_number2(self):
        """Test when the second argument is not an integer (string)."""
        with self.assertRaises(AssertionError):
            compare_or_sum(10, "20")

    def test_non_integer_input_both(self):
        """Test when both arguments are not integers (string and float)."""
        with self.assertRaises(AssertionError):
            compare_or_sum("10", 20)

    def test_non_integer_input_both_float(self):
        """Test when both arguments are floats."""
        with self.assertRaises(AssertionError):
            compare_or_sum(10.5, 20.5)

    # Edge case tests

    def test_maximum_integer_value(self):
        """Test with the maximum possible integer value."""
        max_int = 2147483647
        self.assertEqual(compare_or_sum(max_int, max_int), max_int * 2)

    def test_minimum_integer_value(self):
        """Test with the minimum possible integer value."""
        min_int = -2147483648
        self.assertEqual(compare_or_sum(min_int, min_int), min_int * 2)
