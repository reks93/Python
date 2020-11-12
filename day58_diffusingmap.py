# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 13:23:31 2020

@author: rekha
"""
#Question 59: Write a Python program to add two given lists and find the difference between lists. Use map() function.

list1 = [1, 2, 3,45]
list2 = [4, 5, 6,90]
print("list before:", list1 , "\n" , list2)
result_add = map(lambda x, y: x + y, list1, list2)
result_diff = map(lambda x, y: x - y, list1, list2)
print("\nResult:after adding two list" , list(result_add) )
print("\nResult:difference of two list" , list(result_diff) )
