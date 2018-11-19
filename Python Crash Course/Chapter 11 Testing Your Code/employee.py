class Employee():
    def __init__(self, name, last, salary):
        self.name = name.title()
        self.last = last.title()
        self.salary = salary

    def give_raise(self, amount='50000'):
        self.salary += amount

    def __repr__(self):
        return "{}, {} will earn {}".format(self.last, self.name, self.salary)


e1 = Employee('Jackson', 'Huang', 0)
e2 = Employee('Jose', "lol", 50000)

print(e1.__repr__())
print(e2.__repr__())
