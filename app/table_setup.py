import pyglet
import sys, os
from game_setup import GameSetup, app_setup


class PlayGame(object):
    def __init__(self, score=0, hand_num=1):
        self.score = score
        self.hand_num = hand_num

    def get_score(self):
        return int(self.score)

    def get_hand_num(self):
        return int(self.hand_num)

start_game = GameSetup(app_setup)
num_players, range, file_extension, show_feedback = start_game.setup_game()


window = pyglet.window.Window(width=1050, height=700, caption="No Limit Texas Hold'em Preflop Range Trainer: Test Range")

current_dir = sys.path[0]
img_path = os.path.join(current_dir, "../images/tables/" + str(num_players) + "_Handed.png")

table_image = pyglet.image.load(img_path)

@window.event()
def on_draw():
    window.clear()
    table_image.blit(10, 50)

    hand_label = pyglet.text.Label("Hand: " + str(1), # Will change to var later
                              font_name="Arial",
                              font_size=18,
                              x=20, y=50)

    score_label = pyglet.text.Label("Score: " + str(0), # Will change to var later
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

    if show_feedback:
        feedback_label.draw()

pyglet.app.run()
