# Author: Justin Wheeler
# Date: 5/5/2021
# Description: Guessing game for letters in Bellingham

# Importing our system module and module for random choices
import sys
import random

# Getting command line arguments and defining parameters for DEBUG and PLAYER modes
tries = int(sys.argv[1])
mode = sys.argv[2]
if mode == "DEBUG":
    letter1 = sys.argv[3]
    letter2 = sys.argv[4]
if mode == "PLAYER":
    letter1 = random.choice(['b','e','l','i','n','g','h','a','m'])
    letter2 = random.choice(['b','e','l','i','n','g','h','a','m'])


print("Let's play a letter guessing game. The goal is for you to guess two letters chosen randomly from among the letters in the word 'bellingham'. The two letters can be the same.")

# Setting the count for while loop and confirming that correct guesses have not yet been made
count = 0
guessed1 = "false"
guessed2 = "false"

while count < tries:
    print("=================")
    print("Try", count+1)
    # Getting guess input and creating if statements for correct and incorrect letters
    guess = input("Guess a letter ")
    if guessed1 != "true":
        if guess == letter1:
            print("You've guessed the first letter")
            guessed1 = "true"
        else:
            print("The first letter is not", guess,)
    if guessed2 != "true":
        if guess == letter2:
            print("You've guessed the second letter")
            guessed2 = "true"
        else:
            print("The second letter is not", guess,)
    count += 1
    # This conditional ends the while loop early if both letters have been correctly guessed
    if guessed1 == "true" and guessed2 == "true":
        count = tries
# Once the game has ended, this final conditional prints results based on if guesses were correct
else:
    if guessed1 != "true" or guessed2 != "true":
        print("You are out of tries. Game over. The secret letters were ", letter1," and ",letter2,".", sep="")
    if guessed1 == "true" and guessed2 == "true":
        print("You've guessed the secret letters ", letter1,letter2,". You win!", sep="")
