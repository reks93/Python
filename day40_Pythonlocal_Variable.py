# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 23:43:34 2020

@author: rekha
"""
#Question40 Write a Python program to detect the number of local variables declared in a function.
def local_var():
    pass
def local_var2():
    str_var1 = "xyz"
    a ,b = 3 ,4.5

print("number of local var in function1 :" , local_var.__code__.co_nlocals)
print("number of local var in function2 :" ,local_var2.__code__.co_nlocals)