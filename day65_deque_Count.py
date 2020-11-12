# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 23:18:55 2020

@author: rekha
"""
#Question 65: Write a Python program to count the number of times a specific element presents in a deque object.

import collections

tuple_1 = (2, 4, 6, 8, 10,2, 4, 6, 8, 10,2, 4, 6, 8, 10,8)
my_deque = collections.deque(tuple_1)
print("original_deque" , my_deque)
int_find = int(input("Enter a number to count the occurence in the original Deque"))
print(my_deque.count(int_find))