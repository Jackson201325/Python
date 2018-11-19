# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 20:31:43 2018

@author: USER
"""
print("Press 99999 to stop")
nums = []

while True:    
    try: 
        a = input("Enter a random number: ")
        a = int(a)
        if a == 99999:
            break
        if a/1 == True:
            nums.append(a)
        else:
            nums.index()
            a = 0
    except (ValueError, TypeError):       
        print("Invalid input")
    
   

import statistics

print(statistics.mean(nums))
print(statistics.median(nums))
print(statistics.mode(nums))
        