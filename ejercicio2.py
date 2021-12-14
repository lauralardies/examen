import random
import os

dimension = int(input("How many rows do you want your board to have? (Please note that rows and columns will have the same value): "))
white_piece = 0x2656 #White piece starts first --> Player1
black_piece = 0x265C #Black piece starts second --> Player 2

def createBoard(dimension, black_piece, white_piece):
    board = []
    for x in range(dimension):
        row = []
        for y in range(dimension):
            if board[x][y] == board[x][random.sample(range(dimension), 1)]:
                row.append(black_piece) #black tower
            if board[x][y] == board[x][random.sample(range(dimension), 1)]:            
                row.append(white_piece) #white tower
            else:
                row.append(" ")
        board.append(row)
    return board

def printBoard(board):
    for i in range(len(board)):
        print(board[i])

def play(black_piece, white_piece):
    column = random.randint(0, dimension)
    for i in column:
        if black_piece[0][1] != white_piece[0][1]:
            break
        else:
            black_piece = black_piece[0 + i][1]
    return black_piece

board = createBoard(dimension)
printBoard(board)