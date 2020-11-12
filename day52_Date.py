# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 00:09:47 2020

@author: rekha
"""
#Question 52- Find yesterday s , today's and tomorrow's date using a python program

import numpy as np
yes = np.datetime64('today' , 'D' ) - np.timedelta64(1,'D')
today = np.datetime64('today' , 'D' )
tomorrow = np.datetime64('today' , 'D' )+ np.timedelta64(1,'D')

print("\nyesterday-" , yes , "\ntoday-" , today , "\nTomorrow-" , tomorrow)