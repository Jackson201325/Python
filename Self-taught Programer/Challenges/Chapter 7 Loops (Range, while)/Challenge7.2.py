# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 06:54:35 2018

@author: USER
"""
n1 = input("State the range of numbers you want to print ")
n1 = int(n1)
n2 = input("State the range of numbers you want to print ")
n2 = int(n2)
if n1 > n2:
    while n1 > n2:        
        print (n2)
        n2 += 1
elif n2 > n1 :
    while n2 > n1:        
        print (n1)
        n1 += 1       
else: 
    print ("The numbers have the same value")
    

