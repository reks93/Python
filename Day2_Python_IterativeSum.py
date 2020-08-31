# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 19:41:26 2020
@author: bairavi
"""
#Question 2: Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number and previous number
print ("My Program for Iterative Sum") 
num1 = int(input("Enter the range"))
previousnum = 0
print('Printing current and previous number sum in a given range({0})'.format(num1))

for i in range(num1):
    sum1 = i+previousnum
    print("Current Number" , i , "Previous number" , previousnum , "Sum:" , sum1)
    previousnum = i 