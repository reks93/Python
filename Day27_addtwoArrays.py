# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 22:29:45 2020

@author: rekha
"""
#Question 27: Add the corresponding elements of two same size arrays without looping.
#Input:
#array1 = [1,2,3,4,5]
#array2 = [6,7,8,9,10]
#Output:
#[7,9,11,13,15]

import numpy as np
array1 = [1,2,3,4,5]
array2 = [6,7,8,9,10]
sum_array =np.add(array1 , array2)
print("sum array",sum_array)