class State(object):
    def __init__(self, game):
        self.game_setup = game # TODO might be confusing, use a different name

    def __str__(self):
        return "State: " + str(self.game_setup)

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))
