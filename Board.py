class Board(object):

    def __init__(self):
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]

    def reset(self):
        """ Reset the board """
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]


    def update(self, pos, mark):
        """
        Update the board with the latest action

        @param pos: the position at which the marker was placed. List of [vertical, horizontal]
        @param mark: the mark representation in string format
        """
        self.board[pos[0]][pos[1]] = mark

    def print_game(self):
        """
        A helper method that helps visualing the state of the game in a user-
        friendly format
        """
        print "-------------"
        for row in range(len(self.board)):
            print "|",
            for line in range(len(self.board[row])):
                print self.board[row][line] + " |",
            print ""
            print "-------------"
