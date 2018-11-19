class Square():
    def __init__ (self, s):
        self.side = s

    def perimeter_Square(self):
        return self.side * 4

    def change_size(self, ns):
        self.side += ns
        return self.side * 4

s1 = Square(10)
print("""The side of the Square is {}""".format(s1.side))
print("""The perimeter of the Square is {}""".format(s1.perimeter_Square())


s1.change_size(-5)
print(s1.side)
