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

    def setup_game(self):
        # print(session_players)
        session_players = 6
        range = "Unimproved Range.txt"
        # print(range)
        output_format = "csv"
        feedback_file = app.feedback_file.FeedbackFile(session_players, output_format)
        feedback_file.create_feedback_file()
        # print(feedback)
        show_feedback = True
        return session_players, range, feedback_file, show_feedback

    def play_hand(self, session_players, range, feedback_file, show_feedback):
        date_time = datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S")
        print("Hand number: " + str(self.hand_num))
        # print(self.score)

        deck = app.deck.Deck()
        deck.create()
        deck.shuffle()
        # print(deck)
        hand = app.hand.Hand()
        hand.get_hand(deck)
        print(hand)
        hand.order_hand()
        type = hand.hand_type()
        # print(type)

        position = app.position.Position()
        position.current_position(session_players)
        print(position)
        position_min = position.min_open()
        # print(position_min)

        r = app.range.Range(range)
        correct_decision, hand_percent, total_cards = r.correct_decision(type, position_min)
        # print(correct_decision)
        # print(hand_percent)
        # print(total_cards)  # To confirm the hand percentage is correct - total_cards / 1326 = hand_percent

        min_open_hand = r.min_open_card(position_min)
        # print(min_open_hand)

        action = int(input("What is your decision? (4=Open, 6=Fold): "))
        decision = app.decision.Decision(action).decision()
        # print(decision)

        if decision != "stop":
            if decision == correct_decision:
                # screen feedback
                print("Good job! You should", correct_decision, "because you want to play the top {0:.2f}".format(position_min * 100) + "% of your range; which ends at " + str(min_open_hand) + ".\n" + str(hand) +
                      "is in the top {0:.2f}".format(hand_percent * 100) + "% of starting hands for the " + range + " range.")
                feedback = "Correct"  # report feedback
                self.score += 1
            else:
                print("Sorry, you should", correct_decision, "because you want to play the top {0:.2f}".format(position_min * 100) + "% of your range; which ends at " + str(min_open_hand) + ".\n" + str(hand) +
                      "is in the top {0:.2f}".format(hand_percent * 100) + "% of starting hands for the " + range + " range.")
                feedback = "Incorrect"  # report feedback
            feedback_file.save_hand(self.hand_num, date_time, range, feedback, position, position_min, min_open_hand, hand, type, hand_percent, decision, correct_decision, self.score)
            self.hand_num += 1
            print("Score: " + str(self.score) + "\n")
        else:
            print("Thanks for playing.")

        return action


a = PlayGame()
b, c, d, e = a.setup_game()
play = None
while play != 0:
    play = a.play_hand(b, c, d, e)