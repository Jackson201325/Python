class Rectangle ():
    def __init__ (self, l, w):
        self.length = l
        self.wide = w

    def perimeter(self):
        return self.length * 2 + self.wide * 2

class Square():
    def __init__ (self, s):
        self.side = s

    def perimeter_Square(self):
        return self.side * 4

r1 = Rectangle(10, 20)
print(r1.length)
print(r1.wide)
s1 = Square(10)
print(s1.perimeter_Square())
