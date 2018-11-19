class Name():
    def __init__ (self, n, ln, s, e):
        self.name = n
        self.lname = ln
        self.salary = s
        self.email = e

    def __repr__ (self):
        return "Name('{}','{}',{},'{}')".format(self.name, self.lname, self.salary, self.email)

    def __str__ (self):
        return '{} - {} - {} - {}'.format(self.name, self.name, self.salary, self.email)

    def __add__ (self, other):
        return self.salary + other.salary

p1 = Name("Lion", "Wagner", 10000, "jacksonh201325@gmail.com")
p2 = Name("Hehe", "xD", 3000, "asdgewge@gmail.com")
p3 = Name("daf", "daffg", 5000, "ewfgrbfdd@hotmail.com")

print(p1.__repr__())
print(p2.__str__())
print(p1 + p2)
