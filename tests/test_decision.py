from app.decision import Decision


class TestDecision:
    """These decisions will be replaced in the gui. However, they will still be useful for the auto application tests later."""
    def test_decision(self):
        open_decision = Decision(4)
        fold_decision = Decision(6)
        end_game_decision = Decision(0)
        assert open_decision.decision() == "open"
        assert fold_decision.decision() == "fold"
        assert end_game_decision.decision() == "stop"
