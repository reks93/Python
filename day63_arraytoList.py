# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 23:09:01 2020

@author: rekha
"""
# Question 63: Write a Python program to convert an array to an ordinary list with the same items.

from array import *

my_array = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: ",str(my_array))
num_list = my_array.tolist()
print(num_list)

