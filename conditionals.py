#!/bin/python3
"""
    This module demonstrates the use of conditional statements in Python.

    Conditionals are used to execute certain pieces of code based on whether a condition is true or false.
    The most common conditional statements in Python are `if`, `elif`, and `else`.

    Examples:
        if condition:
            # code to execute if condition is true
        elif another_condition:
            # code to execute if another_condition is true
        else:
            # code to execute if none of the above conditions are true

    This module provides examples and explanations to help beginners understand how to use these conditional statements effectively.
    Task:
    Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
    """

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input('Enter a number: ').strip())
    """Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird"""

    #Here is a simple way to make it, but it isn't the best one
    if n % 2 == 1:  # Si es impar
        print('Weird')
    elif 2 <= n <= 5:  # Si es par y está entre 2 y 5
        print('Not Weird')
    elif 6 <= n <= 20:  # Si es par y está entre 6 y 20
        print('Weird')
    else:  # Si es par y mayor que 20
        print('Not Weird')

"""This is a optimized way to do it. Remove the above comments if you want to check it and coment the previous code """
# if n % 2 == 1 or (6 <= n <= 20):
#         print('Weird')
# else:
#     print('Not Weird')
