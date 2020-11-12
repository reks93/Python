# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 13:20:21 2020

@author: rekha
"""
#Question 61: Write a Pandas program to convert a dictionary to a Pandas series. Go to the editor 
#Original dictionary:
#{'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
#Converted series:
#a 100
#b 200
#c 300
#d 400
#e 800
#dtype: int64
import pandas as pd
print("Creating new dictionary:")
my_new_dict ={}
len_dict = int(input("Enter the number of items to be added:"))
for i in range(len_dict):
    key = input("Enter key :")
    value = input ("Enter Value:")
    my_new_dict[key] = value
print("Dictionary:\n")
new_Series= pd.Series(my_new_dict)
print("Panda series", new_Series)