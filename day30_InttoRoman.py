# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 23:07:34 2020

@author: rekha
"""


def int_to_Roman(self, num):
    val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
    syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


print(int_to_Roman(5002))
#print(py_solution().int_to_Roman(4000))
