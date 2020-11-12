# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 22:02:27 2020

@author: rekha
"""
#Question 60: Write a Python class to get all possible unique subsets from a set of distinct integers.
#Input : [4, 5, 6]
#Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

length = int(input("enter the length of the list"))
inp_list =[]
for i in range(length):
    inp_list.append(input())
print("Input_list" , inp_list)

list2 = []
out_list= [list2]
#new = []
for i in range(len(inp_list)):
    #new = inp_list[i]
    slices = out_list[:] 
    #out_list.append(list(inp_list[i]))
    k = inp_list[i]
    for j in range(len(out_list)):
        #print("Out",out_list[j])
        out_list[j] = out_list[j] + [k]
    out_list =slices + out_list
print("Output list",out_list)