import random

class EGreedy(object):

    def __init__(self, game):
        self.game = game

    def choose_action(self):
        pass

    def get_random_action(self):
        valid_cells = self.get_valid_actions()
        valid_index = [index for index, cell in enumerate(valid_cells) if cell == 1]
        rnd_index = random.choice(valid_index)
        pos = [rnd_index//3, rnd_index%3]
        return pos# a position

    def get_best_action(self):
        pass

    def get_egreedy_action(self):
        pass

    def get_valid_actions(self):
        """
        Get the cells that are still empty
        """
        game = self.game.get_game()
        empty_cells = [ 1 if cell == 0 else 0 for cell in game]
        return empty_cells
