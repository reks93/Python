# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 22:09:37 2020

@author: Rekha
"""
#Question 20: Write a Python program to rank the frequency of 5 given keywords in a given file.
import operator

def wordListToFreqDict(wordlist , word_counts):
    wordfreq = [word_counts.count(p) for p in wordlist]
    dict1 ={}
    #dict1 = dict(list(zip(wordlist,wordfreq)))
    dict1 = dict(list(zip(wordlist,wordfreq)))
    #print("doct\n" , dict1)
    return dict(sorted(dict1.items(), key=operator.itemgetter(1), reverse=True)[:5])

keys = []
print("Enter keywords to search in the file")
for i in range(5):
    keys.append(input())
text = open("sample.txt", "r") 
words ={}
word_count ={}
line1  = []
list1 = []
for line in text:
    #Strip any white space
    line = line.strip() 
    #convert into lower for case mismatch
    line = line.lower()
    line = line.split()
    line1.extend(line)
words = line1
for i in range(len(keys)):
    if keys[i] in words:
        list1.append(keys[i])
    else:
        print(keys[i],"Keyword not found")
word_count = list1
print("\n", words)
print("\n", word_count)
print("_________",wordListToFreqDict(word_count , words ))


