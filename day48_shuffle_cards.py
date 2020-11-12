# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 22:57:06 2020

@author: rekha
"""
#Question48:write Python program to shuffle a deck of 5 cards
#Output : 5 of Heart,1 of Heart,8 of Spade,12 of Spade,4 of Spade

import itertools , random

deck = list(itertools.product(range(1,14) ,['Heart', 'Spade' , 'Diamond','Club']))

random.shuffle(deck)
print('Shuffling your cards......Please wait\n')
for i in range(5):
    print(deck[i][0] , 'of' , deck[i][1])