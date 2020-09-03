# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 22:10:36 2020
@author: Rekha
"""
# Question6: Create a function that returns True if the given circles are intersecting, otherwise return False. The circles are given as two lists containing the values in the following order: Radius of the circle.Center position on the x-axis.Center position on the y-axis.

import math
def circle_intersect():
    circle1 = []
    print("Enter Radius ,Position on the x-axis ,Position on the y-axis for circle1 and circle2")
    for i in range(6):
        val1 = float(input())
        if val1 < 0 and val1.is_integer():
            raise ValueError('Negative values not allowed!')
        circle1.append(val1)
    print(circle1)
    #[r1,x1,y1,r2,x2,y2]
    dsq = (circle1[1] - circle1[4])**2 + (circle1[2]-circle1[5]) **2
    dsq = math.sqrt(dsq)
    if( dsq < circle1[0] + circle1[3]):
        return True
    else:
        return False
print("Program to find whether two circles Intersect \n")
print("The two circles intersect:" , circle_intersect())
