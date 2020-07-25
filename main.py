# the board
# class object or list or dict???????? how...

a_line = [[], [], []]
b_line = [[], [], []]
c_line = [[], [], []]

the_board = ['1', '2', '3',
            '4', '5', '6',
            '7', '8', '9']

# player signs

player1 = 'x'
player2 = 'y'

# checks
def game_check(new_board):
    gameOn = True
    while gameOn:
    # check_horizontally(new_board):
        if new_board[0] == new_board[1] == new_board[2]:
            print(f'{new_board[0]} is the winner.')
            gameOn = False
            break

        if new_board[3] == new_board[4] == new_board[5]:
            print(f'{new_board[3]} is the winner.')
            gameOn = False
            break

        if new_board[6] == new_board[7] == new_board[8]:
            print(f'{new_board[6]} is the winner.')
            gameOn = False
            break

    # check_vertically(new_board):
        if new_board[0] == new_board[3] == new_board[6]:
            print(f'{new_board[0]} is the winner.')
            gameOn = False
            break

        if new_board[1] == new_board[4] == new_board[7]:
            print(f'{new_board[1]} is the winner.')
            gameOn = False
            break

        if new_board[2] == new_board[5] == new_board[8]:
            print(f'{new_board[2]} is the winner.')
            gameOn = False
            break

    # check_obliquely(new_board):
        if new_board[0] == new_board[4] == new_board[8]:
            print(f'{new_board[0]} is the winner.')
            gameOn = False
            break

        if new_board[6] == new_board[4] == new_board[2]:
            print(f'{new_board[6]} is the winner.')
            gameOn = False
            break
        
        else:
            print('Time for the next move.')
            break

    return gameOn




def view_board(new_board):
    print(f'\n\t  {new_board[0][0]} | {new_board[1][0]} | {new_board[2][0]}')
    print('\t-------------')
    print(f'\t  {new_board[3][0]} | {new_board[4][0]} | {new_board[5][0]}')
    print('\t-------------')
    print(f'\t  {new_board[6][0]} | {new_board[7][0]} | {new_board[8][0]}')
    print('\t')


def user_move(new_board):
    move = []
    message = "Time to move. Choose position from 1 to 9:"
    message += "\nLike this: 5"
    message += "\nPlayer moves: "
    field = int(input(message))
    symbol = str(input('Type your symbol: '))
    field -= 1
    move.append(field)
    move.append(symbol)
    print(move)
    return move

def allocate_choice(board, move):
    position = board.pop(move[0])
    board.insert(move[0], move[1])
    return board

def main(the_board):
    gameOn = True
    while gameOn:
        view_board(the_board)
        choice = user_move(the_board)
        the_board = allocate_choice(the_board, choice)
        view_board(the_board)
        gameOn = game_check(the_board)


main(the_board)
    