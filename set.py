class Set:
    """
    A set is an array of cards. Can be empty.
    """
    set = []

    def __init__(self, cards):
        """
        Constructor

        cards: Card or Card[]
        """
        if isinstance(cards, list):
            for x in cards:
                if not isinstance(x, Card):
                    raise TypeError("Contents of cards are not all Cards.")
            self.cards = cards
        else:
            if isinstance(cards, Card):
                self.cards = [cards]
            else:
                raise TypeError("Card is not a type Card")

    def __getitem__(self, key):
        return self.cards[key]

    def play(self, index):
        """
        Returns a set of card/cards

        index: Int[]
        """
        ret = Set([self.cards[i] for i in index])
        for x in ret:
            self.cards.remove(x)
        return ret

    def show(self):
        """
        Lists out all cards in the set
        """
        for x in self.cards:
            x.name()

    def sort(self):
        """
        Sorts cards in set by rank and suit
        """
        self.cards.sort(key=lambda x: (x.rank, x.suit))

    def append(self, another_set):
        """
        Method appends a set to another set
        """
        for x in a_set.cards:
            self.cards.append(x)
