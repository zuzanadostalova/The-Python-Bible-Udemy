# # 62. lesson - Tic tac toe
# # we need datastructure - list, tuple? we cannot use tuples - they are not changeable
# # but a list is changeable

# board = [" " for i in range(9)] # a board with 9 blank spaces, we used list comprehension
# # to make it faster
# # print(board)
# # Output: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# # three by three grid for tic tac toe

# def print_board():
#     row1 = "|{}|{}|{}|".format(board[0], board[1], board[2]) # | pipe symbol - shift and \
#     row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
#     row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])
#     # slightly repetitive we could write for loop

#     print()
#     print(row1)
#     print(row2)
#     print(row3)
#     print()

# # print(print_board()) # do not forget to print "print_board" otherwise it will not run
# # Output:
# # | | | |
# # | | | |
# # | | | |

# # while True: # the game loop - runs forever, the rest of out code inside
# #     print_board()
# #     choice = int(input("Enter your move (1-9): ").strip())
# #     board[choice - 1] = "X"
# # the first player X, careful - if he is going to type in number 5 it means "board[4]""
# # Python indexing starts at [0], therefore we have to write "choice - 1"

# # Output:
# # Enter your move (1-9): 3

# # | | |X|
# # | | | |
# # | | | |

# # Enter your move (1-9): 5

# # | | |X|
# # | |X| |
# # | | | |

# # Enter your move (1-9): 7

# # | | |X|
# # | |X| |
# # |X| | |

# # we can stop it by pressing ctrl + C

# while True: # the game loop - runs forever, the rest of out code inside
#     print_board()
#     choice = int(input("Enter your move (1-9): ").strip())
# # we need to make sure that the player is writing numbers of yet available spaces on the keyboard
#     if board[choice - 1] == " ":
#         board[choice - 1] = "X"
#     else:
#         print()
#         print("That space is taken.")

# # 63. lesson - Continuing with Tic tac toe
board = [" " for i in range(9)]

def print_board():
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2]) 
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])
    
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon): # icon x or y
    if icon== "X":
        number = 1
    elif icon == "O":
        number = 2

    print("Your turn, player {}.".format(icon))

    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print()
        print("That space is taken.")

# Who has won the game?

def is_victory(icon): 
    if(board[0] == icon and board[1] == icon and board[2] == icon) or \
      (board[3] == icon and board[4] == icon and board[5] == icon) or \
      (board[6] == icon and board[7] == icon and board[8] == icon) or \
      (board[0] == icon and board[3] == icon and board[6] == icon) or \
      (board[1] == icon and board[4] == icon and board[7] == icon) or \
      (board[2] == icon and board[5] == icon and board[8] == icon) or \
      (board[0] == icon and board[4] == icon and board[8] == icon) or \
      (board[2] == icon and board[4] == icon and board[6] == icon) or \

# [0], [3], [6], all the rows   
# all the columns

while True: 
    print_board()
    player_move("X")
    print_board
    player_move("O")


