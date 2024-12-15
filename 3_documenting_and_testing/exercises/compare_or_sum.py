#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for comparing two numbers. It compares two numbers and returns
    the smallest. If they are equal, it will sum both number.

Module contents:
    - compare_or_sum: Compares two arguments but if they are same, it
    will sum them

Created on 14.12.2024
@author: Abdul Qader Dost
"""


def compare_or_sum(number1: int, number2: int) -> int :
    """Compares number1 and number2 and returns the smallest number,
    but if they are equal, it will return their sum.
    
    Parameters:
        number1: int, float, the first number to be compared
        number2: int, float, the second number to be compared
        
    Returns -> int, the smallest number or if they are equal 
        it will return the sum.
    
    Raises:
        AssertionError: if the argument is not an int.
        
    >>> compare_or_sum(10,20)
    10

    >>> compare_or_sum(30,20)
    20
    
    >>> compare_or_sum(10,10)
    20
    """
    
    assert isinstance(number1, int), "input must be integer."
    assert isinstance(number2, int), "input must be integer."
    
    if number1 < number2:
        return number1
    elif number1 > number2:
        return number2
    else:
        return number1 + number2

