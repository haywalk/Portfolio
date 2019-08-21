# Minefield by Hayden Walker
# V2, 20 July 2019
# Pylint 7.5/10

from os import system, name # For screen clearing
import random # For mine generation

def clear():
	'''
	Clear the screen.
	'''
	if name == "nt": # If on windows, command CLS
		_ = system("cls")
	else: # If on *nix, command clear
		_ = system("clear")

def getdiff():
	'''
	Select a random amount of mines, and place them in unique random spots on the board
	'''
	global mine
	mine = list() # A list of spots that are mines
	numofmines = random.randint(1, 6)
	x = 0
	while x < numofmines:
		spot = random.randint(1, 24)
		# Only add the mind if it is in a unique place
		if spot in mine:
			continue
		else:
			mine.append(spot)
			x += 1

def drawboard():
	'''
	Draw the playing board.
	'''
	clear()
	print("M I N E F I E L D\nBy: Hayden Walker\n\n# = Ground; C = Cleared;\n$ = Beside Mine; * = Mine.\n")
	print(f"20-24   {spaces[20]} {spaces[21]} {spaces[22]} {spaces[23]} {spaces[24]}")
	print(f"15-19   {spaces[15]} {spaces[16]} {spaces[17]} {spaces[18]} {spaces[19]}")
	print(f"10-14   {spaces[10]} {spaces[11]} {spaces[12]} {spaces[13]} {spaces[14]}")
	print(f"05-09   {spaces[5]} {spaces[6]} {spaces[7]} {spaces[8]} {spaces[9]}")
	print(f"00-04   {spaces[0]} {spaces[1]} {spaces[2]} {spaces[3]} {spaces[4]}\n")

def getinput():
	'''
	Gets the user's input and checks validity.
	'''
	while True:
		try:
			playat = int(input(f"There are {len(mine)} mines. Choose a square to examine. 0-24: "))
		except:
			print("ERR Invalid number")
			continue
		else:
			if playat > 24:
				print("ERR Number too high")
				continue
			elif (spaces[playat] == "C") or\
				(spaces[playat] == "$"):
				print("ERR Space occupied")
				continue
			else:
				break
	return playat

def checkinput(playat):
	'''
	The logic that determines whether or not a spot is on a mine, next to a mine, or clear.
	'''
	# Check if the spot is a mine
	if playat in mine:
		# Display all mines
		for i in mine:
			spaces[i] = "*"
		drawboard()
		print(f"You uncovered a mine, and were killed. The mines were at:\n{sorted(mine)}")
		again()
	# Check if the spot is next to a mine
	elif (0 < playat < 4) or \
		(5 < playat < 9) or \
		(10 < playat < 14) or \
		(15 < playat < 19) or \
		(20 < playat < 24):
			if (playat + 1 in mine) or \
				(playat - 1 in mine) or \
				(playat + 5 in mine) or\
				(playat - 5 in mine):
				spaces[playat] = "$"
				cleared.append(1)
			else:
				spaces[playat] = "C"
				cleared.append(1)
	elif playat in (0, 5, 10, 15, 20):
		if (playat + 1 in mine) or \
			(playat + 5 in mine) or \
			(playat - 5 in mine):
			spaces[playat] = "$"
			cleared.append(1)
		else:
			spaces[playat] = "C"
			cleared.append(1)
	elif playat in (4, 9, 14, 19, 24):
		if (playat - 1 in mine) or \
			(playat + 5 in mine) or \
			(playat - 5 in mine):
			spaces[playat] = "$"
			cleared.append(1)
		else:
			spaces[playat] = "C"
			cleared.append(1)
	else:
		spaces[playat] = "C"
		cleared.append += 1

def checkclear():
	'''
	Check if the board is cleared.
	'''
	if sum(cleared) == 25 - len(mine):
		# Display all mines
		for i in mine:
			spaces[i] = "*"
		drawboard()
		print("\nBoard cleared, congratulations!")
		again()
	else:
		return 0

def again():
	'''
	Ask the user to play again.
	'''
	if input("\nPlay again? Y/N: ").lower() == "y":
		gameloop()
	else:
		quit()

def gameloop():
	'''
	The main game loop
	'''
	global spaces
	global cleared

	spaces = ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", ] # The spaces on the board
	cleared = list() # A tally of cleared spaces

	clear()
	getdiff()

	while True:
		drawboard()
		checkinput(getinput())
		checkclear()

gameloop()
