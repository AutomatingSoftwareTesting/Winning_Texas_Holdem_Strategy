from app.card import Card


class Deck(object):
    def __init__(self):
        self.cards = []

    def create(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        """This takes the deck that is always created in the same order and scrambles it. Originally, was only going to randomize the dealt cards; but think this will be clearer for testing."""
        import random
        random.shuffle(self.cards)

    def deal_card(self):
        if self.cards:
            top_card = self.cards[0]
            self.cards.remove(top_card)
            return top_card
        else:
            return "Sorry, unable to continue dealing because we are out of cards.\n" \
                   "This is somewhat odd because community card games (like No Limit Texas Hold'em) came about because many players don't like to fold.\n" \
                   "As a result, the community cards (the board consisting of the flop, turn, and river) should prevent this.\n" \
                   "Regardless, please create a new deck; and then, shuffle up and deal."

    def __str__(self):
        """Displaying the deck or a user friendly backup message in case someone makes a mistake."""
        if self.cards:
            c = ""
            for card in self.cards:
                c += str(card) + " "
        else:
            c = "Sorry, no cards in deck. Please create a new deck; and then, shuffle up and deal."
        return c
