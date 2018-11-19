import json

fn = input("What is your favourite number? ")

filename = 'FavNum.json'

with open(filename, 'w') as f_obj:
    json.dump(fn, f_obj)
