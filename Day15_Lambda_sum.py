# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 00:08:27 2020

@author: Rekha
"""
#Question 15: Use lambda function to find the sum of three numbers

print("Enter the numbers")
x = lambda a, b, c : a + b + c
print("Sum is" , x( int(input("num1")),int(input("num2")),int(input("num3"))))