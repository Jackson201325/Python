def show_magician():
    magician_list = []

    while True:
        magician = input("Name of the magician: ")
        if magician == 'q':
            break
        else:
            magician_list.append(magician)

    for magicians in magician_list:
        print(magicians)


show_magician()
