#!/usr/bin/env phyton

import random

def main():
    """Start a genre guessing game."""
    print("Guess the genre!")

    genre = [
       "hip hop",
       "rock",
       "country",
       "jazz",
       "pop"
       ]
          
    x = "pop"
    print ("Hint: Justin Bieber")
    guess = None

    while x != guess:
          
        guess = str(input("What genre could it be?"))

        if x == guess:
            print("Wow, you guessed {} correctly! Congratulations.".format(guess))
            break
        else:
            print("Oh No, You guessed {}. But it's wrong, please try again!".format(guess))

main()
     


