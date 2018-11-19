import re
import os
text_to_search = """
abcdefghijklmnopqrstuvyxz
ABCDEFGHIJKLMNOPQRSTUVYXZ
1234567890

Ha HaHa

MetaCharacter (Needs to be escaped):
.[{()\^$|?*+

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""
sentence = 'Start a sentence and then bring it to an end'


def __repr__(self):
    return "'{}'"


pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

matches = pattern.finditer(text_to_search)

with open('useit.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    for match in matches:
        print(match.__repr__())
print(cwd)
