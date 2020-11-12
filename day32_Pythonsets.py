# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 23:22:51 2020

@author: rekha
"""
#Question 32: given two python sets, update first set with items that exists only in the first set and not in the second set

set1 = {10 , 20 , 30 , 40 , 50}
set2 = {30 , 50 , 60 , 80 , 70 }

set1.difference_update(set2)
print(set1)