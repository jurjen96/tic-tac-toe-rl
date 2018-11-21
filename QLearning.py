class QLearning(object):

    def __init__(self):
        self.q = {} # the Q table consists out of a state and actions with their action value
        # example  {[0,0,1,-1 ... 0,0,1]: {0:0.1, 5: 0.7}}

    def update_q(self, state, action, next_state, q_learning, possible_actions, alpha, reward, gamma):
        q = self.get_action_value(state, action)
        best_action_values = q_learning.get_action_values(next_state)
        if best_action_values:
            best_index = best_action_values.index(max(best_action_values))
            best_action = possible_actions[best_index]
        else:
            best_action = 0

        new_q = q + alpha * (reward + gamma * best_action - q)
        # print "-------"
        # print alpha
        # print reward
        # print gamma
        # print best_action
        # print q
        # print new_q
        # print "-------"
        self.set_q(state, action, new_q)

    def get_q(self):
        return self.q

    def set_q(self, state, action, q):
        try:
            action_values = self.q[state]
            action_values[action] = q
            print "Using old q" + str(state)

        except KeyError:
            action_values = {}
            action_values[action] = q
            self.q[state] = action_values
            print "New q entry" + str(state)


    def get_actions(self, state):
        try:
            return self.q[state]
        except KeyError:
            return {}

    def get_action_value(self, state, action):
        try:
            return self.q[state][action]
        except KeyError:
            return 0

    def get_action_values(self, state):
        result = []
        try:
            actions = self.q[state]
            for _, value in actions.iteritems():
                result.append(value)
        except KeyError: # current state is not in q-table
            pass
        return result
