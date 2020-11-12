# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 13:13:57 2020

@author: rekha
"""
#Question 57: Write a program to remove empty list from a list

list1  = [[], [], [], [], [], 'text', 'text2', [], 'lsit23']
list2 = [x for x in list1 if x!=[]]
print('\nlist before-' , list1  ,'\nlist after removing empty lists',list2)