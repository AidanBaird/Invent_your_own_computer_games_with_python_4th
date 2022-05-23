# Chapter 14

# Create to global variables

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
MAX_KEY_SIZE = len(SYMBOLS)

# # A function to get the mode for either decrypting or encrypting
# User inputs whether they want to encrypt or decrypt a message
# If statement to choose the correct mode depending on the users input

def getMode():
    while True:
        print("Do you wish to encrypt or decrypt a message?")
        mode = input().lower()
        if mode in ["encrypt", "e", "decrypt", "d"]:
            return mode
        else:
            print("Enter either 'encrypt' or 'e' or 'decrypt' or 'd'.")

# # A function that gives the user an input for their message

def getMessage():
    print("Enter your message:")
    return input()

# # A function that gets the key from the user
# Starts the key off at 0
# Makes sure the key is within a usable range before returning the key

def getKey():
    key = 0
    while True:
        print("Enter the key (1-%s)" % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

# # A function  that creates a new string from message by moving letters by the key and returning translated

def getTranslateMessage(mode, message, key):
    if mode[0] == "d":
        key = -key
    translated = ""

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:
            translated += symbol

        else:
            symbolIndex += key
            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]
    return translated

# #

mode = getMode()
message = getMessage()
key = getKey()
print("your translated test is:")
print(getTranslateMessage(mode, message, key))

# debugging
# line 56 replaced SYMBOLS with len(SYMBOLS)
# Line 52 replaced symbol with symbolIndex