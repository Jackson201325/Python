class Square():
    SquareList = []

    def __init__ (self, s1):
        self.s1 = s1
        self.SquareList.append((self.s1))

    def __repr__ (self):
        return "Square({} by {} by {} by {})".format(self.s1, self.s1, self.s1, self.s1)

    def __str__(self):
        return '{} by {} by {} by {}'.format(self.s1, self.s1, self.s1, self.s1)
s1 = Square(29)
print(s1.__repr__())
print(s1.__str__())
