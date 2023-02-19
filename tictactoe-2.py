import random

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def draw_board(board):
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

def is_winner(board, player):
    return ((board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player))

def get_bot_move(board):
    while True:
        move = random.randint(0, 8)
        if board[move] == ' ':
            return move

def play_game():
    player = 'X'
    while True:
        draw_board(board)
        if is_winner(board, player):
            print(player + ' wins!')
            break
        elif ' ' not in board:
            print('Draw!')
            break
        elif player == 'X':
            move = int(input('Enter move (0-8): '))
            if board[move] == ' ':
                board[move] = player
                player = 'O'
        else:
            move = get_bot_move(board)
            board[move] = player
            player = 'X'

play_game()
