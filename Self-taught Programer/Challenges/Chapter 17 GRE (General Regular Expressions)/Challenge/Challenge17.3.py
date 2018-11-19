# Create a regular expression that matches any word that starts any character and is followed by tow o's. Then use python;s re module to match voo and loo in the sentences
import re

sentence = "The ghost that says boo haunts the loo"

pattern = re.compile(r"[b|l]oo")

matches = pattern.finditer(sentence)

for match in matches:
    print(match)
