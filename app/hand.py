from app.deck import Deck


class Hand(Deck):
    """In real play we would also need to know the total number of players so that we could deal the cards out in the correct order. However, here we are only interested in our hand (we never fully know our
    opponent's hand); which will later be compared to an opening range based off of our position. Therefore, it doesn't matter which two cards we get as long as they are valid, random, and different."""
    def __init__(self):
        super(Hand, self).__init__()
        self.hole_cards = []

    def get_hand(self, deck):
        self.hole_cards.append(deck.deal_card())
        self.hole_cards.append(deck.deal_card())
        return self.hole_cards

    def order_hand(self):
        """Need to order the hand from highest to lowest value; i.e. 3s Ah needs to be reordered to Ah 3s to compare it to the hand type of A3o."""
        if self.hole_cards[0].get_rank() < self.hole_cards[1].get_rank():  # This is similar to a reverse sort which gets the majority of hands in the correct order.
            self.hole_cards = [self.hole_cards[1], self.hole_cards[0]]

        if self.hole_cards[1].get_rank() == "A":  # Now need to get the A-T in correct order b/c cannot use the alphabetical sort order.
            self.hole_cards = [self.hole_cards[1], self.hole_cards[0]]
        elif self.hole_cards[1].get_rank() == "K":
            self.hole_cards = [self.hole_cards[1], self.hole_cards[0]]
        elif self.hole_cards[1].get_rank() == "Q":
            self.hole_cards = [self.hole_cards[1], self.hole_cards[0]]
        elif self.hole_cards[1].get_rank() == "J" and self.hole_cards[0].get_rank() == "T":
            self.hole_cards = [self.hole_cards[1], self.hole_cards[0]]
        return self.hole_cards

    def hand_type(self):
        """The 3 hand types are pairs (5h5s is 55), suited (KhQh is KQs; s = suited here; not to be confused as 'spades'), and unsuited (5d4c is 54o; o = off-suit)."""
        if self.hole_cards[0].get_rank() == self.hole_cards[1].get_rank():
            return str(self.hole_cards[0].get_rank()) + str(self.hole_cards[1].get_rank())
        elif self.hole_cards[0].get_suit() == self.hole_cards[1].get_suit():
            return str(self.hole_cards[0].get_rank()) + str(self.hole_cards[1].get_rank() + "s")
        else:
            return str(self.hole_cards[0].get_rank()) + str(self.hole_cards[1].get_rank() + "o")

    def __str__(self):
        if self.hole_cards:
            c = ""
            for card in self.hole_cards:
                c += str(card) + " "
        else:
            c = "No cards in hand."
        return c
