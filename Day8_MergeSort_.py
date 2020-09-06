# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 11:23:57 2020

@author: Rekha
"""
#Question 8 : Sort a tuple containing 10 numbers in ascending order using merge sort

def merge_Sort(input_list):
    if len(input_list) <=1:
        return input_list
    else:
       left_list,right_list =  split(input_list)
       return merging_lists(merge_Sort(left_list) , merge_Sort(right_list))
    
def split(input_list):
    mid = len(input_list) //2 
    return input_list[:mid] , input_list[mid:]    

def merging_lists(left , right):
    i = 0 
    j = 0
    mer=[]
    max_length = len(left) + len(right)
    if len(left) == 0:
        return right
    elif len(right) == 0:
        return left
    while len(mer) < max_length:
        if(left[i] <= right[j]):
            mer.append(left[i])
            i +=1
        else:
            mer.append(right[j])
            j +=1
        if j == len(right):
            mer += left[i:]
            break
        elif i == len(left):
            mer += right[j:]
            break
    print("Merge sort" , tuple(mer))
    return tuple(mer)

input_list = []
len_ip_list =int(input("Enter the length of the input list"))
print("Enter the elements of the list")
for i in range(len_ip_list):
    input_list.append(int(input()))
merge_Sort(input_list)
