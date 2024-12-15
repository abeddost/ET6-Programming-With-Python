#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 14.12.2024

@author: Abdul Qader Dost
"""

import unittest

from ..get_length import get_length

class TestGetList(unittest.TestCase):
    """ """

    def test_empty_list_input(self):
        """It should return None"""
        self.assertEqual(get_length([]), None)

    def test_empty_string_input(self):
        """It should return None"""
        self.assertEqual(get_length(''), None)
        
    def test_string_input(self):
        """Testing a string as input"""
        self.assertEqual(get_length('Abdul'), 5)

    def test_list_input(self):
        """Testing a list as input"""
        self.assertEqual(get_length([1,2,3,4,5,8]), 6)
        
    def test_tuple_input(self):
        """Testing a tuple as input"""
        self.assertEqual(get_length((65,32,523,64)), 4)

    def test_dict_input(self):
        """Testing a dictionary as input"""
        self.assertEqual(get_length({"Name": "Abed", "Age": 27}), 2)
        
    def test_nested_iterable_input(self):
        """Testing lists inside list"""
        self.assertEqual(get_length([[1,2],[2,4]]), 2)   
        
    def test_large_string_input(self):
        """It should return the length of a large string."""
        self.assertEqual(get_length("a" * 10000), 10000)
        
    def test_single_element_list(self):
        """It should handle a single-element list."""
        self.assertEqual(get_length([42]), 1)

    def test_single_character_string(self):
        """It should handle a single-character string."""
        self.assertEqual(get_length('a'), 1)

    def test_invalid_int_input(self):
        """It should raise AssertionError for an int."""
        with self.assertRaises(AssertionError):
            get_length(42)

    def test_invalid_float_input(self):
        """It should raise AssertionError for a float."""
        with self.assertRaises(AssertionError):
            get_length(3.14)

    def test_none_input(self):
        """It should raise AssertionError for None."""
        with self.assertRaises(AssertionError):
            get_length(None)

    def test_function_input(self):
        """It should raise AssertionError for a function."""
        with self.assertRaises(AssertionError):
            get_length(get_length)

    def test_generator_input(self):
        """It should raise AssertionError for a generator."""
        with self.assertRaises(AssertionError):
            get_length(x for x in range(10))

    def test_boolean_input(self):
        """It should raise AssertionError for boolean values."""
        with self.assertRaises(AssertionError):
            get_length(True)
        with self.assertRaises(AssertionError):
            get_length(False)
        
    