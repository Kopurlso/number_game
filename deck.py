from card import Card
from set import Set

class Deck(Set):
    """
    Deck is a subset of Set and by default will contain all the cards in a
    standard deck
    """

    def __init__(self, jokers = False):
        if jokers:
            self.cards = [Card(suit, rank) for rank in range(1,14) for suit in suits]
            self.cards.append(Card('joker', 0))
            self.cards.append(Card('joker', 0))
        else:
            self.cards = [Card(suit, rank) for rank in range(1,14) for suit in suits]

    def __getitem__(self, key):
        return self.cards[key]

    def flip(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, number):
        cards = self.cards[:number]
        self.cards = self.cards[number:]
        return Set(cards)

    def size(self):
        return len(self.cards)
