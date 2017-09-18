import pyglet
import sys
import os
from game_setup import GameSetup, app_setup


class TableSetup(object):
    def __init__(self, num_players=None, hand_range=None, file_extension=None, show_feedback=None, score=0, hand_num=1):
        self.score = score
        self.hand_num = hand_num
        self.num_players = num_players
        self.hand_range = hand_range
        self.file_extension = file_extension
        self.show_feedback = show_feedback

    def get_score(self):
        return int(self.score)

    def get_hand_num(self):
        return int(self.hand_num)

    def get_num_players(self):
        return int(self.num_players)

    def get_hand_range(self):
        return self.hand_range

    def get_file_extension(self):
        return self.file_extension

    def get_show_feedback(self):
        return self.show_feedback

    def create_table(self):
        window = pyglet.window.Window(width=1050, height=700, caption="No Limit Texas Hold'em Preflop Range Trainer: Test Range")
        # The size of the screens for the game setup and table setups are different; however, they are specific sizes for the information they display. In a future project, will work with dynamically sized screens.

        current_dir = sys.path[0]
        img_path = os.path.join(current_dir, "../images/tables/" + str(self.num_players) + "_Handed.png")

        table_image = pyglet.image.load(img_path)

        @window.event()
        def on_draw():
            window.clear()
            table_image.blit(10, 50)

            hand_label = pyglet.text.Label("Hand: " + str(self.hand_num),  # Will change to var later
                                           font_name="Arial",
                                           font_size=18,
                                           x=20, y=50)

            score_label = pyglet.text.Label("Score: " + str(self.score),  # Will change to var later
                                            font_name="Arial",
                                            font_size=18,
                                            x=20, y=20)

            open_label = pyglet.text.Label("Open",
                                           font_name="Arial",
                                           font_size=18,
                                           x=450, y=20)

            fold_label = pyglet.text.Label("Fold",
                                           font_name="Arial",
                                           font_size=18,
                                           x=550, y=20)

            feedback_label = pyglet.text.Label("Feedback",
                                               font_name="Arial",
                                               font_size=18,
                                               x=450, y=665)

            hand_label.draw()
            score_label.draw()
            open_label.draw()
            fold_label.draw()

            if self.show_feedback:
                feedback_label.draw()

        pyglet.app.run()


# start_game = GameSetup(app_setup)
# num_players, range, file_extension, show_feedback = start_game.setup_game()
TableSetup(GameSetup(app_setup).setup_game()).create_table()
