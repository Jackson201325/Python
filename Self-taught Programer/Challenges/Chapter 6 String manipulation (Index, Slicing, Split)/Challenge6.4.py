# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 11:50:02 2018

@author: USER
"""

q = ("Where now? Who now? When now?").split(" ")

a = [q[0], q[1]]
a1 = " ".join(a)

b = [q[2], q[3]]
b1 = " ".join(b)

c = [q[4], q[5]]
c1 = " ".join(c)

s = "[\"{}\", \"{}\", \"{}\"]".format(a1, b1, c1)

print(s)
print(q[2])
