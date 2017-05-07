import datetime
from app.dir_nav import FolderNavigation


class FeedbackFile(object):
    def __init__(self, num_players, output_format="csv"):
        date_time = datetime.datetime.now().strftime("%m-%d-%y %H%M")
        report_dir = FolderNavigation().get_path("reports")
        feedback_file = report_dir + str(num_players) + "-Handed Range Trainer " + date_time + "." + output_format
        self.feedback_file = feedback_file

    def create_feedback_file(self):
        """Adding a header line for the selected setup. This will overwrite other files with the same setup in the same minute. Using overwrite b/c only want one header line per file."""
        file = open(self.feedback_file, "w")
        file.write("Hand Number,Date/Time,Range File,Feedback,Position,Position Percentage,Min Opening Hand Type,Hole Cards,Hand Type,Hand Ranking Percentage,Your Decision,Correct Decision,Score\n")
        file.close()

    def save_hand(self, hand_num, date_time, session_range, feedback, position, min_play, min_open_hand, hole_cards, type_hand, hand_percent, decision, correct_decision, score):
        file = open(self.feedback_file, "a")
        file.write("%i,%s,%s,%s,%s,%0.2f,%s,%s,%s,%0.2f,%s,%s,%i\n" % (hand_num, date_time, session_range, feedback, position, min_play * 100, min_open_hand, hole_cards, type_hand, hand_percent * 100,
                                                                       decision, correct_decision, score))
        file.close()

    def __str__(self):
        return self.feedback_file
