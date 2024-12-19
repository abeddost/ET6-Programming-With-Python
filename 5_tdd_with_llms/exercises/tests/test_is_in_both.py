#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from ..is_in_both import is_in_both

class TestIsInBoth(unittest.TestCase):

  def test_false_example(self):
    self.assertFalse(is_in_both("a", ["1","2","3","4","5"],["a","b","c","d"]))

  def test_true_example(self):
    self.assertTrue(is_in_both("a", ["a","2","3","4","5"],["a","b","c","d"]))

  def test_third_example(self):
    self.assertTrue(is_in_both("d", ["a","g","d"],["m","n","c","d"]))
  
  def test_empty_lists(self):
      self.assertFalse(is_in_both("a", [], []))
      self.assertFalse(is_in_both("", ["a"], ["b"]))
      self.assertFalse(is_in_both("a", ["a"], []))

  def test_duplicate_item(self):
      self.assertTrue(is_in_both("a", ["a","a","b"],["a","b","c"]))

  def test_not_in_any_list(self):
      self.assertFalse(is_in_both("z", ["a","b","c"],["x","y","z"]))

  def test_only_one_list(self):
      self.assertFalse(is_in_both("a", ["a","b","c"],["d","e","f"]))

  def test_large_lists(self):
      large_list1 = [str(i) for i in range(100000)]
      large_list2 = [str(i) for i in range(200000)]
      self.assertTrue(is_in_both("50000", large_list1, large_list2))
  
  def test_string_argument(self):
      with self.assertRaises(AssertionError):
          is_in_both(123, ["a", "b", "c"], ["d", "e", "f"])

  def test_second_list_argument(self):
      with self.assertRaises(AssertionError):
          is_in_both("a", "not a list", [])

  def test_third_list_argument(self):
      with self.assertRaises(AssertionError):
          is_in_both("a", [], "not a list")


if __name__ == '__main__':
    unittest.main()
