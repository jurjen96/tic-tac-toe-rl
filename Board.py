import sys
import numpy as np

class Board(object):

    def __init__(self):
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]

    def reset(self):
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]


    def update(self, pos, mark):
        self.board[pos[0]][pos[1]] = mark
        # print self.board

    def print_game(self):
        print "-------------"
        for row in range(len(self.board)):
            print "|",
            for line in range(len(self.board[row])):
                print self.board[row][line] + " |",
            print ""
            print "-------------"
