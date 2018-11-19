filename = 'dog.txt'
filename1 = 'cat.txt'

try:
    with open(filename) as f_obj:
        lines = f_obj.readlines()
except FileNotFoundError:
    pass
else:
    for line in lines:
        print(line)
