# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:50:17 2020

@author: bairavi
"""
#Finding the duplicate strings in a linked list. You are given a linked list with some elements and you have to write a function to list all the strings occurring more than once. But each such string should be printed only once, irrespective of the number of times it occurs in the linked list.
    
# Node class 
class Node: 
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None  
class LinkedList: 
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    def append(self, new_data): 

        new_node = Node(new_data) 
        if self.head is None: 
            self.head = new_node 
            return
  
        last = self.head 
        while (last.next): 
            last = last.next
  
        last.next =  new_node 
    def countNode(self,head): 
        list1 =[]
        while (head.next != None):
            ptr = head.next
            while (ptr != None): 
                if (head.data == ptr.data) and head.data not in list1: 
                    list1.append(head.data)
                    break
                ptr = ptr.next
            head = head.next
        return list1   
count = int(input("Enter the number of elements to be inserted"))
linked_list = LinkedList()
print("Enter the elements")
for i in range(count):
    data1 = input()
    linked_list.append(data1)
node = linked_list.head
print("Printing the linked list elements...\n")
while node:
    print (node.data)
    node = node.next
print("Printing only the duplicate elements",linked_list.countNode(linked_list.head))