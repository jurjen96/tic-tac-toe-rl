import random

class Action(object):

    def __init__(self, game):
        self.game = game

    def get_random_action(self):
        """
        Get all the available actions from the game and select a random action

        @return: a random index of the game celss (int)
        """
        valid_cells = self.get_valid_actions()
        valid_index = [index for index, cell in enumerate(valid_cells) if cell == 1]
        action = random.choice(valid_index)
        return action

    def get_best_action(self, q_learning, state):
        """
        Select the best action based on the learned actions it has done before.
        If there are no actions it can choose from (the bot has never been in
        this state), select a random action.
        """
        actions = q_learning.get_actions(state)
        explotation_actions = actions.keys()
        if not explotation_actions:
            return self.get_random_action()

        action_values = q_learning.get_action_values(state)
        max_index = action_values.index(max(action_values))
        return explotation_actions[max_index]

    def get_egreedy_action(self, epsilon, q_learning, state):
        """
        Use egreedy to select if a random action (exploration) should be choosen
        over learned actions (exploitation)
        """
        random_nr = random.uniform(0, 1)
        if random_nr > epsilon:
            action = self.get_best_action(q_learning, state)
        else:
            action = self.get_random_action()

        return action

    def get_valid_actions(self, game=None):
        """
        Get the cells that are still empty
        """
        if game is None: # If the game is not defined use the current game state
            game = self.game.get_game()

        empty_cells = [1 if cell == 0 else 0 for cell in game]

        return empty_cells
