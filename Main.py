import time
import matplotlib.pyplot as plt

from Board import Board
from Agent import Agent
from Game import Game


def train(board, game, player_x, player_o):
    """
    Train the players/agents that are using qlearning to learn how to play
    the game. In the current implementation we make use of a number of games
    per run and use the fraction of how many times a player has won as
    indication how well the players is doing. For example if the player wins
    half of the games in the first run (e.q. fraction of 0.5) and wins 90% of
    the time in the last runs (e.q. fraction of 0.9), we can conclude that the
    player is performing better over the number of games it played.
    """
    max_games = 100
    max_runs = 400

    players = [player_x, player_o]
    # The next few variables are used to store the progress for every run and
    # game.
    player_x_won = 0
    player_o_won = 0
    draw = 0
    fraction_x = []
    fraction_o = []
    fraction_draw = []

    for _ in range(max_runs): # train
        for _ in range(max_games):
            print "\nNew game"
            game.play_and_learn(players) # play a single game and learn from it

            if game.has_won(player_x.get_mark()):
                player_x_won += 1
            elif game.has_won(player_o.get_mark()):
                player_o_won += 1
            else:
                draw += 1

            board.print_game()

            game.reset()
            board.reset()

        fraction_o.append(player_o_won / float(max_games))
        fraction_x.append(player_x_won / float(max_games))
        fraction_draw.append(draw / float(max_games))

        player_o_won = 0
        player_x_won = 0
        draw = 0

    # Uncomment the following lines to see in graph format how the players
    # performed
    # plt.figure(0)
    # plt.title("Random Player (X) vs Q-learning (O)")
    # plt.plot(fraction_o)
    # plt.plot(fraction_x)
    # plt.plot(fraction_draw)
    # labels = ["Player O won", "Player X won", "Draw"]
    # plt.legend(labels)
    # plt.ylabel("Fraction")
    # plt.ylabel("Nr. runs")
    # plt.show()

def play(game, board, player_x, player_o):
    """ Play a single game against the bot"""
    players = [player_x, player_o]
    status = game.play_and_learn(players)

    board.print_game()

    game.reset()
    board.reset()

    return status

def main():
    board = Board()
    game = Game()
    player_x = Agent("X", board, game, "qlearning")
    player_o = Agent("O", board, game, "random")

    print "---" * 20
    print "|                   Training the bot                       |"
    print "---" * 20
    time.sleep(3)

    train(board, game, player_x, player_o)

    print "\n\n\n"
    print "---" * 20
    print "|               Playing against the bot                    |"
    print "---" * 20

    player_o = Agent("O", board, game, "human")
    status = "success"
    while status != "quit":
        status = play(game, board, player_x, player_o)

if __name__ == "__main__":
    print "Starting the tic-tac-toe game"
    main()
