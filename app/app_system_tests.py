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
    assurance tester, 5) this could help troubleshoot performance issues with hardware (and if valid networks, databases), etc., and 6) this simulates gui user selection options."""

    def __init__(self, score=0, hand_num=1):
        self.score = score
        self.hand_num = hand_num

    # System setup folder location checks
    if len(os.listdir("..\\images\\cards")) != 52:
        print("Something is wrong with the setup. There aren't 52 cards in the images -> cards folder.")
    if len(os.listdir("..\\images\\tables")) != 9:
        print("Something is wrong with the setup. There aren't 9 tables in the images -> tables folder.")
    if len(os.listdir("..\\hand_ranges")) < 1:
        print("Something is wrong with the setup. There aren't any ranges in the hand_ranges folder.")

    def setup_game_tests(self, session_players, session_range, output_format, show_feedback):
        feedback_file = FeedbackFile(session_players, output_format)
        feedback_file.create_feedback_file()
        return session_players, session_range, feedback_file, show_feedback

    def play_hand(self, session_players, session_range, feedback_file, show_feedback, action):  # Adding the action to simulate faster input of '4' = open and '6' = close.
        date_time = datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S")
        deck = Deck()
        deck.create()
        deck.shuffle()
        hand = Hand()
        hand.get_hand(deck)
        hand.order_hand()
        type = hand.hand_type()
        position = Position()
        position.current_position(session_players)
        position_min = position.min_open()
        r = Range(session_range)
        correct_decision, hand_percent, total_cards = r.correct_decision(type, position_min)
        min_open_hand = r.min_open_card(position_min)
        decision = Decision(action).decision()
        # show_feedback = True  # This setting is only used in the gui so there isn't any additional test for it here.

        if show_feedback:
            if decision == correct_decision:
                feedback = "Correct"  # report feedback
                self.score += 1
            else:
                feedback = "Incorrect"  # report feedback
            feedback_file.save_hand(self.hand_num, date_time, session_range, feedback, position, position_min, min_open_hand, hand, type, hand_percent, decision, correct_decision, self.score)
            self.hand_num += 1

        return self.hand_num




"""These tests could be done several different ways depending on who they are for and what is need. I'm displaying them below to show the general idea of each test. Note: Some of these tests don't really make
sense in a simplified example such as this project. However, the ideas would still apply if there were at least tens of thousands of lines of code written by multiple developers over time, several networks,
different types of databases/operating systems, etc., involved."""

# Testing default setup parameters in the gui.
start_test1 = AppSystemTests()
num_players, range, file_extension, show_feedback = start_test1.setup_game_tests(6, "Unimproved Range.txt", "csv", True)
hand_num = 0
while hand_num < 21:
    hand_num = start_test1.play_hand(num_players, range, file_extension, show_feedback, 6)

# Testing non-default setup parameters.
start_test2 = AppSystemTests()
num_players, range, file_extension, show_feedback = start_test2.setup_game_tests(10, "Starting Hands EV Range.txt", "txt", False)
hand_num = 0
while hand_num < 21:
    hand_num = start_test2.play_hand(num_players, range, file_extension, show_feedback, 6)

# Testing the min player size. Note: with manual bounds testing would also test the number of players that aren't valid (2, 11, d); however, instead made it impossible to enter these values in the gui.
start_test3 = AppSystemTests()
num_players, range, file_extension, show_feedback = start_test3.setup_game_tests(3, "Unimproved Range.txt", "txt", False)
hand_num = 0
while hand_num < 21:
    hand_num = start_test3.play_hand(num_players, range, file_extension, show_feedback, 4)

# Testing a mix of setup parameters that have not already been selected for other tests.
start_test4 = AppSystemTests()
num_players, range, file_extension, show_feedback = start_test4.setup_game_tests(5, "Starting Hands EV Range.txt", "csv", True)
hand_num = 0
while hand_num < 21:
    hand_num = start_test4.play_hand(num_players, range, file_extension, show_feedback, 4)


"""Testing performance of system.
Note: This is really a different type of test than those above and would have separate analysis. Its result could encourage enhancing performance: i.e. multi-threading or parallel processing. It is also
unnecessary to do this type of testing if the tests above aren't working. The following tests were run on my machine at different times over 2 days as csv output. Base test result for future comparisons:
1) Less than a minute for 10,000 hands with a file size of 1,012KB; 2) 4 min for 100,000 hands with a file size of 10,519KB; 3) 17 minutes for 388,544 hands with a file size of 40,659KB; and
4) 52 minutes for 1 million hands with a file size of 114,312KB."""

# Only running 200 times here to show the concept.
start_test5 = AppSystemTests()
num_players, range, file_extension, show_feedback = start_test5.setup_game_tests(9, "Starting Hands EV Range.txt", "csv", True)
hand_num = 0
while hand_num < 201:
    hand_num = start_test5.play_hand(num_players, range, file_extension, show_feedback, 4)


# def test_application(self):
#     from app_no_gui import PlayGame
#
#     # System setup folder location checks
#     if len(os.listdir("..\\images\\cards")) != 52:
#         print("Something is wrong with the setup. There aren't 52 cards in the images -> cards folder.")
#     if len(os.listdir("..\\images\\tables")) != 9:
#         print("Something is wrong with the setup. There aren't 9 tables in the images -> tables folder.")
#     if len(os.listdir("..\\hand_ranges")) < 1:
#         print("Something is wrong with the setup. There aren't any ranges in the hand_ranges folder.")
#
#     return PlayGame()
#
#
# start = AppSystemTests().test_application()
# np, r, f, sf = start.setup_game()
# hand_num = 0
# while hand_num < 21:
#     hand_num = start.play_hand(np, r, f, sf, 6)