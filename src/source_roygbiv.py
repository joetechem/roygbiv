import random

colors = ['orange', 'red', 'blue', 'yellow', 'indigo', 'green', 'violet']

favColor = random.choice(colors)

print("Hi! My favorite color is found in the rainbow.")

GameRunning = True

while GameRunning:
	guess = raw_input("\nGuess my favorite color: ")

	if guess != favColor:
		print("Wrong!")
		print("Please, try again :)")
	elif guess == favColor:
		print("\nYou guessed correctly!")
		raw_input("\n\nPress the enter key to exit")
		GameRunning = False
		exit()
