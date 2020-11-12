# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 23:14:36 2020

@author: bairavi
"""
#Question 64: Write a Python program to add more number of elements to a deque object from an iterable object.

import collections

tuple_1 = (2, 4, 6, 8, 10)
my_deque = collections.deque(tuple_1)
print("original_deque" , my_deque)
print("Extending Deque..")
even_nums = (12,58,64,36)
my_deque.extend(tuple_1)
print(my_deque)