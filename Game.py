class Game(object):
    def __init__(self):
        self.magic_square = [[8,1,6],
                             [3,5,7],
                             [4,9,2]]
        #http://mathworld.wolfram.com/MagicSquare.html
        self.game = [0] * 9

    def get_game(self):
        return self.game

    def set_cell(self, pos, mark):
        mark_int = 1 if mark == 'X' else -1
        index = pos[0]*3 + pos[1]
        self.game[index] = mark_int


    def has_won(self, mark):
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

        # Diagnol cells: /
        sum_cells = 0
        for i in range(3):
            sum_cells += self.magic_square[i][i] * marked[i][i]
        if sum_cells == 15:
            return True

        # Diagnol cells: \
        sum_cells = 0
        for i in range(3):
            sum_cells += self.magic_square[i][-i+2] * marked[i][-i+2]
        if sum_cells == 15:
            return True

        return False
