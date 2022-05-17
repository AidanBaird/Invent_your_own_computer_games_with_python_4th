# Chapter 9 extending hangman

import random

HANGMAN_PICS = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
  O |
    |
    |
   ===''', '''
+---+
  O |
  | |
    |
   ===''', '''
+---+
  O |
 /| |
    |
   ===''', '''
+---+
  O |
 /|\|
    |
   ===''', '''
+---+
  O |
 /|\|
 /  |
   ===''', '''
+---+
  O |
 /|\|
 / \|
   ===
   ''', '''
+---+
 [O |
 /|\|
 / \|
   ===
   ''', '''
+---+
 [O] |
 /|\|
 / \|
   ===
   ''']

#words = """ant baboon badger bat bear beaver camel cat clam cobra cougar
 #coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
 #lion lizard llama mole monkey moose mouse mule newt otter owl panda
 #parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
 #skunk sloth snake spider stork swan tiger toad trout turkey turtle
 #easel whale wolf wombat zebra""".split()

# Adding dictionaries to be used as another database of words

words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
         'Shapes': 'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon'
                   ' octagon'.split(),
         'Fruits': 'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry'
                   ' tomato'.split(),
         'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey'
                   ' moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel'
                   ' whale wolf wombat zebra'.split()}



#print(words)
#print(HANGMAN_PICS[0])
#print(HANGMAN_PICS[1])
#print(HANGMAN_PICS[2])
#print(HANGMAN_PICS[3])
#print(HANGMAN_PICS[4])
#print(HANGMAN_PICS[5])
#print(HANGMAN_PICS[6])

# A function that chooses a random word from a wordlist

#def getrandomword(wordlist):
    #wordindex = random.randint(0, len(wordlist) - 1)
    #return wordlist[wordindex]

# A new function that will give a choice
def getrandomword(worddict):
    wordkey = random.choice(list(worddict.keys()))
    wordindex = random.randint(0, len(worddict[wordkey]) -1)
    return [worddict[wordkey][wordindex], wordkey]


# A function that shows the progress of the hangman

def displayboard(missedletters, correctletters, secretword):
    print(HANGMAN_PICS[len(missedletters)])
    print()

    # Produces a string with all the missed letters separated by a " "

    print("Missed letters:", end="")
    for letter in missedletters:
        print(letter, end="")
    print()


    # Produces the "_____" depending on the length of the secret word

    blanks = "_" * len(secretword)

    # Creates a for loop that will iterate through every letter in the secret word and replace the "_" with the
    # correct letter

    for i in range(len(secretword)):
        if secretword[i] in correctletters:
            blanks = blanks[:i] + secretword[i] + blanks[i+1:]

    # Displays the blanks and correct letters with a space inbetween

    for letter in blanks:
        print(letter, end=" ")
    print()

    # Gets a guess from the player and ensures that it is a single letter and then returns the guess

def getguess(alreadyguessed):
    while True:
        print("Guess a letter")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please guess a single letter")
        elif guess in alreadyguessed:
            print("You have already guessed this letter. Choose another")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Enter a letter (abcdefghijklmnopqrstuvwxyz)")
        else:
            return guess

# Asks if the player would like to play again

def playagain():
    print("Do you want to play again? (Yes or no)")
    return input().lower().startswith("y")

# Prints the title of the game and holds the certain variables that it needs to run

print("H A N G M A N")

# New code to allow for a difficulty that revolves around taking away 'lives' via deleting HANGMAN_PICS elements

difficulty = " "
while difficulty not in "EMH":
    print("Enter difficulty: E - Easy, M - Medium, H - Hard")
    difficulty = input().upper()

if difficulty == "M":
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == "H":
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedletters = ""
correctletters = ""
secretword, secretset = getrandomword(words)
gameisdone = False

# a while loop that

# Adding a print command that will show what dictionary your word is from

while True:
    print("The secret word is in the set: " + secretset)
    displayboard(missedletters, correctletters, secretword)

    guess = getguess(missedletters + correctletters)

    if guess in secretword:
        correctletters += guess

        for i in range(len(secretword)):
            foundallletters = True
            if secretword[i] not in correctletters:
                foundallletters = False
                break
        if foundallletters:
            print("Yes! the secret word is " + secretword + "! You have won!")
            gameisdone = True
    else:
        missedletters = missedletters + guess


    if len(missedletters) == len(HANGMAN_PICS) - 1:
        displayboard(missedletters, correctletters, secretword)
        print("You have ran out of guesses! \nAfter " + str(len(missedletters)) + " missed guesses and " +
                        str(len(correctletters)) + " correct guesses" + "\nthe secret word was " + secretword + ".")
        gameisdone = True


    if gameisdone:
        if playagain():
            missedletters = ""
            correctletters = ""
            gameisdone = False
            secretword, secretset = getrandomword(words)
        else:
            break