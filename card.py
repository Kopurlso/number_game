import random
from vardata import suits, names, ranks

class Card:
    """
    This is a Card class. This object will store information relevant to a
    single Card, the suit and the rank. Suits can be hearts, spades, clubs, or
    diamonds. Ranks range from 1-14.
    """
    rank = None
    suit = None

    def __init__(self, suit, rank):
        if rank not in range(1, 14):
            raise TypeError("Rank must be an integer from 1 to 14. Rank was " + rank)
        if suit not in suits and suit != 'joker':
            raise TypeError("Suit must be hearts, spades, clubs or diamonds. Suit was " + suit)
        self.rank = rank
        self.suit = suit

    def name(self):
        if self.suit == 'joker':
            print("Joker")
        else:
            print(names[str(self.rank)] + " of " + self.suit)
