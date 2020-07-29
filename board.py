class Board:

    """Class for the board"""

    def __init__(self):

        self.the_board = ['1', '2', '3',
                         '4', '5', '6',
                         '7', '8', '9']
    
    def game_check(self):

        """This funcion checks the board if the signs create a line it returns a gameON as False."""

        gameOn = True
        while True:
        # check_horizontally(new_board):
            if self.the_board[0] == self.the_board[1] == self.the_board[2]:
                print(f'{self.the_board[0]} is the winner.')
                gameOn = False
                break

            if self.the_board[3] == self.the_board[4] == self.the_board[5]:
                print(f'{self.the_board[3]} is the winner.')
                gameOn = False
                break

            if self.the_board[6] == self.the_board[7] == self.the_board[8]:
                print(f'{self.the_board[6]} is the winner.')
                gameOn = False
                break

        # check_vertically(new_board):
            if self.the_board[0] == self.the_board[3] == self.the_board[6]:
                print(f'{self.the_board[0]} is the winner.')
                gameOn = False
                break

            if self.the_board[1] == self.the_board[4] == self.the_board[7]:
                print(f'{self.the_board[1]} is the winner.')
                gameOn = False
                break

            if self.the_board[2] == self.the_board[5] == self.the_board[8]:
                print(f'{self.the_board[2]} is the winner.')
                gameOn = False
                break

        # check_obliquely(new_board):
            if self.the_board[0] == self.the_board[4] == self.the_board[8]:
                print(f'{self.the_board[0]} is the winner.')
                gameOn = False
                break

            if self.the_board[6] == self.the_board[4] == self.the_board[2]:
                print(f'{self.the_board[6]} is the winner.')
                gameOn = False
                break
            
            else:
                print('Time for the next move.')
                break
        
        #print(f'The gameOn is {gameOn}')
        return gameOn

    def view_board(self):

        """This function is used to show the board to the players """

        print(f'\n\t  {self.the_board[0][0]} | {self.the_board[1][0]} | {self.the_board[2][0]}')
        print('\t-------------')
        print(f'\t  {self.the_board[3][0]} | {self.the_board[4][0]} | {self.the_board[5][0]}')
        print('\t-------------')
        print(f'\t  {self.the_board[6][0]} | {self.the_board[7][0]} | {self.the_board[8][0]}')
        print('\t')

    
    def allocate_choice(self, move):

        """Update and return the board with allocated move."""

        position = self.the_board.pop(move[0])
        self.the_board.insert(move[0], move[1])
        return self.the_board
