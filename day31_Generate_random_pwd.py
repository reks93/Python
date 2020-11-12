# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 22:57:13 2020

@author: rekha
"""
#Question 31 : You're trying to create a website or mobile app that's capable of generating a random user password based on  your specific requirements. Generate a random alphanumeric password of letters n numbers with a fixed  length. A-Z , a-z , 0-9
import random
import string

def password_random(length):
    password = string.ascii_lowercase + string.ascii_uppercase + string.digits 
    rand_pwd = ''.join(random.choice(password ) for i in range(length))
    rand_pwd += ''.join(random.choice(string.punctuation ) for i in range(1))
    print("Random password for user is: " ,rand_pwd)
password_random(8)
password_random(9)
