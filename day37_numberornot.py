# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 19:40:13 2020

@author: rekha
"""
#Question 37: Write a Python program to check whether a given string is number or not using Lambda.
num1 =[]
is_num = lambda num: 'True' if (num.replace('.','',1).isdigit() or  num[0]=='-' ) else False

print(is_num('26587'))
print(is_num('4.2365'))
print(is_num('-12547'))
print(is_num('00'))
print(is_num('A001'))
print(is_num('001'))
print(is_num('-16.4'))
print(is_num('-24587.11'))
