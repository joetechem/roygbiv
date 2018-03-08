# adding comments to guide students

import random, time

colors = ['orange', 'red', 'blue', 'yellow', 'indigo', 'green', 'violet']

favColor = random.choice(colors)

print("Hi! My favorite color is found in the rainbow." +
      "\n\n" +
      "Colors in the Rainbow:")

## THE LOOP THROUGH THE LIST LOOP
for color in colors:
        print(color.title())

time.sleep(1)

GameRunning = True

## NUMBER OF GUESSES START
numberOfGuesses = 0

## TIMER START
start = time.clock()

while GameRunning:
        
        guess = raw_input("\nGuess my favorite color in the rainbow (lowercase): ")

        if guess.lower() != favColor:
                print("Wrong!")
                ## RETURN NUMBER OF GUESSES SO FAR
                numberOfGuesses += 1
                print("Amount of guesses so far: " + str(numberOfGuesses))
                print("Please, try again :)")
                
        elif guess == favColor:
                print("\nYou guessed correctly!")
                ## RETURN FINAL NUMBER OF GUESSES
                numberOfGuesses += 1
                print("Total number of guesses: " + str(numberOfGuesses))

                ## RETURN TOTAL AMOUNT OF TIME TAKEN TO GUESS
                time_elapsed = time.clock() - start
                print("Total time: " + str(time_elapsed) + " seconds")
                
                raw_input("\n\nPress the enter key to exit")
                GameRunning = False
                exit()
