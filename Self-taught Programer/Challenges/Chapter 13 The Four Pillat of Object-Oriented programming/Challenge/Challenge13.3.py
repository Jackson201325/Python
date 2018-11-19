class Shape ():
    def what_am_i(self):
        print("I am a shape")

class Rectangle (Shape):
    def __init__ (self, l, w):
        self.length = l
        self.wide = w

        def perimeter(self):
            return self.length * 2 + self.wide * 2

class Square(Shape):
    def __init__ (self, s):
        self.side = s

    def perimeter_Square(self):
        return self.side * 4

r1 = Rectangle(20, 10)
s1 = Square(5)

r1.what_am_i()
s1.what_am_i()
