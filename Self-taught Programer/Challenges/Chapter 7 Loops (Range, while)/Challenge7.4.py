# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 11:54:28 2018

@author: USER
"""

n = [1,2,3,42,31,345,564,23,6,23,24,523,5,23,5,22,34,245,56,64,23]

g = 0

while True: 
    print ("Type q to quit")
    a = input("Insert a number: ")
    a = int(a)
    if a in n:
        print("You have guessed the number")
    elif a == 999 :
        break
    else:
        print("Incorrect")
        