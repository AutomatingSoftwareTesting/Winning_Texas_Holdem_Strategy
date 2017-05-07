from app.position import Position


class TestPosition:
    def test_all_positions_there(self):
        positions = Position()
        assert sorted(positions.POSITIONS) == ['5 Off Button', '6 Off Button', '7 Off Button', '8 Off Button', 'Big Blind', 'Button', 'Cut Off', 'High Jack', 'Low Jack', 'Small Blind']

    def test_default_random_position(self):
        """Could improve this test in relation to what the current position becomes. However, if there was an error it could be hard to track down because the random functionality isn't always reproducible.
        Therefore, this test is to confirm there are no errors with the default table size. Another test case that saves data to a file will record what position is getting randomly assigned."""
        from app.players import Players
        session_size = str(Players())  # Default is 10 players.
        num_players = int(session_size)
        position = Position()
        cp = position.current_position(num_players)
        assert num_players == 10
        assert len(cp) > 5  # The button has the shortest length of 6 characters. These names are also constants (POSITIONS) so they shouldn't be changed; i.e. changing 'button' to 'b'.

    def test_smallest_random_position(self):
        """This makes the only valid choice become the button."""
        from app.players import Players
        session_size = str(Players(3))
        num_players = int(session_size)
        position = Position()
        cp = position.current_position(num_players)
        assert num_players == 3
        assert cp == "Button"

    def test_min_open(self):
        """ Since we are working with decimals/fractions not all numbers can be represented. Will leave all formatting for the gui so the end user will see it. These are just approximations."""
        b = Position('Button')
        p = int(b.min_open() * 100)
        p /= 100
        assert p == 0.33

        co = Position('Cut Off')
        p = int(co.min_open() * 100)
        p /= 100
        assert p == 0.25

        hj = Position('High Jack')
        p = int(hj.min_open() * 100)
        p /= 100
        assert p == 0.20

        lj = Position('Low Jack')
        p = int(lj.min_open() * 100)
        p /= 100
        assert p == 0.16

        b5o = Position('5 Off Button')
        p = int(b5o.min_open() * 100)
        p /= 100
        assert p == 0.14

        b6o = Position('6 Off Button')
        p = int(b6o.min_open() * 100)
        p /= 100
        assert p == 0.12

        b7o = Position('7 Off Button')
        p = int(b7o.min_open() * 100)
        p /= 100
        assert p == 0.11

        b8o = Position('8 Off Button')
        p = int(b8o.min_open() * 100)
        p /= 100
        assert p == 0.10
