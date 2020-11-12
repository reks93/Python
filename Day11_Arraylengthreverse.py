# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 21:08:42 2020

@author: Rekha
"""
#Question11:Printing the length of an array in reverse order
#For this problem, you need to print the length of the arrays provided to you in the test cases in reverse order, i.e. the length of the last array provided as input will be printed first.

n = int(input("Enter the length of the array"))
#lists = [ [] for i in range(n)]
stringlist = []
listoflist = []
for i in range(n):
    inp = input().split()
    stringlist = [int(j) for j in inp]
    listoflist.append(stringlist)

for j in listoflist[len(listoflist)::-1]:
    print(len(j))