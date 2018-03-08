# adding comments to guide students

import random, time

colors = ['orange', 'red', 'blue', 'yellow', 'indigo', 'green', 'violet']

favColor = random.choice(colors)

print("Hi! My favorite color is found in the rainbow." +
      "\n\n" +
      "Colors in the Rainbow:")

## THE LOOP THROUGH THE LIST LOOP
#
#

time.sleep(1)

GameRunning = True

## NUMBER OF GUESSES START
#

## TIMER START
#

while GameRunning:
        
        guess = raw_input("\nGuess my favorite color in the rainbow (lowercase): ")

        if guess.lower() != favColor:
                print("Wrong!")
                ## RETURN NUMBER OF GUESSES SO FAR
                #
                #
                print("Please, try again :)")
                
        elif guess == favColor:
                print("\nYou guessed correctly!")
                ## RETURN FINAL NUMBER OF GUESSES
                #
                #

                ## RETURN TOTAL AMOUNT OF TIME TAKEN TO GUESS
                #
                #
                
                raw_input("\n\nPress the enter key to exit")
                GameRunning = False
                exit()
