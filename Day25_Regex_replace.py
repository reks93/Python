# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 22:36:39 2020

@author: rekha
"""
#Question 25: Replace a single character or string with another character or string using Regex. Replace all the occurrences

import re

input_str = input("Enter the string:")
repl_str = input("\nEnter a single character to be replaced in the main string")
replac_str = input("\nEnter a replacement character/string ")

output = re.sub (repl_str, replac_str ,input_str)
print("\n Output stirng is " , output)