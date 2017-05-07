class Players(object):
    def __init__(self, num_players=10):
        self.num_players = num_players

    def get_num_players(self):
        return int(self.num_players)

    def __str__(self):
        return str(self.num_players)
