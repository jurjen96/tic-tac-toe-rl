class QLearning(object):
    def __init__(self):
        self.q_table = {} # the Q table consists out of a state and actions with their action value
        # example  {[0,0,1,-1,-1,0,0,0,1]: {0:0.1, 5: 0.7}}

    def update_q(self, state, action, next_state, possible_actions, alpha, reward, gamma):
        """
        Use the update rule for Q-learning to update the Q value with the new Q-
        value.
        """
        q = self.get_action_value(state, action)
        if next_state:
            best_action_values = self.get_action_values(next_state)
            if best_action_values:
                best_index = best_action_values.index(max(best_action_values))
                best_next_action = possible_actions[best_index]
            else: # The bot has never seen this action and as such does not have a best action yet
                best_next_action = 0
        else: # When this is the last action the bot took before the game was ended,
              # the best next action is 0
            best_next_action = 0

        new_q = q + alpha * (reward + gamma * best_next_action - q)
        self.set_q(state, action, new_q)

    def set_q(self, state, action, q):
        """
        Set one entry of the Q-table.

        @param state: the state that should be updated with a new Q-value
        @param action: the action that should be set in the corresponding state (int 0-8)
        @param q: the new q value which is related to the action taken in the state (float)
        """
        try:
            action_values = self.q_table[state]
            action_values[action] = q
        except KeyError:
            action_values = {}
            action_values[action] = q
            self.q_table[state] = action_values

    def get_actions(self, state):
        """
        @return the actions that were learned for a particle state
                (dict with key: the actions -> value: the corresponding Q-values)
        """
        try:
            return self.q_table[state]
        except KeyError:
            return {}

    def get_action_value(self, state, action):
        """
        Get the Q-value for a certain action in a state

        @param state: a list representation of the requested state
        @param action: an int for the selected action
        """
        try:
            return self.q_table[state][action]
        except KeyError:
            return 0

    def get_action_values(self, state):
        """
        @return all the action Q-values for a certain state
        """
        result = []
        try:
            actions = self.q_table[state]
            for _, value in actions.iteritems():
                result.append(value)
        except KeyError: # current state is not in Q-table
            pass
        return result
