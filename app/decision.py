class Decision(object):
    def __init__(self, action=None):
        self.action = action

    def get_action(self):
        return self.action

    def decision(self):
        action = self.get_action()
        if action == 4:
            return "open"
        elif action == 6:
            return "fold"
        elif action == 0:  # A way to stop getting more hands without an IDE
            return "stop"
        else:
            print("Invalid choice.")

    def __str__(self):
        return str(self.action)
