# Chapter 15

# Imports

import random
import sys

# Creating constant variables for the height and width of the board

WIDTH = 8
HEIGHT = 8

# # A function that generates the game board
# Prints the top numbers and upper line of the board
# two loops that create the inner lines with in the board
# Repeated prints to do the same on the bottom as the top

def drawBoard(board):
    print("    123456789")
    print("   +--------+")
    for y in range(HEIGHT):
        print("%s|" % (y+1), end="")
        for x in range(WIDTH):
            print(board[x][y], end="")
        print("|%s" % (y+1))
    print("  +--------+")
    print("   123456789")

# # Contains the board and the free spaces with it

def getNewBoard():
    board = []
    for i in range(WIDTH):
        board.append([" ", " ", " ", " ", " ", " ", " ", " "])
    return board

# # A function that does various checks to ensure that the move is valid
# Makes sure you're only able to flip the other players markers
# Only allows you to go certain directions
# Makes sure your move is on the board

def isValidMove(board, tile, xstart, ystart):
    if board[xstart][ystart] != " " or not isOnBoard(xstart, ystart):
        return False
    if tile == "X":
        otherTile = "O"
    else:
        otherTile = "X"

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        while isOnBoard(x, y) and board [x][y] == otherTile:
            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])

    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip

# # Defines what is and is not on the board

def isOnBoard(x, y):
    return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT - 1

#

def getBoardWithValidMoves(board, tile):
    boardCopy = getBoardCopy(board)

    for x, y in getBoardWithValidMoves(boardCopy, tile):
        boardCopy[x][y] = "."
    return boardCopy

# # Generates a list of valid moves

def getValidMoves(board, tile):
    validMoves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves

# # Works out the score of both players and returns them in a dictionary

def getScoreOfBoard(board):
    xscore = 0
    oscore = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == "X":
                xscore += 1
            if board [x][y] == "O":
                oscore += 1
    return {"X":xscore, "O":oscore}

# # Lets the player choose their character

def enterPlayerTile():
    tile = ""
    while not (tile == "X" or tile == "O"):
        print("Do you want to be X or O?")
        tile = input().upper()

    if tile == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]

# Randomly chooses between 0-1 to return the player that goes first

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return "computer"
    else:
        return "player"

#

def makeMove(board, tile, xstart, ystart):
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x,y in tilesToFlip:
        board [x][y] = tile
    return True

# Creates a copy of the board

def getBoardCopy(board):
    boardCopy = getNewBoard()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            boardCopy[x][y] = board[x][y]

    return boardCopy

# Checks in the move is on the corner

def isOnCorner(x, y):
    return (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGHT - 1)

# Takes the players move as an input and makes sure it's valid and on the board

def getPlayerMove(board, playerTile):
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print("Enter your move, 'quit' to end the game, or 'hints' to toggle hints.")
        move = input().lower()
        if move == "quit" or move == "hints":
            return move

        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[0]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print("That is not a valid move. Enter the column (1-8) and the the row (1-8).")
            print('For example, 81 will move on the top-right corner.')

    return [x, y]

# Uses other functions the return the best move using the algorithm used

def getComputerMove(board, computerTile):
    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves)

    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    bestScore = -1
    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, computerTile, x, y)
        score = getScoreOfBoard(boardCopy)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove

# Prints the score so it is visible to the player

def printScore(board, playerTile, computerTile):
    scores = getScoreOfBoard(board)
    print("You: %s points. Computer: %s points" % (scores[playerTile], scores[computerTile]))

# Begins the game and populates it with the first markers
# Checks who is going first and if they have any valid moves
# Takes their move and either quits, shows hints or adds the move to the board
# The bounces the turn to the other player

def playGame(playerTile, computerTile):
    showHints = False
    turn = whoGoesFirst()
    print("The " + turn + " will go first.")

    board = getNewBoard()
    board[3][3] = "X"
    board[3][4] = "O"
    board[4][3] = "O"
    board[4][4] = "X"

    while True:
        playerValidMoves = getValidMoves(board, playerTile)
        computerValidMoves = getValidMoves(board, computerTile)

        if playerValidMoves == [] and computerValidMoves == []:
            return board

        elif turn == "player":
            if playerValidMoves != []:
                if showHints:
                    validMovesBoard = getBoardWithValidMoves(board, playerTile)
                    drawBoard(validMovesBoard)
                else:
                    drawBoard(board)
                printScore(board, playerTile, computerTile)

                move = getPlayerMove(board, playerTile)
                if move == "quit":
                    print("Thanks for playing!")
                    sys.exit()
                elif move == "hints":
                    showHints = not showHints
                    continue
                else:
                    makeMove(board, playerTile, move[0], move[1])
            turn = "computer"

        elif turn == "computer":
            if computerValidMoves != []:
                drawBoard(board)
                printScore(board, playerTile, computerTile)

                input("Press Enter to see the computer's move.")

                move = getPlayerMove(board, computerTile)
                makeMove(board, computerTile, move[0][1])
            turn = "player"

print("Welcome to reversegam!")

playerTile, computerTile = enterPlayerTile()

while True:
    finalBoard = playGame(playerTile, computerTile)

    drawBoard(finalBoard)
    scores = getScoreOfBoard(finalBoard)
    print(" X scores %s points. O scored %s points." % (scores["X"], scores["O"]))
    if scores[playerTile] > scores[computerTile]:
        print("You beat the computer by %s points! Congratulations!" % (scores[playerTile] - scores[computerTile]))
    elif scores[playerTile] < scores[computerTile]:
        print("You lost. The computer beat you by %s points." % (scores[computerTile] - scores[playerTile]))
    else:
        print("The game was a tie!")

    print("Do you want to play again?(yes or no)")
    if not input().lower().startswith("y"):
        break

# Problems
# Misaligned board
# Hints doesn't work
# Add a starter board?
# Moves are not added to the board
# Board is not redrawn
#

# Debugging
# line 175 added print('For example, 81 will move on the top-right corner.')
#
#
#
#
#
#




