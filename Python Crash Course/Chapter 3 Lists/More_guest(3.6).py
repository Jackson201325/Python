# You just found a bigger dinner table, so now more space is available. Think of three more guest to invite
# Use insert() to add new guesto to the beginning of your list
# Use insert() to add one new guest to the middle of the list
# Use append() to add new guest to the end of your list

names = ['Jackson', 'David', 'Campos', 'Ale']
for i in names:
    print("Hi,", i, "I would like to invite you to a Dinner ")

print()

cant = ['David', 'Ale']
print("{} and {} cant make it".format(cant[0], cant[1]))


names.remove('David')
names.remove('Ale')

dinner = ['Jackson', 'Campos']
print("{} and {} are still available for the dinner.".format(dinner[0], dinner[1]))

names.append('Ali')
names.insert(3, 'Juan')
names.insert(0, 'Jose')

print()

for i in names:
    print("Hi,", i, "I would like to invite you to a Dinner ")
