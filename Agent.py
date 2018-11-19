from EGreedy import EGreedy

class Agent(object):
    def __init__(self, mark, board, game, player_type):
        self.mark = mark
        self.board = board
        self.game = game
        self.player_type = player_type
        self.action = EGreedy(self.game)


    def do_action(self):
        """
        Perform an action based on the player type. An actions is defined as
        placing a mark in one of the empty cells. Currently the game will support
        three types of players:
        - human: us
        - random: a bot that just places marks randomly in cells
        - qlearning: a smarter bot (hopefully) that learns what the best options are
        """

        if self.player_type == "human":
            pos = self.get_input()
        elif self.player_type == "random":
            pos = self.action.get_random_action()
        elif self.player_type == "qlearning":
            raise NotImplementedError
        else:
            print "Undefined player type"
            raise NotImplementedError

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

    def reset(self):
        pass

    def get_mark(self):
        """
        Get the mark the agent is using

        @return a string representing the mark. E.q. 'X' or 'O'
        """
        return self.mark
