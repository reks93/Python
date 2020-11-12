# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 22:46:56 2020

@author: Rekha
"""
#Question18-Given a string “str” and another string “sub_str”. We are allowed to delete “sub_str” from “str” any number of times. It is also given that the “sub_str” appears only once at a time. The task is to find if “str” can become empty by removing “sub_str” again and again.

def checking_substr(input_str , sub_str):
    if(input_str.find(sub_str) == -1):
        print("substring is not available in the input string")
    else:
        rem_str =input_str.replace(sub_str,"",1 )      
        if(rem_str == ""):
            print("Main string is made of substrings..")
        else:
            print("substrings is present in string, remaining string is:",rem_str)
            checking_substr(rem_str , sub_str)
    
print("Checking for a substring inside a string")
inp_str = input("Enter the Main string")
subs_tr = input("Enter the substring to search")
checking_substr(inp_str , subs_tr)