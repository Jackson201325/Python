class Square():
    def __init__ (self, s):
        self.side = s

    def perimeter_Square(self):
        return self.side * 4

    def change_size(self, ns):
        self.side += ns #allow us to change the value of self.side

    def change_size_p(self):
        return self.side * 4

s1 = Square(10)
print("""The side of the Square is {}""".format(s1.side))
print("""The perimeter of the Square is {}""".format(s1.perimeter_Square()))

s1.change_size(-3)
print("""The new side of the square {}""".format(s1.side))
print("""The new perimeter is {}""".format(s1.change_size_p()))

