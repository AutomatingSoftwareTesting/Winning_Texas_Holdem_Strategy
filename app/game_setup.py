from tkinter import *
from instructions import game_setup_instructions
from app.dir_nav import DirNav
import app.feedback_file
import app.range
import os


class GameSetup(Frame):
    def __init__(self, master, instruction_text=NONE, num_players=NONE, hand_range=NONE, file_extension=NONE, is_feedback=NONE, button_image=NONE):
        super(GameSetup, self).__init__(master)
        self.instructions_text = instruction_text
        self.num_players = num_players
        self.hand_range = hand_range
        self.file_extension = file_extension
        self.is_feedback = is_feedback
        self.button_image = button_image
        self.create_widgets()
        app_setup.grid_columnconfigure(0, weight=1)

    def get_instructions_text(self):
        return self.instructions_text

    def get_num_players(self):
        return int(self.num_players)

    def get_hand_range(self):
        return self.hand_range

    def get_file_extension(self):
        return self.file_extension

    def get_is_feedback(self):
        return self.is_feedback

    def get_button_image(self):
        return self.button_image

    def create_widgets(self):
        Label(self, text="Welcome to the No Limit Texas Hold'em Pre-flop Range Trainer Setup Lobby", font=("Arial", 18)).grid(row=0, column=0, columnspan=3, pady=(20, 0))

        self.instructions_text = Text(self, width=160, height=25, wrap=WORD)
        self.instructions_text.grid(row=1, column=0, columnspan=3, pady=20)
        self.instructions_text.delete(0.0, END)
        self.instructions_text.insert(0.0, game_setup_instructions())
        self.instructions_text.config(state=DISABLED)

        Label(self, text="How many players do you want to play against? (3-10): ", font="bold").grid(row=2, column=0, pady=10, sticky=W)

        self.num_players = IntVar()
        Scale(self, variable=self.num_players, from_=3, to=10, resolution=1, orient=HORIZONTAL).grid(row=2, column=0, columnspan=3)
        self.num_players.set(6)

        Label(self, text="Select your range: ", font="bold").grid(row=3, column=0, pady=10, sticky=W)

        self.hand_range = StringVar()
        self.hand_range.set(None)
        range_options = []
        for file in os.listdir("..\\hand_ranges"):  # Getting all the text files in the hand_ranges folder.
            if file.endswith(".txt"):
                range_options.append(os.path.join(file))
        range_options += ["does_not_exist.txt"]  # Adding a non existent file to demonstrate how to handle a file not found exception later.
        ranges = range_options
        OptionMenu(self, self.hand_range, *ranges).grid(row=3, column=0, columnspan=3)
        self.hand_range.set("Unimproved Range.txt")

        Label(self, text="Feedback report output format: ", font="bold").grid(row=4, column=0, pady=10, sticky=W)

        self.file_extension = StringVar()
        self.file_extension.set(None)
        Radiobutton(self, text="Comma Separated Value (.csv)", value="csv", variable=self.file_extension).grid(row=4, column=0, columnspan=3)
        Radiobutton(self, text="Text (.txt)", value="txt", variable=self.file_extension).grid(row=4, column=1, sticky=E)
        self.file_extension.set("csv")

        self.is_feedback = BooleanVar()

        Checkbutton(self, text="Display decision feedback at the table?", font="bold", variable=self.is_feedback).grid(row=5, column=0, sticky=W, pady=10)
        self.is_feedback.set(1)

        image_file_path = DirNav().get_path("tables")
        self.button_image = PhotoImage(file=image_file_path + "table_icon.png")
        Button(self, command=self.shutdown, text=" Start Playing", font=("Arial", 18), image=self.button_image, compound="left", width=250, height=60).grid(row=6, column=0, columnspan=3, pady=10)

    def setup_game(self):
        session_range = self.hand_range.get()
        app.range.Range(session_range).file_layout()
        session_players = self.num_players.get()
        output_format = self.file_extension.get()
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
