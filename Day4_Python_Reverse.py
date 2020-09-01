# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 21:53:59 2020

@author: Rekha
"""
#Question 4: Reverse a given number and return true if it is the same as the original number
def reverse(Number):
#Number = int(input("original number"))
    originalNum = Number
    reverse = 0
    while (Number > 0):
        reminder = Number % 10
        reverse = (reverse * 10) + reminder
        Number = Number//10
    if(originalNum == reverse):
        print("The original and reverse number is the same")
        return True
    else:
        print("The original and reverse number is not same")
        return False
num = int(input("original number"))
print(reverse(num))
