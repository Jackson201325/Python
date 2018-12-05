import pygal
from dice import Dice

import os
dir_path = os.path.dirname(os.path.realpath(__file__))


dice_1 = Dice()
dice_2 = Dice()

results =[]
for roll_num in range(1000):
    max_result = dice_1.roll() + dice_2.roll()
    results.append(max_result)

# print(results)

# Analize result
frequencies = []
for value in range(2, dice_1.num_side + dice_2.num_side):
    frecuency = results.count(value)
    frequencies.append(frecuency)

print(frequencies)
xlabel =[]
for label in range(2, dice_1.num_side + dice_2.num_side):
    xlabel.append(str(label))

# Visualize the result
hist = pygal.Bar()

hist.title = "Result of rolling two D6 1000 times"
hist.x_labels = xlabel
hist.x_title = "Results"
hist.y_title = "Frequencies of results"

hist.add("D6 + D6", frequencies)
hist.render_to_file('die_visual.svg')
