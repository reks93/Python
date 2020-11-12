# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 21:00:25 2020

@author: rekha
"""
#Question 34: Write a Python class to find the three elements that sum to zero from a set of n real numbers. 
def findTriplets(arr, n): 
    found = False
    lis =[]
    new_lis = []
    for i in range(n - 1): 

        # Find all pairs with sum  
        # equals to "-arr[i]"  
        s = set() 
        for j in range(i + 1, n): 
            x = -(arr[i] + arr[j]) 
            if x in s: 
                lis = [ x, arr[i], arr[j]]
                found = True
                new_lis.append(lis)
            else: 
                s.add(arr[j])
                #print(s)
    print(new_lis)
    if found == False: 
        print("No Triplet Found") 
  
# Driver Code 
arr = [-25, -10, -7, -3, 2, 4, 8, 10]
n = len(arr) 
findTriplets(arr, n)