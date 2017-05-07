class Position(object):
    POSITIONS = ["Big Blind", "Small Blind", "Button", "Cut Off", "High Jack", "Low Jack", "5 Off Button", "6 Off Button", "7 Off Button", "8 Off Button"]

    def __init__(self, position=None):
        self.position = position

    def get_position(self):
        return self.position

    def current_position(self, num_players):
        import random
        self.position = Position.POSITIONS[random.randrange(2, num_players)]  # Not starting in the blinds
        return self.position

    def min_open(self):
        total_cards = 1326
        if self.position == "Button":
            return (total_cards / 3) / total_cards
        elif self.position == "Cut Off":
            return (total_cards / 4) / total_cards
        elif self.position == "High Jack":
            return (total_cards / 5) / total_cards
        elif self.position == "Low Jack":
            return (total_cards / 6) / total_cards
        elif self.position == "5 Off Button":
            return (total_cards / 7) / total_cards
        elif self.position == "6 Off Button":
            return (total_cards / 8) / total_cards
        elif self.position == "7 Off Button":
            return (total_cards / 9) / total_cards
        elif self.position == "8 Off Button":
            return (total_cards / 10) / total_cards
        else:
            print("Unexpected position.")

    def __str__(self):
        return str(self.position)
