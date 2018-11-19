import json

filename = 'FavNum.json'

try:
    with open(filename) as f_obj:
        num = json.load(f_obj)
except FileNotFoundError:
    fn = input("What is your favourite number? ")
    with open(filename, 'w') as f_obj:
        json.dump(fn, f_obj)
else:
    print("Your Favourite number is", num)
