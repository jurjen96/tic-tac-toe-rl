class Agent(object):
    def __init__(self, mark, board, game):
        self.mark = mark
        self.board = board
        self.game = game


    def do_action(self, pos):
        self.game.set_cell(pos, self.mark)
        self.board.update(pos, self.mark)

    def reset(self):
        pass

    def get_mark(self):
        return self.mark
