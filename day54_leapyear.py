# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 23:06:14 2020

@author: rekha
"""
#Question 54: Write a Python program to determine whether a given year is a leap year.

year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
