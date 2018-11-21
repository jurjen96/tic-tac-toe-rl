from Board import Board
from Agent import Agent
from Game import Game
from EGreedy import EGreedy
from QLearning import QLearning
from State import State


def main():

    # Parameters:
    decay_rate = 0.01   # decay rate for decreasing the epsilon value per trail
    max_epsilon = 1.0   # max value of epsilon
    min_epsilon = 0.01  # min value of epsilon
    epsilon = 0.1       # for greedy selection
    alpha = 0.7         # learning rate
    gamma = 0.9         # discount reward

    max_runs = 10000

    board = Board()
    game = Game()
    q_learning = QLearning()
    action = EGreedy(game)
    player_x = Agent("X", board, game, "qlearning")
    player_o = Agent("O", board, game, "random")
    players = [player_x, player_o]
    player_x_won = 0
    player_o_won = 0
    draw = 0

    for run in range(max_runs):

        game_finished = False
        while not game_finished:
            for player in players:
                if player.get_type() == "qlearning":
                    state = game.get_state()
                    selected_action = player.select_action(epsilon, q_learning, state)
                    player.do_action(selected_action)
                    new_state = game.get_state()
                    #get the next possible actions
                    possible_actions = action.get_valid_actions()

                    if game.has_won(player.get_mark()) or game.is_tie():
                        # print player.get_mark()
                        pass

                    reward = game.get_reward(player.get_mark())
                    # print "REWARD " + str(reward)
                    q_learning.update_q(state, selected_action, new_state, q_learning, possible_actions, alpha, reward, gamma)

                    if reward:
                        game_finished = True
                        break
                else:
                    selected_action = player.select_action()
                    player.do_action(selected_action)

                    if game.has_won(player.get_mark()) or game.is_tie():
                        break


        if game.has_won(player_x.get_mark()):
            player_x_won += 1
        elif game.has_won(player_o.get_mark()):
            player_o_won += 1
        else:
            draw += 1
        # print game.get_reward(player_x.get_mark())
        # print game.get_reward(player_o.get_mark())
        #
        # board.print_game()
        # print "X has won: " + str(game.has_won(player_x.get_mark()))
        # print "O has won: " + str(game.has_won(player_o.get_mark()))

        game.reset()
        board.reset()

    print len(q_learning.q)
    print "Player x won: " + str(player_x_won)
    print "Player o won: " + str(player_o_won)
    print "It was a draw: " + str(draw)

if __name__ == "__main__":
    print "Starting the tic-tac-toe game"
    main()
