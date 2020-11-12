# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 22:17:43 2020

@author: rekha
"""
#Question 68: Write a Python program to double all numbers of a given list of integers. Use Python map

def add(n1):
    return n1+n1

num1 =(2,4,5,6,8)
add_result = map(add , num1)
print(list(add_result))
