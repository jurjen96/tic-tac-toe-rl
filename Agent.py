from Action import Action
from QLearning import QLearning

class Agent(object):
    def __init__(self, mark, board, game, player_type):
        self.mark = mark
        self.board = board
        self.game = game
        self.player_type = player_type
        self.action = Action(self.game)
        self.q_learning = QLearning()
        self.ordered_actions = []

    def reset(self):
        """Resets the list of actions taken"""
        self.ordered_actions = []

    def store_action(self, action, state, game):
        """
        Store the action taken in an ordered list of actions taken during the game
        """
        self.ordered_actions.append({"action":action, "state":state, "game":list(game)})

    def select_action(self, epsilon=0.0, state=None):
        """
        Select the action based on the players types

        @param epsilon: the E-greedy action value. Determines if a random actions
                        (exploration) should be chosen over learned Q-values
                        (exploitation).
        @param state: the current state of the game, used to determine the available
                      actions

        @return the index of where the marker will be placed (the action)
        """
        if self.player_type == "human":
            action = self.get_input()
        elif self.player_type == "random":
            action = self.action.get_random_action()
        elif self.player_type == "qlearning":
            action = self.action.get_egreedy_action(epsilon, self.q_learning, state)
        else:
            print "Undefined player type"
            raise NotImplementedError
        return action

    def learn_from_game(self, alpha, reward, gamma):
        if not self.player_type == "qlearning": # the other type of agents do not learn
            return

        for index, action in enumerate(self.ordered_actions):
            if index + 1 < len(self.ordered_actions):
                next_state = self.ordered_actions[index + 1]["state"]
            else:
                next_state = None

            state = action["state"]
            selected_action = action["action"]
            game = action["game"]

            # Only the last state receives a reward
            if index == len(self.ordered_actions) - 1:
                state_reward = reward
            else:
                state_reward = 0

            possible_actions = self.action.get_valid_actions(game)
            self.q_learning.update_q(state, selected_action, next_state, possible_actions,
                                     alpha, state_reward, gamma)

    def do_action(self, action):
        """
        Perform an action based on the player type. An actions is defined as
        placing a mark in one of the empty cells. Currently the game will support
        three types of players:
        - human: us
        - random: a bot that just places marks randomly in cells
        - qlearning: a smarter bot (hopefully) that learns what the best options are
        """
        pos = [action//3, action%3]
        self.game.set_cell(pos, self.mark)
        self.board.update(pos, self.mark)

    def get_input(self):
        """
        Get input from user via keyboard. Input refers to the index of one of the
        fields

        @return a position in the board where the user wants there mark to be placed
        """
        self.board.print_game()

        while True:
            user_input = input("Your turn " + str(self.get_mark()) + " (0-8): ")
            valid_actions = self.action.get_valid_actions()
            if user_input >= 0 and user_input < 9 and valid_actions[user_input] == 1:
                break
            print "Invallid turn, please try another cell"

        return user_input

    def get_type(self):
        """
        Return the type of user: human, random, qlearning
        """
        return self.player_type

    def get_mark(self):
        """
        Get the mark the agent is using

        @return a string representing the mark. E.q. 'X' or 'O'
        """
        return self.mark
