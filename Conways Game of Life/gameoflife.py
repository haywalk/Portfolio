'''
Conway's Game of Life
Hayden Walker, 22 August 2019

1. Live cell < 2 neighbours         --> dies
2. Live cell with 2-3 neighbours    --> lives to next generation
3. Live cell > 3 neighbours         --> dies from overcrowding
4. Dead cell with 3 live neighbours --> Becomes live (reproduction)
'''
import pygame
import random
import math


class Space:
	'''
	A space, which can be either living or dead
	'''
	def __init__(self, living, x, y):
		self.living = living
		self.x = x
		self.y = y
		self.neighbours = 0

	def draw(self):
		if self.living:
			pygame.draw.rect(win, (255, 255, 0), (self.x, self.y, 10, 10))
		else:
			pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, 10, 10))

def startwin():
	'''
	Create the window based on specified size, and define the edges
	'''
	global redge
	global tedge
	global bedge
	global ledge
	global win

	# Use h/w to find # of creatures, # of rows/cols, and creatures per row
	creatures = (wh // 10) ** 2
	rowscols = int(math.sqrt(creatures))
	cperrow = wh // 10

	# Initialize the pygame window
	pygame.init()
	win = pygame.display.set_mode((wh, wh))
	pygame.display.set_caption("Life")

	# Define edges of screen
	redge = list(range(rowscols - 1, creatures, cperrow))
	ledge = list(range(0, creatures - cperrow - 1, cperrow))
	tedge = list(range(0, cperrow))
	bedge = list(range(creatures - cperrow - 1, creatures))

def genchars():
	'''
	Randomly generate living/dead squares
	'''
	global chars
	
	chars = list()

	for y in range(0, wh, 10):
		for x in range(0, wh, 10):
			chars.append(Space(random.randint(0, 1), x, y))

def drawchars():
	'''
	Draw all squares
	'''
	win.fill((255, 255, 255))
	for i in chars:
		i.draw()
	pygame.display.update()

def checkneighbours():
	'''
	Check how many living neighbours a square has
	'''
	for i in chars:
		neighbours = 0
		spot = chars.index(i)
		# To the left
		if (not (spot in ledge)) and (chars[spot - 1].living):
			neighbours += 1
		# To the right
		if (not (spot in redge)) and (chars[spot + 1].living):
			neighbours += 1
		# Below
		if (not (spot in bedge)) and (chars[spot + (wh // 10)].living):
			neighbours += 1
		# Above
		if (not(spot in tedge)) and (chars[spot - (wh // 10)].living):
			neighbours += 1
		# Diag. upper left
		if (not (spot in tedge)) and (not (spot in ledge)) and (chars[spot - ((wh // 10) + 1)].living):
			neighbours += 1
		# Diag. bottom right
		if (not (spot in bedge)) and (not (spot in redge)) and (chars[spot + ((wh // 10) + 1)].living):
			neighbours += 1
		# Diag. upper right
		if (not (spot in tedge)) and (not (spot in redge)) and (chars[spot - ((wh // 10) - 1)].living):
			neighbours += 1
		# Diag. bottom left
		if (not (spot in bedge)) and (not (spot in ledge)) and (chars[spot + ((wh // 10) - 1)].living):
			neighbours += 1

		i.neighbours = neighbours

def evolve():
	'''
	Either kill or generate living squares based on neighbours
	'''
	for i in chars:
		if i.living:
			if (i.neighbours < 2) or (i.neighbours > 3):
				i.living = False
		else:
			if i.neighbours == 3:
				i.living = True

def mainloop():
	'''
	The main loop
	'''
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

		drawchars()
		checkneighbours()
		evolve()

		pygame.time.delay(100) # Time between generations

wh = 500 # Window width and height
startwin() # Initiate the window
genchars() # Generate the initial characters
mainloop() # Start the game loop
