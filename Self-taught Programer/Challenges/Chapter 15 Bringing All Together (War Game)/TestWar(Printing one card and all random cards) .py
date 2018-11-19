from random import shuffle

class Card:
    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]

    values = [None, None,"2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def __repr__(self):
        return '{}'.format(self.cards)


c1 = Deck()
print(c1.__repr__())
