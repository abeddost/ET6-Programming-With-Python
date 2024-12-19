#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_in_both(string:str, list1:list, list2:list) -> list:

  """ Is in Both

  Function will take in a string and two lists of strings. 
  It will return true if the item is in _both_ of the lists.

  Parameters:
      string: str, The string that will be checked by the function
      list1: list, The first list
      list2: list, The second list.
      
  Returns:
      Returns a Boolean. (True or False)  
      
  Raises:
    AssertionError: If the first argument is not a string
    AssertionError: If the second argument is not a list
    AssertionError: If the third argument is not a list
      
  >>> is_in_both("a", ["1","2","3","4","5"],["a","b","c","d"])
  False

  >>> is_in_both("a", ["a","2","3","4","5"],["a","b","c","d"])
  True

  >>> is_in_both("d", ["a","g","d"],["m","n","c","d"])
  True

  """
  assert isinstance(string, str), "string must be str type"
  assert isinstance(list1, list), "list1 must be a list"
  assert isinstance(list2, list), "list1 must be a list"
  
  
  return string in list1 and string in list2 
