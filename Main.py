from Board import Board
from Agent import Agent
from Game import Game

def main():
    board = Board()
    game = Game()
    player_x = Agent("X", board, game)
    player_o = Agent("O", board, game)

    player_x.do_action([0, 2])
    player_x.do_action([1, 1])
    player_x.do_action([2, 0])
    # player_o.do_action([1, 1])
    board.print_game()
    print game.has_won(player_x.get_mark())


if __name__ == "__main__":
    print "Starting the tic-tac-toe game"
    main()
