# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 20:59:15 2020

@author: rekha
"""
#Question38: Sort a given list of strings in a case- insensitive way using lambda fucntion
colors = ["Goldenrod", "purple", "Salmon", "turquoise", "cyan"]
print(sorted(colors, key=lambda s: s.casefold()))