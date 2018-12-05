import matplotlib.pyplot as plt

from random_walk import RandomWalk


# Make a RandomWalk, and plot the num_points
while True:
    rw = RandomWalk(9999)
    rw.fill_walk()

    # Set the sieze of the plotting window.
    plt.figure(dpi=226, figsize=(8, 5))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1)
    plt.scatter(0, 0, c='green', edgecolors=None, s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
