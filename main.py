# the board
# class object or list or dict???????? how...

a_line = [[], [], []]
b_line = [[], [], []]
c_line = [[], [], []]

the_board = [[], [], [],
            [], [], [],
            [], [], []]

# player signs

player1 = 'x'
player2 = 'y'

# checks

def check_horizontally(new_board):
    if new_board[0] == new_board[1] == new_board[2]:
        print(f'{new_board[0]} is the winner.')
    else:
        print(f'next move.')

    if new_board[3] == new_board[4] == new_board[5]:
        print(f'{new_board[3]} is the winner.')
    else:
        print(f'next move.')

    if new_board[6] == new_board[7] == new_board[8]:
        print(f'{new_board[6]} is the winner.')
    else:
        print(f'next move.')

def check_vertically(new_board):
    if new_board[0] == new_board[3] == new_board[6]:
        print(f'{new_board[0]} is the winner.')
    else:
        print(f'next move.')

    if new_board[1] == new_board[4] == new_board[7]:
        print(f'{new_board[1]} is the winner.')
    else:
        print(f'next move.')

    if new_board[2] == new_board[5] == new_board[8]:
        print(f'{new_board[2]} is the winner.')
    else:
        print(f'next move.')

def check_obliquely(new_board):
    if new_board[0] == new_board[4] == new_board[8]:
        print(f'{new_board[0]} is the winner.')
    else:
        print(f'next move.')

    if new_board[6] == new_board[4] == new_board[2]:
        print(f'{new_board[6]} is the winner.')
    else:
        print(f'next move.')


the_board = [['x'], ['x'], ['x'],
            [], [], [],
            [], [], []]

check_horizontally(the_board)