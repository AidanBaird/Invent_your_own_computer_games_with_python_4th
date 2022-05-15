# Chapter two

# The contents of this chapter will revolve around a 1-20 guessing game

import random

guessestaken = 0

print("Hello! What is your name?")

myname= input()

number = random.randint(1,20)

print("Well, " + myname + ", I am thinking of a number between 1 and 20. What do you think it is?")

# Creating a for loop that will repeat at most 6 times iterating over certain code

for guessestaken in range(6):
    print("Take a guess " + myname)
    guess= input()
    guess = int(guess)

    # If statements to print a statement that will help you decypher the random number

    if guess < number:
        print("Your guess is too low")

    if guess > number:
        print("Your guess is too damn high")

    if guess == number:
        # break here to leave the loop and continue on with the code
        break

if guess == number:
    guessestaken = str(guessestaken + 1)
    print("Welldone " + myname + "! You guessed my number in " + guessestaken + " guesses!")

if guess != number:
    number = str(number)
    print("Shamefully " + myname + "you did not guess the number, the number I was thinking of was " + number)

# This project is a useful example of importing random and the use of input()
