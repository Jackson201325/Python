filename = 'dog.txt'
filename1 = 'cat.txt'

try:
    with open(filename) as f_obj:
        lines = f_obj.readlines()
except FileNotFoundError:
    msg = "ERROR 404 File not found"
    print(msg)
else:
    for line in lines:
        print(line)
