# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 23:23:18 2020

@author: rekha
"""
#Question 35: Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence.

arr =[]
arr_numeric =[]
input_bin_Str = input("Enter the sequence of 4 digit binary nums separated by ,")
arr = input_bin_Str.split(',')
for i in arr:
    input_int = int(i,2)
    if input_int % 5 == 0 :
        arr_numeric.append(i)
print(",".join(arr_numeric))