# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:53:34 2020

@author: rekha
"""
#Question 62: Write a Pandas program to find the positions of numbers that are multiples of 5 of a given series.

import pandas as pd
import numpy as np
num_series = pd.Series(np.random.randint(1, 10, 10))
print("Original Series:")
print(num_series)
result = np.argwhere(num_series % 5==0)
print("Positions of numbers that are multiples of 5:")
print(result)
