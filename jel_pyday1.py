# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 21:32:49 2020

@author: bairavi
"""

#Day 1 Coding Callenge

#Question 1: Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum.' ' '
import ast

var1 = int(input ("Enter input 1: "))
var2 = int(input ("Enter input 2: "))

if (var1*var2 > 1000):
    print ("The product of two inputs is greater than 1000, so the output of their sum is ")
    print (var1 + var2)
else:
    print ("The product of two inputs is less than 1000, so the output is ")
    print (var1*var2)

var3 = input ("Enter Random input (string/integer/float): ")

try:
    var4 = type(ast.literal_eval(var3))
    if (str(var4) == "<class 'float'>"):
        print ("The type of user input is FLOAT")
    elif (str(var4) == "<class 'int'>"):
        print ("The type of user input is INT")
except (ValueError, SyntaxError):
        print ("The type of user input is STRING")