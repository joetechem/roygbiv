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
