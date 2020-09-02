# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 22:46:11 2020

@author: Rekha
"""
#Question 5: Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second.
print("My Program to append 2 lists")
list1len = int(input("Enter length of list 1"))
list2len = int(input("Enter length of list 2"))
list1= []
list2= []
list3 = []
print("Enter list1 elements")
for i in range(list1len):
    v = int(input("Element"))
    list1.append(v)
print(list1)
print("Enter list2 elements")
for j in range(list2len):
    y = int(input("Element"))
    list2.append(y)
print(list2)
list1 = list1[1::2]
list2 = list2[0::2]
print("odd index list :", list1)
print("even index list :", list2)
list3.extend(list1)
list3.extend(list2)
print("consolidted list :", list3)