import datetime
from app.deck import Deck
from app.hand import Hand
from app.position import Position
from app.range import Range
from app.decision import Decision
from app.feedback_file import FeedbackFile


class PlayGame(object):
    def __init__(self, num_players=6, hand_range="Unimproved Range.txt", file_extension=".csv", show_feedback=True, score=0, hand_num=1):
        self.score = score
        self.hand_num = hand_num
        self.num_players = num_players
        self.hand_range = hand_range
        self.file_extension = file_extension
        self.show_feedback = show_feedback

    def get_score(self):
        return int(self.score)

    def get_hand_num(self):
        return int(self.hand_num)

    def get_num_players(self):
        return int(self.num_players)

    def get_hand_range(self):
        return self.hand_range

    def get_file_extension(self):
        return self.file_extension

    def get_show_feedback(self):
        return self.show_feedback

    def setup_game(self):
        full_file_name = FeedbackFile(self.num_players, self.file_extension)
        if self.show_feedback:  # Create feedback file only if user wants it.
            full_file_name.create_feedback_file()
        return full_file_name

    def play_hand(self, feedback_file_name):
        date_time = datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S")
        print("Hand number: " + str(self.hand_num))

        deck = Deck()
        deck.create()
        deck.shuffle()

        hand = Hand()
        hand.get_hand(deck)
        print(hand)

        hand.order_hand()
        hand_type = hand.hand_type()

        position = Position()
        position.current_position(self.num_players)
        print(position)

        position_min = position.min_open()

        r = Range(self.hand_range)
        correct_decision, hand_percent, total_cards = r.correct_decision(hand_type, position_min)
        # Leaving the following several print statements for reference in case someone else isn't that familiar with hand range calculations.
        # print(correct_decision)
        # print(hand_percent)
        # print(total_cards)  # To confirm the hand percentage is correct: total_cards / 1326 = hand_percent

        min_open_hand = r.min_open_card(position_min)
        # print(min_open_hand)

        action = int(input("What is your decision? (4=Open, 6=Fold): "))  # For faster keyboard input
        decision = Decision(action).decision()

        if decision != "stop":
            if self.show_feedback:
                if decision == correct_decision:
                    # screen feedback
                    print("Good job! You should", correct_decision, "because you want to play the top {0:.2f}".format(position_min * 100) + "% of your range; which ends at " + str(min_open_hand) + ".\n" + str(hand) +
                          "is in the top {0:.2f}".format(hand_percent * 100) + "% of starting hands for the " + self.hand_range + " range.")
                    feedback = "Correct"  # report feedback
                    self.score += 1
                else:
                    print("Sorry, you should", correct_decision, "because you want to play the top {0:.2f}".format(position_min * 100) + "% of your range; which ends at " + str(min_open_hand) + ".\n" + str(hand) +
                          "is in the top {0:.2f}".format(hand_percent * 100) + "% of starting hands for the " + self.hand_range + " range.")
                    feedback = "Incorrect"  # report feedback
                feedback_file_name.save_hand(self.hand_num, date_time, self.hand_range, feedback, position, position_min, min_open_hand, hand, hand_type, hand_percent, decision, correct_decision, self.score)
                self.hand_num += 1
                print("Score: " + str(self.score) + "\n")
            else:
                self.hand_num += 1
                print()
        else:
            print("Thanks for playing.")

        return action


start_game = PlayGame()
file_name = start_game.setup_game()
play = None
while play != 0:
    play = start_game.play_hand(file_name)
