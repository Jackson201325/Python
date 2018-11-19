def show_magician(magician_list, great_magicians):
    current_magician = magician_list[:]
    while magician_list:
        magicians = magician_list.pop()
        print("Magician noobs about to graduate: ", magicians)
        great_magicians.append(magicians)
    print()
    print(current_magician)


def make_great(great_magicians, new_magicians):
    old_list = great_magicians[:]
    while great_magicians:
        new = great_magicians.pop()
        a = "The great " + new.title() + "."
        new_magicians.append(a)
    print(new_magicians)


magician_list = ['Shin Lim', 'Jackson', 'Jose']
great_magicians = []
new_magicians = []

show_magician(magician_list, great_magicians)
make_great(great_magicians, new_magicians)
