#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for adding two numbers.

Module contents:
    - sum_of_two_nums: Returns the sum of two float numbers.

Created on 12.09.2024
@author: Abdul Qader Dost
"""

def sum_of_two_numbers(number_1: float, number_2:float) -> float:
    """ Adds two float numbers and returns the sum. 
    
    Parameters:
        number_1: int or float, the first number to be added
        number_2: int or float, the second number to be added
    
    Returns -> The sum of number_1 and number_2  
    
    Raises:
        AssertionError: if the argument is not an integer or float.
    
    >>> sum_of_two_numbers(3,6)
    9
    
    >>> sum_of_two_numbers(-5,10)
    5
    
    >>> sum_of_two_numbers(-3,-6)
    -9
    
    """
    
    # The number_1 and number_2 must be an integer or a float 
    assert isinstance(number_1, (int, float)), "number_1 is not an integer or a float"
    assert isinstance(number_2, (int, float)), "number_2 is not an integer or a float"
    
    # Returns the sum of two numbers
    return  number_1 + number_2
