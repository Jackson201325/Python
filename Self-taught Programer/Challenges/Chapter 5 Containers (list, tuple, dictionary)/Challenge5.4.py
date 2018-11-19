# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 10:18:29 2018

@author: USER
"""
attribute = {"height":"180cm", "book":"How to not give a fuck", "author":"Dan Brown"}
q = input("What do you want to know about me? ")

if q in attribute:
    atr = attribute[q]
    print (atr)
else:
    print("Sorry I do have the  information to respond about your ",q)
