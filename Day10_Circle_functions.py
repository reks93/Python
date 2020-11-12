# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 22:45:23 2020

@author: Rekha
"""
#Question 10: Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle
import math

print("Python classes and methods using Circle class")
class circle:
    def __init__(self , rad):
        self.rad = rad
    def Circumf(self):
        print("Circumference of the circle is" , round((2*math.pi*self.rad) , 3))
    def area(self):
        print("Area of the circle is",round((math.pi*self.rad**2),3))
rad= float(input("Enter the radius of the circle"))
if rad < 0:
    print("Radius cannot be negative!!!")
else:
    c= circle(rad)
    c.area()
    c.Circumf()