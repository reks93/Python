# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:24:24 2020

@author: rekha
"""
#Question 47 : Given an integer ‘n’, write a Python function that returns true if binary representation of x is palindrome else return false
def is_bin(num):

    binary = bin(num)
    binary = binary[2:]
    print("Binary number is",binary)
    if binary == binary[::-1]:
        return True
    else:
        return False

number = int(input("Enter the integer"))
print(is_bin(number))