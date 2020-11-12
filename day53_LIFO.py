# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:09:55 2020

@author: rekha
"""
#Question53:Write a Python program to create a LIFO queue.

import queue

Q=queue.LifoQueue()
num = int(input('Enter the num of entries'))
print('Enter the values one by one to insert into the queue')
for i in range(num):
    Q.put(input())
print("Inserted into the LIFO queue!!")
while not Q.empty():
    print(Q.get() , end= " ")
# print()