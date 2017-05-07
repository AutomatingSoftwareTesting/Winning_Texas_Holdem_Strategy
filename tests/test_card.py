from app.card import Card


class TestSingleCard:
    """Unique and consistent playing cards. All valid cards have a length of 2; one for the rank and the other for the suit."""
    def test_ace_of_spades(self):
        assert str(Card("A", "s")) == "As"

    def test_four_of_hearts(self):
        assert str(Card("4", "h")) == "4h"

    def test_two_of_diamonds(self):
        assert str(Card("2", "d")) == "2d"

    def test_queen_of_clubs(self):
        assert str(Card("Q", "c")) == "Qc"  # Both correct
        assert str(Card("Q", "c")) != "Qd"  # Rank correct, suit incorrect
        assert str(Card("Q", "c")) != "Jc"  # Rank incorrect, suit correct
        assert str(Card("Q", "c")) != "5h"  # Both incorrect
        assert str(Card("Q", "c")) != "2d"  # Both incorrect; but both correct for card above which shouldn't be cached

    def test_card_length(self):
        assert len(str(Card("T", "d"))) == 2
        assert len(str(Card("10", "d"))) != 2


class TestRank:
    """There are 13 ranks or values in a standard deck. The rank determines the high card, pairs, two pair, trips, straight, full house, quads, and 'half' of a straight flush."""
    def test_card1(self):
        card = Card("A", "s")
        assert card.get_rank() == "A"
        assert card.get_rank() != "s"

    def test_card2(self):
        card = Card("6", "d")
        assert card.get_rank() == "6"
        assert card.get_rank() != "d"

    def test_card3(self):
        card = Card("5", "s")
        assert card.get_rank() == "5"
        assert card.get_rank() != "T"
        assert card.get_rank() != "6"
        assert card.get_rank() != "s"
        assert card.get_rank() != "c"

    def test_number_of_ranks(self):
        assert len(Card.RANKS) == 13

    def test_all_ranks_there(self):
        """The default numeric and alphabetic sorting of the ranks is NOT equal to the value sorting of them."""
        assert sorted(Card.RANKS) == ['2', '3', '4', '5', '6', '7', '8', '9', 'A', 'J', 'K', 'Q', 'T']
        assert sorted(Card.RANKS) != ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


class TestSuit:
    """There are 4 suits in a standard deck. The suit determines a flush and the other 'half' of a straight flush."""
    def test_card1(self):
        card = Card("J", "c")
        assert card.get_suit() == "c"
        assert card.get_suit() != "J"

    def test_card2(self):
        card = Card("9", "h")
        assert card.get_suit() == "h"
        assert card.get_suit() != "9"

    def test_card3(self):
        card = Card("3", "c")
        assert card.get_suit() == "c"
        assert card.get_suit() != "K"
        assert card.get_suit() != "9"
        assert card.get_suit() != "3"
        assert card.get_suit() != "d"
        assert card.get_suit() != "h"
        assert card.get_suit() != "s"

    def test_number_of_suits(self):
        assert len(Card.SUITS) == 4

    def test_all_suits_there(self):
        assert sorted(Card.SUITS) == ["c", "d", "h", "s"]
