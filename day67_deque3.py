# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 22:11:23 2020

@author: rekha
"""
#Question 67: Write a Python program to create a new deque with three items and iterate over the deque's elements.

from collections import deque

queue1 = deque(['a','b','c'])

for element in queue1:
    print(element)