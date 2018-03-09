import random, time

# Starting with an empty list
colors = []

# Adding items to the list (in bulk)
colors.extend(('orange', 'red', 'blue', 'yellow', 'indigo', 'green', 'violet'))

# Uncomment the line below to test colors.extend() worked
#print(colors)

favColor = random.choice(colors)

print("Hi! My favorite color is found in the rainbow.")

time.sleep(1)

GameRunning = True

while GameRunning:
	guess = raw_input("\nGuess my favorite color in the rainbow (lowercase): ")

	if guess.lower() != favColor:
		print("Wrong!")
		print("Please, try again :)")
	elif guess == favColor:
		print("\nYou guessed correctly!")
		raw_input("\n\nPress the enter key to exit")
		GameRunning = False
		exit()
