# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 22:25:35 2020

@author: Rekha
"""
print("Creating new dictionary:")
my_new_dict ={}
len_dict = int(input("Enter the number of items to be added:"))
for i in range(len_dict):
    key = input("Enter key :")
    value = input ("Enter Value:")
    my_new_dict[key] = value
print("Dictionary:\n")
for key,val in my_new_dict.items():
    print (key, "=>", val)
find_key = input("Enter the key to be found")
if find_key in my_new_dict:
    print("Entered key is available and its value is :" , my_new_dict[find_key])
else:
    print("Entered key is not found!!")