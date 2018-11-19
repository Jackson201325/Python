filename = 'pi_million_digit.txt'

with open(filename) as f_obj:
    lines = f_obj.readlines()

pi_string = ''

for line in lines:
    pi_string += line

b_day = input("Enter the date of your birthday in ddmmyy: ")

if b_day in pi_string:
    print("we found it")
else:
    print("no")
