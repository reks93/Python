# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 23:44:17 2020

@author: rekha
"""
#Question42:You are climbing a stair case. It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#Example 1:
#Input: 2 Output: 2 Explanation: There are two ways to climb to the top. 1. 1 step + 1 step 2. 2 steps 
#Example 2: 
#Input: 3 Output: 3 Explanation: There are three ways to climb to the top. 1. 1 step + 1 step + 1 step 2. 1 step + 2 steps 3. 2 steps + 1 step

def climbStairs( n):
   if n == 1:
       return 1
   """
   if n == 2:
       return 2
   return climbStairs(n-1)+climbStairs(n-2)
"""
   a, b = 1, 2
   for i in range(2, n):
       tmp = b
       b = a+b
       a = tmp
   return b

input_Steps = int(input("Enter the number of steps to reach the top"))
print(climbStairs(input_Steps))