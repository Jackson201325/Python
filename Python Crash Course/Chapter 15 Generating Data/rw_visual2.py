import matplotlib.pyplot as plt

from random_walk2 import RandomWalk2


# Make a RandomWalk, and plot the num_points
while True:
    rw = RandomWalk2(9999)
    rw.fill_walk()

    # Set the sieze of the plotting window.
    plt.figure(dpi=80, figsize=(8, 5))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values)
    plt.plot(0, 0, c='green')

    plt.show()
