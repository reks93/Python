# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 23:10:50 2020

@author: day49
"""
#Question 49: Write a Python program that accepts a string and calculate the number of digits and letters.
#Sample Data : Python 3.2
#Expected Output :
#Letters 6 
#Digits 2
input_str = input("Enter the string:")
num = 0
alp = 0
for i in input_str:
    if i.isalpha():
        alp +=1
    elif i.isdigit():
        num +=1
print("Letters", alp ,"\nDigits" , num )
        