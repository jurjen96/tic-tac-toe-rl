from EGreedy import EGreedy

class Agent(object):
    def __init__(self, mark, board, game, player_type):
        self.mark = mark
        self.board = board
        self.game = game
        self.player_type = player_type
        self.action = EGreedy(self.game)

    def select_action(self, epsilon=0.0, q_learning=None, state=None):
        if self.player_type == "human":
            action = self.get_input()
        elif self.player_type == "random":
            action = self.action.get_random_action()
        elif self.player_type == "qlearning":
            action = self.action.get_egreedy_action(epsilon, q_learning, state)
        else:
            print "Undefined player type"
            raise NotImplementedError
        return action

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
            if valid_actions[user_input] == 1:
                break
            print "Invallid turn, please try another cell"

        return [user_input//3, user_input%3]

    def get_type(self):
        return self.player_type

    def get_mark(self):
        """
        Get the mark the agent is using

        @return a string representing the mark. E.q. 'X' or 'O'
        """
        return self.mark
