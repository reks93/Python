# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 22:49:41 2020

@author: Rekha
"""
#Question19:Given a set of n nuts of different sizes and n bolts of different sizes. There is a one-one mapping between nuts and bolts. Match nuts and bolts efficiently.
#Constraint: Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means nut can only be compared with bolt and bolt can only be compared with nut to see which one is bigger/smaller.

nuts = []
bolts= []
hash_nut_bolt = {}
print("Give the Nuts available to sort")
nut = input()
print("Give the Bolts available to sort")
bolt = input()
nuts = nut.split()
bolts = bolt.split()
print("UnMatched Nuts", nuts , "\nBolts" ,bolts)
for i in range(len(nuts)):
    hash_nut_bolt[nuts[i]] = ""
for j in bolts:
    for key  in hash_nut_bolt:
        if(key == j):
             hash_nut_bolt[key]=j
        
print("Matched Items")
for key,val in hash_nut_bolt.items():
    if(val):
        
        print (key, "=>", val)
