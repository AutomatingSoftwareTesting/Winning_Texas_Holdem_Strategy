class Card(object):
    """Originally was going to have separate rank and suit classes; however, they would have to be combined eventually. This is possible in Python, but was avoided because it can run into inheritance conflicts later.
    RANKS and SUITS are capitalized to demonstrate they are constants."""
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def __str__(self):
        return self.rank + self.suit
