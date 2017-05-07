from app.hand import Hand


class TestHand:
    def test_new_hand(self):
        """The two starting cards for each player consist of their pre-flop hand. Also, called the hole cards."""
        from app.deck import Deck
        deck = Deck()
        deck.create()
        deck.shuffle()
        before_deal = str(deck)
        hand = Hand()
        hand.get_hand(deck)
        assert str(hand) == before_deal[:6]  # See the test_deck module for an explanation of the number of characters.

    def test_hand_has_2_cards(self):
        from app.deck import Deck
        deck = Deck()
        deck.create()
        deck.shuffle()
        before_deal = str(deck)
        hand = Hand()
        hand.get_hand(deck)
        card1, card2 = hand.hole_cards
        assert str(card1) == before_deal[:2]
        assert str(card2) == before_deal[3:5]
        assert str(deck) == before_deal[6:]

    def test_order_2_num_no_sort_needed(self):
        from app.card import Card
        card1 = Card("6", "s")
        card2 = Card("4", "d")
        hand = Hand()
        hand.hole_cards = [card1, card2]
        oc1, oc2 = hand.order_hand()
        assert str(oc1) == "6s" and str(oc2) == "4d"
        assert str(oc1) != "4d" and str(oc2) != "6s"

    def test_order_2_num_sort_needed(self):
        from app.card import Card
        card1 = Card("3", "h")
        card2 = Card("4", "s")
        hand = Hand()
        hand.hole_cards = [card1, card2]
        oc1, oc2 = hand.order_hand()
        assert str(oc1) == "4s" and str(oc2) == "3h"
        assert str(oc1) != "3h" and str(oc2) != "4s"
        assert str(card1) == "3h" and str(card2) == "4s"

    def test_order_1_num_1_bw_no_sort_needed(self):
        from app.card import Card
        card1 = Card("A", "c")
        card2 = Card("4", "d")
        hand = Hand()
        hand.hole_cards = [card1, card2]
        oc1, oc2 = hand.order_hand()
        assert str(oc1) == "Ac" and str(oc2) == "4d"
        assert str(oc1) != "4d" and str(oc2) != "Ac"

    def test_order_1_num_1_bw_sort_needed(self):
        from app.card import Card
        card1 = Card("2", "h")
        card2 = Card("K", "s")
        hand = Hand()
        hand.hole_cards = [card1, card2]
        oc1, oc2 = hand.order_hand()
        assert str(oc1) == "Ks" and str(oc2) == "2h"
        assert str(oc1) != "2h" and str(oc2) != "Ks"
        assert str(card1) == "2h" and str(card2) == "Ks"

    def test_order_2_bw_no_sort_needed(self):
        from app.card import Card
        card1 = Card("J", "h")
        card2 = Card("T", "h")
        hand = Hand()
        hand.hole_cards = [card1, card2]
        oc1, oc2 = hand.order_hand()
        assert str(oc1) == "Jh" and str(oc2) == "Th"
        assert str(oc1) != "Th" and str(oc2) != "Jh"

    def test_order_2_bw_sort_needed(self):
        from app.card import Card
        card1 = Card("T", "d")
        card2 = Card("K", "c")
        hand = Hand()
        hand.hole_cards = [card1, card2]
        oc1, oc2 = hand.order_hand()
        assert str(oc1) == "Kc" and str(oc2) == "Td"
        assert str(oc1) != "Td" and str(oc2) != "Kc"
        assert str(card1) == "Td" and str(card2) == "Kc"

    def test_order_2_same_no_sort_needed(self):
        from app.card import Card
        card1 = Card("J", "h")
        card2 = Card("J", "c")
        hand = Hand()
        hand.hole_cards = [card1, card2]
        oc1, oc2 = hand.order_hand()
        assert str(oc1) == "Jh" and str(oc2) == "Jc"
        assert str(oc1) != "Jc" and str(oc2) != "Jh"

    def test_order_2_same_sort_needed(self):
        """This really never requires a sort; however, it will still be sorted alphabetically."""
        from app.card import Card
        card1 = Card("A", "s")
        card2 = Card("A", "d")
        hand = Hand()
        hand.hole_cards = [card1, card2]
        oc1, oc2 = hand.order_hand()
        assert str(oc1) == "Ad" and str(oc2) == "As"
        assert str(oc1) != "As" and str(oc2) != "Ad"
        assert str(card1) == "As" and str(card2) == "Ad"

    def test_off_suit_hand_type(self):
        from app.card import Card
        card1 = Card("A", "s")
        card2 = Card("T", "d")
        hand = Hand()
        hand.hole_cards = [card1, card2]
        assert str(hand.hand_type()) == "ATo"
        assert str(hand.hand_type()) != "ATs"

    def test_suited_hand_type(self):
        from app.card import Card
        card1 = Card("8", "h")
        card2 = Card("6", "h")
        hand = Hand()
        hand.hole_cards = [card1, card2]
        assert str(hand.hand_type()) == "86s"
        assert str(hand.hand_type()) != "86o"

    def test_pair_hand_type(self):
        from app.card import Card
        card1 = Card("Q", "c")
        card2 = Card("Q", "d")
        hand = Hand()
        hand.hole_cards = [card1, card2]
        assert str(hand.hand_type()) == "QQ"
        assert str(hand.hand_type()) != "QQs"
        assert str(hand.hand_type()) != "QQo"
        assert str(hand.hand_type()) != "QcQd"
