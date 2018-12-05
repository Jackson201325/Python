from dice import Dice
import pygal

dice_1 = Dice()
dice_2 = Dice()

results = []
for roll_result in range(1000):
    max_mult = dice_1.roll() * dice_2.roll()
    results.append(max_mult)

nums = []
for num1 in range(1, dice_1.num_side+1):
    for num2 in range(1, dice_2.num_side+1):
        multiplication = num1 * num2
        if multiplication in nums:
            pass
        else:
            nums.append(int(multiplication))
print(nums)

frequencies = []
for value in nums:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

h = pygal.Bar()

h.title = "Result of 2 D6 multiplication 1000 times"
h.x_labels = nums
h.x_title = "Results"
h.y_title = "Frequencies of results"

h.add("D6 * D6", frequencies)
h.render_to_file('hello.svg')
