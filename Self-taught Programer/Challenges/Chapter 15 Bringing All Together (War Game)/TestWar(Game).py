class Game:
    def __init__ (self):
        name1 = input ("Player 1 name")
        name2 = input ("Player 2 name")
        self.Deck = Deck()
        self.p1 = name1
        self.p2 = name2

    def wins(self, winner):
        w = "{} wins this round".format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} draw {}, {} draw {}".format(p1n, p1c, p2n, p2c)
        print (d)

    def play_game (self):
        cards = self.deck.cards
        print ("Beginning of War")
        while len (cards) >= 2:
            response = input("Press q to quit. Press any other")
            if response == 'q':
                break
            p1c = self.Deck.rm_card
            p2c = self.Deck.rm_card
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p2n, p1c, p2c)
            if p1c > p2c:
                self.p1.win += 1
                self.wins(self.p1.name)
            else:
                self.p2.win += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("War is over.{} wins ".format(win))

    def winner (self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie"
