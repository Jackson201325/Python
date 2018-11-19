class Orange:
    def __init__ (self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print ("created")
    def rot (self, d, t):
        self.mold = d * t
or1 = Orange(10 , "dark orange")
or1.rot(9 , 90)
print(or1.weight)
print(or1.color)
print(or1.mold)
