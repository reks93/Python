# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 19:37:16 2020

@author: Rekha
"""
#Question 14: Search and replace string in the given sentence
#Input : The meeting is scheduled for Monday evening
#Find: Monday
#Replace: Tuesday
def replace(input_str,replacestr,newstr,flag_y_n):
    if flag_y_n == 'Y':
        Mod_str = input_str.replace(replacestr,newstr)
        return Mod_str
    else:
        list1 = input_str.split()
        count_occurence = list1.count(replacestr)
        if count_occurence ==0:
            print("Entered string not found!!")
        else:
            for i in range(1,len(list1)):
                Mod_str = input_str.replace(replacestr,newstr,i)
                input_str = Mod_str
                print("Modified String : ",Mod_str)
                y_n = input("Do you wanna replace the next occurence")
                if y_n == 'Y':
                    continue
                else:
                    break
        return Mod_str
    
input_str = input("Enter the input string..")
replace_str = input("Enter the string to be replaced..")
new_str =  input("Enter the new string..")
flag_y_n = input("Do you wanna replace all the occurences of the given String?..")
print("\nReplacing...please wait\n" ,"OutputString" , replace(input_str,replace_str,new_str,flag_y_n ))
#print(input_str.replace(replace_str,new_str))
