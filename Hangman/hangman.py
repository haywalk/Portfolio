'''
A game of hangman
'''

import random

def getword():
	'''
	Choose a word
	'''
	global word
	global letters
	global corrguesses
	global wrong

	# Create lists of correct and incorrect letters
	corrguesses = list()
	wrong = list()

	# Get a random word from a list file
	word_file = "dict.txt"
	dictwords = open(word_file).read().splitlines()
	word = dictwords[random.randint(0, 99)].lower()

	# Add unique letters to a set
	letters = set()
	for i in word:
		letters.add(i)

def drawman(parts):
	'''
	Draws the appropriate number of body parts
	'''
	# Define the parts of the men
	man = ["___", "| |","| o", "|-|-", "|| |", "|", "----"]

	# Draw the appropriate number of parts of the man
	for i in range(parts):
		print(man[i])
	print()

def drawword(word, guesses, wrong):
	'''
	Draws guessed letters, empty spaces, and incorrect guesses
	'''
	# List of spaces to fill
	spaces = list()
	# For each letter in the word, either add a blank space or a guessed letter
	for i in word:
		if i in guesses:
			spaces.append(i)
		else:
			spaces.append("_")

	# Print out the spaces and incorrect guesses
	print(" ".join(spaces))
	print(" ".join(wrong))
	print()

def getguess():
	'''
	Gets the user's guess
	'''
	# Get the user's input
	guess = input("Letter? : ").lower()

	# Check if it is a valid letter
	if guess not in "abcdefghijklmnopqrstuvwxyz":
		print("Invalid guess.")
		getguess()
	# Check if it has already been guessed
	elif (guess in corrguesses) or (guess in wrong):
		print("You've already guessed that!")
		getguess()
	# Check if it is in the word
	elif guess in letters:
		corrguesses.append(guess)
	# If not, add to wrong guesses
	else:
		wrong.append(guess)

def checklose(num):
	'''
	Checks if the user has lost
	'''
	if num > 6:
		print(f"You lost; the word was '{word}.'")
		playagain()
 
def checkwin():
	'''
	Check if the player has won
	'''
	# Check if the number of correct guesses equals unique letters
	if len(letters) == len(corrguesses):
		print("Congratulations! You have won.")
		playagain()

def playagain():
	'''
	Ask the user to play again
	'''
	if input("Play again? Y/N: ").lower() == "y":
		print() # Draw a blank line
		gameloop() # Initialize the game loop
	else:
		quit()

def gameloop():
	'''
	The main game loop
	'''
	print("H A N G M A N\nHayden Walker, 5 Aug/19")
	getword()

	while True:
		drawman(len(wrong))
		drawword(word, corrguesses, wrong)
		checklose(len(wrong))
		checkwin()
		getguess()

gameloop() # Initialize the game loop
