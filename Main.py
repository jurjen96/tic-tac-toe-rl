from Board import Board
from Agent import Agent
from Game import Game

def main():
    board = Board()
    game = Game()
    player_x = Agent("X", board, game, "human")
    player_o = Agent("O", board, game, "random")

    game.play(player_x, player_o)

    board.print_game()
    print "X has won: " + str(game.has_won(player_x.get_mark()))
    print "O has won: " + str(game.has_won(player_o.get_mark()))

if __name__ == "__main__":
    print "Starting the tic-tac-toe game"
    main()
