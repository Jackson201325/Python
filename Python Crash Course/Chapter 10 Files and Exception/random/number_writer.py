import json

numbers = [2, 3, 4, 5, 6, 7]

filename = 'numbers.json'

with open(filename, 'w') as fbj:
    json.dump(numbers, fbj)
