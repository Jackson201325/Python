class Data:
    def __init__ (self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n
d1 = Data()
d1.nums[0] = 20
print(d1.nums)

d2 = Data()
d2.change_data(1, 20)
print(d2.nums)
