class Shape():
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def print_size(self):
        print("""{} by {}""".format(self.width, self.length))

class Square(Shape):
    def area(self):
        return self.width * self.length

    def print_area(self):
        print("""{} by {}""".format(self.width, self.length))

s1 = Square(10, 20)
s2 = Square(20, 20)
s1.print_size()
print(s1.area())
s1.print_size()
print(s2.area())
