from app.deck import Deck


class TestDeck:
    """Creating a standard 52 card deck by combining all the ranks and suits."""
    def test_new_deck(self):
        deck = Deck()
        deck.create()
        assert len(deck.cards) == 52
        assert str(deck) == "2c 3c 4c 5c 6c 7c 8c 9c Tc Jc Qc Kc Ac 2d 3d 4d 5d 6d 7d 8d 9d Td Jd Qd Kd Ad 2h 3h 4h 5h 6h 7h 8h 9h Th Jh Qh Kh Ah 2s 3s 4s 5s 6s 7s 8s 9s Ts Js Qs Ks As "

    def test_shuffle_deck(self):
        unshuffled_deck = "2c 3c 4c 5c 6c 7c 8c 9c Tc Jc Qc Kc Ac 2d 3d 4d 5d 6d 7d 8d 9d Td Jd Qd Kd Ad 2h 3h 4h 5h 6h 7h 8h 9h Th Jh Qh Kh Ah 2s 3s 4s 5s 6s 7s 8s 9s Ts Js Qs Ks As "
        deck = Deck()
        deck.create()
        assert str(deck) == unshuffled_deck
        deck.shuffle()
        assert str(deck) != unshuffled_deck  # There is a VERY SMALL chance the shuffled deck will still be in the same order as above after the shuffle; but I wouldn't bet on it.
        assert len(deck.cards) == 52

    def test_shuffle_multiple_decks(self):
        unshuffled_deck = "2c 3c 4c 5c 6c 7c 8c 9c Tc Jc Qc Kc Ac 2d 3d 4d 5d 6d 7d 8d 9d Td Jd Qd Kd Ad 2h 3h 4h 5h 6h 7h 8h 9h Th Jh Qh Kh Ah 2s 3s 4s 5s 6s 7s 8s 9s Ts Js Qs Ks As "
        deck1 = Deck()
        deck1.create()
        deck2 = Deck()
        deck2.create()
        assert str(deck1) == str(deck2) == unshuffled_deck  # Same string results before the shuffle.
        assert deck1 != deck2  # Still different in memory because they were created as objects.
        deck1.shuffle()
        deck2.shuffle()
        assert str(deck1) != str(deck2) != unshuffled_deck
        assert len(str(deck1)) == len(str(deck2)) == len(unshuffled_deck) == 156  # The character length of each deck is 156 because there are 52 cards with a length of 2 + a space that separates them.
        assert len(deck1.cards) == len(deck2.cards) == 52
        assert str(deck1.cards) != str(deck2.cards)  # Both decks always have 52 cards, but they are in a random order after the shuffle.

    def test_dealt_deck(self):
        deck = Deck()
        deck.create()
        deck.shuffle()
        assert len(deck.cards) == 52
        before_deal = str(deck)
        deck.deal_card()
        assert len(deck.cards) == 51
        deck.deal_card()
        assert len(deck.cards) == 50
        after_deal = str(deck)
        assert before_deal[6:] == after_deal  # The 'top' cards of the deck are being dealt out just like in live play.

    def test_dealt_card(self):
        deck = Deck()
        deck.create()
        deck.shuffle()
        assert len(deck.cards) == 52
        before_deal = str(deck)
        top_card = deck.deal_card()
        assert len(deck.cards) == 51
        assert len(str(top_card)) == 2  # The top card trims off the trailing whitspace (Technically, doesn't really trim. The space was added to make it easier in the str method for development and manual testing).
        assert str(top_card) == before_deal[:2]  # The first 3 characters of the random deck match the first 2 dealt for the top card + the space.
        assert before_deal[3:] == str(deck)  # The rest of the deck is still in its random shuffled order.

    def test_no_deck_created(self):
        deck = Deck()
        deck.shuffle()
        assert str(deck) == "Sorry, no cards in deck. Please create a new deck; and then, shuffle up and deal."

    def test_out_of_cards(self):
        """For this game we are only concerned about the first two cards. However, if this was expanded to post flop the game flow could be like this.
        px = player number, cx = card number, xb = street burn card, fx = flop card, t = turn, r = river, ccx = count remaining cards."""
        deck = Deck()
        deck.create()
        deck.shuffle()
        assert len(deck.cards) == 52
        before_deal = str(deck)
        p1c1 = deck.deal_card()
        p1c2 = deck.deal_card()
        p2c1 = deck.deal_card()
        p2c2 = deck.deal_card()
        p3c1 = deck.deal_card()
        p3c2 = deck.deal_card()
        p4c1 = deck.deal_card()
        p4c2 = deck.deal_card()
        p5c1 = deck.deal_card()
        p5c2 = deck.deal_card()
        p6c1 = deck.deal_card()
        p6c2 = deck.deal_card()
        p7c1 = deck.deal_card()
        p7c2 = deck.deal_card()
        p8c1 = deck.deal_card()
        p8c2 = deck.deal_card()
        p9c1 = deck.deal_card()
        p9c2 = deck.deal_card()
        p10c1 = deck.deal_card()
        p10c2 = deck.deal_card()  # At a full table (10 players) this would complete the preflop deal.
        assert len(deck.cards) == 32  # 32 cards are left; which is more than enough for the community cards.
        assert p1c1 != p1c2 != p2c1 != p2c2 != p3c1 != p3c2 != p4c1 != p4c2 != p5c1 != p5c2 != p6c1 != p6c2 != p7c1 != p7c2 != p8c1 != p8c2 != p9c1 != p9c2 != p10c1 != p10c2  # All the cards are different.
        assert before_deal[60:] == str(deck)
        bf = deck.deal_card()  # Burning cards is done in live play to help prevent cheating and isn't really necessary online. Regardless, we still have enough cards either way.
        f1 = deck.deal_card()
        f2 = deck.deal_card()
        f3 = deck.deal_card()
        bt = deck.deal_card()
        t = deck.deal_card()
        br = deck.deal_card()
        r = deck.deal_card()
        assert len(deck.cards) == 24  # 24 cards are left; which sometimes you'll see the dealer count out to confirm all the cards are there.
        assert bf != f1 != f2 != f3 != bt != t != br != r
        assert before_deal[84:] == str(deck)
        cc1 = deck.deal_card()
        cc2 = deck.deal_card()
        cc3 = deck.deal_card()
        cc4 = deck.deal_card()
        cc5 = deck.deal_card()
        cc6 = deck.deal_card()
        cc7 = deck.deal_card()
        cc8 = deck.deal_card()
        cc9 = deck.deal_card()
        cc10 = deck.deal_card()
        cc11 = deck.deal_card()
        cc12 = deck.deal_card()
        cc13 = deck.deal_card()
        cc14 = deck.deal_card()
        cc15 = deck.deal_card()
        cc16 = deck.deal_card()
        cc17 = deck.deal_card()
        cc18 = deck.deal_card()
        cc19 = deck.deal_card()
        cc20 = deck.deal_card()
        cc21 = deck.deal_card()
        cc22 = deck.deal_card()
        cc23 = deck.deal_card()
        cc24 = deck.deal_card()
        assert len(deck.cards) == 0
        assert cc1 != cc2 != cc3 != cc4 != cc5 != cc6 != cc7 != cc8 != cc9 != cc10 != cc11 != cc12 != cc13 != cc14 != cc15 != cc16 != cc17 != cc18 != cc19 != cc20 != cc21 != cc22 != cc23 != cc24  # All different.
        assert str(deck) == "Sorry, no cards in deck. Please create a new deck; and then, shuffle up and deal."
        cc25 = deck.deal_card()  # This card doesn't exist.
        assert str(cc25) == "Sorry, unable to continue dealing because we are out of cards.\n" \
                            "This is somewhat odd because community card games (like No Limit Texas Hold'em) came about because many players don't like to fold.\n" \
                            "As a result, the community cards (the board consisting of the flop, turn, and river) should prevent this.\n" \
                            "Regardless, please create a new deck; and then, shuffle up and deal."
