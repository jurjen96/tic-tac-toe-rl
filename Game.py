from EGreedy import EGreedy

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
        self.action = EGreedy(self)

    def get_game(self):
        """
        Getter for getting the game status

        @return a list representing the current status of the game. 1 corresponds
                to 'X', 0 to an empty cell and -1 to 'O'
        """
        return self.game

    def set_cell(self, pos, mark):
        """
        Mark a cell

        @param pos: list with the coordinate of the marked cell
        @param mark: the mark that will be placed inside the cell
        """
        mark_int = 1 if mark == 'X' else -1
        index = pos[0]*3 + pos[1]
        self.game[index] = mark_int

    def play(self, player_x, player_o):
        """
        Play a single game of tic-tac-toe until a player either has won or the
        game has ended in a tie.

        @param player_x: an Agent object referencing to the player using mark X
        @param player_o: an Agent object referencing to the player using mark O
        """
        game_finished = False
        while not game_finished:

            player_x.do_action()
            if self.has_won(player_x.get_mark()) or self.tie():
                game_finished = True
                break

            player_o.do_action()
            if self.has_won(player_o.get_mark()):
                game_finished = True
                break

        print "Done playing"

    def tie(self):
        """
        Check if there are still valid actions to take and if there are no longer
        valid actions to take, the game ended in a tie(draw)

        @return a boolean that is True when the game is ended in a draw
        """
        valid_actions = self.action.get_valid_actions()
        if sum(valid_actions) == 0:
            return True
        return False


    def has_won(self, mark):
        """
        Check if a player has won the game, by fullfilling the winning condition
        of the game.

        @param mark: a string representing the mark of player, should be 'X' or 'O'
        @return  if the player has won: return True, else: False
        """
        mark = 1 if mark == 'X' else -1

        marked_cells = [1 if cell == mark else 0 for cell in self.game]

        marked = []
        for i in range(3):
            marked.append(marked_cells[i*3:i*3+3])

        # Horizontal cells:
        for i in range(3):
            sum_cells = 0
            for j in range(3):
                sum_cells += self.magic_square[i][j] * marked[i][j]
            if sum_cells == 15:
                return True

        # Vertical cells:
        for i in range(3):
            sum_cells = 0
            for j in range(3):
                sum_cells += self.magic_square[j][i] * marked[j][i]
            if sum_cells == 15:
                return True

        # Diagnol cells: from left up to right down
        sum_cells = 0
        for i in range(3):
            sum_cells += self.magic_square[i][i] * marked[i][i]
        if sum_cells == 15:
            return True

        # Diagnol cells: from right up to left down
        sum_cells = 0
        for i in range(3):
            sum_cells += self.magic_square[i][-i+2] * marked[i][-i+2]
        if sum_cells == 15:
            return True

        return False
