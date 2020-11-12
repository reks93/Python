# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 22:49:27 2020

@author: rekha
"""

#Question 26: Bowl 6 balls in an over and generate random run between 0 and 6 for each ball. Print the score at the end of the over.
import random

score =0 
for i in range(6):
    balls = random.randint(0,6)
    print("runs per ball" , balls)
    score +=balls

print("score at the end of the over -" , score)