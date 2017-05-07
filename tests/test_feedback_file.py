from app.feedback_file import FeedbackFile


class TestFeedbackFile:
    def test_file_name(self):
        """The directory paths will be unique for each installation."""
        import datetime
        date_time = datetime.datetime.now().strftime("%m-%d-%y %H%M")
        setup_specific_path = "C:\\Users\\jdcald13\\Documents\\repos\\Winning_Texas_Holdem_Strategy\\"

        file_name_1 = str(FeedbackFile(8))
        assert file_name_1 == setup_specific_path + "../reports/8-Handed Range Trainer " + str(date_time) + ".csv"  # .csv is the default file extension.

        file_name_2 = str(FeedbackFile(5, "txt"))
        assert file_name_2 == setup_specific_path + "../reports/5-Handed Range Trainer " + str(date_time) + ".txt"

    def test_create_file(self, tmpdir):
        """Using temporary directories so that nothing is created from a user's perspective if this was also used in a live environment."""
        temp_file = tmpdir.mkdir("create").join("temp_file.csv")
        temp_file.write("Hand Number,Date/Time,Range File,Feedback,Position,Position Percentage,Min Opening Hand Type,Hole Cards,Hand Type,Hand Ranking Percentage,Your Decision,Correct Decision,Score\n")
        assert temp_file.read() == "Hand Number,Date/Time,Range File,Feedback,Position,Position Percentage,Min Opening Hand Type,Hole Cards,Hand Type,Hand Ranking Percentage,Your Decision,Correct Decision,Score\n"
        assert len(tmpdir.listdir()) == 1

    def test_save_hand(self, tmpdir):
        hand_num, date_time, session_range, feedback, position, min_play, min_open_hand, hole_cards, type_hand, hand_percent, decision, correct_decision, score = \
            1, "5/5/2017 3:54:50", "test.txt", "Correct", "Button", .333333, "K2o", "Kc 7c", "K7c", .267019, "open", "open", 1
        temp_file = tmpdir.mkdir("save").join("temp_file.txt")
        temp_file.write("%i,%s,%s,%s,%s,%0.2f,%s,%s,%s,%0.2f,%s,%s,%i\n" % (hand_num, date_time, session_range, feedback, position, min_play * 100, min_open_hand, hole_cards, type_hand, hand_percent * 100,
                                                                            decision, correct_decision, score))
        assert temp_file.read() == "1,5/5/2017 3:54:50,test.txt,Correct,Button,33.33,K2o,Kc 7c,K7c,26.70,open,open,1\n"
        assert len(tmpdir.listdir()) == 1

        temp_file_2 = tmpdir.join("temp_file_2.csv")
        temp_file_2.write("%i,%s,%s,%s,%s,%0.2f,%s,%s,%s,%0.2f,%s,%s,%i\n" % (hand_num, date_time, session_range, feedback, position, min_play * 100, min_open_hand, hole_cards, type_hand, hand_percent * 100,
                                                                              decision, correct_decision, score))
        assert temp_file_2.read() == "1,5/5/2017 3:54:50,test.txt,Correct,Button,33.33,K2o,Kc 7c,K7c,26.70,open,open,1\n"
        assert len(tmpdir.listdir()) == 2
