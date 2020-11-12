# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 22:44:38 2020

@author: rekha
"""
#question23:Write a function called is_abecedarian that returns True if the letters in a word
#appear in alphabetical order (double letters are ok). How many abecedarian words are there?
def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
            print("False")
        previous = c
    print("true")

    return True

#print(is_abecedarian("abcde"))
list1 = []
count_abec = 0
text = open("day23_file.py" , "r")
for line in text:
    line.strip()
    line.split()
    if is_abecedarian(line):
        list1.append(line)
        count_abec +=1
    else:
        print("Else" , line)
print("There are {} abecedarian words" .format(count_abec))
print(list1)