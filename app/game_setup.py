from tkinter import *
from app.dir_nav import DirNav
import app.feedback_file
import app.range
import os


class GameSetup(Frame):
    def __init__(self, master):
        super(GameSetup, self).__init__(master)
        self.create_widgets()
        app_setup.grid_columnconfigure(0, weight=1)

    def create_widgets(self):
        Label(self, text="Welcome to the No Limit Texas Hold'em Pre-flop Range Trainer Setup Lobby", font=("Arial", 18)).grid(row=0, column=0, columnspan=3, pady=(20, 0))

        instructions = "The vast majority of poker trainers use simplified starting hand charts with a fixed number of players. As a result, they aren't very helpful unless you play in the same " \
                       "very limited scenarios that they simulate.\n\n" \
                       " A brief overview:\n" \
                       "- There are 1,326 unique starting hands in the deck; therefore, we can use card combinatorics to determine which types of hands you (and your opponents) will get dealt on average. These " \
                       "simplify to a 169 different types of hands; such as pairs, suited, and unsuited cards. But the likelihood of being dealt any combination of these varies.\n" \
                       "- There are 6 (3x2) ways to get dealt any pocket pair; i.e. 44 can be dealt as 4♠4♥, 4♠4♦, 4♠4♣, 4♥4♦, 4♦4♣, or 4♣4♥. Also, there are 4 (4x1) ways to get dealt any suited hand because there " \
                       "are 4 different suites; i.e. A4s as A♠4♠, A♥4♥, A♦4♦, or A♣4♣. Finally, there are 12 (4x3) ways to get dealt any unsuited hand; " \
                       "i.e. AKo as A♠K♣, A♠K♦, A♠K♥, A♥K♣, A♥K♦, A♥K♠, A♦K♣, A♦K♥, A♦K♠, A♣K♦, A♣K♥, A♣K♠.\n\n" \
                        "The settings below allow you to setup your own unique games for whatever situation you may run into.\n\n" \
                        "You can use the predefined ranges in the hand_ranges folder or create your own. If you create your own there should be one hand type per line in the imported text file. The higher ranked card " \
                       "needs to be first for suited and unsuited hands.\n\n" \
                        "The maximum number of players is 10 because this is the max in live play and at higher stakes 6 players is often the most. The minimum number of players is 3 because blind play is more " \
                       "complex and will always have additional considerations because of the different pot odd calculations.\n\n" \
                        "You can review the results of your sessions in the exported reports folder. For all operating systems, if you want the raw data select text files. Otherwise, comma separated value files are " \
                       "often opened in spreadsheet applications that are good at analyzing data.\n\n" \
                        "Showing immediate feedback is beneficial if you want to confirm what the correct decision was, and a brief reason why, while you are playing at the table.\n\n" \
                       "Once everything is setup the way you want click on 'Start Playing'. You can always come back and change these as often as you want. Good luck and have fun!"

        self.instructions_text = Text(self, width=160, height=25, wrap=WORD)
        self.instructions_text.grid(row=1, column=0, columnspan=3, pady=20)
        self.instructions_text.delete(0.0, END)
        self.instructions_text.insert(0.0, instructions)
        self.instructions_text.config(state=DISABLED)

        Label(self, text="How many players do you want to play against? (3-10): ", font="bold").grid(row=2, column=0, pady=10, sticky=W)

        self.num_players = IntVar()
        Scale(self, variable=self.num_players, from_=3, to=10, resolution=1, orient=HORIZONTAL).grid(row=2, column=0, columnspan=3)
        self.num_players.set(6)

        Label(self, text="Select your range: ", font="bold").grid(row=3, column=0, pady=10, sticky=W)

        self.range = StringVar()
        self.range.set(None)
        range_options = []
        for file in os.listdir("..\\hand_ranges"):  # Getting all the text files in the hand_ranges folder.
            if file.endswith(".txt"):
                range_options.append(os.path.join(file))
        range_options += ["does_not_exist.txt"]  # Adding a non existent file to demonstrate how to handle a file not found exception later.
        ranges = range_options
        OptionMenu(self, self.range, *ranges).grid(row=3, column=0, columnspan=3)
        self.range.set("Unimproved Range.txt")

        Label(self, text="Feedback report output format: ", font="bold").grid(row=4, column=0, pady=10, sticky=W)

        self.service = StringVar()
        self.service.set(None)
        Radiobutton(self, text="Comma Separated Value (.csv)", value="csv", variable=self.service).grid(row=4, column=0, columnspan=3)
        Radiobutton(self, text="Text (.txt)", value="txt", variable=self.service).grid(row=4, column=1, sticky=E)
        self.service.set("csv")

        self.is_feedback = BooleanVar()

        Checkbutton(self, text="Display decision feedback at the table?", font="bold", variable=self.is_feedback).grid(row=5, column=0, sticky=W, pady=10)
        self.is_feedback.set(1)

        image_file_path = DirNav().get_path("tables")
        self.image = PhotoImage(file=image_file_path + "table_icon.png")
        Button(self, command=self.shutdown, text=" Start Playing", font=("Arial", 18), image=self.image, compound="left", width=250, height=60).grid(row=6, column=0, columnspan=3, pady=10)

    def setup_game(self):
        session_range = self.range.get()
        app.range.Range(session_range).file_layout()
        session_players = self.num_players.get()
        output_format = self.service.get()
        show_feedback = self.is_feedback.get()
        feedback_file = app.feedback_file.FeedbackFile(session_players, output_format)
        feedback_file.create_feedback_file()
        play_hand = session_players, session_range, feedback_file, show_feedback
        print(play_hand)  # Only printing out for now to help with testing
        return play_hand

    def shutdown(self):
        self.setup_game()
        app_setup.destroy()


app_setup = Tk()
app_setup.title("No Limit Texas Hold'em Pre-flop Range Trainer")
app_setup.geometry("1366x768+100+100")
game_setup = GameSetup(app_setup).grid()

app_setup.mainloop()
