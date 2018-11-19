# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 06:56:33 2018

@author: USER
"""

shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

for index, show in enumerate (shows):
    index = index + 1
    new = show 
    new = new.upper()
    show = new
    print (index, ". ", show)
    
    