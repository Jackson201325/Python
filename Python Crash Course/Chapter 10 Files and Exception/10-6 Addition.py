a = input("Insert a number ")
b = input("Insert another number ")

try:
    c = a/b
except TypeError:
    print("It has to be a number ")
else:
    print("The ansewer is ", c)
