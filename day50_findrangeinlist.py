# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 22:17:24 2020

@author: rekha
"""
#Question 50 -Write a Python program to count the number of elements in a list within a specified range.
list1 = [10,20,30,40,40,40,70,80,99]
min_range = int(input("Enter the min range"))
max_range = int(input("Enter the max range"))
num = 0
for i in list1:
    if max_range>=i>=min_range:
        num += 1
print("count:" ,num)