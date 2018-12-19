import matplotlib.pyplot as plt

from Board import Board
from Agent import Agent
from Game import Game

def train(board, game, player_x, player_o):
    # Parameters:
    decay_rate = 0.01   # decay rate for decreasing the epsilon value per trail
    max_epsilon = 1.0   # max value of epsilon
    min_epsilon = 0.01  # min value of epsilon
    epsilon = 0.1       # for greedy selection
    alpha = 0.7         # learning rate
    gamma = 0.9         # discount reward

    max_games = 50 #40
    max_runs = 800 #100


    # action = EGreedy(game)
    players = [player_x, player_o]
    player_x_won = 0
    player_o_won = 0
    draw = 0
    fraction_x = []
    fraction_o = []
    fraction_draw = []

    for _ in range(max_runs): # train
        for _ in range(max_games):

            game_finished = False
            print "---"*20
            print "New epoch"
            while not game_finished:
                for player in players:
                    state = game.get_state()
                    selected_action = player.select_action(epsilon, state)

                    player.store_action(selected_action, state, game.get_game())

                    player.do_action(selected_action)
                    new_state = game.get_state()


                    if game.has_won(player.get_mark()) or game.is_tie():
                        game_finished = True
                        break

            if game.has_won(player_x.get_mark()):
                player_x_won += 1
            elif game.has_won(player_o.get_mark()):
                player_o_won += 1
            else:
                draw += 1

            print "Learning from game"
            reward = game.get_reward(player_x.get_mark())
            player_x.learn_from_game(new_state, alpha, reward, gamma)
            player_x.reset()

            board.print_game()

            game.reset()
            board.reset()

        fraction_o.append(player_o_won / float(max_games))
        fraction_x.append(player_x_won / float(max_games))
        fraction_draw.append(draw / float(max_games))
        print "Player x won: " + str(player_x_won)
        print "Player o won: " + str(player_o_won)
        print "It was a draw: " + str(draw)
        player_o_won = 0
        player_x_won = 0
        draw = 0

    print fraction_o
    print fraction_x
    print fraction_draw

    plt.figure(0)
    plt.plot(fraction_o)
    plt.plot(fraction_x)
    plt.plot(fraction_draw)
    plt.ylabel("fraction")
    plt.show()

def main():
    board = Board()
    game = Game()
    player_x = Agent("X", board, game, "qlearning")
    player_o = Agent("O", board, game, "random")
    train(board, game, player_x, player_o)

if __name__ == "__main__":
    print "Starting the tic-tac-toe game"
    main()
