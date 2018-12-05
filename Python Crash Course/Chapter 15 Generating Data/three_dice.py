from dice import Dice
import pygal

d1 = Dice()
d2 = Dice()
d3 = Dice()

results = []
for roll_num in range (1000):
    result = d1.roll() + d2.roll() + d3.roll()
    results.append(result)
print(results)
xlabel = []
for label in range(3, d1.num_side * 3 + 1):
    xlabel.append(label)

frequencies = []
for value in range(3, d1.num_side * 3 + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

hist = pygal.Bar()

hist.title = "Result of rolling 3 D6 1000 times"
hist.x_labels = xlabel
hist.x_title = "Results"
hist.y_title = "Frequencies of results"

hist.add("D6 + D6 + D6", frequencies)
hist.render_to_file('three_die_visual.svg')
