import pyglet
import sys
import os
from deck import Deck
from hand import Hand
from position import Position
from range import Range


class TableSetup(object):
    # This is a demo (hack) of how the screens can work together and what type of information should be displayed. I've run out of time for this project because my coding bootcamp begins soon.
    # Plan on taking several lessons learned here and translating this into java (or maybe javascript). Want to be able to distribute it, and any following updates, much easier.
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
        print(card1)  # Leaving print statements to show the gui display is correct.
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

        r = Range(self.hand_range)
        correct_decision, hand_percent, total_cards = r.correct_decision(hand_type, position_min)

        min_open_hand = r.min_open_card(position_min)

        def feedback_demo():
            return "You should " + str(correct_decision) + " because you want to play the top {0:.2f}".format(position_min * 100) + "% of your range; which ends at " + str(min_open_hand) + "."

        def feedback_demo_ln2():
            return str(hand) + "is in the top {0:.2f}".format(hand_percent * 100) + "% of starting hands for the " + str(self.hand_range) + " range."

        position = str(position)

        @window.event()
        def on_draw():
            window.clear()
            table_image.blit(10, 50)

            if position == "Button":
                card1_image.blit(630, 60)
                card2_image.blit(690, 60)
            elif position == "Cut Off":
                card1_image.blit(770, 160)
                card2_image.blit(850, 160)
            elif position == "High Jack":
                card1_image.blit(770, 310)
                card2_image.blit(850, 310)
            elif position == "Low Jack":
                card1_image.blit(630, 390)
                card2_image.blit(690, 390)
            elif position == "5 Off Button":
                card1_image.blit(390, 390)
                card2_image.blit(450, 390)
            elif position == "6 Off Button":
                card1_image.blit(210, 390)
                card2_image.blit(270, 390)
            elif position == "7 Off Button":
                card1_image.blit(70, 310)
                card2_image.blit(130, 310)
            elif position == "8 Off Button":
                card1_image.blit(70, 160)
                card2_image.blit(130, 160)
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

            open_label = pyglet.text.Label("What is your decision?  '4' = Open",
                                           font_name="Arial",
                                           font_size=18,
                                           x=250, y=20)

            fold_label = pyglet.text.Label("'6' = Fold",
                                           font_name="Arial",
                                           font_size=18,
                                           x=650, y=20)

            feedback_label = pyglet.text.Label(str(feedback_demo()),
                                               font_name="Arial",
                                               font_size=14,
                                               x=100, y=665)

            feedback_label_ln2 = pyglet.text.Label(str(feedback_demo_ln2()),
                                                   font_name="Arial",
                                                   font_size=14,
                                                   x=150, y=645)

            hand_label.draw()
            score_label.draw()
            open_label.draw()
            fold_label.draw()

            if self.show_feedback:
                feedback_label.draw()
                feedback_label_ln2.draw()

        pyglet.app.run()
