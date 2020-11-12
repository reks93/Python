# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 22:33:33 2020

@author: rekha
"""
#Question59:Write a Python program to remove a key from a dictionary.

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
    del my_new_dict[find_key]
    print("Key-Value pair deleted!",my_new_dict)
else:
    print("Entered key is not found!!")