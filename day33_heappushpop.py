# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 22:14:53 2020

@author: rekha
"""
#Question 33: write a program to push 3 items into a heap and return smallest item from the heap..also pop n return the smallest item from the heap.

import heapq

heap = []
heapq.heappush( heap , 3)
heapq.heappush( heap , 5)
heapq.heappush( heap , 1)
heapq.heappush( heap , 1)
print("The heap is" , heap)
print("pop smallest element in heap",heapq.heappop(heap))
print("result heap")
for a in heap:
    print(a)