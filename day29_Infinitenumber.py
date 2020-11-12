# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 22:31:17 2020

@author: rekha
"""
#Question29:check if a given number is infinite or not

import math 
def isinfinite(num):
    if(math.isinf(num)):
        print("The number {} is infinite:" .format(num))
    else:
        print("The number {} is not infinite:" .format(num))
a = -300
b = float(math.inf)
c= float(-math.inf)
isinfinite(a)
isinfinite(b)
isinfinite(c)