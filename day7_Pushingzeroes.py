# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 22:29:16 2020

@author: Rekha
"""
def pushing_xeroes():
    len = int(input("Enter the length of the list \n"))
    list1 = []
    print("Enter the items of the list")
    for i in range(len):
        list1.append(int(input()))
    if (any(list1)):
        count =0
        for i in range(len):
            if list1[i] != 0:
                list1[count] = list1[i]
                count += 1
        while count < len:
            list1[count]= 0
            count +=1
            return list1
    else:
        print("All the items are 0")
        return list1
print("Output list with 0's at the end" , pushing_xeroes())