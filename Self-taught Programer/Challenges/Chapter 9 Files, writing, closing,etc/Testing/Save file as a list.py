
script = list()

import os

a = os.path.join("C:/Users/jacks/Desktop/Atom Python/Self-taught Programer/Challenges/Chapter 9 Files, writing, closing,etc/Testing/text.txt")

with open (a, "r") as t:
    script.append(t.read())

print (script)
