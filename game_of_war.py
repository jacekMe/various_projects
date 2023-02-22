from random import shuffle

class Card:
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']

    def __init__(self, value, suit):
        """lists 'suit' & 'value' => int"""
        self.value = value
        self.suit = suit

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.value:
                return True
            else:
                return False
        return False

    def __repr__(self):
        return self.values[self.value] + " " + self.suits[self.suit]

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("Give your name: ")
        name2 = input("Give your name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "This round wins {}\n"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} pulled {}, {} pulled {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("\nWe start entertainment\n")
        while len(cards) >= 2:
            m = "Press 'q' to finish or other key to continue\n"
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("War over - won {}". format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It's draw."
game = Game()
game.play_game()
