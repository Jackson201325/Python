def describe_city(country='Paraguay', city='Asuncion'):
    return "{} is in {}".format(country, city)


l = []

a = describe_city()
b = describe_city('Mexico', 'Tijuan')
c = describe_city('England', 'London')

print(a)
print(b)
print(c)
