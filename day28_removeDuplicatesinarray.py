# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 22:19:57 2020

@author: rekha
"""
#Question 28:  Write a program to remove the duplicates in an array

pizza = ['Hawaiian', 'Margherita', 'Mushroom', 'Prosciutto', 'Meat Feast', 'Hawaiian', 'Bacon', 'Black Olive Special', 'Sausage', 'Sausage']

final_new_menu = list(dict.fromkeys(pizza))

print("YAYYY!! new menu is" , final_new_menu)