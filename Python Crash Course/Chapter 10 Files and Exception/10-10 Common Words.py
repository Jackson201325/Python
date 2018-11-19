filename = 'book.txt'

try:
    with open(filename) as fobj:
        lines = fobj.readlines()
except FileNotFoundError:
    pass
else:
    string = ''
    for line in lines:
        string += line
    a = string.lower().count('the')
    print(a)
