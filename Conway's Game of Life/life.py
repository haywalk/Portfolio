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

# Initialize the pygame window
pygame.init()
win = pygame.display.set_mode((100, 100))
pygame.display.set_caption("Life")


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

chars = list()

def genchars():
	'''
	Randomly generate living/dead squares
	'''
	global chars
	for y in range(0, 100, 10):
		for x in range(0, 100, 10):
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
		if (not (spot % 10 == 0)) and (chars[spot - 1].living == True):
			neighbours += 1
		if (not (spot in (9, 19, 29, 39, 49, 59, 69, 79, 89, 99))) and (chars[spot + 1].living == True):
			neighbours += 1
		if (not (90 <= spot <= 99)) and (chars[spot + 10].living == True):
			neighbours += 1
		if (not(0 <= spot <= 9)) and (chars[spot - 10].living == True):
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

genchars() # Generate the initial characters

while True:
	'''
	The main loop
	'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()

	drawchars()
	checkneighbours()
	evolve()

	pygame.time.delay(1000) # One second per generation
