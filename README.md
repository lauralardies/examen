# examen

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/examen)
https://github.com/lauralardies/examen

Ejercicio 1:
```
banana = list("Banana")
banana1 = []
banana2 = []

def sepVowelConsonant(banana, banana1, banana2):
    banana1 = []
    banana2 = []
    for i in range(len(banana)):
        if banana[i] == "a" or banana[i] == "e" or banana[i] == "i" or banana[i] == "o" or banana[i] == "u":
            banana[i] = "Vowel"
        else:
            banana[i] = "Consonant"

    for i in range(len(banana)):
        if banana[i] == "Vowel":
            banana1.append(banana[i])
        if banana[i] == "Consonant":
            banana2.append(banana[i])

# Player 1 --> Plays with vowels (banana1)

def pyramid(banana):
    for i in range(len(banana) + 1):
        line = " "*(len(banana) - i) + printPyramid(banana[0:i])
        print(line)

def printPyramid(banana):
    solution = ""
    for i in range(len(banana)):
        solution = solution + banana[i] + " "
    return solution

# Player 2 --> Plays with consonants (banana2)

def pyramid2(banana):
    for i in range(len(banana) + 1):
        line = " "*(len(banana) - i) + printPyramid2(banana[0:i])
        print(line)

def printPyramid2(banana):
    solution = ""
    for i in range(len(banana)):
        solution = solution + banana[i] + " "
    return solution

pyramid(banana)
pyramid2(banana)
```

Ejercicio 2:
```
import random

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
