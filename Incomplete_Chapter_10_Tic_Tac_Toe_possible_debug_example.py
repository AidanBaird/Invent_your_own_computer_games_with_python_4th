# Chapter 10

import random

# A function that creates a visible board in the output

def drawboard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

# Gives the player the choice of either X or O

def inputplayerletter():
    letter = " "
    while not (letter == "X" or letter == "O"):
        print(" Do you want to be X or O?")
        letter = input().upper()
        if letter == "X":
            return ["X", "O"]
        else:
            return ["0", "X"]

# A function that randomly chooses the player that goes first and returns the respective player

def whogoesfirst():
    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "player"

# Takes the players letter and replaces the board element with it

def makemove(board, letter, move):
    board[move] = letter

# Checks all the ways in which a player can win

def iswinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))

# creates a copy of the board in a new variable "boardcopy" then goes through the current board and appends the elements

def getboardcopy(board):
    boardcopy = []
    for i in board:
        boardcopy.append(i)
    return boardcopy

# Checks if the board space is free and returns a " "

def isspacefree(board, move):
    return board[move] == " "

#

def getplayermove(board):
    move = ""
    while move not in "1 2 3 4 5 6 7 8 9".split() or not isspacefree(board,int(move)):
        print("What is your next move?")
        move = input()
    return int(move)

# Creates a simple AI the firstly works out what spaces are left then chooses randomly from that list

def chooserandommovefromlist(board, movelist):
    possiblemoves = []
    for i in movelist:
        if isspacefree(board, i):
            possiblemoves.append(i)
    if len(possiblemoves) != 0:
        return random.choice(possiblemoves)
    else:
        return None

# Checks past variable "computerletter" and changes playerletter in relation to it
# # Going through a few scenarios to increase the complexity of the AI
# Then checks if the player will fulfil any requirement to win next turn and moves to block them
# Checks is the corners are empty and returns one of the for corners as a move
# if there are no corner spaces it will aim to take the center
# If none of the prior options are left it will randomly pick from the four remaining positions

def getcomputermove(board, computerletter):
    if computerletter == "X":
        playerletter = "O"
    else:
        playerletter = "X"

    for i in range(1, 10):
        boardcopy = getboardcopy(board)
    if isspacefree(boardcopy, i):
        makemove(boardcopy, playerletter, i)
        if iswinner(boardcopy, playerletter):
            return i

    move = chooserandommovefromlist(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isspacefree(board, 5):
        return 5

    return chooserandommovefromlist(2, 4, 6, 8)

# Checks if there are any positions left to fill and returns True if so and False otherwise

def isboardfull(board):
    for i in range(1, 10):
        if isspacefree(board, 1):
            return False
    return True

# Sets all the positions to " ", being a clear space to enter a letter onto
# # Players turn
# Checks if it's the players turn and inputs their move onto the board
# Checks if the players last move won and congratulates them if so
# Checks if the board is full and ties the game if so, otherwise gives the computer a turn
# # Computers turn
# Goes through all the same checks as the "players turn" section
# # Bouncing the turns back and forth until there is either a tie or a winner
# Finally once the gameisplaying = False asking if the player would like to play again
while True:
    theboard = [" "] * 10
    playerletter, computerletter = inputplayerletter()
    turn = whogoesfirst()
    print("The " + turn + " will go first.")
    gameisplaying = True

    while gameisplaying:
        if turn == "player":
            drawboard(theboard)
            move = getplayermove(theboard)
            makemove(theboard, playerletter, move)

            if iswinner(theboard, playerletter):
                drawboard(theboard)
                print("Hooray! You have won the game!")
                gameisplayer = False
            else:
                if isboardfull(theboard):
                    drawboard(theboard)
                    print("The game is a tie!")
                    break
                else:
                    turn = "computer"
        else:
            move = getcomputermove(theboard, computerletter)
            makemove(theboard, computerletter, move)

            if iswinner(theboard, computerletter):
                drawboard(theboard)
                print("The computer has beaten you! You lose.")
                gameisplaying = False
            else:
                if isboardfull(theboard):
                    drawboard(theboard)
                    print("The game is a tie!")
                    break

    print("Do you want to play again? (yes or no)")
    if not input().lower().startswith("y"):
        break

