# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 21:02:46 2020

@author: bairavi
"""
#Question 3: Given a string, display only those characters which are present at an even index number.
#Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string
print("Program to print only the characters at even index")
str1 = input("Enter the string")
for j in range(1,len(str1),2):
    print(str1[j])
print("Program to remove characters upto given range")
range = int(input("Enter the range to remove characters"))
print(str1[range:])