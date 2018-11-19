filename = 'guest.txt'


with open(filename, 'w') as f_obj:
    names = []
    while True:
        answer = input("\nWhat is your name? ")
        if answer == 'q':
            for name in names:
                f_obj.write("\n")
                f_obj.write(name)
            break
        else:
            print("Hello " + answer + ", welcome back")
            names.append(answer)
    
