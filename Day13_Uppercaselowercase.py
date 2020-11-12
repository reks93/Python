# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 23:11:43 2020

@author: Rekha
"""
#Question 13: Count all lower case, upper case, digits, and special symbols from a given string
input_string = input("Type the string:")
print("counting Letters , digits , special characters")
upper =lower = digit = special =0
for i in range(len(input_string)):
    if input_string[i].isupper():
        upper +=1
    elif input_string[i].islower():
        lower += 1
    elif input_string[i].isdigit():
        digit +=1
    else:
        special =+1
print("Character upper:", upper , "\nCharacter lower:",lower, "\ndigit:" , digit , "\nspecial char" , special)
            