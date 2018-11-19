while True:
    a = input("Insert a number: ")
    if a == 'q':
        break
    b = input("Insert another number: ")
    try:
        c = int(a)/int(b)
    except (TypeError, ValueError):
        print("You have to type another number")
    else:
        print("The number is: ", c)
        continue

