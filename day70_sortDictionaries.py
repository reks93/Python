# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 22:50:45 2020

@author: rekha
"""
#Question 70: Write a Python program to sort a list of dictionaries using Lambda.

list_1 = [
	{'make':'Nokia', 'model':'216', 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': '7', 'color':'Blue'}]

sorted_models = sorted(list_1, key = lambda x: x['model'])
print ((sorted_models))