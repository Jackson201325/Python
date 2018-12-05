from random import randint

class Dice():
    """A class representing a single die."""

    def __init__(self, num_side=6):
        """Assume a 6 side dice"""
        self.num_side = num_side

    def roll(self):
        """Return a number betweeen 1 and the num_side"""
        return randint(1, self.num_side)
