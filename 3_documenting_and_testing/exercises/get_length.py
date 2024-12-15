#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for finding the length of the input.

Module contents:
    - get_length: counts the length of the input.

Created on 12.14.2024
@author: Abdul Qader Dost
"""


def get_length(input) -> int:
    """ Calculates the length of input and returns the result

    Parameters: 
        Input: any iterable like: Strings, Lists, Tuples or Dictionaries
        
    Returns -> int, The length of input
    
    Raises:
        AssertionError: if the argument is not an iterable. (int, float
        NoneType)
        
    >>> get_length([1,2,3,4])
    4
    
    >>> get_length("asikardirzaatihak")
    17
    
    >>> get_length((5,4,3))
    3
    """
    # The input should be iterable
    
    assert isinstance(input, (str, list, tuple, dict, set)), "Input should be iterable"

    
    # Will return none if the input is empty
    if len(input) == 0:
        return None

    return len(input)
