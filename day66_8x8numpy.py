# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 21:41:24 2020

@author: rekha
"""

#Question66:a) Create an 8*8 array with ones on all edges and zeroes everywhere using numpy
#b)Create a 8x8 matrix and fill it with a checkerboard pattern
import numpy as np
x = np.ones((8,8), dtype =int)
x[1:-1, 1:-1] = 0
print("Output array 1 on edges and 0's everywhere \n")
print(x)

y = np.zeros((8,8), dtype =int)
y[1::2,::2] = 1
y[::2,1::2] = 1
print("Output array chessboard pattern\n")
print(y)