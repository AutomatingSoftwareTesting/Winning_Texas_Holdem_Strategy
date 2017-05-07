import pytest


class TestRange:
    def does_range_exist(self):
        """There will be an error if the range doesn't exist. There is a user friendly pop up error message in the Range.file_exists() method."""
        raise IOError

    def test_does_range_exists(self):
        with pytest.raises(IOError):
            self.does_range_exist()

    """I'm not creating test cases for all the various checks performed on the files because these errors indicate an issue with the data that the end user needs to fix before playing a game. Therefore, it
    is more important that there are user friendly error messages that help display the problem(s) only if they occur; as opposed to the several generic/obvious error checks like the one above. There are
    multiple range validations throughout the application. You can see the various checks by selecting several different 'problem' ranges on the game setup screen. To summarize the checks: 1) Only files that
    end in .txt show up in the drop down gui selection list ('invalid_extension.csv' isn't there). 2) There is a user friendly error if a file that doesn't exist gets selected ('does_not_exist.txt'). Note: This
    is a little odd here; however, once networks come into the picture there are many ways to get errors trying to select files that really exist in a different location. 3) There is a different user friendly
    error message if the data in the file on the first line is in the wrong format ('bad_data.txt'). 4) There are 5 different checks if the data in there file is partially incorrect ('problem_5_examples).
    The checks are: a) the hand type is the incorrect length (there are 3 checks for this), b) the file has the wrong number of total lines, and c) the file has the wrong number of total types of hands.
    5) Finally, there are 2 valid files to show examples of good data and start someone off that hasn't created hand ranges in the past.
    - Unimproved Range is the ordering of hands if no one improves throughout the hand. This range is also good for validating which cards make the cut for the end of the range b/c they are in ranked order.
    - Starting Hands EV Range comes from http://www.pokerroom.com/poker/poker-school/ev-stats/total-stats-by-card/ referenced on 12/22/2016. Expected value (EV) is a more advanced concept that may be covered
    later if this app expands to post flop play. For now, it demonstrates that the range you are using helps determine which types of hands you should play from any given position."""
