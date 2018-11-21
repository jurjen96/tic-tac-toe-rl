from EGreedy import EGreedy
from State import State

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
        self.action = EGreedy(self)

    def get_game(self):
        """
        Getter for getting the game status

        @return a list representing the current status of the game. 1 corresponds
                to 'X', 0 to an empty cell and -1 to 'O'
        """
        return self.game

    def reset(self):
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
        valid actions to take, the game ended in a tie(draw)

        @return a boolean that is True when the game is ended in a draw
        """
        valid_actions = self.action.get_valid_actions()
        if sum(valid_actions) == 0:
            self.tie = True
            return True
        return False


    def has_won(self, markStr):
        """
        Check if a player has won the game, by fullfilling the winning condition
        of the game.

        @param mark: a string representing the mark of player, should be 'X' or 'O'
        @return  if the player has won: return True, else: False
        """
        mark = 1 if markStr == 'X' else -1

        marked_cells = [1 if cell == mark else 0 for cell in self.game]

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
                self.mark_that_won = markStr
                return True

        # Diagnol cells: from left up to right down
        sum_cells = 0
        for i in range(3):
            sum_cells += self.magic_square[i][i] * marked[i][i]
        if sum_cells == 15:
            self.mark_that_won = markStr
            return True

        # Diagnol cells: from right up to left down
        sum_cells = 0
        for i in range(3):
            sum_cells += self.magic_square[i][-i+2] * marked[i][-i+2]
        if sum_cells == 15:
            self.mark_that_won = markStr
            return True

        return False

    def get_reward(self, mark):
        if self.tie:
            return -0.5

        if self.mark_that_won == "":
            return 0
        elif mark == self.mark_that_won:
            return 1
        return -1

    def get_state(self):
        return State(self.game)
