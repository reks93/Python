# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 22:20:48 2020

@author: Rekha
"""
#Question 9 : Swap the positions of the given two element list
#Input : ['2','4']
#Output : ['4','2']
def swap(list1):
    list1[0],list1[1] = list1[1],list1[0]
    return list1

list1 = []
print("Enter the elements in the list")
for i in range(2):
    list1.append(input())
print("Input list is" , list1)
print("Swapping the first and second element in a list" ,swap(list1))
