from app.players import Players


class TestPlayers:
    def test_default_num_players(self):
        players = str(Players())
        assert players == "10"

    def test_set_num_players(self):
        players = str(Players(6))
        assert players == "6"
