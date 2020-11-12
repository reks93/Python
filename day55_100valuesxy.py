# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 23:47:43 2020

@author: rekha
"""
#Question55-calculate 100 values for x and y without a for loop
import numpy as np
x = np.linspace(0, 2* np.pi, 100)
y = np.sin(x)
print("X-" , x , " Y-" , y)