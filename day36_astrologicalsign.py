# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:44:40 2020

@author: rekha
"""
#Question 36: Write a Python program to display astrological sign for given date of birth. The input date of birth should be a single string in the format “dd-mm-yyyy”.

def zodiac_sign(day, month): 
      
    astro_sign = ''
    if month == '12': 
        astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
          
    elif month == '01': 
        astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
          
    elif month == '02': 
        astro_sign = 'Aquarius' if (day < 19) else 'pisces'
          
    elif month == '03': 
        astro_sign = 'Pisces' if (day < 21) else 'aries'
          
    elif month == '04': 
        astro_sign = 'Aries' if (day < 20) else 'taurus'
          
    elif month == '05': 
        astro_sign = 'Taurus' if (day < 21) else 'gemini'
          
    elif month == '06': 
        astro_sign = 'Gemini' if (day < 21) else 'cancer'
          
    elif month == '07': 
        astro_sign = 'Cancer' if (day < 23) else 'leo'
          
    elif month == '08': 
        astro_sign = 'Leo' if (day < 23) else 'virgo'
          
    elif month == '09': 
        astro_sign = 'Virgo' if (day < 23) else 'libra'
          
    elif month == '10': 
        astro_sign = 'Libra' if (day < 23) else 'scorpio'
          
    elif month == '11': 
        astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
          
    return astro_sign 
    
print("FIND your Astro sign based on birth date:\n")
dob = input("Enter you dob in the format “dd-mm-yyyy” ")
dayarr = dob.split("-")
day = int(dayarr[0])
month = dayarr[1]
print(zodiac_sign(day, month) )

