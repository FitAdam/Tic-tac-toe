from board import Board
from user import User

def main():

    """Main flow of the game. The gameOn set up to False ends game."""
    the_board = Board()
    the_user = User()

    while True:
        the_board.view_board()
        choice = the_user.user_move(the_user.player1)
        the_board.allocate_choice(choice)
        the_board.view_board()
        gameOn = the_board.game_check()
        if gameOn == False:
            break
        #print(f'The gameOn in MAIN is {gameOn}')
        the_board.view_board()
        choice = the_user.user_move(the_user.player2)
        the_board.allocate_choice(choice)
        the_board.view_board()
        gameOn = the_board.game_check()
        if gameOn == False:
            break

main()