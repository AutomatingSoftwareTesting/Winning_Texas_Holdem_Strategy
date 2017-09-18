import pyglet
import sys
import os
from deck import Deck
from hand import Hand
from position import Position


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
        window = pyglet.window.Window(width=1050, height=700, caption="No Limit Texas Hold'em Preflop Range Trainer: " + self.hand_range)
        # The size of the screens for the game setup and table setups are different; however, they are specific sizes (fixed) for the information they display.
        # Will work with dynamically sized screens in a future project.

        current_dir = sys.path[0]
        img_path = os.path.join(current_dir, "../images/tables/" + str(self.num_players) + "_Handed.png")

        table_image = pyglet.image.load(img_path)

        deck = Deck()
        deck.create()
        deck.shuffle()

        hand = Hand()
        hand.get_hand(deck)
        print(hand)

        card1 = hand.hole_cards[0]
        card2 = hand.hole_cards[1]
        print(card1)
        print(card2)

        img_card1 = os.path.join(current_dir, "../images/cards/" + str(card1) + ".png")
        card1_image = pyglet.image.load(img_card1)
        img_card2 = os.path.join(current_dir, "../images/cards/" + str(card2) + ".png")
        card2_image = pyglet.image.load(img_card2)

        hand.order_hand()
        hand_type = hand.hand_type()

        position = Position()
        position.current_position(self.num_players)
        print(position)

        position_min = position.min_open()

        position = str(position)

        @window.event()
        def on_draw():
            window.clear()
            table_image.blit(60, 60)

            if position == "Button":
                card1_image.blit(680, 70)
                card2_image.blit(740, 70)
            elif position == "Cut Off":
                card1_image.blit(820, 170)
                card2_image.blit(880, 170)
            elif position == "High Jack":
                card1_image.blit(820, 320)
                card2_image.blit(880, 320)
            elif position == "Low Jack":
                card1_image.blit(680, 400)
                card2_image.blit(740, 400)
            elif position == "5 Off Button":
                card1_image.blit(440, 400)
                card2_image.blit(500, 400)
            elif position == "6 Off Button":
                card1_image.blit(260, 400)
                card2_image.blit(320, 400)
            elif position == "7 Off Button":
                card1_image.blit(120, 320)
                card2_image.blit(150, 320)
            elif position == "8 Off Button":
                card1_image.blit(120, 170)
                card2_image.blit(150, 170)
            else:
                print("Sorry, don't know which position you are sitting at.")


            hand_label = pyglet.text.Label("Hand: " + str(self.hand_num),
                                           font_name="Arial",
                                           font_size=18,
                                           x=20, y=50)

            score_label = pyglet.text.Label("Score: " + str(self.score),
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
