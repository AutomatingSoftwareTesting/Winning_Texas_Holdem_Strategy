import sys
import tkinter.messagebox
from dir_nav import DirNav


class Range(object):
    def __init__(self, my_range=None):
        self.my_range = my_range
        self.file_path = DirNav().get_path("hand_ranges")

    def get_my_range(self):
        return self.my_range

    def get_file_path(self):
        return self.file_path

    def full_file_name(self):
        return str(self.file_path) + str(self.get_my_range())

    def error_notes(self):
        return "Notes:\n" \
               "- Each hand type should be on its own line.\n" \
               "- Valid hand types are pairs (55), off-suit (AKo), and suited (75s) hands.\n" \
               "- There are 6 ways to make any pair, 12 combos of any off-suited hand, and 4 combos for suited hands.\n" \
               "- For example, 6♠6♥, plus the 5 other ways to make this pair, in the file would map to '66'; K♥3♣ to 'K3o', and 9♦8♦ to '98s'.\n" \
               "- There cannot be blank lines at the beginning or middle of the file. They shouldn't matter at the end.\n" \
               "- The higher ranked card needs to be first for suited and unsuited hands.\n" \
               "- Please fix your " + str(self.get_my_range()) + " file and then start the game again."

    def file_exists(self):
        file = self.full_file_name()
        error_notes = self.error_notes()
        try:
            with open(file, "r") as my_range:
                if len(my_range.readline()) < 2 or len(my_range.readline()) > 3:
                    pass
                else:
                    a = my_range.readline()[-1]  # Once here we always want to trigger an index error. Assigning to a variable to 'fix' error pep8 error message.
                    # If I return this to get rid of the warning it causes problems later because a '\n' is added. Also, if I remove the else part entirely a different, less helpful Index Error message is displayed.
        except IOError as ex:
            tkinter.messagebox.showerror("ERROR! Unable to read the file.", "Please fix the spelling of the text file name and then start the game again. Remember, the file extension should be '.txt'.\n\n" + str(ex))
            sys.exit()
        except IndexError as ex:
            tkinter.messagebox.showerror("ERROR! The first line in the file isn't in the correct format.", error_notes + "\n\nPython exception message: " + str(ex))
            sys.exit()
        else:
            return file

    def file_layout(self):
        # Validates card length, number of hand types, and number of card combos. However, will not catch if the smaller card is first; i.e. KAs instead of AKs.
        # In the future, may try to use the gui to have only valid cards in range instead of having the user upload a file. This will prevent the last issue above.
        file = self.file_exists()
        error_notes = self.error_notes()
        counter = 0
        total_cards = 0
        is_error = False
        error_count = 0
        error_total = 0

        with open(file, "r") as my_range:
            for line in my_range:
                counter += 1
                ranking = line.split()
                for hand_type in ranking:
                    invalid_hand_type = []
                    invalid_line = []
                    error_len = "You have an invalid hand type in your range at line " + str(counter) + ".\n" \
                                "Problem data: '" + str(hand_type) + "'"
                    if len(hand_type) < 2 or len(hand_type) > 3:
                        invalid_hand_type.append(hand_type)
                        invalid_line.append(counter)
                        tkinter.messagebox.showerror("ERROR! Problem with data in file.", error_len)
                        is_error = True
                    elif hand_type[0] == hand_type[1]:
                        if len(hand_type) == 2:
                            num_cards = 6
                            total_cards += num_cards
                        else:
                            invalid_hand_type.append(hand_type)
                            invalid_line.append(counter)
                            tkinter.messagebox.showerror("ERROR! Problem with data in file.", error_len)
                            is_error = True
                    elif hand_type[2] == "s":
                        num_cards = 4
                        total_cards += num_cards
                    else:
                        num_cards = 12
                        total_cards += num_cards
                    total_cards = total_cards

            if counter != 169:
                error_count = "There are 169 different hand types in a range.\n" \
                              "Your file has " + str(counter) + " lines.\n"
                is_error = True

            if total_cards != 1326:
                error_total = "There are 1,326 different card combinations in a range.\n" \
                              "Your file has " + str(format(total_cards, ",d")) + ".\n" \
                              "Hint: This most likely means that you have a duplicate hand type somewhere in your range if this is the only error."
                is_error = True

            if is_error:
                tkinter.messagebox.showerror("ERROR! Problem with data in file.", error_count + "\n" + error_total + "\n\n" + error_notes)
                sys.exit()
            else:
                return file

    def correct_decision(self, hand_type_dealt, min_open):
        file = self.file_layout()
        counter = 0
        total_cards = 0
        with open(file, "r") as my_range:
            for line in my_range:
                counter += 1
                ranking = line.split()
                for hand_type in ranking:
                    if hand_type[0] == hand_type[1]:
                        num_cards = 6
                        total_cards += num_cards
                    elif hand_type[2] == "s":
                        num_cards = 4
                        total_cards += num_cards
                    else:
                        num_cards = 12
                        total_cards += num_cards
                    total_cards = total_cards

                    if hand_type == hand_type_dealt:
                        if total_cards / 1326 <= min_open:
                            correct_decision = "open"
                        else:
                            correct_decision = "fold"

                        hand_percent = total_cards / 1326
                        return correct_decision, hand_percent, total_cards

    def min_open_card(self, min_open):
        file = self.file_layout()
        counter = 0
        total_cards = 0
        with open(file, "r") as my_range:
            for line in my_range:
                counter += 1
                ranking = line.split()
                for hand_type in ranking:
                    if hand_type[0] == hand_type[1]:
                        num_cards = 6
                        total_cards += num_cards
                    elif hand_type[2] == "s":
                        num_cards = 4
                        total_cards += num_cards
                    else:
                        num_cards = 12
                        total_cards += num_cards
                    total_cards = total_cards

                    if total_cards / 1326 <= min_open:
                        pass
                    else:
                        return hand_type

    def __str__(self):
        return self.my_range
