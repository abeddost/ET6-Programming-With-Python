#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module generates a list of numbers from 0 to desired number.

Module contents:
    - count_up_to: generates a list of consecutive numbers from 0.

Created on 14.12.2024
@author: Abdul Qader Dost
"""

def count_up_to(length):
    """ 
    Parameters:
        length: int, the length of the list
    
    Returns:
        list, a list of consecutive numbers from 0.
    
    Raises:
        AssertionError: if the argument is not an integer
        AssertionError: if the argument is less than 0
        
    >>> count_up_to(5)
    [0, 1, 2, 3, 4]
    
    >>> count_up_to(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> count_up_to(0)
    []
    """
    
    assert isinstance(length, int), "sequence length is not an integer"
    assert length >= 0, "sequence length is less than 0"
    
    numbers_list = []

    current_number = 0
    while len(numbers_list) < length:
        numbers_list.append(current_number)
        current_number += 1

    return numbers_list
print(count_up_to(0))
