# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:51:46 2020

@author: rekha
"""
#Question 39: Write a Python program to execute a string containing Python code.
code = """
def mycode():
    print("Executing a string containing python code:")
    
mycode()
"""
exec(code)