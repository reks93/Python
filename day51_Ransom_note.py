# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 23:36:13 2020

@author: rekha
"""
# Question 51:Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

#Each letter in the magazine string can only be used once in your ransom note.

#Input: ransomNote = "aa", magazine = "aab"
#Output: true

#Constraints:
#You may assume that both strings contain only lowercase letters.
def ransom(input_ransom, input_magaz):
    for i in input_ransom:
        if i in input_magaz:
            input_magaz = input_magaz.replace(i,"",1)
        else: return False
    return True

input_ransom = input("Ransom Note:!!!")
input_magaz  = input("Magazine string")
print(ransom(input_ransom, input_magaz))
