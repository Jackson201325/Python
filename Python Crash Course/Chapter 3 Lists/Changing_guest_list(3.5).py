# Start with your program from the exersize 3.4. Add print statement at the end of your program stating the name of the guest who cant make it
# Modify your list, replacing the name of the guest whi cant make it with the name of the new person you are inviting
# Print a second set of invitation messages, one for each person who is still in your list

names = ['Jackson', 'David', 'Campos', 'Ale']
for i in names:
    print("Hi,", i, "I would like to invite you to a Dinner ")

print()

cant = ['David', 'Ale']
print("{} and {} cant make it".format(cant[0], cant[1]))

names.remove('David')
names.remove('Ale')
names.append('Ali')
names.append('Juan')

print()

for i in names:
    print("Hi,", i, "I would like to invite you to a Dinner ")
