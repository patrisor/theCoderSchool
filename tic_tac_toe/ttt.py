# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ttt.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: patrisor <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/07/20 02:01:05 by patrisor          #+#    #+#              #
#    Updated: 2019/07/20 03:35:05 by patrisor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def choose_piece(player):
    if player == "Player 1":
        return 'X'
    if player == "Player 2":
        return 'O'

def player_turn(player):
    if player == "Player 1":
        return "Player 2"
    if player == "Player 2":
        return "Player 1"

def print_board(b):
    out = "     |     |     \n"
    out += "  " + str(b[0][0]) + "  |  " + str(b[0][1]) + "  |  " + str(b[0][2]) + "  \n"
    out += "_____|_____|_____\n"
    out += "     |     |     \n"
    out += "  " + str(b[1][0]) + "  |  " + str(b[1][1]) + "  |  " + str(b[1][2]) + "  \n"
    out += "_____|_____|_____\n"
    out += "     |     |     \n"
    out += "  " + str(b[2][0]) + "  |  " + str(b[2][1]) + "  |  " + str(b[2][2]) + "  \n"
    out += "     |     |     "
    print(out)

def solver_algorithm(board, x, y):
    if board[0][y] == board[1][y] == board [2][y]:
        return True
    if board[x][0] == board[x][1] == board [x][2]:
        return True
    if x == y and board[0][0] == board[1][1] == board [2][2]:
        return True
    if x + y == 2 and board[0][2] == board[1][1] == board [2][0]:
        return True
    return False

def check_for_game_over(board):
    hit = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if isinstance(board[i][j], str):
                hit += 1
    if hit == 9:
        return True
    else:
        return False

def tic_tac_toe():
    BOARD = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    player = "Player 2"
    while True:
        print_board(BOARD)
        player = player_turn(player)
        piece = choose_piece(player)
        inp = input(player + ", please enter location to place game piece: \n")
        for i in range(len(BOARD)):
            for j in range(len(BOARD[i])):
                if BOARD[i][j] == int(inp):
                    BOARD[i][j] = piece
                    if (solver_algorithm(BOARD, i, j)):
                        print_board(BOARD)
                        print(player + " WINS!")
                        return 1
        if check_for_game_over(BOARD) == True:
            print("GAME OVER! No more moves left!")
            return 0

def main():
    while True:
        ret = tic_tac_toe()
        if ret == 1 or ret == 0:
            resp = input("Play Again? (y/n)")
        if resp == 'y':
            continue
        else:
            break

if __name__ == "__main__":
    main()
