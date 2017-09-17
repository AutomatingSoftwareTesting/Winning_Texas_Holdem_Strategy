import datetime
from app.deck import Deck
from app.hand import Hand
from app.position import Position
from app.range import Range
from app.decision import Decision
from app.feedback_file import FeedbackFile
import os


class AppSystemTests(object):
    """This module is different from the rest of the application and is intended to show some concepts related to testing the whole system. This will create 5 different reports in the user's report folder.
    Additional information about the setup scenarios for each of the reports is below. Some key ideas: 1) this runs in a 'live' environment and touches all of the critical functionality of the application,
    2) if there are serious errors in any of the modules, none of the reports will output and there should be an exception somewhere to analyze and fix, 3) if someone implements the system incorrectly, or
    moves key setup items later, #2 will also happen, 4) the outputted data simulates 'real' results that someone could further analyze for varying reasons; i.e. the customer, software manager, manual quality
    assurance tester, 5) this could help troubleshoot performance issues with hardware (and if valid networks, databases), etc., and 6) this simulates gui user selection options.
    If the future want to change this so it runs against app_no_gui code. Several things in the play hand section have to be updated only here for that to work."""

    def __init__(self, num_players=6, hand_range="Unimproved Range.txt", file_extension=".csv", show_feedback=True, score=0, hand_number=1):
        self.score = score
        self.hand_num = hand_number
        self.num_players = num_players
        self.hand_range = hand_range
        self.file_extension = file_extension
        self.show_feedback = show_feedback

    # System setup folder location checks
    if len(os.listdir("..\\images\\cards")) != 52:
        print("Something is wrong with the setup. There aren't 52 cards in the images -> cards folder.")
    if len(os.listdir("..\\images\\tables")) != 9:
        print("Something is wrong with the setup. There aren't 9 tables in the images -> tables folder.")
    if len(os.listdir("..\\hand_ranges")) < 1:
        print("Something is wrong with the setup. There aren't any ranges in the hand_ranges folder.")

    def test_setup_game(self):
        full_file_name = FeedbackFile(self.num_players, self.file_extension)
        if self.show_feedback:  # Create feedback file only if user wants it. This will also allow non-Windows machines to play; just without feedback.
            full_file_name.create_feedback_file()
        return full_file_name

    def play_hand(self, feedback_file_name, action):
        date_time = datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S")
        deck = Deck()
        deck.create()
        deck.shuffle()
        hand = Hand()
        hand.get_hand(deck)
        hand.order_hand()
        hand_type = hand.hand_type()
        position = Position()
        position.current_position(self.num_players)
        position_min = position.min_open()
        r = Range(self.hand_range)
        correct_decision, hand_percent, total_cards = r.correct_decision(hand_type, position_min)
        min_open_hand = r.min_open_card(position_min)
        decision = Decision(action).decision()

        if self.show_feedback:
            if decision == correct_decision:
                feedback = "Correct"  # report feedback
                self.score += 1
            else:
                feedback = "Incorrect"  # report feedback
            feedback_file_name.save_hand(self.hand_num, date_time, self.hand_range, feedback, position, position_min, min_open_hand, hand, hand_type, hand_percent, decision, correct_decision, self.score)
            self.hand_num += 1
        else:
            self.hand_num += 1

        return self.hand_num


"""These tests could be done several different ways depending on who they are for and what is need. I'm displaying them below to show the general idea of each test. Note: Some of these tests don't really make
sense in a simplified example such as this project. However, the ideas would still apply if there were at least tens of thousands of lines of code written by multiple developers over time, several networks,
different types of databases/operating systems, etc., involved."""

# Testing default setup parameters in the gui.
start_test1 = AppSystemTests(6, "Unimproved Range.txt", "csv", True)
feedback_file = start_test1.test_setup_game()
hand_num = 0
while hand_num < 21:
    hand_num = start_test1.play_hand(feedback_file, 6)

# Testing non-default setup parameters.
start_test2 = AppSystemTests(10, "Starting Hands EV Range.txt", "txt", True)
feedback_file = start_test2.test_setup_game()
hand_num = 0
while hand_num < 21:
    hand_num = start_test2.play_hand(feedback_file, 6)

# Testing the min player size. Note: with manual bounds testing would also test the number of players that aren't valid (2, 11, d); however, instead made it impossible to enter these values in the gui.
start_test3 = AppSystemTests(3, "Unimproved Range.txt", "txt", True)
feedback_file = start_test3.test_setup_game()
hand_num = 0
while hand_num < 21:
    hand_num = start_test3.play_hand(feedback_file, 4)

# Testing a mix of setup parameters that have not already been selected for other tests.
start_test4 = AppSystemTests(5, "Starting Hands EV Range.txt", "csv", True)
feedback_file = start_test4.test_setup_game()
hand_num = 0
while hand_num < 21:
    hand_num = start_test4.play_hand(feedback_file, 4)

# Testing that no report is generated (7 is a unique number so if this is working no report should start with 7 in the hand_range folder). This also means the user won't see feedback on the screen.
start_test6 = AppSystemTests(7, "Unimproved Range.txt", "txt", False)
feedback_file = start_test6.test_setup_game()
hand_num = 0
while hand_num < 21:
    hand_num = start_test6.play_hand(feedback_file, 4)


"""Testing performance of system.
Note: This is really a different type of test than those above and would have separate analysis. Its result could encourage enhancing performance: i.e. multi-threading or parallel processing. It is also
unnecessary to do this type of testing if the tests above aren't working. The following tests were run on my machine at different times over 2 days as csv output. Base test result for future comparisons:
1) Less than a minute for 10,000 hands with a file size of 1,012KB; 2) 4 min for 100,000 hands with a file size of 10,519KB; 3) 17 minutes for 388,544 hands with a file size of 40,659KB; and
4) 52 minutes for 1 million hands with a file size of 114,312KB."""

# Only running 200 times here to show the concept.
start_test5 = AppSystemTests(9, "Starting Hands EV Range.txt", "csv", True)
feedback_file = start_test5.test_setup_game()
hand_num = 0
while hand_num < 201:
    hand_num = start_test5.play_hand(feedback_file, 4)
