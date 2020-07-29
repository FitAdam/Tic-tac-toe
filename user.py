class User:
    """This is the class for the user"""
    def __init__(self):
        self.player1 = 'X'
        self.player2 = 'O'

    def user_move(self, player_sign):

        """This function is used to get user's move and return it"""

        move = []
        message = "Time to move. Choose position from 1 to 9:"
        message += "\nLike this: 5"
        message += f"\nPlayer {player_sign} moves: "
        while True:
            try:
                field = int(input(message))
                #symbol = str(input('Type your symbol: '))
            except ValueError:
                print("\nOops!  That was no valid number.  Try again...\n")
                continue
            else:
                field -= 1
                move.append(field)
                move.append(player_sign)
                print(move)
                return move
