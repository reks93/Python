# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 23:11:51 2020

@author: rekha
"""
#Question46:Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#Example 1:
#Input: nums = [1,3,5,6], target = 5
#Output: 2
def index(target , nums):
    for i  in range(len(nums)):
        if nums[i] >= target:
            return i
    return i+1            

num = [1,3,5,6]
print("list is" , num)
target_1 = int(input("Enter the target"))
print(index( target_1 , num))

