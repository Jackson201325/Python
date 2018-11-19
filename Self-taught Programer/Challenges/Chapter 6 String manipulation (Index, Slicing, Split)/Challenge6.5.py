# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 12:22:47 2018

Problem: Take the list ["The","fox","jumped","over","the","fence"] and turn it into a gramatically correct string

@author: USER
"""

p = ["The","fox","jumped","over","the","fence","."]

a = [p[0], p[1], p[2], p[3], p[4]]

a =" ".join(a)

b = [p[5],p[6]]

b = "".join(b)

print (a,b)