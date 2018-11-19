class Square():
    def __init__(self, s):
        self.side = s
    def area (self):
        return self.side ** 2
    def perimeter(self):
        return self.side * 4
class Hexagon(Square):
    def perimeter (self):
        return self.side * 6
    def change_size(self, ns):
        self.side += ns
    def new_perimeter (self):
        return self.side * 6

s1 = Hexagon(10)
print (s1.side)
print (s1.perimeter())
s1.change_size(-4)
print (s1.side)
print (s1.new_perimeter())`13`
