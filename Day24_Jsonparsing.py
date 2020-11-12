# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 23:34:55 2020

@author: rekha
"""
#Question 24. Get a sample json (simple , not nested). Load into dictionary and fetch the values from dictionary.

import json

with open('json.txt') as json_file:
        data = json.load(json_file)
# show values
for p in data:
    #print('Name: ' + p['name'])
    #print(p)
    print('\nWebsite: ' + p['employee']['website'])
    print('\nFirstName: ' + p['employee']['firstName'])
    print('\nLastName: ' + p['employee']['lastName'])

