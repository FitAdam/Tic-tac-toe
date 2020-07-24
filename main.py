# the board
the_board = {
    'a_line' : [[], [], []],
    'b_line' : [[], [], []],
    'c_line' : [[], [], []]
    }

# player signs

player1 = 'x'
player2 = 'y'

# checks

def check_horizontally(new_board):
    for key, value in new_board.items():
        if value[0] == value[1] == value[2]:
            print(f'{value[0]} is the winner.')
        else:
            print(f'next move.')
"""
        if b_line[0] == b_line[1] == b_line[2]:
            print(f'{b_line[0]} is the winner.')
        else:
            print(f'next move.')

        if c_line[0] == c_line[1] == c_line[2]:
            print(f'{a_line[0]} is the winner.')
        else:
            print(f'next move.')

def check_vertically(new_board):
    if a_line[0] == b_line[0] == c_line[0]:
        print(f'{a_line[0]} is the winner.')
    else:
        print(f'next move.')

    if a_line[1] == b_line[1] == c_line[1]:
        print(f'{b_line[1]} is the winner.')
    else:
        print(f'next move.')

    if a_line[2] == b_line[2] == c_line[2]:
        print(f'{a_line[0]} is the winner.')
    else:
        print(f'next move.')

def check_obliquely(new_board):
    if a_line[0] == b_line[1] == c_line[2]:
        print(f'{a_line[0]} is the winner.')
    else:
        print(f'next move.')

    if a_line[2] == b_line[1] == c_line[0]:
        print(f'{b_line[1]} is the winner.')
    else:
        print(f'next move.')
"""

new_board = {
    'a_line' : [['x'], ['x'], ['x']],
    'b_line' : [[], [], []],
    'c_line' : [[], [], []]
    }

check_horizontally(new_board)