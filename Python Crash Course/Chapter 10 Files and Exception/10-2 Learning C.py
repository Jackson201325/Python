filename = 'learning_python.txt'

with open(filename) as f_obj:
    lines = f_obj.readlines()

for line in lines:
    print(line.replace('python', 'C++'))
