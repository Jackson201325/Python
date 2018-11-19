filename = 'guest.txt'

answer = input("What is your name? ")

with open(filename, 'w') as f_obj:
    f_obj.write(answer)
    print("Hello " + answer + ", welcome back")
