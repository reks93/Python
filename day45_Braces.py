# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 23:38:26 2020

@author: rekha
"""
#Question 45: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
def valid_braces(list2):
    if not list2:
        return True
    if len(list2) % 2 != 0:
        return False
    for item in ["()", "[]", "{}"]:
        if item in list2:
            return valid_braces(list2.replace(item, ""))
    return True
    """ left = "([{"
    right = ")]}"
    stack = []
    for i in list1:
        print("list1" , i)
        if i in left:
            print("left" , i)
            stack.append(i)
            print("stack" , stack)
        elif not stack 
            return False
        print("Stack" , stack)
    return not stack
            """
    
braces1 = input("Enter the braces:")
print(valid_braces(braces1))