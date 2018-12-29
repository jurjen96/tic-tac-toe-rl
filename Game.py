from Action import Action

class Game(object):
    def __init__(self):
        # Magic square is used to calculate if there is a winning combination
        # the sum of all winning combination is always 15
        self.magic_square = [[8, 1, 6],
                             [3, 5, 7],
                             [4, 9, 2]]
        # More info about magic square can be found here:
        # http://mathworld.wolfram.com/MagicSquare.html
        self.game = [0] * 9
        self.tie = False
        self.mark_that_won = ""
        self.action = Action(self)

        # Parameters:
        self.alpha = 0.7         # learning rate
        self.gamma = 0.9         # discount reward
        self.epsilon = 0.1       # for greedy selection

    def play_and_learn(self, players):
        """
        Play a single game of tic-tac-toe with the players and let the players,
        that use q-learning, learn from the game.
        """
        # Play a single game
        game_finished = False
        while not game_finished:
            for player in players:
                state = self.get_state()
                selected_action = player.select_action(self.epsilon, state)

                if selected_action == "q": # keep playing the game, until q is pressed
                    return "quit"

                player.store_action(selected_action, state, self.get_game())

                player.do_action(selected_action)

                if self.has_won(player.get_mark()) or self.is_tie():
                    game_finished = True
                    break

        # Learn from the game
        for player in players:
            reward = self.get_reward(player.get_mark())
            player.learn_from_game(self.alpha, reward, self.gamma)
            player.reset()

        return "success"

    def get_game(self):
        """
        Getter for getting the game status

        @return a list representing the current status of the game. 1 corresponds
                to 'X', 0 to an empty cell and -1 to 'O'
        """
        return self.game

    def reset(self):
        """
        Reset the game by setting some class variables back to default values.
        """
        self.tie = False
        self.mark_that_won = ""
        self.game = [0] * 9

    def set_cell(self, pos, mark):
        """
        Mark a cell

        @param pos: list with the coordinate of the marked cell
        @param mark: the mark that will be placed inside the cell
        """
        mark_int = 1 if mark == 'X' else -1
        index = pos[0]*3 + pos[1]
        self.game[index] = mark_int

    def is_tie(self):
        """
        Check if there are still valid actions to take and if there are no longer
        valid actions to take, the game ended in a tie (draw)

        @return a boolean that is True when the game is ended in a draw
        """
        valid_actions = self.action.get_valid_actions()
        if sum(valid_actions) == 0:
            self.tie = True
            return True
        return False

    def has_won(self, mark_str):
        """
        Check if a player has won the game, by fullfilling the winning condition
        of the game.

        @param mark: a string representing the mark of player, should be 'X' or 'O'
        @return  if the player has won: return True, else: False
        """
        mark = 1 if mark_str == 'X' else -1

        # Filter out only the cells that correspond with the players mark
        marked_cells = [1 if cell == mark else 0 for cell in self.game]

        # Convert the single []*9 list to a multi-dimensional list 3 x 3
        marked = []
        for i in range(3):
            marked.append(marked_cells[i*3:i*3+3])

        # Horizontal and vertical cells:
        for i in range(3):
            sum_cells_hor = 0 # The sum over a horizontal row of cells
            sum_cells_ver = 0 # The sum over a verical column of cells
            for j in range(3):
                sum_cells_hor += self.magic_square[i][j] * marked[i][j]
                sum_cells_ver += self.magic_square[j][i] * marked[j][i]

            if sum_cells_hor == 15 or sum_cells_ver == 15:
                self.mark_that_won = mark_str
                return True

        # Diagnol cells: from left up to right down
        sum_cells = 0
        for i in range(3):
            sum_cells += self.magic_square[i][i] * marked[i][i]
        if sum_cells == 15:
            self.mark_that_won = mark_str
            return True

        # Diagnol cells: from right up to left down
        sum_cells = 0
        for i in range(3):
            sum_cells += self.magic_square[i][-i+2] * marked[i][-i+2]
        if sum_cells == 15:
            self.mark_that_won = mark_str
            return True

        return False

    def get_reward(self, mark):
        """
        Get the reward for the played game

        reward: +1 the player with the mark won the game
                 0 the game is still goin on (no winners and no losers)
                -0.5 the gamed ended up in a tie
                -1 the player with the mark lost the game
        """
        if self.tie:
            return -0.5

        if self.mark_that_won == "":
            return 0
        elif mark == self.mark_that_won:
            return 1
        return -1

    def get_state(self):
        return ''.join(str(i) for i in self.game)
