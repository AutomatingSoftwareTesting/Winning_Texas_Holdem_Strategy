import datetime
import app.players
import app.deck
import app.position
import app.range
import app.hand
import app.decision
import app.feedback_file


class PlayGame(object):
    def __init__(self, score=0, hand_num=1):
        self.score = score
        self.hand_num = hand_num

    def get_score(self):
        return int(self.score)

    def get_hand_num(self):
        return int(self.hand_num)

    def setup_game(self, session_players=6, hand_range="Unimproved Range.txt", output_format="csv", show_feedback=False):
        sp = session_players
        hr = hand_range
        of = output_format
        ff = app.feedback_file.FeedbackFile(sp, of)
        if show_feedback:  # Create feedback file only if user wants it. This will also allow non-Windows machines to play; just without feedback.
            ff.create_feedback_file()
        sf = show_feedback
        return sp, hr, ff, sf

    def play_hand(self, num_players, hand_range, feedback_file, show_feedback):
        date_time = datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S")
        print("Hand number: " + str(self.hand_num))

        deck = app.deck.Deck()
        deck.create()
        deck.shuffle()
        hand = app.hand.Hand()
        hand.get_hand(deck)
        print(hand)
        hand.order_hand()
        hand_type = hand.hand_type()

        position = app.position.Position()
        position.current_position(num_players)
        print(position)
        position_min = position.min_open()

        r = app.range.Range(hand_range)
        correct_decision, hand_percent, total_cards = r.correct_decision(hand_type, position_min)
        # print(correct_decision)  Leaving for reference in case someone else isn't that familiar with hand ranges.
        # print(hand_percent)
        # print(total_cards)  # To confirm the hand percentage is correct - total_cards / 1326 = hand_percent

        min_open_hand = r.min_open_card(position_min)
        # print(min_open_hand)

        action = int(input("What is your decision? (4=Open, 6=Fold): "))
        decision = app.decision.Decision(action).decision()

        if decision != "stop":
            if show_feedback:
                if decision == correct_decision:
                    # screen feedback
                    print("Good job! You should", correct_decision, "because you want to play the top {0:.2f}".format(position_min * 100) + "% of your range; which ends at " + str(min_open_hand) + ".\n" + str(hand) +
                          "is in the top {0:.2f}".format(hand_percent * 100) + "% of starting hands for the " + hand_range + " range.")
                    feedback = "Correct"  # report feedback
                    self.score += 1
                else:
                    print("Sorry, you should", correct_decision, "because you want to play the top {0:.2f}".format(position_min * 100) + "% of your range; which ends at " + str(min_open_hand) + ".\n" + str(hand) +
                          "is in the top {0:.2f}".format(hand_percent * 100) + "% of starting hands for the " + hand_range + " range.")
                    feedback = "Incorrect"  # report feedback
                feedback_file.save_hand(self.hand_num, date_time, hand_range, feedback, position, position_min, min_open_hand, hand, hand_type, hand_percent, decision, correct_decision, self.score)
                self.hand_num += 1
                print("Score: " + str(self.score) + "\n")
            else:
                self.hand_num += 1
                print()
        else:
            print("Thanks for playing.")

        return action


start_game = PlayGame()
session_num_players, session_range, session_file_extension, session_show_feedback = start_game.setup_game()
play = None
while play != 0:
    play = start_game.play_hand(session_num_players, session_range, session_file_extension, session_show_feedback)
