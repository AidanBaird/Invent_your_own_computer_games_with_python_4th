# Chapter 11 Bagels deduction game

#

import random

# Two variables that contain the max amounts of digits needed to be deciphered and the max attempts to do so

NUM_DIGITS = 3
MAX_GUESS = 10

# #  A function that generates the secret digits to be used with in the game
# Firstly generating a list of numbers from 1-9
# Shuffling said numbers
# Creates an empty variable with which to store the secret number in
# Uses a for loop to add the 3 depending on NUM_DIGITS to the secretNum variable and returning it


def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ""
    for index in range(NUM_DIGITS):
        secretNum += str(numbers[index])
    return secretNum

# # A function that gives clues depending on the players guess
# Creates a list variable to store the clues
# # Multiple if statements to check what to append into the clues variable
# Checks if the number is EQUAL to the number that position in secretNum, then appending "Fermi" to the clues
# Checks if the number is IN the secretNum and adds "Pico" if so
# Otherwise appends Bagel telling the player that the number in question is nowhere in secretNum
# Sorts the clues and joins them together before returning them

def getClues(guess, secretNum):
    clues = []
    for index in range(len(guess)):
        if guess[index] == secretNum[index]:
            clues.append("Fermi")
        elif guess[index] in secretNum:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"

    clues.sort()
    return " ".join(clues)

# # A function that makes sure "num" is made up of only the digits [0,1, 2, 3, 4, 5, 6, 7, 8, 9]
# Uses an if statement to ensure there is something in the "num"
# uses a for loop to make sure that only the digits 1-9 are in "num"
# returns True is both these checks are passed

def isOnlyDigits(num):
    if num == "":
        return False
    for index in num:
        if index not in "0 1 2 3 4 5 6 7 8 9".split():
            return False
    return True

# # Print statements introducing the game and it's concepts

print("BAGEL DEDUCTION GAME")

print("I am thinking of a %s-digit number. Try to guess what it is." % (NUM_DIGITS))
print("The clues I give are...")
print('When I say:  That means:')
print('  Bagels   None of the digits is correct.')
print('  Pico     One digit is correct but in the wrong position.')
print('  Fermi    One digit is correct and in the right position.')

# # A while statement that will check if the game is still ongoing
# Prints a statement telling you how many guesses you have
# Another while loop that tells you how many guesses you've taken and includes an input to add another
# if statement that checks if you've guessed correctly and breaks the loop if so
# if statement that checks if you've reached the MAX_GUESSES and ends the game if so

while True:
    secretNum = getSecretNum()
    print("I have thought up a number. You have %s guesses to get it." %(MAX_GUESS))

    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ""
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print("Guess #%s: " % (guessesTaken))
            guess = input()

        print(getClues(guess, secretNum))
        guessesTaken += 1
        if guess == secretNum:
            print("You have guessed the secret number!")
            break
        if guessesTaken > MAX_GUESS:
            print("You ran out of guesses. The answer was %s." %(secretNum))

    print("Do you want to play again? (Yes or No)")
    if not input().lower().startswith("y"):
        break

# Debugging steps
# line 38 changed an "i" to "index"
# Added a message telling the player they have won after guessing the number






