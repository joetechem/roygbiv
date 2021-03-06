# Adding a score feature,
        # similar to golf, the lower a user's score, the better
        # (depending on how you decide to play)

import random, time

colors = ['orange', 'red', 'blue', 'yellow', 'indigo', 'green', 'violet']

favColor = random.choice(colors)

print("Hi! My favorite color is found in the rainbow." +
      "\n\n" +
      "Colors in the Rainbow:")

for color in colors:
        print(color.title())

time.sleep(1)

GameRunning = True
numberOfGuesses = 0

while GameRunning:
	guess = raw_input("\nGuess my favorite color in the rainbow (lowercase): ")

	if guess.lower() != favColor:
		print("Wrong!")
		numberOfGuesses += 1
		print("Amount of guesses so far: " + str(numberOfGuesses))
		print("Please, try again :)")
	elif guess == favColor:
		print("\nYou guessed correctly!")
		print("Total number of guesses: " + str(numberOfGuesses))
		raw_input("\n\nPress the enter key to exit")
		GameRunning = False
		exit()
