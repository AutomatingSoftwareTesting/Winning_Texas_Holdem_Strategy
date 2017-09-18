from game_setup import GameSetup, Tk


def main():
    start_game = Tk()
    start_game.title("No Limit Texas Hold'em Pre-flop Range Trainer")
    start_game.geometry("1366x768+100+100")
    start_game.grid_columnconfigure(0, weight=1)
    GameSetup(start_game).grid()

    start_game.mainloop()

main()
