# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 22:29:51 2020

@author: rekha
"""
#Question 69: Write a Python program to calculate the area of a trapezoid.

val1 = float(input("Enter the base1 value"))
val2 = float(input("Enter the base1 value"))
height = float(input("Enter the height value"))

area = ((val1+val2)/2)*height
print('Area of trapezoid:', area)